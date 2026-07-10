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

## Citation Behavior

- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use concrete surface paths when they materially improve navigation or maintenance

## Search Steps

1. Read the relevant routing surfaces from the engaged depots.
2. Apply depot and chapter scope; default chapter is `design`.
3. Identify the target concept or nearby related concepts.
4. Read the chapter file that owns the routed concept.
5. Load appendix depth only when the block does not carry enough signal.
