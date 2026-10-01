---
title: Monthly Budget Session
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, finance]
---

# Skill: Monthly Budget Session

## Trigger
`finance-monthly-session-reminder` scheduled task (nudge only — this skill itself runs when Tyler
confirms), or "let's do our money date", "monthly budget session", "money date."

This is a live, conversational interview with Tyler and Brooklyn together — not a batch job. Take
it slow, one section at a time, and never fill in a number they haven't stated.

## Inputs (read first)
1. `context/finances.md`, `projects/household-money/README.md`
2. `projects/household-money/BUCKETS.md`, `RULES.md`, `GOALS.md`, `CONTACTS.md`
3. Last month's `projects/household-money/budgets/YYYY-MM.md` (if it exists) — this month's
   starting point is last month's plan, not a blank page
4. `data/finances/transactions.csv` — last month's actuals, already categorized

## Procedure

### 0. Ingest first
Run [[skills/transaction-ingest]] so the interview is grounded in real, current data.

### 1. Structure (first session only)
If `projects/household-money/MONEY-DATE.md` still has blanks in its "Structure" and "Accounts
map" sections, walk through those first (money structure, who's CFO, accounts map). Once
answered, those don't need to be re-asked in future sessions — check what's already filled before
asking again.

### 2. Income (every session — it's irregular)
Ask for last month's actual take-home by source. All of it is 1099/self-employment income, none
withheld at the source:
- UVY Venmo revenue — Tyler (gross, fully integrated into household income per `context/finances.md`; UVY's own costs are a separate `UVY Expenses` bucket, not netted out here)
- Frosted (Brooklyn's cake business) Venmo revenue — Brooklyn (same treatment: gross counts as income, costs are the `Frosted Expenses` bucket)
- Mercury 1099 role ($30/hr, biweekly) — Tyler
- Brooklyn's administration job (1099/contract, confirmed via W-9)
- Any other personal Venmo activity not already counted above
- Anything irregular/one-time

Cross-check against what actually landed in `data/finances/transactions.csv` for that source/
month if it's ingested — flag if their stated number and the ledger disagree by a lot, don't
silently trust one over the other.

### 3. Bucket discovery
Show last month's spend grouped by bucket (from the ledger) **and** anything in
`NEEDS-BUCKETS.md` (uncategorized spend) — this is real evidence of what buckets they actually
need, better than guessing from scratch. For each:
- Confirm existing buckets still make sense (rename/merge/split as they want)
- Ask about new recurring goals: emergency fund (if not already a bucket — always propose one),
  house/vacation/other savings goals, debt payoff, self-employment tax set-aside (always propose
  this one too, given 100% 1099 income)
- Write the final list to `projects/household-money/BUCKETS.md`

### 4. Allocate this month's $
Propose a $ per bucket based on: income actually received this cycle + each bucket's stated
priority (must-fund first). Show the math, let them adjust live. Write the result to
`projects/household-money/budgets/YYYY-MM.md` using exactly this shape (weekly_report.py and
affordability.py parse these headings/columns literally):

```markdown
---
title: Budget — YYYY-MM
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: budget
tags: [finance, budget]
month: YYYY-MM
---

# Budget — <Month> <Year>

## Income
| Source | Who | Amount |
|---|---|---|
| UVY Venmo revenue (gross) | Tyler | |
| Frosted Venmo revenue (gross) | Brooklyn | |
| Mercury 1099 (30/hr) | Tyler | |
| Administration job (1099) | Brooklyn | |
| Other personal Venmo | Tyler/Brooklyn | |

## Buckets
| Bucket | Monthly Target | Notes |
|---|---|---|
| UVY Expenses | | mulch/materials/subcontractor costs |
| Frosted Expenses | | baking supplies/business costs |
| ... | | |
| Self-Employment Tax Set-Aside | | ~X% of 1099 income |
| Emergency Fund | | target: N months fixed expenses |

## Fixed Bills
| Bill | Amount | Due Day | Bucket |
|---|---|---|---|
| ... | | | |
```

### 5. Emergency fund + goals
Update `projects/household-money/GOALS.md`: emergency fund target (ask for N months if not set),
current progress (from ledger, not a guess), and any savings/debt goals — progress computed from
actual bucket funding, not estimated.

### 6. Bill calendar
Run [[skills/bill-calendar-sync]] with this month's Fixed Bills table.

### 7. Subscription audit
Run [[skills/subscription-audit]].

### 8. Regenerate the dashboard
Run `python3 scripts/finance/render_dashboard.py` — rewrites
`projects/household-money/DASHBOARD.md`. Tell them to open/refresh that note in Obsidian to see
it. (Retired 2026-08-17: no more localhost web server — second-brain lives in Obsidian now, so
the dashboard is a plain markdown note read there, not a separate app.)

### 9. Close out
- Update `context/finances.md` if the household's rules/philosophy changed
- Append `wiki/finances-log.md` and `log.md`
- Say what changed vs. last month in plain language, not just "budget saved"

## Done when
- `budgets/YYYY-MM.md` exists with real numbers (or explicit blanks where they said "not sure yet")
- `BUCKETS.md`, `GOALS.md` reflect the conversation
- Bill calendar + subscription audit both ran
- `projects/household-money/DASHBOARD.md` regenerated
- `wiki/finances-log.md` and `log.md` updated
