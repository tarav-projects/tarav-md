# agentos-pkg Index — Conflict Report

> Diagnosis-only (`Maintenance.System`: report-first, evidence-based). No fixes applied.
> Scope: all `skills/agentos-pkg/index/` flat files `000`–`106`. Date: 2026-06-12.
> Each issue: involved blocks (with file) + short problem statement.

Counts: 3 contradictions/wrong-refs · 4 naming-drift · 2 dangling-refs · 3 coverage-gaps · 3 overlaps · 3 minor.

Status: **A1, A3 resolved** 2026-06-12 — established the rule that index blocks name concepts inline and never point at `NNN-index.md` (the `000` router resolves location); applied to `Alignment.Loop`, `Conceptual.Space`, `Impl.Req`, `Development.Principles`.

---

## A. Contradictions & wrong cross-references

### A1. `Alignment.Loop` — broken `How.Design` specialization pointer
- blocks: `Alignment.Loop` (`102`)
- "see `102-index.md` for `How.Design` specialization" points at its own file, and no `Alignment.Loop:How` block exists anywhere. (The `What.Design` sibling pointer was corrected to `106`; this one was not.)
- **RESOLVED 2026-06-12**: both `see NNN-index.md` lines removed; the `:What`/`:How`/`:Exec` specializations are already named inline and the router resolves them. (A2 — the missing `:How`/`:Exec` blocks — is a separate, still-open question.)

### A2. `Alignment.Loop:How` / `Alignment.Loop:Exec` — promised but undefined
- blocks: `Alignment.Loop` (`102`), `Impl.Req` (`102`, uses `Alignment.Loop:How`)
- the loop is declared "parameterized by phase `:What`/`:How`/`:Exec`" and `Impl.Req` cites `Alignment.Loop:How`, but only `:What` has a block (`106`). `:How`/`:Exec` have no blocks — gap is fine as `Dangling.Cite`, but A1 actively promises the definition.

### A3. `Development.Principles` — "definitions in 102" but one lives in 105
- blocks: `Development.Principles` (`102`), `RED.GREEN.Test.Suite` (`105`)
- the block lists `RED.GREEN.Test.Suite` and says "see `102-index.md` for definitions", but that block is in `105`. Partially stale pointer.
- **RESOLVED 2026-06-12**: the `see 102 for definitions` line was removed under the inline-only rule; the stale file pointer no longer exists.

---

## B. Naming drift — same idea, multiple unregistered names

### B1. Workflow-skill name family is inconsistent
- blocks: `Workflow.Neutral.Skill` (`101`), `Aux.Workflow.Skill` (`101`), `Usage.Workflow` (`105`, uses bare `Workflow.Neutral`), `Usage.Skill` (`101`, uses `Workflow.Skill`)
- `Workflow.Neutral` and `Workflow.Skill` appear as concepts but have no blocks; canonical names are `Workflow.Neutral.Skill` / `Aux.Workflow.Skill`. Can't tell if same or distinct.

### B2. Index-notes name variants
- blocks: `Agentos.Index.Notes` (`100`), `Index.Runtime` (`103`, "`Index.Notes` are the data"), `Soft.Programming.Language` (`103`, "module → `Index.Note`")
- `Index.Notes` and `Index.Note` are used as if defined; the registered concept is `Agentos.Index.Notes` (and `Kernel.Note` for the portable container). Three names blur.

### B3. `Reference.Implementation` vs `Canonical.Reference.Implementation`
- blocks: `Reference.Implementation` (`100`), `Natural.Placement` (`100`, uses `Canonical.Reference.Implementation`)
- Natural.Placement introduces `Canonical.Reference.Implementation` as a concept; only `Reference.Implementation` has a block. Unregistered variant/alias.

### B4. `Hugentic.Concept` block defines `Hugentic`
- blocks: `Hugentic.Concept` (`103`)
- routed/heading name is `Hugentic.Concept` but the body defines the bare term `Hugentic`. Name vs subject mismatch.

---

## C. Dangling references to undefined concepts

### C1. `Index.Depot` cites `Agentos.Index.Framework`
- blocks: `Index.Depot` (`104`)
- "built on the `Agentos.Index.Framework`" — no such block; the system concept is `Agentos.Index.System` / `Agentos.Index`. Likely a wrong/renamed reference.

### C2. `Soft.Programming.Language` cites `Index.Block.Syntax`
- blocks: `Soft.Programming.Language` (`103`)
- "type system → `Index.Block.Syntax`" names a concept with no block and no other mention. Dangling (same mapping also uses the undefined `Index.Note`, see B2).

---

## D. Coverage gaps — referenced widely, no block

### D1. `Public.Surface` / `Local.Surface`
- blocks referencing them: `Surface.Link.Directionality` (`100`), `Usage.Surface` (`101`), `Surface.Concept` (`103`, defines them inline only)
- both are used as first-class concepts across blocks but have no routed block — defined only inline inside `Surface.Concept`.

### D2. Loop-step concepts `Alignment.Question` / `Alignment.Discussion` / `Alignment.Consolidation`
- blocks referencing them: `Alignment.Loop` (`102`), `Impl.Req` (`102`), `Alignment.Loop:What` (`106`)
- the three named loop steps appear throughout but have no blocks (inline only). Possibly intentional soft; flagged against `Index.Concept.Coverage`.

### D3. `Provider.Family`
- blocks: `Provider.Instance` (`104`)
- Provider.Instance is defined entirely in terms of `Provider.Family`, which has no block.

---

## E. Overlap / unclear boundaries

### E1. `Usage.Workflow` vs `Package.Skill.UsagePattern`
- blocks: `Usage.Workflow` (`105`), `Package.Skill.UsagePattern` (`101`)
- both are "named situation → operational guidance," in different folders (`usage-workflows/` vs `usage-patterns/`), and the relationship is never reconciled. Unclear when to use which, or whether one deploys the other.

### E2. `Surface.Concept` vs `Surface.Types`
- blocks: `Surface.Concept` (`103`), `Surface.Types` (`103`)
- two "kinds of surface" taxonomies on different axes (character: Stable/Public/Md vs function: Codebase/Index/Skills/Docs/Chat) sharing the "surface type" vocabulary, with no explicit statement of how the axes relate.

### E3. `Distributed.Index` vs `Index.Depot` vs `Index.Surface.Layout` — repeated structural facts
- blocks: `Distributed.Index` (`103`), `Index.Depot` (`104`), `Index.Surface.Layout` (`104`)
- the same public/local split, `100-299`/`300-499` ranges, and two-router facts are restated in all three (uncited duplication) — a `Placement.Balance` smell; one edit drifts the others.

---

## F. Minor tensions

### F1. `Maintenance.System` (diagnose-only) vs `Index.Writer.Maintenance.Pass` (updates)
- blocks: `Maintenance.System` (`100`), `Index.Writer.Maintenance.Pass` (`100`)
- Maintenance.System: "diagnosis-first, not fix-first ... user decides"; the writer pass "may update clear cited duplicates in the same approved write pass." Different scopes, but reads as a mild fix-vs-diagnose contradiction without a reconciling line.

### F2. `Design.Index` (artifact section) vs `Design.Index.Block` (alias)
- blocks: `Kernel.Block:Design` (`100`, alias `Design.Index.Block`), `Designer.Turn.Kernel.Form` (`105`), `Alignment.Backend:Artifact:What` (`106`)
- `Design.Index` names an artifact section; `Design.Index.Block` is an alias of `Kernel.Block:Design`. Near-identical names, different referents.

### F3. `Distributed.Index` still narrates automatic loading
- blocks: `Distributed.Index` (`103`), `Agentos.Index.Notes` (`100`), `Index.Activation` (`104`)
- "a fresh agent ... loads only `000-index.md`" reads as automatic, against the new "the index has no loading policy of its own / activation is opt-in." Softened earlier but phrasing still implies auto-load.
