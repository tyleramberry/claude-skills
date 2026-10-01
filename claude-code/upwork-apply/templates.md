# Proposal templates

**v2 (2026-10-01)**. v1 was Claude-written. Each version folds in Tyler's
own edits (see `edit-lessons.md` and the changelog at the bottom), so the
templates get more Tyler-written over time. The benchmark says human-written
templates beat AI-written ones.

Rules for the model: fill ONLY the [bracketed slots]. Keep every other word.
One proof. One closer. Line 1 never starts with "I" and is never about Tyler.
Slot guidance:
- [their problem → outcome] = restate their exact system/pipeline in their words and tools, with the result they want, so it reads written for them (L1)
- [proof] = one project from the Proof library, with its number if any
- [approach] = 1–2 sentences, concrete, specific to their stack
- [where it usually breaks] = the specific failure point for this kind of build, plus that you'd put the most care there (L1)
- [Loom line] = only if Tyler recorded one: `Recorded a 2-min walkthrough of how I'd wire this: <link>`. Otherwise delete the line (L4)
- [closer] = ONE question, OR one free observation / Loom offer

---

## A. n8n / Make automation

[Their problem → outcome, e.g. "Getting every new Typeform lead into HubSpot, scored and assigned, without anyone copy-pasting."] This is exactly the kind of automation I like building, and I know where these usually break: [where it usually breaks]. That's where I'd put the most care, and I can have it running in your account this week.

I recently built [proof]. For yours I'd [approach], with an error alert to Slack or email so nothing fails silently. You own the workflow and every key.

[Loom line]

[Closer]

---

## B. AI agent / chatbot

[Their problem → outcome, e.g. "A Jira-to-merge pipeline where every agent has one job, with a human signing off before anything merges." / "An agent that answers your support inbox from your own policies and hands anything unusual to a human."] This is exactly the kind of system I get excited to build, and I know where these usually break: [where it usually breaks]. That's where I'd put the most care.

The closest thing I've built is [proof]. Here I'd [approach].

[Loom line]

[Closer]

---

## C. RAG / knowledge base

[Their problem → outcome, e.g. "Staff asking one place and getting answers from your SOPs and PDFs, with the source cited every time."] This is exactly the kind of build I enjoy, and I know where these usually break: [where it usually breaks, e.g. answers without sources, so nobody trusts them]. That's where I'd put the most care, starting with citations back to the source from day one.

I built [proof]. For your docs I'd [approach], and test it on real questions from your team before handover.

[Loom line]

[Closer]

---

## D. Full-stack AI app

[Their problem → outcome, e.g. "An MVP where customers upload a contract and get the key terms back in plain English, with Stripe billing live."] This is exactly the kind of product I get excited to build, and I know where these usually break: [where it usually breaks]. I build the whole thing myself, front end to database to the AI layer, so there's one person accountable.

I built [proof] end to end (Next.js, Supabase, Stripe, Claude). For this I'd [approach], and you'd have something clickable to test every week.

[Loom line]

[Closer]

---

## Closer bank (pick one, adapt to the job)

- One question: "Is [specific tool/data] already in [system], or would I be setting that up too?"
- One question: "What happens today when [edge case from their post] comes in?"
- Free value: "One thing I noticed: [specific observation about their setup/stack]. Worth handling up front."
- Free value: "Happy to send a 2-min Loom of how I'd wire this before you decide."

---

## Changelog (step 8 of SKILL.md appends here; newest last)

- **v1 (2026-09-29):** Claude-written first draft.
- **v2 (2026-10-01):** From the 09-30 "Set Up AI Agents for Developers" edit
  (kept 61%). All four: replaced the stock line-2 sentence with enthusiasm
  about this build plus where it usually breaks (L1, L2); added the optional
  Loom line above the closer (L4). B: dropped the trailing human-approval
  clause from para 2 (C1, applied in B only because that's where it was seen).
  Only B was actually edited by Tyler. A, C and D got the same pattern
  because he stated L1 as a general rule; watch their first edits.
