---
type: Interview
title: "Project kickoff: Sauerkrautperformance monorepo and moped dynamometer test bench"
date: 2026-11-26T09:04:00+01:00
author: human:ekneissl
interviewer: copilot/claude-sonnet-5.5
topic: sauerkrautperformance
language: en
tags: [kickoff, monorepo, dynamometer, test-bench, requirements]
---

# Project kickoff: Sauerkrautperformance monorepo and moped dynamometer test bench

Captured from the human's own messages in the repo-setup session on 2026-11-26 (not a full interview; follow-up interview pending). Wording lightly condensed.

## Summary

- New hobby project "Sauerkrautperformance", a **monorepo** that can hold several subprojects.
- Planned technology: agents (Copilot), CI/CD, Python (Litestar, Polars, DuckDB, ...), TypeScript (Svelte, Vite), C++ for Arduino, Docker for deployment, "and more".
- First project: a **measurement station / test bench for mopeds**. Initially called "Trägheitsprüfstand für Mofas" (inertia test bench); later clarified that this is only one possibility: it may also be a **roller test bench (Rollenprüfstand)** or a dynamometer test bench in general. The design should be **generic**.
- Hardware roles: Arduino/ESP32 controls the physical hardware; a Raspberry Pi collects the data from the Arduino/ESP32 and also runs the GUI.
- GUI: a Svelte UI. Backend in Python: stores measurement data long term, processes the signals, calculates the performances.
- A **simulation** of the measurement station is wanted so that development does not need the hardware.
- The **software architecture is not decided yet** ("I'm not yet sure about the software architecture"); wanted for now: lint files and similar repo tooling, not project code. The project itself will be created later with the user's agents once the LLM wiki is filled.
- **Documentation** lives in the global `docs/` folder of the repo and is split into an internal technical set and an end-user set; the end-user documentation is hosted through this repo on the Raspberry Pi.
- The LLM wiki (OKF) lives under `docs/llm-wiki` and should reuse the learnings of the user's earlier wiki.

## Open questions and uncertainties

- Bench type(s): inertia, roller, with or without brake/load unit: unknown.
- Sensors, boards, roller geometry/inertia, throttle control, safety features: unknown.
- Software architecture (process split between Pi, backend, GUI): undecided.

## Evidence and attachments

Repo: `C:\Users\ekneissl\src\Sauerkrautperformance` (path of the local checkout).
