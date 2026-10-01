---
name: asana-task
description: Create Asana tasks (to-dos, reminders, follow-ups, to-do lists) for Tyler — always in the spacetiger.ai project, never any other project. Trigger on "/asana-task", "add an Asana task", "make a task", "put this in Asana", "remind me to…", "add to my to-do list", "make a to-do list in Asana", or any request to create or add tasks in Asana, even if he doesn't say "spacetiger" by name.
---

# Asana Task

Turn whatever Tyler says into Asana tasks in the **spacetiger.ai** project. Create them
right away. Don't preview, and don't ask which project.

## Fixed settings (don't change these)

| Setting | Value |
|---|---|
| Workspace | `1211961497176165` (Streak Advisors, signed in as tyler@streakadvisors.com) |
| Project | **spacetiger.ai**, GID `1216069794470815`, the only allowed project |
| Assignee | `me`, unless Tyler names someone else |

**Never** add tasks to any other project: Streak Advisors - Grants, Streak Advisors - RFP,
Zo Agency RFP, or anything else. That holds even if a task sounds like it belongs there.
If Tyler explicitly names another project, check with him before doing it, because his
standing rule is spacetiger.ai only.

## Steps

1. **Load the tool** (if it isn't loaded yet): ToolSearch
   `select:mcp__1a63d00d-4021-498b-a837-6d4974362d2c__create_tasks`.
   If the tool ID has changed, search ToolSearch for `asana create_tasks`.
2. **Parse the request** into one task per item:
   - `name`: short and imperative ("Call Britton", "Send proposal to Acme").
   - `due_on`: turn relative dates into `YYYY-MM-DD` using today's date
     ("today", "tomorrow", "Friday", "end of week" = that Friday). If no date is given,
     leave it off. Don't invent one.
   - `notes`: only when Tyler gives extra context (phone number, what the call is about).
   - Multiple items or a "list" means multiple tasks in one `create_tasks` call (max 50 per call).
3. **Create** with `create_tasks`, `default_project: "1216069794470815"`, `default_assignee: "me"`.
4. **Report back** briefly: each task name as a link to its `permalink_url`, plus its due date.
   If any task appears in `failed`, say so and give the error. Never claim it worked
   without checking the response.

## Edge cases

- **Assigning to someone else:** look them up with `search_objects` (resource_type `user`)
  and use their GID. If no one matches, ask Tyler.
- **"Personal" tasks:** these still go in spacetiger.ai, assigned to `me`. That's what
  Tyler asked for.
- **Asana not connected / auth error:** tell Tyler to reconnect the Asana connector in his
  claude.ai connector settings. Don't try any other way.

<!-- self-improve:v1 -->
## Self-improvement loop

This skill gets better from Tyler's edits. Run the loop every time; it's part of the job.
Full procedure: `~/.claude/skills/self-improving-skills/SKILL.md`. Tool:
`L=~/.claude/skills/self-improving-skills/learn.py`.

1. **Before running:** apply every Active rule under *Learned from edits* below. Then run
   `python3 $L pending asana-task`. For each pending run, check whether Tyler changed that
   output outside chat (re-read the file, or re-fetch it from the app). If he did, do step 3.
   *Asana:* each pending run-id is a task GID. Re-fetch it with `get_task` and rebuild the
   same three lines. If the task is completed and unchanged, diff it as-is (100%) to clear it.
2. **After producing output:** save what you made with
   `python3 $L snapshot asana-task <run-id> <<'EOF' … EOF`. Use a stable run-id (file name,
   task GID, date-slug). Snapshot the parts Tyler might change, as plain text.
   *Asana:* one snapshot per created task. Run-id = task GID. Body = exactly
   `name: …` / `due: YYYY-MM-DD or none` / `notes: …` (three lines).
3. **When Tyler edits it** (in chat, in the file, or in the destination app): pipe his
   final version to `python3 $L diff asana-task <run-id>`. Turn each *general preference*
   into a rule (not one-off facts). If he stated it, it's Active. If you inferred it once,
   it's a Candidate. If you've seen it twice, it's Active. If he reverses a rule, it's
   Retired. Add a Scoreboard row. Fold Active rules into the steps above where they belong.
4. **Never** learn a rule that breaks this skill's hard rules; ask Tyler instead. Report in
   one line: kept %, rules added/promoted/retired.

## Learned from edits

### Scoreboard
| date | run | kept % | rules |
|---|---|---|---|

### Active
| id | rule | evidence | since |
|---|---|---|---|

### Candidates
| id | rule | seen | evidence |
|---|---|---|---|

### Retired
| id | rule | why |
|---|---|---|
