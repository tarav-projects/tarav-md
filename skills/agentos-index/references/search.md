# agentos-index --search

Use this module when the caller wants cited index context, conceptual lookup, or appendix depth.

## Search Model

- use routing-first selective loading
- start with the relevant router: public `000-INDEX.md`, local `notes/index/001-index.md`, or both
- find the concept or a nearby related name before loading chapter files
- load only the concept blocks, appendix pages, and references that are relevant to the current task
- do not preload the full index as a default runtime
- follow symlinks when traversing surfaces — index files, appendix pages, and whole skill trees are commonly symlinked in; use symlink-following tooling (e.g. `grep -R`, `find -L`) so linked surfaces are not silently skipped

## Search Steps

1. Read the relevant routing surface.
2. Identify the target concept or nearby related concepts.
3. Read the chapter file (`design/NNN-design.md`) that owns the routed concept.
4. Load appendix depth only when the block does not carry enough signal.
5. Load references only when the task needs operational detail or concrete examples.

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
