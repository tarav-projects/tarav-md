# Skw.Ann.Dependency — Appendix

****

## Skw.Ann.Dependency/Appendix

Derivation mechanics and address depth, absorbed from the retired `Derivation.Rule`, `Derived.Content`, `Derived.Module`, and `Skillware.Recipe` blocks.

- a derivation is the relation `Dependencies + Context → Derived`: run forward it (re)generates the derived content; run as a check it answers the drift question — does the current derived still match what its dependencies + context would now produce? ^c20260709-14u
- the check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps — and maintenance is derivation's main cost
- context is everything informing the derivation other than the declared dependencies — from implicit (the derived surface itself + ambient knowledge) to explicit (written down); dependencies and context span inline + external
- the `copy` binding needs no rule — equality is its whole check ^c20260709-14u
- derived-ness is granular and a ratio: any span may be derived, the rest is original content; the more derived or imported a surface, the more its maintenance automates — human work stays at the seams with original content
- targets are addressed by `Skw.Address.Schema` names — `Dotted.Name`s for blocks, `Locator.Name`s for files, regions, and spans, `Anchory.Anchor`s for chat moments ^c20260712-10u
- v1 recipe realization: declarations were `[!skw]` recipe callouts inline in `.skw.md` src, declaration and current solution side by side; the toolchain materializes `copy` and `derived` — `pointer` remains routed prose, not yet toolchain-checked ^c20260710-2u
- [RJ] `Import.Manifest` — a separate flat artifact per consuming module — was superseded before implementation: declarations live inline; `lock.json` is the machine record ^c20260709-13u ^c20260710-2u

****

## Skw.Ann.Dependency/Context.Assembly.Coverage

- [DF] an assembly-covered source is a dependency target included within a `Context.Assembly.Module` context boundary ^c20260725-33u
- [DC] every dependency role using an assembly-covered source requires a companion `--dev-from` edge to each covering assembly ^c20260725-33u
- [PR] a missing companion edge raises `context-assembly-bypass` because the builder may lack the shared subject context; the direct dependency remains valid ^c20260725-33u
- [RJ] coverage is not ownership or import mediation and does not restrict direct dependency, copy, derivation, or citation ^c20260725-33u
- [CT] `--dev-from` governs development context and does not force the assembly into the running agent’s workflow context ^c20260725-33u
