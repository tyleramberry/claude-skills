---
title: Skill — MSB 380 Reflection
created: 2026-09-25
updated: 2026-09-25
type: skill
tags: [skill, school, byu, msb-380]
---

# Skill: MSB 380 Reflection

Draft the graded weekly reflection for MSB 380-003 Executive Lectures from that
week's lecture note, and write it into the note's reflection section.

## Trigger
- Hermes cron `msb380-reflection` — **Wednesdays 1:00pm America/Denver**
- "write my MSB 380 reflection", "reflect on today's lecture"

## Inputs
- `/Users/tyleramberry/second-brain` (workdir)
- `projects/byu-strategy/notes/MSB380/MM-DD-speaker-slug.md` — today's note
- Course hub: [[projects/byu-strategy/courses/MSB380]] · Board: [[DEADLINES]]

## Prompt being answered (Canvas, weekly)
> Two-paragraph reflection, ≥250 words: *What is something meaningful you learned
> from this week's speaker? Why was it personally meaningful to you?*

**Length target (Tyler, set 2026-09-30): ~250 words TOTAL across both paragraphs.**
The ≥250 in the Canvas prompt is the floor *and* the target — not a number to exceed.
Aim **250–270**, hard ceiling **275**. Overshooting is a defect, not a bonus: the
2026-09-30 run shipped a 455-word draft and Tyler had to trim it by hand.

## Procedure
1. `date +%F`, `date +%m-%d` → today's local date.
2. Find today's note by filename `MM-DD-*` (skip `_template.md`).
   - No note for today → report it and stop (never draft from a stale note).
   - Reflection section already filled → say so and stop (don't overwrite Tyler's writing).
3. Read the note in full. At most one previous note for continuity.
4. Draft **2 paragraphs, ~250 words total** (aim 250–270, hard ceiling 275, roughly even halves):
   - Para 1 `**What I learned:**` — the concrete lesson, anchored in the speaker name,
     company, stories, numbers and quotes from his own notes.
   - Para 2 `**Why it was personally meaningful:**` — connect to Utah Valley Yards /
     Streak Brands, Brooklyn and marriage, LDS faith, PM/strategy goals.
5. Voice: first person, past tense, plain and warm; concrete over abstract.
   No invented anecdotes, quotes, dates or numbers. No AI-isms. Thin notes → flag the
   gap instead of padding.
6. `patch` the note — replace only the placeholder under
   `## Reflection draft (2 paragraphs, ≥250 words)`. Takeaways / Notes / Questions untouched.
7. `wc -w` (labels stripped) must land in **250–270** — verify with a tool. Short → add real detail
   and re-count. Long (>275) → cut restated quotes, repeated ideas and generic closers, then re-count;
   never ship over the ceiling just because it clears the ≥250 floor.
8. Don't tick checkboxes, don't edit `DEADLINES.md`.
9. Append a one-line `log.md` entry.
10. Return the draft + note path + word count.

## Calibration
`projects/byu-strategy/notes/MSB380/09-23-dean-madrian.md` is the reference for tone, length and specificity —
that draft (~265 words) is the length to match, not to exceed.

## Related
- [[skills/class-notes]]
- [[jobs/msb380-reflection]]
- [[projects/byu-strategy/courses/MSB380]]
