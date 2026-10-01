---
title: Canvas Radar
created: 2026-09-09
updated: 2026-09-09
type: skill
tags: [skill, school, byu, canvas, cron]
---

# Skill: Canvas Radar

Daily pull of Canvas assignments + announcements across Tyler's active courses, diffed
against the last run so only genuinely **new or changed** items surface. This is the
live source of truth that feeds the morning brief's School section.

## Trigger
- Hermes cron `canvas-radar` (daily ~6:30am America/Denver)
- User says "canvas radar" / "what's new in canvas" / "any new assignments"

## Procedure
1. `cd /Users/tyleramberry/second-brain`
2. Run `python3 scripts/canvas/radar.py`. Read its stdout summary line (counts) + the
   `NEW` / `CHANGED` / `ANN` bullets it prints.
3. Read `projects/byu-strategy/canvas-radar/latest.md` — this is the authoritative digest
   (due-in-7-days and due-in-8-14-days tables + new/changed/announcement lists).
4. Compose a **short** message (delivery is to origin chat every day, so keep it tight):
   - Lead with what's **new/changed** (if anything) — that's the whole point.
   - Then a compact "due next 7 days" list (course + item + day), max ~7 lines.
   - If the 8–14 day window has a heavy item (a Case Submission, sprint, midterm, ≥100pts),
     flag it one line.
   - If nothing new/changed, say exactly that in one line and skip the rest.
5. If a due date conflicts with `projects/byu-strategy/DEADLINES.md`, fix DEADLINES.md
   (Canvas is live truth; the board is hand-maintained).
6. Append `log.md`: `## [date] job | canvas-radar` + one-line summary (n new, n changed).

## Output format
```
# Canvas — YYYY-MM-DD

## New / changed
- (item or "none")

## Due next 7 days
- COURSE — item (day)

## Worth a look (8–14d)
- (only heavy items)
```

## Done when
- `scripts/canvas/radar.py` ran without crashing and updated
  `projects/byu-strategy/canvas-radar/latest.md` + `data/canvas/state.json`
- Tyler got a short message: new/changed items first, then the near-term due list
- `log.md` updated

## Notes / pitfalls
- First run seeds the baseline: everything shows "NEW" once, then only real changes after.
  If a run shows a huge NEW list and `data/canvas/state.json` was just created, say
  "baseline pulled — N assignments on record" instead of dumping all of them.
- `due_at` is UTC; the script already converts to America/Denver. Don't re-convert.
- "no due date" items (In-Class Participation, Class Participation Policy, Guest Speaker
  Question) are legitimate — they have `due_at = null`. Don't flag them as missing data.
- STRAT 402 has ~30 reading quizzes; don't enumerate them all in chat — summarize the
  window ("2 quizzes + 1 exercise this week").
