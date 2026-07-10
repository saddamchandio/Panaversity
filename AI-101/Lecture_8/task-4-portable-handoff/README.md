# Task 4 — Make It Portable (Second Surface)

**Path chosen:** Make it portable (load the Skill into a second surface and run it there)
**Origin surface:** claude.ai (where `my-official-style` was authored)
**Second surface:** Claude Code (CLI / IDE)

---

## What I did

The `my-official-style` skill was originally built and stored on **claude.ai**. To prove it
is a real, reusable asset — not a one-conversation trick — I moved it to a completely
different surface and ran it there:

1. **Exported** the skill from claude.ai as `my-official-style.skill` (a zip containing
   `SKILL.md` + `references/{letters,disputes,internal}.md`).
2. **Installed** it into Claude Code's skills directory:
   `~/.claude/skills/my-official-style/`.
3. Claude Code **auto-discovered** it — the skill now appears in the Claude Code skill
   registry with the same `name` and `description`.
4. **Ran it** on the second surface with no re-explanation.

## Proof it works elsewhere

Two independent runs in Claude Code, both producing correct house-style output:

| Run | Command | Genre | Result |
|---|---|---|---|
| 1 | `/my-official-style` reminder to HESCO re: 11KV feeder | Reminder (REMINDER–I) | ✅ correct format — see `../task-1-my-skill/demo-run.md` |
| 2 | `/official` employee notice from Drive transport policy | Notice | ✅ correct format — see `../task-3-skill-plus-connector/result-notice.md` |

In both runs the skill reproduced the exact skeleton, courtesy idioms, escalation tone,
and `Master File.`-terminated CC — **identical discipline to the claude.ai original**, and
the anti-fabrication rule held (unverified references left as bracketed placeholders).

## Why the port was clean

A Skill is just a folder — `SKILL.md` plus plain-Markdown reference files, no code and no
platform-specific dependencies. That is exactly why it is portable: any surface that reads
the Skills format (claude.ai, Claude Code, Cowork) can load the same folder and behave the
same way. Nothing had to be rewritten.

## Verification

- ✅ Skill file copied intact (4 files, byte-for-byte from the export).
- ✅ Registered and invocable in Claude Code.
- ✅ Produced correct, consistent output on the new surface without re-explanation.

## Files
- The portable skill folder is committed under `../task-1-my-skill/my-official-style/`
  (and `my-official-style.skill` is the raw export).
- `screenshots/` — Claude Code skill list + a run on the second surface (to be added).
