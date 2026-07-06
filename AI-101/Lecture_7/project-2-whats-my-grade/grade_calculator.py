"""
What's My Grade, Really — encode YOUR teacher's exact rules.
Panaversity AI-101 · Lecture 7 · Project 2

Generic grade apps don't know your teacher's real rules: dropped lowest quiz,
weighted categories, and a conditional replacement (final replaces midterm if
higher). This script encodes those exact rules and answers two questions:
  1. Where do I actually stand right now (on completed work)?
  2. What exact score do I need on the final to hit my target grade?

VERIFY, DON'T TRUST: the script prints each category %. Re-compute ONE category
by hand (quizzes) and confirm it matches before trusting the final-exam target.

Usage:  python grade_calculator.py grades_data.json
"""

import json
import sys


def letter(scale, pct):
    for lg, cutoff in sorted(scale.items(), key=lambda x: -x[1]):
        if pct >= cutoff:
            return lg
    return "F"


def quiz_pct(scores, policy):
    """Best (count - drop_lowest) quizzes, as a percentage."""
    q = sorted(scores, reverse=True)
    keep = len(q) - policy["drop_lowest"]
    best = q[:keep]
    return sum(best) / (keep * policy["out_of"]) * 100, best


def category_percents(data):
    s, p = data["scores"], data["policy"]
    pcts = {}
    pcts["quizzes"], best = quiz_pct(s["quizzes"], p["quizzes"])
    pcts["assignments"] = sum(s["assignments"]) / (len(s["assignments"]) * p["assignments"]["out_of"]) * 100
    pcts["midterm"] = s["midterm"] / p["midterm"]["out_of"] * 100
    pcts["project"] = s["project"] / p["project"]["out_of"] * 100
    pcts["final"] = None if s["final"] is None else s["final"] / p["final"]["out_of"] * 100
    return pcts, best


def weighted_current(pcts, policy):
    """Grade on COMPLETED work only (ignore ungraded final): normalise by completed weight."""
    done = [(k, policy[k]["weight"]) for k in ("quizzes", "assignments", "midterm", "project")]
    earned = sum(pcts[k] * w for k, w in done)
    total_w = sum(w for _, w in done)
    return earned / total_w, total_w


def required_final(pcts, policy, rules, target):
    """
    Return (needed_final_pct, replacement_applied).
    Rule: if Final% > Midterm%, midterm's weight moves to the final.
    We solve both scenarios and return the one that is self-consistent and best
    for the student.
    """
    qw, aw = policy["quizzes"]["weight"], policy["assignments"]["weight"]
    mw, pw = policy["midterm"]["weight"], policy["project"]["weight"]
    fw = policy["final"]["weight"]
    mid = pcts["midterm"]

    base_ex_mid = (pcts["quizzes"] * qw + pcts["assignments"] * aw + pcts["project"] * pw) / 100
    base_in_mid = base_ex_mid + (mid * mw) / 100

    # Scenario A — no replacement: final keeps weight fw, midterm counts.
    need_a = (target - base_in_mid) / (fw / 100)
    # Scenario B — replacement: final absorbs midterm weight, midterm dropped.
    need_b = (target - base_ex_mid) / ((fw + mw) / 100)

    if rules.get("final_replaces_midterm_if_higher"):
        # Replacement is valid only when the resulting final % actually exceeds midterm.
        if need_b > mid:            # student benefits and rule is consistent
            return need_b, True
        if need_a <= mid:           # final wouldn't beat midterm anyway -> no replacement
            return need_a, False
        # edge: need_a>mid but need_b<=mid -> replacement not triggered by need_b; use need_a
        return need_a, False
    return need_a, False


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "grades_data.json"
    data = json.load(open(path, encoding="utf-8"))
    policy, scale, rules = data["policy"], data["grading_scale"], data["special_rules"]
    pcts, best_quizzes = category_percents(data)

    print("=" * 60)
    print(f" WHAT'S MY GRADE, REALLY  —  {data['course']}")
    print(f" {data['semester']} · {data['institution']}")
    print("=" * 60)

    print("\n CATEGORY BREAKDOWN (after your teacher's rules)")
    print(" " + "-" * 56)
    print(f"   Quizzes      {pcts['quizzes']:6.2f}%   (best {len(best_quizzes)} of "
          f"{len(data['scores']['quizzes'])}, dropped lowest; kept {best_quizzes})")
    print(f"   Assignments  {pcts['assignments']:6.2f}%   (weight {policy['assignments']['weight']}%)")
    print(f"   Midterm      {pcts['midterm']:6.2f}%   (weight {policy['midterm']['weight']}%)")
    print(f"   Project      {pcts['project']:6.2f}%   (weight {policy['project']['weight']}%)")
    fin = "not taken yet" if pcts["final"] is None else f"{pcts['final']:.2f}%"
    print(f"   Final        {fin}   (weight {policy['final']['weight']}%)")

    current, done_w = weighted_current(pcts, policy)
    print("\n CURRENT STANDING (on completed work only)")
    print(" " + "-" * 56)
    print(f"   {current:.2f}%   ->  grade {letter(scale, current)}   "
          f"({done_w}% of the course is graded so far)")

    target = data["target_grade_percent"]
    tletter = letter(scale, target)
    print(f"\n FINAL EXAM TARGET  (to reach {target:.0f}% = grade {tletter})")
    print(" " + "-" * 56)
    need, replaced = required_final(pcts, policy, rules, target)
    if need <= 0:
        print(f"   You've already secured {tletter}. Even 0% on the final keeps it.")
    elif need > 100:
        print(f"   Not reachable: would need {need:.2f}% on the final (>100).")
        print(f"   Aim for the next grade down instead.")
    else:
        print(f"   You need  {need:.2f}%  on the final exam.")
    if replaced:
        print("   NOTE: Replacement rule APPLIES — your final (>{:.0f}% midterm) absorbs".format(pcts["midterm"]))
        print(f"         the midterm's {policy['midterm']['weight']}% weight, lowering the bar.")
        # show what it would have been without the rule
        need_no, _ = (required_final(pcts, policy, {"final_replaces_midterm_if_higher": False}, target))
        print(f"         Without the rule you'd have needed {need_no:.2f}%.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
