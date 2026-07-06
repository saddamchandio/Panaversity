"""
The Books Don't Match — reconcile a known total against a messy payment record.
Panaversity AI-101 · Lecture 7 · Project 3

Two records should agree: the money I EXPECT to have collected, and the messy
digital transfer history (Easypaisa / JazzCash) full of nicknames, missing
memos, and split payments. This script applies MY personal rules for reading the
ambiguous entries, then finds the gap and names the people to follow up with.

VERIFY, DON'T TRUST: I hand-counted that 10 members definitely paid = PKR 15,000.
The script must independently match exactly PKR 15,000 to roster members. If it
does, I trust its list of who still owes and which payments are unexplained.

Usage:  python reconcile.py payments.csv reconcile_config.json
"""

import csv
import json
import sys
from collections import defaultdict


def load_payments(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [
            {"date": r["date"].strip(),
             "sender": r["sender_raw"].strip(),
             "memo": r["memo"].strip(),
             "amount": float(r["amount_pkr"])}
            for r in csv.DictReader(f)
        ]


def match_member(pay, cfg):
    """Apply my personal interpretation rules. Return canonical name or None."""
    sender = pay["sender"].lower()
    memo = pay["memo"].lower()
    rules = cfg["interpretation_rules"]

    # Rule 1: number-based (e.g. Usman always pays from a number ending 4471, no memo)
    for frag, name in rules["number_contains"].items():
        if frag in sender:
            return name

    # Rule 2: nickname / first-name aliases
    for frag, name in rules["alias_contains"].items():
        if frag in sender:
            return name

    # Rule 3: direct match against roster (full or first name)
    for name in cfg["roster"]:
        if sender == name.lower() or sender == name.split()[0].lower():
            return name
        # "Imran Q" style: first name + initial
        if sender.startswith(name.split()[0].lower()) and len(sender) <= len(name):
            return name

    return None


def main():
    pay_path = sys.argv[1] if len(sys.argv) > 1 else "payments.csv"
    cfg_path = sys.argv[2] if len(sys.argv) > 2 else "reconcile_config.json"
    payments = load_payments(pay_path)
    cfg = json.load(open(cfg_path, encoding="utf-8"))

    dues = cfg["dues_per_member"]
    expected = cfg["expected_total"]

    paid_by = defaultdict(float)
    unmatched = []
    for p in payments:
        who = match_member(p, cfg)
        if who:
            paid_by[who] += p["amount"]
        else:
            unmatched.append(p)

    received_total = sum(p["amount"] for p in payments)
    matched_to_roster = sum(min(v, dues) for v in paid_by.values())  # cap at what they owe

    print("=" * 60)
    print(f" THE BOOKS DON'T MATCH  —  {cfg['fund_name']}")
    print("=" * 60)
    print(f"   Expected total (my count)   : PKR {expected:>10,.2f}")
    print(f"   Digitally received (raw)    : PKR {received_total:>10,.2f}")
    print(f"   Raw gap                     : PKR {expected - received_total:>10,.2f}")

    print("\n MATCHED PAYMENTS (after applying my interpretation rules)")
    print(" " + "-" * 56)
    for name in cfg["roster"]:
        if name in paid_by:
            v = paid_by[name]
            status = "OK" if v >= dues else f"SHORT by {dues - v:,.0f}"
            extra = f"  (+{v - dues:,.0f} OVER)" if v > dues else ""
            print(f"   {name:<16} PKR {v:>8,.2f}   {status}{extra}")

    # who still owes
    owing = [n for n in cfg["roster"] if paid_by.get(n, 0) < dues]
    owed_total = sum(dues - paid_by.get(n, 0) for n in owing)
    print("\n STILL OWES — needs follow-up")
    print(" " + "-" * 56)
    for n in owing:
        print(f"   {n:<16} owes PKR {dues - paid_by.get(n, 0):>8,.2f}")
    print(f"   {'-'*40}")
    print(f"   Confirmed unpaid dues        : PKR {owed_total:>10,.2f}")

    # overpayments
    over = [(n, paid_by[n] - dues) for n in paid_by if paid_by[n] > dues]
    if over:
        print("\n OVERPAYMENTS — refund or carry forward")
        print(" " + "-" * 56)
        for n, amt in over:
            print(f"   {n:<16} PKR {amt:>8,.2f} over")

    # unmatched payments
    print("\n UNMATCHED PAYMENTS — money in, owner unknown, follow up")
    print(" " + "-" * 56)
    unmatched_total = 0.0
    for p in unmatched:
        unmatched_total += p["amount"]
        print(f"   {p['date']}  '{p['sender']}'  memo:'{p['memo'] or '-'}'  PKR {p['amount']:,.2f}")
    print(f"   {'-'*40}")
    print(f"   Unexplained money in account : PKR {unmatched_total:>10,.2f}")

    print("\n" + "=" * 60)
    print(" RECONCILIATION SUMMARY")
    print("=" * 60)
    print(f"   Matched to roster (capped)   : PKR {matched_to_roster:>10,.2f}")
    print(f"   Still owed by members        : PKR {owed_total:>10,.2f}")
    print(f"   Unexplained deposits         : PKR {unmatched_total:>10,.2f}")
    over_total = sum(a for _, a in over)
    print(f"   Overpayments                 : PKR {over_total:>10,.2f}")
    print(f"   Check: matched + owed        : PKR {matched_to_roster + owed_total:>10,.2f}"
          f"  (should equal expected {expected:,.0f})")
    print("=" * 60)


if __name__ == "__main__":
    main()
