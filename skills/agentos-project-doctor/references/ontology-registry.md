# Ontology Checks

Check whether the index covers active dotted concepts. Architecture context (router role, concept scoping, public/local split) comes from the index itself.

## Deterministic Checks

When a router exists:

- search for dotted concept-like names across stable surfaces
- compare concept headings in chapter/flat files with router entries
- check that obvious active concepts appear in the router

Use simple search first. Do not overfit the regex.

## Agentic Checks

- Decide whether unregistered dotted names are real concepts, examples, parameters, or incidental prose.
- Distinguish `Dotted.Notation` concepts from `Dotted.Parameterized.Notation` examples.
- Treat missing routing entries as findings only when concept identity matters.

## Expected Findings

- `fail`: index exists but router is missing.
- `warn`: important concepts appear in stable surfaces but are missing from the router.
- `warn`: router appears stale relative to obvious active concepts.
- `info`: dotted names are sparse or only examples.
- `pass`: router exists and covers obvious active concepts.
