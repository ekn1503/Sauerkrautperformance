#!/usr/bin/env python3
"""Download a web page or file into raw/ as a NEW immutable source file.

Usage: python tools/fetch_raw.py <url> [--topic TOPIC] [--author human:ekneissl]

HTML is saved as markdown (frontmatter + converted text) plus the original
.html; PDFs/other binaries are saved as-is with a sidecar .md metadata file.
Stdlib only. Existing files are never overwritten (a -2, -3 suffix is added).
"""
import argparse
import hashlib
import ipaddress
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
MAX_BYTES = 20 * 1024 * 1024
TIMEOUT = 30
UA = "Mozilla/5.0 (compatible; llm-wiki-fetch-raw/1.0; +local knowledge base)"


def check_host(host):
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror as e:
        raise SystemExit(f"error: cannot resolve {host}: {e}")
    for info in infos:
        ip = ipaddress.ip_address(info[4][0].split("%")[0])
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast or ip.is_unspecified):
            raise SystemExit(f"error: refusing local/private address {ip} for {host}")


def check_url(url):
    p = urllib.parse.urlparse(url)
    if p.scheme not in ("http", "https") or not p.hostname:
        raise SystemExit("error: only http(s) URLs are allowed")
    check_host(p.hostname)


class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class TextExtractor(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "head", "nav", "footer", "form"}
    BLOCK = {"p", "div", "section", "article", "br", "tr", "ul", "ol", "table",
             "blockquote", "pre", "main", "header"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.title, self.author = [], "", ""
        self._skip, self._in_title, self._href = 0, False, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "meta" and (a.get("name") or "").lower() == "author":
            self.author = a.get("content") or self.author
        if tag in self.SKIP:
            self._skip += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n* ")
        elif tag == "a" and a.get("href"):
            self._href = a["href"]
            self.out.append("[")
        elif tag in self.BLOCK:
            self.out.append("\n\n")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in self.SKIP and self._skip:
            self._skip -= 1
        elif tag == "a" and self._href:
            self.out.append(f"]({self._href})")
            self._href = None
        elif tag in self.BLOCK or tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append("\n\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if not self._skip:
            self.out.append(re.sub(r"\s+", " ", data))

    def text(self):
        t = "".join(self.out)
        t = re.sub(r"[ \t]+\n", "\n", t)
        return re.sub(r"\n{3,}", "\n\n", t).strip()


def slugify(s, default="page"):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60].strip("-") or default


def free_path(base: Path):
    p, n = base, 2
    while p.exists():
        p = base.with_name(f"{base.stem}-{n}{base.suffix}")
        n += 1
    return p


def yq(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("url")
    ap.add_argument("--topic", default="web")
    ap.add_argument("--author", default="human:ekneissl")
    args = ap.parse_args()

    check_url(args.url)
    topic = slugify(args.topic, "web")
    req = urllib.request.Request(args.url, headers={"User-Agent": UA, "Accept": "*/*"})
    opener = urllib.request.build_opener(SafeRedirect)
    try:
        with opener.open(req, timeout=TIMEOUT) as r:
            data = r.read(MAX_BYTES + 1)
            ctype = (r.headers.get_content_type() or "").lower()
            charset = r.headers.get_content_charset() or "utf-8"
            final_url = r.geturl()
    except urllib.error.HTTPError as e:
        hint = " (login required? ask the user to paste the content or save the file into raw/ manually)" if e.code in (401, 403) else ""
        raise SystemExit(f"error: HTTP {e.code} for {args.url}{hint}")
    except urllib.error.URLError as e:
        raise SystemExit(f"error: {e.reason}")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"error: response larger than {MAX_BYTES // 1024 // 1024} MB")

    now = datetime.now().astimezone()
    date = now.strftime("%Y-%m-%d")
    digest = "sha256:" + hashlib.sha256(data).hexdigest()
    parsed = urllib.parse.urlparse(final_url)
    folder = RAW / topic
    folder.mkdir(parents=True, exist_ok=True)

    meta = {"source_url": args.url, "fetched_at": now.isoformat(timespec="seconds"),
            "author": args.author, "topic": topic, "content_hash": digest}

    def front(extra):
        lines = ["---"] + [f"{k}: {yq(v) if k in ('title', 'source_url') else v}"
                           for k, v in {**extra, **meta}.items()] + ["---", ""]
        return "\n".join(lines)

    if ctype in ("text/html", "application/xhtml+xml"):
        html = data.decode(charset, errors="replace")
        ex = TextExtractor()
        ex.feed(html)
        title = re.sub(r"\s+", " ", ex.title).strip() or parsed.netloc
        base = free_path(folder / f"{date}-{slugify(title or parsed.path)}.md")
        extra = {"type": "Web Page", "title": title}
        if ex.author:
            extra["page_author"] = ex.author
        base.write_text(front(extra) + f"\n# {title}\n\n{ex.text()}\n", encoding="utf-8", newline="\n")
        base.with_suffix(".html").write_bytes(data) if not base.with_suffix(".html").exists() else None
        print(base)
        return

    if ctype.startswith("text/") or ctype in ("application/json", "application/xml"):
        ext = {"text/plain": ".txt", "text/markdown": ".md", "application/json": ".json",
               "text/csv": ".csv"}.get(ctype, ".txt")
        stem = slugify(Path(parsed.path).stem or parsed.netloc)
        path = free_path(folder / f"{date}-{stem}{ext}")
        path.write_bytes(data)
        side = path.with_name(path.stem + "-meta.md")
        side.write_text(front({"type": "Web File", "title": path.name, "file": path.name}), encoding="utf-8", newline="\n")
        print(path)
        return

    ext = {"application/pdf": ".pdf"}.get(ctype) or Path(parsed.path).suffix or ".bin"
    stem = slugify(Path(parsed.path).stem or parsed.netloc)
    path = free_path(folder / f"{date}-{stem}{ext}")
    path.write_bytes(data)
    side = path.with_name(path.stem + "-meta.md")
    side.write_text(front({"type": "Web File", "title": path.name, "file": path.name,
                           "content_type": ctype}), encoding="utf-8", newline="\n")
    print(path)


if __name__ == "__main__":
    sys.exit(main())
