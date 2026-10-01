# Fathom API — meetings endpoint reference

Base: `GET https://api.fathom.ai/external/v1/meetings`
Auth: header `X-Api-Key: <FATHOM_API_KEY>` (or `Authorization: Bearer <token>`)

Handled for you by `scripts/fathom_meetings.py` — read this file only if you
need a field the script doesn't already expose, or you're calling the API
by hand.

## Query params
- `created_after`, `created_before` — ISO 8601 timestamps, e.g. `2026-09-02T00:00:00Z`
- `include_summary`, `include_action_items` — booleans; the script always sends both as `true`
- `recorded_by[]` — filter by recorder email (repeatable)
- `teams[]` — filter by team name (repeatable)
- `calendar_invitees[]` — filter by invitee email (repeatable)
- `meeting_type` — filter by meeting type name
- `cursor` — pagination cursor (the script follows `next_cursor` automatically)

This skill never requests `include_transcript`, `include_highlights`, or
`include_crm_matches` — it only pulls meeting notes (summary + action
items), not raw transcripts.

## Response shape
`{ "items": [...], "next_cursor": ..., "limit": ... }`

Each item (meeting):
- `title`, `meeting_title` — display / calendar event title
- `recording_id`, `url`, `share_url`, `meeting_url`
- `created_at`, `scheduled_start_time`, `scheduled_end_time`
- `recording_start_time`, `recording_end_time` — use these (not scheduled_*) for actual duration
- `recorded_by` — `{name, email, email_domain, team}`
- `calendar_invitees` — array of `{name, email, email_domain, is_external, matched_speaker_display_name}`
  - `matched_speaker_display_name` is null when an invitee didn't actually speak/attend
- `default_summary` — `{template_name, markdown_formatted}` — has Meeting Purpose / Key Takeaways / Topics / Next Steps sections, with `fathom.video` deep links per bullet
- `action_items` — array of `{description, user_generated, completed, recording_timestamp, recording_playback_url, assignee: {name, email, team}}`

## Gotchas
- Title matching should be loose (case-insensitive substring) since recurring meeting titles can drift ("Daily Check in" vs "Daily Check-in" vs "Daily Standup").
- `assignee.email` is how to tell which action items are Tyler's (`tyler@streakadvisors.com`) vs. someone else's.
