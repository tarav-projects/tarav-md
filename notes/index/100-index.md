## Stable.Surface

- `Stable.Surface` is a durable, authoritative surface where a specific facet of project knowledge lives
- the "stable" contract: the content aims to be maintained, current, and trustworthy
- all `Stable.Surfaces` have equal authority — no surface is positioned as more important than another
- misalignments between surfaces are resolved context-dependently, not by a fixed hierarchy
- drift between stable surfaces is the target of `Internal.Alignment` — a problem to detect and resolve

****

## Stable.Md.Surface

- `Stable.Md.Surface` is the markdown subset of `Stable.Surfaces`
- the set of `.md` stable surfaces in a project: index notes, docs, skills, AGENTS.md, and similar

****

## Natural.Placement

- `Natural.Placement` is the principle that each surface holds the facet of a concept that is natural to its function
- the full description of a concept is distributed across surfaces — each complements the others
    - index → conceptual grounding (what it is, why, how it connects) and discovery (where to find it)
    - appendix → extended depth, rationale, scoped views through `Concept.Scoping`
    - skills → operational behavior, workflows
    - code → the implementation itself (the code IS the description)
- each surface should mostly contain what the other surfaces don't
- a well-maintained system has no drift between surfaces AND has content balanced by the nature of each surface
- content that feels unnatural in a surface is probably misplaced
- the anti-pattern is duplication across surfaces — the pattern is complementary coverage
- minimal duplication is allowed when a surface needs self-sufficiency — e.g. a skill repeating just enough context to be usable without loading the index

****

## Placement.Balance

- `Placement.Balance` is the equilibrium state of content across surfaces
- the system is balanced when moving content from one surface to another would feel less natural than its current placement
- diagnostic signal: if you find yourself needing the same content in two different surfaces and linking is not possible, the system is unbalanced
- complementary to `Natural.Placement` — natural placement is the principle, placement balance is the resulting state

****

## Surface.Link.Directionality

- `Surface.Link.Directionality` defines which surfaces can reference which
- `Local.Surface` can reference `Public.Surface` — not the reverse
- `Public.Surface` must be self-contained — it cannot depend on local project knowledge
- `Local.Surface` has access to everything — it bridges public and local naturally
- this constraint exists because public surfaces are distributable — they must work outside the project
- when the full dependency project is available (`Project.Dev.Install`), the local/public boundary shifts — local surfaces of the dependency become reachable too

****

## Agentos.Index.Notes

- `Agentos.Index.Notes` is one of the `Stable.Surfaces` of an Agentos-style project — the `notes/index/*.md` files
- implements the `Agentos.Index` — a `Soft.Programming.Language` for project knowledge
- four roles: conceptual implementation of the system, discovery and navigation index, development surface, main alignment surface
- contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in flat index files, registered in the `Ontology.Registry`
- agents execute the index at runtime through the `Index.Eval.Loop` — resolving names, loading blocks, detecting gaps

****

## Index.Concept.Coverage

- `Index.Concept.Coverage` is the goal that the index covers all `Named.Concepts` in the project
- any `Dotted.Name` that appears in a stable surface should have an index entry
- concepts can emerge anywhere — authors use `Dotted.Notation` naturally without worrying about index maintenance
- the system detects new `Named.Concepts` and triggers index updates separately

****

## Kernel.Block:Index

- `Kernel.Block:Index` is `Kernel.Block` placed in `notes/index/` — the loadable unit of meaning in the index
- anchored by a heading (H2–H6) that names the concept using `Dotted.Notation`
- `Kernel.Writing` at tight space constraints — conceptual completeness under compression
- must carry enough signal for an agent to reason correctly about the concept
- the index must have at least a block for any meaningful concept in the system
    - blocks can link out to other surfaces rather than define everything inline
- inherits fundamentals + `### appendix` + `### meta` from `Kernel.Block`
- index blocks should NOT become transcripts, changelogs, progress dashboards, task lists, or implementation dumps

### meta

- aliases: `Index.Block`, `Global.Block`

****

## Kernel.Block:Appendix

- `Kernel.Block:Appendix` is `Kernel.Block` placed in `notes/appendix/` — extended material for a concept
- `Kernel.Writing` at relaxed space constraints — depth over compression
- extended material: examples, use cases, reasoning, pros/cons, design depth
- a `Stable.Surface` — maintained, not throwaway
- not part of `Context.Minimal.Surface` — agents reach it only on explicit need
- discovery is implicit — agents check if `notes/appendix/Concept.Name-appendix.md` exists

### meta

- aliases: `Appendix.Block`

****

## Kernel.Block:Design.Session

- `Kernel.Block:Design.Session` is `Kernel.Block` used in `Design.Session` artifacts — session-local concept capture
- captures the relevant conceptual value produced by session discussion about a subject concept
- fundamentals have the same semantic role as `Kernel.Block:Index` fundamentals
    - draft quality may vary during the session, but the meaning target is the same
- `### appendix` carries extended conceptual value: examples, rationale, pressure tests, tradeoffs, rejected alternatives
- `### meta` covers session mechanics: status, sources, open questions, promotion notes
- at promotion time: fundamentals compress into `Kernel.Block:Index`, appendix material goes to `Kernel.Block:Appendix`, meta is dropped

### meta

- aliases: `Design.Session.Block`, `Design.Index.Block`

****

## Md.Surface

- `Md.Surface` is the markdown layer of a project — the set of `.md` files
- parameterized to scope: `Md.Surface:Agentos`, `Md.Surface:Agentos.Stack`

****

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- a dotted name is a signal that the phrase refers to a concept, not casual prose
- every name has at least two parts; dot depth is flexible and natural to the concept
- dots provide context but are not a strict hierarchy — definition and relationships live in notes and registry entries, not the name
- `Explicit.Namespace` must be explicit; do not infer a namespace from a dotted prefix alone
- a dotted name can appear before it is registered
    - agents infer concept maturity from the repository: prose-only, registry entry, or dedicated note
- registry lookup is opportunistic, not mandatory — use it when concept identity matters, avoid turning ordinary work into ontology maintenance

****

## Dotted.Parameterized.Notation

- `Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept
- form: `Concept.Name:Target`
- the part before the colon is the concept, the part after is the parameter
- colon parameters may themselves use dots
- parameterized references are instances of the same concept, not different concepts
    - use a new dotted name when the meaning changes
    - use a colon parameter when the same concept is applied to a different target
- examples: `Maintenance.System:Agentos`, `Md.Surface:Agentos.Stack`, `Project.CLI:Agentos`

****

## File.Numbering.Protocol

- `File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces
- numeric prefixes are stable handles — the title may change, but the prefix should not be renumbered
- canonical prefixes use three digits; allocation is append-only; gaps are allowed; do not renumber or fill gaps if unnecessary

### Current Agentos range model

- `000-099`: reserved files with fixed system roles
- `100-499`: rolling index and appendix notes
- `500-999`: rolling other files (live notes, live scripts)

### CLI support

- `agentos stdlib prefix` provides deterministic allocation
- desired direction: project-wide duplicate detection, range validation, append-only enforcement

****

## Maintenance.System

- `Maintenance.System` defines how a project surface is diagnosed over time
- diagnosis-first, not fix-first — report issues with evidence, then the user decides
- parameterized: `Maintenance.System:Agentos` is the Agentos instance
- reports must be evidence-based — suggestions without evidence must be marked as such

****

## Agentos.Project

- `Agentos.Project` is a concrete project that adopts the `Agentos.Stack` model
- exists when the project root contains `.agentos/project.json` — the `Agentos.Project.Marker`
    - `.agentos/config.json`, `.agentos/AGENTS.md`, skill depots, `.agents/`, `.claude/` do not define project existence
- `.agentos/AGENTS.md` is the project-local natural-language instruction surface — human-writable, loadable by skills
- naming boundary: `Agentos.Project` means a project that adopts Agentos, not the Agentos implementation itself
    - `Agentos.Project:agentos-py` = agentos-py as an adopting project
    - `Agentos.Implementation:agentos-py` = agentos-py as part of the Agentos implementation
    - the same repo can be both under different reference frames

****

## Agentos.AGENTS.md

- `Agentos.AGENTS.md` is the project-local natural-language instruction surface at `.agentos/AGENTS.md`
- human-writable — contains project-specific guidance for Agentos workflows and skills
- skills may load it when they need custom local instructions or interpretation guidance
- does not define project identity — the marker remains `.agentos/project.json`
