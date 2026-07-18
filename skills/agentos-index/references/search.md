# agentos-index --search

Use this module when the caller wants cited index context, conceptual lookup, appendix depth, or the current discussion grounded against the index.

`--search`, `--research`, and `--ground` all route here. The prompt is a focus argument: it narrows the search frame, but the search pass still compares the current visible discussion against the index when discussion context exists.

Search is read-only and ungated. It changes the agent's context, never a surface.

## Search Model

- use routing-first selective loading
- start with the relevant routers in the engaged `Index.Depot`s
- respect `--depot` as the engaged depot scope; otherwise use task-relevant engaged depots
- respect `--chapter` as the active `Index.Chapter` within engaged depots; default to `design`
- derive the active concepts, claims, tensions, and decisions from the current visible discussion
- use the prompt as the focus argument; a bare concept name is a valid focus, not a separate mode
- find the concept or nearby related names before loading chapter files
- load only the concept blocks, appendix pages, and references that are relevant to the current task
- compare loaded index material against the visible discussion and focus argument
- distinguish what the index explicitly says from what the agent infers by comparing discussion against index material
- do not preload the full index as a default runtime
- follow symlinks when traversing surfaces — index files, appendix pages, and whole skill trees are commonly symlinked in; use symlink-following tooling (e.g. `grep -R`, `find -L`) so linked surfaces are not silently skipped

## Search Steps

1. Identify the focus argument and the visible discussion context: concepts, claims, tensions, decisions, and open questions.
2. Read the relevant routing surfaces from the engaged depots.
3. Apply depot and chapter scope; default chapter is `design`, and widen only when the task, routed concept, or live discussion calls for it.
4. Identify the target concept or nearby related concepts.
5. Read the chapter file (`<chapter>/NNN-<chapter>.md`) that owns the routed concept.
6. Load appendix depth only when the block does not carry enough signal.
7. Load references only when the task needs operational detail or concrete examples.
8. Compare the loaded material against the visible discussion and report what matters.

## Reading What You Find

- lines may carry a leading `Line.Type` code (`- [CT] ...`): the type is the line's act — `[CT]`/`[DC]`/`[RJ]` bind, `[PR]` orients, `[FR]` frees, `[DF]`/`[EX]` inform, `[GR]` cites evidence; see `references/type.md` to read them as constraints
- parser-backed tools read index surfaces as typed nodes: `RouterEntry` rows, `BlockHeading`s, `KernelLine`s, `MetaLine`s, code fences, and inline spans such as anchors, concept cites, type brackets, and file mentions
- untyped lines are pre-fence legacy — same authority, just not yet classified
- a trailing `^YYYYMMDD-N` token is an `Anchory.Anchor`: a pointer to chat evidence, resolvable via `agentos chatlas views inline --anchor <token> --filter turns`; see `references/link.md` — resolution is optional depth, not required reading
- appendix blocks named `Concept.X/Grounding.Head` and `Concept.X/Grounding.Drift` are inert legacy sections from the retired block-grounding scheme, not conceptual content; current grounding lives on the lines themselves (`Index.Line`)
- `agendix/` files are agent-captured, user-unreviewed material — zero authority, useful as leads, never citable as accepted design

## Citation Behavior

- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use concrete surface paths when they materially improve navigation or maintenance

## Search Report

Use a compact report shape. Include only sections that help the current task:

- `relevant-concepts` — the most relevant concepts surfaced from the index
- `supporting-citations` — the blocks, appendix pages, or references that support the search result
- `discussion-grounding` — how the visible discussion or focus argument aligns with the index
- `possible-contradictions` — tensions between the current discussion and current index material
- `significant-remarks` — accepted or high-signal observations from the discussion that matter for continuation
- `missing-index-coverage` — meaningful discussion content that appears not to be modeled yet
- `recommended-next-index-action` — the single best next move from the index perspective

For a bare concept lookup with no live claim beyond the focus argument, keep the grounding section brief: say there is no additional discussion claim to compare.

## Appendix Loading Rules

- use `Appendix.Discovery` when the index block signals or suggests a need for depth
- check `appendix/Concept.Name-appendix.md` by naming convention
- load only the appendix pages that matter to the current question

## Unresolved Names

- when a name appears unresolved, search nearby routed concepts first
- if the name remains unresolved, surface it as unresolved instead of inventing a concept
- repeated unresolved names are a capture signal, not a reason to guess

## Grounding Depth

- this module runs `Index.Grounding` as the first `Context.Grounding` level: enrich the agent's context with the index's digest of the topic
- when the digest is not enough, escalate to full grounding: follow the blocks' anchors out to the original surfaces — chat evidence via `references/link.md` resolution (`views inline --anchor … --filter turns`), code and files directly
- do not pretend to ground against conversation state that is not actually visible in the current prompt or thread
- recommend `--edit` when the search pass reveals a likely needed block revision, new concept, line append, or appendix update
- keep the report continuation-oriented: make it easier to continue the work, not just easier to inspect the search
