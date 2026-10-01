---
name: fathom-meeting
description: Pull meeting notes (summary + action items) from the Fathom API (api.fathom.ai) — Tyler's meetings are recorded there, and this is the way to check what happened in one without him having to open Fathom himself. Trigger this whenever Tyler asks about a recent meeting, the "daily check-in," a "check-in call," what happened on a call, meeting notes, meeting summary, or action items from a meeting — even if he doesn't say "Fathom" by name. Also trigger on "/fathom-meeting", "poll Fathom", or "check Fathom". Don't trigger for meetings tracked elsewhere (Slack huddles, Google Meet notes already pasted in, Zoom) unless Fathom is the source he names.
---

# Fathom Meeting

Tyler's team (Streak Advisors) records meetings with Fathom. This skill
pulls a meeting's notes from the Fathom API — nothing more. It doesn't
search transcripts, check attendance, or answer "was I mentioned"; if Tyler
asks something like that, tell him this skill only pulls notes and doesn't
have transcript-level detail.

## Setup

The Fathom API key (`FATHOM_API_KEY`) lives in `~/second-brain/.env`. Never
print its value — the bundled script reads it directly from that file.
If it's missing from there, ask Tyler where his current Fathom API key is
kept and pass `--env-path` accordingly.

## 1. Figure out which meeting

Default ask is "yesterday's daily check-in" — but handle whatever Tyler
actually asks for (a specific date, "last Monday's," "the call with
[client]," a date range, "this week's check-ins").

- Compute the date window relative to **today's actual date** (check the
  environment/system date — don't assume). For a single day, query a
  padded UTC window: that day's start-of-day to the *next* day's
  start-of-day, e.g. for Sept 3: `--after 2026-09-02T00:00:00Z --before
  2026-09-05T00:00:00Z` (pad a day on each side — a meeting's `created_at`
  can land just outside a tight midnight-to-midnight window depending on
  timezone).
- Fetch with the bundled script (always pulls summary + action items):
  ```
  python3 ~/.claude/skills/fathom-meeting/scripts/fathom_meetings.py \
    --after 2026-09-02T00:00:00Z --before 2026-09-05T00:00:00Z \
    --out /tmp/fathom_meetings.json
  ```
- Match the meeting by title (case-insensitive substring — "daily check
  in", "check-in", etc., since recurring titles drift). If more than one
  meeting matches, or none do, show Tyler what came back in that window
  and ask which one he means rather than guessing.
- See `references/api.md` for the full parameter/response reference if
  you need something the script doesn't already surface (team filters,
  specific recorder, etc).

## 2. Report — always these three sections, in this order

Report in chat (not a file, unless Tyler asks for one). Every response
from this skill takes this exact shape:

**Brief overview** — a couple sentences on what the meeting was about,
drawn from `default_summary`'s Meeting Purpose / Key Takeaways. Just
enough for Tyler to place the meeting without reading the whole thing.

**Actions for the whole meeting** — every item in `action_items`, as a
table of owner → description. This is the full list regardless of who's
assigned — everyone's action items, not just Tyler's.

**Detailed look at what Tyler needs to do** — filter `action_items` down
to the ones assigned to Tyler (`assignee.email` = `tyler@streakadvisors.com`,
or name match on "Tyler"), and expand each with whatever detail the notes
give (the description, plus anything relevant from the summary's Topics/
Next Steps sections that fills in context). If nothing in the notes is
assigned to Tyler, say that plainly — don't stretch someone else's task
into his or invent one.

## Notes

- If nothing matches in the requested window, say so plainly — don't
  invent a meeting or a summary that didn't come back from the API.
- Meeting titles, action items, and summary text must come from the API
  response, not from memory of past invocations — always poll fresh.
- This skill's scope stops at meeting notes. It doesn't fetch or search
  transcripts, check who attended vs. was just invited, or dig into
  duration/scheduling detail — if Tyler wants that, that's a different
  ask outside what this skill does.
