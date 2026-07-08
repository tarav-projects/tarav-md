# agentos-index --ground

Use this module when the caller wants the current prompt or ongoing conversation grounded against the index.

`--ground` is not a raw lookup alias. It is a conversation-to-index grounding pass.

## Grounding Levels

- this module runs `Index.Grounding` — the first `Context.Grounding` level: enrich the agent's context with the index's digest of the topic
- when the digest is not enough, escalate to full grounding: follow the blocks' anchors out to the original surfaces — chat evidence via `references/link.md` resolution (anchory + chatlas), code and files directly
- grounding is read-only and ungated — it changes the agent's context, never a surface

## Grounding Goal

- derive the active concepts, claims, tensions, and decisions from the live discussion
- check the relevant index surfaces for matching or related concepts
- make the relationship between the conversation and the index explicit
- surface contradictions, gaps, and significant remarks worth carrying forward

## Grounding Model

- use `--search` behavior as the retrieval base: depot-scoped routing, chapter-scoped selective loading, citations, and appendix depth only when needed
- respect `--depot` as the engaged depot scope; otherwise use task-relevant engaged depots
- respect `--chapter` as the first grounding scope inside engaged depots; default to `design`, and widen when the conversation needs another chapter
- do not pretend to ground against conversation state that is not actually visible in the current prompt or thread
- distinguish what the index explicitly says from what the agent infers by comparing the conversation against the index
- prefer a compact grounding report over a long raw search dump

## Grounding Steps

1. Identify the main concepts, claims, decisions, and tensions in the current prompt or ongoing discussion.
2. Derive a focused search frame from that live context.
3. Read the relevant routing surfaces and load only the most relevant concept blocks, appendix pages, or references under the active depot and chapter scope.
4. Compare the loaded index material against the live discussion.
5. Return a compact grounding report with citations.

## Grounding Report

Use a stable report shape when it helps:

- `relevant-concepts` — the most relevant concepts surfaced from the index
- `supporting-citations` — the blocks, appendix pages, or references that support the grounding
- `possible-contradictions` — tensions between the current discussion and the current index
- `significant-remarks` — accepted or high-signal observations from the discussion that matter for continuation
- `missing-index-coverage` — meaningful conversation content that appears not to be modeled yet
- `recommended-next-index-action` — the single best next move from the index perspective

## Grounding Behavior

- surface related concepts, not just exact-name matches
- call out unresolved names instead of inventing concepts
- treat repeated missing or contradictory discussion as an index-maintenance signal
- recommend `--edit` when the grounding pass reveals a likely needed block revision, new concept, line append, or appendix update
- keep the report continuation-oriented: make it easier to continue the work, not just easier to inspect the search
