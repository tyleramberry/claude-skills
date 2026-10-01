---
title: Quarterly Review
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, finance]
---

# Skill: Quarterly Review

## Trigger
`finance-quarterly-review` scheduled task (1st of Jan/Apr/Jul/Oct), or "quarterly review" /
"how's the quarter looked."

## Procedure
1. `cd /Users/tyleramberry/second-brain`
2. Run [[skills/transaction-ingest]] first.
3. Read the last 3 months of `projects/household-money/budgets/YYYY-MM.md` files and the matching
   slice of `data/finances/transactions.csv` (by month prefix). If fewer than 3 months of budgets
   exist yet, say so and review whatever exists — don't backfill or estimate missing months.
4. For each bucket that existed across the quarter, compute: total spent vs. total target,
   trend (getting better/worse/flat). Use simple arithmetic on the already-categorized ledger —
   no new script needed for this; if the comparison logic gets reused a third time, promote it to
   a `scripts/finance/` script per the second brain's latent-vs-deterministic rule.
5. Report on the **Self-Employment Tax Set-Aside** bucket specifically: total set aside this
   quarter, and flag this as the natural moment to actually make the estimated tax payment
   (federal quarterly estimated tax deadlines: mid-Jan, mid-Apr, mid-Jun, mid-Sep — note the
   closest one, but don't give personalized tax advice beyond "here's what's set aside").
6. Report on Emergency Fund and any other goals in `projects/household-money/GOALS.md`: progress
   this quarter, on pace for target date or not.
7. Write the review to `logs/finance-checkins/quarterly-YYYY-Q#.md`.
8. Append a summary to `wiki/finances-log.md` and `log.md`.

## Output format
```
# Quarterly Review — YYYY Q#

## Bucket trends
(3-month totals vs targets, trend direction)

## Self-employment tax set-aside
(total set aside, nearest estimated-tax deadline)

## Goals progress
(emergency fund, savings goals, debt if any)

## One thing to change next quarter
```

## Done when
- Review file written under `logs/finance-checkins/`
- `wiki/finances-log.md` and `log.md` updated
- Tax set-aside total and nearest deadline explicitly stated
