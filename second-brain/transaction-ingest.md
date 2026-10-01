---
title: Transaction Ingest
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, finance]
---

# Skill: Transaction Ingest

## Trigger
"close the month", "I dropped statements", "ingest transactions" — or automatically as the first
step of `weekly-money-check-in` and `monthly-budget-session` (always pick up new drops before
reporting on them).

## Procedure
1. `cd /Users/tyleramberry/second-brain`
2. Run `python3 scripts/finance/ingest.py`. Read its output: how many new transactions, how many
   need manual review.
3. If anything landed in `data/finances/needs_review.md`, say so plainly — don't silently ignore
   it. Offer to look at the raw rows and help fix the source file if asked.
4. Run `python3 scripts/finance/categorize.py`. Read its output: how many categorized, how many
   still need a bucket.
5. If `projects/household-money/NEEDS-BUCKETS.md` exists and has rows, summarize the top few
   (by $ total) in your reply — these are real spend that isn't in any bucket yet, worth
   surfacing even outside a full check-in.
6. Append one line to `log.md`:
   `## [date] job | transaction-ingest` with counts (new txns, needs-review, needs-bucket).

## Output format
Short: "Ingested N new transactions (M need review). Categorized X, Y still need a bucket:
[top merchants by $]."

## Done when
- `scripts/finance/ingest.py` and `categorize.py` both ran without crashing
- Tyler/Brooklyn have a clear count of what's new and what needs a decision
- `log.md` updated
