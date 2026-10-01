---
name: whatgotbuilt
description: Produces a plain-language, visual walkthrough of what got built in a coding session or day — explaining each change simply, drawing a diagram where a picture actually clarifies the mechanism, showing real proof it works (not just "it compiled"), and closing with specific open questions for the user's input. Publishes as an Artifact. Trigger this whenever the user runs /whatgotbuilt, asks for "a rundown of what got built," "walk me through today's changes," "explain what you just did," "recap the session," or anything asking for a build summary aimed at a non-engineer audience — even if they don't name the skill explicitly. This is a recurring end-of-session habit, not a one-off report, so reach for it by default after any day of development work on a project the user is tracking.
---

# /whatgotbuilt

The user isn't reading this to review code — they want to understand, in
their own words, what exists now that didn't exist before, why it was built
that way, and where their opinion actually matters. Write for that reader:
someone who can make product calls but doesn't need `processMessage()`
explained as a function signature.

## 1. Figure out the scope

Default to "what changed in this repo today." Concretely:

- `git log --since="midnight" --oneline` (or since the start of the current
  work session if that's clearer from context) in the relevant repo.
- If commits span multiple unrelated repos/projects in the session, ask
  the user which one they mean rather than guessing.
- If there's no git history to lean on (a non-code task, or changes not
  yet committed), fall back to what actually changed this session —
  new/edited files, docs written, things verified — from your own context.

Read the actual diffs/new files, not just commit subject lines. You need to
explain the *mechanism*, and commit messages alone won't give you that.

## 2. Ground it in the plan, if there is one

Check for a roadmap/plan doc in the repo (a calendar, spec, README,
`docs/` folder) that explains *why* today's work exists. If one exists,
connect each piece back to it in a sentence — that's what turns "I added a
file called engine.ts" into "this is the piece that makes texting the app
possible later without a rewrite." Don't force a connection that isn't
there.

## 3. Decide what earns a diagram

Not everything does. Before drawing anything, ask: is there a mechanism
here a cold reader would otherwise have to assemble from prose — a data
flow, a state machine, a before/after, a boundary being crossed? If a
sentence says it faster, write the sentence instead.

When a diagram does earn its place, load the `artifact-diagramming` skill
and follow it: hand-authored inline SVG, `currentColor` for theme-safe
strokes, labeled arrows, one figure with one clear claim per diagram. Two
diagrams is a normal amount for a day's work; zero is fine if nothing in
today's build has a mechanism worth drawing; more than three probably means
some of them aren't earning their space.

## 4. Get real proof, don't describe it secondhand

"It works" is not proof. Before writing the walkthrough:

- If you already ran lint/build/tests or drove the feature through a
  browser/simulator earlier in this session, pull the *actual* output —
  real state JSON, a real terminal result, a real screenshot — into the
  writeup. Quote it verbatim in a `<pre>` block or similar; don't
  paraphrase data into prose.
- If that verification hasn't happened yet and the change is the kind
  covered by `<when_to_verify>` (something a dev server, test suite, or
  build actually exercises), do it now before writing the recap — run the
  real workflow, not just a compile check.
- If verification genuinely isn't possible right now (no server to run,
  no way to test in this environment), say so plainly instead of
  fabricating evidence. A missing "proof" section is honest; an invented
  one is worse than none.

## 5. Write it

Load `artifact-design` fresh (its guidance says to, and calibration is
per-artifact) and build the page as a **utilitarian/memo treatment** —
polished typography and real hierarchy, not a landing-page hero. This is a
report the user reads once and acts on, not something they'll share
publicly.

Structure, adapted to what actually got built (don't force sections that
don't apply):

1. **Header** — one line naming the day/session, a title stating the
   throughline of what got built (not just a list), and a short lede.
2. **Status strip** — small pills for whatever's objectively true: lint
   clean, build clean, tested live, pushed, etc. Only claim what you
   actually verified.
3. **One section per meaningful piece built** — plain-language
   explanation first, diagram if it earns one (step 3), then real
   evidence (step 4: an actual code quote, actual question text, actual
   JSON, actual screenshot reference).
4. **Proof / what changed** — the concrete file list, each with a
   one-line plain-English description of its job, not its type.
5. **Where I'd like your take** — the closing section, and the one that
   matters most. Pull *specific* open questions out of the actual work —
   a design tradeoff you made a judgment call on, an ambiguity in the
   spec, a thing that could reasonably go two ways. Generic questions
   ("any thoughts?") are a sign you haven't actually surfaced a decision
   point yet — go back and find the real ones. Three is a good default
   count; fewer is fine if that's genuinely all there is.

Ground every section in real content from today's work — quote actual
questions, actual file paths, actual output. Never invent example data to
fill a section.

## 6. Publish and close the loop

Publish via the `Artifact` tool. Pick a favicon emoji tied to the subject
matter (reuse the same one across a project's recurring recaps so the
user's tab stays recognizable — check `Artifact` with `action: "list"` if
unsure whether a prior recap for this project already claimed one).

End your chat reply by naming the specific open questions from section 5
inline (don't make the user open the artifact to find out what you're
asking) and explicitly wait for their answer before treating the day's
build as fully wrapped. If they say "looks good, carry it forward," that's
a valid answer too — don't manufacture debate where there isn't any.
