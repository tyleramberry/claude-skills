---
title: Skillify
created: 2026-08-11
updated: 2026-08-11
type: skill
tags: [skill]
---

# Skill: Skillify

## Trigger
End of a non-trivial task; user says "skillify"; or agent notices a task done twice.

## Doctrine
If you have to ask for something twice, you failed. Capture procedures into owned skill files under `skills/`.

## Procedure
1. Summarize what was done (goal, inputs, steps, tools, pitfalls, definition of done)
2. Check `skills/` and `index.md` for an existing skill to extend
3. Write or patch `skills/<name>.md` with:
   - Trigger
   - Inputs
   - Numbered procedure
   - Pitfalls
   - Done when
4. Add to `index.md` Skills section if new
5. Append `log.md`
6. Tell user the skill path and one-line trigger

## Naming
lowercase-hyphen, verb-oriented: `expense-report.md`, `uvy-weekly-status.md`

## Done when
Reusable skill file exists and is indexed.
