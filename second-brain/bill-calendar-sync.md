---
title: Bill Calendar Sync
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, finance]
---

# Skill: Bill Calendar Sync

## Trigger
Called from `monthly-budget-session` after this month's budget is written. Not run standalone
unless Tyler asks ("sync bills to calendar," "put our bills on the calendar").

## Inputs
- This month's `projects/household-money/budgets/YYYY-MM.md`, "Fixed Bills" table
  (Bill / Amount / Due Day / Bucket)
- Tyler's Google Calendar (already-connected Calendar MCP)

## Procedure
1. For each fixed bill with a Due Day, compute this month's actual due date.
2. **First time ever running this skill:** list every event it wants to create (bill name, amount,
   date) and ask Tyler/Brooklyn to confirm before creating anything — this writes to a real,
   shared calendar. Record the answer in `projects/household-money/README.md` (a line noting
   "bill calendar sync: confirmed auto-create on <date>" or "confirmed ask-each-time").
3. If auto-create was confirmed: create/update one all-day (or short) Calendar event per bill,
   titled `Bill due: <name> ($<amount>)`, on the due date. Check for an existing event with the
   same title on that date first (search before creating) so re-running a given month doesn't
   duplicate events.
4. If ask-each-time was chosen: present the list each month and only create the ones Tyler/Brooklyn
   say yes to.
5. Skip any bill whose due date already passed this month (don't create backdated events).

## Done when
- Every current-month fixed bill either has a matching Calendar event or was explicitly declined
- No duplicate events created for a bill/date pair already on the calendar
