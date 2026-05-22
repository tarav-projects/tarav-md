> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

## Index.Architecture

- `Index.Architecture` is the structural design of the Agentos Index system — an `Explicit.Namespace` grouping the concepts that define it
- two scopes: `Global.Index.Scope` (`index/`, lean, always loaded) and `Extended.Index.Scope` (`appendix/`, loaded on demand)
- flat anonymous index files (`100-index.md`, `101-index.md`, ...) with `000-index.md` as concept→file routing table
- writing is append-only to the last file — placement decisions are decoupled from writing
- one universal block structure (`Kernel.Block`) parameterized by surface: `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design`
- one writing philosophy (`Kernel.Writing`) — space constraints come from the surface, not the philosophy
- appendix files are concept-named (`Concept.Name-appendix.md`) with implicit discovery — no outlink required
- `Concept.Scoping` and `Explicit.Namespaces` provide the conceptual overlay on the flat file structure

### meta

- namespace-members: `Global.Index.Scope`, `Extended.Index.Scope`, `Flat.Index.Architecture`, `Kernel.Writing`, `Kernel.Block`, `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design`, `Concept.Scoping`, `Explicit.Namespace`, `Surface.Concept`, `Agentos.Index.System`

****

## Flat.Index.Architecture

- `Flat.Index.Architecture` is the file-level design of the index: anonymous flat containers instead of semantic groupings
- index concept files are `100-index.md`, `101-index.md`, ... — file names carry no semantic meaning
- ~20 concept blocks per file — hard cap
- writing always appends to the last file — zero placement decisions, all focus on writing a great block
- splitting overfull files is maintenance, not a writing concern
- `000-index.md` is the concept→file routing table — always loaded by agents
- organizing happens through `Concept.Scoping` and `Explicit.Namespaces`, not file groupings

****

## Global.Index.Scope

- `Global.Index.Scope` is the always-loaded layer of the index — `index/`
- every concept has one `Kernel.Block:Index` here — the minimum context an agent needs to reason about it
- defines the starting point for the discovery cascade

****

## Extended.Index.Scope

- `Extended.Index.Scope` is the on-demand layer of the index — `appendix/`
- loaded when an agent needs depth beyond what the global scope provides
- loading an appendix is an intentional action — the agent displays intention by choosing to go deeper
- where hidden blocks live — discoverable through the cascade, never loaded by default

****

## Surface.Concept

- `Surface.Concept` is the base idea behind all surfaces in the system — an interface over a subset of a project
- naming something a surface is an implicit contract: it declares what the consumer can expect from that layer
- `Stable.Surface` — the elements that aim to be durable and authoritative
- `Public.Surface` — the elements visible and portable beyond the project
- `Md.Surface` — the markdown layer
- different surfaces can overlap — the same file can participate in multiple surfaces
- a surface is not a folder or a file type — it's a declared interface over project elements

****

## Concept.Scoping

- `Concept.Scoping` is the general mechanism: any concept can scope other concepts through its appendix file
- an appendix file can contain blocks for other concepts, viewed through the host concept's lens
- a concept can appear in multiple scopes — each scoped block should be read in the context of the container concept
- notation: `Concept.B/Concept.A` — Concept.A as seen from Concept.B's scope
- examples: `Index.Architecture/Flat.File.Design`, `Index.Architecture/Meta.Unification`

****

## Explicit.Namespace

- `Explicit.Namespace` is a concept that intentionally organizes a view over a set of related concepts
- the mechanics are `Concept.Scoping` — the difference is intent: this concept declares itself as a namespace
- namespace membership is declared in the namespace's global block under `### meta` as a `namespace-members` list
- the global block is the universal minimum; a namespace appendix block is a scoped view for people digging into that area
- examples: `Index.Architecture`, `Agentos.Index.System`

****

## Agentos.Index.System

- `Agentos.Index.System` is the top concept for the index — a `Soft.Programming.Language` for project knowledge
- a library of micro-prompts invoked by naming — mentioning a `Dotted.Name` triggers a concept-level context load
- manipulates the agent's context window — by controlling what enters context, you control how the agent reasons
- enables semantic computation: composing concepts, finding contradictions, detecting design weakness
- `Agentos.Index.System` is an `Explicit.Namespace` — groups the concepts that compose the index system

### meta

- aliases: `Agentos.Index`

****

## Soft.Semantics.Concept

- `Soft.Semantics.Concept` is the principle that concepts in the system are intentionally under-specified because the consumer (an LLM) has common sense
- you don't need to close every obvious gap — the LLM fills them reliably enough
- this is a feature, not a deficiency — precision costs space and maintenance, common sense is free — trust the LLM
- the entire index is built on `Soft.Semantics.Concept` — it's what makes a `Soft.Programming.Language` possible
- when a concept feels incomplete, ask: would an LLM figure this out? If yes, it's complete enough

****

## Hugentic.Concept

- `Hugentic` is a foundational qualifier: a system, surface, workflow, or tool designed for the human-agentic interface
- the test: a hugentic thing meaningfully changes both sides — how the human works and how the agent works
- if it only changes one side, it's a human tool or an agent tool, not hugentic

****

## Index.Router

- `Index.Router` is the compressed entry point of the index — always loaded, always first
- two instances: `000-index.md` (public, in the `Project.Index.Skill`) and `001-index.md` (local, in `notes/index/`)
- two routing sections: concept routing (every `Dotted.Name` → flat file) and file routing (important project files for research)
- entries can have a one sentence explanation — but depth lives in the blocks themselves

****

## Inline.Relatedness

- `Inline.Relatedness` is the writing discipline of naturally blending related `Dotted.Name` concepts into concept text
- the goal is not to create explicit related-edge metadata
- when a related concept is already part of the sentence meaning, use its `Dotted.Name`
- use `Concept.Cite` only when a materially important relationship should be visible but does not fit naturally into the sentence
- enriches the index by making concept relationships discoverable inside ordinary writing

****

## Project.Surfaces

- `Project.Surfaces` is a `BuiltIn.Namespace` — an expected interface in every project's ontology
- can be empty — populated as surfaces are identified
- custom surfaces are formally exposed as scoped blocks: `Project.Surfaces/Surface.X`

****

## Project.Dev.Install

- `Project.Dev.Install` is a way to make an Agentos project fully available to agents working across projects
- all surfaces of the installed project become reachable — not just its `Public.Surface`
- enables agents to work on multiple projects with full context
- not yet defined — the mechanism is open

****

## Index.Runtime

- `Index.Runtime` is the behavioral program installed in an agent at `Index.Activation` — how to operate the index
- covers: architecture, reading, writing, research, gaps, detection, footer
- once loaded, the agent knows how to navigate, interpret, contribute to, and reason with the index
- the runtime is the skill instructions — it's behavioral, not data
- `Index.Notes` are the data the runtime operates on
- operational detail: `references/launch-runtime.md`

****

## Distributed.Index

- `Distributed.Index` is the architecture where the index spans multiple surfaces
- public index: `skills/<project>-index/index/` — the canonical public surface, other skills assume it exists
- local index: `notes/index/` — project-local concepts
- two routing tables: `000-index.md` (public, in skill) and `001-index.md` (local, in `notes/index/`)
- numbering ranges: `100-299` public flat files, `300-499` local flat files
- a fresh agent from another project loads only `000-index.md` — sees public concepts
- a local agent loads both — sees everything
- the same `Kernel.Block:Index` format, same routing, same scoping — just distributed

****

## Soft.Programming.Language

- `Soft.Programming.Language` is a language with soft syntax (natural language) and programming semantics (execution behavior)
- the Agentos Index is a `Soft.Programming.Language` — the mapping:
    - variable declaration → `Dotted.Notation`
    - symbol table → `000-index.md` routing table
    - module → `Index.Note`
    - function body → `Index.Block`
    - type system → `Index.Block.Syntax`
    - import → loading blocks into agent context
    - undefined variable → `Unresolved.Index.Name`
    - compilation → maintenance passes
    - runtime → the conversation itself
