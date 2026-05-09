# TODO.Design Artifact

`*-todo-design.md` is the task-design layer of a `Design.Session`.

It defines what should be done about the core design to move `Current.Implementation` closer to the staged `Design.Target.Model` fragment.

## Filename

Use:

```txt
NNN-short-topic-todo-design.md
```

Store it in `notes/live/` using `agentos-live-note-base` numbering guidance.

## Structure

```md
# [Short Title] - todo-design

## Motivation

## Items Index

- Task.Name: [status] short description

## Items

### Task.Name

## Notes

## End Log
```

## Writing Guidance

Write task design here, not concrete execution steps.

A TODO design item should usually capture:

- objective
- source evidence or files to inspect
- guidance from the core design
- validation expectations
- boundaries and not-to-do items
- open questions that affect execution readiness

This layer is where implementation philosophy becomes task shape: vertical slices, feedback loops, tests, review points, source-of-truth evidence, and constraints that should guide later execution.

`TODO.Design` may mention files, commands, or tests when they are part of task understanding, but it should not become the ordered step plan. Put ordered steps in `Exec.Plan`.

## Relationship To Core.Design

Every TODO design item should be grounded in core design, even when the relationship is implicit.

If the TODO item requires a design judgment that is not settled, either:

- surface it as open space and continue with a conservative assumption, or
- ask the user to settle it when the uncertainty materially affects direction, taste, risk, or scope.

## Boundaries

Do not redefine core concepts here unless the TODO discussion reveals that core design must be revised.

If implementation reality contradicts the core design, stop and surface the deviation instead of silently adapting the task design.
