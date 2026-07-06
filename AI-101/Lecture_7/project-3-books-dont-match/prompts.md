# Prompts used — The Books Don't Match

## Initial prompt (state the target up front)

> I collect monthly cricket-club dues: 12 members, PKR 1,500 each, so I should
> have collected PKR 18,000. I have a messy JazzCash/Easypaisa CSV
> (`date, sender_raw, memo, amount_pkr`). I do NOT want to clean it first.
> Write a Python script that reconciles the payments against the PKR 18,000
> target and tells me the gap.

## Improved prompt 1 — give my interpretation rules

> The records are ambiguous, so here are my personal rules for reading them.
> Put them in an editable JSON config, don't hard-code them:
> - "Chintu" is Bilal Ahmed. "Guddu" is Faizan Ali.
> - Any number containing 4471 is Usman Khan (he never writes a memo).
> - Kashif Iqbal wrote "Eid Mubarak" but that payment is his dues.
> - First-name and "Imran Q" style entries should match the right roster member.

## Improved prompt 2 — handle the tricky cases

> Two things to handle: (a) one member paid in two installments (800 then 700)
> — add them up to 1,500; (b) if a payment can't be matched to anyone on my
> roster, list it separately as an "unmatched deposit" I need to follow up on.

## Improved prompt 3 — name the follow-ups and overpayments

> Output three action lists: who still owes money (with amounts), any
> overpayments to refund, and any unexplained deposits. End with a
> reconciliation check that matched + still-owed equals my expected 18,000.

## Verification prompt

> I already hand-counted that 10 members definitely paid = PKR 15,000. Print the
> total you matched to roster members. If it says 15,000 and the final check
> equals 18,000, I'll trust the gap and the follow-up list.
