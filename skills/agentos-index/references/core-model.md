# Core Model

## Soft.Programming.Language

- the index is a `Soft.Programming.Language` for project knowledge
- "soft" because the syntax is natural language; "programming" because it has execution semantics
- it is not documentation, not a wiki, not a knowledge base
- it is closer to a program for cognitive operations that humans and agents run against

The code-to-index mapping:

- **variable declaration** → naming a concept with `Dotted.Notation`
- **symbol table** → `000-index.md` routing table — the registry of known names
- **module** → `Index.Note` — a cluster of related definitions
- **function body** → `Index.Block` — the loadable unit of meaning
- **type system** → `Index.Block.Syntax` — structural conventions for writing blocks
- **import** → loading blocks into agent context
- **name resolution** → `Index.Name.Resolution` — fuzzy match to canonical name
- **undefined variable** → `Unresolved.Index.Name` — parked for later
- **compilation** → maintenance passes — linting, deduplication, structure enforcement
- **compiler CLI** → `agentos index` — the deterministic tooling surface
- **runtime** → the conversation itself — where the index is active and concepts are grounded

The structure comes from conventions (Dotted.Names, block shape, separators), not from rigid formal grammar.

****

## Alignment.Surface

- the index is the fundamental `Alignment.Surface` between humans and agents
- it exists precisely at the interface — the shared ground where both sides align on what things mean
- its primary purpose is shared grounding, not storage

Design consequences:

- **readable by humans**: natural language, browsable, self-locating
- **operable by agents**: structured, loadable, searchable, parseable
- **neither side owns it alone**: both contribute, both consume
- the equilibrium is structured natural language with consistent shape

****

## SSOT Rule

- the index is the **definitional authority** for all `Named.Concepts` in the project
- every `Dotted.Name` is defined in the index and nowhere else
- for anything sufficiently relevant → name it → write a block in the index

What the index contains per concept:

- what it IS (the definition)
- why it exists (rationale)
- how it connects to other concepts (relationships, integration)
- user preferences and gated decisions
- boundaries (what it is NOT)

What lives on other surfaces (further detail):

- **code**: exact implementation — classes, fields, methods, flags
- **CLI help**: usage interface — commands, flags, examples
- **skills**: operational behavior, reusable workflows
- **AGENTS.md**: project-local agent guidance

These are further detail, not definitions. The conceptual definition always lives in the index.

### Extraction rule

- the index keeps the conceptual definition (what, why, how it connects)
- the index links out to the surface where the explicit/mechanical detail lives
- do not duplicate what the code or CLI already says precisely
- a block can have a conceptual declaration + a link out for the full mechanics

### The index as entry point

- by traveling the index, an agent should reach all `Stable.Surfaces` of the project
- the index is the main entry point for understanding the whole system
- it achieves this through definitions and links — not by containing all detail

****

## Stable.Surface

- a `Stable.Surface` is a durable, authoritative surface where a specific facet of project knowledge lives
- each `Stable.Surface` is the best place for its kind of information
- a project has multiple `Stable.Surfaces` — the index is one of them
- the index links to all other `Stable.Surfaces`, making the full system navigable

Examples:

- **index** (`notes/index/`) — conceptual model, ontology, rationale, preferences
- **skills** (`skills/`) — public reusable behaviors, operational specs
- **CLI help** — command interface, flags, usage
- **codebase** — current implementation (the full mechanical description by construction)
- **AGENTS.md** — project-local agent workflow guidance

****

## What Belongs In The Index

- the index contains `Named.Concepts` — ideas that are fundamental to the project

A concept belongs in the index when:

- it is long-lasting (survives across sessions, agents, and time)
- it is fundamental (without it, something important is missing)
- it changes future judgment (knowing it affects how decisions are made)
- it can be named (forced into `Dotted.Notation` with a precise definition)

What does NOT belong:

- transcripts, changelogs, session-specific state
- implementation dumps (code belongs in code)
- progress dashboards, task lists (these live in live notes)
- generic tutorials
- anything that doesn't survive the "name it precisely" test
