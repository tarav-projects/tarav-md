# Exec.Plan Artifact

`*-exec-plan.md` is the concrete execution layer of a `Design.Session`.

It translates TODO design into ordered work that can be implemented, verified, and reviewed.

## Filename

Use:

```txt
NNN-short-topic-exec-plan.md
```

Store it in `notes/live/` using `agentos-live-note-base` numbering guidance.

## Structure

```md
# [Short Title] - exec-plan

## Objective

## Inputs

## Plan

## Validation

## Risks

## End Log
```

## Writing Guidance

Keep this layer practical and concrete.

Good `Exec.Plan` material includes:

- ordered implementation steps
- small verifiable chunks
- likely files or surfaces to edit
- commands, checks, or tests to run when known
- manual review or approval points
- risks and deviation triggers

Prefer vertical slices where possible: each slice should move through the relevant layers of the system and produce something observable through an interface, artifact boundary, test, or reviewable state.

## Deviation Handling

If execution reveals that TODO design or core design does not fit reality, stop and surface the mismatch.

Do not silently redesign core concepts inside the execution plan. Record the deviation and return to `Core.Design` or `TODO.Design` when the design needs to change.

## Boundaries

Do not over-design this artifact before it is needed. Simple work may need only a short plan.

Do not use `Exec.Plan` as a progress diary. It is the plan and validation surface, not a transcript or changelog.
