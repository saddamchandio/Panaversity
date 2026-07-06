# Project 4 — Organize the Mess (The Files You Forgot)

**Problem it solves:** My Downloads/Documents folder is chaos — duplicate files, forgotten downloads, screenshots, a giant installer. This script tells me **what's actually in there** (duplicates, large files, groupings) and can tidy it — but it is built so a careless run can **never** delete or overwrite anything.

**AI tool used:** Claude (Sonnet) via Claude Code. The whole point of this project is the **safety discipline**, so I explicitly demanded a dry run and copy-only behaviour in my prompts.

---

## Safety design (the "client, not coder" discipline)

This is the only project that touches real files, so it follows the lecture's safe order:

1. **Work on a copy** — the input is a sample folder; the script only ever **reads** it.
2. **Dry run by default** — running it with no flag shows the **full plan** and touches nothing.
3. **Copy, never move/delete** — `--execute` **copies** files into a brand-new `organized_output/` folder. Originals are left exactly where they were.
4. **Duplicates are reported, not deleted** — identity is proven by **SHA-256**, but *I* decide what to remove.

## The data

`sample_messy_folder/` — 19 synthetic files (regenerate any time with `python make_sample_folder.py`). It deliberately contains **3 true duplicate pairs** (identical bytes) and **1 large file**.

## How to run

```bash
python organize.py sample_messy_folder             # DRY RUN — safe, shows the plan
python organize.py sample_messy_folder --execute   # copies into organized_output/
```

## Result (what I can act on)

- **3 duplicate groups** found by content hash: `IMG_20260501_123456.jpg` (downloaded twice), `assignment1.docx` / `assignment1 - Copy.docx`, and `resume_final.pdf` / `resume_final_v2.pdf`. I can safely delete one of each.
- **1 large file** flagged: `setup_installer.exe` (156 KB) — a finished download I can remove.
- Everything grouped into `Documents/ (9), Images/ (5), Audio/, Archives/, Code/, Installers/, Other/`.
- On `--execute`, all 19 files were copied into `organized_output/` and **the original folder still had all 19 files** — proving nothing was moved or lost.

---

## Verification — *never trust output you cannot check*

The verifiable facts for this project are about **safety and counts**, which I confirmed directly:

| Check | Expected | Actual | Match |
|---|---|---|---|
| Originals after `--execute` | 19 files (untouched) | 19 files | ✅ |
| Files copied to output | 19 | 19 | ✅ |
| Duplicate groups (by SHA-256) | 3 (I planted them) | 3 | ✅ |
| Large files > 100 KB | 1 (the 156 KB installer) | 1 | ✅ |

I planted exactly 3 duplicate pairs and 1 large file, and the script found exactly those — and left every original in place — so I trust it on a real folder.

See `screenshots/organize_dryrun.png`, `output_log_dryrun.txt`, and `output_log_execute.txt`.
