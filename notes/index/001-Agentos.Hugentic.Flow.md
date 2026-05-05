# Agentos.Hugentic.Flow

`Agentos.Hugentic.Flow` is the integrated Agentos subsystem of components and workflows that significantly shape how humans and agents collaborate while developing projects.

---

## What Agentos Is

Agentos is an operating system for agent-oriented work. It provides a modular but integrated set of subsystems, conventions, and reusable solutions for working with agents across projects.

Agentos is not only a collection of isolated tools. Its subsystems are designed to compose and interact so that projects can expose stable working surfaces for agents.

## Hugentic

`Hugentic` describes a system, surface, workflow, or project designed for the human-agentic interface.

A Hugentic thing is built so humans and agents can coordinate, exchange context, make decisions, and co-work through explicit surfaces rather than hidden or one-off interaction.

Examples:

- a Hugentic project exposes surfaces that humans and agents can both use
- a Hugentic workflow preserves enough context for collaboration across turns and sessions
- a Hugentic note surface makes design intent legible to both humans and agents
- a Hugentic CLI moves deterministic work out of fragile chat interaction

## What `Agentos.Hugentic.Flow` Is

`Agentos.Hugentic.Flow` defines the workflows, markdown surfaces, skills, artifacts, doctor passes, design discussions, implementation handoffs, and maintenance loops that let humans and agents co-develop projects with durable memory and explicit collaboration surfaces.

It is the public subsystem name for Agentos' human-agent project-development flow.

## Responsibility

Hugentic Flow owns the model for human-agent project development.

It explains how humans and agents collaborate during project work: how they capture durable design, use live work surfaces, run design sessions, create artifacts, inspect project health, package reusable behaviors, leave traces, and move from exploratory discussion into implementation or maintenance.

## Core Model

- An Agentos project has a stable base identity.
- Hugentic Flow sits on top of that base as a higher-level subsystem.
- The subsystem is defined by capabilities and workflow primitives, not by a rigid folder checklist or ownership manifest.
- Its surfaces are composable and opt-in, but they are also dependency-aware and designed to integrate cleanly.
- A component belongs to Hugentic Flow when it meaningfully changes both sides of the collaboration workflow: how the human works and how the agent works.
- Hugentic Flow is an `Agentos.Soft.Subsystem`: a conceptual responsibility area, not a hard ownership container.

## Boundaries

Hugentic Flow is not all of Agentos.

It does not own the full CLI, Chatlas, Tape, Forum, Iterante, or project identity system. Those systems can support Hugentic Flow workflows, and Hugentic Flow can define how they participate in human-agent development, but they remain independently named subsystems.

## Main Surfaces

- `skills/` packages reusable behaviors, especially workflow skills for adoption, maintenance, consolidation, and operation.
- `notes/live/` captures in-progress design and working state.
- `notes/index/` holds durable high-signal concept notes and steering constraints.
- `dev/live/` or equivalent live-script surfaces support executable exploration when needed.
- Durable artifacts such as design summaries capture converged decisions for later implementation or coordination.

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

Component lists are orientation surfaces, not ownership manifests. The same component can participate in more than one `Agentos.Soft.Subsystem`.

## Current Md Surface

The current Agentos markdown implementation of Hugentic Flow lives mainly in `agentos-md`.

Important surfaces include:

- `notes/index/`
- `notes/live/`
- `skills/`
- `AGENTS.md`

## Subsystem Notes

`Subsystem.Note` is the preferred initial md representation for an Agentos subsystem.

A subsystem note should define the subsystem, explain its responsibility and boundaries, list important components in natural language, and link related subsystems. It should not require formal relationship labels before the subsystem model needs them.

## Canonical Examples

- `agentos-design-session`, because it changes the human workflow through externalized design state and user-gated decisions, and changes the agent workflow through explicit session state, item tracking, and capture discipline.
- `Agentos.Index.Notes`, because it changes the human workflow by making design intent durable and browsable, and changes the agent workflow by making the index the design SSOT and concept lookup surface.
- `Agentos.Project.Doctor`, because it changes the human workflow by producing report-first project diagnosis, and changes the agent workflow through structured checks, evidence, and no-fix default behavior.
- `TODOS.Note`, because it changes the human workflow by giving a common parking surface for deferred work, and changes the agent workflow by avoiding hidden reminders or chat-only TODOs.

## Related Subsystems

- `Agentos.Project.System`
- `Agentos.Skill.System`
- `Agentos.CLI.System`
- `Agentos.Chatlas`
- `Agentos.Tape.System`
- `Agentos.Forum`
- `Agentos.Iterante`

## Workflow Philosophy

- Agent work should leave durable traces.
- Exploratory work and curated knowledge should remain distinct.
- Reusable project-development solutions should be packaged as subsystems and skills.
- Agents should work through recognizable workflows, not hidden personal conventions.
- Integration matters: modular subsystems should still expose a coherent working model together.

## Read Next

- `000-index.md` for the current surface map.
- `ontology.md` for registered Agentos concepts.
- `100-Agentos.Index.Notes.md` for the durable concept-note subsystem and SSOT rule.

## Provenance

Promoted from the closed design session at `../live/507-agentos-subsystems-hugentic-flow-design-session.md`.
