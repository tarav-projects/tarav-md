# Bloberia As The General Record Store - impl-req

## Impl.Abstract

- **Status:** Open. Slices 1–2 and 4 executed; 3 and 5–9 open.
- **Intent:** Rebuild `bloberia` as the general keyed-record store, able to host anchory dossiers and index records without knowing what either means.
- **Source:** the design session in this chat. `bloberia` already existed — *"depot-scoped query:value storage for agent-associated data"* — with namespaces, locking and subset queries. This is a reshaping of it, not a new subsystem.
- **Scope:** `tarav/bloberia/` core and CLI, its existing consumers, and the index as its first real consumer — including retiring anchory into it.
- **Out of scope:** nothing is migrated before slice 4 lands. Slices 1–3 only prove bloberia can host both shapes; the data moves from slice 7.
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
- [DC] `files` is the fully opaque type: one JSON document per record, demanding nothing of cargo.
- [DC] `shards` is the second type, taken from anchory's 2-hex design: many records per file, keyed by a declared cargo path. It exists because 3,956 records under `files` means 3,956 opens per scan.
- [CT] A type may add semantics of its own. Opacity is the `files` contract, not a property of bloberia as a whole — a consumer choosing `shards` opts into its terms, and a missing shard key is a loud failure rather than a silent one.
- [DC] Type-specific demands are depot configuration, declared at creation and recorded in meta; nothing is inferred from cargo.
- [PR] Types stay substitutable only if the shared contract is fixed while implementations vary, so the API is settled now even though the type set grows.
- [EX] The failure mode is already demonstrated: two migration scripts in this project reimplemented anchory's 2-hex sharding because the layout leaked, which would have made anchory's storage unchangeable.

### Depot.Boundary

- [DF] a `Bloberia.Depot` is one directory owning a `meta.json`, a `records/` tree, one lock and one git configuration.
- [RJ] `~/Documents/bloberia` is a depot *root* holding many depots, not itself a depot. The three things that define the boundary — type, history, lock — are all per-depot, so the boundary cannot sit above them.
- [DC] a `Namespace` is placement inside a depot: same type, same history, same lock. The deciding question is whether the material needs its own storage type, its own history, or its own lifetime; if not, it is a namespace.
- [DC] the git configuration is one path to the repo the depot's records live in, absolute or relative to `meta.json`. A depot may own its repo or sit inside one that already tracks it.
- [DC] a depot may own its repo or be tracked by an enclosing one; the index depot owns its own, because it lives user-side outside every project repo.
- [EX] the enclosing-repo case is real all the same: a depot placed inside a project must not nest a second `.git/` under it.

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
- [DC] The public depot root is `~/Documents/bloberia`, beside `~/Documents/chatlas`: an important system gets its own public home rather than hiding under a dotfile.
- [DC] Every index record lives **user-side**, in one depot under `~/Documents/bloberia`. No index record is project-tier.
- [PR] A record's support points at chat evidence held in `~/Documents/chatlas`, which cannot ship with a project. Project-tier records would travel to a clone whose grounding resolves to nothing — storing them user-side does not create that problem, it stops pretending it is not there.
- [CT] Reviewability survives the move: the user depot is its own repo, so a grounding change is still a diff. What is given up is atomicity with the markdown line, which two repos could never have enforced.
- [PR] Placement legitimately differs per consumer — audience and lifetime differ — which is why one store must not impose one location.

### Index.Consumer

- [DF] The index is bloberia's first real consumer, and the thing that proves the design: one depot holds every index record, and anchory is retired into it.
- [DC] Anchory is obsolete as a *design*, not as data. It holds 3,956 dossiers — essentially the whole grounding corpus — against 51 records that have made the trip. `index/record/store.py` already declares the merge in its own docstring; only the data is outstanding.
- [DC] The two shapes merge into one. `dossier: {app, attachment, relationships, schema}` and `record: {id, line, scope, trace, links, equivalence, schema}` describe the same fact through two generations; `LineRecord` is the survivor.
- [DC] Anchory's storage design survives its subsystem: the 2-hex shard becomes the `shards` depot type rather than being reimplemented a third time.
- [DC] The two-tier logic dies with the move. `roots()`, tier moves in `put()` and `tier=` on every write all go; projects stay distinguishable because `scope.address` is already cargo, so it is a query rather than a namespace.
- [RJ] Records keep their own identity: the index resolves through `line.label` and takes no `Record.Coordinate`.

### Stable.Reference

- [DF] a `Record.Coordinate` is `commit + file + path-in-file` — the full position of a value in git history, and the stable link the whole subsystem exists to provide.
- [DC] it is derived on request, never allocated: bloberia stores no mapping and mints no id, so the reference costs no state and touches no cargo.
- [DC] it is read-side — obtained by asking about a record already in hand — so writing is unchanged and arity stays at the call.
- [CT] an uncommitted record has no coordinate. Bloberia reports its absence and never fires a commit to manufacture one.
- [DC] the path addresses sub-values, so a coordinate links to a piece of a record as readily as to the whole.
- [PR] git preserves each commit's tree as it was, so a coordinate keeps resolving across any later change of storage topology. The private layout and the permanent reference turn out to be compatible rather than opposed.
- [RJ] no bloberia-minted record id. A consumer that already has identity uses it: the index resolves through `line.label` and takes no coordinate.
- [DC] `Stable.Surface` is a property of the surface a consumer builds, not a tier bloberia grants. A depot holding scratch and a depot holding index records differ in what the consumer promises, not in what the store does.

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
`tournament/store.py`, `skillware/edition_history.py`, `skillware/commands.py`, `poi/adapters/bloberia.py`, `bloberia/commands.py`.
Their stored files already parse as cargo — the old envelope simply becomes opaque content, and their `{"value": …}` queries keep matching. Only `create()`'s minted id must move consumer-side.
**Check:** the 9 live edition-history records still read; suite green.

### Slice 5 — Git handler
Write-triggered, interval-based checkpoint commit. The depot's git configuration is one path to its repo, absolute or relative to `meta.json` — kept deliberately simple in this round.
**Check:** a git failure never fails a write; a depot tracked by an enclosing repo never nests one of its own.

### Slice 6 — The `shards` depot type
Many records per file under a declared cargo path, carrying anchory's 2-hex design forward.
**Check:** the same query returns identical results under `files` and `shards`; a cargo missing the declared key fails loudly on insert.

### Slice 7 — Anchory → `LineRecord`
Merge the two shapes and convert 3,956 dossiers, retiring the anchory subsystem and its 22 importers.
**Check:** every `^c…` cited on a live surface resolves to a record; a zero-result scan for the dossier shape.

### Slice 8 — The index on bloberia, user-side
One depot for every index record; two-tier logic removed.
**Check:** the linter passes against the depot; no record is written project-tier.

### Slice 9 — `Record.Coordinate`
Derive `commit + file + path` for a record in hand, and resolve one back to its value.
**Check:** a coordinate taken before the record is rewritten still resolves to the original value; an uncommitted record yields none.

## Slice Status

| # | Slice | Status |
|---|---|---|
| 1 | contract over the `files` type | **done** |
| 2 | host anchory + index shapes | **done** |
| 3 | declared indexes | not started |
| 4 | move existing consumers | **done** |
| 5 | git handler | not started |
| 6 | `shards` depot type | not started |
| 7 | anchory → `LineRecord` | not started |
| 8 | index on bloberia, user-side | not started |
| 9 | `Record.Coordinate` | not started |

## Impl.Log

- **Resolved by reading the code, not by asking.** Whether two records ever need to land atomically was raised four times in design. `IndexStore.by_trace` is `[r for r in self.all() if r.trace == trace_id]` — a trace is derived by scan, not a stored record, and `put` writes exactly one. No batch primitive is needed for this consumer, so the contract stays at single-record verbs.
- **Measured:** bloberia is 623 lines with five consumers and 9 live records under `tarav-py/.tarav/state/bloberia`. Small enough to reshape in place.
- **`Index.Presumption`:** existing stored records are assumed to survive the envelope removal because the old envelope parses as ordinary cargo and consumer queries address `value.*`, which stays a valid path. Verified by reading the query code, not by running it.
- **Design correction during the run:** the global depot was going to be `~/.tarav/records/`; the user moved it to `~/Documents/bloberia` so an important system carries its own public depot like chatlas. Recorded because it changes placement, not mechanism.
- **Executed 2026-08-19.** New `bloberia/core.py`: opaque cargo, `insert`/`first`/`all`/`count`/`replace`/`delete`/`iterate`, path queries with `equals`/`contains`/`exists`, namespace placement. 20 new tests, full suite 2074 green, ruff clean.
- **Deviation — slice 4 staged rather than done.** Rewriting the core broke 22 test modules across `tournament`, `skillware.edition_history` and the POI adapter, which all read the old envelope. Rather than leave the tree red or rush three consumer refactors, the previous depot is retained verbatim as `bloberia/depot_v1.py` and those consumers point at it. This is deliberate transitional debt, not a compatibility layer: nothing new may import it, and slice 4 deletes it. Named here so it is a reviewable change of its own rather than a rider on the rewrite.
- **The opacity claim is asserted, not trusted.** A test parses `core.py`, strips every docstring, and fails if executable code names `dossier`, `anchor`, `grounding`, `trace`, `triplet`, `session` or `label`. The first version of that test read raw source and failed on prose in my own docstrings — a comment citing a motivating example couples nothing, so the check was made precise rather than relaxed.
- **Design session 2026-08-20 — the reference system.** Two proposals of mine died in it, recorded because the survivors are shaped by their absence. I proposed a bloberia-minted opaque *handle* returned by `insert()`; the user had already ruled the direction out (*"file name is opaque to bloberia consumers and should not be used by default as id or reference pointer"*) and never adopted it. The coordinate replaces it on a sharper principle: **derived, not allocated** — a coordinate is already fully determined by where the record sits, so it needs no allocator and no stored mapping. I then proposed that asking for a coordinate should force a checkpoint commit; the user rejected it — an uncommitted record simply has no coordinate, and manufacturing one is the store inventing a fact.
- **Correction — `Stable.Surface` misread.** I read `107-design.md`'s *"agent-authored wording, not a `Stable.Surface` — nothing may link into it"* as a general bar on linking to agent-authored data, and reported a tension with git-tracked records. In its block it is a rung of `Capture.Gradient` governed by `Reviewed.Cite.Closure` — a directional citation rule between index surfaces, about *wording*, as the next line states outright (*"the gate buys wording stability, not touched authority"*). It says nothing about record stores. The user's correction was the general one: **read lines in the context of their block.**
- **What stability actually is.** Having dependents is the test that rules out `Volatile.Surface` (*"the defining property is having no dependents, not having a short life"*); it does not confer stability. Stability is the commitment that the system will maintain and improve the surface. `Touched.Index` is one `Stable.Surface` distributed across three stores — chat support in Chatlas, the linking network in bloberia, the readable interface in the project — which makes `Internal.Alignment` a cross-store concern rather than a per-file one.
- **Reversal — index records move user-side.** This doc originally recorded the opposite: *"The index keeps its records at project tier, git-tracked in the repo, because a grounding change must appear in a diff a human reviews."* The user reversed it on a point that argument missed — grounding resolves against chat evidence in `~/Documents/chatlas`, which never ships, so project-tier records would reach a clone as dangling references. Reviewability is unaffected; only line-and-grounding atomicity is given up, and two repos could not have provided it.
- **Correction — opacity is the `files` contract, not bloberia's.** I treated "bloberia refuses cargo knowledge" as universal and called a sharded type a violation. The user's model is per-type: a `Depot.Type` may add semantics, and a consumer choosing that type opts into them. That is what makes anchory's 2-hex design reusable instead of discarded.
- **Anchory is obsolete as a design, not as data.** The question *"why do we need anchory for?"* has a sharp answer: as a mechanism, we do not — but it holds 3,956 dossiers against the index's 51 records, so it is currently the grounding corpus. Retiring it is a data merge, not a deletion.
- **Slice 4 executed 2026-08-20.** `depot_v1` is deleted; five modules and five test modules moved. Each consumer now owns the envelope the store used to impose: `tournament` mints a `record_id` into verdict cargo, `edition_history` carries `record_id` + `revision` in a `_StoredRecord` of its own. The 9 live edition-history records were rewritten from `{_bloberia: {...}, value: {...}}` to the service's own shape and re-read clean. Suite 2057 green, ruff clean.
- **`check()` lost three of its four findings, by the deletion test.** `invalid-record-filename`, `invalid-record` and `identity-mismatch` each inspected a structure the contract removed — a meaningful filename, an envelope, a store-owned id. Only `invalid-json` describes an invariant bloberia still owns. The POI classes `Bloberia.Linter/Record.Filename.Invalid`, `/Record.Invalid` and `/Identity.Mismatch` retire with them, in `102-poi.md` and the `000-INDEX.md` route.
- **`get --id` and `edit --id` left the CLI rather than being reimplemented.** An id flag could only address a record through the private filename, which is the one handle the contract withholds. Both return as queries; a query matching nothing is now an ordinary result rather than a distinct not-found error.
- **Defect found by the port: nested namespaces were lost in slice 1.** The rewritten `_validate_namespace` rejected any `/`, silently narrowing a contract the retired suite had guarded (`a/b/c` addressable as `a`). Caught only because the surviving constraints were ported rather than dropped. Fixed by validating each segment — `..` and a leading dot are the two ways a prefix becomes a re-rooting — and `namespaces()` restored to listing every prefix, since `a/b/c` is readable as `a` too.
- **Waiver:** no anchors minted and no backpropagation attempted, per the index freeze.
