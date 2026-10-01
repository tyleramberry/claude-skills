#!/bin/sh
# Refresh this repo from the live skill folders, then commit + push.
# Optional arg: commit message (the self-improving-skills hook passes "Update skill: <name>").
set -e
cd "$(dirname "$0")"
rsync -aL --delete \
  --exclude 'applied-log.md' --exclude 'seen-jobs.txt' --exclude 'drafts/' --exclude 'edit-lessons.md' \
  --exclude '.runs/' --exclude '.DS_Store' --exclude '__pycache__/' --exclude '.env*' \
  "$HOME/.claude/skills/" claude-code/
rsync -a --delete --exclude '.DS_Store' "$HOME/second-brain/skills/" second-brain/
git add -A
git diff --cached --quiet || git commit -m "${1:-Sync skills $(date +%Y-%m-%d)}"
git push
