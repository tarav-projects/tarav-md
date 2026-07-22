# agentos-skillware --about (doctrine)

Use this module to understand Skillware: the mental model behind skills developed as software. It is a self-contained `Cited.Duplication` of the `Agentos.Skillware` namespace in the `agentos-pkg` index (107) — the index owns the concepts; this module makes an agent operational without leaving the skill.

## The Model

> $kw: --derived
> --from Agentos.Skillware
> --from Skill.Runnable.Surface
> --from Skill.Build.Surface
> --from Skw.Dependency
> --from Skw.Annotation
> --intent the self-contained doctrine — restate the 107 cluster as one
> --cont coherent narrative an agent can hold: discipline, two surfaces, imports
> --cont and bindings, the recipe form, derivation and its drift check; stay
> --cont faithful to the blocks, do not invent mechanics

**Skills as software.** `Agentos.Skillware` treats the skill as the unit of software for agents: the artifacts agents run gain engineering structure — modules, dependencies, builds, lineage — so they are reused and evolved rather than written once and forked. A toolchain spanning agentic and CPU work moves package maintenance off the human. The system realizing the discipline is **skw**: the general annotation language (`Skw.Language`) and its `Skw.Backend`s — skills are the first backend, `skw-skills`.

**Two surfaces.** A skill splits into a `Skill.Runnable.Surface` — loaded into agent context to do work, carrying only executable substance, kept clean because anything on it shapes the run — and its complement, the `Skill.Build.Surface`: everything that produces and maintains runnable content, never loaded at run time, an unconstrained workspace. It is realized as the per-package `.skw/` folder and constitutively carries an engine-stamped `AGENTS.md` redirecting agents outside skillware activity. The clean-surface rule is a building-backend discipline: annotated-only `Skw.Backend`s deliberately trade it for constraint co-location, keeping declarations in place on the surface itself.

**Dependencies.** A `Skw.Dependency` is a declared dependency between any two surfaces — the consumer declares, the target never knows its dependents. The binding mode is a flag: `--pointer` (resolved at load time, always fresh), `--copy` (verbatim materialization at build time), `--derived` (a semantic transformation materialized at build time under a recorded intent). Each binding carries a checkable claim — pointer: the target resolves; copy: equality; derived: the rule still holds. A failed check is a drift finding with no predefined winner. Targets are named by `Skw.Address.Schema` addresses — `Dotted.Name`s, `Locator.Name`s, labeled spans; a `--from` may be refined by a `Skw.Quote.Binding` — quoted lines pinning the exact interest range. On building backends the declarations live on the build surface and only materialized results reach the runnable files; the toolchain materializes `--copy` and `--derived`, `--pointer` remains routed prose.

**Annotations.** The `Skw.Annotation` is the unit of skw: one named block attached at an `Annotation.Point`, identified by one explicit `Skw.Address.Schema` address, its features additive flags — a `$kw:` open carrying the binding flag, `--from` targets, `--intent` (derivation context), and documentation `--note`s, with the produced body directly below and closure by role (a materializing block owns its `end`; a declaration-only dependency or note self-closes). Declaration, rule, and result sit side by side. Compile is deterministic: the toolchain strips the machinery; the runnable surface carries only the produced content.

**Derivation.** A derivation is the relation `Dependencies + Context → Derived`. Run forward it (re)generates the derived content; run as a check it answers the drift question — does the current derived still match what its dependencies and context would now produce? The check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps. Derived-ness is granular — any span of a module can be derived, and the more a module imports, the more its maintenance automates.

> $kw. end

## The Block In Brief

> $kw: --derived
> --from references/lang.skw.md#Block Grammar
> --intent one-paragraph digest of the grammar for a reader who wants the
> --cont shape without the full spec; route to lang.md for the normative rules

The language has one syntactic form — the block, the written form of a `Skw.Annotation` — marked by the `$kw` sigil on its two fence lines: `> $kw: [address] [--flags]` opens (CLI-style, inline when short), `> --flag …` lines belong to it as self-marked flags (`--cont` continues the previous flag), and the native body sits below as flat markdown at column 0. There are no command words — the binding mode (`--derived`/`--copy`/`--pointer`) and every feature (`--from`, `--intent`, `--note [TYPE] … ^anchor`, `--supp`, reserved `--to`) are additive flags; a flag-less block is a content span. Closure is by role, in three cases: a materializing block owns a mandatory `> $kw. end`; a router owns an end while its `--when`/`--then` rows peer-close; a declaration-only block (a `--from` dependency or a `--note` attach) self-closes with no end. A bare `end` closes the innermost open block; a legacy `end-<command>` closer is a finding; headings close nothing; machinery inside code fences is an inert example. The parser is a `Closure.Parser`: parse errors exist only below its `Parse.Floor`; above it, unrecognized content is simply text. The full grammar, locator forms, and compilation rules live in `references/lang.md`.

> $kw. end

## Design Notes

> $kw: #closure-rule --note [DF] closure is by role in three cases — a materializing block (`--derived`/`--copy`) owns a mandatory `end`, a router owns an `end` while its `--when`/`--then` rows peer-close, and a declaration-only block (a `--from` dependency or a `--note` attach) self-closes with no `end` ^c20260721-1u

## Where Things Live

- concepts (canonical): `agentos-pkg/design/107-design.md` — the `Agentos.Skillware` namespace, from `Skill.Runnable.Surface` through `Skw.Network`
- the operational spec: `references/lang.md`
- the working discipline: `references/author.md` (writing), `references/check.md` (maintaining)
- the toolchain: `agentos skw build / check / bless / status`

> $kw: --from Annotation.Point --from Cited.Duplication --from Closure.Parser --from Skw.Address.Schema --from Skw.Backend --from Skw.Language --from Skw.Network --from Skw.Quote.Binding
