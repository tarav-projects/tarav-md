# Ontology Registry Checks

Check whether dotted concepts are supported by an ontology registry.

## Deterministic Checks

When `notes/index/` exists:

- search for dotted concept-like names in `notes/index/*.md`
- check for `notes/index/001-ontology.md`
- compare obvious dotted concept headings or repeated names with registry entries when feasible

Use simple search first. Do not overfit the regex.

## Agentic Checks

- Decide whether unregistered dotted names are real concepts, examples, parameters, or incidental prose.
- Distinguish `Dotted.Notation` concepts from `Dotted.Parameterized.Notation` examples.
- Treat missing registry entries as findings only when concept identity matters.

## Expected Findings

- `warn`: repeated or central dotted concept names exist but no `001-ontology.md` exists.
- `warn`: important concepts appear in index notes but are missing from the registry.
- `info`: dotted names are sparse or only examples.
- `pass`: registry exists and covers obvious active concepts.
