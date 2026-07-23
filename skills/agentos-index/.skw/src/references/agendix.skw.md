# agentos-index --agendix

> $kw: --from Capture.Gradient --from Capture.Offer --from Edition.Trigger.User.Gated --from Grounding.Hugentic.Authority --from Index.Agendix --from Index.Line --from Kernel.Block --from Kernel.Line --from Line.Type --from Verbatim.User.Gated --from Writing.Friction.Reduction

The knowledge of the `Index.Agendix` surface: what it is, what may enter it, and the form material takes to land there.

This module is a `Workflow.Neutral.Module`: it runs no workflow — its rules bind whenever material lands on the agendix, whichever module has control. The capture workflow that harvests chat content lives in `references/capture.md`; `--agendix` runs that workflow with the agendix as preset destination.

The agendix is the agentic path of the same alignment writing the index runs hugentically: same primitives — `Kernel.Line`s, `Line.Type`s, anchors, the current concept set — with the user's review gate replaced by hard provenance. On the `Capture.Gradient` it sits **touched, captured, ungated**: a user routing verdict ("send it to the agendix") triggers the pass, and the writes within it are not individually reviewed — the gate buys stability, not authority; authority lives per-line in its `Chat.Support.Set`.

Authority lives in the index: `Index.Agendix`, `Writing.Friction.Reduction`, `Index.Line`, `Grounding.Hugentic.Authority`, `Chatlas.Anchory` own the concepts.

## The Two Surfaces, Same Primitives

| primitive | ontology + appendix (hugentic) | agendix (agentic) |
|---|---|---|
| unit | `Kernel.Line`s and `Kernel.Block`s | same — lines and candidate blocks, same forms |
| significance gate | `Line.Type` + validation point | same — untypeable lines do not enter |
| evidence | grounding lines / inline anchors | same — every line carries an anchor, mandatory |
| concept set | user can mint routed concepts | primed: candidate names only, attached under routed concepts |
| authority gate | `Edition.Trigger.User.Gated` + `Verbatim.User.Gated` | ungated, user-triggered — provenance replaces review |
| surface | chapter files + `appendix/` | `agendix/Concept.X-agendix.md` next to `appendix/` |

## Surface Rules

- the agendix holds touched but ungated material: summaries of chat discussion — a correction, a decision, a rejection, a boundary, a constraint the index does not yet carry — every line grounded by its `Chat.Support.Set` of user turns, no line's wording passed the user gate
- assistant-grounded capture is excluded: anchors target user turns; assistant material enters only through the user turn that touched it (`Grounding.Hugentic.Authority`: accepted, corrected toward, or acted on)
- every line is typed: pick the `Line.Type` first (`references/type.md`); a line that takes no type does not enter
- every line ends with its anchor: hard provenance, no unanchored agendix lines
- entries may group into blocks — the appendix's block forms apply; a candidate block attaches as a path-child of a routed concept (`Concept.X/Agendix/Candidate.Name`)
- no routed-concept minting on this surface — a candidate block's name is provisional: unrouted, citable from unreviewed surfaces but not reviewed ones (`Reviewed.Cite.Closure`); promotion may rename it
- cite the agendix only through file-referenced line quotes (`--from <agendix-file>` + `--quote`) — its block names are provisional, so block-name cites are disallowed, not merely discouraged
- no duplication: content the index, appendix, or agendix already carries does not enter
- unsourced agent reasoning does not belong — every line must be recoverable from the anchored chat neighborhood

## Landing Form

When landing material on the agendix — from `references/capture.md`, an accepted `Capture.Offer` routed here, or any other trigger:

Present the landing target before the draft text:

```md
Landing: <depot>/agendix/Concept.X-agendix.md
Target: append under ## Concept.X/Agendix
```

For candidate blocks, name the attachment path: `Target: create ## Concept.X/Agendix/Candidate.Name`. For unrouted material, show `Landing: <depot>/agendix/Unassigned-agendix.md` and the provisional target path.

1. **Route** each entry under a routed concept — a line appends to `Concept.X/Agendix`, a candidate block attaches intact as `Concept.X/Agendix/Candidate.Name`. No routed concept → `agendix/Unassigned-agendix.md`, the homeless pool: accumulated evidence that a concept may be missing — promotion evidence, never a dump; an intact candidate block there is the strongest form of that evidence.
2. **Fence**: type each line; drop what cannot take a type.
3. **Anchor**: mint one anchor per line through the linking primitive (`references/link.md`) — chatlas-only session/turn resolution, `Chatlas.Anchory` record shape, composed `c<YYYYMMDD>-<N><tag>` keys.
4. **Write** `agendix/Concept.X-agendix.md` in the engaged depot, next to `appendix/` — appendix writing rules, block heading `Concept.X/Agendix`, lines appended:

   ```md
   - [CT] `Reviewed.Cite.Closure`: reviewed surfaces may not cite the agendix, unreviewed surfaces may — promotion copies content out before an index cite ^c<YYYYMMDD>-<N>u
   ```

5. **Report** compactly: lines captured per concept, fallback entries, candidates dropped at the fence and why.

## Boundaries

- landing on the agendix modifies no ontology, appendix, or router file
- no promotion from this surface: promotion and drop are user decisions on later review; the agendix only accumulates
- the agendix does not restate index content — it holds what the index does not yet capture
- nothing lands without a user trigger; the trigger covers the pass, the writes within it are not individually gated
- agendix content is unreviewed, not authority-less — its lines carry `Touched.Authority` per their `Chat.Support.Set`; what they lack is the reviewed wording, so a reader treats them as freely rewritable leads, not accepted wording
