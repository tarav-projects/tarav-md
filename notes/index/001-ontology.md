# Agentos Ontology Registry

## Index.Note

- `Index.Note` is the structural index of `notes/index/`
- lists what files exist in the index folder and how to navigate them
- maps the file tree, not the conceptual model — for concepts see `Index.Ontology.Note`
- reserved at `000-index.md` — stable path, always the entry point for folder orientation

****

## Index.Ontology.Note

- `Index.Ontology.Note` is the concept-space map of the Agentos index
- low-resolution registry: records what concepts exist, gives each a compact definition, points to fuller notes
- organized by `Ontology.Namespaces` — multiple overlapping views over the same concepts
- a concept lives in one file (routed by `Index.Note`) but can appear in multiple namespaces here
- not the place for deep treatment — that lives in concept notes
- reserved at `001-ontology.md` — stable path, always the entry point for concept lookup

****

## Agentos.Index.Notes

- `Agentos.Index.Notes` is the durable concept-note subsystem of an Agentos-style project
- implements the `Agentos.Index` — a `Soft.Programming.Language` for project knowledge
- see `114-Agentos.Index.Notes.md`

****

## Agentos.Index.Writing.Principles

- `Agentos.Index.Writing.Principles` defines what belongs in durable index notes
- all index content is organized as `Named.Concepts` in `Index.Blocks`
- see `114-Agentos.Index.Notes.md`

****

## Md.Surface

- `Md.Surface` is a qualifier for the markdown layer of a target
- see `115-Md.Surface.md`

****

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- see `116-Dotted.Notation.md`

****

## Dotted.Parameterized.Notation

- `Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept
- see `116-Dotted.Notation.md`
