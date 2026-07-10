# agentos-index2 --search

Use this module when the caller wants cited index context, conceptual lookup, or appendix depth.

## Search Model

- use routing-first selective loading
- start with the relevant routers in the engaged `Index.Depot`s
- respect `--depot` as the engaged depot scope; otherwise use task-relevant engaged depots
- respect `--chapter` as the active `Index.Chapter` within engaged depots; default to `design`
- find the concept or a nearby related name before loading chapter files
- load only the concept blocks, appendix pages, and references that are relevant to the current task
- do not preload the full index as a default runtime
- follow symlinks when traversing surfaces — index files, appendix pages, and whole skill trees are commonly symlinked in; use symlink-following tooling (e.g. `grep -R`, `find -L`) so linked surfaces are not silently skipped

## Search Steps

1. Read the relevant routing surfaces from the engaged depots.
2. Apply depot and chapter scope; default chapter is `design`, and widen only when the task or routed concept calls for it.
3. Identify the target concept or nearby related concepts.
4. Read the chapter file (`<chapter>/NNN-<chapter>.md`) that owns the routed concept.
5. Load appendix depth only when the block does not carry enough signal.
6. Load references only when the task needs operational detail or concrete examples.

## Reading What You Find

- lines may carry a leading `Line.Type` code (`- [CT] ...`): the type is the line's act — `[CT]`/`[DC]`/`[RJ]` bind, `[PR]` orients, `[FR]` frees, `[DF]`/`[EX]` inform, `[GR]` cites evidence; see `references/type.md` to read them as constraints
- parser-backed tools read index surfaces as typed nodes: `RouterEntry` rows, `BlockHeading`s, `KernelLine`s, `MetaLine`s, code fences, and inline spans such as anchors, concept cites, type brackets, and file mentions
- untyped lines are pre-fence legacy — same authority, just not yet classified
- a trailing `^YYYYMMDD-N` token is an `Anchory.Anchor`: a pointer to chat evidence, resolvable via `agentos chatlas views inline --anchor <token> --filter turns`; see `references/link.md` — resolution is optional depth, not required reading
- appendix blocks named `Concept.X/Grounding.Head` and `Concept.X/Grounding.Drift` are evidence sections, not conceptual content: Head supports the block as written, Drift is kept provenance
- `agendix/` files are agent-captured, user-unreviewed material — zero authority, useful as leads, never citable as accepted design

## Citation Behavior

- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use concrete surface paths when they materially improve navigation or maintenance

## Appendix Loading Rules

- use `Appendix.Discovery` when the index block signals or suggests a need for depth
- check `appendix/Concept.Name-appendix.md` by naming convention
- load only the appendix pages that matter to the current question

## Unresolved Names

- when a name appears unresolved, search nearby routed concepts first
- if the name remains unresolved, surface it as unresolved instead of inventing a concept
- repeated unresolved names are a capture signal, not a reason to guess
