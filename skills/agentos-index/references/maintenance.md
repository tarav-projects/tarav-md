# Maintenance

## Maintenance Model

- the index is maintained through constant additive improvement — like code maintenance
- the index is never complete
- each pass should leave things slightly better aligned
- small, frequent passes beat large infrequent ones
- maintenance is diagnosis-first, not fix-first

### Maintenance as "compilation"

Maintenance passes are the index equivalent of compilation:

- **linting**: `Index.Block.Syntax` enforcement, size constraints, separator presence
- **deduplication**: merging overlapping concepts (caught by `Index.Name.Resolution`)
- **naming cleanup**: aligning names with the ontology registry
- **registry sync**: adding new concepts, updating stale entries
- **promotion**: pulling durable truth from other surfaces
- **stub resolution**: expanding stubs or removing empty ones
- **index routing**: keeping `000-index.md` routing table current

### What maintenance is NOT

- maintenance is note-level work, not project progress tracking
- it should not turn the index into a changelog, task list, or status dashboard

****

## Promotion Model

- knowledge flows toward the index through promotion
- material starts wherever it naturally appears: chat, live notes, skills, AGENTS.md, code comments, design sessions
- when it becomes durable design truth, it should be promoted

Signs of a promotion candidate:

- referenced repeatedly from outside its current location
- defines a concept that multiple agents or sessions need
- captures a constraint or decision that would be lost if the current surface is discarded
- lives in a skill but is really design truth, not operational guidance
- keeps appearing as `Unresolved.Index.Name` in conversations

Promotion is a maintenance activity, not a gate on initial capture.

****

## Low-Friction Capture

- the path from idea to storage must have zero friction
- the user must never spend time thinking about where a note should go
- useful material can enter before it has mature structure
- rough notes, partial concepts, stubs are acceptable when the knowledge is important
- organization and polish are maintenance steps, not prerequisites

****

## Stub.Convention

- incomplete index entries are allowed when they still contain minimal durable signal

A valid stub must have:

- a real concept boundary (a `Dotted.Name`, not just a placeholder)
- a short definition or description (at least one grounding sentence)
- explicit acknowledgment of incompleteness
- useful direction for future work

A stub that is just a title with no content is not a valid index entry. But a stub with a name and one precise sentence IS valid.

****

## File.Numbering.Protocol

- numeric filename prefixes provide stable, addressable handles for index files
- 3-digit zero-padded prefix: `NNN-Title.md`
- assigned prefixes are permanent
- gaps are allowed; allocation is append-only
- allocate with `agentos stdlib prefix next`
- range: `000-099` reserved, `100-499` index notes, `500-999` other

****

## Index.CLI

- `agentos index` is the CLI surface for deterministic index operations — the "compiler"
- **doctor**: `agentos index doctor` — detect separator issues, syntax violations, health problems
- **linting**: `Index.Block.Syntax` validation, size enforcement, structural checks
- **lookup**: deterministic concept search and block retrieval
- **name resolution**: supporting `Index.Name.Resolution` programmatically
- **registry sync**: checking ontology registry completeness and staleness

### Block Extraction (current)

- `agentos stdlib mdblocks blocks` — parse blocks anchored by `****` + H2-H6 headings
- `agentos stdlib mdblocks links` — emit companion links for separator-anchored blocks
- `agentos stdlib mdblocks lint` — lint blocks; enforces the 25-line hard limit
- `agentos stdlib mdblocks find --query ...` — find best-matching blocks by query
