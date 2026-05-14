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

Each phase has a named agent role, a workflow master skill with full instructions, and a trigger skill for activation.

## Workflow Map

| Phase | Agent | Workflow Master | Trigger |
|---|---|---|---|
| What.Design | `Main.Designer.Agent` | `hugentics-designer` | `trigger-design-session` |
| How.Design | `impl.designer.agent` | `hugentics-impl-designer` | `trigger-impl-req` |
| Impl.Exec | `impl.executer.agent` | `hugentics-impl-executer` | `trigger-impl-execution` |

## Artifacts

| Artifact | Pointer Skill | Defined In |
|---|---|---|
| `Alignment.Backend:Artifact:What` | `artifact-design-session` | `hugentics-designer` |
| `Impl.Req` | `artifact-impl-req` | `hugentics-impl-designer` |
| `design-summary` | `artifact-design-summary` | owner TBD |
| `issue-report` | `artifact-issue-report` | owner TBD |

## How To Use

- Load a **trigger skill** to activate a workflow — triggers are lightweight and user-invoked
- The trigger will point you to the **workflow master** — the full instructions for that workflow
- Workflow masters contain artifact format definitions, reference files, and operational guidance

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

See `notes/index/123-Impl.Req.md` and `notes/index/125-Development.Principles.md` (pending) for details.

## Related Concepts

- **Alignment.Session** — the general alignment model; see `references/alignment-session.md`
- **Index** — `agentos-index` skill, independent subsystem for durable design truth
- **Orientation** — `agentos-usage` skill, general Agentos entry point (lists this skill)

## Design Surface

The visual map of this harness lives in `Hugentic-Harness.canvas`.
