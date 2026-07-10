# Task 1 — Prompts used

## A. Creation prompt (initial, to `skill-creator`)

> ⚠️ **Author to confirm/replace with your exact original wording.** The text below is a
> faithful reconstruction of the intent used to build the skill.

**Initial:**
> "Use the skill-creator skill to build me a skill that drafts my official office
> correspondence in my exact ISMO – RCC(S) Jamshoro house style. I keep re-explaining the
> same formats — request letters, reminders, Grid-Code rebuttals, point-by-point tabular
> replies, appreciation letters, office orders, notices, POL statements, and noting
> sheets. Capture the fixed reference-number stem, the date format, the bold
> addressee/subject/closing skeleton, the courtesy idioms, my signing designations, and
> the CC rules. Ask me whatever you need, then build it."

**Refinements (answering skill-creator's questions):**
- Provided real, anonymised examples of each genre so it could copy the exact skeleton.
- Added the **hard anti-fabrication rule** (never invent letter numbers, dates, amounts,
  NTNs, or Grid-Code clause text — use bracketed placeholders instead).
- Made it **command-only** (`/my-official-style` / `/official`) and told it explicitly
  *not* to auto-trigger on ordinary letter requests.
- Split the worked examples into three reference files (letters / disputes / internal) so
  the main SKILL.md stays lean and the right template is loaded per genre.
- Specified "paste-ready body text only — no .docx, logo, or footer" because the Word
  letterhead is pre-printed.

## B. Invocation prompt (how it is used day-to-day)

The skill is triggered by the command plus a single plain sentence describing the letter:

> `/my-official-style` Draft a REMINDER – I to the CEO, HESCO Hyderabad, chasing the
> pending energization of the newly constructed 11KV dedicated feeder to RCC(S) ISMO
> Jamshoro. Signer: Senior Director (SN & VRE Operations). Mark it Most Urgent.

See [`demo-run.md`](demo-run.md) for the full input and the output it produced.
