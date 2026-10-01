---
title: Cost Discipline
created: 2026-08-17
updated: 2026-08-17
type: skill
tags: [skill, hermes, cost]
---

# Skill: Cost Discipline

## Trigger
Resuming a long Hermes chat; `[cost-nudge]` in context; Tyler says save money / cheaper model / don't run up the bill; starting a new job inside an old thread.

## Inputs
- Current session size (tokens / message count) if known
- Whether the request is a **new job** or a continuation

## Procedure
1. New job + fat thread → ask for `/new` (or ignore old transcript and go to files)
2. Search the library, read one page — do not walk `~/second-brain`
3. Routine work on `grok-4.3`; hard reasoning stays `grok-4.6`. Don't swap models mid-chat (breaks cache)
4. No browser / vision / delegate unless the job needs them
5. Write durable notes to disk; don't keep the thread alive to remember

## Pitfalls
- Idle chats cost $0. The bill is the next message into a huge history
- Mid-chat toolset/skill/system-prompt changes bust the 88% cache-hit rate
- Crons are already pinned to `grok-4.3` — leave them

## Done when
Work continues in a cheap session (new chat or no vault re-read), and the answer still lands in `~/second-brain` if it should persist.
