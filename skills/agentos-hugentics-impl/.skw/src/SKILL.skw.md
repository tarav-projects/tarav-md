---
name: agentos-hugentics-impl
description: "Unified Hugentic implementation workflow for designing Impl.Req artifacts, reviewing them, executing them, or developing an idea through both phases. USE WHEN the user wants implementation planning, an Impl.Req double-checked, execution of an Impl.Req, or end-to-end design and implementation. Called with an optional input plus --design, --review, --execute/--exec, --develop/--dev/--impl, and --AUTO."
---

# Agentos Hugentics Impl

Unified `Aux.Workflow.Skill` for the implementation side of the Hugentic Harness.

The skill routes into implementation design, implementation execution, or both in sequence while keeping each workflow in an on-demand `Skill.Module`.

This is a `Batchy.Skill` - called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags, aliases, loose forms, and positionals resolve to the `Skill.Arg` names below.

## Skill.Arg.Section

### Skill.Arg::Input
- the implementation source: an idea, direct request, design artifact, design summary, or `Impl.Req`
- required: false
- default: the caller's current explicit request or supplied context
- help: "the idea, design source, or Impl.Req to operate on"
- examples: --input "add project-scoped configuration"

### Skill.Arg::Workflow
- selects one implementation workflow
- required: false
- default: infer `Workflow:Execute` when `Input` resolves to an `Impl.Req`; otherwise infer `Workflow:Design`
- type: selector
- help: "design an Impl.Req, review one, execute one, or develop an idea through both phases"
- examples: --design, --review, --execute, --develop
- `Workflow:Design`: --design; action: load `references/design.md`
- `Workflow:Review`: --review; action: load `references/review.md`
- `Workflow:Execute`: --execute; aliases: --exec; action: load `references/execute.md`
- `Workflow:Develop`: --develop; aliases: --dev, --impl; action: load `references/develop.md`

### Skill.Arg::Alignment.Mode
- whether the workflow prompts at declared `Alignment.Checkpoint`s or resolves them autonomously
- required: false
- default: Interactive
- type: switch
- help: "run the selected workflow autonomously"
- examples: --AUTO
- aliases: --auto, --autonomous
- detail: `agentos-hugentics/references/alignment-session.md`

## Workflow Resolution

Resolve the workflow in this order:

1. An explicit workflow flag always wins.
2. Without a workflow flag, resolve `Input` to `Workflow:Execute` when it is an `Impl.Req`.
3. Otherwise resolve to `Workflow:Design`.
4. Never infer `Workflow:Develop`; end-to-end execution requires `--develop`, `--dev`, or `--impl`.
5. Never infer `Workflow:Review`; the blind-spot check requires an explicit `--review`.

Treat input as an `Impl.Req` when it is:

- a path whose file is an `Impl.Req`, normally ending in `-impl-req.md`
- a note number or reference that resolves to such an artifact
- supplied artifact content carrying the `Impl.Abstract`, `Impl.Index`, `Execution.Plan`, and `Impl.Log` structure

If neither an input nor actionable current context exists, orient to the available workflows and do not guess a target.

## Skill Modules

> $kw: ^workflow-router

> $kw: --when
`Workflow:Design` is selected — the caller wants implementation planning.

> $kw: --then
Load `references/design.md` — produce an implementation-ready `Impl.Req`.

> $kw: --when
`Workflow:Review` is selected — the caller wants an `Impl.Req` double-checked.

> $kw: --then
Load `references/review.md` — verify the artifact's claims against `Hard.Evidence` and report readiness in chat; read-only.

> $kw: --when
`Workflow:Execute` is selected — the caller wants an existing `Impl.Req` executed.

> $kw: --then
Load `references/execute.md` — execute the artifact's `Execution.Plan`.

> $kw: --when
`Workflow:Develop` is selected — the caller wants an idea taken through both phases.

> $kw: --then
Load `references/develop.md` — produce an `Impl.Req`, then execute that exact artifact.

> $kw. end

Load only the selected workflow module. The develop module composes design and execute and therefore loads both in sequence. Review is designed to run in a fresh agent that did not design the artifact — that is where the blind-spot check has value.

## Shared Contract

- Preserve the selected `Alignment.Mode` across every phase.
- Treat the generated or supplied `Impl.Req` as the phase boundary and audit trail.
- Keep the `impl.designer.agent` and `impl.executer.agent` responsibilities distinct even when one agent runs both.
- Load `agentos-pkg` when working in an Agentos project.
- Load `agentos-index` when the task needs index-grounded context or index mutation.
- Respect project-local `AGENTS.md` and repository instructions before any implementation edit.
