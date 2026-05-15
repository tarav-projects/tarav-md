## Index.Architecture

- `Index.Architecture` is the structural design of the Agentos Index system — also an `Ontology.Namespace` grouping the concepts that define it
- two scopes: `Global.Index.Scope` (`notes/index/`, lean, always loaded) and `Extended.Index.Scope` (`notes/appendix/`, loaded on demand)
- flat anonymous index files (`100-index.md`, `101-index.md`, ...) with `000-index.md` as concept→file routing table
- writing is append-only to the last file — placement decisions are decoupled from writing
- one universal block structure (`Kernel.Block`) parameterized by surface: `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design.Session`
- one writing philosophy (`Kernel.Writing`) — space constraints come from the surface, not the philosophy
- appendix files are concept-named (`Concept.Name-appendix.md`) with implicit discovery — no outlink required
- `Ontology.Registry` and `Ontology.Namespaces` provide the conceptual overlay on the flat file structure

### meta

- namespace members: `Global.Index.Scope`, `Extended.Index.Scope`, `Flat.Index.Architecture`, `Kernel.Writing`, `Kernel.Block`, `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design.Session`, `Ontology.Registry`, `Ontology.Namespace`

****

## Flat.Index.Architecture

- `Flat.Index.Architecture` is the file-level design of the index: anonymous flat containers instead of semantic groupings
- index concept files are `100-index.md`, `101-index.md`, ... — file names carry no semantic meaning
- ~20 concept blocks per file — hard cap
- writing always appends to the last file — zero placement decisions, all focus on writing a great block
- splitting overfull files is maintenance, not a writing concern
- `000-index.md` is the concept→file routing table — always loaded by agents
- organizing happens through `Ontology.Namespaces`, not file groupings

****

## Global.Index.Scope

- `Global.Index.Scope` is the always-loaded layer of the index — `notes/index/`
- every concept has one `Kernel.Block:Index` here — the minimum context an agent needs to reason about it

****

## Extended.Index.Scope

- `Extended.Index.Scope` is the on-demand layer of the index — `notes/appendix/`
- loaded when an agent needs depth beyond what the global scope provides
