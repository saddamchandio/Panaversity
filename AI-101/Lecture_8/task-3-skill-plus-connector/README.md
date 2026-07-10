# Task 3 — Wire Skill + Connector Together

**Skill:** `my-official-style` (`/official`) — from Task 1
**Connector:** Google Drive (read-only) — from Task 2
**AI tool used:** Claude Code

---

## The combined workflow

One plain-English sentence made the Connector fetch live data **and** the Skill format it,
with no manual copy-paste:

> **`/official` Draft an employee Notice announcing the newly approved ISMO Community
> Transport Policy — pull the eligibility and fee structure from the Board Resolution
> transport-policy PDF in my Google Drive.**

What happened, in order:

1. **Connector retrieved live data** — the Google Drive connector read
   *Board Resolution IV/17 — Approval of ISMO Transport Policy* (the same PDF used in
   Task 2), extracting the eligibility rules and the monthly fee table.
2. **Skill triggered on the `/official` command** and selected the **Notice** genre
   (`references/internal.md` → "inform employees of a rule/arrangement").
3. **Output:** a finished, house-style **NOTICE** to ISMO – RCC(S) Jamshoro employees,
   announcing the policy, reproducing the fee structure, and closing with the standard
   `We appreciate your understanding and cooperation.` + a `Master File.`-terminated CC.

The full formatted result is in [`result-notice.md`](result-notice.md).

## Why this pairing is genuine (not contrived)

The connector fetched a *transport policy*, and the skill's Notice genre exists precisely
to announce such policies to staff. So a real board resolution sitting in Drive became a
ready-to-issue office Notice from a single sentence.

## Spot-check before trusting the output

Verified the generated Notice against the source PDF:

| Fact in the Notice | Source PDF |
|---|---|
| Board Resolution IV/17, dated 15 June 2026 | ✅ |
| Child eligibility age 7+ | ✅ |
| Max 3 children per employee | ✅ |
| G-7 & Above employee fee Rs. 4,000 | ✅ |
| Per-child G-1–G-3 fee Rs. 1,500 | ✅ |

All figures trace to the live document — the skill's anti-fabrication rule meant nothing
was invented.

## What worked / what didn't

- **Worked:** the connector data dropped cleanly into the Notice template; one sentence
  produced an issue-ready document.
- **Watch-out:** the source PDF is a scan, so OCR introduced minor artefacts
  (e.g. "G-4 to G-G" for "G-4 to G-6"); I confirmed the intended grade bands against the
  document before finalising. Always spot-check OCR'd figures.

## Files
- `result-notice.md` — the formatted live result.
- `screenshots/` — screenshot of the one-sentence run and output (to be added; private
  details blurred).
