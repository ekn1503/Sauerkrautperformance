---
type: Concept
title: "Documentation structure"
description: "The three documentation sets in the global docs/ folder: internal technical docs, end-user docs served on the Raspberry Pi, and this LLM wiki."
tags: [docs, mkdocs, convention]
resource: /docs/README.md
generated: { by: copilot/claude-sonnet-5.5, at: 2026-11-26T09:30:00+01:00 }
status: draft
sources:
  - { id: src-kickoff, resource: /sources/project-kickoff-2026-11-26.md, title: "Project kickoff (2026-11-26)" }
---

# Decision (by the human)

Documentation lives in the global repo folder `docs/`, split into an internal technical set and an end-user set; the end-user documentation is hosted through this repo on the Raspberry Pi.[^src-kickoff]

# Implementation

| Set | Folder | Notes |
|-----|--------|-------|
| Technical | `docs/technical/<project>/` | one folder per subproject, each with `vision/` (product vision and goals) and `architecture/` (arc42 sections in `arc42/`, ADRs in `adr/`); MkDocs Material |
| End user | `docs/user/` | MkDocs Material; `docs/Dockerfile.user` builds a static site served by nginx; CI builds an amd64 + arm64 image |
| LLM wiki | `docs/llm-wiki/` | OKF v0.2; knowledge that is settled gets promoted to the two sets above |

Configs: `docs/mkdocs.user.yml`, `docs/mkdocs.technical.yml`; both build with `--strict` in CI (`.github/workflows/docs.yml`). Details: `docs/README.md`. Per-project docs go into subfolders of each set.

[^src-kickoff]: Kickoff brief by the human, [Project kickoff](/sources/project-kickoff-2026-11-26.md).
