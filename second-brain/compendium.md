---
title: Compendium
created: 2026-08-11
updated: 2026-08-11
type: skill
tags: [skill, ai]
---

# Skill: Compendium

Deep research brief owned by the library (deeper than generic web "deep research").

## Trigger
User wants a thorough brief on a person, company, market, or book set; "compendium on X".

## Procedure
1. Clarify scope in one line if ambiguous (default: proceed with best interpretation)
2. Gather sources → save immutable copies under `raw/` (articles/papers/transcripts)
3. Build synthesis page in `wiki/queries/` or `logs/compendiums/`:
   - Executive summary
   - Dated chronology
   - Where sources disagree
   - Best verbatim quotes with citations
   - Top tellable moments (if story/talk use-case)
   - Open questions
4. Create/update entity/concept pages that meet SCHEMA thresholds
5. Cross-link; update index.md + log.md
6. Deliver skimmable brief + paths

## Done when
Raw sources stored, synthesis filed, index updated.
