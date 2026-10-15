# Implementation Workflow Router

This module routes `tarav-hugentics --impl` into one implementation phase. It
is an agent-operated workflow, not a Python runner.

## Input

Implementation input may be an idea, direct request, design artifact, supplied
context, or an existing live-note `Impl.Req`. `Alignment.Mode` is Interactive
unless `--auto` or `--autonomous` selects Autonomous operation.

Treat input as an `Impl.Req` when a path, note number, or supplied artifact
resolves to a live note containing `Impl.Abstract`, `Impl.Req.Wiki`,
`Execution.Plan`, and `Impl.Log`.

## Phase selection

Keep the shortcuts `--design`, `--review`, `--execute`/`--exec`,
`--develop`/`--dev`, and `--harvest`. An explicit phase wins. Otherwise an
existing Impl.Req defaults to Execute and new actionable input defaults to
Design. Develop, Review, and Harvest require explicit selection. With no
actionable input, orient and stop. `--auto`/`--autonomous` selects autonomous
alignment, not broader execution authority. `--impact` selects input, not a
phase.

Print a compact banner with phase, context backend, input, and Alignment.Mode.

## Context backend

A context backend is where an implementation request reads its User-Touched
context and where it captures that context back. The Project.Wiki is the only
active backend. `--wiki` names it and is optional; notes record it as
`Knowledge.Surface: wiki`.

The Model backend, which grounded requests in a Diagram Model, Collection, and
Draft, is parked; its modules remain in Git history. `--model`, a note
carrying `Impl.Req.Diagram`, or a note with conflicting backend declarations
requires clarification before any mutation. Never silently migrate a request
or create replacement artifacts.

## Routing

Load [`impl/phases.md`](impl/phases.md) for the selected phase. It names the
request contract, code-engineering, and context backend modules it uses.

