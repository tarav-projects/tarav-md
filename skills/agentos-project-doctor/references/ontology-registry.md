# Ontology Checks

Check whether the index covers active dotted concepts. Architecture context (routing table role, concept scoping, public/local split) comes from the index itself.

## Deterministic Checks

When a routing table exists:

- search for dotted concept-like names across stable surfaces
- compare concept headings in flat files with routing table entries
- check that obvious active concepts appear in the routing table

Use simple search first. Do not overfit the regex.

## Agentic Checks

- Decide whether unregistered dotted names are real concepts, examples, parameters, or incidental prose.
- Distinguish `Dotted.Notation` concepts from `Dotted.Parameterized.Notation` examples.
- Treat missing routing entries as findings only when concept identity matters.

## Expected Findings

- `fail`: index exists but routing table is missing.
- `warn`: important concepts appear in stable surfaces but are missing from the routing table.
- `warn`: routing table appears stale relative to obvious active concepts.
- `info`: dotted names are sparse or only examples.
- `pass`: routing table exists and covers obvious active concepts.
