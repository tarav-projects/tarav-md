# Agentos.Mission

`Agentos.Mission` is a lightweight coordination surface for named blocks of work.

It gives a work session a durable anchor point without turning Agentos into a full project-management system.

## Role

A mission answers:

```txt
Where does what we are doing right now fit in the bigger picture?
```

It is:

- a named anchor point
- a coordination layer
- opt-in
- lightweight enough to stay out of the way

## Boundary

`Agentos.Mission` is not:

- required for every work session
- where implementation details live
- a granular task tracker
- the design SSOT

Implementation plans, live notes, index notes, TODO notes, and issue reports should keep their own roles. A mission can link to them, but it should not absorb them.

## Core Model

A mission has a small structured header and freeform notes.

Likely fields:

- `name`: short identifier
- `goal`: concise statement of intended outcome
- `validation`: how completion is judged
- `status`: `active`, `done`, or `parked`
- `last_activity`: recency signal for default selection
- `help`: self-documenting annotation layer
- `todos`: lightweight checklist
- `notes`: append-only context, decisions, links, or relations

## Selection

Default mission selection should be derived from mission state, not a singleton global pointer.

When a command omits the mission name, it can target the most recently active mission by `last_activity`.

## Links Out

Missions reference other surfaces; they do not contain them.

Examples:

- implementation plans live in live notes or implementation artifacts
- specs and durable concepts live in index notes
- deferred reminders live in `TODOS.Note`
- durable issues can live in issue-report artifacts

## Related Concepts

- `Agentos.Index.Notes`
- `TODOS.Note`
- `Agentos.Dev.Notes`
- `Public.Surface`
- `Project.CLI`

## Legacy Source

Promoted from `../live/migrated-agentos-index/003-Agentos.Mission.md`.
