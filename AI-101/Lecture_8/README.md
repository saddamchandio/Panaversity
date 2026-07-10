# AI-101 Lecture 8 — Skills & Connectors

**Student:** Saddam Hussain
**Course:** Panaversity AI-101 · *The AI Agent Factory* — Skills & Connectors crash course

This repository contains all **five** hands-on projects in one place: building a real
Skill, connecting an app read-only, wiring the two together, proving the Skill is portable,
and auditing a Skill before trusting it.

## The five projects

| # | Folder | What it demonstrates |
|---|---|---|
| 1 | [`task-1-my-skill/`](task-1-my-skill/) | **`my-official-style`** — a real, in-use skill that drafts my ISMO – RCC(S) Jamshoro official correspondence (12 genres) in my exact house style, with a hard anti-fabrication rule. |
| 2 | [`task-2-connect-app/`](task-2-connect-app/) | **Google Drive, read-only** — retrieved and summarized a real board resolution PDF, then verified the summary against the source. |
| 3 | [`task-3-skill-plus-connector/`](task-3-skill-plus-connector/) | **Skill + Connector** — one sentence pulled the live transport policy from Drive and formatted it into an official house-style Notice. |
| 4 | [`task-4-portable-handoff/`](task-4-portable-handoff/) | **Portability** — exported the skill from claude.ai and ran it in Claude Code with identical results. |
| 5 | [`task-5-skill-audit/`](task-5-skill-audit/) | **Safety audit** — a code-level audit of the official `skill-creator` skill: what it does, what it touches, and whether it's safe. |

## AI tools & apps used

- **Claude** (claude.ai) — authored the `my-official-style` skill with `skill-creator`.
- **Claude Code** — ran the skill, wired the connector, and audited `skill-creator`.
- **Google Drive connector** (read-only) — retrieved real documents (Tasks 2 & 3).

## Full write-up

See [`REPORT.md`](REPORT.md) for the per-project report (what it does, prompts, how it was
tested, what worked / what didn't).

## Safety & privacy

- No tokens, passwords, OAuth credentials, or private data exports are committed.
- Screenshots have private letter/email content blurred.
- The connector was used **read-only**; no write access was granted.
