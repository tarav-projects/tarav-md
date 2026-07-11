# agentos-skillware --about (doctrine)

Use this module to understand Skillware: the mental model behind skills developed as software. It is a self-contained `Cited.Duplication` of the `Agentos.Skillware` namespace in the `agentos-pkg` index (107) — the index owns the concepts; this module makes an agent operational without leaving the skill.

## The Model

> [!skw]- derived
> from: Agentos.Skillware
> from: Skill.Runnable.Surface
> from: Skill.Build.Surface
> from: Module.Import
> from: Skillware.Recipe
> from: Derivation.Rule
> from: Derived.Content
> intent: the self-contained doctrine — restate the 107 cluster as one
> coherent narrative an agent can hold: discipline, two surfaces, imports
> and bindings, the recipe form, derivation and its drift check; stay
> faithful to the blocks, do not invent mechanics

**Skills as software.** `Agentos.Skillware` treats the skill as the unit of software for agents: the artifacts agents run gain engineering structure — modules, dependencies, builds, lineage — so they are reused and evolved rather than written once and forked. A toolchain spanning agentic and CPU work moves package maintenance off the human.

**Two surfaces.** A skill splits into a `Skill.Runnable.Surface` — loaded into agent context to do work, carrying only executable substance, kept clean because anything on it shapes the run — and its complement, the `Skill.Build.Surface`: everything that produces and maintains runnable content, never loaded at run time, an unconstrained workspace. It is realized as the per-package `.skillware/` folder and constitutively carries an engine-stamped `AGENTS.md` redirecting agents outside skillware activity.

**Imports.** A `Module.Import` is a declared dependency between surfaces — the consumer declares, the imported surface never knows its importers. Three binding modes: `pointer` (resolved at load time, always fresh), `copy` (verbatim materialization at build time), `derived` (a semantic transformation materialized at build time, governed by a `Derivation.Rule`). Each binding carries a checkable claim — pointer: the target resolves; copy: equality; derived: the rule still holds. A failed check is a drift finding with no predefined winner. The v1 toolchain materializes `copy` and `derived`; `pointer` remains routed prose.

**Recipes.** The `Skillware.Recipe` is the inline declaration form: a `[!skw]` callout under a heading in a `.skw.md` src, carrying the verb (binding), `from:` targets, and `intent:` (the rule's context), with the produced body directly below — declaration, rule, and result side by side. Compile is deterministic: the toolchain strips the machinery; the runnable surface carries only the produced content. The recipe is the section-scoped v1 instance of the general `Skillware.Construct` (declaration + body + owned end); v2 makes the construct position-free with enforced explicit closure.

**Derivation.** A `Derivation.Rule` is the relation `Dependencies + Context → Derived`. Run forward it (re)generates the derived content; run as a check it answers the drift question — does the current derived still match what its dependencies and context would now produce? The check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps. `Derived.Content` is granular — any span of a module can be derived, and the more a module imports, the more its maintenance automates.

> [!skw]- end-derived

## The Construct In Brief

> [!skw]- derived
> from: references/lang.skw.md#Construct Grammar
> intent: one-paragraph digest of the grammar for a reader who wants the
> shape without the full spec; route to lang.md for the normative rules

The language has one syntactic form: `> [!skw]- <command>` opens a construct, `> key: value` lines carry its args (a bare `>` line continues the previous key), the body follows as flat markdown at column 0, and a mandatory owned closer `> [!skw]- end-<command>` ends it — bare `end` is invalid, headings close nothing, and a multi-close line (`end-a end-b`) unwinds nested constructs innermost-first. A declaration may carry one `^label` token giving the span a stable heading-independent identity (a bare `^label` is a labeled `text`; `end-^label` is the precise closer). Primitive commands are `text`, `copy`, and `derived`; everything outside constructs is hand-owned prose, and callouts inside code fences are inert examples. The full grammar, locator forms, and compilation rules live in `references/lang.md`.

> [!skw]- end-derived

## Where Things Live

- concepts (canonical): `agentos-pkg/design/107-design.md` — the `Agentos.Skillware` namespace, from `Skill.Runnable.Surface` through `Skillware.Recipe`
- the operational spec: `references/lang.md`
- the working discipline: `references/author.md` (writing), `references/check.md` (maintaining)
- the toolchain: `agentos skillware build / check / status`
