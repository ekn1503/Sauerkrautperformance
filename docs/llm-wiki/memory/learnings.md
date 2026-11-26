# Learnings

Carried over from the author's earlier wiki (generic ones only):

- Footnotes: every `[^id]` needs a `sources[].id` AND a `[^id]:` definition. lint.py now checks it; write the definition block first.
- Windows: PowerShell 5 `Set-Content -Encoding utf8` writes a BOM -> lint says "missing YAML frontmatter". Use create/edit tools. CRLF files can defeat multi-line matches. File-creation tools fail if the parent folder is missing.
- `edit` anchors that appear several times (headings, log entries) hit the wrong place: view the result after editing log.md / syntheses.
- A non-root `index.md` with frontmatter is an error (OKF section 8).
- Ingest: always diff a new source against existing pages (earlier pages can be partly wrong) and add a dated correction note. Qualify IDs by catalogue (same ID, different meaning). Check file sizes: "empty" files can be image stubs.
- Config/infra material embeds IPs, tokens, hostnames: summarise abstractly; lint.py warns on IP/GUID/credential patterns.
- Document-type ingests: PPTX via zipfile+regex over `ppt/slides/slideN.xml`; PDF/xlsx/msg via pypdf/openpyxl/extract-msg. Diagram PNGs: view, describe in prose.
- Staleness signals (update dates) are worth quoting on derived pages. Product choices under discussion are "exploration, not a decision": say so in descriptions and tags.
- Copilot CLI only discovers `.github/agents|skills` at a git repo root. Here the repo root is the monorepo root, so no sync workaround is needed.
