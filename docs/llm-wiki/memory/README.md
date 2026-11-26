# Agent memory

Private working memory for the LLM maintaining this wiki. It lives **outside** `wiki/` on purpose, so the OKF bundle stays clean and shareable.

Read all files here at the start of every session. Update them when you learn something durable.

| File | Purpose |
|------|---------|
| `user.md` | Who the user is, their preferences, language, and working style |
| `decisions.md` | Conventions and decisions made for this wiki, with the reason and date |
| `learnings.md` | Mistakes, gotchas, and what worked or didn't, so you don't repeat them |
| `todo.md` | Open follow-ups, wiki gaps, and sources the user wants ingested |

Rules:
- Keep entries short, dated (`YYYY-MM-DD`), and newest first.
- Store only durable facts. No secrets, credentials, or sensitive personal data.
- Wiki knowledge belongs in `wiki/`, not here. This is about *how to work*, not *what is known*.
- Prune stale or contradicted entries instead of piling up.
