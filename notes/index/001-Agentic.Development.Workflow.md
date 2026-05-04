# Agentic.Development.Workflow

Welcome note for the Agentos subsystem that defines how projects are developed with agents.

---

## What Agentos Is

Agentos is an operating system for agent-oriented work. It provides a modular but integrated set of subsystems, conventions, and reusable solutions for working with agents across projects.

Agentos is not only a collection of isolated tools. Its subsystems are designed to compose and interact so that projects can expose stable working surfaces for agents.

## What `Agentic.Development.Workflow` Is

`Agentic.Development.Workflow` is the Agentos subsystem for developing projects with agents.

It defines the coordinated working model that lets humans and agents collaborate through recognizable surfaces, durable traces, and repeatable workflows rather than one-off ad hoc behavior.

## Core Model

- An Agentos project has a stable base identity.
- The agentic development workflow sits on top of that base as a higher-level subsystem.
- The subsystem is defined by capabilities and workflow primitives, not by a rigid folder checklist.
- Its surfaces are composable and opt-in, but they are also dependency-aware and designed to integrate cleanly.

## Main Surfaces

- `skills/` packages reusable behaviors, especially workflow skills for adoption, maintenance, consolidation, and operation.
- `notes/live/` captures in-progress design and working state.
- `notes/index/` holds durable high-signal concept notes and steering constraints.
- `dev/live/` or equivalent live-script surfaces support executable exploration when needed.
- Durable artifacts such as design summaries capture converged decisions for later implementation or coordination.

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
