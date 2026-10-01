#!/bin/sh
# PostToolUse hook (Write|Edit). When a file under ~/.claude/skills changes:
#   1. a SKILL.md without a learning loop gets the standard block appended
#   2. the claude-skills GitHub backup is synced (debounced 30s, in background)
DIR="$HOME/.claude/skills/self-improving-skills"
FILE=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))' 2>/dev/null)

case "$FILE" in
  "$HOME/.claude/skills/"*) ;;
  *) exit 0 ;;
esac
case "$FILE" in */.runs/*) exit 0 ;; esac

SKILL=$(echo "${FILE#$HOME/.claude/skills/}" | cut -d/ -f1)

if [ "$(basename "$FILE")" = "SKILL.md" ] && \
   [ "$(python3 "$DIR/learn.py" install "$FILE")" = "installed" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"Appended the standard self-improvement loop to %s (re-read before editing it again)."}}\n' "$FILE"
fi

# Debounce: only the last edit in a 30s window pushes.
STAMP="$DIR/.runs/last-edit"
mkdir -p "$DIR/.runs"
NOW=$(date +%s); echo "$NOW $SKILL" > "$STAMP"
(
  sleep 30
  [ "$(cut -d' ' -f1 "$STAMP")" = "$NOW" ] || exit 0
  "$HOME/claude-skills/sync.sh" "Update skill: $SKILL" >> "$DIR/.runs/sync.log" 2>&1
) >/dev/null 2>&1 &
exit 0
