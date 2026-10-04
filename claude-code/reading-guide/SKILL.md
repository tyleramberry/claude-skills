---
name: reading-guide
description: Turns pasted textbook/course reading (transcripts, chapter text, PDFs) into a concise, visual, interactive HTML study guide — core concepts, one worked example or real-world case per concept, charts/diagrams/animations where they clarify, click-to-reveal practice problems, and a one-card cheat sheet — saved to Tyler's second brain and published as an Artifact. Trigger on "/reading-guide", "here's my reading", "help me learn this reading", "study guide for this chapter", "get the learning out of this without reading it all", or whenever Tyler pastes a long chunk of assigned reading for a class (STRAT 402, MSB, ENT, etc.), even if he doesn't name the skill.
---

# Reading guide

Tyler pastes his reading. He wants the learning out of it **without reading it all**: every
important concept, nothing padded, as visual as possible. Output matches
`reference-example.html` in this folder (Baye Ch. 1 & 3 regression + elasticity guide). Read
that file before building; reuse its `<style>` block and JS helpers.

## Hard rules
- **Don't skip important parts; don't pad.** Every concept the reading teaches gets covered.
  Asides, repetition, and "as we'll see later" filler get cut.
- **Don't invent numbers.** Recompute every figure from the pasted tables (run a quick
  `python3` check). Pasted textbook text usually **drops equations** (blank lines where math
  was). Reconstruct from context/known textbook versions, and flag each reconstruction
  in the reply and the md note so Tyler can check it against the book.
- Pasted text may be duplicated (same block twice); dedupe silently.
- Plain language. Short sentences. Proof via worked numbers, not adjectives.

## Steps

1. **Identify the course and source.** Infer course code from the textbook / topic /
   `~/second-brain/projects/byu-strategy/courses/*.md` (each lists its textbook). Note
   chapter + page range from the "Page NN" markers. Ask once only if impossible.
2. **Extract the skeleton.** List: core concepts (usually 5–10), every formula/rule of thumb,
   every worked example / demonstration problem, every real-world case (Inside Business boxes,
   cited studies), and the decision each concept supports. Find the through-line that links
   them and put it in the header as a flow strip (A → B → C → Decision).
3. **Verify the math.** Recompute every example answer. Fill in dropped equations.
4. **Build the HTML** at
   `~/second-brain/projects/byu-strategy/notes/<COURSE>/<source-slug>-guide.html`
   following the reference structure:
   - Header: course/chapter eyebrow, `<title>`/h1 = short topic name (2–4 words, e.g.
     "Regression & Elasticity Guide"), one-sentence lede, flow strip.
   - Sticky chip nav, one chip per section.
   - **One section per concept:** cell-letter eyebrow (A1, B1, …), h2 stating the idea in
     plain words, 1–3 sentences of explanation, a formula box if there's a formula, **one
     visual** where a picture actually clarifies (interactive slider chart, animated fit,
     bar comparison, CI/forest plot, flow diagram, annotated table with crossed-out
     irrelevant rows, decoded-output callout cards), and **one** worked example or real-world
     case box. Don't force a chart where a table or callouts do the job better.
   - At least 1–2 **interactive** visuals per guide (sliders, "animate" button) using the
     reference's inline-SVG helper (`el()`), no libraries needed. Respect reduced motion.
   - **Practice** section: 4–6 `<details>` problems (click to reveal), each tagged with its
     concept; use the book's demo problems plus one or two new ones in the same shape.
   - **Cheat sheet**: one table, every formula/rule on one card.
   - Keep theme tokens, light + dark, phone-width safe (from reference CSS).
5. **Check once** in the built-in browser: navigate to the file, one screenshot pass at
   phone width, `read_console_messages` errors only. Fix what's visibly broken; no loops.
6. **Publish** with the Artifact tool (`icon: "chart"` or fitting word, one-sentence
   description). Re-publishing the same path keeps the URL.
7. **File it in the second brain** (per `~/second-brain/skills/class-notes.md`):
   - md note next to the HTML: `<source-slug>.md` with frontmatter (title, course, date,
     type: note, tags [school, byu, reading]), link to the HTML, 3–7 Takeaways,
     Questions/confusions (include flagged reconstructions).
   - Add a link on the course's line in `~/second-brain/index.md`.
   - Append to `~/second-brain/log.md`: `## [YYYY-MM-DD] action | <COURSE> reading guide — <topic>`.
8. **Open** the HTML (`open <path>`), snapshot for the learning loop (below), and reply
   briefly: artifact link, the concept list (one line each), any flagged reconstructions,
   file paths.

<!-- self-improve:v1 -->
## Self-improvement loop

This skill gets better from Tyler's edits. Run the loop every time; it's part of the job.
Full procedure: `~/.claude/skills/self-improving-skills/SKILL.md`. Tool:
`L=~/.claude/skills/self-improving-skills/learn.py`.

1. **Before running:** apply every Active rule under *Learned from edits* below. Then run
   `python3 $L pending reading-guide`. For each pending run, re-read that guide's HTML file
   in `~/second-brain/projects/byu-strategy/notes/<COURSE>/`; if Tyler changed it, do step 3.
2. **After producing output:** snapshot the visible text of the guide (strip `<style>` and
   `<script>`, keep headings, explanations, examples, practice, cheat sheet) with
   `python3 $L snapshot reading-guide <source-slug> <<'EOF' … EOF`. Run-id = the
   `<source-slug>` used in the file name.
3. **When Tyler edits it** (asks for changes in chat, or edits the HTML file): pipe the
   final visible text to `python3 $L diff reading-guide <source-slug>`. Turn each *general
   preference* (length, which visuals, tone, sections to add/cut) into a rule — not one-off
   facts. Stated → Active. Inferred once → Candidate. Seen twice → Active. Reversed →
   Retired. Add a Scoreboard row. Fold Active rules into the steps above.
4. **Never** learn a rule that breaks this skill's hard rules; ask Tyler instead. Report in
   one line: kept %, rules added/promoted/retired.

## Learned from edits

### Scoreboard
| date | run | kept % | rules |
|---|---|---|---|

### Active
| id | rule | evidence | since |
|---|---|---|---|
| A1 | Concise, visual (charts/diagrams/animations), one example or real case per concept; don't skip important parts, don't pad | Tyler's original request, 2026-10-03 | 2026-10-03 |

### Candidates
| id | rule | seen | evidence |
|---|---|---|---|

### Retired
| id | rule | why |
|---|---|---|
