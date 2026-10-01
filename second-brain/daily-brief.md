---
title: Daily Brief
created: 2026-08-11
updated: 2026-08-11
type: skill
tags: [skill, brief]
---

# Skill: Daily Brief

## Trigger
Morning job, or user says "daily brief" / "my brief" / "morning brief".

## Inputs (read)
1. `context/about-me.md`, `context/business.md` (quick orient)
2. `wiki/business-ideas.md` — revisit one idea OR propose one new from patterns
3. `wiki/ai-developments.md` — one relevant AI development
4. `wiki/lifestyle-log.md` — streaks / at-risk habits
5. `wiki/finances-log.md` — only if something worth flagging
6. `wiki/utah-valley-yards.md` — only if attention needed
7. `projects/byu-strategy/DEADLINES.md` + course pages — school deadlines
8. Last 15 lines of `log.md`

Optional live pulls (if connections live): see `connections/sources.md`.

## Procedure
1. Orient from context + index
2. Draft short newspaper sections (skip empty sections)
3. If you surface a **new** idea or AI development, also append it to the source wiki log
4. Write full markdown to `logs/daily-briefs/YYYY-MM-DD.md`
5. Append `log.md`: `## [date] job | daily-brief`
6. Deliver the brief to the user (chat / cron delivery)

## Output format
```
# Daily Brief — YYYY-MM-DD

## Business Idea
...

## AI Development
...

## Health & Habits
...

## Finances
(only if needed)

## Utah Valley Yards
(only if needed)

## School
(only if needed)

## Open loops
(1-3 bullets Tyler should act on)
```

## Done when
- File exists under `logs/daily-briefs/`
- log.md updated
- User received skimmable brief (printable plain markdown)
