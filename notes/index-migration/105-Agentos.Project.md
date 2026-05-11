# Agentos.Project

`Agentos.Project` defines project identity and targeting for a concrete project adopting the `Agentos.Stack` model.

It is the small contract that lets Agentos commands and workflows decide what counts as a project, what directory a command targets, and when a command may require an existing initialized project.

## Identity

An `Agentos.Project` exists when a concrete project root contains:

```txt
.agentos/project.json
```

Rules:

- `.agentos/project.json` is the canonical marker for project existence.
- `.agentos/config.json` may provide project-local config, but it does not define project existence.
- `.agentos/AGENTS.md` may provide project-local Agentos instructions, but it does not define project existence.
- exported agent folders, skill depots, `.agents/`, `.claude/`, and similar surfaces do not define an `Agentos.Project`.

## Agentos.Project.Marker

`Agentos.Project.Marker` is the canonical filesystem proof that a directory is an `Agentos.Project`.

The marker is:

```txt
.agentos/project.json
```

The marker owns project identity. Project config, skill depots, notes, `.agents/`, `.claude/`, and other Agentos-looking surfaces may indicate adoption, but they do not prove project identity by themselves.

## Agentos.AGENTS.md

`Agentos.AGENTS.md` is the project-local natural-language Agentos instruction surface:

```txt
.agentos/AGENTS.md
```

It is human-writable and can contain project-specific guidance for Agentos workflows and skills.

Skills may load it when custom local instructions or interpretation guidance matter. The surface is general Agentos project guidance, not a doctor-specific config file.

`.agentos/AGENTS.md` does not define project identity. The identity marker remains `.agentos/project.json`.

## Naming Boundary

`Agentos.Project` means a project that adopts Agentos.

It does not mean the concrete implementation of Agentos itself. Use `Agentos.Implementation` when referring to the set of repos, packages, and components that implement Agentos.

Use parameterized notation when a specific target matters:

- `Agentos.Project:agentos-py` means `agentos-py` viewed as an Agentos-adopting project.
- `Agentos.Implementation:agentos-py` means `agentos-py` viewed as part of the concrete Agentos implementation.

The same repository can be both an `Agentos.Project:*` and an `Agentos.Implementation:*` under different reference frames.

## Project Targeting

Project-aware commands must use explicit project targeting.

The minimal explicit form is bare `--project`, which means the current directory is the intended project target.

Explicit targeting rules:

- `--project <path>` targets that path
- bare `--project` targets the current directory

Implicit parent-walk discovery is still part of the discovery system, but project-aware commands should not silently target a project through omitted `--project`.

The resolved explicit target is a `project target`. Command policy decides whether it must already be an existing project.

## Project.Discovery.System

`Project.Discovery.System` is the Agentos mechanism for resolving a command or workflow to an `Agentos.Project` target.

It separates three concerns:

- project identity: whether a directory is an `Agentos.Project`
- project discovery: how a target path resolves to a project root
- command policy: what a command is allowed to do after resolution

Discovery may resolve a project in three related ways:

- implicit discovery: parent-walk from a start path until an `Agentos.Project.Marker` is found
- explicit targeting: resolve the given `--project <path>` as the intended project target
- basename assertion: require the resolved project root basename to match `--project-base <basename>`

Bare `--project` means the current directory is the explicit target.

`--project-base` is primarily a safety check. It checks `resolved_project.root.name`, not marker-level `project_name`, and should not silently select an unrelated project by global search. Without a project registry, it verifies the project that discovery already resolved.

Implicit parent-walk discovery is convenient but can be ambiguous in nested workspaces. When the target surface may live inside a directory that is not itself an initialized `Agentos.Project`, callers should prefer explicit `--project <path>` and verify the resolved project root.

Project-aware commands must not silently target a project when every project selector is omitted. They should require at least one explicit selector: `--project`, `--project-base`, or both.

## Command Policy Boundary

After resolving a project target, each command decides what is allowed.

Examples:

- some commands require an existing project
- some commands may initialize only after explicit targeting
- some commands are not project commands

Safety rule:

- implicit discovery failure must not auto-initialize a project
- project creation requires explicit user targeting or another explicit creation command
- project-aware commands must require explicit `--project`, with bare `--project` as the current-directory target

## Boundaries

`Agentos.Project` is not:

- a complete storage layout catalog
- a global/project config precedence spec
- a subsystem inventory
- a git repository spec

## Related Concepts

- `Project.CLI`
- `Project.Discovery.System`
- `Agentos.Project.Marker`
- `Agentos.AGENTS.md`
- `Agentos.Skills`
- `Maintenance.System`
- `Public.Surface`
- `Usage.Surface`
- `Agentos.Stack`
- `Agentos.Implementation`

## Legacy Source

Promoted from `../live/migrated-agentos-index/004-Agentos.Project.md`.
