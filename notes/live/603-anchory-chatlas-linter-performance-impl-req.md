# Anchory and Chatlas Linter Performance - impl-req

## Impl.Abstract

- **scope:** remove repeated Anchory registry writes and provenance work, prune dead registry entries, isolate test registries, and make Chatlas identity lookup shard-aware with reusable command-lifetime RAM caches
- **status:** implemented and verified
- **source:** direct user request plus profiling of `agentos index linter --depot agentos-md/skills/agentos-pkg --skip line-unlinked --show-passed`
- **out of scope:** changing Index checks, POI semantics, Anchory record authority, Chatlas normal-model authority, or adding persistent derived caches

## Impl.Agendix

- **touched (chat):** the current `--dev --AUTO` request authorizes all four performance corrections
- **touched (index):** `Anchory.Depot.Registry`, `Chatlas.Session.Model`, and `Derived.Surface` constrain the registry and cache boundaries
- **structural:** the implementation extends existing Anchory registry/depot and Chatlas index-query surfaces
- **open space:** exact cache class names and capacity defaults remain implementation choices

## Impl.Index

### Anchory.Read.Runtime

- read operations register a depot at most once per runtime cache instead of rewriting the registry for every resolution
- registry writes prune entries whose depot roots no longer exist
- callers may share an in-memory resolution cache for a bounded operation
- depot mutations invalidate affected cached resolutions and refresh registry metadata

### Anchory.Test.Isolation

- automated tests use temporary Anchory registry and global-depot paths
- test-created depots never pollute the operator's global registry

### Index.Anchor.Provenance

- one linter run computes one provenance result per distinct anchor
- repeated source occurrences reuse that result while retaining occurrence-specific POI locations

### Chatlas.Index.Lookup

- identity-hash lookup reads only matching index shards
- a caller-owned RAM cache may reuse already-read partitions during one command
- a caller-owned support cache indexes each loaded session tape once for turn lookup
- selected rows and loaded session models continue to come from authoritative Chatlas JSON surfaces

## Execution.Plan

### Slice 1 - Anchory runtime and registry

- add explicit reusable runtime-cache capacity to `AnchoryDepot`
- make read-time registration idempotent within that cache
- prune missing roots during registry updates
- add RED/GREEN tests for one-touch behavior, cached resolution, mutation invalidation, and dead-entry pruning
- **observable:** repeated resolution performs no repeated registry write or shard read
- **status:** complete

### Slice 2 - Test registry isolation

- install temporary Anchory registry/global-depot fixtures in affected Python test suites
- **observable:** test depots do not appear in the operator registry
- **status:** complete

### Slice 3 - Chatlas shard-aware lookup

- add a caller-owned partition cache to the Chatlas index-store library
- narrow identity queries to the matching shard across eligible providers
- thread the cache through index query and single-row selection
- add RED/GREEN tests proving partition narrowing and reuse without changing query results
- **observable:** repeated identity selections read each matching partition at most once per cache
- **status:** complete

### Slice 4 - Index provenance integration and benchmark

- cache Anchory resolution and complete Chatlas provenance validation by distinct anchor during one grounding check
- share the Chatlas partition cache and session-model cache across the run
- run focused suites, full relevant suites, and benchmark the original linter command
- **acceptance:** behavior is unchanged and runtime is materially below the profiled 22-34 second baseline
- **status:** complete

## Impl.Log

- profiling found 1,087 resolution calls for 241 distinct anchors, 1,087 global registry rewrites, and 18 full 768-partition Chatlas index scans
- the operator registry contained 1,305 stale pytest depot entries; pruning and test isolation are therefore part of the performance fix
- implementation reduced the operator registry from 1,310 entries / 357,218 bytes to 20 live entries / 5,359 bytes
- the final target linter completed in 5.71 seconds and 6.46 seconds on consecutive verification runs, down from the 22-34 second baseline
- verification: `agentos-py` 590 tests pass; `agentos-chatlas-py` 270 tests pass; changed-file Ruff and formatting pass
- Chatlas repository-wide Ruff remains blocked by seven pre-existing findings in unrelated annotation, delta-scan, normalization, and freshness-test files
