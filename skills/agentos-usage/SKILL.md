---
name: agentos-usage
description: Use when working in or with an Agentos project and you need a minimal orientation to the Agentos universe.
---

# Agentos Usage

Minimal orientation to the Agentos universe for agents working in or with an Agentos project.

This is the master `Usage.Skill` for the Agentos project. It coordinates the project's `Usage.Surface` — routing to skills, CLI help, and index notes as needed.

The durable design truth about Agentos lives in its index notes, not in this skill.

## Source Model

This skill derives from:

- `notes/index/106-Agentos.Skills.md` (Usage.Surface and Usage.Skill definitions)
- `notes/index/001-ontology.md` (concept registry)
- `notes/index/109-Agentos.Hugentic.Flow.md` (Hugentic workflow overview)

If this skill conflicts with `notes/index/`, the index wins.

## What Agentos Is

Agentos is an operating system for agent-oriented work: conventions, surfaces, skills, and CLI tools for developing and using projects with agents and humans together. The typical use is during human/agent co-development of a project — the Hugentic workflow.

## The Surfaces

An `Agentos.Project` is a directory with `.agentos/project.json`. That file is the canonical project identity marker. Agentos-looking folders (`notes/`, `skills/`, `.agents/`) are not proof by themselves.

Inside a project, the main surfaces are:

**Index** — `notes/index/`
The durable design-truth surface. Concept notes, ontology, and stable decisions live here. Start with `000-index.md` and `001-ontology.md`.

**Live Notes** — `notes/live/`
The working surface. Active design sessions, TODOs, reports, and handoffs. Not authority — durable signal gets promoted to the index.

**Skills** — `skills/`
Reusable agent workflows. Imported into a project as managed symlinks via the Agentos CLI.

**CLI** — `agentos`
The project CLI for deterministic operations, checks, and maintenance. Use `agentos --help` to discover commands; `agentos <command> --help` for details.

## Minimal Usage Guide

### Orienting in a project

Read the project index to understand what the project is and what design decisions have been made:

```txt
notes/index/000-index.md    # table of contents and router
notes/index/001-ontology.md # concept lookup
```

Use `001-ontology.md` first when you need to resolve a named concept.

### Hugentic workflows

The Hugentic Harness integrates design, implementation design, and implementation execution workflows. Load the harness entry point for the full workflow map.

→ `agentos-hugentics` skill

### Design sessions

Use the design session trigger to start a structured design conversation. It tracks topics, records converged decisions, and produces durable outputs for promotion to the index.

→ `trigger-design-session` skill

### Live notes lifecycle

Live notes are created for a working session and promoted when they produce durable signal. Use `agentos` to allocate the next prefix:

```sh
agentos live-note --project
```

Durable design truth belongs in `notes/index/`, not in live notes.

Reserved live-note surfaces may also exist for lightweight parked items:

- `notes/live/010.TODOS.md` for deferred work (`live-todo`)
- `notes/live/011.ISSUES.md` for issue-shaped active work (`live-issue`)

→ `agentos-live-note-base` skill

### Project doctor pass

Run a doctor pass to check how well a project conforms to the Agentos stack model. Report-only by default.

```sh
agentos doctor --project
```

→ `agentos-project-doctor` skill

### Skills import

Sync the selected skill catalog into the project depots:

```sh
agentos skills import --project
agentos skills status --project
```

→ `106-Agentos.Skills.md` for the full source and profile model

## Where To Find More

| Subject | Surface |
|---|---|
| Hugentic Harness (workflows) | `agentos-hugentics` skill |
| Hugentic workflow overview | `notes/index/109-Agentos.Hugentic.Flow.md` |
| Project identity and targeting | `notes/index/105-Agentos.Project.md` |
| Skills system | `notes/index/106-Agentos.Skills.md` |
| Index notes system | `agentos-index-notes-base` skill |
| Live notes | `agentos-live-note-base` skill |
| Project doctor | `agentos-project-doctor` skill |
| Design sessions | `trigger-design-session` skill |
| File numbering protocol | `agentos-file-numbering-base` skill |
| Concept lookup | `notes/index/001-ontology.md` |
| Full index | `notes/index/000-index.md` |
| CLI commands | `agentos --help` |
