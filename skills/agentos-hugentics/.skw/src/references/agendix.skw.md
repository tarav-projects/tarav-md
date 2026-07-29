# agentos-hugentics --agendix

> $kw: --from Capture.Gradient --from Capture.Offer --from Edition.Trigger.User.Gated --from Index.Agendix --from Index.Line --from Kernel.Block --from Kernel.Line --from Line.Type --from Reviewed.Cite.Closure --from Support.Set --from Touch.Authority.Surface --from Touched.Authority --from Touched.Data --from Verbatim.User.Gated
> --dev-from references/index-context-assembly.skw.md

The knowledge of the `Index.Agendix` surface: what it is, what may enter it, and the form material takes to land there.

This module is a `Workflow.Neutral.Module`: it runs no workflow — its rules bind whenever material lands on the agendix, whichever module has control. The capture workflow that harvests chat content lives in `references/capture.md`; `--agendix` runs that workflow with the agendix as preset destination.

The agendix is the agentic path of the same alignment writing the index runs hugentically: same kernel primitives, but no per-line review gate. On the `Capture.Gradient` it sits **touched, captured, unreviewed**: each `Index.Line` projects `Touched.Data`, while its authority derives independently from its resolvable `Support.Set`.

The current realization accepts only qualifying user-turn evidence through Chatlas and Anchory. This is an implementation specialization of `Touch.Authority.Surface`, not a general restriction of the agendix model.

## The Two Surfaces, Same Primitives

| primitive | ontology + appendix (hugentic) | agendix (agentic) |
|---|---|---|
| unit | `Kernel.Line`s and `Kernel.Block`s | same — lines and candidate blocks, same forms |
| significance gate | `Line.Type` + validation point | same — untypeable lines do not enter |
| evidence | `Support.Reference` / `Support.Set` | same — every line carries resolvable support |
| concept set | user can mint routed concepts | primed: candidate names only, attached under routed concepts |
| authority gate | `Edition.Trigger.User.Gated` + `Verbatim.User.Gated` | ungated, user-triggered — provenance replaces review |
| surface | chapter files + `appendix/` | `agendix/Concept.X-agendix.md` next to `appendix/` |

## Surface Rules

- the agendix holds touched but unreviewed material: summaries of qualifying authority-surface data that the reviewed index does not yet carry
- in the current chat specialization, every line resolves to one or more qualifying user turns; assistant material enters only through user acceptance, correction, rejection, action, or delegation that qualifies as touch
- preset or administrative user turns with no relevant touch do not become support merely because they are user-authored
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
3. **Support**: build one `Support.Set` per line through `references/link.md`; the current implementation mints a trailing Anchory anchor over qualifying Chatlas user-turn members.
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
- agendix content is unreviewed, not authority-less — grounded lines carry `Touched.Authority` through their support sets; what they lack is reviewed wording, so a reader treats them as freely rewritable leads rather than accepted wording
