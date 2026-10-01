---
name: upwork-apply
description: Find Upwork jobs that fit Tyler's AI agent / automation / RAG / full-stack AI profile, score them hard, and draft short template-based proposals he approves before anything is submitted. Also runs as a fast "scan" on a schedule that pings him only when a fresh, uncrowded, high-fit job appears. Trigger on "/upwork-apply", "find me Upwork jobs", "find jobs to apply to", "run the Upwork workflow", "what should I apply to on Upwork", "any good Upwork jobs", "apply to jobs", or "scan Upwork". Don't trigger for invitations/offers/messages on existing clients (that's a dashboard check) unless he asks to apply.
---

# Upwork Apply

Find → score (skip most) → draft from a template → Tyler approves → submit
→ log → **learn from his edits** (step 8). The skill improves itself: every
edit Tyler makes to a draft gets saved, diffed, turned into a lesson, and
folded back into the templates, so the next draft needs fewer edits. Nothing is submitted, and no Connects are spent, without an explicit
"yes" from Tyler on that specific proposal.

Account: freelancer `org_uid = 2099564090365424699` (confirm with
`list_accounts` if a call errors on org). Upwork tools are deferred: load them with
ToolSearch `+upwork` first.

Files in this folder:
- `templates.md` — Tyler's proposal skeletons, one per job type. **Always
  write from these.**
- `applied-log.md` — every proposal sent + its outcome.
- `seen-jobs.txt` — job ids already surfaced by a scan (don't re-ping).
- `edit-lessons.md` — rules learned from Tyler's edits, plus the kept-%
  scoreboard. **Read it before every draft.**
- `drafts/` — one file per drafted proposal: the AI draft and what was sent.
- `learn.py` — diffs a draft file and prints kept % (`--trend` for all).
- `loomkit.py` + `loom-examples/` — builds the Excalidraw whiteboard sketch
  for each proposal's Loom from a small JSON spec (step 4b).

## Two modes

- **Full run** (Tyler asks: "/upwork-apply", "find me jobs"): steps 1–8,
  up to ~5 jobs on the shortlist.
- **Scan** (scheduled, or "scan Upwork"). See "Scan schedule & cost" below.
  1. **Cheap gate first:** one `smart_search` only (`mode: most_recent`,
     `verified_payment_only: true`, `limit: 10`, `from_date` = now − the
     window). Drop ids already in `seen-jobs.txt`. **Nothing left → stop
     immediately.** No keyword searches, no `get`, no notification.
  2. Only if the gate returned new jobs: run 2 keyword `search` sets from
     step 1 (`limit: 5`) to get exact `proposal_count`s, then step 2 scoring.
  3. **At most 1–2 jobs** that clear the bar. For each, draft the proposal
     and its Loom kit (steps 4, 4b, 5, preview only), then send one `PushNotification`:
     `Upwork: <title> · <budget> · <N> proposals · posted <M> min ago · bid <bid> · fit: <project>. "<first 2 lines of letter>" Reply yes to send.`
     End the run with the **full letter, bid, screening answers, Connects
     cost and boost call** as the final message so Tyler can approve in one
     reply in that session. Save the draft file (step 4). If he edits or
     approves, run step 8 in that same session.
  4. Add every job you scored to `seen-jobs.txt` so it's never re-pinged.

### Scan schedule & cost (set 2026-09-30)

- Weekdays only, Mountain time. **Peak noon–3pm: every 10 min**
  (`from_date` window = 15 min). **9am–noon and 3–5pm: every 30 min**
  (window = 35 min). Windows overlap on purpose; `seen-jobs.txt` dedupes.
- Scheduled tasks: `upwork-scan-peak` and `upwork-scan-offpeak` in
  `~/.claude/scheduled-tasks/`. The scan itself runs in a **Sonnet**
  subagent; drafting stays in that same subagent (templates keep quality).
- Cost lever is the gate: most scans should end after one small call.
  Upwork searches cost no Connects; Connects only move on an approved submit.

## Why speed and filtering matter (the playbook this skill follows)

Benchmark data Tyler brought in (n≈59k proposals):
- Reply rate by send time after posting: 3–4 min **11.9%** · 5–6 min
  6.9% · 30–45 min 5.3% (worst band). Earlier is much better; the cliff is at
  ~5 min.
- 1 other bidder → 9.4% reply; 11+ bidders → 2.1%. Web dev (the most crowded
  subcategory) replies at 5.8% vs a 7.5% platform average.
- Human-written templates 8.1% vs fully AI-written 7.0%.
- Boost: in the first 5 min it slightly *hurts* (9.3% vs 9.6%); best lift at
  15–60 min after posting (+1.7 pts); after 60 min it hurts. 16–20 Connects was
  the best bid band; 21–30 underperformed.
- Reply rates keep rising as a proposal ages (roughly 2× by 75+ days) —
  judge templates on 60+ sends over 90 days, never on last week.

Seen in Tyler's own feed (2026-09-29): an n8n job posted at 19:30 UTC had
19 proposals by 19:36. Weekday feed volume: ~23–30 matching jobs/day,
~73% posted 6am–6pm Mountain, busiest noon–3pm MT; weekends 11–17/day.

## Tyler's targeting (set 2026-09-29 — update here if he changes it)

- **Goal: land first reviews.** Profile has 0 jobs / 0 reviews. Favor
  small, clearly-scoped, winnable jobs (~$300–$1.5k fixed, or short hourly).
- **Work types (all four):** n8n / Make automations · AI agents & chatbots ·
  RAG / knowledge bases · full-stack AI apps (Next.js/Supabase/Stripe).
- **Contract type:** hourly or fixed.
- **Volume:** 3–5 proposals per week. Count this week's rows in
  `applied-log.md`; at 5, only surface a job that scores top-tier.
- **Boost:** decided by timing (step 5), still confirmed per job.

## Proof library (match jobs against this)

Upwork portfolio projects (pulled 2026-09-29 via `get_profile
action=list_highlights` — re-pull if a run finds new ones). Pass the id as
`portfolio_project_ids` on the proposal. **Pick ONE per proposal.**

| Project | id | Best match for | Proof number |
|---|---|---|---|
| Custom agent team for grant writing & RFP creation | 2103166593015046144 | multi-agent systems, RFP/document drafting, research agents | 4 agents, every output human-approved |
| Sundae AI — agent-guided weekly planning SaaS (Next.js, Supabase, Claude, Stripe, GCal) | 2103162144569778176 | full-stack AI apps, SaaS MVPs, scheduling, Stripe | live + paid (ask Tyler for user count) |
| OmniLegislation — 24/7 AI bill & court-ruling monitoring | 2104649267097460736 | monitoring/alert agents, scraping + summaries, legal/gov/compliance | 24/7 monitoring |
| OGE — AI wargaming platform with RAG advisors for universities | 2104650545526939648 | RAG, knowledge-base chat, edtech | — |
| Fastyr AI — frontend for an AI sales automation platform | 2104651755762417664 | React/Next.js frontends for AI products, sales tools | — |
| Leo AI — document intelligence SaaS built from scratch | 2104652745766543360 | document parsing/extraction, doc Q&A | — |
| Lead-to-CRM automation with AI lead scoring (n8n **demo build**) | 2104653834652626944 | n8n, CRM, lead intake/scoring | — |
| After-hours AI receptionist that books appointments (**demo build**) | 2104654944974290944 | voice AI, booking bots, local-service businesses | — |

**Buzz Production Software Factory** (Tyler's own; NOT yet an Upwork portfolio project, so it can't be attached; mention it in the letter only): multi-agent software factory. Engineering team = feature designer agent, engineer agent, QA agent passing work back and forth to spec, code, and QA; Tyler signs off before deploy. Also has design and GTM teams. Best match for multi-agent dev workflows and Claude Code. Once Tyler adds it to the portfolio, re-pull `list_highlights` and add its id to the table.

Other real work (profile overview, not in the portfolio): real-estate blog
automation (Claude + MindStudio) **saves 5+ hrs/week**; 3 AI sales tools for
a digital marketing agency; scheduling/revenue systems for his own service
business (**10+ recurring accounts, 95% retention**).

Certificates: AI Fluency: Frameworks & Foundations (2103157418378291431),
Claude Code 101 (2103156567213194291).

"—" = no number yet. Use a concrete specific instead (what it does, the
stack), and ask Tyler for a number when it's the best-fit proof. Never make
one up.

**Every project above is Tyler's own solo build** (confirmed 2026-09-29) —
not Space Tiger client work, not agency work:
- First person singular: "I built…", never "we" / "our team".
- He applies as an **individual freelancer**. Don't pitch a team or agency
  capacity; Space Tiger (his FDE role) is background credibility only.
- Don't call any portfolio project a client engagement, and don't invent a
  client or results for the two **demo builds**. But don't label them
  "demo" in the letter either, and skip self-undercutting disclaimers like
  "this would be my first X". Just say plainly what he built (L8, Tyler
  2026-10-01).
- The API only returns titles — don't state project details beyond this
  table and the profile overview unless Tyler supplies them.

## 1. Pull candidates

Run in parallel (all read-only):

1. `find_jobs smart_search` — `mode: most_recent`, `verified_payment_only:
   true`, `limit: 10`, and a date window: **scan** = `from_date` = now − 30
   min (RFC3339 UTC); **full run** = `days_posted: 1`.
2. `find_jobs search` with `title` keyword sets (1–3 words; terms are
   ANDed), `verified_payment_only: true`, `sort: recency`, `limit: 10`.
   Sets: `n8n`, `AI agent`, `automation`, `RAG`, `chatbot`, `Make.com`,
   `Claude`, `MCP`. Scan: pick 3; full run: 4–5. No date filter here —
   drop anything whose `published_date` is outside the window yourself.
   `search` rows carry an exact `proposal_count`; `smart_search` rows only a
   tier.

Dedupe by id. Drop `applied: true`. In scan mode, drop ids in `seen-jobs.txt`.

## 2. Score — skip most jobs (that's the feature)

**Hard skips (drop before any `get`):**
- Posted > 60 min ago (scan) / > 24 hrs (full run).
- Too many proposals already. Default: 20+ (raised from 10+ by Tyler,
  2026-10-01). **Exception:** a job posted < 15 min ago stays in up to 29
  proposals (skip at 30+; was 20+) if it's a strong fit to one Proof
  library project and the client is solid (has hired, spend > $1k, good
  rating). AI/n8n jobs hit 25–300 proposals within 30–90 min, so the
  lower cutoffs skipped nearly everything. Tier "20 to 50" is ambiguous at
  these lines: get the exact `proposal_count` from a keyword `search` row
  before skipping or keeping it; tier "50+" is always a skip.
- Payment not verified.
- Budget below the floor: fixed < $150, or hourly max < $20/hr. (These are
  $5–$20 "test tasks" — noise.) Tyler can change this floor.
- Wants voice-over / graphic design / QA only / market research — not his
  work, even if tagged "AI".
- Red flags: unpaid test task, asks to contact off Upwork, already hired.

For survivors, `find_jobs get` (parallel) for `client_record`,
`activityStat.jobActivity`, `preferred_qualifications`, `connects_cost`,
`client_feedback`, and screening questions. Then score:

| Factor | Strong | Weak |
|---|---|---|
| Age | < 5 min | 30–60 min |
| Competition | 0–4 proposals | 10–19 (20–29 only via the < 15 min exception) |
| Fit | concrete match to one Proof library project | only "AI expert" in general |
| Client | has hired, hire rate ≥ 50%, spend > $1k, good freelancer reviews | new client, no spend (OK, just note it) |
| Winnable w/o reviews | no JSS/Top Rated requirement, clear scope, entry/intermediate | "expert only", vague scope |
| Budget | $300–$1.5k fixed or ≥ $35/hr | at floor |
| Subcategory | automation / AI | generic web dev (crowded — penalize) |

Only use numbers the tools return. Report proposals as given (exact count or
tier) — never guess.

## 3. Present the shortlist (full run)

~5 jobs max, best first. For each: title + url, **posted N min ago**, 
proposals, budget, client snapshot (hires, hire rate, spend, rating,
country), Connects cost, the one proof project it maps to, and any risk.
End with Connects balance and this week's count vs the 3–5 target. Ask which
to draft. Speed matters — keep this tight and get to drafts fast.

## 4. Draft the proposal (from the template)

Before `manage_proposals create`:
- **Mandatory:** `list_freelancer_proposals action=invitations` and
  `action=list` for this job. Invitation exists → `accept_invitation`
  instead of `create`.

Open `edit-lessons.md` and apply **every Active rule** (Candidates lightly).
Then open `templates.md`, pick the skeleton for the job type, and **only fill
the bracketed slots**. Don't rewrite Tyler's sentences.

**Save the draft before showing it.** Write
`drafts/<YYYY-MM-DD>-<job id>.md` with the job title, url, type, template +
version, proof, and the exact letter in a fenced ```` ```text ```` block under
`## AI draft` (format: copy an existing file in `drafts/`). Never change the
AI draft block after that. It's the baseline step 8 measures against.

Rules the filled proposal must pass:
1. **First two lines are the proposal** (that's all the client sees in the
   list). Line 1 = their problem + the outcome, **in the client's own
   vocabulary** (their terms, tool names, and framing; don't paste their
   sentences). **Nothing about Tyler in line 1.**
2. **One proof**, the single best-matching project, with its number if it has
   one. No list of projects. Closest match wins even if it can't be attached
   (L3).
3. **Length:** 2–3 short paragraphs, fits on a phone screen (~80–150 words).
4. **End with ONE thing:** one sharp question about their project *or* one
   small piece of free value (a specific observation about their setup, or
   "happy to send a quick Loom of how I'd wire this"). Never three
   questions. Exception: when Tyler recorded a Loom, its link line sits
   above the question and both stay (L4).
5. **Banned:** "I'm excited" as an opener (enthusiasm tied to *this* build
   belongs in sentence 2; see L2), "I have carefully read your job post", "I'm the
   perfect fit", "Dear Hiring Manager", "I hope this finds you well", "I am
   confident", any first line starting with "I", emoji, "we/our team".
6. **Contact details stay out:** no email, phone, WhatsApp, Telegram, Calendly,
   or "let's talk off Upwork". Upwork flags it.
7. **Never claim what the profile can't back.** No invented clients, metrics,
   reviews, or Upwork history.
8. Address the contact by name only if `client_feedback` names them.
9. Voice: first person singular. Being the one person who builds it is a
   selling point; say so when it fits.
10. No price quote or timeline line in the letter, even when the post asks
   for one (L5). The bid field carries the rate; pricing is for the reply.

**Screening questions** (clients filter on these *before* reading the
letter): answer each in 1–3 sentences. Put the answer first, then one
specific detail. No filler, no repeating the cover letter.

**Bid:** match the job's budget range. Fixed → at or slightly under the
client's number (first-reviews goal). Hourly → inside the client's posted
range. Never far outside it. Profile rate is $45/hr. One-line reason; Tyler
decides.

## 4b. Loom kit (every drafted proposal; set 2026-10-01)

Every proposal goes out with a Loom (L4), so build the kit right after the
draft, in both modes (scan too):

1. **Whiteboard sketch.** Write a spec to
   `loom-examples/<YYYY-MM-DD>-<job id>.json` (copy
   `loom-examples/2026-10-01-2105690002080338843.json` for the format), then
   `python3 loomkit.py loom-examples/<file>.json` → writes
   `~/Desktop/Upwork/<file>.excalidraw`. What goes on it:
   - The client's system as they described it, in their own names (their
     tools and channels, left → right: inputs → workflow → AI step → outputs).
   - The thing being added in **green** (`new`).
   - The spot where these builds usually break (the same one line 1 of the
     letter names) in **red** (`risk`), with a note under it saying so.
   - Only what's in the post. No invented components.
2. **1-minute Loom script** (≈150 spoken words; Tyler wants 1 min, not 2).
   Save it under `## Loom script` in the draft file. Five beats, each with
   what to point at on the sketch:
   - 0:00–0:10 hook: "Hi, I'm Tyler…" + their goal restated.
   - 0:10–0:25 the approach, tracing the green path.
   - 0:25–0:35 where it lands (their CRM / DB / outputs).
   - 0:35–0:52 circle the red box: where it usually breaks and how he'd handle it.
   - 0:52–1:00 close with the **same closer question** as the letter.
3. **Open it for him.** There's no Mac app for `.excalidraw`: run
   `open https://excalidraw.com` and `open -R <file>` and tell him to drag
   the file onto the page (Shift+1 to fit). Recording tip: Loom Chrome
   extension → Screen + Camera → **Current Tab** on the excalidraw tab (the
   camera bubble stays on the tab where recording started).
4. When he sends the link, add the Loom line (template slot) and re-run
   `create`.

## 5. Preview, boost, approve

Call `create` → preview. Show Tyler: the full letter, the bid, screening answers,
**connects_cost and connects_balance**, `unmet_preferred_qualifications`, the
proof project being attached, and whether to attach files.

**Boost by timing** (only if `boost.available` is true; use real
`current_top_bids` / `recommended_connects`):
- Job < 15 min old → **don't boost** (early boosts slightly hurt).
- 15–60 min old and a strong fit → **recommend 16–20 Connects**, but only if
  `recommended_connects` ≤ 20. If a paid slot needs more than 20, skip it.
- > 60 min old → **don't boost**.
State the rule you applied; Tyler still says yes or no.

## 6. Submit

Only after an explicit yes on that proposal: `confirm_preview`, `type:
proposal`, `preview_id`. If he edited anything, re-run `create` first
(confirm executes the stored preview). Before confirming, paste the final
letter into the draft file under `## Sent` (fenced the same way), even if
it's unchanged. Verify with `list_freelancer_proposals
action=list` and report status + Connects spent.

## 7. Log it (so templates get tuned on his own data)

Append one row to `applied-log.md` per submitted proposal (columns are in the
file header): date, job title, url, job type, template used, proof used,
posted→sent minutes, proposals at send, bid, connects (+boost), kept %
(from step 8), and
`status`/`viewed`/`replied`/`interview`/`hired`.

Every run (either mode): check `list_freelancer_proposals` for logged proposals
and update their outcome columns. Only compare templates after **60+ sends
spanning 90 days**; before that, report counts and don't draw conclusions.

## 8. Learn from Tyler's edits (self-improvement loop)

Run this after every proposal Tyler edited or approved, including ones he
edited and then decided not to send (save `## Sent` as his final wording and
note "not sent"). It's quick and it's the point of the skill. Reply rates take
months to read; edits are signal today.

1. **Measure.** `python3 learn.py drafts/<file>.md` gives kept % and each
   paragraph he changed. Also copy any reason he gave in chat ("make it sound
   like I wrote it") into the draft file's notes. Stated reasons count more
   than diffs.
2. **Extract lessons.** For each change, ask: is this a *general preference*
   (tone, structure, what proof to pick, what to cut) or a *job-specific
   fact* (his Loom link, a detail only he knew)? Only general preferences
   become lessons. Write each as a rule the next draft can follow.
3. **Update `edit-lessons.md`.**
   - Matches an existing Candidate → bump its count. At 2+ → promote to
     Active.
   - Tyler said it outright → straight to Active.
   - New and inferred → add as Candidate.
   - He undid an Active rule → move it to Retired with the reason.
   - Add a Scoreboard row (date, job, template + version, kept %, lessons).
4. **Fold Active lessons into `templates.md`.** Prefer **Tyler's own wording
   from `## Sent`** over anything Claude writes; that's how the templates
   become human-written. Change only the template(s) the lesson applies to,
   bump the version (v2 → v3), and append a changelog line naming the draft
   and lessons. Rules that aren't template text (proof choice, bid, closer)
   go into the step 4 rules instead.
5. **Guardrails.** Never learn anything that breaks a hard rule (contact
   info, invented claims, "we", approval before submit, Connects/boost
   confirmation). If an edit seems to want that, ask. Don't touch the AI
   draft block of past files.
6. **Show the proof** (end of run, short):
   - Kept % for this proposal and the trend (`python3 learn.py --trend`)
   - Lessons added / promoted / retired, one line each
   - The exact template lines changed, before → after
   - What the next draft will do differently

If Tyler sent the draft untouched (100% kept), log the Scoreboard row and
say so. That's the loop working.

## Don'ts

- Never submit, boost, or accept without an explicit yes for that item.
- Never recommend a job where `applied: true`.
- Never invent competition numbers, client names, or results.
- Never skip step 8 after an edited proposal, and never edit a past
  `## AI draft` block to make the scoreboard look better.
- Accepting an offer happens on upwork.com — give him the link.
