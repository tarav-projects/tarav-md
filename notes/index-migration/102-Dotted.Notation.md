<!-- FILE MIGRATED -->
# Dotted.Notation

`Dotted.Notation` identifies named concepts in an ontology surface.

A dotted name is a signal that the phrase refers to a concept, not just casual prose.

## Base Rules

- Dotted names mark ontology concepts.
- Every ontology name has at least two parts.
- Dot depth is flexible and should be natural to the concept.
- Dots provide context, but they are not a strict hierarchy or namespace system.
- The definition and relationships live in notes and registry entries, not in the name alone.
- `Ontology.Namespace` must be explicit; do not infer a namespace from a dotted prefix alone.

Examples:

- `Agentos.Index.Notes`
- `Md.Surface`
- `Maintenance.System`
- `File.Numbering.Protocol`

## Registry Relationship

A dotted name can appear before it is registered.

The lifecycle is descriptive:

- a dotted name signals a possible concept
- the ontology registry curates stabilized concepts
- a dedicated note expands concepts with enough weight

Agents should not maintain explicit lifecycle state. They should infer concept maturity from the repository: whether the name appears only in prose, has a registry entry, or has a dedicated note.

## Lookup Behavior

Registry lookup is opportunistic, not mandatory for all agent work.

Use registry lookup when concept identity matters, especially when:

- the user uses dotted notation
- the user uses an approximate or old concept name
- a design discussion depends on consistent names
- maintenance is checking duplicate, stale, or unregistered concepts

Avoid turning ordinary work into ontology maintenance when concept identity is not relevant.

## Dotted.Parameterized.Notation

`Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept.

Use:

```txt
Concept.Name:Target
```

Rules:

- the part before the colon is the concept
- the part after the colon is the parameter
- colon parameters may themselves use dots
- parameterized references are instances of the same concept, not different concepts
- use a new dotted name when the meaning changes
- use a colon parameter when the same concept is applied to a different target

Examples:

- `Maintenance.System:Agentos`
- `Maintenance.System:Example.Project`
- `Project.CLI:Agentos`
- `Md.Surface:Agentos.Stack`

Parameterized references may appear as examples or references in the ontology registry, but they are not canonical ontology entries by default unless a separate instance-registry concept is introduced later.

## Related Concepts

- `Agentos.Index.Ontology.Registry`
- `Agentos.Ontology.Workflows`
- `Ontology.Namespace`
- `Stub.Convention`
- `Maintenance.System`

## Provenance

Promoted from the closed design session at `../live/501-agentos-index-notes-design-session.md`.
