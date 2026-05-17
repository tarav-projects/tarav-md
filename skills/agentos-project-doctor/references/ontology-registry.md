# Ontology Checks

Check whether the index covers active dotted concepts.

## Concepts

- `000-index.md` routing table is the concept registry — maps every `Dotted.Name` to its flat file
- `Concept.Scoping` and `Explicit.Namespace` organize views over concepts through appendix files
- Public index lives at `skills/agentos-index/index/`, local index at `notes/index/`

## Deterministic Checks

When `skills/agentos-index/index/` or `notes/index/` exists:

- search for dotted concept-like names across stable surfaces
- check that `000-index.md` routing table covers obvious active concepts
- compare concept headings in flat files with routing table entries

Use simple search first. Do not overfit the regex.

## Agentic Checks

- Decide whether unregistered dotted names are real concepts, examples, parameters, or incidental prose.
- Distinguish `Dotted.Notation` concepts from `Dotted.Parameterized.Notation` examples.
- Treat missing routing entries as findings only when concept identity matters.

## Expected Findings

- `fail`: index exists but `000-index.md` routing table is missing.
- `warn`: important concepts appear in stable surfaces but are missing from the routing table.
- `warn`: routing table appears stale relative to obvious active concepts.
- `info`: dotted names are sparse or only examples.
- `pass`: routing table exists and covers obvious active concepts.
