---
name: tarav-pkg
description: "Agentos provides shared tools for agent-project workflows: concept indexes, index retrofit campaigns, human-agent design sessions, implementation workflows, live notes, package skills, and more. USE WHEN working with any of these, surveying or retrofitting an Index depot, or when a project's AGENTS.md routes here. After loading, the agent gets workflow-neutral orientation and routes to the relevant subsystem."
---

# tarav-pkg

Agentos is a toolkit for agent-project workflows. It gives agents shared, durable surfaces for orientation, design knowledge, working state, and structured collaboration. Instead of starting from scratch each session, agents working in an agentos project find maintained tools and persistent context.

The main tools: concept indexes, live surfaces, package skills, and human-agent workflows.

Any project can adopt agentos incrementally — an AGENTS.md and one package skill is enough to start. This skill (`tarav-pkg`) is the entry point to the system toolkit — it teaches agents how to discover and use agentos tools in whatever project they're working on.

Paths in this skill are package-root-relative unless explicitly absolute. For example, `000-INDEX.md` means `tarav-pkg/000-INDEX.md`.

This is a `Batchy.Skill`, called like a CLI and resolved by one `Batchy.Router`. This compact contract is materialized from `tarav-batchy-skills`; load that skill when the full convention is needed.

- `-h` / `--help` prints callable help into the chat and stops without running
- a written `--<flag>` is intentional run configuration and must be resolved as such
- explicit configuration wins over compatible inferred or default configuration for the same route
- conversational discovery and declared defaults apply only where the applicable router row permits them
- every non-help run with custom configuration first prints its resolved `Batchy.Skill.Banner`
- only external data consumed by the selected behavior is a `Skill.Arg`; operation and module selection remain router effects
- compatible routes may compose, but aliases and composed flags do not create new module identities
- load only selected `Skill.Module`s and the additional context they explicitly require
- declared `User.Command`s are the only way to cross their explicit workflow gates
- when a configured run, command target, or required argument remains materially ambiguous, ask rather than guess

## Agentos Workspace

Two important locations for agentos surfaces: project folders and package skills.

A **Project Folder** is where the project that users and agents are developing lives — in practice, a folder that stores notes, code, data, and other project material. A `.agentos` folder is a hint that a folder might be an agentos project. At the project level, look for `AGENTS.md`, `notes/` (live notes, index, appendix), and `dev/` (scripts and tooling).

A **Package Skill** is a reachable skill that serves as the agentic interface to a package — it contains data, documentation, and operational instructions for using a package's functionalities. For instance, `tarav-pkg` is the Package Skill of the agentos framework. At the package level, a package skill contains its own `000-INDEX.md`, `design/`, optional specialized chapters such as `appendix/` and `references/`, and `SKILL.md`.

When working in a project, the agent may encounter several workspaces — multiple project folders, multiple package skills, or both. Keep clear which workspace an action or prompt is referring to — surfaces from different workspaces should not be confused.

When a surface mentions another skill or reference, load it only if the relevant guidance is not already in context. This applies across all agentos surfaces.

## The Index

The Agentos Index is a concept and design knowledge base — a searchable collection of named entries that capture what a project or package knows about itself. Its atomic content is the typed `Index.Line`; lines attach to a **Kernel Block**, a short named section that supplies their concept context and presents distinct dimensions with minimal overlap. The index is the primary discovery surface — where agents go to understand, question, or extend a project's design.

Concepts are named using **Dotted Notation** — compound names like `Vertical.Slice` or `Agentos.Index.System` that serve as stable identifiers.

Indexes are distributed across routed chapters plus appendix depth:

- `design/` — the default `Index.Chapter`: conceptual fundamentals in flat numbered files (`100-design.md`, `101-design.md`, ...) whose suffix names the chapter. The loading policy is open — when in doubt, search the default chapter only.
- specialized chapters — indexed data with a narrower role. A package may choose an optional `poi/` `POI.Catalog`; executable POI classes are normally discovered from their canonical annotations on the checks that emit them.
- `appendix/` — on-demand depth. Contains concept-named files (`Concept.Name-appendix.md`) — check if one exists when you need depth beyond the index block.

The **router** maps every concept name to the file that holds it — always read this first. Package indexes use `000-INDEX.md`; project-local indexes use `001-index.md`.

Two further layers ride on the blocks — gesture-level here, the index owns the detail:

- **Typed lines** — index lines carry a `Line.Type` from a small vocabulary (`- [CT] ...`), classifying each line's act: define, decide, constrain, reject, orient, free, exemplify. Load `tarav-hugentics --type` for reading and proposing types.
- **Grounding** — grounding is a line property: a concept's evidence links trail inline on its lines as anchors (`^c20260630-0u`), resolved through the Anchory subsystem back to the chats. See `Index.Line` and `Anchory.System` in the index.

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

`tarav-pkg` is the core package skill for the agentos framework. It is the dependency root — other agentos package skills depend on it for the project model, skill model, index model, and workflow concepts.

This package owns: the Agentos Index system, the Hugentic workflow harness, live surface conventions, and the project structure model.

Separate packages exist for other systems:

- `tarav-chatlas-pkg` — session dataset system (query, export, continuation)
- `tarav-iterante-pkg` — mission harness and iterative workflows

`tarav-pkg` is not the same as the `agentos-md` repository — `agentos-md` is one implementation project; `tarav-pkg` is the portable package skill that any project can use.

## Agentos CLI

The `agentos` CLI is available for discovery and operations. Run `agentos --help` to see what it can do.

For configuring and syncing project-local imported skills, read `references/skills-routing.md`.

For provider account credential artifact reconciliation and troubleshooting, use the `tarav-agent-account-management` skill.

## Skill.Arg.Section

Only external data consumed by the selected module is a `Skill.Arg`. Operation flags belong to `Batchy.Router` below.

### Skill.Arg::Target.Depot
- the Project or Package Index depot the retrofit supervisor surveys
- required: true
- flags: --depot
- active only with: --index-retrofit
- help: "the Index depot to survey for retrofit work"
- examples: --depot tarav-chatlas-pkg, --depot skills/tarav-pkg

### Skill.Arg::Target.Scope
- an optional caller-imposed boundary inside the target depot
- required: false
- default: the retrofit supervisor computes a useful bounded scope from the whole depot
- flags: --scope
- repeatable: true
- active only with: --index-retrofit
- help: "override automatic retrofit scope selection"
- examples: --scope design/100-design.md, --scope Chatlas.Anchory

## Package.Driver.Router

This `Package.Driver.Router` is a specialized `Routing.Table` that sends a package-level need to the narrower skill or configured Hugentics route that owns it. Each cross-skill call keeps its routed effect in `--to` and declares its typed whole-file loading edge separately in `--load`.

Selection cardinality: `many`.

### `^route-hugentics-session`

- match: `semantic`
- destinations: `tarav-hugentics`
- loads: `@<tarav-hugentics>/SKILL.md`
- when: the caller needs Hugentic session control, Index research, editing, diagnosis, maintenance, or a structured human-agent workflow
- then: load tarav-hugentics

### `^route-product-design`

- match: `semantic`
- destinations: `tarav-hugentics --design`
- loads: `@<tarav-hugentics>/SKILL.md`
- when: the caller wants touched-data-contextualized product design
- then: load tarav-hugentics --design

### `^route-implementation`

- match: `semantic`
- destinations: `tarav-hugentics --impl`
- loads: `@<tarav-hugentics>/SKILL.md`
- when: the caller wants implementation design, execution, review, or end-to-end development
- then: load tarav-hugentics --impl

### `^route-workflow-status`

- match: `semantic`
- destinations: `tarav-hugentics --workflow-status`
- loads: `@<tarav-hugentics>/SKILL.md`
- when: the caller wants a structured checkpoint for an active workflow
- then: load tarav-hugentics --workflow-status

### `^route-index-retrofit`

- match: `explicit-or-semantic`
- flags: `--index-retrofit`
- destinations: `Index.Retrofit.Workflow.Module`
- loads: `references/index-retrofit.md`, `references/index-retrofit-worker.md`
- when: the caller wants an Index depot surveyed and a supervisor-led retrofit campaign proposed or run without loading transcripts into the supervisor context
- then: load the retrofit supervisor and worker contracts; survey first and pause before spawning research agents

### `^route-index-retrofit-depot-arg`

- match: `explicit`
- flags: `--depot`
- destinations: `Skill.Arg::Target.Depot`
- then: bind the target Index depot for Index.Retrofit.Workflow.Module

### `^route-index-retrofit-scope-arg`

- match: `explicit`
- flags: `--scope`
- destinations: `Skill.Arg::Target.Scope`
- then: bind an optional caller-imposed scope; otherwise let the retrofit supervisor compute one

### `^route-live-surfaces`

- match: `semantic`
- destinations: `tarav-live-surfaces`
- loads: `@<tarav-live-surfaces>/SKILL.md`
- when: the caller needs live-note or live-script location, naming, or numbering
- then: load tarav-live-surfaces

### `^route-batchy-skills`

- match: `semantic`
- destinations: `tarav-batchy-skills`
- loads: `@<tarav-batchy-skills>/SKILL.md`
- when: the caller needs Agentos skill taxonomy, calling conventions, argument parsing, or routing conventions
- then: load tarav-batchy-skills

### `^route-skill-development`

- match: `semantic`
- destinations: `tarav-skills-ingenier`
- loads: `@<tarav-skills-ingenier>/SKILL.md`
- when: the caller wants to create or upgrade a skill
- then: load tarav-skills-ingenier

### `^route-codebase-cleanup`

- match: `semantic`
- destinations: `tarav-hugentics --clean`
- loads: `@<tarav-hugentics>/SKILL.md`
- when: the caller wants a targeted codebase cleanup through the Hugentic harness
- then: load tarav-hugentics --clean

### `^route-git-commit`

- match: `semantic`
- destinations: `tarav-git-commit`
- loads: `@<tarav-git-commit>/SKILL.md`
- when: the caller explicitly requests a deterministic semantic commit workflow
- then: load tarav-git-commit

### `^route-chatlas-package`

- match: `semantic`
- destinations: `tarav-chatlas-pkg`
- loads: `@<tarav-chatlas-pkg>/SKILL.md`
- when: the caller needs to query, export, or continue a previous agent session
- then: load tarav-chatlas-pkg

### `^route-account-management`

- match: `semantic`
- destinations: `tarav-agent-account-management`
- loads: `@<tarav-agent-account-management>/SKILL.md`
- when: the caller needs to inspect, activate, repair, or diagnose provider accounts and provider homes
- then: load tarav-agent-account-management

### `^route-anchory-package`

- match: `semantic`
- destinations: `tarav-anchory-pkg`
- loads: `@<tarav-anchory-pkg>/SKILL.md`
- when: the caller needs anchor literacy, resolution, registration, or depot operation
- then: load tarav-anchory-pkg

### `^route-support-chats`

- match: `semantic`
- destinations: `tarav-support-chats`
- loads: `@<tarav-support-chats>/SKILL.md`
- when: the caller needs to discover, audit, or synchronize the chats supporting a Project or Package Index
- then: load tarav-support-chats

### `^route-forum`

- match: `semantic`
- destinations: `tarav-forum`
- loads: `@<tarav-forum>/SKILL.md`
- when: the caller needs to post, check, or read the Agentos forum
- then: load tarav-forum

### `^route-master-package-agent`

- match: `semantic`
- destinations: `tarav-master-pkg-agent`
- loads: `@<tarav-master-pkg-agent>/SKILL.md`
- when: the caller asks a separate read-only agent to research across Agentos packages
- then: load tarav-master-pkg-agent

### `^route-session-supervisor`

- match: `semantic`
- destinations: `tarav-session-supervisor`
- loads: `@<tarav-session-supervisor>/SKILL.md`
- when: the caller wants read-only supervision of another Chatlas-backed agent session
- then: load tarav-session-supervisor

### `^route-skillware`

- match: `semantic`
- destinations: `tarav-skillware`
- loads: `@<tarav-skillware>/SKILL.md`
- when: the caller needs Skillware doctrine, authoring, building, checking, or adoption
- then: load tarav-skillware

### `^route-testground`

- match: `semantic`
- destinations: `tarav-testground`
- loads: `@<tarav-testground>/SKILL.md`
- when: the caller needs package-skill behavioral test design, execution, or evaluation
- then: load tarav-testground

## Further Discovery

For deeper understanding of agentos concepts, search the `tarav-pkg` index:

- Search for `Kernel.Writing` to understand the writing philosophy behind index blocks
- Search for `Kernel.Block` to understand the structure of index entries
- Search for `Agentos.Index.System` to understand how the index system is designed
- Search for `Alignment.Loop` to understand how human-agent workflows converge
- Search for `Development.Principles` to understand implementation discipline
