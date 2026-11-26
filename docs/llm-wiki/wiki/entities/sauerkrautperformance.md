---
type: Project
title: "Sauerkrautperformance monorepo"
description: "The hobby monorepo that hosts several subprojects, starting with a generic moped dynamometer test bench."
tags: [monorepo, project]
resource: /
generated: { by: copilot/claude-sonnet-5.5, at: 2026-11-26T09:30:00+01:00 }
status: draft
sources:
  - { id: src-kickoff, resource: /sources/project-kickoff-2026-11-26.md, title: "Project kickoff (2026-11-26)" }
---

# What it is

A monorepo for hobby projects of human:ekneissl. It is planned to span several subprojects and several technology families: Python (Litestar, Polars, DuckDB), TypeScript (Svelte, Vite), C++ for Arduino/ESP32, Docker deployment, Copilot agents and CI/CD.[^src-kickoff]

# Projects

| Project | State |
|---------|-------|
| [Dynamometer test bench](/entities/dynamometer-test-bench.md) | planning; architecture undecided |

# Conventions

See [Monorepo conventions](/concepts/monorepo-conventions.md) and [Documentation structure](/concepts/documentation-structure.md). Agent rules: root `AGENTS.md`.

[^src-kickoff]: Kickoff brief by the human, [Project kickoff](/sources/project-kickoff-2026-11-26.md).
