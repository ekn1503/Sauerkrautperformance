---
type: Concept
title: "Simulation mode"
description: "Requirement that every test bench can be developed and tested without hardware by a simulation that behaves like the real device."
tags: [simulation, testing, requirement]
generated: { by: copilot/claude-sonnet-5.5, at: 2026-11-26T09:30:00+01:00 }
status: draft
sources:
  - { id: src-kickoff, resource: /sources/project-kickoff-2026-11-26.md, title: "Project kickoff (2026-11-26)" }
---

# Requirement

The human wants a simulation of the measurement station so that the hardware is not needed during development.[^src-kickoff] This applies to the [Dynamometer test bench](/entities/dynamometer-test-bench.md) and, as a rule, to future benches.

# Design guidance (agent proposal, not decided)

* The simulation should enter the system at the same boundary as the real device (the same protocol between microcontroller and Pi), so everything downstream (processing, storage, GUI) is exercised unchanged. Where that boundary is depends on the undecided architecture.
* Deterministic by default (seeded noise) so tests are reproducible; a real-time mode for the GUI.
* Bench-type specifics (inertia, roller, brake) are parameters of the simulation, matching the generic bench abstraction.
* A first backend scaffold with such a simulator was written and deliberately discarded on 2026-11-26 because the architecture is open (see `memory/decisions.md`).

[^src-kickoff]: Kickoff brief by the human, [Project kickoff](/sources/project-kickoff-2026-11-26.md).
