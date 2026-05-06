# Ontology Registry Checks

Check whether dotted concepts are supported by an ontology registry.

## Concepts

- `notes/index/001-ontology.md` is the local ontology entrypoint.
- `Ontology.Namespace` files or sections are valid organizing views over ontology concepts.
- `Ontology.Integration.Hook` files are valid ontology namespaces for external concepts consumed locally.
- Integration-hook files are not replacements for `001-ontology.md`; they should be routed from it.

## Deterministic Checks

When `notes/index/` exists:

- search for dotted concept-like names in `notes/index/*.md`
- check for `notes/index/001-ontology.md`
- compare obvious dotted concept headings or repeated names with registry entries when feasible
- identify ontology namespace or integration-hook files, such as `*-Integration.Ontology.md`
- check whether `001-ontology.md` routes to active namespace or integration-hook files when those files exist

Use simple search first. Do not overfit the regex.

## Agentic Checks

- Decide whether unregistered dotted names are real concepts, examples, parameters, or incidental prose.
- Distinguish `Dotted.Notation` concepts from `Dotted.Parameterized.Notation` examples.
- Treat missing registry entries as findings only when concept identity matters.
- Treat extra namespace or integration-hook ontology files as valid when they are connected through `001-ontology.md`.
- Treat an integration-hook file as a warning only when it appears to replace, bypass, or drift from the local ontology entrypoint.

## Expected Findings

- `fail`: `notes/index/` exists but `001-ontology.md` is missing.
- `warn`: repeated or central dotted concept names exist but no `001-ontology.md` exists.
- `warn`: important concepts appear in index notes but are missing from the registry.
- `warn`: `001-ontology.md` exists but appears stale relative to obvious active concepts.
- `warn`: an ontology namespace or integration-hook file exists but is not routed from `001-ontology.md`.
- `info`: dotted names are sparse or only examples.
- `pass`: registry exists and covers obvious active concepts.
