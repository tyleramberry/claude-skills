---
title: Subscription Audit
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, finance]
---

# Skill: Subscription Audit

## Trigger
Runs automatically as part of `monthly-budget-session`. Also on-demand: "find our subscriptions",
"what are we paying for that we don't use", "money leak check."

## Procedure
1. `cd /Users/tyleramberry/second-brain`
2. Run `python3 scripts/finance/subscription_scan.py`. It rewrites
   `projects/household-money/SUBSCRIPTIONS.md` and prints three categories:
   - **New** recurring charges never seen before — need a keep/cancel decision from Tyler/Brooklyn.
   - **Price changes** — a subscription's amount crept up since last recorded.
   - **Leak** — anything marked `cancelled` or `unused` in `SUBSCRIPTIONS.md` that is still
     charging. This is the actual "money we didn't realize we're spending" case — call it out
     clearly, it's the highest-value flag this skill produces.
3. Ask Tyler/Brooklyn to mark a Status (`active` / `unused` / `cancelled`) for anything new. Update
   `SUBSCRIPTIONS.md` directly with their answer rather than leaving it as "needs review."
4. If something is confirmed unused/should-cancel, note it — but do NOT attempt to cancel it
   yourself (no account access, and cancelling a subscription is the kind of outward/irreversible
   action Tyler should do himself).

## Output format
Short: "N new subscriptions found: [...]. M price changes: [...]. LEAK: [merchant] is marked
cancelled but charged $X on [date] — still active somewhere?"

## Done when
- `SUBSCRIPTIONS.md` reflects the latest scan
- Any leak (charging despite marked cancelled/unused) was surfaced explicitly, not buried
