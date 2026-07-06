# Project 3 — The Books Don't Match

**Problem it solves:** I collect monthly dues for our cricket club. I *know* what the books should say, but the digital record (Easypaisa / JazzCash history) is a mess — nicknames, blank memos, a split payment, an overpayment, and a deposit from a number I don't recognise. This script applies **my personal knowledge** of who's who, reconciles the record against my known total, and names exactly who I still need to chase.

**AI tool used:** Claude (Sonnet) via Claude Code. I stated the target total up front, handed over the messy records *uncleaned*, and gave my interpretation rules; the AI wrote the reconciler.

---

## The data

- `payments.csv` — the transfer history **exactly as received**, not cleaned up: `Chintu`, `Guddu bhai`, a bare number `0321-XXX4471`, `Kashif … Eid Mubarak`, a split payment from `Danish` (800 + 700), an overpayment from `Saad` (2000), and a mystery deposit `0300-1234567`.
- `reconcile_config.json` — the 12-member roster, dues (PKR 1,500 each), expected total (PKR 18,000), and **my interpretation rules**.

> Synthetic data — names/numbers are made up. Nothing real or sensitive.

## My interpretation rules (personal knowledge no app has)

- `Chintu` → **Bilal Ahmed** (his nickname)
- `Guddu` → **Faizan Ali**
- any number containing `4471` → **Usman Khan** (he never writes a memo)
- `Kashif Iqbal` + memo "Eid Mubarak" → counts as **his dues**
- first-name / `Imran Q` style partial matches → the matching roster member

## How to run

```bash
python reconcile.py payments.csv reconcile_config.json
```

## Result (what I can act on)

- **Follow up with 2 people:** **Waqar Younis** and **Naveed Akhtar** each still owe **PKR 1,500** → **PKR 3,000** confirmed unpaid.
- **One unexplained deposit** of **PKR 1,500** from `0300-1234567` (no memo) — probably one of the two above, but I have no proof, so it needs a message to confirm before I mark them paid.
- **Saad Nadeem overpaid by PKR 500** — refund or carry to next month.
- The split payment from Danish (800 + 700) correctly reconciled to a full **PKR 1,500**.

---

## Verification — *never trust output you cannot check*

I stated my known total **up front** and hand-counted the confirmed payers:

```
I personally confirmed 10 members paid PKR 1,500 each  =  PKR 15,000 (my baseline)
Roster expected total  =  12 × 1,500  =  PKR 18,000
```

| Figure | Known baseline | Script output | Match |
|---|---|---|---|
| Matched to roster | PKR 15,000 | PKR 15,000 | ✅ |
| Reconciliation check (matched + owed) | PKR 18,000 | PKR 18,000 | ✅ |

The script independently reproduced my hand-counted **15,000** and the books balanced back to the expected **18,000**, so I trust its identification of the gap and the unmatched deposit.

See `screenshots/reconcile_result.png` and `output_log.txt`.
