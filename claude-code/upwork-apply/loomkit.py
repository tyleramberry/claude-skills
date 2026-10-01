#!/usr/bin/env python3
"""Build the Excalidraw whiteboard sketch for a proposal's Loom video.

Usage: python3 loomkit.py <spec.json> [out.excalidraw]

Default output: ~/Desktop/Upwork/<spec name>.excalidraw
Open it by dragging the file onto excalidraw.com (there is no Mac app).

Spec format (see loom-examples/gael-whatsapp.json):
{
  "title": "GAEL + WhatsApp: the 4th channel",
  "subtitle": "same engine, nothing rebuilt",
  "nodes": [ {"id": "wa", "label": "WhatsApp (NEW)\\nMeta Cloud API",
              "col": 0, "row": 3, "style": "new"} ],
  "edges": [ {"from": "wa", "to": "n8n", "style": "new", "label": "optional"} ],
  "notes": [ {"text": "where these builds usually break", "col": 2, "row": 4.8,
              "style": "risk"} ]
}
Node styles: plain (grey), new (green, the thing being added), core (blue,
the AI step), router (yellow, n8n/workflow), risk (red, where it breaks),
alert (dashed red). Edge/note styles: plain, new, risk, alert.
col/row are grid cells (floats allowed); one cell = 340 x 130 px.
"""
import json
import os
import random
import sys

COL_W, ROW_H, BOX_W, BOX_H, TOP = 340, 130, 260, 90, 120
STYLES = {
    "plain": dict(stroke="#1e1e1e", bg="#f1f3f5", sw=2, ss="solid"),
    "new": dict(stroke="#2f9e44", bg="#d3f9d8", sw=3, ss="solid"),
    "core": dict(stroke="#1e1e1e", bg="#a5d8ff", sw=2, ss="solid"),
    "router": dict(stroke="#1e1e1e", bg="#fff3bf", sw=2, ss="solid"),
    "risk": dict(stroke="#e03131", bg="#ffe3e3", sw=3, ss="solid"),
    "alert": dict(stroke="#e03131", bg="#ffffff", sw=2, ss="dashed"),
}
TEXT_COLOR = {"plain": "#1e1e1e", "new": "#2f9e44", "risk": "#e03131",
              "alert": "#e03131", "muted": "#868e96"}

els = []


def base(kind, x, y, w, h, stroke="#1e1e1e", bg="transparent", sw=2, ss="solid"):
    e = dict(id=f"e{len(els)}", type=kind, x=x, y=y, width=w, height=h, angle=0,
             strokeColor=stroke, backgroundColor=bg, fillStyle="solid",
             strokeWidth=sw, strokeStyle=ss, roughness=1, opacity=100,
             groupIds=[], frameId=None,
             roundness={"type": 3} if kind == "rectangle" else ({"type": 2} if kind == "arrow" else None),
             seed=random.randint(1, 2**30), version=1,
             versionNonce=random.randint(1, 2**30), isDeleted=False,
             boundElements=[], updated=1, link=None, locked=False)
    els.append(e)
    return e


def text(cx, y, s, size=18, color="#1e1e1e"):
    lines = s.split("\n")
    w = max(len(l) for l in lines) * size * 0.55
    e = base("text", cx - w / 2, y, w, len(lines) * size * 1.25, stroke=color)
    e.update(text=s, originalText=s, fontSize=size, fontFamily=5,
             textAlign="center", verticalAlign="top", containerId=None,
             autoResize=True, lineHeight=1.25)


def fit_size(label, size=18):
    # shrink until the longest line fits inside the box
    longest = max(len(l) for l in label.split("\n"))
    while size > 12 and longest * size * 0.55 > BOX_W - 16:
        size -= 1
    return size


def cell(col, row):
    return 40 + col * COL_W, TOP + row * ROW_H


def build(spec):
    random.seed(spec.get("title", ""))
    ncols = max([n["col"] for n in spec["nodes"]] + [0]) + 1
    mid = (40 + (ncols - 1) * COL_W + BOX_W) / 2
    text(mid, 10, spec.get("title", ""), size=32)
    if spec.get("subtitle"):
        text(mid, 58, spec["subtitle"], size=18, color=TEXT_COLOR["muted"])

    boxes = {}
    for n in spec["nodes"]:
        x, y = cell(n["col"], n["row"])
        st = STYLES[n.get("style", "plain")]
        base("rectangle", x, y, BOX_W, BOX_H, stroke=st["stroke"], bg=st["bg"],
             sw=st["sw"], ss=st["ss"])
        size = fit_size(n["label"], n.get("size", 18))
        lines = n["label"].count("\n") + 1
        text(x + BOX_W / 2, y + BOX_H / 2 - lines * size * 1.25 / 2, n["label"], size=size)
        boxes[n["id"]] = (x, y, n["col"], n["row"])

    for e in spec.get("edges", []):
        ax, ay, ac, ar = boxes[e["from"]]
        bx, by, bc, br = boxes[e["to"]]
        if ac == bc:  # same column: vertical
            if br > ar:
                p1, p2 = (ax + BOX_W / 2, ay + BOX_H), (bx + BOX_W / 2, by)
            else:
                p1, p2 = (ax + BOX_W / 2, ay), (bx + BOX_W / 2, by + BOX_H)
        elif bc > ac:  # left to right
            p1, p2 = (ax + BOX_W, ay + BOX_H / 2), (bx, by + BOX_H / 2)
        else:  # right to left (e.g. a reply going back out)
            p1, p2 = (ax, ay + BOX_H / 2), (bx + BOX_W, by + BOX_H / 2)
        st = STYLES[e.get("style", "plain")]
        stroke = st["stroke"] if e.get("style", "plain") != "plain" else "#1e1e1e"
        a = base("arrow", p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1], stroke=stroke,
                 sw=st["sw"], ss=st["ss"])
        a.update(points=[[0, 0], [p2[0] - p1[0], p2[1] - p1[1]]],
                 lastCommittedPoint=None, startBinding=None, endBinding=None,
                 startArrowhead=None, endArrowhead="arrow", elbowed=False)
        if e.get("label"):
            text((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 8, e["label"], size=16,
                 color=TEXT_COLOR.get(e.get("style", "plain"), "#1e1e1e"))

    for n in spec.get("notes", []):
        x, y = cell(n["col"], n["row"])
        text(x + BOX_W / 2, y, n["text"], size=n.get("size", 18),
             color=TEXT_COLOR.get(n.get("style", "plain"), "#1e1e1e"))

    return dict(type="excalidraw", version=2, source="https://excalidraw.com",
                elements=els, appState=dict(viewBackgroundColor="#ffffff", gridSize=None),
                files={})


if __name__ == "__main__":
    spec_path = sys.argv[1]
    spec = json.load(open(spec_path))
    name = os.path.splitext(os.path.basename(spec_path))[0]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
        f"~/Desktop/Upwork/{name}.excalidraw")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(build(spec), open(out, "w"), indent=1)
    print(out)
