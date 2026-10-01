<!-- self-improve:v1 -->
## Self-improvement loop

This skill gets better from Tyler's edits. Run the loop every time; it's part of the job.
Full procedure: `~/.claude/skills/self-improving-skills/SKILL.md`. Tool:
`L=~/.claude/skills/self-improving-skills/learn.py`.

1. **Before running:** apply every Active rule under *Learned from edits* below. Then run
   `python3 $L pending {{skill}}`. For each pending run, check whether Tyler changed that
   output outside chat (re-read the file, or re-fetch it from the app). If he did, do step 3.
2. **After producing output:** save what you made with
   `python3 $L snapshot {{skill}} <run-id> <<'EOF' … EOF`. Use a stable run-id (file name,
   task GID, date-slug). Snapshot the parts Tyler might change, as plain text.
3. **When Tyler edits it** (in chat, in the file, or in the destination app): pipe his
   final version to `python3 $L diff {{skill}} <run-id>`. Turn each *general preference*
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
