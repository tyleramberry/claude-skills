---
name: self-improving-skills
description: Tyler's standard for every skill in ~/.claude/skills. Each one carries a self-improvement loop (it snapshots what it produced, diffs that against Tyler's edits, and writes the lessons back into the skill) and is backed up to GitHub (tyleramberry/claude-skills). Trigger when creating, building, or editing any skill ("make this a skill", "/skill-creator", "skillify", "turn this into a skill"), when running a skill's "Self-improvement loop" section, or when Tyler asks how a skill learned something, its kept %, or to push skills to GitHub.
---

# Self-improving skills

Two things are true of every skill Tyler has. Both happen **automatically** through a
PostToolUse hook in `~/.claude/settings.json` that runs `hook.sh` on any Write or Edit
under `~/.claude/skills/`:

1. **It learns from his edits.** If a `SKILL.md` has no learning loop, the hook appends
   `block.md` to it: the loop steps plus empty *Learned from edits* tables.
2. **It's on GitHub.** About 30 seconds after the last edit, the hook runs
   `~/claude-skills/sync.sh "Update skill: <name>"`. That mirrors `~/.claude/skills`
   (and `~/second-brain/skills`) into the private repo `tyleramberry/claude-skills` and
   pushes. Log: `.runs/sync.log` in this folder.

## When creating a skill

- Write `SKILL.md` with the **Write/Edit tools**, not a Bash heredoc. The hook only sees
  Write/Edit. If you used Bash anyway, run
  `python3 ~/.claude/skills/self-improving-skills/learn.py install <SKILL.md>` and
  `~/claude-skills/sync.sh "Add skill: <name>"` yourself.
- After the hook appends the block, re-read the file before editing it again.
- Tailor step 2 of the block to the skill: what gets snapshotted, what the run-id is, and
  where Tyler edits it (a file, an Asana task, a Google Doc, a sent email). Name the
  re-fetch tool, e.g. "re-fetch with `get_task <gid>`".
- No secrets in skill folders. They get pushed. Keys go in `.env*` files (excluded) or
  are read from the environment.
- Tell Tyler it's live and pushed. Confirm the push: `tail -3 .runs/sync.log` here, or
  `git -C ~/claude-skills log -1 --oneline`.

## The loop, in full (what the block's steps mean)

**Measure.** `learn.py snapshot` saves the produced output to `<skill>/.runs/<id>.before`.
`learn.py diff` saves Tyler's final version as `.after` and prints the kept % (the share
of produced words he kept) and the changed lines. `learn.py pending` lists recent
snapshots that were never diffed. Check those for edits he made outside chat (in the app
or the file). `learn.py trend` shows whether kept % is rising, which is the proof the
loop works. `.runs/` stays local; it's excluded from GitHub.

**Extract.** For each change, ask whether it's a **general preference** (wording, format,
defaults, what to include or cut) or a **one-off fact** (this client's name, this date).
Only preferences become rules. Something Tyler says in chat ("always…", "don't…",
"no, make it…") counts more than an inferred diff.

**Record** in the skill's *Learned from edits* section:
- Stated outright → **Active**. Inferred once → **Candidate**. Same Candidate seen again →
  promote it to Active.
- Tyler reverses an Active rule → **Retired**, with the reason, so it isn't re-learned.
- Add one **Scoreboard** row per diffed run: date, run-id, kept %, rule ids.
- Fold each Active rule into the skill's main steps where it applies (use Tyler's own
  wording), and note "→ step N" in the Active row.

**Guardrails.** A rule never overrides a skill's hard rules. Ask Tyler instead. Never edit
a `.before` snapshot to make the score look better. Untouched output (100% kept) still
gets a Scoreboard row.

**Report** (one line at the end of the run): kept %, rules added/promoted/retired, and
what the next run will do differently.

## Files here

- `learn.py`: snapshot / diff / pending / trend / install (the stdlib-only script).
- `block.md`: the standard section appended to every skill (`{{skill}}` → folder name).
- `hook.sh`: the PostToolUse hook (install the block, then a debounced GitHub sync).

`upwork-apply` has its own, richer loop (`learn.py`, `edit-lessons.md`). `install` leaves
any skill alone if it already mentions "self-improvement".
