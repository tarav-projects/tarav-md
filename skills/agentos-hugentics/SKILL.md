---
name: agentos-hugentics
description: "Entry point to the Agentos Hugentic Harness — the integrated standard workflow connecting design, implementation design, and implementation execution. USE WHEN you need orientation to hugentic workflows."
---

# Agentos Hugentic Harness

Single entry point to the hugentic workflow system. This skill maps the landscape — what workflows exist, what agents run them, and where to find the full instructions.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.

## What This Is

The Hugentic Harness is the integrated standard workflow that connects three phases of agentic work:

1. **What.Design** — scoped human-agent convergence on what to build (`Main.Designer.Agent`)
2. **How.Design** — fork toward implementation, produce an `Impl.Req` artifact (`impl.designer.agent`)
3. **Impl.Exec** — load and execute the `Impl.Req` (`impl.executer.agent`)

Each phase has a named agent role and an operational workflow-master skill with full instructions.

This skill is workflow neutral. It maps the Hugentic subsystem without entering a specific workflow mode.

## Workflow Map

`What.Design` — the caller wants scoped human-agent convergence on what to build.

Act as `Main.Designer.Agent`; load `hugentics-designer`.

`How.Design` — the caller wants implementation design forked into an `Impl.Req`.

Act as `impl.designer.agent`; load `agentos-hugentics-impl --design`.

`Impl.Exec` — the caller wants an existing `Impl.Req` executed.

Act as `impl.executer.agent`; load `agentos-hugentics-impl --execute`.

## Artifacts

| Artifact | Defined In |
|---|---|
| `Alignment.Backend::Artifact::What` | `hugentics-designer` |
| `Impl.Req` | `agentos-hugentics-impl` design module |

## How To Use

- Load this skill for the Hugentic map.
- Load a workflow master only when the caller intends to enter that operational mode.
- Use `agentos-hugentics-impl --develop` to produce an `Impl.Req` and execute it in one call.
- Workflow masters contain artifact format definitions, reference files, gates, and operational guidance.

## Alignment.Loop.Interruptions

During any workflow, the user can trigger `Alignment.Loop.Interruptions` — sidequests that pause the current loop; the agent always returns to session state afterward:

- `Impl.Req.Handoff` — fork to implementation design
- `Capture.Audit` — audit session state
- `Consolidation.Plan` — consolidate design progress
- `Artifact.Upgrade` — upgrade session backend
- `Session.Split` / `Close.Topic` / `Park.Topic` — session management

## Shared Principles

All agents in the harness should have `Development.Principles` loaded — the set splits by the phase each principle serves.

`How.Design` — shape the implementation design:

- `Deep.Modules` — small interface, hidden complexity
- `Agent.Navigable.Codebase` — code organized for agent exploration

`Impl.Exec` — guide execution discipline:

- `Vertical.Slice` — cut through the stack for one observable end-to-end result
- `No.Legacy.Allowed` — no stale state left behind
- `No.Regression.Tests.Allowed` — no regression test by default; a fix need not add one
- `Test.At.Boundaries` — test through public interfaces, not implementation details
- `RED.GREEN.Test.Suite` — RED/GREEN tests written test-first to drive the implementation

See `skills/agentos-pkg/design/102-design.md` for definitions and how they apply to impl-req work.

## Hugentic Concept Space

The concept vocabulary a design agent reasons *with*. Definitions live in the `agentos-pkg` index — this is the map, not the definitions. The index carries no loading policy of its own; this harness is the `Package.Driver` that brings these concepts into context. Reach any one by name (`Name.As.Index` — search the name to find every surface that uses it).

**`Hugentic.Concept`** (`103`) — the qualifier the harness is named for: designed for the human-agent interface. The test — it changes *both* how the human works and how the agent works; if only one side, it is a human tool or an agent tool, not hugentic.

### Alignment frame — what alignment *is* (`101`–`102`)

- `Hugentic.Alignment` — bringing human + agent to shared understanding of where they are and where they're going
- `Forward.Alignment` — moving the design point into new territory (the creative act)
- `Internal.Alignment` — syncing every surface to the current design point (the maintenance act)
- `Progress.Gradient` — `Forward` + `Internal` combined; the project is never finished, only moving along the gradient
- `Design.Implementation.CoEvolution` — the rhythm: move forward, then realign surfaces; neither side frozen

### Communication form — how a designer *speaks* (`100`, `102`, `105`)

- `Kernel.Writing` — a conceptual writing system for fundamental signal: orthogonal, compressed bullet lines, each an independent fundamental point, direct language — not prose
- `Kernel.Block` / `Kernel.Block::Design` — the base writing object: every design turn is a *block*, an H2 `Dotted.Notation` heading (a conceptual commitment) + orthogonal fundamentals + optional `### meta`
- `Designer.Turn.Kernel.Form` — the turn shape: render the block, then pair it with the question (`Question / Why-now / Recommended / Evidence`); re-render the same block as it evolves
- `Dotted.Notation` [`:Param`] — the concept form of `Skw.Address.Schema`: name concepts with compact dotted names; the name signals "this is a concept" and is the key for `Name.As.Index`

## Related Concepts

- **Alignment.Session** — the general alignment model; see `references/alignment-session.md`
- **Alignment.Mode** — two-value autonomy axis (`Interactive` default / `Autonomous`) over declared `Alignment.Checkpoint`s, respected across hugentic skills; defined in `references/alignment-session.md`
- **Index** — `agentos-index` skill, independent subsystem for durable design truth
- **Orientation** — `agentos-pkg` skill, workflow-neutral Agentos package root

## Design Surface

The visual map of this harness lives in `Hugentic-Harness.canvas`.
