# AI-101 Lecture 8 — Report (Skills & Connectors)

**Student:** Saddam Hussain

A per-project report covering all five tasks: what each does, the AI tools/apps used, the
prompts, how I tested it, and what worked / what didn't.

---

## Task 1 — `my-official-style` skill

**What it does.** Drafts my official ISMO – RCC(S) Jamshoro correspondence in my exact
house style — request letters, reminders, Grid-Code rebuttals, point-by-point tabular
replies, appreciation letters, office orders, notices, POL statements, noting sheets, and
more — as paste-ready text for our pre-printed Word letterhead.

**Tools/apps.** Claude + `skill-creator` (to build it); Claude Code (to run it).

**Prompts.** Built by describing the task to `skill-creator`, answering its clarifying
questions, and feeding anonymised examples of each genre; refined to add the hard
anti-fabrication rule, the command-only trigger, and a 3-file reference split. Invoked
day-to-day as `/my-official-style` + one plain sentence. (See
`task-1-my-skill/prompts.md`.)

**How I tested it.** Installed into Claude Code and invoked it on a reminder scenario in a
fresh context; confirmed it reproduced the exact skeleton, courtesy idioms, escalation
tone, and `Master File.` CC, and that it left unknown reference numbers as `[____]`
placeholders instead of inventing them. (See `task-1-my-skill/demo-run.md`.)

**What worked / didn't.** Worked: consistent house style from one sentence; the
anti-fabrication rule makes drafts safe to trust after a fact check. Watch-outs: emits
Markdown bold (strip asterisks when pasting to Word); quoted Grid-Code clause text must be
supplied by me, by design.

**Why I chose it / how it helps.** Official letter-writing is the task I repeat and
re-explain the most, in a very specific register. This skill turns a one-line description
into a finished draft in my own voice, so my time goes to verifying facts, not formatting.

**Design note.** I deliberately kept it **command-only** (it will not auto-trigger). An
official letter sent in the wrong register or to the wrong addressee is a real liability,
so deliberate invocation is a safety feature, not a limitation.

---

## Task 2 — Connect Google Drive (read-only)

**What it does.** Gives Claude safe, read-only access to my Google Drive so it can find and
summarize a real document with no copy-paste.

**Tools/apps.** Claude Code + Google Drive connector (read-only).

**Prompt.** "Find *BOARD RESOLUTION IVI7 (APPROVAL OF ISMO TRANSPORT POLICY).pdf* in my
Drive and summarize it."

**How I tested it.** The connector searched my Drive, opened the PDF, and summarized it. I
spot-checked five facts (meeting date, child age 7+, max 3 children, G7+ fee Rs. 4,000,
3-year review cycle) against the real file — all matched. (See `task-2-connect-app/`.)

**What worked / didn't.** Worked: genuine retrieval, accurate summary. Didn't: the PDF is a
scan, so OCR added minor artefacts I had to sanity-check.

**Permission granted (one sentence).** I granted **read-only** access — Claude could search
and read files but could not create, edit, move, or delete anything; I would only need
**write** access if I wanted it to save results back into Drive, which I did not grant.

---

## Task 3 — Wire Skill + Connector together

**What it does.** One plain sentence fetches live data from Drive and formats it with my
skill — no manual copy-paste.

**Tools/apps.** Claude Code + Google Drive connector + `my-official-style` skill.

**Prompt (the one sentence).** "`/official` Draft an employee Notice announcing the newly
approved ISMO Community Transport Policy — pull the eligibility and fee structure from the
Board Resolution transport-policy PDF in my Google Drive."

**How I tested it.** The connector read the policy PDF; the skill triggered on `/official`,
picked the Notice genre, and produced an issue-ready house-style Notice with the fee table.
I spot-checked the figures against the source before trusting the output — all traced back
to the live document. (See `task-3-skill-plus-connector/result-notice.md`.)

**What worked / didn't.** Worked: the pairing is genuine (a transport policy → an employee
Notice); one sentence produced a finished document. Watch-out: OCR figures were
double-checked against the PDF.

---

## Task 4 — Make it portable

**What it does.** Proves the skill is a reusable asset, not a one-chat trick, by running it
on a second surface.

**Tools/apps.** Exported from claude.ai → installed into Claude Code (`~/.claude/skills/`).

**How I tested it.** Claude Code auto-discovered the skill and ran it correctly twice (the
Task 1 reminder and the Task 3 notice) with no re-explanation — identical formatting
discipline to the claude.ai original. A Skill is just a folder of Markdown, which is why the
port was clean. (See `task-4-portable-handoff/`.)

**What worked / didn't.** Worked: byte-for-byte port, immediate recognition, correct output.
Didn't: nothing — the format is inherently portable.

---

## Task 5 — Audit a skill before trusting it

**What it does.** A safety assessment of the official `skill-creator` skill.

**Tools/apps.** Claude Code (read the full skill folder + all scripts).

**How I tested it.** Code-level review: searched every script for outbound-network imports,
credential handling, and process execution, and traced each finding.

**Assessment & verdict.** **Safe to enable.** No outbound data, no credential handling; the
core workflow is local Python stdlib scripts, a localhost-only eval viewer, and the local
`claude` CLI. Two honest caveats: (1) it executes local processes and writes files into
`.claude/` (expected for a dev tool); (2) the optional browser viewer pulls fonts + one JS
library from public CDNs (inbound static assets, not data exfiltration). Full reasoning in
`task-5-skill-audit/README.md`.

---

## Overall

All five tasks were completed with **real** tools and **real** data: a skill I genuinely
use, a live read-only Google Drive pull, a one-sentence combined workflow, a cross-surface
portability proof, and an evidence-based safety audit.
