# Anchory Read Surfaces - impl-req

## Impl.Abstract

- **scope:** add `AnchoryDepot.exists`, `AnchoryDepot.anchors`, and their `agentos anchory exists/anchors` CLI surfaces
- **status:** ready for implementation
- **source:** user-requested follow-up to `notes/live/564-anchory-system-impl-req.md`
- **current state:** Anchory supports exact record resolution and record-bearing prefix queries through the library and CLI
- **out of scope:** storage format changes, namespace support, record query changes, Chatlas integration changes, and anchor allocation

## Impl.Index

### Anchory.Exists.Surface

- `AnchoryDepot.exists(anchor)` returns whether the exact anchor exists in the selected depot
- it applies the same non-empty anchor validation and shared-lock read boundary as `resolve`
- an absent anchor returns `False`; absence is not an error
- an existing anchor with an empty record still returns `True`
- corrupt storage remains an error rather than being reported as absence

### Anchory.Anchors.Surface

- `AnchoryDepot.anchors(prefix=None)` returns only anchor keys
- keys use the same deterministic sorting and prefix semantics as `query`
- the return type is `tuple[str, ...]`
- the initial implementation composes over `query` to avoid a second scan contract
- record values are not exposed by this surface

### Anchory.Read.CLI

- `agentos anchory exists --depot <path> --anchor <key>` emits `depot`, `anchor`, and `exists`
- `exists` exits `0` for both present and absent anchors because both are valid boolean results
- `agentos anchory anchors --depot <path> [--prefix <text>]` emits `depot`, `count`, and `anchors`
- both commands emit deterministic JSON and use the existing library methods
- existing `resolve` and `query` behavior remains unchanged
- `agentos-py/AGENTS.md` must include existence and key-listing in the documented Anchory surface

## Execution.Plan

### Slice 1 - Library read surfaces

- add behavior tests for exact existence, empty records, missing anchors, deterministic anchor listing, and prefix filtering
- path: `AnchoryDepot` public API -> existing validation and shared-lock reads -> boolean or key tuple
- RED: `exists` and `anchors` are unavailable
- GREEN: both methods satisfy their contracts without changing stored files
- check: `cd agentos-py && uv run pytest tests/test_anchory.py`
- status: not started

### Slice 2 - CLI read surfaces

- add end-to-end tests and register `exists` and `anchors` under `agentos anchory`
- path: umbrella CLI -> Anchory command handler -> new public library read surface -> deterministic JSON
- RED: both command names are rejected by the parser
- GREEN: true/false existence and filtered/unfiltered key listing return the specified payloads and exit codes
- check: `cd agentos-cli && uv run pytest tests/test_e2e_anchory.py`
- check: reinstall with `uv tool install --reinstall --editable .`, then inspect both command help surfaces
- status: not started

## Acceptance.Signals

- `exists` distinguishes an empty record from a missing anchor
- `exists` returns `False` without raising for a valid missing key
- `anchors` returns sorted keys without records
- `anchors(prefix=...)` matches existing `query(prefix=...)` selection
- both CLI commands require an explicit depot
- CLI output is deterministic JSON
- focused tests and Ruff pass in both touched repositories

## Deviation.Triggers

- stop if implementing either surface requires a storage format change
- stop if CLI absence semantics need a nonzero exit code
- stop if key listing needs pagination or record predicates in this request

## Impl.Log

- 2026-07-06: follow-up implementation request created; execution has not started
