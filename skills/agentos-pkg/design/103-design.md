> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Index.Chapter

- `Index.Chapter` is a folder of the Index that groups concepts into a unit of selective loading
- concepts across chapters are peers, reached by one `Dotted.Name` lookup — a chapter sets only what loads together
- the chapter loading policy is open — if any default holds, only the default chapter is loaded/searched
- the default chapter is `design`; `impl` is reserved; a package may add any number beyond these
- a chapter's files are named `NNN-<chapter>.md`, e.g. `design/100-design.md` — the suffix names the chapter

****

## Index.Appendix

- `Index.Appendix` is the appendix layer of the Index and the root concept for it — the on-demand depth, complement of `Index.Main`
- it is the index-level echo of `Kernel.Block.Appendix`: depth deferred out of the compressed front, loaded by choice
- it is not routed — reached by naming through `Appendix.Discovery`, never loaded by default
- loading an appendix is an intentional action — the agent displays intention by choosing to go deeper
- it lives in one `appendix/` shared across chapters; files are concept-named and addressed as `Appendix.Pages`
- it holds every concept's tail (`Block.Line.Gradient`): `Concept.X/Appendix` catch-alls and scoped `Concept.X/Concept.Y` blocks (`Appendix.Block`)
- with `Index.Main` and `Index.Router` it composes the `Index.Surface`

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

## Surface.Types

- `Surface.Types` are the major axes of surface character in an Agentos project
- a component of the system can have expressions on different surface types — each type serves a different aspect of the component
- **Codebase** — executable implementation. The running system.
- **Index/Appendix** — named concepts, design reasoning, cheap navigation. Where agents and humans go to reason about the system. Aims to contain or cheaply link all components. Not derived from other surfaces.
- **Skills** — agent-executable guidance. The "codebase" for agents. Can contain index-ish components (routers), doc-ish components (references), or operational components — depends on the implementation.
- **Docs.Surface** — natural text, readable, linked. General and flexible — can serve presentation, explanation, onboarding, or any purpose that fits natural prose. Can be a derived surface. Its interaction with other surfaces follows `Natural.Placement` and `Cited.Duplication` like any other stable surface.
- **Chat.Surface** — recorded user/agent communication. The interaction trail. Emit-driven and append-only (unlike the curated stable surfaces). Holds the evidence of alignment moves; other surfaces hold curated forms derived from it.
- surface types are not file locations — a single folder can contain multiple types
- all stable surfaces are peers (`Stable.Surface`) — no type outranks another by default
- the distinction is the access pattern and the purpose, not the authority level
- the footprint of a component across surface types is proportional to its complexity and usage — not every component needs every surface type
- a concept that exists only as design communication may only need an index block
- a major subsystem may have index, codebase, skill, and docs surfaces
- an agent orchestration across subsystems may need index and skill surfaces but no codebase
- this follows `Natural.Placement` — each surface type holds the facet that is natural to its function
- components are deployed on different surfaces as they fit — the surfaces serve the component, not the other way around

****

## Block.Path

- `Block.Path` is a block name written as a `/`-separated path — the full path is the name
- the root segment is a `Dotted.Name`, a top-level index concept; the path anchors on that node
- later segments may be `Dotted.Name` concepts or free labels; an author composes any path that organizes the block
- a concept segment carries `Concept.Scoping` semantics; a label segment just groups, claiming no ontology entry
- a path-named block is attached to its root and lives in the root's appendix by default — it is not itself a top-level index block
- section paths (`Concept.X/Appendix`, `Concept.X/Grounding`) are restricted to the appendix; a scoped concept-child defaults there but may be promoted

****

## Explicit.Namespace

- `Explicit.Namespace` is a concept whose purpose is to group a cluster of blocks — a declared view over the concepts it gathers
- its members are listed in `### meta` under `namespace-members` — the inventory of the cluster
- a member is either a grouped peer (a routed `Index.Block` standing on its own) or an owned child in the namespace's appendix
- the member list is where appendix-depth members surface — path-children the `Index.Router` never routes, otherwise reachable only by `Appendix.Discovery`, are named here
- the appendix is required — it is the namespace's home, holding the owned children and the guided view over the cluster
- example: `Agentos.Index.System`

****

## Agentos.Index.System

- `Agentos.Index.System` is the Agentos Index taken as a whole — the operable system of named concepts agents reason with
- it is a curated `User.Touched` surface — it indexes the `Touched.Space` of the project's other surfaces, the `Chat.Surface` foremost
- it is a `Hugentic.Concept` surface — user and agent collaborate over it: the agent constructs, the user gates
- it enables semantic computation over those concepts: composing them, finding contradictions, detecting design weakness

### meta

- aliases: `Agentos.Index`
- namespace-members: `./Index.Surface.Layout`, `Index.Surface`, `Index.Router`, `Index.Main`, `Index.Chapter`, `Index.Appendix`, `Index.Depot`, `Index.Discovery`, `Kernel.Writing`, `Kernel.Block`, `Kernel.Block.Section`, `Kernel.Block.Fundamentals`, `Kernel.Block.Grounding`, `Kernel.Block.Appendix`, `Kernel.Block.Meta`, `Kernel.Note`, `Index.Block`, `Appendix.Block`, `Design.Block`, `Block.Path`, `Explicit.Namespace`, `Surface.Concept`

****

## Spec.Hardness

- `Spec.Hardness` is how much of an interpreted artifact is specified vs left to its interpreter to complete
- it is set by the interpreter's intelligence — a dumber interpreter needs harder (more specified) artifacts; a smarter interpreter allows softer ones
- it is a soft↔hard axis: hard is fully specified, soft leans on the interpreter's judgment
- placement is a design choice — too hard over-specifies (cost, rigidity); too soft costs reliability
- it applies to anything handed to an interpreter — behavior, meaning, instructions, plans

****

## Concept.Hardness

- `Concept.Hardness` applies `Spec.Hardness` to meaning — how much a concept's definition is fixed vs left to the interpreter to complete
- the index runs its concepts soft: definitions are intentionally under-specified, completed by the LLM's common sense
- soft is a feature, not a deficiency — precision costs space and maintenance; common sense is free
- the writing heuristic: close gaps only to the point where an LLM would reliably figure out the rest
- soft concepts are what make the index a `Soft.Programming.Language`

****

## Hugentic.Concept

- `Hugentic` is a foundational qualifier: a system, surface, workflow, or tool designed for the human-agentic interface
- the test: a hugentic thing meaningfully changes both sides — how the human works and how the agent works
- if it only changes one side, it's a human tool or an agent tool, not hugentic

****

## Index.Router

- `Index.Router` is the lookup table of the Index — `000-INDEX.md`, loaded first when the Index enters context (per the `Package.Driver`)
- it routes concept name → file, sectioned by `Index.Chapter`
- the appendix is not routed — appendix depth is reached by naming (`Appendix.Discovery`), not listed here
- it also carries file routing (`Project.File.Index`) — important project files for research
- entries may carry a one-sentence hint, but depth lives in the blocks themselves
- the routers of the engaged `Index.Depot`s compose into one working Index (`Index.Discovery`)

****

## Inline.Relatedness

- `Inline.Relatedness` is the writing discipline of naturally blending related `Dotted.Name` concepts into concept text
- the goal is not to create explicit related-edge metadata
- when a related concept is already part of the sentence meaning, use its `Dotted.Name`
- use `Concept.Cite` only when a materially important relationship should be visible but does not fit naturally into the sentence
- enriches the index by making concept relationships discoverable inside ordinary writing

****

## File.Mention

- `File.Mention` is the inline token for referencing a file from a block, written `@<path-hint>`
- it is a neutral relation — it brings the file into the block's context, it does not make the block about the file
- it is the file peer of `Inline.Relatedness` and `Concept.Cite`: blocks mention concepts by `Dotted.Name`, files by `@<path-hint>`
- the `@<path-hint>` is a hint, not a contract — the agent resolves it by searching, starting from the project
- resolution is opportunistic, like registry lookup for a `Dotted.Name` — check it when the exact file matters

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
