# Project 2 — What's My Grade, Really

**Problem it solves:** The university portal shows raw marks but does **not** encode my teacher's actual rules — *drop the lowest quiz*, *weighted categories*, and a *conditional replacement* where the final exam replaces the midterm if it's higher. This script encodes those exact rules and tells me (a) where I truly stand and (b) the precise final-exam score I need for an **A**.

**AI tool used:** Claude (Sonnet) via Claude Code. I gave the teacher's grading policy and my scores in plain text; the AI wrote the calculator; I verified one category by hand.

---

## The teacher's rules (encoded in `grades_data.json`)

| Category | Weight | Rule |
|---|---|---|
| Quizzes | 15% | 5 quizzes /10, **drop the lowest 1** (best 4 count) |
| Assignments | 10% | 4 assignments /100, all count |
| Midterm | 25% | /100 |
| Project | 15% | /100 |
| Final | 35% | /100 |
| **Special** | — | **If Final% > Midterm%, the midterm's 25% moves onto the final** (final → 60%, midterm → 0%) |

**Grading scale:** A ≥ 85, A- ≥ 80, B+ ≥ 75, B ≥ 70, …

**My scores:** quizzes `[7, 9, 5, 8, 10]`, assignments `[88, 92, 79, 95]`, midterm `68`, project `90`, final *not taken yet*.

> Synthetic data — course, institution, and scores are made up. Edit `grades_data.json` with your own rules and marks to use it for real.

## How to run

```bash
python grade_calculator.py grades_data.json
```

## Result (what I can act on)

- **Current standing: 80.15% → A-** on the 65% of the course graded so far.
- To reach my **A** target I need **83.17%** on the final — **not** the 94% the naïve calculation suggests — **because the replacement rule applies** (my final will beat my 68% midterm, so the midterm's weight shifts to the final). That single rule is the difference between a reachable and an almost-impossible target.

---

## Verification — *never trust output you cannot check*

I re-computed the **quiz category by hand** and matched it against the script:

```
Quizzes /10: 7, 9, 5, 8, 10   →  drop lowest (5)
Best 4:  10 + 9 + 8 + 7 = 34   →  34 / 40 = 85.00%
```

| Figure | Hand calculation | Script output | Match |
|---|---|---|---|
| Quiz category % | 85.00% | 85.00% | ✅ |
| Current standing | (0.15·85 + 0.10·88.5 + 0.25·68 + 0.15·90)/0.65 = 80.15% | 80.15% | ✅ |
| Final needed (no rule) | (85 − 52.10)/0.35 = 94.00% | 94.00% | ✅ |

Because the category I could check by hand matched exactly, I trust the replacement-rule logic I could **not** easily do by hand.

See `screenshots/grade_result.png` and `output_log.txt`.
