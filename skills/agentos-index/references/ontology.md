# Ontology

## Ontology.Registry

- `001-ontology.md` is the symbol table of the index
- the official entry point to the ontology — the registry of all named concepts
- the primary lookup surface for `Index.Name.Resolution`

### Two navigation trees

- `000-index.md` — entry point to the file organization (which notes exist, where to start reading)
- `001-ontology.md` — entry point to the ontological organization (which concepts exist, how they relate)
- these are complementary views of the same knowledge graph

### Role

- low-resolution concept inventory
- compact definitions (1-3 sentences per concept)
- pointers to fuller notes when they exist
- the lookup surface for `Index.Name.Resolution`
- organized into `Ontology.Namespaces`

### The knowledge graph view

- the index is ultimately a knowledge graph
- blocks are the smallest nodes
- notes are clusters of related nodes
- the ontology registry is the entry point to the graph
- all content should evolve to be under a named concept

****

## Ontology.Namespace

- `Ontology.Namespace` is an explicit bounded organizing view over ontology concepts
- namespaces are not inferred from dotted notation
- namespaces are not exclusive ownership containers
- may overlap — a concept can appear in multiple namespaces
- must be explicitly declared
- can multiply freely from `001-ontology.md` as the entry point

### Ontology.Integration.Hook

- a namespace where one project records external concepts it consumes from another project's ontology
- includes local interpretation, implementation mode, constraints, or mappings

****

## Ontology.Workflows

- concepts have a natural lifecycle in the index
- these workflows are well-defined so agents can participate through the `Index.Eval.Loop`

### Emergence

- a concept appears informally in discussion or prose
- someone uses `Dotted.Notation`, firing a `Dotted.Name.Trigger`
- the `Index.Eval.Loop` detects it as unresolved → `Gap.Detection` → `Emergence.Signal`
- the concept lives in the agent's working memory initially

### Registration

- when the concept stabilizes, it gets a compact entry in `001-ontology.md`
- triggered when concept identity matters: design discussions, naming decisions, repeated `Unresolved.Index.Names`
- the user gates registration (agent proposes, user approves — `User.Gated.Index`)

### Promotion

- when a concept has enough weight, it gets a dedicated `Index.Note` with full `Index.Blocks`
- a concept can have a registry entry without a note
- a concept can have a note without going through registry-first

### Rename and cleanup

- concept names may evolve, but dotted names in published surfaces should be updated together
- stale or duplicate names are caught during maintenance passes or by `Index.Name.Resolution`
- the ontology registry is the lookup surface for current canonical names

****

## Reserved Notes

- some notes have fixed system roles — the index's "built-in functions"
- `000-index.md` — entry point to the file organization; routes to concept notes
- `001-ontology.md` — entry point to the ontological organization; the symbol table

****

## Index Surface Layout

```
notes/
  index/           ← the index: durable concept notes (Design.Target.Model)
    000-index.md   ← reserved: file-organization entry point
    001-ontology.md ← reserved: ontological entry point (symbol table)
    1NN-*.md       ← rolling concept notes (modules)
  live/            ← in-progress work, temporary state
    010.TODOS.md   ← reserved: TODO parking
    011.ISSUES.md  ← reserved: issue parking
    5NN-*.md       ← rolling live notes
  canvas/          ← visual collaboration surfaces
```
