# Agentos.Skillware - design-session

## Session.Abstract

- intent: define the `Agentos.Skillware` ontology — treating skills as the unit of software for agents, with a module model whose content can be derived from sources and maintained automatically — so workflow variants (e.g. a project-tuned `Impl.Req`, a domain `Normalization.Pipeline`) can be produced and maintained instead of forked.
- active focus: the derivation model — `Derivation.Rule` (atom), `Derived.Content`, `Module.Dependency.Management`, the derivation surface (`Derivation.Surface.Arch` + `Derivation.Manifest`), and the `Original ↔ Derived` module spectrum.
- references: `agentos-pkg` index (`Skill.Module`, `Skill.Package`, `Batchy.Skills`, `Cited.Duplication`, `Natural.Placement`, `Deep.Modules`, `General.Avoids.Specific`, `Appendix.Discovery`, `Index.Surface.Layout`, `Normalization.Pipeline`, `Impl.Req`, `Kernel.Writing`); origin discussion in a g702-03 normalization-pipeline design thread.
- graduation target: the `agentos-pkg` index, once blocks stabilize.
- state: active.
- next: decide whether `Original.Module` and the build-plane / runnable-plane split earn their own blocks; sketch a second explicit codification beyond the manifest to test the inline↔external spectrum.

## Design.Index

### Agentos.Skillware

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents, bringing software shape (packaging, dependencies, modules, builds, versions, lineage) to it.
- "as software" means the artifacts agents run stop being flat, standalone prose and gain engineering structure — composed, depended-upon, built, and versioned — so they can be reused and evolved rather than written once and forked.
- a discipline realized by capabilities, not a single mechanism — it names the stance; specific members implement it.

#### appendix

- evaluated by capabilities, not a rigid design — what a build takes in and emits is tunable; no one-fits-all.
- the compiler is an agent — derivation is semantic; Skillware enforces *discipline* (dependency tracking, captured context for reproducibility), not a deterministic mechanism. Determinism is added later, only where a stage proves mechanical.
- medium constraint — **context is executable**: data in a runnable object biases the run, so build/dev material never ships inside it. Skillware separates a **build plane** from a **runnable plane**.
- recurring spine: *keep sources + recipe, treat outputs as regenerable* — the db (`raw`/`normalized`), `Normalization.Pipeline`, and now skill builds.

#### meta

- status: new, design-stage.
- members: `Skill.Package`, `Batchy.Skills`, `Skill.Module`, `Module.Dependency.Management`, `Derivation.Manifest`.
- cross-links: `Normalization.Pipeline` (shared closure idea).
- open: name `Skillware` provisional; build-plane / runnable-plane split may deserve its own block.

### Skill.Module

- `Skill.Module` is a named, encapsulating subsystem of a skill — a bounded unit with an addressable name and hidden internals.
- materially it is a file or section of the skill, addressable by name and loaded on demand (progressive disclosure).
- dependents bind to its name and boundary, never its internals — a `Deep.Module`: narrow surface, hidden depth.

### Runnable.Surface

- `Runnable.Surface` is a surface whose purpose is to be **run** — loaded into agent context to do work; its content is the executable substance and nothing else.
- the system keeps it free of non-runnable artifacts — build, derivation, lineage, and dev material belong on a `Build.Surface`, so they neither obscure nor dilute what runs.
- forced by **context is executable** — anything on a runnable surface is read into context and shapes the run; secondary-function artifacts there are not inert, they interfere.

#### appendix

- a functional classification, orthogonal to public/local — e.g. a skill's executable content is a `Runnable.Surface`.
- it is a materialized projection in the sense of `Chat.Surface.Closure` — re-derivable from its sources, so keeping it clean costs nothing in recoverability.

### Build.Surface

- `Build.Surface` is the complement of `Runnable.Surface` — it holds the artifacts that produce and maintain runnable content, and is never loaded at run time.
- the home for everything kept off the runnable surface: derivation context, dependency declarations, lineage, dev material.
- never run, it carries no "stay clean" constraint — an unconstrained workspace; that freedom is what the two-surface split buys.

#### meta

- `Derivation.Surface.Arch` (the `derivation/` folder) is a `Build.Surface` instance.

### Derivation.Rule

- `Derivation.Rule` is the model's atom: the relation `Dependencies + Context → Derived` — derived content produced from its declared dependencies, interpreted through a context.
- `Context` is everything informing the derivation other than the declared dependencies (interpreted case by case) — from implicit (the derived surface itself + ambient knowledge) to explicit (a written `Derivation.Manifest`).
- both roles span **inline + external** — dependencies and context may live inline in the derived surface (e.g. inline `Dotted.Names`) or external on the derivation surface; the manifest is the home for whatever isn't carried inline.
- run **forward** it (re)generates the derived; run as a **check** it answers the drift question — does the current derived still match what its dependencies + context would now produce?
- the check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps — and maintenance is derivation's main cost.

### Derived.Content

- `Derived.Content` is the *Derived* output of a `Derivation.Rule` — content regenerable from declared dependencies plus a context, a projection of those sources rather than authored standalone.
- granular — any span of a module can be `Derived.Content`; the rest is original content. The "original/derived ratio" is just how much of a module is `Derived.Content`.
- regenerable ⇒ its maintenance is automatable — re-project when sources change; the delta is captured in its `Context` (inline, or an explicit `Derivation.Manifest`).

### Module.Dependency.Management

- `Module.Dependency.Management` is the part of the Skillware module model that maintains a module's `Derivation.Rule`s — automating the regeneration and drift-checking of its `Derived.Content`.
- it records, per derived span, the dependencies (by durable address) and the context, and runs the recurrence `current + dependencies + context → updated`.
- maintenance cost tracks the original/derived ratio — derived parts re-project automatically; original content, and its merge seam with re-projected content, is where human discussion is required.
- general by design — it serves both granularities (fragment via `Cited.Duplication`, whole module) and the whole original↔derived spectrum; summarization etc. are just context values, never special cases.

#### appendix

- dependency expression varies by surface: index dependencies ride implicit machinery (`Dotted.Notation`, `Inline.Relatedness`) and are universal — a `Natural.Placement` consequence; module-to-module dependencies are explicit and asymmetric. This is orthogonal to the original/derived ratio.
- dependencies are addressed via the in-place linking mechanism — `Dotted.Names` for index/module blocks, `Chat.Ref`/`Chat.Grounding` for chat fallback dependencies.

### Derived.Module

- `Derived.Module` is a `Skill.Module` whose content is mostly `Derived.Content` — the high-derivation pole.
- source-agnostic — its sources may be index blocks or other modules; derived-ness is the ratio, not the surface.
- maintenance is mostly automatable — being largely a projection of its sources, it re-derives when they change; human attention concentrates at the seam with any original content.

#### appendix

- common case: grouping/summarizing sparse sources into a better-packaged, more self-contained module — the module-scale of `Cited.Duplication`.
- contrast pole: an `Original.Module` is mostly authored content; it may carry some `Derived.Content` in support, but it does not dominate.

### Derivation.Surface.Arch

- `Derivation.Surface.Arch` is the layout of the canonical derivation surface: a `derivation/` folder (build-plane) holding a skill's explicit `Derivation.Manifest`s, kept out of the runnable surface.
- per-file mirror — `derivation/<name>.md` mirrors the derived file's name, discovered implicitly (check if it exists); the default, no registry needed.
- router — `derivation/002-index.md` routes the surface; listing is cheap, so it lists every derivation and carries the multi-output/subsystem cases the 1:1 mirror can't express.
- discovery is convention-based — a maintainer or agent always knows where a derivation's context lives, mirroring `Appendix.Discovery`.

#### meta

- parallels `Index.Surface.Layout`; the `002` router is derivation-local, borrowing the `NNN-index` naming.
- a `Build.Surface` — build-plane, kept out of the `Runnable.Surface`.
- alt name considered: `Derivation.Surface.Layout`.

### Derivation.Manifest

- `Derivation.Manifest` is the explicit artifact for a `Derivation.Rule` — it carries the parts of the rule (declared **dependencies** + external **`Context`**) not already inline in the derived surface.
- it lives on the derivation surface — `derivation/<name>.md` mirrors the derived file (discovered by name), routed by `derivation/002-index.md`.
- **build-plane, never runnable** — it keeps derivation context out of the clean runnable surface (context is executable).
- it names each dependency by a **durable address** and holds the external context, so a maintainer or agent can re-derive and drift-check from one known place.

#### appendix

- the reproducibility floor is **addressability** — a dependency with no durable address (an ephemeral chat with no `chatlas` entry) can't be re-derived; inlined or pointer, both fine above the floor.
- one manifest can cover several derived spans in its file, or a whole subsystem; it may also declare the derived output's self-containment (linked vs. vendored).

#### meta

- the **explicit/external** end of codifying a `Derivation.Rule`; the **implicit/light** end is inline `Dotted.Names` in the derived surface itself.
- renamed from `Skill.Makefiles`; absorbs the former `Derivation.Design` (explicit context is just what the manifest holds).

## Session.Log

- 2026-06-21 — session opened. Captured seed blocks from a g702-03 normalization-pipeline discussion. Blocks marked immature.
- 2026-06-21 — pulled hugentic-design + `Kernel.Writing` fundamentals via `Packages.Master.Agent`; adopted `Designer.Turn.Kernel.Form`. Matured `Agentos.Skillware` and `Skill.Module`. Wrote `General.Avoids.Specific` to the `agentos-pkg` index (`106-index.md`).
- 2026-06-21 — restructured around the derivation atom: `Derivation.Rule`, `Derived.Content`, `Module.Dependency.Management`; recast `Derived.Module` as the high-derived pole (`Original.Module` folded into its appendix).
- 2026-06-21 — refined the atom to `Dependencies + Context → Derived` (Context = everything but declared deps; implicit↔explicit), with both deps and context spanning inline + external. Renamed `Skill.Makefiles → Derivation.Manifest` and folded in the former `Derivation.Design`. Added `Derivation.Surface.Arch` (the `derivation/` folder, per-file mirror, `002` router, convention-based discovery).
- 2026-06-21 — added the surface split as general blocks: `Runnable.Surface` (purpose is to be run; kept free of non-runnable artifacts because context is executable) and `Build.Surface` (its complement, holds derivation/dev artifacts, never run). Cross-linked `Chat.Surface.Closure` (the regenerable-projection spine is already canon). Noted chat fallback dependencies via `Chat.Ref`/`Chat.Grounding`.
- 2026-06-21 — graduated to the `agentos-pkg` index. New `107-index.md`: `Agentos.Skillware` (`Explicit.Namespace`), `Skill.Runnable.Surface`, `Skill.Build.Surface` (renamed with `Skill.` prefix), `Derivation.Rule`, `Derived.Content`, `Module.Dependency.Management`, `Derived.Module`, `Derivation.Surface.Arch`, `Derivation.Manifest`. `Skill.Module` generalized in `101` (Batchy view preserved as scoped block `Batchy.Skill/Skill.Module` in `appendix/Batchy.Skill-appendix.md`). `Original.Module` left implicit. Router updated; linter clean (0/0/14).
