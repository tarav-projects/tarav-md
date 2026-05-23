---
name: agentos-pkg
description: Agentos core Package.Skill. Workflow-neutral package orientation for the Agentos agentic framework and its public skill surfaces.
---

# agentos-pkg

`agentos-pkg` is the core `Package.Skill` for Agentos.

It is the package-level public agentic surface for the Agentos framework: project model, skills system, index system, Hugentic workflows, live-note conventions, project diagnosis, and shared Agentos operating surfaces.

This root skill is workflow neutral. It gives package identity and orientation only, so loading it does not change the caller's current task.

## Package Surfaces

| Surface | Use |
|---|---|
| `package.md` | package identity, boundaries, dependencies, and current routing |
| `agentos-index` | Agentos Index subsystem: research, writing, diagnosis, testing, and maintenance functions |
| `agentos-hugentics` | workflow-neutral Hugentic Harness map |
| `hugentics-designer` | operational design-session workflow master |
| `hugentics-impl-designer` | operational implementation-request workflow master |
| `hugentics-impl-executer` | operational implementation-execution workflow master |
| `hugentics-workflow-status` | operational status report for active Hugentic workflows |
| `hugentics-chat-status` | short chat/session realignment report |
| `hugentics-capture-audit` | audit for significant chat material not captured in durable surfaces |
| `agentos-live-note-base` | live-note protocol for `Agentos.Live.Note` |
| `agentos-live-script` | live-script protocol for `Agentos.Live.Script` |
| `agentos-skills-ingenier` | skill engineering and source-mining workflow |
| `agentos-codebase-cleanup` | targeted codebase cleanup workflow |
| `agentos-git-commit` | deterministic semantic commit workflow |

Load this skill when you need Agentos package orientation. Load a narrower auxiliary skill when the caller already has a subsystem or workflow intention.
