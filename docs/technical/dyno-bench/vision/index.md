# Product vision and goals

## Vision

A homebuilt, generic dynamometer test bench that lets a moped tuner measure and compare the performance of mopeds (power, torque over rpm) without special hardware knowledge, and keeps every measurement for later comparison.

## Problem

Tuning without measurement is guesswork. Commercial benches are expensive and closed; a homebuilt bench needs reliable data capture, signal processing and a usable UI. *TBD: refine in an interview.*

## Target users

* Operator/tuner (end user): runs measurements via the GUI on the Raspberry Pi. Documented in `docs/user/`.
* Developer (you, agents): extends bench types and analysis.

## Goals

| ID | Goal | Source |
|----|------|--------|
| G1 | Measure moped performance on a test bench and calculate performance values from the signals | kickoff |
| G2 | Keep measurement data long term and make runs comparable | kickoff |
| G3 | GUI on the Raspberry Pi; the Pi collects the data from the Arduino/ESP32 which controls the hardware | kickoff |
| G4 | Generic bench support (inertia, roller, dynamometer/brake) instead of one hard-wired type | kickoff |
| G5 | Full development without hardware through a simulation | kickoff |
| G6 | End-user documentation served from the Pi | kickoff |

"kickoff" = the project kickoff note (`docs/llm-wiki/raw/sauerkrautperformance/2026-11-26-project-kickoff.md`).

## Non-goals

*TBD* (to be captured in the interview, e.g. certified/homologation-grade measurement, emission testing).

## Success criteria

*TBD*, for example: repeatable results within a stated tolerance; a full measurement run in the simulator without hardware; operator can run a measurement using only the user guide.

## Scope and roadmap

*TBD.* Candidate order: (1) simulation and data pipeline, (2) GUI, (3) real hardware integration, (4) further bench types.
