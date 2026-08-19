# Bloberia As The General Record Store - impl-req

## Impl.Abstract

- **Status:** Open. Designed, not executed.
- **Intent:** Rebuild `bloberia` as the general keyed-record store, able to host anchory dossiers and index records without knowing what either means.
- **Source:** the design session in this chat. `bloberia` already existed — *"depot-scoped query:value storage for agent-associated data"* — with namespaces, locking and subset queries. This is a reshaping of it, not a new subsystem.
- **Scope:** `tarav/bloberia/` core and CLI, its existing consumers, and in-flight tests proving both record shapes fit.
- **Out of scope:** migrating any data. Anchory and the index keep their own stores; this run only proves bloberia can host them.
- **Grounding:** none minted. The index freeze (`638` Invariant 1) is in force.
- **Acceptance:** a depot round-trips a real anchory dossier and a real index record, verbatim, and answers path queries over both. Suite green.

## Why This Exists

Four keyed-record stores exist: `anchory/`, `bloberia/`, `.tarav/index/`, `.tarav/state/`. Each writes JSON atomically through `_core.persistence` and then reinvents naming, locking, sharding and query. The duplication is not schema — it is plumbing.

The recurring question was never *which storage technology*. It was **placement** and **who owns identity**. Bloberia answers both by refusing to answer either: the cargo is opaque, and the root is the caller's choice.

## Impl.Index

### Bloberia.Contract

- [DF] `Bloberia.Record` is the consumer's cargo, stored verbatim. There is no envelope: no id, no timestamps, no revision, no `value` wrapper.
- [CT] Bloberia never inspects cargo except at the paths a query names. Uniqueness, schema, collisions and meaning are consumer concerns.
- [DC] Arity belongs to the call, not to configuration: `first(query)` returns one match, `all(query)` returns every match. Nothing is declared and nothing is enforced.
- [RJ] No configured primary key as a contract. A declared index is a cache hint only — addable, removable and repointable with no consequence for any consumer.
- [DC] The storage filename is bloberia's private business. No consumer computes it, parses it, or holds it as a reference.
- [PR] Refusing to model cargo is what lets one store serve consumers whose schemas move independently. A store that understands its cargo acquires a stake in every consumer's schema change.

### Depot.Type

- [DF] A `Depot.Type` is one storage topology under the shared contract — the way a library offers arrays, dicts and queues rather than one container.
- [DC] The type belongs to the depot, is chosen at creation and recorded in its meta. A depot never mixes types.
- [DC] The first and only type in this run is `files`: one JSON document per record.
- [PR] Types stay substitutable only if the contract is fixed while implementations vary, so the API is settled now even though one type exists.
- [EX] The failure mode is already demonstrated: two migration scripts in this project reimplemented anchory's 2-hex sharding because the layout leaked, which would have made anchory's storage unchangeable.

### Query.Model

- [DF] A query names paths inside the cargo with `equals`, `contains` and `exists`, and bloberia iterates and matches.
- [RJ] Regex is not a first-round predicate. It is the one operator no index or prescan can serve, so admitting it now would guarantee a fast path and a slow path that diverge.
- [PR] `contains` and `equals` are exactly the predicates `Scan.Decode.Verify` was designed to escalate through — cheap textual prescan, decode only candidates, verify against the parsed object.

### Index.Cache

- [DF] A declared index maps one cargo path to the records carrying each value, so a common lookup skips the scan.
- [CT] An index is derived and disposable: droppable at any moment and rebuildable by full scan, exactly as `527` requires of a Normal Model cache.
- [DC] Staleness is detected, never assumed — an index carries a fingerprint of the depot state it was built from and rebuilds on mismatch.

### Placement

- [DF] A depot is rooted at an explicit directory, so placement is the caller's decision rather than bloberia's.
- [DC] The global public depot is `~/Documents/bloberia`, beside `~/Documents/chatlas`: an important system gets its own public depot rather than hiding under a dotfile.
- [DC] The index keeps its records at project tier, git-tracked in the repo, because a grounding change must appear in a diff a human reviews.
- [PR] Placement legitimately differs per consumer — audience and lifetime differ — which is why one store must not impose one location.

## Execution.Plan

### Slice 1 — The contract, over the `files` type
Rewrite `bloberia/core.py`: opaque cargo, `insert` / `first` / `all` / `count` / `replace` / `delete` / `iterate`, path queries with `equals` / `contains` / `exists`, depot meta carrying `type` and declared indexes.
**Check:** RED-then-GREEN on a depot that stores a dict bloberia has never seen and returns it byte-identical.

### Slice 2 — Host both real shapes
In-flight tests using a real anchory dossier and a real index record as cargo.
**Check:** each round-trips verbatim; `first({"line.label": ...})` finds the index record; `first({"relationships.support.members.0.session": ...})` finds the dossier. No bloberia code names either schema.

### Slice 3 — Declared indexes
Sidecar index per declared path, fingerprinted, rebuilt on mismatch.
**Check:** results are identical with and without the index; dropping the sidecar changes nothing but speed.

### Slice 4 — Move the existing consumers
`tournament/store.py`, `skillware/edition_history.py`, `poi/adapters/bloberia.py`.
Their stored files already parse as cargo — the old envelope simply becomes opaque content, and their `{"value": …}` queries keep matching. Only `create()`'s minted id must move consumer-side.
**Check:** the 9 live edition-history records still read; suite green.

### Slice 5 — Git handler *(deferred unless slices 1–4 land early)*
Write-triggered, interval-based checkpoint commit, one repo per depot, configurable, off by default.
**Check:** a git failure never fails a write.

## Slice Status

| # | Slice | Status |
|---|---|---|
| 1 | contract over the `files` type | not started |
| 2 | host anchory + index shapes | not started |
| 3 | declared indexes | not started |
| 4 | move existing consumers | not started |
| 5 | git handler | deferred |

## Impl.Log

- **Resolved by reading the code, not by asking.** Whether two records ever need to land atomically was raised four times in design. `IndexStore.by_trace` is `[r for r in self.all() if r.trace == trace_id]` — a trace is derived by scan, not a stored record, and `put` writes exactly one. No batch primitive is needed for this consumer, so the contract stays at single-record verbs.
- **Measured:** bloberia is 623 lines with five consumers and 9 live records under `tarav-py/.tarav/state/bloberia`. Small enough to reshape in place.
- **`Index.Presumption`:** existing stored records are assumed to survive the envelope removal because the old envelope parses as ordinary cargo and consumer queries address `value.*`, which stays a valid path. Verified by reading the query code, not by running it.
- **Design correction during the run:** the global depot was going to be `~/.tarav/records/`; the user moved it to `~/Documents/bloberia` so an important system carries its own public depot like chatlas. Recorded because it changes placement, not mechanism.
- **Waiver:** no anchors minted and no backpropagation attempted, per the index freeze.
