# Dotted.Notation

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- a dotted name is a signal that the phrase refers to a concept, not casual prose
- every name has at least two parts; dot depth is flexible and natural to the concept
- dots provide context but are not a strict hierarchy — definition and relationships live in notes and registry entries, not the name
- `Ontology.Namespace` must be explicit; do not infer a namespace from a dotted prefix alone
- a dotted name can appear before it is registered
    - agents infer concept maturity from the repository: prose-only, registry entry, or dedicated note
- registry lookup is opportunistic, not mandatory — use it when concept identity matters, avoid turning ordinary work into ontology maintenance

****

## Dotted.Parameterized.Notation

- `Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept
- form: `Concept.Name:Target`
- the part before the colon is the concept, the part after is the parameter
- colon parameters may themselves use dots
- parameterized references are instances of the same concept, not different concepts
    - use a new dotted name when the meaning changes
    - use a colon parameter when the same concept is applied to a different target
- examples: `Maintenance.System:Agentos`, `Md.Surface:Agentos.Stack`, `Project.CLI:Agentos`
