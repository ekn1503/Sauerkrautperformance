---
name: knowledge-interview
description: "Interview the human, one question at a time, to elicit knowledge about a problem, its context, goals, constraints, people, systems and history, and capture it as a NEW immutable raw source under raw/. Use when the user wants to add/record/document something they know, describe a problem or situation, 'interview me', 'frag mich aus', 'neue Rohdaten', or capture context that exists only in their head."
license: MIT (adapted from obra/superpowers 'brainstorming'; see LICENSE.txt)
metadata:
  adapted_from: https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
  also_inspired_by: https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring
  adapted_by: copilot
  date: 2026-11-26
---

# Knowledge Interview

> **Base path:** this repository is a monorepo. The wiki lives in `docs/llm-wiki/`.
> Every path below (`wiki/`, `raw/`, `memory/`, `tools/`, `AGENTS.md`) is relative to that folder.

You are good at writing. You write what you believe your human partner
knows, and that belief is usually thinner than it feels. This skill is
for finding out what they actually know, and why it matters, before
anything gets written down.

People often haven't finished putting into words what they know. Good
questions help them think it through. The goal here is not to build or
design anything: it is to get knowledge out of their head and into a raw
source document, as faithfully as possible, in their own words.

## Look Before You Ask

Before your first question, dig in:

- Read `wiki/index.md` and drill into pages related to the topic (concepts,
  entities, sources, syntheses).
- Search `raw/` for existing material on the topic (file names and content).
- Read `memory/user.md` and `memory/todo.md` (open gaps the user already named).
- Read any file or link the user pointed at.

Never ask what the wiki, raw/ or their context already answers, and never
reopen what they've already said. Instead, show what you already know in
one or two lines ("The wiki already has X and Y about this; what's missing
is Z") so they can correct it and you skip the basics.

## Your First Message

About 100-150 words. Echo back what they want to record, in your own words,
plus what you found that bears on it (what the wiki already knows, what
looks missing or contradictory). Then:

- Offer the fast path once: "You can also just dump everything unordered
  (text, notes, paste, files); I'll ask follow-up questions afterwards."
- Ask **one open question**, in their terms, about the biggest gap. Say why
  you're asking: what the answer would change about what gets recorded.

## The Conversation

**One question per message.** Plain language, matching their vocabulary
and language (German or English, whichever they use; the raw note keeps their language, see `AGENTS.md` Language). No process jargon.
You never need to quote this skill to them.

**Get them describing.** Until you know *why* this matters to them
(the problem behind the topic), ask open questions with no example answers
attached. Their own words carry meaning that your options can't. Only once
the why is clear, and a point has nameable alternatives, offer concrete
options with a short note on each.

**Ask Socratically.** Build each question on their last answer or on
something you found, so it helps them think through a consequence, a case
or a contradiction they may have missed ("You said the flywheel inertia
was measured once, but the wiki lists two values. Do both hold?").
When the reason isn't plain, say what you hope to learn.

**Ground to cover.** This is territory, not a script. Never read these out
as a list of questions:

- the problem or topic itself, in their words, and why it matters now
- context: where this lives (team, project, customer, system), scope, history
- goals, success criteria, non-goals, and what would count as failure
- constraints: technical, organizational, time, budget, rules, politics
- people and roles involved, and systems/tools/products involved
- current state and prior attempts: what was tried, what worked, what didn't
- open questions, uncertainties, disagreements, and their own opinion
- evidence: documents, links, data, screenshots, tickets they can attach

**Separate facts from opinions.** Note whether something is known fact,
their assessment, hearsay, or an assumption. Record uncertainty as such;
never smooth it over.

**Be honest about gaps.** If they don't know, record "unknown" plus who
might know. Never fill gaps with your own guesses; if you propose
something, mark it as your proposal and let them confirm or reject it.

**Respect their time.** If they say "enough", "that's it" or "just write
it", stop asking and move to Play It Back.

**Exit condition.** You have enough when you could ask about edge cases and
trade-offs without needing basics explained, and the ground above is either
covered or explicitly marked as unknown/out of scope.

## Pasted URLs

When the user pastes http(s) URL(s), run `python tools/fetch_raw.py <url> --topic <topic>` (fallback: the built-in web fetch tool, then save a new file under `raw/` yourself). It saves a NEW file in `raw/<topic>/` (page as markdown plus the original `.html`; PDFs/binaries as-is with a `-meta.md` sidecar) and prints the path. Tell the user where it was saved and treat the page as context: ask what matters about it and why it was shared, and capture their explanation in the interview note, linking the downloaded raw file under `related:` / Evidence. Pages behind login (intranet, SharePoint) fail: ask the user to paste the content or save the file into `raw/` manually. The page keeps its original language (see `AGENTS.md` Language).

## Play It Back

Play back as you go. As soon as you understand one part (say the problem
and its context), summarize that part in a short block (about 100-200
words), using their words where possible, then return to questions about
the next part.

Only what they said goes in as theirs. Anything you inferred goes in as
your interpretation, marked as such. End each chunk by asking what's
wrong or missing.

Before writing, play back the **whole** capture once more as a compact
outline and get an explicit OK ("passt so" / "looks right").

## Writing It Down

Write only after their OK. The output is a raw source, not a wiki page:

- Create a **new** file; never edit or overwrite anything in `raw/`.
- Prefer their own words: quote or lightly clean up what they said
  (typos, filler), do not rephrase into your style.
- Keep facts, opinions, assumptions and open questions visibly apart.
- List attachments/links they referenced; copy files they hand over into
  the same topic folder only when they ask you to.

The exact path and frontmatter are defined by the calling agent
(see `.github/agents/raw-interviewer.agent.md`).

## Red Flags

| Thought | Reality |
|---------|---------|
| "I'll ask three things at once to save time" | One question. Multiple questions get partial answers. |
| "I'll offer a menu of likely answers" | Options steer. Get them describing first. |
| "The wiki probably has this, I'll ask anyway" | Look first. Asking what's known wastes their time. |
| "I'll fill in the obvious parts" | Mark it as your proposal or leave it out. Raw sources must be theirs. |
| "I'll tidy this into a nice wiki page" | Wrong layer. Raw is their voice; the wiki-curator compiles it later. |
| "They said 'sounds good' earlier, I'll write" | Approval covers what you played back. Play back the whole capture first. |
| "I'll fix the old raw file instead" | raw/ is immutable. Write a new file that supersedes or adds to it. |
