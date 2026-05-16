## Index.Architecture

- `Index.Architecture` is the structural design of the Agentos Index system — an `Explicit.Namespace` grouping the concepts that define it
- two scopes: `Global.Index.Scope` (`notes/index/`, lean, always loaded) and `Extended.Index.Scope` (`notes/appendix/`, loaded on demand)
- flat anonymous index files (`100-index.md`, `101-index.md`, ...) with `000-index.md` as concept→file routing table
- writing is append-only to the last file — placement decisions are decoupled from writing
- one universal block structure (`Kernel.Block`) parameterized by surface: `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design.Session`
- one writing philosophy (`Kernel.Writing`) — space constraints come from the surface, not the philosophy
- appendix files are concept-named (`Concept.Name-appendix.md`) with implicit discovery — no outlink required
- `Concept.Scoping` and `Explicit.Namespaces` provide the conceptual overlay on the flat file structure

### meta

- namespace-members: `Global.Index.Scope`, `Extended.Index.Scope`, `Flat.Index.Architecture`, `Kernel.Writing`, `Kernel.Block`, `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design.Session`, `Concept.Scoping`, `Explicit.Namespace`, `Surface.Concept`, `Agentos.Index.System`

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

- `Global.Index.Scope` is the always-loaded layer of the index — `notes/index/`
- every concept has one `Kernel.Block:Index` here — the minimum context an agent needs to reason about it

****

## Extended.Index.Scope

- `Extended.Index.Scope` is the on-demand layer of the index — `notes/appendix/`
- loaded when an agent needs depth beyond what the global scope provides
- loading an appendix is an intentional action — the agent displays intention by choosing to go deeper

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
