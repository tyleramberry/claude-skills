---
title: CFO Text Reply
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, finance]
---

# Skill: CFO Text Reply

## Trigger
Called by the `finance-imessage-listener` scheduled task once per new incoming text from a
configured contact ([[projects/household-money/CONTACTS]]). Can also be invoked directly in chat
if Tyler pastes a question and says "answer this like a text."

## Inputs (per call)
- `sender` (Tyler or Brooklyn), `handle` (their iMessage address), `text` (the question)
- Current month's `projects/household-money/budgets/YYYY-MM.md`
- `data/finances/transactions.csv`

## Procedure
1. `cd /Users/tyleramberry/second-brain`
2. Read the question. Two common shapes:
   - **Affordability** ("can I afford X", "do I have money for X", "is $40 for dinner ok") — pull
     out a bucket name and a dollar amount. If the bucket isn't stated, infer the single most
     likely bucket from the merchant/activity described (e.g. "dinner" → Dining) using
     `projects/household-money/BUCKETS.md`'s bucket list; if genuinely ambiguous between two
     buckets, ask a clarifying question back instead of guessing.
     Run: `python3 scripts/finance/affordability.py --bucket "<bucket>" --amount <amount>`
     Use its `verdict` and `explanation` fields directly — don't recompute the math yourself.
   - **General status** ("how much do we have left for groceries", "are we on track this month")
     — run `python3 scripts/finance/weekly_report.py` and answer from its output.
3. **Never invent a balance or number that isn't in a script's output.** If the script says there's
   no budget for this month, or the bucket doesn't exist, say exactly that — e.g. "We haven't set
   a budget for October yet — want to do the money date?" — don't estimate.
4. Compose a short reply (text-message length, 1-3 sentences, lead with the answer, cite the
   number). Example: "Yes — Dining has $86 left with 9 days to go." or "Tight — that'd leave
   Dining at $6 with a week left. Your call."
5. Send it: `osascript scripts/finance/send_imessage.applescript "<handle>" "<reply text>"`
6. Append one line to `logs/cfo-texts.md` (create if missing): `- YYYY-MM-DD HH:MM <sender>: "<question>" -> "<reply>"`

## Done when
- A reply was sent back via iMessage (or, if data was missing, an honest "I don't have that yet"
  was sent instead of a guess)
- `logs/cfo-texts.md` has the record
