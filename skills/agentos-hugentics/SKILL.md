---
name: agentos-hugentics
description: "Entry point to the Agentos Hugentic Harness — the integrated standard workflow connecting design, implementation design, and implementation execution. Load when you need orientation to hugentic workflows."
---

# Agentos Hugentic Harness

Single entry point to the hugentic workflow system. This skill maps the landscape — what workflows exist, what agents run them, and where to find the full instructions.

## What This Is

The Hugentic Harness is the integrated standard workflow that connects three phases of agentic work:

1. **What.Design** — scoped human-agent convergence on what to build (`Main.Designer.Agent`)
2. **How.Design** — fork toward implementation, produce an `Impl.Req` artifact (`impl.designer.agent`)
3. **Impl.Exec** — load and execute the `Impl.Req` (`impl.executer.agent`)

Each phase has a named agent role and an operational workflow-master skill with full instructions.

This skill is workflow neutral. It maps the Hugentic subsystem without entering a specific workflow mode.

## Workflow Map

| Phase | Agent | Workflow Master |
|---|---|---|
| What.Design | `Main.Designer.Agent` | `hugentics-designer` |
| How.Design | `impl.designer.agent` | `hugentics-impl-designer` |
| Impl.Exec | `impl.executer.agent` | `hugentics-impl-executer` |

## Artifacts

| Artifact | Defined In |
|---|---|
| `Alignment.Backend:Artifact:What` | `hugentics-designer` |
| `Impl.Req` | `hugentics-impl-designer` |

## How To Use

- Load this skill for the Hugentic map.
- Load a workflow master only when the caller intends to enter that operational mode.
- Workflow masters contain artifact format definitions, reference files, gates, and operational guidance.

## Session Interruptions

During any workflow, the user can trigger interruptions that pause the current loop:

- `Impl.Req.Handoff` — fork to implementation design
- `Capture.Audit` — audit session state
- `Consolidation.Plan` — consolidate design progress
- `Artifact.Upgrade` — upgrade session backend
- `Session.Split` / `Close.Topic` / `Park.Topic` — session management

## Shared Principles

All agents in the harness should have `Development.Principles` loaded. These include:

- `Vertical.Slice` — thin end-to-end changes
- `No.Legacy.Allowed` — no stale state left behind
- `Test.At.Boundaries` — test through public interfaces
- `Deep.Modules` — small interface, hidden complexity
- `Agent.Navigable.Codebase` — code organized for agent exploration

See `skills/agentos-pkg/index/102-index.md` for definitions and how they apply to impl-req work.

## Related Concepts

- **Alignment.Session** — the general alignment model; see `references/alignment-session.md`
- **Alignment.Mode** — two-value autonomy axis (`Interactive` default / `Autonomous`) over declared `Alignment.Checkpoint`s, respected across hugentic skills; defined in `references/alignment-session.md`
- **Index** — `agentos-index` skill, independent subsystem for durable design truth
- **Orientation** — `agentos-pkg` skill, workflow-neutral Agentos package root

## Design Surface

The visual map of this harness lives in `Hugentic-Harness.canvas`.
