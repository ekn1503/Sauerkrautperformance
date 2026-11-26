#!/usr/bin/env python3
"""OKF v0.2 conformance + health check for ./wiki. Usage: python docs/llm-wiki/tools/lint.py [bundle_dir]"""
import posixpath
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RESERVED = {"index.md", "log.md"}
FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
LINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+?)(?:#[^)]*)?\)")


def parse_fm(text):
    m = FM.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        k = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if k:
            fm[k.group(1)] = k.group(2).strip()
    return fm


SENSITIVE = [
    (re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b"), "IP address"),
    (re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I), "GUID"),
    (re.compile(r"(?i)\b(?:password|passwd|secret|api[_-]?key|token)\s*[:=]\s*\S{6,}"), "credential"),
]


def check_footnotes(rel, text, errors):
    """Every [^id] ref needs a sources[].id in the frontmatter AND a [^id]: definition."""
    m = FM.match(text)
    fm_text = m.group(1) if m else ""
    body = text[m.end():] if m else text
    declared = set(re.findall(r"\bid:\s*([\w-]+)", fm_text))
    defined = set(re.findall(r"^\[\^([\w-]+)\]:", body, re.M))
    used = set(re.findall(r"\[\^([\w-]+)\](?!:)", body))
    for fid in sorted(used - declared):
        errors.append(f"{rel}: footnote [^{fid}] not declared in sources")
    for fid in sorted(used - defined):
        errors.append(f"{rel}: footnote [^{fid}] has no definition")


def resolve(rel_file, target):
    if target.startswith("/"):
        return posixpath.normpath(target.lstrip("/"))
    return posixpath.normpath(posixpath.join(posixpath.dirname(rel_file), target))


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "wiki")
    errors, warnings = [], []
    concepts = {}
    others = {}
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8")
        fm = parse_fm(text)
        if p.name in RESERVED:
            others[rel] = text
            if p.name == "index.md" and fm is not None and rel != "index.md":
                errors.append(f"{rel}: non-root index.md must not have frontmatter")
            if p.name == "log.md" and not re.search(r"^## \d{4}-\d{2}-\d{2}$", text, re.M):
                warnings.append(f"{rel}: no ISO date headings")
            continue
        if fm is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        if not fm.get("type"):
            errors.append(f"{rel}: missing/empty 'type'")
        concepts[rel] = (fm, text)

    inbound = {c: 0 for c in concepts}
    now = datetime.now(timezone.utc)
    pages = {**{r: t for r, (_, t) in concepts.items()}, **others}
    for rel, text in pages.items():
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target) or target.endswith("/"):
                continue
            t = resolve(rel, target)
            if t in inbound:
                if t != rel:
                    inbound[t] += 1
            elif not (root / t).exists():
                warnings.append(f"{rel}: broken link -> {target}")

    for rel, (fm, text) in concepts.items():
        check_footnotes(rel, text, errors)
        for pat, what in SENSITIVE:
            if pat.search(text):
                warnings.append(f"{rel}: possible {what} (summarise abstractly, never copy)")
        if "description" not in fm:
            warnings.append(f"{rel}: no description")
        if fm.get("status") == "deprecated":
            warnings.append(f"{rel}: deprecated")
        sa = fm.get("stale_after")
        if sa:
            try:
                if now >= datetime.fromisoformat(sa.replace("Z", "+00:00")):
                    warnings.append(f"{rel}: stale (stale_after {sa})")
            except ValueError:
                errors.append(f"{rel}: bad stale_after '{sa}'")
        if inbound[rel] == 0:
            warnings.append(f"{rel}: orphan (no inbound links)")

    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("WARN   ", w)
    print(f"{len(concepts)} concepts, {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
