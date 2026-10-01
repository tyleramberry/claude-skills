---
title: Study Aid Generator
created: 2026-09-09
updated: 2026-09-09
type: skill
tags: [skill, school, byu, study, on-demand]
---

# Skill: Study Aid Generator

Turn Tyler's lecture notes into active-recall study material — review questions and
flashcards — for a specific course, right before a quiz/exam. On-demand only (cheap),
not a cron.

## Trigger
"make flashcards for MSB 341", "study guide for STRAT 401", "quiz me on X", "review
questions for the midterm".

## Procedure
1. Identify the course code. Confirm once if ambiguous; don't ask if obvious.
2. Read the course page `projects/byu-strategy/courses/<CODE>.md` (grade snapshot, weekly
   rhythm, key deadlines) + the extracted syllabus `projects/byu-strategy/syllabi/extracted/<CODE>.md`
   if present, so questions align with what's actually assessed (quizzes vs sprints vs cases).
3. Read the notes: `projects/byu-strategy/notes/<CODE>/*.md` (and `readings/summaries/`
   if the course has them). If the folder is empty (e.g. MSB341 pre-notes), say so plainly
   and offer to generate from the syllabus/readings instead — don't fabricate lecture content.
4. Generate the study aid to `projects/byu-strategy/exams/<CODE>-study-aid-YYYY-MM-DD.md`:
   - **Recall questions** (facts, definitions, frameworks) — from the notes.
   - **Application questions** (given a scenario/case, what do you do / what framework applies).
   - **Anki-ready cards** in a `Q:: / A::` block (front/back separated by `::`) so Tyler can
     paste straight into Anki.
   - **Predicted quiz/exam questions** — infer from the syllabus grade breakdown what's likely
     tested (e.g. MSB 341 quizzes are chapter-based; STRAT 402 midterms cover specific sessions).
   - A short **"gaps"** section listing anything the notes don't yet cover that the syllabus says
     will be tested (honest, not invented).
5. Use Tyler's note structure (Takeaways / Notes / Questions / Actions) as the source of truth;
   surface his own "Questions" section back as cards to answer.
6. Append `log.md`: `## [date] study-aid | <CODE>`.

## Output format
```markdown
# <CODE> Study Aid — YYYY-MM-DD

## Recall
1. Q...

## Application
1. Scenario: ... → ...

## Anki cards
Q:: <front>
A:: <back>

## Likely on the quiz/exam
- ...

## Gaps (notes don't cover yet)
- ...
```

## Done when
- File written to `projects/byu-strategy/exams/`
- Tyler gets the path + a 1-line summary (N recall, N application, N cards)
- `log.md` updated

## Notes / pitfalls
- Don't invent facts the notes don't contain. If a framework is half-remembered in the notes,
  mark it "(verify in textbook)" rather than completing it from memory.
- Honor-code/AI-policy: this is a study aid from Tyler's own notes, not a graded submission —
  no submission concern, but keep it review material, not answers to a specific live quiz he
  hasn't taken yet.
