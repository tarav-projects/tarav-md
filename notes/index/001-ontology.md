# Agentos Ontology Registry

## Index.Note

- `Index.Note` is the structural index of `notes/index/`
- lists what files exist in the index folder and how to navigate them
- maps the file tree, not the conceptual model — for concepts see `Index.Ontology.Note`
- reserved at `000-index.md` — stable path, always the entry point for folder orientation

****

## Index.Ontology.Note

- `Index.Ontology.Note` is the concept-space map of the Agentos index
- low-resolution registry: records what concepts exist, gives each a compact definition, points to fuller notes
- organized by `Ontology.Namespaces` — multiple overlapping views over the same concepts
- a concept lives in one file (routed by `Index.Note`) but can appear in multiple namespaces here
- not the place for deep treatment — that lives in concept notes
- reserved at `001-ontology.md` — stable path, always the entry point for concept lookup

****

## Agentos.Index.Notes

- `Agentos.Index.Notes` is the durable concept-note subsystem of an Agentos-style project
- implements the `Agentos.Index` — a `Soft.Programming.Language` for project knowledge
- see `114-Agentos.Index.Notes.md`

****

## Agentos.Index.Writing.Principles

- `Agentos.Index.Writing.Principles` defines what belongs in durable index notes
- all index content is organized as `Named.Concepts` in `Index.Blocks`
- see `114-Agentos.Index.Notes.md`

****

## Md.Surface

- `Md.Surface` is a qualifier for the markdown layer of a target
- see `115-Md.Surface.md`

****

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- see `116-Dotted.Notation.md`

****

## Dotted.Parameterized.Notation

- `Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept
- see `116-Dotted.Notation.md`

****

## File.Numbering.Protocol

- `File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces
- see `117-File.Numbering.Protocol.md`

****

## Maintenance.System

- `Maintenance.System` defines how a project surface is diagnosed over time
- see `118-Maintenance.System.md`

****

## Agentos.Project

- `Agentos.Project` is a concrete project that adopts the `Agentos.Stack` model
- see `119-Agentos.Project.md`

****

## Agentos.AGENTS.md

- `Agentos.AGENTS.md` is the project-local natural-language instruction surface at `.agentos/AGENTS.md`
- see `119-Agentos.Project.md`

****

## Project.Discovery.System

- `Project.Discovery.System` resolves a command or workflow to an `Agentos.Project` target
- see `119-Agentos.Project.md`

****

## Agentos.Skills

- `Agentos.Skills` defines skill selection, routing, and import behavior for Agentos projects
- see `120-Agentos.Skills.md`

****

## Usage.Surface

- `Usage.Surface` is the usage-useful subset of `Public.Surface`
- see `120-Agentos.Skills.md`

****

## Usage.Skill

- `Usage.Skill` is a special-purpose, usage-centric skill designed primarily as documentation
- see `120-Agentos.Skills.md`

****

## Project.Surfaces

- `Project.Surfaces` is a built-in `Ontology.Namespace` for the surfaces the index covers
- see `002-surfaces.md`

****

## Stable.Surface

- `Stable.Surface` is a durable, authoritative surface where a specific facet of project knowledge lives
- see `100-Agentos.Surfaces.md`

****

## Natural.Placement

- `Natural.Placement` is the principle that each surface holds the facet of a concept that is natural to its function
- see `100-Agentos.Surfaces.md`

****

## Index.Concept.Coverage

- the index is the collection point for all `Named.Concepts` in the project's stable surfaces
- see `114-Agentos.Index.Notes.md`

****

## Complete.Index.Block

- `Complete.Index.Block` is an `Index.Block` with an `### appendix` section for extended material
- see `114-Agentos.Index.Notes.md`

****

## Index.Appendix.Block

- `Index.Appendix.Block` is an appendix-only block hosted at `notes/appendix/`
- see `114-Agentos.Index.Notes.md`

****

## Design.Index.Block

- `Design.Index.Block` is a session-local `Complete.Index.Block` used in `Design.Session` artifacts
- see `114-Agentos.Index.Notes.md`

****

## Design.Session

- `Design.Session` is a scoped human-agent convergence surface for design work
- see `121-Design.Session.md`

****

## Session.Runtime.Loop

- `Session.Runtime.Loop` is the general workflow the agent tries to make a `Design.Session` follow
- see `121-Design.Session.md`

****

## InChat.Design.Session

- `InChat.Design.Session` is the default `Design.Session` backend — state lives in chat
- see `121-Design.Session.md`

****

## Artifact.Design.Session

- `Artifact.Design.Session` is the file-backed `Design.Session` backend — state lives in a `Live.Note`
- see `121-Design.Session.md`

****

## Impl.Req

- `Impl.Req` is an implementation-request artifact — a surface for designing and tracking an implementation plan
- see `123-Impl.Req.md`

****

## Vertical.Slice

- `Vertical.Slice` is the preferred shape of implementation work — thin end-to-end changes
- see `123-Impl.Req.md`

****

## No.Legacy.Allowed

- `No.Legacy.Allowed` is an implementation constraint: do not leave stale state behind
- see `123-Impl.Req.md`

****

## Test.At.Boundaries

- `Test.At.Boundaries` is the testing guidance: test through public interfaces, not implementation details
- see `123-Impl.Req.md`

****

## Deep.Modules

- `Deep.Modules` is an architectural principle: small interface, hidden complexity
- see `125-Development.Principles.md` (pending)

****

## Agent.Navigable.Codebase

- `Agent.Navigable.Codebase` is the structural principle that code should be organized so agents can explore naturally
- see `125-Development.Principles.md` (pending)

****

## Design.Target.Model

- `Design.Target.Model` is the current explicit design model of a system — distributed across surfaces, with the index as discovery layer
- see `124-Development.Model.md`

****

## Current.Implementation

- `Current.Implementation` is the current realized state of a system
- see `124-Development.Model.md`

****

## Progress.Gradient

- `Progress.Gradient` is the current best direction of movement between `Current.Implementation` and `Design.Target.Model`
- see `124-Development.Model.md`

****

## Design.Implementation.CoEvolution

- `Design.Implementation.CoEvolution` is the development dynamic where design and implementation reshape each other
- see `124-Development.Model.md`
