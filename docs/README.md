# Documentation

Three separate documentation sets, all in this global `docs/` folder (not per project; a project gets a subfolder inside each set).

| Set | Folder | Audience | Written by | Published |
|-----|--------|----------|------------|-----------|
| Internal technical | [technical/](technical/index.md) | developers (you, agents) | humans + agents, in the same PR as the code | MkDocs site, internal (CI artifact; optional private hosting); **per subproject**: `technical/<project>/vision/` (product vision and goals) and `technical/<project>/architecture/` (arc42, ADRs) |
| End user | [user/](user/index.md) | people who operate the measurement station | humans + agents | MkDocs site, built into a Docker image and served **on the Raspberry Pi** from this repo |
| LLM wiki | [llm-wiki/](llm-wiki/GUIDE.md) | Copilot agents and you (requirements, decisions, physics, interview notes) | agents (OKF v0.2) | not published; read via Obsidian or agents |

Rules of thumb:

- *Why / how it fits together / how to build it* -> `technical/` (architecture, ADRs, protocols, runbooks).
- *How do I use it / what do the buttons do / safety* -> `user/` (plain language, no internals, task oriented; each project in `user/<project>/`).
- Knowledge that is still being captured or explored -> `llm-wiki/`; once it is settled, promote it into `technical/` or `user/`.
- The user docs ship with the product: they must be updated in the same PR as any UI or behaviour change, and must build with `--strict`.

## Build locally

```powershell
pip install -r docs/requirements.txt
mkdocs serve -f docs/mkdocs.user.yml        # end-user docs on http://127.0.0.1:8000
mkdocs serve -f docs/mkdocs.technical.yml   # internal docs
mkdocs build --strict -f docs/mkdocs.user.yml
```

## Deploy the user docs on the Raspberry Pi

`docs/Dockerfile.user` builds the user docs and serves them with nginx:

```powershell
docker build -f docs/Dockerfile.user -t sauerkraut-user-docs .
docker run -d -p 8080:80 --restart unless-stopped sauerkraut-user-docs
```

Once the GUI exists, the docs container becomes one service of the project's compose file and is linked from the GUI ("Help"). CI (`.github/workflows/docs.yml`) builds a multi-arch image (amd64 + arm64 for the Pi) on `main`.
