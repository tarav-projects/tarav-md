# Agentos.Project

`Agentos.Project` defines project identity and targeting for project-scoped Agentos behavior.

It is the small contract that lets Agentos commands and workflows decide what counts as a project, what directory a command targets, and when a command may require an existing initialized project.

## Identity

An `Agentos.Project` exists when a project root contains:

```txt
.agentos/project.json
```

Rules:

- `.agentos/project.json` is the canonical marker for project existence.
- `.agentos/config.json` may provide project-local config, but it does not define project existence.
- exported agent folders, skill depots, `.agents/`, `.claude/`, and similar surfaces do not define an `Agentos.Project`.

## Project Targeting

Commands that support project targeting have two entry paths:

- implicit discovery by parent-walking from `cwd`
- explicit targeting through `--project`

Explicit targeting rules:

- `--project <path>` targets that path
- bare `--project` targets the current directory

The resolved target is a `project target`. Command policy decides whether it must already be an existing project.

## Command Policy Boundary

After resolving a project target, each command decides what is allowed.

Examples:

- some commands require an existing project
- some commands may initialize only after explicit targeting
- some commands are not project commands

Safety rule:

- implicit discovery failure must not auto-initialize a project
- project creation requires explicit user targeting or another explicit creation command

## Boundaries

`Agentos.Project` is not:

- a complete storage layout catalog
- a global/project config precedence spec
- a subsystem inventory
- a git repository spec

## Related Concepts

- `Project.CLI`
- `Agentos.Skills`
- `Maintenance.System`
- `Public.Surface`

## Legacy Source

Promoted from `../live/migrated-agentos-index/004-Agentos.Project.md`.
