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

## Ontology.Registry

- `Ontology.Registry` is the conceptual layer of the index that gives the full list of registered concepts
- one of the overlays on `notes/index/` — same files, different concern than file navigation
- `001-ontology.md` is the entry point that coordinates the registry
- organized through `Ontology.Namespaces` — multiple views over the same set of concepts
- a concept can have multiple blocks across namespaces, focusing on different aspects

****

## Ontology.Namespace

- `Ontology.Namespace` is an explicit bounded organizing view over ontology concepts
- namespaces share concepts — the same concept can appear in multiple namespaces
- a namespace is a concept itself — has a `Dotted.Name`, a `Kernel.Block:Index`, and can have an appendix file
- a namespace appendix file can contain multiple `Kernel.Block:Appendix` entries — concept views focused on that namespace's semantics
- coordinated from `001-ontology.md` — can be sections there or links to separate files

****

## Index.Architecture

- `Index.Architecture` is the structural design of the Agentos Index — also an `Ontology.Namespace`
- see `103-index.md`

****

## Flat.Index.Architecture

- `Flat.Index.Architecture` is the file-level design: anonymous flat containers, append-only writing, routing table
- see `103-index.md`

****

## Global.Index.Scope

- `Global.Index.Scope` is the always-loaded layer of the index — `notes/index/`
- see `103-index.md`

****

## Extended.Index.Scope

- `Extended.Index.Scope` is the on-demand layer of the index — `notes/appendix/`
- see `103-index.md`

****

## Agentos.Index

- `Agentos.Index` is a `Soft.Programming.Language` for project knowledge — a library of micro-prompts invoked by naming
- manipulates the agent's context window — by controlling what enters context, you control how the agent reasons
- enables semantic computation: composing concepts, finding contradictions, detecting design weakness
- also an `Ontology.Namespace` — groups the concepts that define the index system itself

****

## Agentos.Index.Notes

- `Agentos.Index.Notes` is one of the `Stable.Surfaces` of an Agentos-style project — the implementation of the `Agentos.Index`
- four roles: conceptual implementation, discovery index, development surface, main alignment surface
- see `100-index.md`

****

## Agentos.Index.Writing.Principles

- `Agentos.Index.Writing.Principles` defines what belongs in durable index notes
- all index content is organized as `Named.Concepts` in `Index.Blocks`
- see `100-index.md`

****

## Md.Surface

- `Md.Surface` is a qualifier for the markdown layer of a target
- see `100-index.md`

****

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- see `100-index.md`

****

## Dotted.Parameterized.Notation

- `Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept
- see `100-index.md`

****

## File.Numbering.Protocol

- `File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces
- see `100-index.md`

****

## Maintenance.System

- `Maintenance.System` defines how a project surface is diagnosed over time
- see `100-index.md`

****

## Agentos.Project

- `Agentos.Project` is a concrete project that adopts the `Agentos.Stack` model
- see `100-index.md`

****

## Agentos.AGENTS.md

- `Agentos.AGENTS.md` is the project-local natural-language instruction surface at `.agentos/AGENTS.md`
- see `100-index.md`

****

## Project.Discovery.System

- `Project.Discovery.System` resolves a command or workflow to an `Agentos.Project` target
- see `101-index.md`

****

## Agentos.Skills

- `Agentos.Skills` defines skill selection, routing, and import behavior for Agentos projects
- see `101-index.md`

****

## Usage.Surface

- `Usage.Surface` is the usage-useful subset of `Public.Surface`
- see `101-index.md`

****

## Usage.Skill

- `Usage.Skill` is a special-purpose, usage-centric skill designed primarily as documentation
- see `101-index.md`

****

## Chatlas.Query.Surface

- `Chatlas.Query.Surface` is the Chatlas session discovery interface family
- `chatlas index query` is the base index-row selection surface
- `chatlas query` is the higher-level session query surface that extends index selection with later query layers
- see `102-index.md`

****

## Chatlas.Query.Envelope

- `Chatlas.Query.Envelope` is the normalized top-level JSON response shape shared by Chatlas query surfaces
- it separates query phase counts from row projection
- see `102-index.md`

****

## Project.Surfaces

- `Project.Surfaces` is a built-in `Ontology.Namespace` for the surfaces the index covers
- see `002-surfaces.md`

****

## Stable.Surface

- `Stable.Surface` is a durable, authoritative surface where a specific facet of project knowledge lives
- see `100-index.md`

****

## Natural.Placement

- `Natural.Placement` is the principle that each surface holds the facet of a concept that is natural to its function
- see `100-index.md`

****

## Index.Concept.Coverage

- the index is the collection point for all `Named.Concepts` in the project's stable surfaces
- see `100-index.md`

****

## Kernel.Block:Index

- `Kernel.Block:Index` is `Kernel.Block` in `notes/index/` — the loadable unit of meaning in the index
- aliases: `Index.Block`, `Global.Block`
- see `100-index.md`

****

## Kernel.Block:Appendix

- `Kernel.Block:Appendix` is `Kernel.Block` in `notes/appendix/` — extended concept material
- aliases: `Appendix.Block`
- see `100-index.md`

****

## Kernel.Block:Design.Session

- `Kernel.Block:Design.Session` is `Kernel.Block` in session artifacts — session-local concept capture
- aliases: `Design.Session.Block`, `Design.Index.Block`
- see `100-index.md`

****

## Forward.Alignment

- `Forward.Alignment` is moving the design point to a new place in the `Conceptual.Space`
- see `101-index.md`

****

## Internal.Alignment

- `Internal.Alignment` is keeping all surfaces in sync at the current design state
- see `101-index.md`

****

## Hugentic.Alignment

- `Hugentic.Alignment` is bringing human and agent to shared understanding in the `Conceptual.Space`
- see `101-index.md`

****

## Agentos.Soft.Subsystem

- `Agentos.Soft.Subsystem` is a conceptual responsibility area, not a hard ownership container
- a more or less defined set of concepts that interact together with a clear responsibility
- components can participate in multiple soft subsystems
- component lists are orientation surfaces, not ownership manifests
- examples: Hugentic Workflows, the Index system, the Canvas system

****

## Hugentic.Concept

- `Hugentic` is a foundational qualifier: a system, surface, workflow, or tool designed for the human-agentic interface
- the test: a hugentic thing meaningfully changes both sides — how the human works and how the agent works
- if it only changes one side, it's a human tool or an agent tool, not hugentic

****

## Hard.Evidence

- `Hard.Evidence` is the principle that evidence-based arguments have priority over agent assumptions during alignment work
- see `102-index.md`

****

## Alignment.Session

- `Alignment.Session` is a shallow container for the general concepts that compose an alignment session
- see `102-index.md`

****

## What.Design.Session

- `What.Design.Session` is a scoped human-agent convergence surface for design work — the `What.Design` specialization of `Alignment.Session`
- see `101-index.md`

****

## Alignment.Loop

- `Alignment.Loop` is the general workflow machinery for human-agent convergence: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`
- see `102-index.md`

****

## Alignment.Backend:InChat:What

- `Alignment.Backend:InChat:What` is the default `What.Design.Session` backend — state lives in chat
- see `101-index.md`

****

## Alignment.Backend:Artifact:What

- `Alignment.Backend:Artifact:What` is the file-backed `What.Design.Session` backend — state lives in a `Live.Note`
- see `101-index.md`

****

## Impl.Req

- `Impl.Req` is an implementation-request artifact — a surface for designing and tracking an implementation plan
- see `102-index.md`

****

## Vertical.Slice

- `Vertical.Slice` is the preferred shape of implementation work — thin end-to-end changes
- see `102-index.md`

****

## No.Legacy.Allowed

- `No.Legacy.Allowed` is an implementation constraint: do not leave stale state behind
- see `102-index.md`

****

## Test.At.Boundaries

- `Test.At.Boundaries` is the testing guidance: test through public interfaces, not implementation details
- see `102-index.md`

****

## Deep.Modules

- `Deep.Modules` is an architectural principle: small interface, hidden complexity
- see `102-index.md`

****

## Agent.Navigable.Codebase

- `Agent.Navigable.Codebase` is the structural principle that code should be organized so agents can explore naturally
- see `102-index.md`

****

## Design.Target.Model

- `Design.Target.Model` is the current explicit design model of a system — distributed across surfaces, with the index as discovery layer
- see `102-index.md`

****

## Current.Implementation

- `Current.Implementation` is the current realized state of a system
- see `102-index.md`

****

## Progress.Gradient

- `Progress.Gradient` is the combined direction of `Forward.Alignment` + `Internal.Alignment` at any point
- see `102-index.md`

****

## Design.Implementation.CoEvolution

- `Design.Implementation.CoEvolution` is the development rhythm of `Forward.Alignment` then `Internal.Alignment`, co-developing design and implementation surfaces
- see `102-index.md`

****

## Kernel.Writing

- `Kernel.Writing` is a writing philosophy for capturing concepts directly and completely
- see `102-index.md`

****

## Kernel.Block

- `Kernel.Block` is the base writing object of `Kernel.Writing` — fundamentals + `### appendix` + `### meta`
- all block types are parameterizations: `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design.Session`
- see `102-index.md`
