# Impl.Req Component

`Impl.Req` is the implementation-request handoff produced by a `Design.Session`.

It replaces a separate session-local execution-plan artifact. When a session produces implementation work, activate the `trigger-impl-req` skill to hand off to the `hugentics-impl-designer` workflow, which defines the full `Impl.Req` artifact format and design process.

## Role

`Impl.Req` translates the current design-session artifact into implementation-ready guidance.

Good implementation-request material includes:

- concrete requested change
- source design inputs and relevant surfaces
- constraints and invariants
- vertical slices as the preferred implementation shape
- ordered work when useful
- validation commands, checks, or review expectations
- risks and deviation triggers
- acceptance signals

## Vertical Slices

Vertical slices are fundamental to `Impl.Req`.

A vertical slice is a small end-to-end change that exercises the full useful path for one behavior or artifact outcome. It is not a layer-by-layer task.

Avoid horizontal plans like:

```txt
1. Add all schema changes.
2. Add all service logic.
3. Add all UI.
4. Test later.
```

That delays feedback. The implementation can look busy for a long time while still proving nothing about whether the intended behavior works.

Prefer a slice shaped like:

```txt
When X happens, Y is observable, and Z checks it.
```

The observable result can be a passing behavior test, command output, changed artifact, visible UI state, API response, reviewable file/data state, or clear manual QA result.

Use vertical slices to turn broad design intent into implementation work that can be checked quickly. Each slice should state:

- what changes
- which path through the system or artifact surface it exercises
- what observable result should exist afterward
- how the result will be checked
- what design or task assumption it validates

Horizontal work is allowed only when it is truly enabling infrastructure that cannot be made observable yet. If a horizontal step is necessary, name why and pair it with the earliest possible vertical slice.

## Relationship To Design Session

`Design.Index` defines the conceptual background: concept fundamentals, appendix material, and concept-level session meta. `Session.Notes` may contain task-shaped observations, readiness questions, validation hints, and boundaries that are not yet execution-ready.

`Impl.Req` is the handoff surface for doing the work. It should not reopen design silently. If implementation planning reveals that the session design does not fit reality, surface the mismatch and return to the relevant section before proceeding.

## Boundaries

Do not create an `Impl.Req` automatically. Propose it when the session reaches implementation handoff, then wait for explicit user approval.

Do not use an `Impl.Req` as a progress diary. It is the implementation request, validation contract, and handoff surface.
