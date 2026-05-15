# Index System Revisit - design-session

## Session.Abstract

- intent: full revisit of the Agentos Index system — review all major elements, double-check design decisions, align and enrich
- active focus: skill map agreed, per-item protocol defined, ready to start Layer 1
- references: notes/index/ (agentos-md), index-related skills
- state: active
- next: item 7 — Index.Note / Index.Ontology.Note

## Design.Index

### Agentos.Index

- a `Soft.Programming.Language` for project knowledge
- a library of micro-prompts invoked by naming
- manipulates the agent's context window — by controlling what enters context, you control how the agent reasons
- the agent is a CPU processing context; the index is one of five context manipulation channels
- enables semantic computation: composing concepts, finding contradictions, detecting design weakness

#### appendix

- five context manipulation channels (most-static to most-dynamic): agent harness, AGENTS.md, skills, index, chat
- SPL framing: the agent-as-CPU processes context; the index structures that context into loadable, composable, relationally connected units
- semantic computation: once concepts are loaded, the agent computes with them — not just recall but composition, contradiction detection, gap analysis, implication testing
- micro-skills analogy: a Dotted.Name mention triggers a concept-level context load, similar to how a skill trigger loads operational behavior but at concept granularity

#### meta

- status: reviewed — confirmed, enrichment identified
- needs its own Ontology.Namespace in 001-ontology.md (currently only appears as qualifier inside Agentos.Index.Notes)
- needs standalone concept block in the index (separate from Agentos.Index.Notes)

### Agentos.Index.Notes

- the implementation surface of the `Agentos.Index` — the `notes/index/*.md` files
- one of the `Stable.Surfaces` of the project (not a special subsystem — a peer surface alongside code, skills, docs)
- four roles:
    - conceptual implementation of the system — where the system's design is realized in concept form
    - discovery and navigation index — useful for finding things across the project
    - development surface — one of the surfaces where the project is actively developed
    - main alignment surface — the primary place where human and agent converge on meaning
- enables the transition from co-development to autonomous implementation: human and agent co-develop concepts in the index, then the agent implements under those semantics and constraints

#### appendix

- the relationship between Agentos.Index and Agentos.Index.Notes is concept vs implementation — same as a design pattern vs its concrete realization
- "Notes" in the name correctly signals it's the markdown realization of the index concept
- the current 114 wording "durable concept-note subsystem" should be revised to reflect the Stable.Surface framing

#### meta

- status: reviewed — confirmed, wording correction identified
- current 114 wording needs revision: "durable concept-note subsystem" → Stable.Surface framing
- "main alignment surface" role is an enrichment over current source material

### Kernel.Writing

- a writing philosophy for capturing concepts directly and completely
- each line aims to describe a fundamental dimension of the concept — the view is multi-faceted
- lines aim to be orthogonal — avoid redundancy, prefer independent facts
- language is direct — prefer concise expression, avoid superfluous words
- completeness over clarity — every fundamental dimension has at least evidence in the block, even if not fully explained
- coverage over compression — losing a fundamental dimension is more costly than an extra line
- a `Kernel.Block` positions a concept in the `Conceptual.Space` — an agent reading it can reconstruct the full context
- space constraints are external — the surface determines the budget, not the philosophy
- `Kernel.Block` is the writing object that embodies `Kernel.Writing`

### Kernel.Block

- the base writing object of `Kernel.Writing`
- structure: fundamentals (conceptual) + `### appendix` (extended conceptual) + `### meta` (non-conceptual)
- the dividing rule: fundamentals and appendix are about the concept; meta is about the block itself
- meta covers: outlinks, findability, status, open questions, session mechanics — anything non-conceptual
- all block types in the system are parameterizations of `Kernel.Block` placed in specific surfaces with specific constraints

#### appendix

- replaces `Complete.Index.Block` — the appendix + meta structure is now part of the base, not an extension
- absorbs `### index` (findability) and `### outlinks` (surface links) into `### meta`
- block zoo after simplification:
    - `Index.Block` — `Kernel.Block` in `notes/index/`, tight space constraints
    - `Index.Appendix.Block` — appendix-only fragment in `notes/appendix/`, paired with an Index.Block
    - `Design.Index.Block` — session-local `Kernel.Block` in a design artifact
- removed: `Complete.Index.Block` — redundant now that Kernel.Block includes appendix + meta

#### meta

- status: new concept — emerged from item 3 (Index.Block) review
- extracted from writing principles previously conflated with Index.Block
- Index.Block, Index.Appendix.Block, Design.Index.Block are parameterizations of Kernel.Block

### Index.Block

- `Kernel.Block` placed in `Agentos.Index.Notes` — the loadable unit of meaning in the index
- anchored by a heading that names the concept using `Dotted.Notation`
- `Kernel.Writing` at tight space constraints — conceptual completeness under compression
- must carry enough signal for an agent to reason correctly about the concept
- inherits fundamentals + `### appendix` + `### meta` from `Kernel.Block`

#### meta

- status: reviewed — design change: redefined as Kernel.Block parameterization
- `### index` and `### outlinks` absorbed into `### meta`
- `Complete.Index.Block` removed — Kernel.Block already includes appendix + meta
- 114 needs revision to reference Kernel.Writing and Kernel.Block

## Session.Notes

### Per-Item Protocol

For each skill map item:

1. **Test** — agent asks 1-2 questions about the concept (minimum: "name one feature"; preferred: design-judgment question about relationships or purpose)
2. **Align** — agent confirms or corrects against the actual source material, grounding the user in the current system
3. **React** — user decides: confirm, explore, request changes, or flag for later redesign
4. **Capture** — light by default (check + note); full Design.Index.Block only when a design decision changes or enrichment is identified

### Skill Map — Traversal Tracker

#### Layer 1 — Identity & Foundation
- [x] 1. Agentos.Index — what the index IS (SPL concept) — confirmed + enrichment: needs own namespace and block; micro-prompts fundamental; appendix: SPL framing, five channels, semantic computation
- [x] 2. Agentos.Index.Notes — Stable.Surface, implementation of the index (`114`) — wording correction: not "subsystem" but peer Stable.Surface; four roles identified; main alignment surface enrichment
- [x] 3. Index.Block — fundamental semantic unit (`114`) — design change: extracted Kernel.Writing as base writing philosophy; Index.Block redefined as Kernel.Block + index space constraints; new concepts: Kernel.Writing, Kernel.Block

#### Layer 2 — Naming & Addressing
- [x] 4. Dotted.Notation (`116`) — confirmed as-is
- [x] 5. Dotted.Parameterized.Notation (`116`) — confirmed as-is
- [x] 6. File.Numbering.Protocol (`117`) — confirmed as-is

#### Layer 3 — Structure & Organization
- [ ] 7. Index.Note / Index.Ontology.Note (`000`, `001`)
- [ ] 8. Ontology.Namespaces
- [ ] 9. Project.Surfaces (`002`)
- [ ] 10. Block types — Complete, Appendix, Design (`114`)

#### Layer 4 — Surface Model
- [ ] 11. Stable.Surface / Natural.Placement / Placement.Balance (`100`)
- [ ] 12. Md.Surface (`115`)
- [ ] 13. Surface.Link.Directionality (`100`)

#### Layer 5 — Writing & Maintenance
- [ ] 14. Index.Writing.Principles / Index.Concept.Coverage (`114`)
- [ ] 15. Index.Block.Outlinks (`114`)
- [ ] 16. Maintenance.System (`118`)

#### Layer 6 — Runtime (skills)
- [ ] 17. agentos-index — full design reference
- [ ] 18. agentos-index-activate — session bootstrap
- [ ] 19. agentos-index-trigger — detection loop
- [ ] 20. agentos-index-resolution — name resolution
- [ ] 21. agentos-index-writer — gated write path
- [ ] 22. agentos-index-doctor — health diagnosis
- [ ] 23. agentos-index-appendix-base — appendix protocol

#### Layer 7 — Integration Points
- [ ] 24. Design.Index.Block promotion path
- [ ] 25. Alignment.Model connections
- [ ] 26. Cross-project index instances

## Session.Log

- session opened — goal: full index system revisit
- backend upgraded to Alignment.Backend:Artifact:What
- skill map agreed as traversal tracker
- per-item protocol defined: test → align → react → capture
- item 1 (Agentos.Index) reviewed — Design.Index.Block captured
- item 2 (Agentos.Index.Notes) reviewed — Design.Index.Block captured; wording correction + enrichment
- item 3 (Index.Block) reviewed — design change: Kernel.Writing and Kernel.Block extracted as new base concepts
- block zoo simplified: Kernel.Block as base (fundamentals + appendix + meta), Complete.Index.Block removed, ### index and ### outlinks absorbed into ### meta
- items 4-5 (Dotted.Notation, Dotted.Parameterized.Notation) confirmed as-is
- item 6 (File.Numbering.Protocol) confirmed as-is
