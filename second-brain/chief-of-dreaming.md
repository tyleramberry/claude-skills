---
title: Chief of Dreaming
created: 2026-08-14
updated: 2026-08-14
type: skill
tags: [skill, brief, hygiene]
---

# Skill: Chief of Dreaming

Evening agent. Two jobs, in order:

1. **Librarian** — notice what landed in the vault today, file/index it, flag mess
2. **Dreamer** — from *his* context, propose smart uses, ideas, and next moves

Not the 7am newspaper (deadlines/habits/UVY flags). This is “what changed + what’s worth imagining.”

## Trigger
5pm cron, or user says "chief of dreaming" / "dreaming brief" / "file my inbox".

## Inputs (read)
1. `AGENTS.md`, `SCHEMA.md` (skim), `context/about-me.md`, `context/business.md`
2. `index.md` + tail of `log.md` (~30 lines)
3. `inbox/` — drop zone (anything here is unfiled)
4. New or unindexed files under `people/`, `projects/`, `wiki/`, `raw/`, `projects/byu-strategy/` (especially `syllabi/raw/`, `notes/`)
5. `wiki/business-ideas.md`, `projects/ai-venture-2026.md`, `projects/byu-strategy/DEADLINES.md`
6. Yesterday’s dreaming brief if present: `logs/dreaming-briefs/`
7. `hygiene/contradictions.md`

## Librarian procedure
1. List `inbox/` (skip `.gitkeep` / README). For each real file:
   - Infer type: syllabus → `projects/byu-strategy/syllabi/raw/`; lecture dump → `notes/COURSE/`; article → `raw/articles/`; person notes → `people/`; otherwise ask via brief “where should X live?” and leave in inbox
   - If destination is obvious, **move** it, add frontmatter if markdown, add `index.md` + `log.md` entries
   - Never invent titles/dates; use filename + today
2. Scan for orphans / missing index / new notes without `[[course]]` links — safe auto-fix index gaps only
3. If a new syllabus PDF landed in `syllabi/raw/` and no matching `syllabi/extracted/`, note it as **ingest next** (do a full ingest only if the file is markdown/text and small enough; don’t stall the brief on a 50-page PDF)
4. Write a short hygiene note into the brief (not a full lint report unless the vault is messy)

## Dreamer procedure
Using only library facts (no invented revenue, health, or grades):

Propose **3–5** items, each one of:
- **Use case** — a way Tyler should use the vault this week he isn’t yet
- **Idea** — venture / UVY / 341 product spark; if it meets SCHEMA threshold, append `wiki/business-ideas.md`
- **Smart move** — sequenced action given school + UVY + household + empty logs
- **Connection** — two existing pages that should talk to each other

Rules:
- Specific to *his* files and calendar, not generic founder Twitter
- Prefer one idea that compounds MSB 341 + UVY + venture over three random apps
- If logs are still empty, dream smaller: “capture X” not “scale a SaaS”
- Do not repeat yesterday’s top item unless still undone and still the highest leverage

## Output
Write `logs/dreaming-briefs/YYYY-MM-DD.md` and deliver the same markdown.

```
# Chief of Dreaming — YYYY-MM-DD

## Filed today
- (moves / index updates, or “inbox empty”)

## Library health
- (2–5 bullets: orphans, uningested syllabi, missing numbers)

## Dreams
### 1. …
Why it fits your vault: …
Do this next: …

### 2. …

## Open questions for you
- (only if a file couldn’t be filed safely)
```

## Done when
- Brief file written
- `log.md` appended: `## [date] job | chief-of-dreaming`
- Inbox items that were obvious are moved
- Substantial new ideas logged to `wiki/business-ideas.md`

## Never
- Invent private facts
- Delete user files
- Overwrite `raw/` bodies
- Duplicate the 7am brief’s format
