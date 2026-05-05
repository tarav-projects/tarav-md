# Agentos Usage Skill Draft

```md
---
name: agentos-usage
description: Use when working in an Agentos project or when you need a practical entrypoint for understanding how to use the Agentos project surfaces.
---

# Agentos Usage

Practical entrypoint for using an Agentos project.

This skill explains where to look, which surfaces matter, and how to avoid common authority and targeting mistakes. It is a usage surface, not the design source of truth.

## When To Use

Use this skill when:

- working inside a project that adopts Agentos
- trying to understand the project's public surfaces
- deciding where durable project knowledge lives
- deciding whether a directory is an `Agentos.Project`
- using Agentos commands or skills against a project target

Do not use this skill as a substitute for project-specific instructions, current user directions, or the project's durable index notes.

## First Steps

1. Read the current user request.
2. Read local `AGENTS.md` files that apply to the workspace.
3. Check whether the target is an Agentos project by looking for:

```txt
.agentos/project.json
```

4. If the task needs project design context, use the project index:

```txt
notes/index/000-index.md
```

5. If the task needs concept lookup, use:

```txt
notes/index/001-ontology.md
```

## Authority Order

When sources disagree, use this order:

1. Current user instructions.
2. Applicable `AGENTS.md` instructions.
3. Durable project index notes in `notes/index/`.
4. Project usage skills and other public documentation surfaces.
5. Live notes, issue reports, design sessions, and implementation artifacts as evidence.

Closed live design sessions are provenance, not active authority.

## Common Project Surfaces

### Project Identity

```txt
.agentos/project.json
```

This is the canonical marker that a directory is an `Agentos.Project`.

Agentos-looking folders do not define project identity by themselves. Do not treat these as proof of an Agentos project:

```txt
.agents/
.claude/
skills/
notes/
```

### Project Index

```txt
notes/index/
```

The project index is the durable design-truth surface.

Start with:

```txt
notes/index/000-index.md
notes/index/001-ontology.md
```

### Live Notes

```txt
notes/live/
```

Live notes are working surfaces for temporary coordination, active design sessions, TODOs, reports, or handoffs. Promote durable design truth into `notes/index/`.

### Skills

```txt
skills/
```

Skills are reusable agent workflows. They operationalize behavior, but major design concepts should not live only in skills.

### Project CLI

If the project exposes a CLI, prefer documented project commands for deterministic operations, checks, transformations, and maintenance workflows.

For Agentos project commands, prefer explicit project targeting when available.

## Project Targeting

Agentos project-aware commands should target projects explicitly.

Typical forms:

```sh
agentos <command> --project <path>
agentos <command> --project
```

Bare `--project` means the current directory is the intended project target.

Do not silently initialize or modify an Agentos project just because implicit discovery failed.

## Safe Operating Rules

- Do not treat copied skills, agent folders, or assistant config folders as project identity.
- Do not turn index notes into progress trackers.
- Do not treat closed live notes as current design authority.
- Do not assume Agentos implementation repositories define required structure for every Agentos-adopting project.
- Do not add project-design-relevant facts only to usage documentation.
- When a usage skill and the project index conflict, prefer the project index.

## Deeper Context

For Agentos's own markdown surface, the usual durable entrypoints are:

```txt
notes/index/000-index.md
notes/index/001-ontology.md
notes/index/101-Md.Surface.md
notes/index/105-Agentos.Project.md
notes/index/106-Agentos.Skills.md
notes/index/108-Agentos.Project.Doctor.md
```

Use the ontology first when you need to resolve a named concept. Use the numbered notes when you need the durable design details behind that concept.
```
