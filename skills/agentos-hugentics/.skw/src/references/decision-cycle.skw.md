> $kw: --from Context.Grounding --from Index.Presumption --from Open.Inference --from POI.Instance --from Product.Design.Session --from Touched.Authority --from Touched.Data --from Touched.Decision.Cycle
> --dev-from references/index-context-assembly.skw.md

# Touched.Decision.Knowledge.Module

Use this workflow-neutral module whenever index work makes a decision or advances a `Target.Product`. It operationalizes `Touched.Decision.Cycle` beneath search, design, capture, implementation, and reconciliation; it does not replace their distinct purposes.

`Product.Design.Session` repeats the cycle inside its open concerns. `Context.Grounding` contextualizes; `Touched.Authority` constrains; `Open.Inference` completes the unresolved region.

## Contextualize

1. Name the active decision and the target product it affects.
2. Run index grounding as the cheap first pass for historical touch.
3. Classify relevant live lines by grounded authority or ungrounded index presumption.
4. Descend through support references when the digest is insufficient, disputed, stale, or consequential.
5. Load adjacent non-touch evidence such as code, documentation, Git history, and runtime state when it changes the valid answer region.
6. Turn incoherence, ambiguity, and unresolved applicability into explicit `POI.Instance`s before treating the evidence as guidance.

Contextualization is read-only. It conditions action but does not mutate a surface.

## Act

- coherent applicable `Touched.Data` constrains the valid answer region
- `Index.Presumption` participates with weaker, defeasible weight
- `Open.Inference` completes whatever the evidence leaves unresolved
- the agent may proceed without waiting for more touch when a coherent provisional action exists
- action must preserve unresolved touched positions as evidence rather than silently rewriting them

## Reconcile

1. Compare the changed target product with its touched design and adjacent implementation surfaces.
2. Surface new contradictions, stale projections, missing grounding, or uncovered relevant touch as POIs.
3. Decide whether the product, the index, another projection, or nothing should change; a POI never dictates the remedy.
4. Route every surface mutation through that surface's own gate.
5. Re-contextualize after a material reconciliation because the live cut and support network may have changed.

Reconciliation may keep, ground, modify, add, replace, remove, reorganize, demote, or deliberately leave material unresolved.

## Workflow Composition

- `--search` primarily contextualizes and reports; it does not reconcile by writing
- `--design` repeats the cycle inside whichever What/How/Exec concerns remain open
- `--capture` contextualizes candidate touch, acts by drafting a curated projection, and reconciles only after a landing command
- `--edit` performs a gated reconciliation already selected by prior reasoning
- `--reconcile` runs the complete cycle explicitly against a changed product
- implementation workflows apply the same cycle inside their own How/Exec products

`What.Design`, `How.Design`, and `Impl.Exec` remain an abstraction gradient. They are concerns exposed when unresolved, not mandatory sequential stages.
