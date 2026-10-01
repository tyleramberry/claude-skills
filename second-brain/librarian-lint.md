---
title: Librarian Lint
created: 2026-08-11
updated: 2026-08-11
type: skill
tags: [skill, hygiene]
---

# Skill: Librarian Lint

## Trigger
User: "lint the library" / "hygiene"; weekly job; after large ingest.

## Checks
1. Orphans — pages with no inbound wikilinks
2. Broken `[[wikilinks]]`
3. Index completeness vs filesystem
4. Frontmatter required fields on people/projects/wiki/*
5. Tags not in SCHEMA taxonomy
6. Pages >200 lines
7. `contested: true` / contradictions queue
8. Stale pages (updated >90d and still "active" topics) — soft flag
9. raw/ immutability note (flag if body edited without new ingest)

## Procedure
1. Scan with `search_files` / small Python via `execute_code` or `terminal`
2. Write report `hygiene/lint-YYYY-MM-DD.md` severity-grouped
3. Append open contradictions to `hygiene/contradictions.md`
4. Fix **safe auto-fixes only**: missing index entries, obvious broken link typos you can prove
5. Do NOT mass-delete or invent resolutions for contested facts
6. Update `log.md`

## Done when
Report filed; user gets top 5 issues.
