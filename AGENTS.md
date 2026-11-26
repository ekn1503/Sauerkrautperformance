# AGENTS.md (Sauerkrautperformance monorepo)

Hobby monorepo. First project: a **dynamometer test bench** ("Prüfstand") for mopeds. The bench type is deliberately generic and still open: inertia dynamometer (Trägheitsprüfstand), roller dynamometer (Rollenprüfstand), possibly with a brake/load unit. The software architecture is **not decided yet**; do not invent one or hard-code one bench type. Planned technology families: Python (Litestar, Polars, DuckDB), TypeScript (Svelte, Vite), C++ for Arduino/ESP32, Docker for deployment, GitHub Actions CI/CD.

## Read first

1. The LLM wiki in [`docs/llm-wiki/`](docs/llm-wiki/): the project's knowledge (requirements, hardware, decisions, physics). Schema and rules: [`docs/llm-wiki/AGENTS.md`](docs/llm-wiki/AGENTS.md). Start at `docs/llm-wiki/wiki/index.md` and `docs/llm-wiki/memory/`.
2. Before building something, ask the wiki (agent `wiki-retriever` / `wiki-unicorn`). If the wiki lacks the answer, say so and interview the human instead of guessing.

## Layout

```
apps/<project>/...   one folder per project (created when the architecture is decided)
packages/            shared libraries (later)
docs/technical/      internal technical docs, one folder per subproject: <project>/vision/ (product vision, goals) and <project>/architecture/ (arc42, adr/); MkDocs
docs/user/           end-user docs (MkDocs), served on the Raspberry Pi
docs/llm-wiki/       OKF knowledge base (raw/, wiki/, memory/, tools/)
.github/             agents, skills, workflows, templates (must be at the repo root)
```

## Conventions

- Lint/format: ruff (Python, `ruff.toml`), prettier (TS/Svelte), clang-format (C++), markdownlint, hadolint; all wired in `.pre-commit-config.yaml` and `.github/workflows/lint.yml`. Run `pre-commit run --all-files`.
- Python: 3.11+, type hints, uv for environments. TypeScript: strict mode. Keep each project self-contained with its own manifest.
- A test bench must be developable without hardware: provide a simulation mode that speaks the same protocol as the real device. Keep bench-specific physics (inertia, roller, brake) behind a generic bench/measurement abstraction so new bench types can be added.
- Never commit secrets (`.env`), measurement dumps (`*.duckdb`, `*.parquet`) or build output.
- When a decision, protocol, formula or architecture changes, update the wiki in the same PR (see the PR template). Wiki content is English; run `python docs/llm-wiki/tools/lint.py`.
- Commit trailer for agent commits: `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`.

## Agents

`wiki-unicorn` (all-in-one), `wiki-retriever` (read-only Q&A), `wiki-curator` (ingest/lint), `raw-interviewer` (capture knowledge) in `.github/agents/`. Guide: [`docs/llm-wiki/GUIDE.md`](docs/llm-wiki/GUIDE.md).
