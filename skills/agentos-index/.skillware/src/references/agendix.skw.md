# agentos-index --agendix

The knowledge of the `Index.Agendix` surface: what it is, what may enter it, and the form material takes to land there.

This module is a `Workflow.Neutral.Module`: it runs no workflow — its rules bind whenever material lands on the agendix, whichever module has control. The capture workflow that harvests chat content lives in `references/capture.md`; `--agendix` runs that workflow with the agendix as preset destination.

The agendix is the agentic path of the same alignment writing the index runs hugentically: same primitives — `Kernel.Line`s, `Line.Type`s, anchors, the current concept set — with the user's review gate replaced by hard provenance. It is **trigger-gated, not content-gated**: a user routing verdict ("send it to the agendix") is the whole gate; the writes within a pass are not individually reviewed.

Authority lives in the index: `Index.Agendix`, `Writing.Friction.Reduction`, `Kernel.Block.Grounding`, `Inline.Grounding`, `Grounding.Hugentic.Authority`, `Chatlas.Anchory` own the concepts.

## The Two Surfaces, Same Primitives

| primitive | index main + appendix (hugentic) | agendix (agentic) |
|---|---|---|
| unit | `Kernel.Line` under a concept | same |
| significance gate | `Line.Type` + validation point | same — untypeable lines do not enter |
| evidence | grounding lines / inline anchors | same — every line carries an anchor, mandatory |
| concept set | user can mint concepts | primed: existing routed concepts only |
| authority gate | `Edit.Trigger.Gated` + `Content.Verbatim.Gated` | trigger-gated — provenance replaces review |
| surface | chapter files + `appendix/` | `agendix/Concept.X-agendix.md` next to `appendix/` |

## Surface Rules

- only `User.Touched` material enters: summaries of chat discussion — a correction, a decision, a rejection, a boundary, a constraint the index does not yet carry (`Grounding.Hugentic.Authority`: user turns primarily; assistant material only when the user accepted, corrected toward, or acted on it)
- every line is typed: pick the `Line.Type` first (`references/type.md`); a line that takes no type does not enter
- assistant-grounded lines are allowed here (only here), marked on the source axis: `[AS:CT] … @anchor` — the anchor targets the assistant turn; promotion re-grounds on the approving user turn and drops the marker
- every line ends with its anchor: hard provenance, no unanchored agendix lines
- lines attach only under existing routed concepts — no concept minting on this surface; a candidate with no concept goes to the fallback file
- no duplication: content the index, appendix, or agendix already carries does not enter
- unsourced agent reasoning does not belong — every line must be recoverable from the anchored chat neighborhood

## Landing Form

When landing material on the agendix — from `references/capture.md`, an accepted `Capture.Offer` routed here, or any other trigger:

1. **Route** each line under a routed concept. No match → `agendix/Unassigned-agendix.md`, the homeless pool: accumulated evidence that a concept may be missing — promotion evidence, never a dump. A would-be-new-concept block is decomposed the same way: its lines pool under `Unassigned` until the concept earns a gated landing.
2. **Fence**: type each line; drop what cannot take a type.
3. **Anchor**: mint one anchor per line through the linking primitive (`references/link.md`) — chatlas-only session/turn resolution, `Chatlas.Anchory` record shape, `YYYYMMDD-N` keys.
4. **Write** `agendix/Concept.X-agendix.md` in the engaged depot, next to `appendix/` — appendix writing rules, block heading `Concept.X/Agendix`, lines appended:

   ```md
   - [CT] no stable surface links into the agendix — promotion copies content out ^YYYYMMDD-N
   ```

5. **Report** compactly: lines captured per concept, fallback entries, candidates dropped at the fence and why.

## Boundaries

- landing on the agendix modifies no index main, appendix, or router file
- no promotion from this surface: promotion and drop are user decisions on later review; the agendix only accumulates
- the agendix does not restate index content — it holds what the index does not yet capture
- nothing lands without a user trigger; the trigger covers the pass, the writes within it are not individually gated
- agendix content has zero authority — freely rewritable, assumed unreviewed by every reader
