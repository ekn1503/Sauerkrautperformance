---
type: Source
title: "Project kickoff (2026-11-26)"
description: "The human's initial brief for the Sauerkrautperformance monorepo and its first project, a generic moped dynamometer test bench."
tags: [kickoff, monorepo, dynamometer]
resource: /raw/sauerkrautperformance/2026-11-26-project-kickoff.md
generated: { by: copilot/claude-sonnet-5.5, at: 2026-11-26T09:30:00+01:00 }
status: draft
---

# Summary

Raw note: `raw/sauerkrautperformance/2026-11-26-project-kickoff.md` (the human's own statements, captured from the setup session).

Key claims (all by human:ekneissl):

* The repo is a monorepo for several hobby subprojects; planned technology: Copilot agents, CI/CD, Python, TypeScript, C++ for Arduino, Docker.
* First project: a moped test bench, deliberately generic (inertia, roller or dynamometer bench).
* Arduino/ESP32 controls the hardware; a Raspberry Pi collects data and runs the Svelte GUI; a Python backend stores, processes and evaluates measurements.
* A simulation is wanted so the hardware is not needed for development.
* Architecture undecided; documentation split into technical and end-user sets, the latter served from the Pi.

Pages derived from it: [Sauerkrautperformance monorepo](/entities/sauerkrautperformance.md), [Dynamometer test bench](/entities/dynamometer-test-bench.md), [Simulation mode](/concepts/simulation-mode.md), [Documentation structure](/concepts/documentation-structure.md), [Monorepo conventions](/concepts/monorepo-conventions.md).
