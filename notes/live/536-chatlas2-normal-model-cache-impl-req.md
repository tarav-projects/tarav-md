# Chatlas2 Normal Model cache and streaming reads - impl-req

## Impl.Abstract

- **scope:** add a disposable compact Normal Model cache; identify freshness from the selected session, ordered transcript fingerprints, Normal Model schema, and producer commit; materialize metadata plus stream-readable event, message, and loaded-context collections; move exact-session message reads onto that cache; and bound multi-session model retention in the existing Anchory route
- **status:** implemented and verified; captured as recovery checkpoint `c2dd14f` before the transparent-provider follow-up
- **source:** the cache-first/read-streaming decisions captured in design session 527 and the explicit autonomous develop invocation in Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`
- **target:** Chatlas2 mechanics and tests in `tarav-py`, maintained Chatlas2 guidance, and this implementation audit trail
- **out of scope:** streaming normalization; constraining normalizer internals; caching raw-attached diagnostic models; cross-session search/index construction; bulk cache warming; cache eviction or historical cache retention; daemon integration; changing the Raw Archive or Normal Model schema
- **acceptance:** one exact-session read may build a compact cache; later reads stream from a fresh cache without normalizing; stale sources are detected; explicit cache build/status are inspectable; limits stop cached message reads early; Anchory retains at most one full cached model at a time; and all existing Codex, Claude, corpus, reference, and raw-diagnostic behavior remains valid

## Impl.Agendix

- **touched (authorization):** implement the captured `Normal.Model.Cache` design through the autonomous Hugentics develop route. ^d20260816-16u
- **touched (normalizer boundary):** normalizers may use any internal strategy needed to produce a complete model; cache mechanics do not constrain normalization ^d20260816-5u ^d20260816-6u
- **touched (cache identity):** cache identity and freshness use session identity, ordered source fingerprints, Normal Model schema, and producer commit ^d20260816-8u
- **touched (authority):** cached models are disposable, non-authoritative, and rebuildable from the retained Raw Archive ^d20260816-9u
- **touched (compactness):** ordinary caches contain only the default compact model; raw-attached diagnostic builds remain uncached ^d20260816-10u
- **touched (read policy):** exact-session reads may narrowly build their cache, but a future bulk read must not silently normalize missing or stale caches ^d20260816-11u ^d20260816-12u
- **touched (memory):** multi-session workflows consume and release one model at a time; read limits are applied during cached iteration ^d20260816-13u ^d20260816-14u
- **touched (accepted limit):** this layer does not remove a normalizer's first-build memory peak ^d20260816-15u
- **structural:** Chatlas2 may reuse current Chatlas archive/index/persistence mechanics, while current Chatlas must not import Chatlas2

## Impl.Index

### Cache identity and placement

- one cache belongs to one neutral Chatlas session identity and lives below a Chatlas2-specific cache root
- the current cache key hashes the session identity, ordered transcript source fingerprints, Normal Model schema version, and repository commit recorded by the producer
- each source fingerprint uses its resolved path, byte size, and nanosecond modification time; this is a cheap freshness detector rather than a second raw-content archive
- the session-addressed cache directory contains the current key in metadata and is atomically replaced when rebuilt; stale cache history is not retained
- missing, malformed metadata, incomplete file sets, or key-mismatched cache material reports non-fresh standing and is never repaired during a cache-only status read; malformed JSONL records fail when their stream is consumed

### Compact stream-readable representation

- `metadata.json` contains cache schema/key, the Normal Model envelope fields, ordered source fingerprints, and collection counts
- `events.jsonl` contains one complete Normal Event per line
- `chat-messages.jsonl` contains one message-read record per line: the complete `Chat.Message` plus its diagnostic derived `at`
- `agent-loaded-contexts.jsonl` contains one complete `Agent.Loaded.Context` annotation per line
- the materializer accepts only the compact default model and never writes the optional top-level `raw` channel
- a cache reader validates metadata once, then exposes independent iterators; a compatibility loader may reconstruct one complete Normal Model for consumers that still require it

### Read and creation policy

- explicit `cache build` normalizes one exact selected session and atomically replaces its cache
- `cache status` computes current freshness without normalizing or mutating storage
- one exact-session message or Anchory read uses a narrow load-or-build operation; a fresh cache is read without invoking a normalizer
- message list/find iterate only the cached message collection, filter while reading, and stop at an optional non-negative limit
- message output uses cached diagnostic `at` directly and preserves the existing support-member/reference shape
- the direct `normalize` command remains an uncached producer and continues to support `--include-raw`
- no bulk selector or multi-session API gains implicit cache production in this slice

### Bounded consumer lifetime

- the Anchory route reconstructs models from the compact cache only when its existing reference/neighborhood operations require a full model
- its shared operation-local model slot has capacity one; loading another session releases the previous model
- repeated access may reread a persistent cache rather than holding every participating session model in RAM
- this is a lifecycle bound, not a new global in-memory cache abstraction

## Execution.Plan

### Vertical.Slice 1 - Cache identity, materialization, and streaming reader

- add RED tests for the four-file representation, compact-only enforcement, fresh/missing/stale standing, exact metadata/key inputs, atomic replacement, independent JSONL iteration, and complete-model reconstruction
- implement a focused Chatlas2 cache module using existing persistence and locking mechanics where useful
- observable: a completed Normal Model can be materialized once and its collections consumed independently without loading the whole model
- check: focused cache, Codex, Claude, and model tests plus Ruff
- status: complete

### Vertical.Slice 2 - Exact-session CLI and message read path

- add RED tests for explicit cache build/status, automatic narrow creation by message reads, reuse without normalization, stale rebuild, streaming side/text filtering, and limit validation
- add the minimal CLI surface and move `messages list|find` from direct normalization to cached message iteration
- preserve member refs, diagnostic time, JSON shape, chronological order, and direct `normalize --include-raw`
- observable: repeated exact-session message lookup avoids normalization and can stop after a bounded number of matches
- check: focused CLI, cache, message, and end-to-end Anchory tests
- status: complete

### Vertical.Slice 3 - Anchory lifecycle bound, guidance, and system verification

- change the Anchory model loader to narrow load-or-build and replace its unbounded per-operation model dictionary with a one-model slot
- add behavioral coverage proving multi-session work never retains more than one reconstructed model while existing preview/register/batch/resolve behavior remains stable
- update `tarav-py/AGENTS.md` and `ARCHITECTURE.md` for the cache/read boundary and new CLI surface
- run the complete Chatlas2 suite, conformance verify/check, architecture tests, focused Ruff, repository tests proportionate to the change, and `git diff --check`
- observable: the first consumer path uses disposable persistent models while preserving all reference and grounding semantics
- status: complete

## Impl.Log

- **2026-08-16 — execution gate:** the autonomous develop invocation authorizes implementation of the cache/read design and is grounded as `^d20260816-16u`
- **2026-08-16 — inspected baseline:** every message and Anchory command currently rebuilds a complete Normal Model; Anchory additionally retains every loaded session model in an operation-wide dictionary
- **2026-08-16 — design boundary:** normalization stays a complete-model black box; optimization begins only after that model exists, and the direct raw-diagnostic normalization path remains uncached
- **2026-08-16 — representation decision:** use one metadata file plus three JSONL collections; cache message records duplicate only derived diagnostic time so support reads do not need an event index
- **2026-08-16 — checkpoint:** mandatory pre-edit recovery commit `0983c29` captured the complete prior `tarav-py` worktree; the finished cache slice was later captured as follow-up recovery checkpoint `c2dd14f`
- **2026-08-16 — slice 1:** added the session-addressed four-file cache, cheap path/size/mtime source fingerprints, schema/commit keying, atomic replacement under a per-session lock, compact-only validation, independent iterators, and one-model reconstruction
- **2026-08-16 — validation boundary:** `cache status` validates metadata, required files, and current key without scanning whole collections; malformed JSONL is rejected by the consuming iterator rather than turning a cheap freshness check into a full read
- **2026-08-16 — slice 2:** added explicit `tarav chatlas2 cache status|build`; exact-session `messages list|find` now load-or-build once, stream cached message records, preserve support refs and diagnostic time, and apply `--limit` during iteration
- **2026-08-16 — slice 3:** Anchory now reconstructs from the persistent cache only when needed and uses a capacity-one operation-local model slot; batch preview computes its plan directly so it never opens a redundant second model
- **2026-08-16 — live trial:** this session moved from `MISSING` to `FRESH` through one exact message read; the 5.1 MB cache holds 9,746 events, 442 messages, and 2,302 loaded contexts, and a repeated exact read left cache metadata unchanged
- **2026-08-16 — verification:** all 1,958 repository tests pass; the focused Chatlas2 plus architecture set passes 57 tests; all 21 conformance captures verify and normalize; focused Ruff and diff checks pass; project Skillware retains 30 pre-existing POIs and none target Chatlas2
