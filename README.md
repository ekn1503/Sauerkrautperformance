# Sauerkrautperformance

Monorepo for the Sauerkrautperformance hobby projects. First project: a generic dynamometer test bench for mopeds (inertia, roller or brake type, still open): ESP32/Arduino firmware, Raspberry Pi with Svelte GUI, Python backend for signal processing and long-term storage.

Status: planning. The architecture is being captured in the LLM wiki before code is written.

- Knowledge base: [docs/llm-wiki](docs/llm-wiki/GUIDE.md) (OKF v0.2, maintained with Copilot agents)
- Rules for humans and agents: [AGENTS.md](AGENTS.md)

## Setup

```powershell
pip install pre-commit
pre-commit install
pre-commit run --all-files
python docs/llm-wiki/tools/lint.py
```

Start an agent in this folder: `copilot --agent wiki-unicorn`.
