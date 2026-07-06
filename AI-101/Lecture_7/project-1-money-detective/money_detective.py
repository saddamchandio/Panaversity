"""
Money Detective — hunt the leaks in your own transaction history.
Panaversity AI-101 · Lecture 7 · Project 1

WHAT IT DOES (plain English):
  1. Reads a bank/wallet statement (date, description, amount).
  2. Finds RECURRING charges  -> the same merchant + amount that shows up
     in more than one month. These are your subscriptions.
  3. Flags FORGOTTEN subscriptions -> recurring charges that look like
     "set and forget" services (gym, cloud storage, streaming add-ons).
  4. Finds DUPLICATE charges  -> the exact same charge (date + merchant +
     amount) billed more than once = you were charged twice.
  5. Prints MONTHLY TOTALS so you can verify against a figure you already
     know (your bank statement footer).

VERIFY, DON'T TRUST: check the monthly totals below against your real
statement. If they match, the rest of the findings can be trusted.

Usage:  python money_detective.py transactions.csv
"""

import csv
import sys
from collections import defaultdict, Counter

# Keywords that usually mean "silent monthly drain" — tune to your own life.
FORGOTTEN_HINTS = ("gym", "membership", "cloud", "storage", "vip",
                   "premium", "netflix", "spotify", "youtube", "prime")


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                "date": r["date"].strip(),
                "month": r["date"].strip()[:7],
                "desc": r["description"].strip(),
                "amount": float(r["amount_pkr"]),
            })
    return rows


def monthly_totals(rows):
    totals = defaultdict(float)
    for r in rows:
        totals[r["month"]] += r["amount"]
    return dict(sorted(totals.items()))


def find_recurring(rows):
    """A (description, amount) pair seen in 2+ distinct months = recurring."""
    months_seen = defaultdict(set)
    for r in rows:
        months_seen[(r["desc"], r["amount"])].add(r["month"])
    recurring = {k: sorted(v) for k, v in months_seen.items() if len(v) >= 2}
    return recurring


def find_duplicates(rows):
    """Exact (date, description, amount) appearing more than once = double charge."""
    counts = Counter((r["date"], r["desc"], r["amount"]) for r in rows)
    return {k: n for k, n in counts.items() if n > 1}


def looks_forgotten(desc):
    d = desc.lower()
    return any(h in d for h in FORGOTTEN_HINTS)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "transactions.csv"
    rows = load(path)

    print("=" * 62)
    print(" MONEY DETECTIVE  —  leak report")
    print("=" * 62)
    print(f" Loaded {len(rows)} transactions from '{path}'\n")

    # --- 1. Monthly totals (VERIFY THESE against your bank statement) ---
    print("-" * 62)
    print(" MONTHLY TOTALS  (verify against your statement footer)")
    print("-" * 62)
    for m, t in monthly_totals(rows).items():
        print(f"   {m}   PKR {t:>12,.2f}")

    # --- 2. Recurring charges / subscriptions ---
    recurring = find_recurring(rows)
    print("\n" + "-" * 62)
    print(f" RECURRING CHARGES  ({len(recurring)} found)")
    print("-" * 62)
    monthly_bleed = 0.0
    for (desc, amt), months in sorted(recurring.items(), key=lambda x: -x[0][1]):
        flag = "  <-- FORGOTTEN?" if looks_forgotten(desc) else ""
        monthly_bleed += amt
        print(f"   PKR {amt:>9,.2f} x {len(months)} mo  {desc}{flag}")
        print(f"                        seen: {', '.join(months)}")

    # --- 3. Forgotten-subscription summary ---
    forgotten = [(d, a) for (d, a) in recurring if looks_forgotten(d)]
    forgotten_cost = sum(a for _, a in forgotten)
    print("\n" + "-" * 62)
    print(" FORGOTTEN-SUBSCRIPTION SUSPECTS")
    print("-" * 62)
    for d, a in sorted(forgotten, key=lambda x: -x[1]):
        print(f"   PKR {a:>9,.2f} / month   {d}")
    print(f"   {'-'*40}")
    print(f"   PKR {forgotten_cost:>9,.2f} / month  = PKR {forgotten_cost*12:,.2f} / year")

    # --- 4. Duplicate charges ---
    dups = find_duplicates(rows)
    print("\n" + "-" * 62)
    print(f" DUPLICATE / DOUBLE CHARGES  ({len(dups)} found)")
    print("-" * 62)
    dup_loss = 0.0
    for (date, desc, amt), n in dups.items():
        overcharge = amt * (n - 1)
        dup_loss += overcharge
        print(f"   {date}  x{n}  PKR {amt:,.2f}  {desc}")
        print(f"                 overcharged by PKR {overcharge:,.2f}")
    print(f"   {'-'*40}")
    print(f"   Total recoverable from duplicates: PKR {dup_loss:,.2f}")

    # --- 5. Bottom line ---
    print("\n" + "=" * 62)
    print(" THE LEAK")
    print("=" * 62)
    print(f"   Forgotten subscriptions : PKR {forgotten_cost:>9,.2f} / month")
    print(f"   Duplicate charges       : PKR {dup_loss:>9,.2f} (one-off recover)")
    print(f"   Annualised subscription bleed: PKR {forgotten_cost*12:,.2f}")
    print("=" * 62)


if __name__ == "__main__":
    main()
