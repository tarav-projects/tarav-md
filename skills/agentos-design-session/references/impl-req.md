# Impl.Req Component

`Impl.Req` is the implementation-request component of a `Design.Session`.

It replaces a separate session-local execution-plan artifact. When a session produces implementation work, use the `agentos-artifact-impl-req` skill and write a `*-impl-req.md` artifact.

## Role

`Impl.Req` translates `Core.Design` and `TODO.Design` into implementation-ready guidance.

Good implementation-request material includes:

- concrete requested change
- source design inputs and relevant surfaces
- constraints and invariants
- vertical slices when the work is complex enough
- ordered work when useful
- validation commands, checks, or review expectations
- risks and deviation triggers
- acceptance signals

## Vertical Slices

Prefer vertical slices when possible.

A vertical slice is a thin end-to-end change that produces something observable through a relevant interface, artifact boundary, test, command, or reviewable state. It should be small enough to validate, but complete enough to exercise the important path through the system.

Use vertical slices to avoid broad, unverified implementation plans. Each slice should state:

- what changes
- what observable result should exist afterward
- how the result will be checked
- what design or task assumption it validates

## Relationship To TODO.Design

`TODO.Design` defines what action should be taken and why. It may include objectives, evidence, validation expectations, boundaries, and readiness questions.

`Impl.Req` is the handoff surface for doing the work. It should not reopen core design silently. If implementation planning reveals that `Core.Design` or `TODO.Design` does not fit reality, surface the mismatch and return to the relevant design surface.

## Boundaries

Do not create an `Impl.Req` automatically. Propose it when the session reaches implementation handoff, then wait for explicit user approval.

Do not use an `Impl.Req` as a progress diary. It is the implementation request, validation contract, and handoff surface.
