---
name: agentos-pkg
description: "Agentos provides shared tools for agent-project workflows: concept indexes, human-agent design sessions, implementation workflows, live notes, package skills, and more. USE WHEN working with any of these — or when a project's AGENTS.md routes here. After loading, the agent gets workflow-neutral orientation: what tools exist, where each subsystem starts, and which narrower surface to load next."
---

# agentos-pkg

Agentos is a toolkit for agent-project workflows. It gives agents shared, durable surfaces for orientation, design knowledge, working state, and structured collaboration. Instead of starting from scratch each session, agents working in an agentos project find maintained tools and persistent context.

The main tools: concept indexes, live surfaces, package skills, and human-agent workflows.

Any project can adopt agentos incrementally — an AGENTS.md and one package skill is enough to start. This skill (`agentos-pkg`) is the entry point to the system toolkit — it teaches agents how to discover and use agentos tools in whatever project they're working on.

Paths in this skill are package-root-relative unless explicitly absolute. For example, `000-INDEX.md` means `agentos-pkg/000-INDEX.md`.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.

## Agentos Workspace

Two important locations for agentos surfaces: project folders and package skills.

A **Project Folder** is where the project that users and agents are developing lives — in practice, a folder that stores notes, code, data, and other project material. A `.agentos` folder is a hint that a folder might be an agentos project. At the project level, look for `AGENTS.md`, `notes/` (live notes, index, appendix), and `dev/` (scripts and tooling).

A **Package Skill** is a reachable skill that serves as the agentic interface to a package — it contains data, documentation, and operational instructions for using a package's functionalities. For instance, `agentos-pkg` is the Package Skill of the agentos framework. At the package level, a package skill contains its own `000-INDEX.md`, `design/`, `appendix/`, `references/`, and `SKILL.md`.

When working in a project, the agent may encounter several workspaces — multiple project folders, multiple package skills, or both. Keep clear which workspace an action or prompt is referring to — surfaces from different workspaces should not be confused.

When a surface mentions another skill or reference, load it only if the relevant guidance is not already in context. This applies across all agentos surfaces.

## The Index

The Agentos Index is a concept and design knowledge base — a searchable collection of named entries that capture what a project or package knows about itself. Each entry is a **Kernel Block** — a short, named section that describes one concept from multiple angles using direct, orthogonal lines. The index is the primary discovery surface — where agents go to understand, question, or extend a project's design.

Concepts are named using **Dotted Notation** — compound names like `Vertical.Slice` or `Agentos.Index.System` that serve as stable identifiers.

Indexes are distributed across two scopes:

- `design/` — always-loaded fundamentals. Contains flat numbered files (`100-design.md`, `101-design.md`, ...) where file names carry no semantic meaning — concepts are just appended.
- `appendix/` — on-demand depth. Contains concept-named files (`Concept.Name-appendix.md`) — check if one exists when you need depth beyond the index block.

The **router** maps every concept name to the file that holds it — always read this first. Package indexes use `000-INDEX.md`; project-local indexes use `001-index.md`.

Both project folders and package skills can have their own index. If a project is developing a package skill, the agent can access both indexes locally.

**Project folder with a local index:**

```
my-project/
├── notes/
│   ├── index/
│   │   ├── 001-index.md        ← local router
│   │   ├── 300-index.md        ← local concept blocks
│   │   └── 301-index.md
│   └── appendix/
│       └── My.Concept-appendix.md
```

**Package skill with its own index:**

```
skills/some-pkg/
├── SKILL.md
├── 000-INDEX.md                ← package router
├── design/
│   ├── 100-design.md           ← package concept blocks
│   └── 101-design.md
└── appendix/
    └── Some.Concept-appendix.md
```

**Project developing a package skill (both indexes accessible):**

```
my-project/
├── notes/
│   ├── index/
│   │   ├── 001-index.md        ← local router
│   │   └── 300-index.md
│   └── appendix/
├── skills/
│   └── my-pkg/
│       ├── SKILL.md
│       ├── 000-INDEX.md        ← package router
│       ├── design/
│       │   └── 100-design.md
│       └── appendix/
```

**To search an index:** read the router, find the concept or a related name, read the file it points to, then check the appendix for depth — or just wander around following your intuition.

## Local Surfaces

A project folder may contain several local surfaces — the project's own working and knowledge spaces:

- `AGENTS.md` — project-level agent instructions
- `notes/index/` — project-local index layer (see The Index above)
- `notes/appendix/` — project-local appendix depth (see The Index above)
- `notes/live/` — maintained working files that persist across sessions, numbered with an incrementing prefix. Common artifacts: design sessions, impl-reqs, issue reports, and working drafts.
- `notes/canvas/` — visual collaboration surfaces
- `dev/live/` — small maintained code scripts and tooling snippets that persist across sessions

## Package

`agentos-pkg` is the core package skill for the agentos framework. It is the dependency root — other agentos package skills depend on it for the project model, skill model, index model, and workflow concepts.

This package owns: the Agentos Index system, the Hugentic workflow harness, live surface conventions, and the project structure model.

Separate packages exist for other systems:

- `agentos-chatlas-pkg` — session dataset system (query, export, continuation)
- `agentos-iterante-pkg` — mission harness and iterative workflows

`agentos-pkg` is not the same as the `agentos-md` repository — `agentos-md` is one implementation project; `agentos-pkg` is the portable package skill that any project can use.

## Agentos CLI

The `agentos` CLI is available for discovery and operations. Run `agentos --help` to see what it can do.

For configuring and syncing project-local imported skills, read `references/skills-routing.md`.

For provider account credential artifact reconciliation and troubleshooting, use the `agentos-agent-account-management` skill.

## Go Deeper

When the Driver is not enough, load a narrower surface:

- **Index operations** — load `agentos-index` for index research, writing, diagnosis, and maintenance
- **Human-agent workflows** — load `agentos-hugentics` for structured design, implementation, and alignment workflows
- **Design sessions** — load `hugentics-designer` for scoped human-agent design convergence
- **Implementation planning** — load `hugentics-impl-designer` for implementation-request design
- **Implementation execution** — load `hugentics-impl-executer` for executing implementation plans
- **Workflow status** — load `hugentics-workflow-status` for a structured checkpoint
- **Live surfaces** — load `agentos-live-surfaces` for live-note and live-script location, naming, and numbering
- **Skill conventions** — load `agentos-batchy-skills` for the conventions a proper Agentos skill follows (skill taxonomy, the Batchy calling convention, argument parsing)
- **Skill engineering** — load `agentos-skills-ingenier` for creating or upgrading skills
- **Codebase cleanup** — load `hugentics-codebase-cleaner` for targeted refactoring through the hugentic harness
- **Git commits** — load `agentos-git-commit` for deterministic semantic commit workflows
- **Project health** — load `agentos-project-doctor` to diagnose project conformance
- **Previous agent sessions** — load `agentos-chatlas-pkg` for querying, exporting, and continuing previous agent sessions across projects

For deeper understanding of agentos concepts, search the `agentos-pkg` index:

- Search for `Kernel.Writing` to understand the writing philosophy behind index blocks
- Search for `Kernel.Block` to understand the structure of index entries
- Search for `Agentos.Index.System` to understand how the index system is designed
- Search for `Alignment.Loop` to understand how human-agent workflows converge
- Search for `Development.Principles` to understand implementation discipline
