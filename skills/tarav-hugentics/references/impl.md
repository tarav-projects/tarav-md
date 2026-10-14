# Implementation Workflow Router

This module routes `tarav-hugentics --impl` into the implementation workflow.
Implementation contextualizes through the Project.Wiki. The former
Model-backed route, which grounded requests in a Diagram Model, Collection, and
Draft, is parked; its modules remain in Git history.

## Input

Implementation input may be an idea, direct request, design artifact, supplied
context, or an existing live-note `Impl.Req`. `Alignment.Mode` is Interactive
unless `--auto` or `--autonomous` selects Autonomous operation.

Treat input as an `Impl.Req` when a path, note number, or supplied artifact
resolves to a live note containing `Impl.Abstract`, `Impl.Req.Wiki`,
`Execution.Plan`, and `Impl.Log`.

## Routing

Load [`impl/wiki.md`](impl/wiki.md) for every implementation route. It owns
phase selection, `--impact` input, the live-note contract, capture, and
evidence commits, and it loads the shared code-engineering module.

`--model` and live notes carrying `Impl.Req.Diagram` belong to the parked
Model-backed route. Report that the route is parked and ask before any
mutation; never silently migrate a request or recreate Diagram artifacts.

