****

## Agentos.Index.System/Alignment.Role

- the index is a `Stable.Surface` — it must be aligned with all other surfaces (`Internal.Alignment`)
- the index explicitly holds the conceptual model of the project — `Forward.Alignment` passes often target it first
- the index is both `Write.Trigger.Gated` and `Content.Verbatim.Gated` by default — this review point supports `Hugentic.Alignment`

****

## Agentos.Index.System/Appendix

- it is a `Soft.Programming.Language` for project knowledge — a library of micro-prompts invoked by naming
- mentioning a `Dotted.Name` triggers a concept-level context load
- it manipulates the agent's context window — by controlling what enters context, you control how the agent reasons
- it is an `Explicit.Namespace` grouping the concepts that compose the index system
- the Index is a nested indexing surface — each layer indexes the one beneath it: the surface indexes the project's content across its `Surface.Types` (the `Chat.Surface` foremost), the chapters index the surface, the `Index.Router` indexes the chapters; "the index" resolves by context, the `Index.*` names disambiguate the layers
- ~20 concept blocks per chapter file — hard cap
- the Index loads when the `Package.Driver` brings it into context — not unconditionally
- chapters group loading, not meaning — conceptual organization stays with `Block.Path` and `Explicit.Namespace`
- one base block (`Kernel.Block`) with surface-placement variants `Index.Block`, `Appendix.Block`, `Design.Block`
- one portable file container (`Kernel.Note`) for collecting `Kernel.Block` sections outside index routing
- one writing philosophy (`Kernel.Writing`) — space constraints come from the surface, not the philosophy

****

## Agentos.Index.System/Index.Surface.Layout

- `Index.Surface.Layout` is the directory protocol a package follows to host an Index
- a hosted Index is a `000-INDEX.md` lookup over one folder per `Index.Chapter`, plus a shared `appendix/`

public Index — in the package skill:
```
skills/<package>-pkg/
├── 000-INDEX.md          — concept→file lookup, sectioned by chapter
├── design/            — default chapter;     NNN-design.md
├── impl/              — reserved chapter;     NNN-impl.md
├── <chapter>/         — any further chapter;  NNN-<chapter>.md
└── appendix/          — shared depth;         Concept.Name-appendix.md
```

- each `Index.Depot` follows this shape, whether owned by a project (under `notes/`) or a `Package.Skill`; they compose via `Index.Discovery`
- the layout is a protocol — a package follows it to be Index-compatible
- within a chapter, files are flat and anonymous; writing appends to the last file, so placement is never a writing decision
- splitting an overfull file is maintenance, not a writing concern

