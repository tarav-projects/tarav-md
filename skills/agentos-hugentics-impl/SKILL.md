---
name: agentos-hugentics-impl
description: "Unified Hugentic implementation workflow for designing Impl.Req artifacts, reviewing them, executing them, developing an idea through both phases, or capturing the session's ready implementation work. USE WHEN the user wants implementation planning, an Impl.Req double-checked, execution of an Impl.Req, end-to-end design and implementation, or to bank the touched, non-design-gated work from a session and park the rest. Called with an optional input plus --design, --review, --execute/--exec, --develop/--dev/--impl, --impl-capture/--capture, and --AUTO."
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
- help: "design an Impl.Req, review one, execute one, develop an idea through both phases, or capture the ready implementation work from the session"
- examples: --design, --review, --execute, --develop, --impl-capture
- `Workflow:Design`: --design; action: load `references/design.md`
- `Workflow:Review`: --review; action: load `references/review.md`
- `Workflow:Execute`: --execute; aliases: --exec; action: load `references/execute.md`
- `Workflow:Develop`: --develop; aliases: --dev, --impl; action: load `references/develop.md`
- `Workflow:Capture`: --impl-capture; aliases: --capture; action: load `references/impl-capture.md`

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
6. Never infer `Workflow:Capture`; harvesting the session's ready work requires an explicit `--impl-capture`.

Treat input as an `Impl.Req` when it is:

- a path whose file is an `Impl.Req`, normally ending in `-impl-req.md`
- a note number or reference that resolves to such an artifact
- supplied artifact content carrying the `Impl.Abstract`, `Impl.Index`, `Execution.Plan`, and `Impl.Log` structure

If neither an input nor actionable current context exists, orient to the available workflows and do not guess a target.

## Skill Modules

`Workflow:Design` is selected — the caller wants implementation planning.

Load `references/design.md` — produce an implementation-ready `Impl.Req`.

`Workflow:Review` is selected — the caller wants an `Impl.Req` double-checked.

Load `references/review.md` — verify the artifact's claims against `Hard.Evidence` and report readiness in chat; read-only.

`Workflow:Execute` is selected — the caller wants an existing `Impl.Req` executed.

Load `references/execute.md` — execute the artifact's `Execution.Plan`.

`Workflow:Develop` is selected — the caller wants an idea taken through both phases.

Load `references/develop.md` — produce an `Impl.Req`, then execute that exact artifact.

`Workflow:Capture` is selected — the caller wants the session's ready implementation work banked and the rest parked.

Load `references/impl-capture.md` — rank the touched, implementation-ready candidates, gate on the best pick, and hand it to develop.

Load only the selected workflow module. The develop module composes design and execute and therefore loads both in sequence. Review is designed to run in a fresh agent that did not design the artifact — that is where the blind-spot check has value.

## Shared Contract

- Preserve the selected `Alignment.Mode` across every phase.
- Treat the generated or supplied `Impl.Req` as the phase boundary and audit trail.
- Keep the `impl.designer.agent` and `impl.executer.agent` responsibilities distinct even when one agent runs both.
- Load `agentos-pkg` when working in an Agentos project.
- Load `agentos-index` when the task needs index-grounded context or index mutation.
- Respect project-local `AGENTS.md` and repository instructions before any implementation edit.
