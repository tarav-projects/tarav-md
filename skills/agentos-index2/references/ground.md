# agentos-index2 --ground

Use this module when the caller wants the current prompt or ongoing conversation grounded against the index.

`--ground` is not a raw lookup alias. It is a conversation-to-index grounding pass.

## Grounding Model

- this pass runs `Index.Grounding` — the first `Context.Grounding` level: enrich the agent's context with the index's digest of the topic, read-only and ungated
- use `--search` behavior as the retrieval base: routing-first selective loading over the engaged depots, `--depot` and `--chapter` scoping (default chapter `design`), loading only task-relevant blocks
- when the digest is not enough, escalate to full grounding: follow the blocks' pointers out to the original surfaces — chat evidence via `agentos chatlas`, code and files directly
- distinguish what the index explicitly says from what the agent infers by comparing the conversation against the index

Prefer a compact grounding report over a long raw search dump.

## Citation Behavior

- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use concrete surface paths when they materially improve navigation or maintenance

## Grounding Report

Use a stable report shape when it helps:

- `relevant-concepts` — the most relevant concepts surfaced from the index
- `supporting-citations` — the blocks, appendix pages, or references that support the grounding
- `possible-contradictions` — tensions between the current discussion and the current index
- `significant-remarks` — accepted or high-signal observations worth carrying forward
