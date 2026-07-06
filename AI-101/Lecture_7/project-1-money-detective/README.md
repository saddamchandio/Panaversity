# Project 1 — Money Detective

**Problem it solves:** Ordinary budgeting apps track money *going forward*. This project hunts the leak *already hiding* in past transactions — forgotten subscriptions and duplicate (double) charges — using rules that are personal to me.

**AI tool used:** Claude (Sonnet) via Claude Code, acting as the code generator. I was the *client*: I described the problem and the personal "leak" rules, the AI wrote the script, and I verified the output against a total I already knew.

---

## The data

`transactions.csv` — a synthetic but realistic Pakistani bank/wallet statement (PKR) covering **March–May 2026**, 50 transactions. Merchants are local: K-Electric, SSGC, PTCL, PSO, Foodpanda, Careem, Daraz, Imtiaz, Naheed, Jazz, plus streaming/gym subscriptions.

> Data is synthetic — no real account numbers or personal data. Replace with your own statement export (columns: `date, description, amount_pkr`) to use it for real.

## How to run

```bash
python money_detective.py transactions.csv
```

## What it finds

- **Recurring charges** — a `(description, amount)` pair appearing in 2+ distinct months.
- **Forgotten-subscription suspects** — recurring charges matching personal keywords (gym, cloud, VIP, streaming).
- **Duplicate charges** — exact `(date, description, amount)` billed more than once.
- **Monthly totals** — printed so they can be verified against the real statement.

## The concrete finding (what I can act on)

- **PKR 7,088 / month** is bleeding out through 6 recurring subscriptions — a **Shaukat Khanum gym membership (PKR 4,500)** I stopped using is the biggest. That is **PKR 85,056 / year**.
- **Two duplicate charges** were caught: Foodpanda Pizza Max double-billed on 2026-04-13 (PKR 1,899) and a Daraz bedsheet double-billed on 2026-05-22 (PKR 2,499) — **PKR 4,398 recoverable**.

---

## Verification — *never trust output you cannot check*

I confirmed the script against **two figures I already knew** from the statement footer:

| Figure | Known baseline (statement) | Script output | Match |
|---|---|---|---|
| April 2026 total spend | PKR 44,965.00 | PKR 44,965.00 | ✅ |
| May 2026 total spend | PKR 44,646.00 | PKR 44,646.00 | ✅ |

Hand-check of the subscription total: 4500 + 1100 + 550 + 439 + 299 + 200 = **7,088** ✅ — matches the script's monthly bleed figure.

Because the totals I *already knew* matched exactly, I trust the recurring/duplicate findings that I could not have computed by hand.

See `screenshots/money_detective_result.png` for the full run and `output_log.txt` for the raw text.
