---
name: hypothesis-one-pager
description: Turns a completed Space Tiger client intake form and/or a first-call transcript (either alone is enough; intake-only is the usual case) into a branded, client-facing PDF Hypothesis Doc — the one-pager prepared before every Blueprint call, showing 1-3 candidate AI Enablement/Automation/Custom solutions for a prospect. Trigger when Tyler pastes or attaches an intake form and/or a first-call transcript and asks for a hypothesis doc, one-pager, or "run the hypothesis doc"/"/hypothesis-one-pager" for a client, or says a discovery call just happened and he needs prep for the Blueprint call.
---

# Hypothesis One-Pager

Generates the Hypothesis Doc: the prep document Space Tiger builds before every
Blueprint call, giving 1-3 educated-guess directions to walk in with. Output is a
Space Tiger-branded PDF, not the plain internal docx the doc used to be.

Reference material (read once per run, not per hypothesis):
- `assets/hypothesis-doc-template.docx` — the original doc, including its embedded "AI
  GENERATION INSTRUCTIONS" section. That section is still the source of truth for
  tone, banned words, and per-category criteria — treat it as binding, not this file's
  paraphrase of it. (The docx itself is no longer the output format — see Assembly.)
- `references/client-package-scopes.md` — the three package tiers, for mapping each
  hypothesis to Enablement / Automation / Custom correctly.
- `references/first-call-structure.md` — the call outline and 8 discovery questions,
  for locating answers inside a messy transcript.
- `references/intake-form-structure.md` — the client intake form's 8 sections, for
  when one has been completed and is available as a second input.
- `references/brand-pdf-template.html` — the literal HTML/CSS to reuse for the output
  PDF (see Assembly). Copy its structure and styling; don't redesign from scratch.

## Inputs

Required — at least one of:
- A completed client intake form. This is the usual case, and often the only input.
  It is written by the client, so treat it as the more structured/precise source (see
  `references/intake-form-structure.md`).
- The first-call transcript (pasted text or an attached file).

Also required: client/company name.

When both exist, combine them (intake leads, transcript fills gaps). When only one
exists, work from it alone — never ask for the other, and never mention a missing
input in the doc. Only use a transcript Tyler says is that client's first call; don't
pick up an unrelated recording.

If there's no intake form and no transcript, or no client name, ask — don't guess a
client name or invent source material. Nice-to-have, ask only if not inferable from the transcript
itself: call date, who ran the call (Space Tiger team member).

## Process

1. **Read everything before drafting.** Read every input in full. For an intake form,
   use `references/intake-form-structure.md` to map sections to what you need. For a
   transcript — people volunteer answers out of order — use
   `references/first-call-structure.md` to map dialogue to the 8 discovery questions
   (current state, trigger, prior attempts, existing tools, decision owner, timeline;
   budget is for your own reasoning only, never the output). If both are provided,
   lead with the intake form's answers where both cover the same ground, and use the
   transcript to fill gaps or add color.

2. **Fill Client Information.** Client name, industry/business type, and date. Who
   "completed" the intake side: if an intake form exists, that's its Section 1 primary
   contact (the client's own contact person); if there's no intake form, use
   whoever ran/took notes on the first call instead. Industry: take it from the
   transcript, else the intake form (Section 2 or the website) — ask only if neither
   says. Space Tiger team member defaults
   to Tyler unless told otherwise.

3. **Write Pain Points (3-5 bullets).** Pull primarily from Section 5 + supporting
   Sections 2 and 6 (intake form) and/or the current-state/trigger answers
   (transcript). Address the reader directly — "you", "your team" — never "the
   client". This is a client-facing doc end to end. Interpret and restate in plain language — do not copy the client's raw
   words verbatim. Each bullet is one specific, concrete friction point (time lost,
   errors, missed opportunity), not a vague theme.

4. **Identify 1-3 hypotheses.** For each candidate, use the template's own per-category
   criteria (Enablement / Automation / Custom — see the template's AI GENERATION
   INSTRUCTIONS section) to decide what it is:
   - **Enablement** — a capable person doing a repetitive, predictable task by hand,
     with no tool currently doing it well.
   - **Automation** — a repetitive, predictable process triggered by a consistent
     event, requiring no judgment to execute. One isolated process → Tier 2a. Several
     linked processes/handoffs → Tier 2b (see `references/client-package-scopes.md`).
   - **Custom** — a need unique to this client requiring custom logic, proprietary
     data, or judgment no off-the-shelf tool covers.

   Grounding rule overrides the 1-3 target: only write what's actually supported. If
   it clearly supports just one, stop there and say why rather than padding to three.
   Never write a fourth — cap is 1-3, full stop.

   For each hypothesis, write:
   - A title and category label (Enablement / Automation / Custom).
   - 2-3 sentences: what gets set up, who on your team uses it, what changes
     about their day. (Speak to the client — "your" — not about "the client".) Written for someone who has never used an AI tool — describe
     what it does for the person, never how it works technically.
   - One ROI sentence. No dollar amounts, ever. Use the first rung the inputs
     actually support — never reach past the evidence:
     1. **Client gave hours, or frequency × time** → state it in their terms ("about
        3 hours a week"; "20 quotes a week at ~15 minutes each"). Do arithmetic only
        from numbers they gave.
     2. **Client gave frequency or volume but no time** → name the repeated task and
        what disappears, with their own count: "the re-typing on each of your ~20
        weekly quotes goes away." No hours figure.
     3. **Nothing quantifiable** → state the qualitative win concretely — a task
        eliminated, a handoff removed, a turnaround that shrinks, an error source
        closed, something you can do that you can't today — and end with "we'll size
        this together on the call." No hours figure.
     Never estimate hours from industry norms or how long a task "usually" takes — an
     invented number in a doc the client reads is worse than no number. Custom
     hypotheses are already framed as capacity/outcome in the template, so rung 3 is
     their normal form. Note which hypotheses landed on rung 2 or 3 and flag them to
     Tyler at hand-off (step 8) so he can ask for the number on the call.

5. **Timeline note.** If a deadline, renewal, or event came up (transcript Q6 or
   intake form Section 7), add one line after the Hypotheses noting it. Write it
   client-facing, second person, like the rest of the doc — this is not a private
   aside to Tyler, it's the same voice as the Hypotheses and Next Steps. (The template's header, intro,
   and Next Steps are second person with no "Internal" label — keep them that way.)
   Works the same when the source is the intake form. Lead with
   "You mentioned..." / "You said...", not "The client wants..." or "worth weighing
   when we pick a direction" (that phrasing reads as an internal note slipped into a
   client-facing doc — avoid it). E.g. "You mentioned wanting something in place
   before storm season picks up, roughly 8 weeks out — we'll keep that in mind as we
   scope a direction together."

6. **Enforce the template's general rules before finalizing** (all defined in
   `assets/hypothesis-doc-template.docx`'s instructions section — re-check the actual
   file, this is a summary):
   - No dollar figures anywhere in client-facing sections.
   - No jargon: API, LLM, RAG, prompt, model, integration, webhook, pipeline, vector,
     embedding, inference, or similar technical terms banned from Pain Points and
     Hypotheses.
   - Fits one printed page when the content is light. A full case (3 hypotheses + 5
     pain points, plus the brand header/footer) can legitimately run to a clean second
     page — that's fine, don't sacrifice readability to force one page, but don't pad
     length either.
   - Tone is calm, clear, confident — not salesy. You're demonstrating understanding,
     not pitching.

7. **Assemble the branded PDF.** Output format is PDF, not docx.
   - Take `references/brand-pdf-template.html`, keep its CSS and component structure
     exactly as-is, and fill in the bracketed `[[TOKEN]]` placeholders (client name,
     industry, date, team member, source description — "your intake form", "our first
     call", or "your intake form and our first call", whichever was actually used — pain-point `<li>` items,
     hypothesis blocks, timeline note). Write the filled file to a scratch path (not
     inside the skill folder).
   - Inject the three base64 assets into the matching `[[...]]` tokens by reading the
     files directly — do not paste their contents inline into a Bash/Python heredoc,
     they're large: `assets/logo.png`, `assets/bebasneue.woff2`, `assets/oswald.woff2`
     (base64-encode each with `base64 -i <file> | tr -d '\n'`, save to a temp file,
     read that file's content in your substitution step). Fonts must stay self-hosted
     like this — do not revert to a Google Fonts `<link>`; headless Chrome doesn't
     reliably wait for network web-font requests before rasterizing, which silently
     drops to a serif fallback on any element that doesn't also list one (this bit us
     once already — see the comment in the template).
   - Render with headless Chrome (verified working on this Mac):
     ```
     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
       --disable-gpu --no-sandbox --no-pdf-header-footer \
       --print-to-pdf="<output>.pdf" "file://<path-to-filled>.html"
     ```
     `--no-pdf-header-footer` is required — without it Chrome prints its own
     date/URL header and footer on every page.
   - Verify before handing off: `pdftoppm -jpeg -r 150 <output>.pdf preview` and Read
     the resulting image(s) — confirm fonts rendered correctly (no serif fallback),
     the logo shows, and page breaks didn't split a hypothesis block awkwardly.

8. **Save and hand off.** Default save location: `~/Desktop/Space Tiger AI/Hypothesis
   Docs/<Client Name>/Hypothesis Doc - <Client Name> - <YYYY-MM-DD>.pdf` (create the
   client folder if it doesn't exist). Space Tiger/Streak Advisors work doesn't belong
   in `~/second-brain` — Desktop is correct. After saving, `open` the file per
   standing instructions, and show Tyler the Pain Points + Hypotheses inline in chat
   too so he can sanity-check them without switching windows. Add one line listing any
   hypothesis whose ROI had no client-supplied hours (rung 2 or 3) — those are the
   numbers to ask for on the Blueprint call.

## Guardrails

- This document walks into a real sales conversation — flag it plainly if the
  inputs are too thin to responsibly ground even one hypothesis, rather than
  inventing plausible-sounding pain points that weren't actually said.
- Never present this as a final Blueprint or a commitment — it's explicitly a set of
  educated guesses to pressure-test live, and the template's own copy says so; don't
  strengthen that language when drafting.

## After each run

Once the PDF is handed off, suggest one or two concrete ways this skill could be
improved — based on something you actually ran into this time (a phrasing that didn't
quite fit, an input the process/references don't cover well, a mapping rule that was
ambiguous, a template quirk), not a generic suggestion. Then ask Tyler whether he wants
those changes made now. Make it recursively self-improving in small steps, but only
ever with his go-ahead — never edit SKILL.md or its assets on your own initiative.

## Change log

- **2026-10-02** — Three changes, made together:
  1. *Intake-only input.* The intake form alone (now the usual case) or the transcript
     alone is enough; both together still works, intake leads. Updated the description,
     Inputs, steps 1-3, the source-description token, and
     `references/intake-form-structure.md`.
  2. *Client-facing voice throughout.* Removed "Internal" from the PDF header; the
     template intro and Next Steps now say "you/your" instead of "the client"; Pain
     Points and Hypotheses are written in second person. Edits in
     `references/brand-pdf-template.html` and steps 3-5.
  3. *ROI rule when the client gives no hours.* Three-rung ladder in step 4 (their
     hours → their volume with no hours figure → qualitative win + "we'll size this
     on the call"); never estimate hours from norms; rung 2/3 hypotheses are flagged
     to Tyler at hand-off (step 8).
- **2026-10-02** (later) — Template spacing tightened so 3 hypotheses + a timeline note
  fit on one page: `.page` vertical padding 0.45in → 0.35in, `.hyp` padding 10px → 7px
  (Next Steps is `page-break-inside:avoid`, so it was jumping to page 2). Same look.
