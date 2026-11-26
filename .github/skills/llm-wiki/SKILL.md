---
name: llm-wiki
description: "Operate this repository as an LLM-maintained, compounding knowledge base (Karpathy's LLM Wiki pattern): ingest raw sources into the OKF wiki, answer questions from the wiki and file good answers back, and lint the wiki's health. Use for 'ingest raw/...', 'what do we know about ...', 'lint the wiki', 'update the wiki', 'file this answer', 'was wissen wir über ...'."
metadata:
  based_on: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  author_of_pattern: Andrej Karpathy
  adapted_by: copilot
  date: 2026-11-26
---

# LLM Wiki

> **Base path:** this repository is a monorepo. The wiki lives in `docs/llm-wiki/`.
> Every path below (`wiki/`, `raw/`, `memory/`, `tools/`, `AGENTS.md`) is relative to that folder,
> so run `cd docs/llm-wiki` first (or prefix the paths).

Based on Andrej Karpathy's "LLM Wiki" idea file
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
The concrete rules for *this* repository (layout, OKF frontmatter, index and
log formats, page types) live in `AGENTS.md`; follow them exactly. This skill
explains the **why** and the **working loop**, so you make the many small
decisions the way the pattern intends. For OKF format details use the
`okf-open-knowledge-format` skill.

## The idea in one paragraph

Plain RAG re-discovers knowledge from scratch on every question; nothing
accumulates. Here, the LLM **compiles** sources once into a persistent,
interlinked wiki and **keeps it current**. Each new source updates entity
and concept pages, sharpens the synthesis, and flags where it contradicts
older claims. The wiki is a compounding artifact: cross-references,
contradictions and synthesis are already there when a question comes.
The human curates sources, asks questions and decides what matters; the
LLM does the reading-into-structure, cross-referencing, filing and
bookkeeping, which is the part humans abandon wikis over.

## Three layers (and who owns them)

| Layer | Here | Owner | Rule |
|-------|------|-------|------|
| Raw sources | `raw/` | human (+ raw-interviewer for new captures) | Immutable source of truth. Read, never modify. |
| Wiki | `wiki/` (OKF v0.2 bundle) | LLM | You write and maintain all of it. |
| Schema | `AGENTS.md` (+ `memory/`) | human and LLM together | Co-evolve it when a convention proves useful; record the decision in `memory/decisions.md`. |

## Operations

### Ingest: compile one source into the wiki

1. Read the raw source fully (for HTML/PDF extract the text; view images separately if they matter).
2. **Discuss key takeaways with the human** briefly: what's new, what's surprising, what to emphasize. Prefer one source at a time with the human involved; batch only if they ask.
3. Write the source summary page, then update or create every touched concept/entity page (a single source often touches 5-15 pages). Integrate, don't append: revise summaries so they reflect everything known.
4. **Flag contradictions explicitly** on the affected pages (old claim vs. new claim, both attributed). Don't silently overwrite.
5. Update indexes and append a log entry (formats in `AGENTS.md`).
6. Run `python tools/lint.py`.

### Query: answer from the wiki, then compound

1. Read `wiki/index.md` first, drill into folder indexes and pages. At this scale the index replaces vector search.
2. Answer with links/citations to the pages used. Go to `raw/` only to check details; say when the wiki lacks the answer instead of guessing.
3. Pick the answer form that fits: prose, table, comparison, checklist, diagram.
4. **File good answers back.** If the answer is a reusable comparison, analysis or newly discovered connection, offer to save it as a Synthesis page (and log it), so explorations compound like sources do. If the question revealed a gap, add it to `memory/todo.md` or propose an interview (raw-interviewer).

### Lint: keep the wiki healthy

Run `python tools/lint.py`, then check by judgment:

- contradictions between pages; claims superseded by newer sources
- stale pages (`stale_after` passed)
- orphan pages (no inbound links); hub concepts that deserve a page but lack one
- missing cross-references
- data gaps: suggest concrete new questions to investigate, sources to look for, or topics to interview the human about

Fix what's safe, report the rest, log the pass.

## Habits that make it work

- **Index first, always.** It is the map; keep every entry's one-line description accurate.
- **Log is the timeline.** Consistent entry prefixes make it greppable and tell the next session what happened recently.
- **Small, many, linked pages** beat a few long ones. Link generously; the prose around a link says what the relationship is.
- **Provenance on every claim** (footnotes keyed to `sources[].id`). Trust is visible: new pages start `status: draft`; only the human verifies.
- **Stay in the loop with the human** on ingests: they read the result and steer emphasis.
- **Grow tooling only when needed** (e.g. a local search script once the index stops being enough).

## Not this skill's job

- Capturing new knowledge from the human by interview: use the `raw-interviewer` agent / `knowledge-interview` skill. It writes new files in `raw/`; this skill then ingests them.
