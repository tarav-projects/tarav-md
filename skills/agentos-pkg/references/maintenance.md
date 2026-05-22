# Maintenance

## Maintenance Checklist

Maintenance passes are the index equivalent of compilation:

- **linting**: `Index.Block.Syntax` enforcement, size constraints, separator presence
- **deduplication**: merging overlapping concepts
- **naming cleanup**: aligning names across surfaces
- **promotion**: pulling durable truth from other surfaces into index/appendix
- **stub resolution**: expanding stubs or removing empty ones
- **index routing**: keeping `000-index.md` routing table current
- **placement audit**: detecting content drift between surfaces (`Placement.Heuristic`)

****

## Index.CLI

- `agentos index` is the CLI surface for deterministic index operations — the "compiler"
- **doctor**: `agentos index doctor` — detect separator issues, syntax violations, health problems
- **linting**: `Index.Block.Syntax` validation, size enforcement, structural checks
- **lookup**: deterministic concept search and block retrieval

### Block Extraction (current)

- `agentos stdlib mdblocks blocks` — parse blocks anchored by `****` + H2-H6 headings
- `agentos stdlib mdblocks links` — emit companion links for separator-anchored blocks
- `agentos stdlib mdblocks lint` — lint blocks; enforces the 25-line hard limit
- `agentos stdlib mdblocks find --query ...` — find best-matching blocks by query
