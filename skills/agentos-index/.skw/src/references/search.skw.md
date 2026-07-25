# agentos-index --search

> $kw: --from Appendix.Discovery --from Context.Grounding --from Index.Agendix --from Index.Chapter --from Index.Depot --from Index.Grounding --from Index.Line --from Line.Type --from Reviewed.Cite.Closure --from Touched.Authority --from User.Attention
> --dev-from references/index-context-assembly.skw.md

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
- escalate down the `User.Attention` gradient: the reviewed block and its appendix first (presumably higher attention), then the concept's unreviewed `Index.Agendix` leads, then raw chat/code — a heuristic order, not a guarantee, which is why the steps are explicit
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
7. Read the top-relevant concept's agendix (`agendix/Concept.Name-agendix.md`) when it exists — unreviewed `Touched.Authority` leads, surfaced separately from accepted citations.
8. Load references only when the task needs operational detail or concrete examples.
9. Compare the loaded material against the visible discussion and report what matters.

## Reading What You Find

- lines may carry a leading `Line.Type` code (`- [CT] ...`): the type is the line's act — `[CT]`/`[DC]`/`[RJ]` bind, `[PR]` orients, `[FR]` frees, `[DF]`/`[EX]` inform, `[GR]` cites evidence; see `references/type.md` to read them as constraints
- parser-backed tools read index surfaces as typed nodes: `RouterEntry` rows, `BlockHeading`s, `KernelLine`s, `MetaLine`s, code fences, and inline spans such as anchors, concept cites, type brackets, and file mentions
- untyped lines are pre-fence legacy — same authority, just not yet classified
- a trailing `^c<YYYYMMDD>-<N><tag>` token is an `Anchory.Anchor`: a pointer to chat evidence (`c` = chatlas namespace; tag `u`/`a` = user/assistant landing turn), resolvable via `agentos chatlas views inline --anchor <token> --filter turns`; see `references/link.md` — resolution is optional depth, not required reading
- appendix blocks named `Concept.X/Grounding.Head` and `Concept.X/Grounding.Drift` are inert legacy sections from the retired block-grounding scheme, not conceptual content; current grounding lives on the lines themselves (`Index.Line`)
- `agendix/` files are agent-captured, unreviewed material carrying `Touched.Authority` — useful as leads and citable from other unreviewed surfaces, but a reviewed surface may not cite them (`Reviewed.Cite.Closure`); not accepted design wording

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
- `agendix-leads` — unreviewed `Index.Agendix` material surfaced for the top concepts, kept distinct from `supporting-citations` (leads, not citations); flag any the pass relied on as promotion candidates
- `missing-index-coverage` — meaningful discussion content that appears not to be modeled yet, and not already harvested in the agendix
- `recommended-next-index-action` — the single best next move from the index perspective

For a bare concept lookup with no live claim beyond the focus argument, keep the grounding section brief: say there is no additional discussion claim to compare.

## Appendix Loading Rules

- use `Appendix.Discovery` when the index block signals or suggests a need for depth
- check `appendix/Concept.Name-appendix.md` by naming convention
- load only the appendix pages that matter to the current question

## Agendix Loading Rules

- always check the top-relevant concept's `agendix/Concept.Name-agendix.md` by naming convention — unlike the appendix, do not gate this on the block being thin: the agendix holds user-touched leads worth surfacing whenever the concept is central
- read agendix lines as unreviewed `Touched.Authority` leads, never as accepted wording — they inform continuation, they do not settle it
- keep them out of `supporting-citations`: report them under `agendix-leads` — a reviewed surface may not cite the agendix (`Reviewed.Cite.Closure`)
- before reporting `missing-index-coverage`, check the agendix — a lead already harvested there is promotion-ready, not missing
- when the pass actually leans on an agendix lead, recommend its promotion through `--edit` (gated) — use is the promotion signal

## Unresolved Names

- when a name appears unresolved, search nearby routed concepts first
- if the name remains unresolved, surface it as unresolved instead of inventing a concept
- repeated unresolved names are a capture signal, not a reason to guess

## Grounding Depth

- this module runs `Index.Grounding` as the first `Context.Grounding` level: enrich the agent's context with the index's digest of the topic
- next down the `User.Attention` gradient, read the concept's `Index.Agendix` — the last index-local rung: unreviewed touched leads already harvested from chat, cheaper than resolving anchors back out
- when the index-local rungs are not enough, escalate to full grounding: follow the blocks' anchors out to the original surfaces — chat evidence via `references/link.md` resolution (`views inline --anchor … --filter turns`), code and files directly
- do not pretend to ground against conversation state that is not actually visible in the current prompt or thread
- recommend `--edit` when the search pass reveals a likely needed block revision, new concept, line append, or appendix update
- keep the report continuation-oriented: make it easier to continue the work, not just easier to inspect the search
