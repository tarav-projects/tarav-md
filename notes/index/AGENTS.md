# notes/index/ — Agent Instructions

- this surface is **read-only by default** for agents
- agents can read freely — the index is their primary grounding source
- agents can propose — suggest new concepts, flag gaps, draft blocks
- agents cannot trigger writes or commit content without explicit user approval

## Writing to the index

- writing requires two gates: `Write.Trigger.Gated` (user initiates) and `Content.Verbatim.Gated` (user approves exact wording)
- use the `agentos-index-writer` skill for all write operations
- each block gets individual attention — no bulk-approve
