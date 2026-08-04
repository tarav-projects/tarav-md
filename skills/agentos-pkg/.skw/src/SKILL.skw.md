---
name: agentos-pkg
description: "Agentos provides shared tools for agent-project workflows: concept indexes, human-agent design sessions, implementation workflows, live notes, package skills, and more. USE WHEN working with any of these — or when a project's AGENTS.md routes here. After loading, the agent gets workflow-neutral orientation: what tools exist, where each subsystem starts, and which narrower surface to load next."
---

# agentos-pkg

> $kw: ^driver-critical-context --dev-from Cited.Duplication --dev-from Context.Loading.Path --dev-from Package.Driver.Base --dev-from SKILL.Loading
> --supp root driver context is selected by the alignment failure its absence could cause, not by minimizing line count; preserve context whose omission could make the agent misunderstand authority, violate a gate, select the wrong workflow, or lose the session model ^c20260729-48u
> $kw: --from Alignment.Loop --from Anchory.System --from Batchy.Router --from Batchy.Skill --from Batchy.Skill.Banner --from Development.Principles --from Kernel.Writing --from Package.Driver.Router --from POI.Catalog --from Routing.Table --from Skill.Arg --from Skill.Module --from User.Command --from Vertical.Slice

Agentos is a toolkit for agent-project workflows. It gives agents shared, durable surfaces for orientation, design knowledge, working state, and structured collaboration. Instead of starting from scratch each session, agents working in an agentos project find maintained tools and persistent context.

The main tools: concept indexes, live surfaces, package skills, and human-agent workflows.

Any project can adopt agentos incrementally — an AGENTS.md and one package skill is enough to start. This skill (`agentos-pkg`) is the entry point to the system toolkit — it teaches agents how to discover and use agentos tools in whatever project they're working on.

Paths in this skill are package-root-relative unless explicitly absolute. For example, `000-INDEX.md` means `agentos-pkg/000-INDEX.md`.

> $kw: ^agentos-pkg-batchy-runtime-contract --copy
> --from @<agentos-batchy-skills>/references/batchy-skill-run.skw.md^batchy-skill-runtime-contract

This is a `Batchy.Skill`, called like a CLI and resolved by one `Batchy.Router`. This compact contract is materialized from `agentos-batchy-skills`; load that skill when the full convention is needed.

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

> $kw. end

## Agentos Workspace

> $kw: ^driver-workspace-literacy

Two important locations for agentos surfaces: project folders and package skills.

A **Project Folder** is where the project that users and agents are developing lives — in practice, a folder that stores notes, code, data, and other project material. A `.agentos` folder is a hint that a folder might be an agentos project. At the project level, look for `AGENTS.md`, `notes/` (live notes, index, appendix), and `dev/` (scripts and tooling).

A **Package Skill** is a reachable skill that serves as the agentic interface to a package — it contains data, documentation, and operational instructions for using a package's functionalities. For instance, `agentos-pkg` is the Package Skill of the agentos framework. At the package level, a package skill contains its own `000-INDEX.md`, `design/`, optional specialized chapters such as `poi/`, `appendix/`, `references/`, and `SKILL.md`.

When working in a project, the agent may encounter several workspaces — multiple project folders, multiple package skills, or both. Keep clear which workspace an action or prompt is referring to — surfaces from different workspaces should not be confused.

When a surface mentions another skill or reference, load it only if the relevant guidance is not already in context. This applies across all agentos surfaces.

> $kw. end

## The Index

> $kw: ^driver-index-literacy --derived
> --from Agentos.Index.System
> --from Dotted.Notation
> --from Index.Appendix
> --from Index.Chapter
> --from Index.Line
> --from Kernel.Block
> --from Line.Type
> --from Package.Skill
> --from Touched.Index
> --intent adapt the index ontology into package-driver literacy sufficient for
> --cont discovery, correct routing, and interpretation of typed and grounded
> --cont content; keep operational mechanics outside this guaranteed projection

The Agentos Index is a concept and design knowledge base — a searchable collection of named entries that capture what a project or package knows about itself. Its atomic content is the typed `Index.Line`; lines attach to a **Kernel Block**, a short named section that supplies their concept context and presents distinct dimensions with minimal overlap. The index is the primary discovery surface — where agents go to understand, question, or extend a project's design.

Concepts are named using **Dotted Notation** — compound names like `Vertical.Slice` or `Agentos.Index.System` that serve as stable identifiers.

Indexes are distributed across routed chapters plus appendix depth:

- `design/` — the default `Index.Chapter`: conceptual fundamentals in flat numbered files (`100-design.md`, `101-design.md`, ...) whose suffix names the chapter. The loading policy is open — when in doubt, search the default chapter only.
- specialized chapters such as `poi/` — indexed data with a narrower role; `poi/` is the machine-discoverable `POI.Catalog` of package-owned class blocks.
- `appendix/` — on-demand depth. Contains concept-named files (`Concept.Name-appendix.md`) — check if one exists when you need depth beyond the index block.

The **router** maps every concept name to the file that holds it — always read this first. Package indexes use `000-INDEX.md`; project-local indexes use `001-index.md`.

Two further layers ride on the blocks — gesture-level here, the index owns the detail:

- **Typed lines** — index lines carry a `Line.Type` from a small vocabulary (`- [CT] ...`), classifying each line's act: define, decide, constrain, reject, orient, free, exemplify. Load `agentos-hugentics --type` for reading and proposing types.
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
├── poi/
│   └── 100-poi.md              ← optional package-owned POI classes
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

> $kw. end

## Local Surfaces

> $kw: ^driver-local-surfaces-literacy

A project folder may contain several local surfaces — the project's own working and knowledge spaces:

- `AGENTS.md` — project-level agent instructions
- `notes/index/` — project-local index layer (see The Index above)
- `notes/appendix/` — project-local appendix depth (see The Index above)
- `notes/live/` — maintained working files that persist across sessions, numbered with an incrementing prefix. Common artifacts: design sessions, impl-reqs, issue reports, and working drafts.
- `notes/canvas/` — visual collaboration surfaces
- `dev/live/` — small maintained code scripts and tooling snippets that persist across sessions

> $kw. end

## Package

> $kw: ^driver-package-literacy

`agentos-pkg` is the core package skill for the agentos framework. It is the dependency root — other agentos package skills depend on it for the project model, skill model, index model, and workflow concepts.

This package owns: the Agentos Index system, the Hugentic workflow harness, live surface conventions, and the project structure model.

Separate packages exist for other systems:

- `agentos-chatlas-pkg` — session dataset system (query, export, continuation)
- `agentos-iterante-pkg` — mission harness and iterative workflows

`agentos-pkg` is not the same as the `agentos-md` repository — `agentos-md` is one implementation project; `agentos-pkg` is the portable package skill that any project can use.

> $kw. end

## Agentos CLI

> $kw: ^driver-cli-literacy

The `agentos` CLI is available for discovery and operations. Run `agentos --help` to see what it can do.

For configuring and syncing project-local imported skills, read `references/skills-routing.md`.

For provider account credential artifact reconciliation and troubleshooting, use the `agentos-agent-account-management` skill.

> $kw. end

## Package.Driver.Router

> $kw: --dev-from Package.Driver.Router
> $kw: ^package-driver-router --routing-table --select many

This `Package.Driver.Router` is a specialized `Routing.Table` that sends a package-level need to the narrower skill or configured Hugentics route that owns it. Each cross-skill call keeps its routed effect in `--to` and declares its typed whole-file loading edge separately in `--load`.

> $kw: ^route-hugentics-session --router-row --table ^package-driver-router
> --match semantic
> --to agentos-hugentics
> --load @<agentos-hugentics>/SKILL.md
> --when the caller needs Hugentic session control, Index research, editing, diagnosis, maintenance, or a structured human-agent workflow
> --then load agentos-hugentics

> $kw: ^route-product-design --router-row --table ^package-driver-router
> --match semantic
> --to agentos-hugentics --design
> --load @<agentos-hugentics>/SKILL.md
> --when the caller wants touched-data-contextualized product design
> --then load agentos-hugentics --design

> $kw: ^route-implementation --router-row --table ^package-driver-router
> --match semantic
> --to agentos-hugentics --impl
> --load @<agentos-hugentics>/SKILL.md
> --when the caller wants implementation design, execution, review, or end-to-end development
> --then load agentos-hugentics --impl

> $kw: ^route-workflow-status --router-row --table ^package-driver-router
> --match semantic
> --to agentos-hugentics --workflow-status
> --load @<agentos-hugentics>/SKILL.md
> --when the caller wants a structured checkpoint for an active workflow
> --then load agentos-hugentics --workflow-status

> $kw: ^route-live-surfaces --router-row --table ^package-driver-router
> --match semantic
> --to agentos-live-surfaces
> --load @<agentos-live-surfaces>/SKILL.md
> --when the caller needs live-note or live-script location, naming, or numbering
> --then load agentos-live-surfaces

> $kw: ^route-batchy-skills --router-row --table ^package-driver-router
> --match semantic
> --to agentos-batchy-skills
> --load @<agentos-batchy-skills>/SKILL.md
> --when the caller needs Agentos skill taxonomy, calling conventions, argument parsing, or routing conventions
> --then load agentos-batchy-skills

> $kw: ^route-skill-development --router-row --table ^package-driver-router
> --match semantic
> --to agentos-skills-ingenier
> --load @<agentos-skills-ingenier>/SKILL.md
> --when the caller wants to create or upgrade a skill
> --then load agentos-skills-ingenier

> $kw: ^route-codebase-cleanup --router-row --table ^package-driver-router
> --match semantic
> --to agentos-hugentics --clean
> --load @<agentos-hugentics>/SKILL.md
> --when the caller wants a targeted codebase cleanup through the Hugentic harness
> --then load agentos-hugentics --clean

> $kw: ^route-git-commit --router-row --table ^package-driver-router
> --match semantic
> --to agentos-git-commit
> --load @<agentos-git-commit>/SKILL.md
> --when the caller explicitly requests a deterministic semantic commit workflow
> --then load agentos-git-commit

> $kw: ^route-project-doctor --router-row --table ^package-driver-router
> --match semantic
> --to agentos-project-doctor
> --load @<agentos-project-doctor>/SKILL.md
> --when the caller wants a project-health or Agentos-conformance diagnosis
> --then load agentos-project-doctor

> $kw: ^route-chatlas-package --router-row --table ^package-driver-router
> --match semantic
> --to agentos-chatlas-pkg
> --load @<agentos-chatlas-pkg>/SKILL.md
> --when the caller needs to query, export, or continue a previous agent session
> --then load agentos-chatlas-pkg

> $kw: ^route-account-management --router-row --table ^package-driver-router
> --match semantic
> --to agentos-agent-account-management
> --load @<agentos-agent-account-management>/SKILL.md
> --when the caller needs to inspect, activate, repair, or diagnose provider accounts and provider homes
> --then load agentos-agent-account-management

> $kw: ^route-anchory-package --router-row --table ^package-driver-router
> --match semantic
> --to agentos-anchory-pkg
> --load @<agentos-anchory-pkg>/SKILL.md
> --when the caller needs anchor literacy, resolution, registration, or depot operation
> --then load agentos-anchory-pkg

> $kw: ^route-support-chats --router-row --table ^package-driver-router
> --match semantic
> --to agentos-support-chats
> --load @<agentos-support-chats>/SKILL.md
> --when the caller needs to discover, audit, or synchronize the chats supporting a Project or Package Index
> --then load agentos-support-chats

> $kw: ^route-forum --router-row --table ^package-driver-router
> --match semantic
> --to agentos-forum
> --load @<agentos-forum>/SKILL.md
> --when the caller needs to post, check, or read the Agentos forum
> --then load agentos-forum

> $kw: ^route-master-package-agent --router-row --table ^package-driver-router
> --match semantic
> --to agentos-master-pkg-agent
> --load @<agentos-master-pkg-agent>/SKILL.md
> --when the caller asks a separate read-only agent to research across Agentos packages
> --then load agentos-master-pkg-agent

> $kw: ^route-session-supervisor --router-row --table ^package-driver-router
> --match semantic
> --to agentos-session-supervisor
> --load @<agentos-session-supervisor>/SKILL.md
> --when the caller wants read-only supervision of another Chatlas-backed agent session
> --then load agentos-session-supervisor

> $kw: ^route-skillware --router-row --table ^package-driver-router
> --match semantic
> --to agentos-skillware
> --load @<agentos-skillware>/SKILL.md
> --when the caller needs Skillware doctrine, authoring, building, checking, or adoption
> --then load agentos-skillware

> $kw: ^route-testground --router-row --table ^package-driver-router
> --match semantic
> --to agentos-testground
> --load @<agentos-testground>/SKILL.md
> --when the caller needs package-skill behavioral test design, execution, or evaluation
> --then load agentos-testground

> $kw: ^package-driver-routing-view --routing-view full --table ^package-driver-router

## Further Discovery

> $kw: ^driver-further-discovery

For deeper understanding of agentos concepts, search the `agentos-pkg` index:

- Search for `Kernel.Writing` to understand the writing philosophy behind index blocks
- Search for `Kernel.Block` to understand the structure of index entries
- Search for `Agentos.Index.System` to understand how the index system is designed
- Search for `Alignment.Loop` to understand how human-agent workflows converge
- Search for `Development.Principles` to understand implementation discipline

> $kw. end
