# Blueprint Intake Form Structure

Space Tiger's client intake form ("Space Tiger Blueprint Intake Form"). Per the
microsite flow, this goes out to the client after they pay for the Blueprint Process —
so it may or may not exist yet for a given client at the point this skill runs. Treat
it as a **second input when available**, not a hard requirement — the first-call
transcript alone is enough to draft a Hypothesis Doc.

## Sections

1. **Business & Billing Info** — primary contact name/email/phone, legal business
   name, website, billing/mailing address. Source for the Client Information block
   (and for who "completed" the intake form).
2. **Company Context** — anything about the company beyond the website: structure,
   priorities, what's changing. Optional attached deck/one-pager/org chart. Supporting
   source for Pain Points (broader business pressures).
3. **Tech Stack** — email/file hosting, CRM/task/storage/e-sign/accounting/chat tools,
   which AI tools the team has already used.
4. **Security & Compliance** — required certifications (HIPAA, SOC 2, PCI, FedRAMP,
   etc.). Rarely relevant to the Hypothesis Doc itself, but flag if it constrains which
   hypothesis is realistic (e.g. a Custom system touching regulated data).
5. **The Core Problem** — the process causing the most frustration, step by step,
   start to finish; what's already been tried. **Primary source for Pain Points**,
   equivalent to the transcript's Q1/Q2/Q3.
6. **What Success Looks Like** — what a clear win looks like a month out; anything
   off-limits. Supporting source for Pain Points (the gap between current and desired
   state) and useful context for scoping the ROI lines.
7. **Logistics** — who else should be involved in the decision; any deadline or event
   driving the timeline. Source for the Timeline note, equivalent to the transcript's
   Q5/Q6.
8. **Catch-All** — SOPs, screenshots, prompts, sample outputs. Skim for anything that
   sharpens a hypothesis's specificity.

## How to use it alongside the transcript

- When both exist: the intake form is written directly by the client, so treat its
  answers as the more precise/structured source — lead with it for Pain Points
  (Sections 5, 2, 6) and the Timeline note (Section 7). Use the transcript to fill
  gaps, add color, or catch things the client didn't think to write down.
- When only the transcript exists (the common case today, since the intake form goes
  out later in the funnel): fall back entirely to `first-call-structure.md`'s mapping.
  Don't block on a missing intake form.
- Client Information block: Section 1's primary contact name is who "completed" the
  intake form when one exists. Without an intake form, use whoever ran/took notes on
  the first call instead (see SKILL.md step 2).
