# Agentos Subsystems And Hugentic Flow - design-session

## Motivation

Define the first Agentos subsystem ontology so Agentos can be modeled as a complex stack with named subsystems.

The immediate need is to stop treating the md-heavy human-agent development framework as all of Agentos. Agentos has multiple subsystems, including project identity, skills, CLI, Chatlas, Tape, Forum, and the human-agent development workflow surface. This session introduces `Hugentic`, defines `Agentos.Hugentic.Flow`, defines the general subsystem model, and establishes `Agentos.Subsystem.Registry` as the subsystem namespace/subchapter inside the ontology registry.

## Items

- Hugentic.Concept: [closed] define `Hugentic` as adjective/concept for systems designed at the human-agentic interface
- Agentos.Hugentic.Flow: [closed] define the subsystem for human-agent project-development workflows
- Agentos.Subsystem.Model: [closed] define what counts as an Agentos subsystem and how subsystem notes/components work
- Agentos.Subsystem.Registry: [closed] define the subsystem namespace/subchapter inside the ontology registry, including when it lives in `ontology.md` versus a linked-out index file

## Hugentic.Concept

Current direction: `Hugentic` describes a system, surface, workflow, or project designed for the human-agentic interface.

A Hugentic thing is built so humans and agents can coordinate, exchange context, make decisions, and co-work through explicit surfaces rather than hidden or one-off interaction.

Examples:

- a Hugentic project exposes surfaces that humans and agents can both use
- a Hugentic workflow preserves enough context for collaboration across turns and sessions
- a Hugentic note surface makes design intent legible to both humans and agents
- a Hugentic CLI moves deterministic work out of fragile chat interaction

`Hugentic` is usable as an adjective. It can describe projects, surfaces, workflows, systems, or interfaces.

## Agentos.Hugentic.Flow

Current direction: `Agentos.Hugentic.Flow` is the integrated Agentos subsystem of components and workflows that significantly shape how humans and agents collaborate while developing projects.

Hugentic Flow defines the workflows, markdown surfaces, skills, artifacts, doctor passes, design discussions, implementation handoffs, and maintenance loops that let humans and agents co-develop projects with durable memory and explicit collaboration surfaces.

Inclusion rule:

A component belongs to Hugentic Flow when it meaningfully changes both sides of the collaboration workflow: how the human works and how the agent works.

Common implementation forms include many md surfaces, most non-automatic workflow skills, and some supporting Agentos commands or conventions. But a component does not belong to Hugentic Flow merely because an agent uses it.

Canonical examples:

- `agentos-design-session`, because it changes the human workflow through externalized design state and user-gated decisions, and changes the agent workflow through explicit session state, item tracking, and capture discipline.
- `Agentos.Index.Notes`, because it changes the human workflow by making design intent durable and browsable, and changes the agent workflow by making the index the design SSOT and concept lookup surface.
- `Agentos.Project.Doctor`, because it changes the human workflow by producing report-first project diagnosis, and changes the agent workflow through structured checks, evidence, and no-fix default behavior.
- `TODOS.Note`, because it changes the human workflow by giving a common parking surface for deferred work, and changes the agent workflow by avoiding hidden reminders or chat-only TODOs.

Boundary note:

Hugentic Flow is allowed to be somewhat blurry because it is an integrated workflow subsystem. The blur should be controlled by the human-plus-agent workflow impact test.

Working subsystem-note draft:

```md
# Agentos.Hugentic.Flow

`Agentos.Hugentic.Flow` is the integrated Agentos subsystem of components and workflows that significantly shape how humans and agents collaborate while developing projects.

Hugentic Flow defines the workflows, markdown surfaces, skills, artifacts, doctor passes, design discussions, implementation handoffs, and maintenance loops that let humans and agents co-develop projects with durable memory and explicit collaboration surfaces.

## Responsibility

Hugentic Flow owns the model for human-agent project development.

It explains how humans and agents collaborate during project work: how they capture durable design, use live work surfaces, run design sessions, create artifacts, inspect project health, package reusable behaviors, leave traces, and move from exploratory discussion into implementation or maintenance.

## Boundaries

Hugentic Flow is not all of Agentos.

It does not own the full CLI, Chatlas, Tape, Forum, Iterante, or the project identity system. Those systems can support Hugentic Flow workflows, and Hugentic Flow can define how they participate in human-agent development, but they remain independently named subsystems.

## Components

Current components include:

- `Agentos.Index.Notes`, the durable design surface for concepts, constraints, rationale, naming, and reusable patterns.
- `Agentos.Project.Doctor`, the diagnosis-first workflow for evaluating how well a project conforms to `Agentos.Stack`.
- `Agentos.Dev.Notes`, the internal development markdown surface for project work.
- `TODOS.Note`, the lightweight reserved live note for deferred work.
- `Live.Scripts`, the script-shaped working surface for executable or executable-looking exploration.
- Design-session and design-summary artifacts, which support convergence from discussion into durable design or implementation.
- Implementation-request and issue-report artifacts, which support follow-up implementation and maintenance work.
- Hugentic Flow workflow skills such as `agentos-design-discussion`, `agentos-design-session`, `agentos-design-implementation`, `agentos-project-doctor`, and artifact skills.
- Markdown coordination guidance such as `AGENTS.md`, when used as local agent workflow guidance rather than design authority.

## Current Md Surface

The current Agentos markdown implementation of Hugentic Flow lives mainly in `agentos-md`.

Important surfaces include:

- `notes/index/`
- `notes/live/`
- `skills/`
- `AGENTS.md`

## Related Subsystems

- `Agentos.Project.System`, because Hugentic Flow work usually happens relative to a project target.
- `Agentos.Skill.System`, because reusable agent behavior is packaged as skills.
- `Agentos.CLI.System`, because deterministic project operations should move into CLI commands when useful.
- `Agentos.Chatlas`, because preserved session data can support continuity, audit, and history-aware workflows.
- `Agentos.Tape.System`, because some durable traces and structured records may use tape-like storage.
- `Agentos.Forum`, because multi-agent coordination may need shared local communication surfaces.
- `Agentos.Iterante`, because iterative agent execution can support or automate Hugentic Flow workflows.
```

## Agentos.Subsystem.Model

Topic framing: define what counts as an Agentos subsystem and how subsystem notes/components work.

Current direction:

- Agentos should be modeled as `Agentos.Stack`, a complex stack made of named subsystems.
- An `Agentos.Subsystem` is a named responsibility area inside `Agentos.Stack`.
- These are better understood as `Agentos.Soft.Subsystem`s: conceptual responsibility areas, not hard ownership containers.
- Subsystems should be named by conceptual responsibility, not by repo, folder, package, or implementation layout.
- Subsystems can use shared primitives and components.
- A component can participate in multiple subsystems.
- The md surface should not force a folder-per-subsystem layout.

Working definition:

An `Agentos.Soft.Subsystem` is a named responsibility area inside `Agentos.Stack` that helps humans and agents orient around what a part of Agentos is for, what it coordinates, and what components commonly participate in it.

It is not defined by folder, repo, package, command namespace, or exclusive ownership. The same component can appear in more than one subsystem when it plays different roles.

Important: component lists are not ownership manifests. They are orientation surfaces.

This is why `Agentos.Project.Doctor` can be relevant to `Agentos.Hugentic.Flow`, `Agentos.Maintenance.System`, `Agentos.Skill.System`, and `Agentos.CLI.System` without creating a conflict.

`Subsystem.Note` is the preferred initial md representation:

- one dedicated index note defines a subsystem
- it explains responsibility and boundaries
- it lists important components in natural language
- it links related subsystems
- it does not require formal relationship labels yet

Current starting subsystem list:

- `Agentos.Hugentic.Flow`
- `Agentos.Project.System`
- `Agentos.Skill.System`
- `Agentos.CLI.System`
- `Agentos.Chatlas`
- `Agentos.Tape.System`
- `Agentos.Forum`

## Agentos.Subsystem.Registry

Current direction: `Agentos.Subsystem.Registry` is a special namespace/subregistry inside `Agentos.Index.Ontology.Registry`.

It curates subsystem concepts and provides a low-resolution map of Agentos subsystems. It is not a separate ontology and should not become a competing registry authority.

Physical representation can vary:

- as a `## Subsystems` section inside `notes/index/ontology.md`
- or as a linked-out index file under `notes/index/` if the subsystem list becomes too large

Conceptually:

- `Agentos.Index.Ontology.Registry` is the registry system
- `Agentos.Subsystem.Registry` is the subsystem namespace/subregistry inside that system
- it remains part of the ontology registry system in either physical form
- a physical linked-out file is only an implementation detail of the ontology surface

Purpose:

- give agents and humans a low-resolution map of Agentos subsystems
- act as a subindex for fuller subsystem notes
- keep subsystem orientation discoverable without requiring full-text search
- help avoid treating one subsystem, such as Hugentic Flow, as all of Agentos

## Notes

- The earlier working label `Agentos.Agentic.Dev.Framework` is superseded by `Agentos.Hugentic.Flow`.
- `Hugentic` is a proper design adjective/concept, not just a nickname.
- `Hugentic Flow` is the public subsystem name; `Agentos.Hugentic.Flow` is the ontology-qualified name.
- `Agentos.Subsystem.Registry` should be developed inside the ontology system, not beside it.

## End Log

- 2026-05-04: Created initial design-session artifact from converged discussion on Hugentic, Hugentic Flow, subsystem modeling, and subsystem registry framing.
- 2026-05-04: Closed `Hugentic.Concept` and `Agentos.Subsystem.Registry` as sufficient for this session.
- 2026-05-04: Closed `Agentos.Subsystem.Model` and `Agentos.Hugentic.Flow` as sufficient first-pass subsystem design definitions.
