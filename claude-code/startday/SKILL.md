---
name: startday
description: Morning kickoff for a day-by-day build challenge (like a 30-day launch calendar). Reads today's entry from the project's calendar/roadmap doc plus the actual repo state (git log, existing code) to produce a concrete plan of today's Development and Content tasks — adjusted for anything already done or left over from yesterday — and presents it for approval. Once approved, autonomously implements, verifies, and ships the Development tasks without further check-ins except for genuine blockers (spend, login/CAPTCHA/OAuth), then hands off to a build recap and walks through the Content tasks. Trigger this whenever the user runs /startday, says "what's on deck today," "let's start today's build," "kick off day N," or opens a session on a project that has a day-by-day plan doc without saying what to work on.
---

# /startday

This is the other end of `whatgotbuilt`: that skill explains what happened
after the fact, this one decides what should happen before it starts, gets
a green light, then executes it unattended. Treat the approval step as a
real gate — everything after it should run without pinging the user again,
except for the specific things below that genuinely need them.

## 1. Find today's entry

- Locate the calendar/roadmap doc — look for `docs/*calendar*.md`,
  `docs/*roadmap*.md`, or similar in the current repo. If more than one
  plausible candidate exists, ask which. If none exists, tell the user
  this skill needs a day-by-day plan doc to work from and stop.
- Match "today" against the doc's actual dates (the doc usually pins a
  real calendar date to each day number — trust that over assumptions).
  If today is marked a rest day, say so plainly and stop — don't invent
  work to fill it.
- Pull that day's **Development** and **Content** tasks verbatim, plus
  its stated outcome/goal — you'll need the outcome to know what "done"
  looks like, not just the task list.

## 2. Reconcile against reality before proposing anything

The plan doc is a forecast written days ago; the repo is what's actually
true now. Before presenting anything to the user:

- `git log` since roughly the start of today (or since the last day's
  entry, if today's work already started) to see what's already landed.
  Cross-check against today's task list — don't propose redoing work
  that's already committed.
- Skim yesterday's entry too. If yesterday's Development tasks weren't
  fully finished (check commits/outcomes against what was planned), flag
  that explicitly and ask whether to fold the leftover into today's plan
  or knowingly defer it — don't silently drop it and don't silently
  double today's load without asking.
- If a task depends on something upstream that isn't actually in place
  yet (an env var, a service that isn't provisioned, a prior day's
  outcome that didn't actually land), surface that as a risk in the plan
  rather than discovering it mid-implementation.

## 3. Present the plan and stop

Show the user, concisely:

- Today's Development tasks, each with a one-line note on approach if
  it's not obvious from the calendar doc alone.
- Anything carried over from yesterday, and why.
- Anything in today's Development list that involves spending money
  (a paid API tier, ad spend, a domain purchase, anything with a real
  bill attached) — call these out by name here, before starting, even
  though the actual spend confirmation happens later if you reach it.
- Today's Content tasks, unstarted — those stay the user's to execute,
  same as always; just list them so the plan is complete.

Then wait for a clear go-ahead. A vague "sounds fine" in the middle of an
unrelated message doesn't count — get an actual signal this plan is
approved before touching code.

## 4. Execute the Development tasks autonomously

Once approved, work through today's Development tasks the same way you
would if the user were watching over your shoulder and had already told
you to keep going without asking:

- Implement each task, run lint + build, and actually verify the behavior
  (spin up the dev server, drive it through the browser, hit real
  endpoints) before moving to the next one — never advance on "it
  compiles" alone.
- Commit and push working increments as you go, matching the existing
  commit message style in the repo's git log.
- If a task needs something spend-related that you flagged in step 3 (or
  discover mid-task), stop and confirm that specific spend before doing
  it — don't treat the day's initial approval as covering money you
  haven't separately confirmed.
- If a task needs a genuine human-in-the-loop step (signing into a real
  account, an OAuth consent screen, a CAPTCHA, anything needing a
  password or payment), do everything else around it, then tell the user
  exactly the one action you need, wait for it, and continue from there
  without re-explaining the whole task or re-asking about unrelated
  already-approved work.
- Don't stop and ask about anything that doesn't actually require it —
  that's the whole point of the approval gate in step 3.

## 5. Hand off to the recap, then walk through Content

When the Development tasks are done (or you've gone as far as you can,
e.g. blocked on a human-in-the-loop step), invoke the `whatgotbuilt`
skill to produce today's build walkthrough — don't re-derive that format
here, it already owns that job.

After the recap, walk the user through today's **Content** tasks (pulled
in step 1): what to capture/film/screenshot for each, and a draft caption
where the task calls for a post. They handle the actual posting/filming;
your job stops at handing them something ready to use.
