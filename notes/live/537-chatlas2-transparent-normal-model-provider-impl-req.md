# Chatlas2 transparent Normal Model provider - impl-req

## Impl.Abstract

- **scope:** make cache validation and transparent recomputation the default Chatlas2 Normal Model access path; expose explicit refresh and uncached raw-diagnostic computation; route full-model and streaming consumers through one canonical provider boundary; and remove Anchory-specific cache loading and model-slot policy
- **status:** implemented and verified; implementation remains uncommitted after recovery checkpoint `c2dd14f`
- **source:** the cache-provider discussion and explicit autonomous develop invocation in Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`
- **target:** Chatlas2 provider, cache, CLI, Anchory, tests, and maintained guidance in `tarav-py`; this implementation audit trail in `tarav-chatlas-md`
- **out of scope:** streaming normalization; changing normalizer freedom; caching raw-attached models; bulk cache warming, eviction, or historical retention; changing the Raw Archive or Normal Model schema
- **acceptance:** ordinary consumers request Normal Model content without cache knowledge; a fresh cache is reused, a missing or stale cache is rebuilt transparently, refresh forces replacement, raw diagnostics bypass cache, and Anchory has no cache import, private cache loader, or model slot

## Impl.Agendix

- **touched (authorization):** make the cache-backed provider the transparent default for all Chatlas2 Normal Model consumers and remove Anchory-specific cache handling. ^d20260816-17u
- **structural:** normalizers remain unconstrained complete-model producers; the provider owns cache policy after production
- **structural:** Chatlas2 may reuse current Chatlas mechanics, while current Chatlas must not import Chatlas2

## Impl.Index

### Canonical access boundary

- one provider facade supplies complete Normal Models and stream-readable model content
- default access validates the session-addressed cache, rebuilds it when missing or stale, and returns content without exposing that decision to consumers
- refresh forces compact normalization and atomic cache replacement before returning content
- diagnostic computation with optional raw evidence runs the producer directly and never reads or writes the ordinary compact cache
- direct fragment normalization remains available to versioner/normalizer and hermetic corpus tests; it is production mechanics, not a session-consumer path

### Consumer boundary

- `normalize` uses default provider access unless refresh or raw-diagnostic behavior is explicitly requested
- message reads obtain their stream reader through the provider facade rather than importing cache mechanics
- Anchory requests a complete Normal Model through the same provider facade and owns no cache validation, cache loader, or model-retention slot
- explicit `cache status|build` remains the inspectable cache-administration surface

## Execution.Plan

### Vertical.Slice 1 - Provider modes

- add RED behavioral tests for fresh reuse, transparent missing/stale rebuild, forced refresh, and uncached raw diagnostics
- add the minimal provider facade over the existing producer and cache mechanics
- status: complete

### Vertical.Slice 2 - Consumer reconnection

- reconnect normalize and message reads through the provider facade
- remove Anchory's cache import, private loader, and `_ModelSlot`; preserve grounding and ref-resolution behavior
- status: complete

### Vertical.Slice 3 - Verification and guidance

- update Chatlas2 architecture and agent guidance
- run focused provider/cache/CLI/Anchory tests, full Chatlas2 and architecture tests, corpus checks, repository tests, Ruff, and diff checks
- status: complete

## Impl.Log

- **2026-08-16 — execution gate:** autonomous development is authorized and grounded as `^d20260816-17u`
- **2026-08-16 — baseline:** cache mechanics are complete, but normalize bypasses them, messages import them directly, and Anchory owns a cache loader plus capacity-one model slot
- **2026-08-16 — checkpoint:** recovery commit `c2dd14f` captured the complete preceding cache implementation before provider edits began
- **2026-08-16 — provider:** added one facade returning either a complete model or stream reader; default access opens/rebuilds transparently, refresh forces materialization, and direct diagnostic computation bypasses cache
- **2026-08-16 — consumers:** `normalize` and message reads now use the provider; Anchory imports only the complete-model provider and no longer has `_ModelSlot`, `_load_model`, or a cache import
- **2026-08-16 — live trial:** this session moved from `STALE` to `FRESH` through default normalization; a second default read preserved metadata inode `152752682`, while `--refresh` replaced it with inode `152752922`; all paths returned 10,223 events, 456 messages, and 2,422 loaded contexts
- **2026-08-16 — verification:** all 1,962 repository tests pass; focused Chatlas2 plus architecture coverage passes 61 tests; all 21 conformance captures verify and normalize; Ruff and diff checks pass; Skillware reports 30 pre-existing POIs and none target Chatlas2
