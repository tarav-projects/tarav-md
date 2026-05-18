# Gating

## User.Gated.Index

- agents treat the index as read-only by default
- the index is the design authority — corrupting it corrupts everything downstream
- agent writes to the index are high-consequence because they change what future agents and humans will reason from

### Two gates

- `Write.Trigger.Gated` — the user must explicitly initiate write flows; the agent never starts writing on its own
- `Content.Verbatim.Gated` — the user must approve the exact wording of each block before it's committed

### Rules

- agents can **read** freely — the index is their primary grounding source
- agents can **propose** — suggest new concepts, flag gaps, draft blocks
- agents cannot **trigger writes** without explicit user initiation
- agents cannot **commit content** without user approval of exact wording
- the user is the quality gate for what earns a place in the index

This is fundamentally different from `Live.Notes`, where agents may write more freely. The index has a higher write bar precisely because it is the `Alignment.Surface`.

****

## Write Loop

The writer operates as an interactive alignment conversation, one block at a time:

```
User triggers write → agentos-index-writer activates

For each block to write/modify:
    1. Show proposed block (diff view for updates, full block for new)
    2. User reads, suggests changes
    3. Agent shows revised version
    4. Repeat until user accepts
    5. Move to next block

All accepted → commit to index
```

- each block gets individual attention — no bulk-approve
- the user always sees final form before anything touches the files
- the loop is an alignment opportunity — human and agent refine wording together
- handles: new concept registration, block creation, block updates, ontology registry entries
- write first, polish later — the write loop focuses on meaning alignment, not format enforcement
- linting happens later during maintenance passes (`agentos index doctor`), not during the write flow

****

## Unresolved.Index.Name

- `Unresolved.Index.Name` is the result when a name cannot be resolved against the loaded index and the concept is not clearly new
- the agent parks it in a session working list
- available for later resolution if more context emerges
- suggestion to the user if it keeps recurring
- explicit registration if the user confirms it's a new concept
- this is the "undefined variable" of the index — acknowledged but not yet resolved
