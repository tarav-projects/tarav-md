# Ontology

## Concept.Scoping

- `Concept.Scoping` is the general mechanism: any concept can scope other concepts through its appendix file
- an appendix file can contain blocks for other concepts, viewed through the host concept's lens
- notation: `Concept.B/Concept.A` — Concept.A as seen from Concept.B's scope

****

## Explicit.Namespace

- `Explicit.Namespace` is a concept that intentionally organizes a view over a set of related concepts
- the mechanics are `Concept.Scoping` — the difference is intent: this concept declares itself as a namespace
- namespace membership is declared in the namespace's global block under `### meta` as a `namespace-members` list

****

## Concept.Lifecycle

- concepts have a natural lifecycle in the index

### Emergence

- a concept appears informally in discussion or prose
- someone uses `Dotted.Notation` — it doesn't resolve against the loaded index
- the agent detects it as unresolved → parks as `Unresolved.Index.Name`

### Capture

- when the concept stabilizes, it gets a `Kernel.Block:Index` in a flat index file
- the user gates capture (`Write.Trigger.Gated` + `Content.Verbatim.Gated`)
- the routing table (`000-index.md`) is updated to include the new concept

### Rename and cleanup

- concept names may evolve, but dotted names in published surfaces should be updated together
- stale or duplicate names are caught during maintenance passes or by `Index.Name.Resolution`
- the routing table is the lookup surface for current canonical names

****

## Index Surface Layout

```
skills/agentos-index/
  index/             ← public index (Distributed.Index)
    000-index.md     ← routing table (public entry point)
    100-299-*.md     ← public flat index files
  appendix/          ← public appendix
    Concept.Name-appendix.md

notes/
  index/             ← local index
    000-index.md     ← local entry point (points to public)
    300-499-*.md     ← local flat index files
  appendix/          ← local appendix
  live/              ← in-progress work, temporary state
    010.TODOS.md     ← reserved: TODO parking
    011.ISSUES.md    ← reserved: issue parking
    5NN-*.md         ← rolling live notes
  canvas/            ← visual collaboration surfaces
```
