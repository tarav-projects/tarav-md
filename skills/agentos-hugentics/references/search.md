# Index.Search.Operation.Module

Use this module when the caller wants cited index context, conceptual lookup, appendix depth, or the current discussion grounded against the index.

`--search`, `--research`, `--ground`, and their `--index`-prefixed forms are exact aliases of this one Index search route. When the namespace flag is omitted, the route supplies its declared Index default. The prompt is a focus argument: it narrows the search frame, but the search pass still compares the current visible discussion against the index when discussion context exists.

Search is read-only and ungated. It changes the agent's context, never a surface.

Load `references/touched-data.md` and apply the contextualization portion of `references/decision-cycle.md`.

This is the read-only `Touched.Decision.Cycle` entry: it classifies `Live.Index.Line`, `Demoted.Index.Line`, `Touched.Data`, and `POI.Instance` evidence before using `Open.Inference`.

## Search Model

- use routing-first selective loading
- start with the relevant routers in the engaged `Index.Depot`s
- respect `--depot` as the engaged depot scope; otherwise use task-relevant engaged depots
- respect `--chapter` as the active `Index.Chapter` within engaged depots; default to `design`
- derive the active concepts, claims, tensions, and decisions from the current visible discussion
- use the prompt as the focus argument; a bare concept name is a valid focus, not a separate mode
- find the concept or nearby related names before loading chapter files
- load only the concept blocks, appendix pages, and references that are relevant to the current task
- distinguish live grounded authority, live ungrounded index presumption, review state, and demoted history before weighing content
- escalate down the `User.Attention` gradient: reviewed live content first, then unreviewed grounded leads, then original authority surfaces and adjacent non-touch evidence
- compare loaded index material against the visible discussion and focus argument
- turn relevant contradiction, ambiguity, and missing support into POIs without assuming a remedy
- distinguish what touched data, index presumption, and open inference each contribute
- do not preload the full index as a default runtime
- follow symlinks when traversing surfaces — index files, appendix pages, and whole skill trees are commonly symlinked in; use symlink-following tooling (e.g. `grep -R`, `find -L`) so linked surfaces are not silently skipped

## Search Steps

1. Identify the focus argument and the visible discussion context: concepts, claims, tensions, decisions, and open questions.
2. Read the relevant routing surfaces from the engaged depots.
3. Apply depot and chapter scope; default chapter is `design`, and widen only when the task, routed concept, or live discussion calls for it.
4. Identify the target concept or nearby related concepts.
5. Read the chapter file (`<chapter>/NNN-<chapter>.md`) that owns the routed concept.
6. Load appendix depth only when the block does not carry enough signal.
7. Read the top-relevant concept's agendix (`agendix/Concept.Name-agendix.md`) when it exists — unreviewed grounded leads, surfaced separately from accepted citations.
8. Load references only when the task needs operational detail or concrete examples.
9. Classify relevant line standing, surface POIs, compare the material against the visible discussion, and report what matters.

## Reading What You Find

- lines may carry a leading `Line.Type` code (`- [CT] ...`): the type is the line's act — `[CT]`/`[DC]`/`[RJ]` bind, `[PR]` orients, `[FR]` frees, `[DF]`/`[EX]` inform, `[GR]` cites evidence; see `references/type.md` to read them as constraints
- parser-backed tools read index surfaces as typed nodes: `RouterEntry` rows, `BlockHeading`s, `KernelLine`s, `MetaLine`s, code fences, and inline spans such as anchors, concept cites, type brackets, and file mentions
- untyped lines are pre-fence legacy — same authority, just not yet classified
- a trailing `^c<YYYYMMDD>-<N><tag>` token is the current `Support.Reference` realization: an `Anchory.Anchor` resolving to a Chatlas support set; see `references/link.md`
- appendix blocks named `Concept.X/Grounding.Head` and `Concept.X/Grounding.Drift` are inert legacy sections from the retired block-grounding scheme, not conceptual content; current grounding lives on the lines themselves (`Index.Line`)
- `agendix/` files are agent-captured, unreviewed material; grounded lines carry touched authority while any ungrounded live residue carries only index presumption

## Line Standing

- a grounded live line has a resolvable nonempty `Support.Set` and carries `Touched.Authority`
- an ungrounded live line remains relevant through weaker `Index.Presumption`; report missing grounding as debt
- a reviewed line has approval-protocol evidence, independently of whether its support is strong or factually correct
- a demoted line is historical evidence and does not condition current reasoning
- a contradiction does not demote a live line; it creates a POI until gated reconciliation changes the live cut

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
- `line-standing` — grounded authority, ungrounded presumption, or demoted history when that distinction changes the answer
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
- read agendix lines as unreviewed leads; verify their support before attributing touched authority
- keep them out of `supporting-citations`: report them under `agendix-leads` — a reviewed surface may not cite the agendix (`Reviewed.Cite.Closure`)
- before reporting `missing-index-coverage`, check the agendix — a lead already harvested there is promotion-ready, not missing
- when the pass actually leans on an agendix lead, recommend its promotion through `--edit` (gated) — use is the promotion signal

## Unresolved Names

- when a name appears unresolved, search nearby routed concepts first
- if the name remains unresolved, surface it as unresolved instead of inventing a concept
- repeated unresolved names are a capture signal, not a reason to guess

## Grounding Depth

- this module runs `Index.Grounding` as the first `Context.Grounding` level: enrich the agent's context with the `Touched.Index` digest of the topic
- next down the `User.Attention` gradient, read the concept's `Index.Agendix` — the last index-local rung: unreviewed touched leads already harvested from chat, cheaper than resolving anchors back out
- when the index-local rungs are not enough, escalate to full grounding: follow support references through their sets to the original `Touch.Authority.Surface`; inspect code and files independently as adjacent evidence
- where evidence leaves the answer unresolved, report the coherent provisional conclusion as `Open.Inference` rather than presenting it as touched truth
- do not pretend to ground against conversation state that is not actually visible in the current prompt or thread
- recommend `--edit` when the search pass reveals a likely needed block revision, new concept, line append, or appendix update
- keep the report continuation-oriented: make it easier to continue the work, not just easier to inspect the search
