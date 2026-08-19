# Migrate The tarav-pkg Legacy Folders Into The Homes Layout - impl-req

## Impl.Abstract

- **Status:** Open. Designed, not executed.
- **Parent:** `638-tarav2-migration-master-impl-req.md`, Step 5.
- **Scope:** Move `tarav-pkg`'s five legacy folders — 1,941 typed lines — into `homes/`, carrying their existing grounding and approval gates across. Delete the legacy folders as they empty.
- **Out of scope:** grounding anything that is not already grounded, and clearing the POI queue the migration produces. Both are Step 8.
- **Grounding:** none. This is a plan for a one-time move; it asserts nothing that needs a support set.
- **Acceptance:** `tarav index linter` sees all of `tarav-pkg`, no line lost grounding or its gate, and only one layout remains.

## Why This Exists

`homes/` was added beside the old folders rather than replacing them. The new index discovers surfaces with two globs — `skills/*/homes/*/chapters/*.md` and `skills/*/homes/*/appendix/*.md` — so nothing outside `homes/` is opened at all.

The effect is worse than a failing check. A line outside discovery is not `blocked`, it is absent from the denominator: `29 passed, 0 failed, 0 blocked over 50 surface lines` is true, and says nothing about the other 1,941. The report's honesty machinery only covers what discovery already found.

## The Thing That Makes This Cheap

A legacy `^c` anchor is not dead. It resolves today, and its dossier already holds what a record needs:

```
dossier.support.members[]                  →  links.grounding[]
dossier.gates.tokenized_verbatim_approval  →  links.landing (token, proposal turn, approval turn)
dossier.attachment.triplet_hash            →  the type + body + anchor assertion
the anchor                                 →  line.label
```

Sampled across `design/`, every anchor carried support; anchors from late July 2026 onward also carried a token round-trip through a user turn — which is exactly what this design calls a landing gate. Same dossier schema the current system mints.

So this is a **shape transformation**. Nothing is grounded that was not already grounded; the same evidence is re-expressed in the record's vocabulary.

## Placement

A one-time mapping. **Not a rule** — nothing here should be read as a standing policy about which folder kind belongs in which home.

```
design/     1391  →  homes/ceo/chapters/     user home
appendix/    170  →  homes/ceo/appendix/     user home
agendix/     196  ─┐
poi/         179   ├→ homes/agent/chapters/  agent home
issues/        5  ─┘
```

No per-line decision. Placement is by folder, once, and afterwards the record carries meaning rather than the path.

## Alignment Is Not A Precondition

An unreviewed block may sit in the user home. It raises `landing-evidenced`, and that finding says *find its approval turn* — it is a work item, not a violation and not a reason to route the line elsewhere.

The migration is therefore expected to produce a **large pile of findings**, and that pile is the queue. Do not attempt to zero it during the move, and do not place lines to avoid it. The surfaces converge over time.

## What Must Be Fixed First

`tarav index import` is built on a premise that is false:

> *"tarav1's support is `^c` anchors, which no active workflow resolves"* — they resolve.
> *"That tarav1 reviewed a line is not evidence this design can check"* — a token round-trip through a user turn is precisely what this design calls evidence.

As built it lands everything agent-side and ungrounded as `Index.Presumption`. Run unchanged it would discard 1,623 lines of grounding and every gate in the later half, and leave someone re-establishing by hand what was never lost. `637` made that call in good faith; `638`'s `Shape.Transformation` overturned it and the importer has not caught up.

## Execution.Plan

### Slice 1 — Teach the importer to read the dossier
Resolve each line's `^c` anchor and map support members onto `links.grounding` and any tokenized verbatim approval onto `links.landing`. Preserve labels; relabel only on collision.
**Check:** an imported line with a gated dossier lands with `links.landing` populated and `landing-evidenced` quiet. One with support only lands grounded, and raises `landing-evidenced` if it is in the user home.

### Slice 2 — Rehearse on one `design/` chapter
Pick a single chapter and import it to `homes/ceo/chapters/`. `design/` is the right rehearsal because it exercises the gate → user home path; `issues/` would not.
**Check:** grounding and gates survive; the finding count is read and understood rather than fixed.

### Slice 3 — Report triplet mismatches separately
Where `triplet_hash` does not match the line's current text, the line was edited after its approval. That is a different POI from "never approved" and must not fold into the same pile.
**Check:** the import report counts drifted lines apart from ungated ones.

### Slice 4 — Migrate the four remaining folders
`agendix/` and `issues/` (fully anchored) to the agent home, `appendix/` to the user home, then the rest of `design/`.
**Check:** every folder's typed-line count is accounted for in the new layout.

### Slice 5 — `poi/` on its own terms
153 of its 179 lines carry no anchor, so most of it is not a shape transformation at all. Move what is anchored; the rest is capture-loop work and belongs to Step 8.
**Check:** the unanchored remainder is named as a count, not silently imported as if equivalent.

### Slice 6 — Delete the legacy folders
Each folder goes as it empties.
**Check:** `tarav-pkg` has one layout; the linter's surface-line count reflects the whole depot.

## Slice Status

| # | Slice | Status |
|---|---|---|
| 1 | importer reads the dossier | not started |
| 2 | rehearse on one `design/` chapter | not started |
| 3 | triplet mismatches reported apart | not started |
| 4 | migrate the four remaining folders | not started |
| 5 | `poi/` on its own terms | not started |
| 6 | delete the legacy folders | not started |

## Impl.Log

- Measured at authoring: `design/` 1391 typed / 1229 anchored, `appendix/` 170 / 167, `agendix/` 196 / 196, `poi/` 179 / 26, `issues/` 5 / 5. Totals 1,941 typed and 1,623 anchored. Take fresh counts before executing.
- The gate cutoff is approximate. A sample of twelve `design/` anchors showed gates from 2026-07-29 onward and none before. Nobody has counted the split across all 1,229, and the size of the resulting POI queue follows from it.
- Two layouts standing side by side is what hid these lines. Slice 6 is not tidying; it is the slice that stops the failure recurring.
