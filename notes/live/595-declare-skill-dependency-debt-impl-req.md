# 595 — declare skill-surface dependency debt

## Impl.Abstract

- **scope:** declare the **48 `undeclared-dependency`** mentions across three skw skills — `agentos-skillware` (22), `agentos-hugentics-impl` (18), `agentos-hugentics` (8) — so every resolving `Dotted.Name` a skill surface mentions carries a `--from`, gaining `dangling`-drift protection (a rename/removal now surfaces instead of silently breaking).
- **out of scope:** any content/doctrine change; `bless`/remove (all 48 are legitimate concept dependencies → declare); the design-gated backlog (index-drift resolver, code backend, agendix promotion).
- **status:** ✅ executed — undeclared 48 → 0; whole project skw-clean.
- **source:** the session's `agentos skw check` drift signal; touched decision to bank the ready declaration debt.

## Impl.Index

### Declaration.Rule

- `Dependency.Sync` is **file-scoped**: a resolving mention needs a `--from` in *that file's* `.skw.md` source.
- add one passthrough `> $kw: --from …` declaration block per src file covering its undeclared mentions; a declaration-only block self-closes, and the machinery strips at build so the runnable `.md` stays **byte-identical**.
- all 48 mentions resolve and are genuine references → declare every one; none blessed or removed.

## Execution.Plan

Behaviour-preserving: each rebuilt `.md` stays byte-identical to its committed version; each skill's `undeclared-dependency` count goes to 0. `agentos skw check` per skill is the inner guard.

### Slice 1 — agentos-skillware (22)
- clusters: `SKILL` (Batchy.Skill, Package.Aux.Skill, Semantic.Router, Skill.Module, Touched.Surface.Index) · `author` (Inline.Relatedness, Skw.Address.Schema) · `check` (Skw.Address.Schema) · `doctrine` (Annotation.Point, Cited.Duplication, Closure.Parser, Skw.Address.Schema, Skw.Backend, Skw.Language, Skw.Network, Skw.Quote.Binding) · `lang` (Closure.Parser, Index.Line, Semantic.Router, Skw.Address.Schema, Skw.Annotation, Skw.Dependency)
- **check:** build clean; `skw check` undeclared 22 → 0; `.md` byte-identical.
- **status:** ✅ done.

### Slice 2 — agentos-hugentics-impl (18)
- clusters: `SKILL` (Alignment.Checkpoint, Alignment.Mode, Aux.Workflow.Skill, Batchy.Skill, Batchy.Skill.Banner, Batchy.Skill.Help, Hard.Evidence, Impl.Req, Skill.Arg, Skill.Module) · `design` (Hard.Evidence) · `develop` (Alignment.Mode, Impl.Req) · `execute` (Alignment.Mode, Impl.Req, No.Legacy.Allowed) · `review` (Impl.Req, RED.GREEN.Test.Suite)
- **check:** undeclared 18 → 0; `.md` byte-identical.
- **status:** ✅ done.

### Slice 3 — agentos-hugentics (8)
- clusters: `SKILL` (Alignment.Checkpoint, Batchy.Skill, Impl.Req, Name.As.Index, Package.Driver) · `alignment-session` (Cited.Duplication, Open.Variable, Touched.Variable)
- **check:** undeclared 8 → 0; `.md` byte-identical.
- **status:** ✅ done.

### Acceptance signals
- project `agentos skw check`: **undeclared 48 → 0**, `derived-stale` 0, `dangling` 0; every rebuilt `.md` byte-identical to HEAD.

## Impl.Log
- 2026-07-21 — created and executed under `impl-capture` → `--develop` (Interactive). All 3 slices landed by appending one passthrough `--from` declaration block per src file (15 files). **Result: undeclared 48 → 0; project `skw check` now 0 POIs across all 21 packages** (derived-stale 0, dangling 0, unhonored 0). Every rebuilt runnable `.md` byte-identical to HEAD. No deviations.
