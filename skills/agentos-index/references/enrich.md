# agentos-index --enrich

Use this module to run `Index.Enrichment` on a block: spawn a focused discussion whose qualifying user turns produce new `Touched.Data`, then route resulting projections through their gates.

`Index.Enrichment` owns the retrospective/generative split: grounding mines existing authority-surface evidence, while enrichment creates opportunities for new touch. If evidence is probably already present in the corpus, route to `--gr-survey` or `--back-link`.

Enrichment applies `Touched.Decision.Cycle`; qualifying turns are editions of the current chat `Touch.Authority.Surface`, while contradictions become `POI.Instance`s before any remedy is chosen.

This module is NOT `Workflow.Neutral`: it drives a discussion and applies gated index writes (`Edition.Trigger.User.Gated`, `Verbatim.User.Gated`).

## Target Selection

- an explicit block from the caller wins
- default selector: the head of the density worklist — `agentos index blocks --depot <depot> --sort gr-density [--scope <path>] --json` — filtered to **non-zero** density (zero-density blocks go to grounding first: mine before you generate)
- `Grounding.Density` reads as pipeline position (`Index.Enrichment`): zero → grounding; low → enrich here; high → rest until touched again

## Enrichment Loop (per block)

1. **Load** the block, its appendix depth, and its current grounding (board + inline anchors). Note the density before.
2. **Probe.** Open a short, scoped discussion with the user about the block — a micro design-session one block wide. Good probes: a tension between two lines; a line that reads ambiguous cold; a missing example or boundary; a claim the user never stated in their own words; how the block relates to a newer concept. One probe at a time — this is a conversation, not a questionnaire.
3. **Harvest.** Classify which user replies qualify as touched editions for the subject. For each touched outcome:
   - a line the user confirmed, corrected, or restated → mint on that turn (`references/link.md`) and land it as the line's inline best pointer (upgrade per `Index.Line` grounding, ≤3 per line)
   - a noticeable turn about the concept as a whole → stamp it as the fallback trailing anchor on the lines no more specific turn covers
   - new content the discussion produced → `Capture.Offer` with destination options (main / appendix / agendix / decline); landed lines are born grounded on their turns
   - a contradiction with the current text → create a POI and reason about the resolution; propose `--edit` only when revision is the selected reconciliation
4. **Land** through the normal gates — verbatim proposals, per-entry or batch approval, nothing self-written.
5. **Receipt.** Report the density delta (before → after) and anything the discussion opened but did not close.

## Boundaries

- one block at a time; the user picks when to stop — enrichment has no completion state (`Index.Enrichment`: no block is finished)
- do not interrogate: if a probe gets no traction, move on or end the pass — forced turns are weak evidence
- do not manufacture disagreement as a probe; a genuine contradiction may reopen the relevant decision but does not prescribe an index edit
- not `--search` (read-only conversation-to-index comparison) and not a full `agentos-hugentics-designer` session (unscoped) — block-scoped, gated, receipt-measured
- linter check after any landing, per the edit path
