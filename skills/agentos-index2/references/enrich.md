# agentos-index2 --enrich

Use this module to run `Index.Enrichment` on a block: spawn a focused discussion with the user that produces new `Touched.Surface`, and land the resulting evidence through the gates.

Authority lives in the index: `Index.Enrichment` (107) owns the doctrine — grounding is retrospective (mining the existing chat corpus), enrichment is generative (producing new surface). This module is the generative side. If a block's evidence is probably sitting unmined in the corpus, that is grounding work: route to `--gr-survey` / `--back-link` instead.

This module is NOT `Workflow.Neutral`: it drives a discussion and applies gated index writes (`Edit.Trigger.Gated`, `Content.Verbatim.Gated`).

## Target Selection

- an explicit block from the caller wins
- default selector: the head of the density worklist — `agentos index blocks --depot <depot> --sort gr-density [--scope <path>] --json` — filtered to **non-zero** density (zero-density blocks go to grounding first: mine before you generate)
- `Grounding.Density` reads as pipeline position (`Index.Enrichment`): zero → grounding; low → enrich here; high → rest until touched again

## Enrichment Loop (per block)

1. **Load** the block, its appendix depth, and its current grounding (board + inline anchors). Note the density before.
2. **Probe.** Open a short, scoped discussion with the user about the block — a micro design-session one block wide. Good probes: a tension between two lines; a line that reads ambiguous cold; a missing example or boundary; a claim the user never stated in their own words; how the block relates to a newer concept. One probe at a time — this is a conversation, not a questionnaire.
3. **Harvest.** The user's replies are new evidence surface. For each touched outcome:
   - a line the user confirmed, corrected, or restated → mint on that turn (`references/link.md`) and land it as the line's inline best pointer (upgrade per `Inline.Grounding`, ≤3 per line)
   - a noticeable turn about the concept as a whole → a `[GR]` board spot in `Grounding.Head`
   - new content the discussion produced → `Capture.Offer` with destination options (main / appendix / agendix / decline); landed lines are born grounded on their turns
   - a contradiction with the current text → propose the revision through `--edit`; the approving turn grounds the new wording
4. **Land** through the normal gates — verbatim proposals, per-entry or batch approval, nothing self-written.
5. **Receipt.** Report the density delta (before → after) and anything the discussion opened but did not close.

## Boundaries

- one block at a time; the user picks when to stop — enrichment has no completion state (`Index.Enrichment`: no block is finished)
- do not interrogate: if a probe gets no traction, move on or end the pass — forced turns are weak evidence
- do not re-litigate settled design as a probe; enrichment deepens evidence, it does not reopen decisions (a genuine contradiction is an `--edit` proposal, not a debate)
- not `--ground` (read-only conversation-to-index comparison) and not a full `agentos-hugentics-designer` session (unscoped) — block-scoped, gated, receipt-measured
- linter check after any landing, per the edit path
