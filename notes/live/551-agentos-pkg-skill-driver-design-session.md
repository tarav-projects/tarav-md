# agentos-pkg SKILL.md Driver — Design Session

## Session.Abstract

- Goal: redesign `agentos-pkg/SKILL.md` as the Driver of the agentos system
- The current SKILL.md is a routing table for insiders; the new one teaches agents from zero
- Format: one `Kernel.Block::Design` per section, six sections total
- State: all six blocks converged — design complete

## Design.Index

****

## What.is.Agentos

- the section should introduce agentos as a toolkit for agent-project workflows
- should convey that agentos gives agents shared, durable surfaces for orientation, design knowledge, working state, and structured collaboration
- should explain that agents working in an agentos project find maintained tools and persistent context instead of starting from scratch each session
- should name the main tools: concept indexes, live surfaces, package skills, and human-agent workflows
- should mention that any project can adopt agentos incrementally — an AGENTS.md and one package skill is enough to start
- should establish that this skill (`agentos-pkg`) is the entry point — it teaches agents how to discover and use agentos tools in whatever project they're working on

### meta

- status: converged
- maps to SKILL.md section 1

****

## Agentos.Workspace

- the section should present two important locations for agentos surfaces: project folders and package skills
- should define `Project.Folder` as where the project that users and agents are developing lives — in practice, a folder that stores notes, code, data, and other project material
- should mention that a `.agentos` folder is a hint that a folder might be an agentos project
- should list project-level surfaces: `AGENTS.md`, `notes/` (live notes, index, appendix), and `dev/` (scripts and tooling)
- should define `Package.Skill` as a reachable skill that serves as the agentic interface to a package — containing data, documentation, and operational instructions for using a package's functionalities
- should use `agentos-pkg` as a concrete example of a `Package.Skill`
- should list package-level surfaces: `index/`, `appendix/`, `references/`, and `SKILL.md`
- should warn that the agent may encounter several workspaces and must keep clear which workspace an action or prompt refers to
- should teach that when a surface mentions another skill or reference, the agent should load it only if the relevant guidance is not already in context — this applies across all agentos surfaces

### meta

- status: converged
- maps to SKILL.md section 2

****

## The.Index

- the section should introduce the Agentos Index as a concept and design knowledge base — a searchable collection of named entries that capture what a project or package knows about itself
- should explain that each entry is a `Kernel.Block` — a short, named section that describes one concept from multiple angles using direct, orthogonal lines
- should establish the index as the primary discovery surface — where agents go to understand, question, or extend a project's design
- should describe the two scopes: `index/` (always-loaded fundamentals) and `appendix/` (on-demand depth)
- should explain that `index/` contains flat numbered files (`100-index.md`, `101-index.md`, ...) where file names carry no semantic meaning
- should teach how to use the routing table — it maps every concept name to the file that holds it (`000-index.md` for package indexes, `001-index.md` for project-local indexes)
- should explain that `appendix/` contains concept-named files (`Concept.Name-appendix.md`) for depth beyond the index block
- should clarify that both project folders and package skills can have their own index — project index in `notes/index/`, package skill index in `<package-skill>/index/`
- should mention that if a project is developing a package skill, the agent can access both indexes locally
- should introduce `Dotted.Notation` as the naming convention for concepts
- should teach how to search: read the routing table, find the concept, read the file, check appendix for depth — or just wander around following your intuition
- the section must include file tree examples showing the index layout for the different situations (project-only, package-only, project developing a package)

### meta

- status: converged
- maps to SKILL.md section 3

****

## Local.Surfaces

- the section should present the local surfaces an agent may find in a project folder
- should frame these as the project's own working and knowledge surfaces — not part of any package skill
- should cover each surface briefly with a "why it exists" line:
  - `notes/index/` — project-local index layer (already covered in The.Index, light mention here)
  - `notes/appendix/` — project-local appendix depth (already covered in The.Index, light mention here)
  - `notes/live/` — maintained working files that persist across sessions, numbered with an incrementing prefix — common artifacts include design sessions, impl-reqs, issue reports, and working drafts
  - `notes/canvas/` — visual collaboration surfaces
  - `dev/live/` — small maintained code scripts and tooling snippets that persist across sessions
  - `AGENTS.md` — project-level agent instructions
- should keep descriptions short — this is orientation, not a manual for each surface

### meta

- status: converged
- maps to SKILL.md section 4

****

## Agentos.CLI

- the section should mention that the agent has access to the `agentos` CLI
- should point to `agentos --help` for discovering how to use it

### meta

- status: converged
- maps to SKILL.md section 5

****

## Go.Deeper

- the section should work as a router table — pointing the agent to narrower surfaces when the Driver is not enough
- should list available subsystems and skills of the package with a one-line "when to load"
- should not only point to loadable skills and references, but also suggest index search prompts for learning more about a topic
- for example: "search `agentos-pkg` index for `Kernel.Writing` to understand the writing philosophy" — providing the search hint so the agent knows what to query
- this combines skill routing with index discovery — the agent learns both where to go and what to ask

### meta

- status: converged
- maps to SKILL.md section 6
