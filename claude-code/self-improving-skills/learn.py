#!/usr/bin/env python3
"""Shared learn-from-edits tool for every skill in ~/.claude/skills.

Usage:
  learn.py snapshot <skill> <run-id>   < output   # save what the skill produced
  learn.py diff     <skill> <run-id>   < final    # compare with Tyler's final version
  learn.py pending  <skill> [--days N]            # snapshots never diffed (check for edits)
  learn.py trend    <skill>                       # kept % across every diffed run
  learn.py install  <path/to/SKILL.md>            # add the self-improvement block if missing

<skill> is a folder name (asana-task) or path. Snapshots live in <skill>/.runs/,
which is never pushed to GitHub (it can hold client details).
"""
import difflib, glob, os, re, sys, time

SKILLS = os.path.expanduser("~/.claude/skills")
HERE = os.path.dirname(os.path.abspath(__file__))
MARKER = "<!-- self-improve:v1 -->"


def skill_dir(name):
    return name if os.sep in name else os.path.join(SKILLS, name)


def runs(skill):
    d = os.path.join(skill_dir(skill), ".runs")
    os.makedirs(d, exist_ok=True)
    return d


def safe(run_id):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", run_id).strip("-") or "run"


def kept_pct(before, after):
    # Word-level similarity, so additions count as edits too (100 = untouched).
    a, b = before.split(), after.split()
    if not a and not b:
        return 100
    return round(100 * difflib.SequenceMatcher(None, a, b, autojunk=False).ratio())


def snapshot(skill, run_id):
    path = os.path.join(runs(skill), safe(run_id) + ".before")
    open(path, "w").write(sys.stdin.read())
    print(f"saved {path}")


def diff(skill, run_id):
    base = os.path.join(runs(skill), safe(run_id))
    if not os.path.exists(base + ".before"):
        sys.exit(f"no snapshot for {run_id}; run `snapshot` when the skill produces output")
    before = open(base + ".before").read()
    after = sys.stdin.read()
    open(base + ".after", "w").write(after)
    pct = kept_pct(before, after)
    print(f"# {os.path.basename(skill_dir(skill))} / {run_id}")
    print(f"Kept {pct}% of words\n")
    bl, al = before.strip().splitlines(), after.strip().splitlines()
    if bl == al:
        print("No changes. Tyler kept it as-is.")
    for line in difflib.unified_diff(bl, al, "produced", "final", lineterm="", n=0):
        if not line.startswith(("---", "+++", "@@")):
            print(line)


def pending(skill, days=14):
    cutoff = time.time() - days * 86400
    found = False
    for f in sorted(glob.glob(os.path.join(runs(skill), "*.before"))):
        if os.path.exists(f[: -len(".before")] + ".after") or os.path.getmtime(f) < cutoff:
            continue
        found = True
        print(f"{os.path.basename(f)[:-7]}  ({time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(f)))})")
    if not found:
        print("nothing pending")


def trend(skill):
    rows = []
    for f in sorted(glob.glob(os.path.join(runs(skill), "*.after")), key=os.path.getmtime):
        b = f[: -len(".after")] + ".before"
        if os.path.exists(b):
            rows.append((os.path.basename(f)[:-6], kept_pct(open(b).read(), open(f).read())))
    if not rows:
        print("No diffed runs yet.")
        return
    print("| run | kept % |\n|---|---|")
    for name, pct in rows:
        print(f"| {name} | {pct} |")
    half = max(1, len(rows) // 2)
    avg = lambda r: round(sum(p for _, p in r) / len(r))
    print(f"\nOlder avg {avg(rows[:half])}% -> newer avg {avg(rows[half:] or rows)}% (n={len(rows)})")


def install(path):
    """Append the standard block. Returns True if the file changed."""
    path = os.path.abspath(os.path.expanduser(path))
    name = os.path.basename(os.path.dirname(path))
    if os.path.basename(path) != "SKILL.md" or name == "self-improving-skills":
        return False
    text = open(path).read()
    # Skip skills that already have a loop (marker, or a hand-built one like upwork-apply).
    if MARKER in text or re.search(r"self-improvement", text, re.I):
        return False
    block = open(os.path.join(HERE, "block.md")).read().replace("{{skill}}", name)
    open(path, "w").write(text.rstrip() + "\n\n" + block)
    return True


if __name__ == "__main__":
    a = sys.argv[1:]
    cmd = a[0] if a else ""
    if cmd == "snapshot" and len(a) == 3:
        snapshot(a[1], a[2])
    elif cmd == "diff" and len(a) == 3:
        diff(a[1], a[2])
    elif cmd == "pending" and len(a) >= 2:
        pending(a[1], int(a[a.index("--days") + 1]) if "--days" in a else 14)
    elif cmd == "trend" and len(a) == 2:
        trend(a[1])
    elif cmd == "install" and len(a) == 2:
        print("installed" if install(a[1]) else "already has a loop (or not a skill)")
    else:
        print(__doc__)
