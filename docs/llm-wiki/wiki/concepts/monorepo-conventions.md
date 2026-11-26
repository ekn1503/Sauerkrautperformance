---
type: Concept
title: "Monorepo conventions"
description: "Tooling and lint conventions for the Sauerkrautperformance monorepo (no application architecture decided yet)."
tags: [monorepo, lint, ci, convention]
resource: /AGENTS.md
generated: { by: copilot/claude-sonnet-5.5, at: 2026-11-26T09:30:00+01:00 }
status: draft
sources:
  - { id: src-kickoff, resource: /sources/project-kickoff-2026-11-26.md, title: "Project kickoff (2026-11-26)" }
---

# Scope

The human asked for lint files and similar repo tooling only; the architecture is undecided.[^src-kickoff] What exists:

| Concern | File |
|---------|------|
| Shared editor/line endings | `.editorconfig`, `.gitattributes` |
| Python | `ruff.toml` (lint + format) |
| TypeScript/Svelte | `.prettierrc.json`, `.prettierignore` (eslint to be added with the first TS project) |
| C++ (Arduino/ESP32) | `.clang-format` |
| Markdown | `.markdownlint-cli2.jsonc` |
| Docker | hadolint via pre-commit |
| Hooks | `.pre-commit-config.yaml` (hygiene, ruff, clang-format, hadolint, markdownlint, wiki lint) |
| CI | `.github/workflows/lint.yml`, `docs.yml`; add per-project workflows with path filters when projects exist |
| Dependencies | `.github/dependabot.yml` (extend per project) |
| Agents | `.github/agents`, `.github/skills`, root `AGENTS.md`, `.github/copilot-instructions.md` |

# Not yet decided

Project layout beyond `apps/<project>` / `packages/`, build tooling per language, test frameworks, release process, deployment topology.

[^src-kickoff]: Kickoff brief by the human, [Project kickoff](/sources/project-kickoff-2026-11-26.md).
