# Lecture 7 — Code You Never Write

**Student:** Saddam Hussain · **Course:** Panaversity AI-101 · **Email:** saddamchandio@gmail.com

Four real-world projects built with the **"client, not coder"** approach: I describe a problem to an AI, hand off the coding, and **verify every result against a fact I already know**. The rule for all four: *never trust output you cannot check.*

> **AI tool used across all four projects:** Claude (Sonnet) via Claude Code.
> All input data is **synthetic and Pakistan-centric** — no real bank numbers, accounts, or personal data.

---

## The four projects

| # | Project | Problem it solves | Verified against | Result |
|---|---|---|---|---|
| 1 | [Money Detective](project-1-money-detective/) | Find the leak hiding in past transactions | Known monthly totals (Apr 44,965 / May 44,646) | PKR **7,088/mo** in forgotten subs + **PKR 4,398** double charges |
| 2 | [What's My Grade, Really](project-2-whats-my-grade/) | Encode my teacher's exact grading rules | Hand-computed quiz category (85.00%) | Standing **A- (80.15%)**; need **83.17%** on final for an A |
| 3 | [The Books Don't Match](project-3-books-dont-match/) | Reconcile messy dues against a known total | Hand-counted PKR 15,000 confirmed | 2 people owe **PKR 3,000**; 1 unexplained **PKR 1,500** deposit |
| 4 | [Organize the Mess](project-4-organize-the-mess/) | Safely see what's in a cluttered folder | Planted 3 dup pairs + 1 large file | Found exactly those; **0 originals touched** |

## Repository structure

```
Lecture_7/
├── README.md                          ← you are here
├── Lecture_7_Report.docx              ← detailed written report (all four projects)
├── project-1-money-detective/
│   ├── money_detective.py             ├── transactions.csv
│   ├── README.md  ├── prompts.md      └── screenshots/
├── project-2-whats-my-grade/
│   ├── grade_calculator.py            ├── grades_data.json
│   ├── README.md  ├── prompts.md      └── screenshots/
├── project-3-books-dont-match/
│   ├── reconcile.py                   ├── payments.csv  ├── reconcile_config.json
│   ├── README.md  ├── prompts.md      └── screenshots/
└── project-4-organize-the-mess/
    ├── organize.py  ├── make_sample_folder.py
    ├── sample_messy_folder/           ├── organized_output/
    ├── README.md  ├── prompts.md      └── screenshots/
```

## How to run everything

```bash
# Project 1
cd project-1-money-detective && python money_detective.py transactions.csv

# Project 2
cd project-2-whats-my-grade && python grade_calculator.py grades_data.json

# Project 3
cd project-3-books-dont-match && python reconcile.py payments.csv reconcile_config.json

# Project 4  (dry run is safe; --execute copies into a new folder)
cd project-4-organize-the-mess && python organize.py sample_messy_folder
```

No third-party libraries required — standard Python 3 only.

## What I learned

The skill isn't coding — it's being a **good client**: describe the problem precisely, encode the rules only *I* know, and then **prove the output** against a number I already trust. In every project the verification step was what turned "the AI said so" into "I checked, and it's right."
