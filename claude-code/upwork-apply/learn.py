#!/usr/bin/env python3
"""Compare the AI draft with what Tyler actually sent.

Usage: python3 learn.py drafts/<file>.md      # one proposal
       python3 learn.py --trend               # kept % across every draft

A draft file has two fenced blocks under the headings "## AI draft" and
"## Sent". Prints % of draft words Tyler kept, then each change by paragraph.
"""
import difflib, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def blocks(path):
    text = open(path).read()
    out = {}
    for name in ("AI draft", "Sent"):
        m = re.search(rf"## {name}\s*```(?:text)?\n(.*?)```", text, re.S)
        out[name] = m.group(1).strip() if m else None
    return out["AI draft"], out["Sent"]


def kept_pct(draft, sent):
    a, b = draft.split(), sent.split()
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    kept = sum(blk.size for blk in sm.get_matching_blocks())
    return round(100 * kept / max(len(a), 1)), len(a), len(b)


def report(path):
    draft, sent = blocks(path)
    if not draft or not sent:
        print(f"{os.path.basename(path)}: missing AI draft or Sent block")
        return None
    pct, na, nb = kept_pct(draft, sent)
    print(f"# {os.path.basename(path)}")
    print(f"Kept {pct}% of draft words ({na} drafted -> {nb} sent)\n")
    dp = [p.strip() for p in draft.split("\n\n") if p.strip()]
    sp = [p.strip() for p in sent.split("\n\n") if p.strip()]
    sm = difflib.SequenceMatcher(None, dp, sp, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        for p in dp[i1:i2]:
            print(f"- REMOVED/CHANGED: {p}\n")
        for p in sp[j1:j2]:
            print(f"+ SENT: {p}\n")
    return pct


def trend():
    rows = []
    for f in sorted(glob.glob(os.path.join(HERE, "drafts", "*.md"))):
        draft, sent = blocks(f)
        if draft and sent:
            rows.append((os.path.basename(f), kept_pct(draft, sent)[0]))
    if not rows:
        print("No finished drafts yet.")
        return
    print("| draft | kept % |\n|---|---|")
    for name, pct in rows:
        print(f"| {name} | {pct} |")
    first = rows[: max(1, len(rows) // 2)]
    last = rows[len(rows) // 2 :]
    avg = lambda r: round(sum(p for _, p in r) / len(r))
    print(f"\nOlder half avg {avg(first)}% -> newer half avg {avg(last)}% (n={len(rows)})")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--trend":
        trend()
    elif len(sys.argv) > 1:
        report(sys.argv[1])
    else:
        print(__doc__)
