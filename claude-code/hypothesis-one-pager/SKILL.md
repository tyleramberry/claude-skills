---
name: hypothesis-one-pager
description: Turns a Space Tiger first-call transcript (plus a completed client intake form, when one exists) into a branded PDF Hypothesis Doc — the one-pager prepared before every Blueprint call, showing 1-3 candidate AI Enablement/Automation/Custom solutions for a prospect. Trigger when Tyler pastes or attaches a first-call transcript (and/or an intake form) and asks for a hypothesis doc, one-pager, or "run the hypothesis doc"/"/hypothesis-one-pager" for a client, or says a discovery call just happened and he needs prep for the Blueprint call.
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

Required:
- The first-call transcript (pasted text or an attached file).
- Client/company name.

Optional but preferred when it exists:
- A completed client intake form. The intake form goes out to the client later in the
  funnel (after they pay for the Blueprint Process), so for many clients it won't
  exist yet at this stage — that's normal, not a blocker. When it is available, treat
  it as the more structured/precise source (see `references/intake-form-structure.md`
  for how the two inputs combine).

If the transcript or client name is missing, ask for it — don't guess a client name or
invent a transcript. Nice-to-have, ask only if not inferable from the transcript
itself: call date, who ran the call (Space Tiger team member).

## Process

1. **Read everything before drafting.** Read the whole transcript — people volunteer
   answers out of order — using `references/first-call-structure.md` to map dialogue
   to the 8 discovery questions (current state, trigger, prior attempts, existing
   tools, decision owner, timeline; budget is for your own reasoning only, never the
   output). If an intake form is also provided, read it too and use
   `references/intake-form-structure.md` to combine the two: lead with the intake
   form's answers where both cover the same ground, use the transcript to fill gaps or
   add color.

2. **Fill Client Information.** Client name, industry/business type, and date. Who
   "completed" the intake side: if an intake form exists, that's its Section 1 primary
   contact (the client's own contact person); if there's no intake form yet, use
   whoever ran/took notes on the first call instead. Space Tiger team member defaults
   to Tyler unless told otherwise.

3. **Write Pain Points (3-5 bullets).** Pull primarily from the current-state/trigger
   answers (transcript) or Section 5 + supporting Sections 2 and 6 (intake form, when
   available). Interpret and restate in plain language — do not copy the client's raw
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
   - 2-3 sentences: what gets set up, who on the client's team uses it, what changes
     about their day. Written for someone who has never used an AI tool — describe
     what it does for the person, never how it works technically.
   - One ROI sentence: hours saved per week, tasks eliminated, or time recovered.
     No dollar amounts, ever.

5. **Timeline note.** If a deadline, renewal, or event came up (transcript Q6 or
   intake form Section 7), add one line after the Hypotheses noting it. Write it
   client-facing, second person, like the rest of the doc — this is not a private
   aside to Tyler, it's the same voice as the Hypotheses and Next Steps. Lead with
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
     industry, date, team member, source description, pain-point `<li>` items,
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
   too so he can sanity-check them without switching windows.

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
