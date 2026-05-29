---
name: hugentics-impl-designer
description: "impl.designer.agent workflow master — design implementation plans and produce Impl.Req artifacts. Covers the Alignment.Loop:How and artifact format."
---

# Hugentics Impl Designer

Workflow master for the `impl.designer.agent` — the second phase of the Hugentic Harness.

Design an implementation path and produce an `Impl.Req` artifact. The agent forks toward implementation, writing `Impl.Index` + `Execution.Plan`, and baking in development principles.

## Activation

Activate this skill when the user wants to plan an implementation or produce an `Impl.Req`.

Typical activation phrases include "let's plan the implementation", "create an impl-req", "make an impl-req", `Impl.Req.Handoff`, or an explicit `hugentics-impl-designer` invocation.

Can be triggered from a design session (`Impl.Req.Handoff` interruption) or independently from any context where implementation guidance is needed.

## Alignment.Loop:How

The `How.Design` specialization of `Alignment.Loop`, scoped to implementation concerns:

- `Alignment.Question:How` — drive toward implementation design, enrich the `Impl.Index` with `Hard.Evidence`-based facts
- `Alignment.Discussion:How` — discuss implementation concerns
- `Alignment.Consolidation:How` — update `Impl.Req` artifact

The loop continues until the implementation design is sufficiently aligned for execution.

## Impl.Req Artifact Format

An `Impl.Req` is an implementation-request artifact — a surface for designing and tracking an implementation plan.

The plan is pre-shaped so the implementer naturally follows good practices: `Vertical.Slice`, `No.Legacy.Allowed`, `Test.At.Boundaries` are built into the plan structure, not listed as recommendations.

The goal: if handed to an agent with no other context, the plan itself steers them toward quality work.

### Artifact Structure

- `Impl.Abstract` — scope, status, source context — fully agent-maintained, the agent must evaluate changes to it on each design change
- `Impl.Index` — implementation design alignment as `Design.Index.Blocks` — same block format, same evidence tracking, same alignment semantics
- `Execution.Plan` — ordered vertical slices, validation per slice, risks, deviation triggers, acceptance signals, status per slice (updated by implementer)
- `Impl.Log` — progress tracking: deviations, blockers, decisions made in open space (updated by implementer)

### Location And Naming

- Use a filename ending in `-impl-req.md`
- Store in `notes/live/`
- Use `agentos-live-surfaces` for live-note location and numbering

### Writing Guidance

- Write for another agent who did not see the full discussion
- Be direct and clear
- Self-contained enough for any agent to understand and execute — can link out to other surfaces for extended context
- Prefer references to files, notes, commands, or surfaces over pasted code — do not include large file fragments or long code excerpts
- Prefer implementation-shaping context over implementation detail
- Prefer vertical slices — convert broad intent into small end-to-end changes
- Do not silently replace accepted intent with your own reinterpretation
- Do not write automatically — only on explicit user request

### Vertical Slices

A `Vertical.Slice` is the preferred shape of implementation work — a unit that cuts through the stack as deeply as possible to produce one observable result end-to-end.

Each slice should state:

- what changes
- which path through the system it exercises
- what observable result should exist
- how the result will be checked

Design the implementation to reach the first observable endpoint as fast as possible — get to a testable running state first, then expand.

See `references/example.md` for a concrete sample.

### Updating Guidance

- Preserve the original request intent unless the user explicitly changes it
- When refining, prefer focused updates over full rewrites
- When implementation work occurs, update `Impl.Abstract` and append to `Impl.Log`
- Post-execution log entries should say what was implemented, what remains if anything, and any drift or blockers discovered

### Realignment Notes

When an `Impl.Req` is written to correct drift from an accepted design:

- Explain the observed drift in the relevant `Impl.Index` block
- Make the corrective request explicit in the `Execution.Plan`
- Reference the original design artifact or discussion in `Impl.Abstract`

## Agent Chain Context

- `conceptual.designer.agent` → `impl.designer.agent` → `impl.executer.agent`
- This skill covers the middle agent
- Input may come from a `What.Design.Session` artifact, a design summary, or direct user request
- Output is an `Impl.Req` artifact ready for the `impl.executer.agent`
- All agents should have `Development.Principles` loaded

## Feedback To Design

The impl design process may surface issues with the fundamentals design. When this happens:

- Note the feedback in the `Impl.Req`
- If working from a `Design.Session` artifact, signal that the design session may need updating

## Evidence Priority

1. The user's current explicit directions.
2. Confirmed understanding from the current discussion.
3. Source design artifact or context.
4. Current codebase state, diffs, and referenced surfaces.

## Exit Condition

Exit this skill when the `Impl.Req` is complete and approved, or when the user switches to a different task.
