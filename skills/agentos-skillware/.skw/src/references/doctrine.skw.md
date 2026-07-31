# agentos-skillware --about (doctrine)

Use this module to understand Skillware: the mental model behind skills developed as software. It is a self-contained `Cited.Duplication` of the `Agentos.Skillware` namespace in the `agentos-pkg` index (107) — the index owns the concepts; this module makes an agent operational without leaving the skill.

## The Model

> $kw: --derived
> --from Agentos.Skillware
> --from Skill.Runnable.Surface
> --from Skill.Build.Surface
> --from Index.Line
> --from Skw.Ann.Dependency
> --from Skw.Pkg.Dependency
> --from Skw.Annotation
> --from Skw.Touched.Index
> --intent the self-contained doctrine — restate the 107 cluster as one
> --cont coherent narrative an agent can hold: discipline, two surfaces, imports
> --cont and bindings, the recipe form, derivation and its drift check; stay
> --cont faithful to the blocks, do not invent mechanics

**Skills as software.** `Agentos.Skillware` treats the skill as the unit of software for agents: the artifacts agents run gain engineering structure — modules, dependencies, builds, lineage — so they are reused and evolved rather than written once and forked. A toolchain spanning agentic and CPU work moves package maintenance off the human. The system realizing the discipline is **skw**: the general annotation language (`Skw.Language`) and its `Skw.Backend`s — skills are the first backend, `skw-skills`. Touch remains orthogonal to this structure: an skw object becomes touched only through its own provenance, while `Skw.Touched.Index` materializes grounded `Index.Line`s attached to annotations.

**Two surfaces.** A skill splits into a `Skill.Runnable.Surface` — loaded into agent context to do work, carrying only executable substance, kept clean because anything on it shapes the run — and its complement, the `Skill.Build.Surface`: everything that produces and maintains runnable content, never loaded at run time, an unconstrained workspace. It is realized as the per-package `.skw/` folder and constitutively carries an engine-stamped `AGENTS.md` redirecting agents outside skillware activity. The clean-surface rule is a building-backend discipline: annotated-only `Skw.Backend`s deliberately trade it for constraint co-location, keeping declarations in place on the surface itself.

**Dependencies.** A `Skw.Ann.Dependency` is an annotation-level edge declared by the consumer; the target never knows its dependents. `--from` is generic, `--dev-from` loads silent builder context, and `--cite` requires its target to remain explicit on the compiled surface; `Skw.Quote.Binding` remains the finer content-range refinement of an edge. Materialization is orthogonal: `--pointer` resolves at load time, `--copy` binds verbatim at build time, and `--derived` records a semantic transformation under an intent. Targets use `Skw.Address.Schema`; cross-package targets resolve only through `Skw.Pkg.Dependency`. A `Context.Assembly.Module` is a whole `.skw.md` file declaring the direct sources whose shared context it assembles. Any package-local dependency on one of those sources is expected to load the whole assembly through `--dev-from`; a missing companion edge becomes a semantic POI, not a rejected dependency.

**Annotations.** The `Skw.Annotation` is the unit of skw: one named block attached at an `Annotation.Point`, identified by one explicit `Skw.Address.Schema` address, its features additive flags — a `$kw:` open carrying the binding flag, `--from` targets, `--intent` (derivation context), and documentation `--note`s, with the produced body directly below and closure by role (a materializing block owns its `end`; a declaration-only dependency or note self-closes). Declaration, rule, and result sit side by side. Compile is deterministic: the toolchain strips the machinery; the runnable surface carries only the produced content.

**Derivation.** A derivation is the relation `Dependencies + Context → Derived`. Run forward it (re)generates the derived content; run as a check it answers the drift question — does the current derived still match what its dependencies and context would now produce? The check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps. Derived-ness is granular — any span of a module can be derived, and the more a module imports, the more its maintenance automates.

> $kw. end

## The Block In Brief

> $kw: --derived
> --from references/lang.skw.md#Block Grammar
> --intent one-paragraph digest of the grammar for a reader who wants the
> --cont shape without the full spec; route to lang.md for the normative rules

The language has one syntactic form — the block, the written form of a `Skw.Annotation` — marked by the `$kw` sigil on its two fence lines: `> $kw: [address] [--flags]` opens, `> --flag …` lines belong to it, and the native body sits below. Bindings and dependency roles (`--from`/`--dev-from`/`--cite`) are additive flags; `--context-assembly` is the self-closing line-1 declaration whose product is the complete file. Materializing blocks and `Routing.Table`s own an end; declaration-only blocks self-close. The parser is a `Closure.Parser`: parse errors exist only below its `Parse.Floor`; above it, unrecognized content is simply text. The full grammar, locator forms, and compilation rules live in `references/lang.md`.

> $kw. end

## Design Notes

> $kw: #closure-rule --note [DF] closure is by role in three cases — a materializing block (`--derived`/`--copy`) owns a mandatory `end`, a `Routing.Table` owns an `end` while its `--when`/`--then` rows peer-close, and a declaration-only block (a `--from` dependency or a `--note` attach) self-closes with no `end` ^c20260721-1u

## Where Things Live

- concepts (canonical): `agentos-pkg/design/107-design.md` — the `Agentos.Skillware` namespace, from `Skill.Runnable.Surface` through `Skw.Network`
- the operational spec: `references/lang.md`
- the working discipline: `references/author.md` (writing), `references/check.md` (maintaining)
- the toolchain: `agentos skw build / check / bless / status`

> $kw: --from Annotation.Point --from Cited.Duplication --from Closure.Parser --from Routing.Table --from Skw.Address.Schema --from Skw.Backend --from Skw.Language --from Skw.Network --from Skw.Quote.Binding
