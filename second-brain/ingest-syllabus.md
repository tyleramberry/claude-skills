---
title: Ingest Syllabus
created: 2026-08-11
updated: 2026-08-11
type: skill
tags: [skill, school, byu]
---

# Skill: Ingest Syllabus

## Trigger
"Ingest syllabus", "parse this syllabus", drop PDF in `projects/byu-strategy/syllabi/raw/`, "ingest all syllabi".

## Inputs
- Raw file under `projects/byu-strategy/syllabi/raw/COURSE_CODE.*`
- Or pasted text / path user provides

## Procedure
1. Read raw syllabus (PDF via available extract tools / text)
2. Write `projects/byu-strategy/syllabi/extracted/COURSE_CODE.md` with:
   - Course meta (code, title, instructor, time, location, LMS)
   - Grade weights table
   - Assignment list with due dates (best effort)
   - Exam dates
   - Attendance / late / AI-policy notes (quote short)
   - Required texts
   - Office hours
3. Create/update `projects/byu-strategy/courses/COURSE_CODE.md` from `courses/_TEMPLATE.md`
4. Merge all dated items into `projects/byu-strategy/DEADLINES.md` (sorted)
5. Update `projects/byu-strategy/README.md` active courses table
6. Add pages to root `index.md` if new; append root `log.md`
7. Tell Tyler: next 3 deadlines + anything weird (missing dates, conflicting policies)

## Done when
Extracted page + course page + deadlines updated. Never invent due dates — mark `TBD` if unclear.
