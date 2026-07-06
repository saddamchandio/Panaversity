# Prompts used — Money Detective

I acted as the **client**, not the coder. Below are the actual prompts, in order.

## Initial prompt

> I have a CSV of my bank transactions with columns `date, description, amount_pkr`
> covering three months. I don't want a budget going forward — I want to find the
> money leaking out of my past history. Write me a Python script that:
> 1. Finds recurring charges (same merchant + same amount in more than one month).
> 2. Flags likely forgotten subscriptions (gym, cloud storage, streaming, VIP).
> 3. Finds duplicate charges — the exact same charge billed twice.
> 4. Prints my total spend per month so I can check it against my statement.
> Keep it a single file I can re-run every month.

## Improved prompt 1 — make the leak actionable

> Good. Now add a summary at the end that totals the forgotten subscriptions per
> month AND annualised (× 12), and totals how much I can recover from the duplicate
> charges. I want one clear "here's your leak" number.

## Improved prompt 2 — personalise the rules

> The forgotten-subscription detection should use a keyword list I can edit at the
> top of the file, because what counts as "forgotten" is personal to me. Put
> gym, membership, cloud, storage, VIP, premium, and the streaming names in it.

## Improved prompt 3 — explain the logic (per the task)

> Explain in plain English, as comments at the top of the file, exactly how each
> detection works, so I understand what the code is doing before I trust it.

## Verification prompt

> Before I trust anything: print my monthly totals so I can compare them to the
> totals on my real statement. If April says 44,965 and May says 44,646, I'll know
> the parsing is correct and I can trust the rest.
