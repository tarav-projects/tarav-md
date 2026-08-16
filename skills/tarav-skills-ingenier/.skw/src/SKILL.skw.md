> $kw: ^tarav-skills-ingenier-root-reachability --reachable-from @<tarav-pkg>/SKILL.md

---
name: tarav-skills-ingenier
description: Research, design, develop, and evaluate new or existing agent skills from a focused set of local and external sources. USE WHEN the user wants to audit a skill, mine comparable work, discuss a skill design, or create or upgrade a complete skill stack; accepts the target through `--target` or the live conversation and never mutates during research or design.
---

# Agentos Skills Ingenier

`tarav-skills-ingenier` is the operational `Package.Aux.Skill` for developing skills under `tarav-pkg`. It turns a skill idea or existing target into a focused research, design, development, or evaluation run without forcing every run through one linear pipeline.

> $kw: ^skills-ingenier-batchy-runtime-contract --copy
> --from @<tarav-batchy-skills>/references/batchy-skill-run.skw.md^batchy-skill-runtime-contract

This is a `Batchy.Skill`, called like a CLI and resolved by one `Batchy.Router`. This compact contract is materialized from `tarav-batchy-skills`; load that skill when the full convention is needed.

- `-h` / `--help` prints callable help into the chat and stops without running
- a written `--<flag>` is intentional run configuration and must be resolved as such
- explicit configuration wins over compatible inferred or default configuration for the same route
- conversational discovery and declared defaults apply only where the applicable router row permits them
- every non-help run with custom configuration first prints its resolved `Batchy.Skill.Banner`
- only external data consumed by the selected behavior is a `Skill.Arg`; operation and module selection remain router effects
- compatible routes may compose, but aliases and composed flags do not create new module identities
- load only selected `Skill.Module`s and the additional context they explicitly require
- declared `User.Command`s are the only way to cross their explicit workflow gates
- when a configured run, command target, or required argument remains materially ambiguous, ask rather than guess

> $kw. end

## Skill.Arg.Section

Only external data consumed by the selected module is a `Skill.Arg`. Research, design, development, and evaluation are router effects rather than arguments.

### Skill.Arg::Target.Skill
- the existing skill, skill folder, prompt, or capability idea being worked on
- required: true
- flags: --target
- resolution: explicit or from the live conversation when unique
- help: "the skill, folder, prompt, or capability idea to work on"
- examples: --target skills/tarav-example, --target "a skill for release readiness"

### Skill.Arg::Sources
- extra repositories, folders, documents, sessions, or constraints to mine beyond the curated registry
- required: false
- flags: --sources
- repeatable: true
- help: "additional sources or source constraints for this run"
- examples: --sources ./local-skills, --sources "user-invariant Chatlas sessions"

### Skill.Arg::Platform
- target agent or platform constraints that materially shape the resulting skill
- required: false
- flags: --platform
- help: "target agent or platform constraints"
- examples: --platform claude-code, --platform "portable Agent Skills"

## Batchy.Router

The public call surface and module catalog below are compiled from one canonical `Routing.Table`. Research and design are read-only. Development mutates only within the caller-authorized target and follows any target-local gate.

> $kw: ^skills-ingenier-public-call-surface --routing-view calls --table ^skills-ingenier-router

## Skill.Module Catalog

> $kw: ^skills-ingenier-module-catalog --routing-view modules --table ^skills-ingenier-router

## User.Command.Section

### User.Command::Apply
- apply the foregrounded skill design to its resolved target
- triggers: `::apply`
- available: when the design workflow holds one current implementation-ready proposal and one resolved target
- action: select `Skill.Develop.Workflow.Module` with the foregrounded proposal as its development context
- policy: this command crosses only the skill-design workflow's apply gate; target-local gates remain authoritative

#### User.Command.Arg::Target
- the skill target receiving the approved design
- required: true
- resolution: Contextual

## Routing.Table

This is the skill's single declarative router. Rows compose because one run may research before design or evaluate after development; explicit configuration wins for the same route.

> $kw: ^skills-ingenier-router --routing-table --select many

> $kw: ^route-skill-research --router-row --table ^skills-ingenier-router
> --flag --research
> --alias --mine
> --alias --audit
> --alias --check
> --match explicit-or-semantic
> --to Skill.Research.Operation.Module
> --load references/research.md
> --when the caller wants an existing skill inspected, comparable sources mined, stale conventions identified, or a read-only report before deciding what to change
> --then load the research operation and report evidence, candidate moves, and unresolved questions without mutating the target

> $kw: ^route-skill-design --router-row --table ^skills-ingenier-router
> --flag --design
> --alias --draft
> --match explicit-or-semantic
> --to Skill.Design.Workflow.Module
> --load references/design.md
> --when the caller wants findings turned into a proposed skill boundary, Batchy call surface, module graph, workflow, or artifact layout without implementation
> --then load the design workflow and keep the target unchanged until a development route or `::apply` crosses the gate

> $kw: ^route-skill-develop --router-row --table ^skills-ingenier-router
> --flag --develop
> --alias --dev
> --alias --apply
> --alias --update
> --match explicit-or-semantic
> --to Skill.Develop.Workflow.Module
> --load references/develop.md
> --when the caller explicitly asks to create, implement, apply, update, or upgrade a skill or full skill stack
> --then load the development workflow, resolve the target's owning source surface, implement the authorized change, and validate it

> $kw: ^route-skill-evaluate --router-row --table ^skills-ingenier-router
> --flag --evaluate
> --alias --test
> --match explicit-or-semantic
> --to Skill.Evaluation.Operation.Module
> --load references/evaluate.md
> --when the caller wants trigger behavior, routing, output shape, or the completed skill pressure-tested
> --then load the evaluation operation and run a lightweight reality check or route to `tarav-testground` when behavioral testing is warranted

> $kw: ^route-target-skill-arg --router-row --table ^skills-ingenier-router
> --flag --target
> --match explicit-or-semantic
> --to Skill.Arg::Target.Skill
> --when the caller supplies or clearly identifies the one existing skill, skill folder, prompt, or capability idea consumed by the selected module
> --then bind the unique existing skill, skill folder, prompt, or capability idea consumed by the selected module

> $kw: ^route-sources-arg --router-row --table ^skills-ingenier-router
> --flag --sources
> --match explicit-or-semantic
> --to Skill.Arg::Sources
> --when the caller names additional repositories, folders, documents, sessions, or source constraints for the current run
> --then bind the caller's additional source set or source constraints for this run

> $kw: ^route-platform-arg --router-row --table ^skills-ingenier-router
> --flag --platform
> --match explicit-or-semantic
> --to Skill.Arg::Platform
> --when the caller names a target agent or platform constraint that materially shapes the resulting skill
> --then bind the platform constraints that materially shape the target skill

> $kw: ^skills-ingenier-full-routing-table --routing-view full --table ^skills-ingenier-router

## Boundary

- this skill owns source mining, skill design, skill development, and focused evaluation; `tarav-batchy-skills` owns the conventions it applies
- research and design are read-only; a direct development request or available `::apply` command authorizes target mutation within the caller's scope
- when the target is Skillware-managed, edit `.skw/src/`, build the runnable surfaces, and check drift; never hand-edit compiled targets
- target-local `AGENTS.md`, package instructions, approval gates, and source ownership override this skill's generic workflow
- use `tarav-testground` for behavioral package-skill tests that need controlled traces and evaluation
- prefer a focused local evidence set; external research is optional and justified by the target rather than automatic

## Response Shape

- research: evidence, `adopt` / `adapt` / `avoid` findings, and the best next move
- design: proposed boundary, routes and modules, artifact placement, tradeoffs, and the available `::apply` command at the apply checkpoint
- development: changed surfaces, important design choices, sources used, and validation results
- evaluation: prompts or scenarios exercised, observed routing or behavior, and remaining POIs

> $kw: --from Batchy.Router --from Batchy.Skill --from Batchy.Skill.Banner --from Package.Aux.Skill --from Routing.Table --from Skill.Arg --from Skill.Module --from User.Command
