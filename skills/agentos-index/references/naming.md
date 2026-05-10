# Naming

## Dotted.Notation

- `Dotted.Notation` is the language of the index — the syntax for naming concepts
- a dotted name is a signal that the phrase refers to a concept, not casual prose
- it is also the primary trigger for `Index.Call` execution via `Dotted.Name.Trigger`

### Rules

- every ontology name has at least two parts
- dot depth is flexible and natural to the concept
- dots provide context but are not a strict hierarchy
- definitions and relationships live in blocks, not in the name alone
- `Ontology.Namespace` must be explicit; do not infer from prefix

****

## Dotted.Parameterized.Notation

- `<Concept>.Name:Target` identifies an instance of a named concept without creating a new concept
- the part before the colon is the concept
- the part after the colon is the parameter (the target)
- parameterized references are instances, not different concepts
- use a new dotted name when the meaning changes
- use a colon parameter when the same concept is applied to a different target

Examples: `Maintenance.System:Agentos`, `Md.Surface:Agentos.Stack`

****

## Variable.Notation

- `<Variable>.Name` expresses a family of names — an open/variable part
- angle brackets mark the variable part
- it means "any name of this form" — not one specific concept
- example: `<Concept>.Name:<Target>` — both parts are open
- distinct from parameterized notation which has a specific concept and a specific target

****

## Dotted.Name.Detection

- detection rules for recognizing a `Dotted.Name` in conversation
- used by `agentos-index-trigger`
- all shapes share the same signal: capitalized words joined by dots, always two+ parts

### Shapes and patterns

```
Basic:            Word.Word(.Word)*
                  e.g. Index.Block, Soft.Programming.Language

Parameterized:    Word.Word(.Word)*:target
                  e.g. Maintenance.System:Agentos, Md.Surface:Agentos.Stack

Variable:         <Word>.Word(.Word)*
                  e.g. <Concept>.Name, <Target>.System

Variable+Param:   <Word>.Word(.Word)*:<target>
                  e.g. <Concept>.Name:<Target>
```

### Regex-like definitions

```
Basic:          [A-Z][a-z]+(\.[A-Z][a-z]+)+
Parameterized:  [A-Z][a-z]+(\.[A-Z][a-z]+)+:[A-Za-z][\w\-\.]*
Variable:       <[A-Z][a-z]+>(\.[A-Z][a-z]+)+
Variable+Param: <[A-Z][a-z]+>(\.[A-Z][a-z]+)+(:<[A-Z][a-z]+>|:[A-Za-z][\w\-\.]*)
```

### NOT triggers (exclusions)

- abbreviations: `e.g.`, `i.e.`, `etc.`
- filenames: `file.txt`, `config.json`, `SKILL.md`
- URLs: `github.com`, `anthropic.com`
- lowercase dotted: `user.name`, `object.method`
- single-part names: just `Index` alone is not a trigger
