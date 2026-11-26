---
type: Project
title: "Dynamometer test bench (moped)"
description: "Generic measurement station for mopeds: ESP32/Arduino controls the hardware, a Raspberry Pi collects data and shows a Svelte GUI, a Python backend stores and evaluates measurements; bench type still open."
tags: [dynamometer, test-bench, hardware, requirements]
generated: { by: copilot/claude-sonnet-5.5, at: 2026-11-26T09:30:00+01:00 }
status: draft
sources:
  - { id: src-kickoff, resource: /sources/project-kickoff-2026-11-26.md, title: "Project kickoff (2026-11-26)" }
---

# Goal

Measure the performance of mopeds on a test bench ("Prüfstand"): record signals, process them, calculate performance values and keep the data long term.[^src-kickoff]

# Bench type is open

Initially thought of as an inertia test bench (Trägheitsprüfstand); the human then stated it may also be a roller test bench (Rollenprüfstand) or any dynamometer-style bench, so the design must stay **generic**.[^src-kickoff] Consequences for planning (agent proposal, not a decision): keep bench-specific physics behind a generic measurement abstraction; do not name folders, APIs or tables after one bench type.

# Known roles (not an architecture)

| Role | Said by the human |
|------|-------------------|
| Arduino / ESP32 | controls the physical hardware[^src-kickoff] |
| Raspberry Pi | collects the data from the microcontroller and hosts the GUI; also hosts the end-user docs[^src-kickoff] |
| Svelte UI | the GUI[^src-kickoff] |
| Python backend | stores measurement data long term, processes signals, calculates performances[^src-kickoff] |

How these are split into processes, protocols and deployables is **undecided**.

# Requirements so far

* [Simulation mode](/concepts/simulation-mode.md): develop and test without hardware.
* End-user documentation served from the Pi: [Documentation structure](/concepts/documentation-structure.md).

# Open questions

Bench type(s), sensors and boards, roller geometry/inertia, throttle control, safety features, correction model for results, software architecture. Tracked in `memory/todo.md`; an interview is the next step.

[^src-kickoff]: Kickoff brief by the human, [Project kickoff](/sources/project-kickoff-2026-11-26.md).
