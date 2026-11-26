# Technical documentation

Internal documentation for developers and agents, **one folder per subproject**. Each subproject has the same two parts:

| Part | Content |
|------|---------|
| `vision/` | Product vision and goals: problem, target users, goals and non-goals, success criteria, scope, roadmap |
| `architecture/` | Software architecture: [arc42](https://arc42.org) sections in `arc42/` and architecture decision records in `adr/` |

## Subprojects

| Subproject | Status |
|------------|--------|
| [Dynamometer test bench](dyno-bench/index.md) | planning; architecture undecided |

## Adding a subproject

Copy the folder structure of an existing subproject (`<name>/index.md`, `vision/`, `architecture/arc42/` with the 12 sections, `architecture/adr/`), add it to the nav in `docs/mkdocs.technical.yml` and to the table above. Use lowercase-kebab-case names that match the project folder under `apps/`.

Cross-cutting topics that belong to no single subproject (repo tooling, shared libraries) get their own top-level folder here. Open questions and not-yet-decided material stay in the LLM wiki (`docs/llm-wiki/`, not part of this site) and are promoted here once settled; end-user material belongs in `docs/user/`.
