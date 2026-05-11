# Index Migration — 2026-05-11

Migration session notes for the `Agentos.Index` rebuild.
Protocol: `517-index-migration-protocol.md`

---

## Index.Block.Findability

- `Index.Block.Findability` is a field in the `### index` section of an `Index.Block`
- populated only when there is evidence of search misses — not as a summary of the block content
- typical evidence: the user calls the block using an unexpected context or name
- during initial block creation, findability should be empty by default
- the block body itself is the primary search surface — findability is a supplementary hint for known gaps
