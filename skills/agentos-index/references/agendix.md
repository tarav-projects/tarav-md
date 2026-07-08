# agentos-index --agendix

Use this module when the user triggers agendix capture: harvesting `User.Touched` material from the current conversation into the `Index.Agendix`.

This module is NOT `Workflow.Neutral` — it runs a capture workflow and writes agendix files. It is the agentic path of the same alignment workflow `--edit` runs hugentically: same primitives — `Kernel.Line`s, `Line.Type`s, anchors, the current concept set — with the user gate replaced by hard provenance.

Authority lives in the index: `Index.Agendix`, `Writing.Friction.Reduction`, `Kernel.Block.Grounding`, `Inline.Grounding`, `Grounding.Hugentic.Authority`, `Chatlas.Anchory` own the concepts.

## The Two Paths, Same Primitives

| primitive | hugentic path (`--edit`) | agentic path (`--agendix`) |
|---|---|---|
| unit | `Kernel.Line` under a concept | same |
| significance gate | `Line.Type` + validation point | same — untypeable lines do not enter |
| evidence | grounding lines / inline anchors | same — every line carries an anchor, mandatory |
| concept set | user can mint concepts | primed: existing routed concepts only |
| authority gate | `Edit.Trigger.Gated` + `Content.Verbatim.Gated` | user-triggered, not gated — provenance replaces review |
| surface | index main + appendix | `agendix/Concept.X-agendix.md` next to `appendix/` |

## Capture Rules

- capture only `User.Touched` material: summaries of chat discussion — a correction, a decision, a rejection, a boundary, a constraint the index does not yet carry (`Grounding.Hugentic.Authority`: user turns primarily; assistant material only when the user accepted, corrected toward, or acted on it)
- every line is typed: pick the `Line.Type` first (`references/type.md`); a line that takes no type does not enter
- every line ends with its anchor: hard provenance, no unanchored agendix lines
- attach only under existing routed concepts — the agent cannot mint concepts; a candidate with no concept goes to the fallback file
- no duplication: skip content the index, appendix, or agendix already carries
- unsourced agent reasoning does not belong — every line must be recoverable from the anchored chat neighborhood

## Capture Loop

1. **Scan** the recent conversation for touched, significant, un-captured material. Use `--ground` behavior to compare against the engaged depot: what the index already models is out; gaps and fresh touch are candidates.
2. **Route** each candidate to a routed concept. No match → `agendix/Unassigned-agendix.md`, the homeless pool: accumulated evidence that a concept may be missing — promotion evidence, never a dump.
3. **Fence**: type each line; drop what cannot take a type.
4. **Anchor**: mint one anchor per line through the linking primitive (`references/link.md`) — chatlas-only session/turn resolution, `Chatlas.Anchory` record shape, `YYYYMMDD-N` keys.
5. **Write** `agendix/Concept.X-agendix.md` in the engaged depot, next to `appendix/` — appendix writing rules, block heading `Concept.X/Agendix`, lines appended:

   ```md
   - [CT] no stable surface links into the agendix — promotion copies content out @YYYYMMDD-N
   ```

6. **Report** compactly: lines captured per concept, fallback entries, candidates dropped at the fence and why.

## Boundaries

- do not modify index main, appendix, or router files from this module — capture only
- do not promote: promotion and drop are user decisions on later review; this module only accumulates
- do not restate index content into the agendix — the agendix holds what the index does not yet capture
- do not capture without a user trigger; the trigger is per-pass, the writes within a pass are not individually gated
- agendix content has zero authority — freely rewritable, assumed unreviewed by every reader
