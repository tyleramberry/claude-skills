---
title: Weekly Money Check-In
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, finance]
---

# Skill: Weekly Money Check-In

## Trigger
Sunday-evening scheduled task (`finance-weekly-checkin`), or "how are we doing this week" /
"weekly check-in" / "are we on track."

## Inputs
1. `context/finances.md` — quick orient (household scope, UVY rule, 1099 tax-set-aside note)
2. Current month's `projects/household-money/budgets/YYYY-MM.md` — if it doesn't exist yet, stop
   and say "no budget set for this month — run the monthly session first," don't invent targets.
3. `data/finances/transactions.csv`

## Procedure
1. `cd /Users/tyleramberry/second-brain`
2. Run [[skills/transaction-ingest]] first (pick up anything dropped since last check-in).
3. Run `python3 scripts/finance/weekly_report.py` (defaults to the current month). Read its full
   output: bucket pace, over-pace/overspent flags, size anomalies, 14-day bill calendar.
4. Turn the raw numbers into 1-2 concrete, specific corrections — not generic advice. E.g. "Dining
   is $180 over pace with 12 days left — either hold off on eating out this week or move $180
   from a flexible bucket." Never invent a number not in the script's output.
5. If `projects/household-money/NEEDS-BUCKETS.md` has rows, ask about the top 1-2 by $ amount so
   the ledger keeps getting smarter — don't dump the whole list every week.
6. Write the full check-in to `logs/finance-checkins/YYYY-MM-DD.md`.
7. Append a dated bullet to `wiki/finances-log.md` under the current month's entry (create the
   month's entry if this is its first check-in) — short summary + link to the full check-in file.
8. Append `log.md`: `## [date] job | weekly-money-check-in` with a one-line summary.
9. Deliver the check-in to the user (chat or scheduled-task delivery).

## Output format
```
# Weekly Check-In — YYYY-MM-DD

## Pace
(bucket-by-bucket, only call out ones that need attention — don't list every bucket as "fine")

## Corrections to make this week
(1-2 specific, numeric)

## Watch
(any size anomalies, any bill due in the next 14 days not yet seen paid)

## Needs a decision
(top unmatched merchants, if any)
```

## Done when
- `logs/finance-checkins/YYYY-MM-DD.md` written
- `wiki/finances-log.md` and `log.md` updated
- User received a specific, numeric, skimmable check-in — not a vague "looking good"
