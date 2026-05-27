---
name: agentos-pkg
description: "Agentos provides shared tools for agent-project workflows: concept indexes, human-agent design sessions, implementation workflows, live notes, package skills, and project structure (AGENTS.md). Load this skill when working with any of these — or when a project's AGENTS.md routes here. After loading, the agent gets workflow-neutral orientation: what tools exist, where each subsystem starts, and which narrower surface to load next."
---

# agentos-pkg

`Agentos.Pkg` is the package skill that provides Agentos tools to any project. Agentos is a Hugentic and agentic project system — it gives agents shared surfaces for orientation, durable concepts, human-agent workflows, reusable skills, and maintained working state. This skill installs the minimal context an agent needs to use those tools without relying on hidden session knowledge.

Paths in this skill are package-root-relative unless explicitly absolute. For example, `index/000-index.md` means `skills/agentos-pkg/index/000-index.md`.

## Loading Discipline

When this file mentions another skill or reference, load it only if its relevant guidance is not already in context. If it is already in context, reuse it and load only missing detail needed for the current task.

## Decision Router

Choose the narrowest surface that matches your current task:

- **Durable concepts or design knowledge** — use the Agentos Index. Start with `agentos-index` for index workflow orientation or `index/000-index.md` for concept routing.
- **Design, implementation planning, execution, status, or alignment recovery** — use the Hugentics surfaces. Start with `agentos-hugentics` for the workflow map.
- **Maintained working data or snippets** — use live surfaces. `agentos-live-note-base` for notes, `agentos-live-script` for small code snippets.
- **Package boundaries, dependencies, or full skill routing** — use `package.md`.

If none of these match, stay with the caller's current task and use this file as the package map.

## Subsystem Map

### Agentos Index

A concept and design navigation system for any project. The index is where agents go to question, understand, or extend a project's design. Contains durable concepts organized in flat index pages with appendix depth. Any project can have its own index.

- `agentos-index` — auxiliary skill for index orientation and functions (research, writing, diagnosis, testing, maintenance)
- `index/000-index.md` — public index routing table

`Agentos.Pkg` has its own index at `index/` — use it when the task is about Agentos concepts or maintaining this package. Other projects have their own indexes. Do not assume the target index is `Agentos.Pkg`.

### Hugentics

The human-agent workflow harness for structured design, implementation, and alignment.

- `agentos-hugentics` — workflow-neutral harness orientation
- `hugentics-designer` — design sessions (`What.Design`)
- `hugentics-impl-designer` — implementation-request design (`How.Design`)
- `hugentics-impl-executer` — implementation execution
- `hugentics-workflow-status` — active workflow status
- `hugentics-chat-status` — short chat/session realignment
- `hugentics-capture-audit` — find significant chat material not captured in durable surfaces

### Live Surfaces

Maintained working surfaces for notes and small code snippets. Workflow artifacts can use them as storage backends, but artifacts get semantics from the workflow that produces them.

- `agentos-live-note-base` — live-note location and numbering
- `agentos-live-script` — live-script location and numbering

### Operational Skills

- `agentos-skills-ingenier` — skill engineering and source mining
- `agentos-codebase-cleanup` — targeted codebase cleanup
- `agentos-git-commit` — deterministic semantic commit workflows

### Project Model

Any project can adopt the Agentos project model: `AGENTS.md` for agent instructions, a package skill as its primary orientation surface, and optional index, live, and reference surfaces. The `agentos-project-doctor` skill can diagnose how well a folder conforms to this model.

## Auxiliary Skills

Auxiliary skills are `Agentos.Pkg` subsystem surfaces — not separate package roots. They improve subsystem visibility and provide tuned entry points. Reuse them if already in context.

Primary auxiliary skills: `agentos-index`, `agentos-hugentics`.

## Default Rule

If unsure, stay with the caller's current task, use this file as the package map, and load the narrowest missing surface needed to proceed.
