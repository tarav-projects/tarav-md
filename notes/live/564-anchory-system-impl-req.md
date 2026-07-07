# Anchory System - impl-req

## Impl.Abstract

- **scope:** implement the first Anchory core library in `agentos-py`, expose `agentos anchory ...` through `agentos-cli`, and prove the application boundary with a Chatlas depot adapter
- **status:** implementation complete; awaiting review
- **source:** `skills/agentos-pkg/design/107-design.md` (`Anchory.System`) and `skills/agentos-pkg/appendix/Anchory.System-appendix.md`
- **current state:** no Anchory code or CLI exists; `agentos-py` owns foundation libraries, `agentos-cli` aggregates command registration, and `agentos-chatlas-py` already resolves a Chatlas root
- **out of scope:** automatic anchor allocation, Chatlas record semantics, Chatlas command integration, `Chat.Ref` migration, namespace selection, delete operations, and application Git workflows
- **verification:** 268 `agentos-py`, 52 `agentos-cli`, and 140 `agentos-chatlas-py` tests pass; Ruff passes on every touched Python file

## Impl.Index

### Anchory.Package.Boundary

- core implementation lives under `agentos-py/src/agentos/anchory/`
- the public module is a small depot-scoped library interface
- `agentos-cli` only imports and registers Anchory commands
- Chatlas depends on the public library rather than Anchory depending on Chatlas
- no Anchory module imports Git behavior
- `agentos-py/AGENTS.md` must gain the new subsystem and CLI surface because its local guidance requires architecture changes to remain documented

### Anchory.Data.Model

- `AnchoryDepot` represents one exact Anchory root, such as `<chatlas-root>/anchory`
- `AnchoryRecord` is an application-owned JSON object
- `AnchoryEntry` pairs an anchor string with its record for query and CLI results
- the anchor exists only as the dictionary key; it is not duplicated inside the record
- Anchory adds no timestamps, application type, Git metadata, or application-specific fields to records
- the initial implementation accepts caller-supplied non-empty anchor strings
- namespace selection is not public API; every operation uses the constant namespace `global`

### Anchory.Storage.Format

- the logical `global` dictionary is physically sharded under `<anchory-depot>/global/`
- shard selection is `sha256(anchor UTF-8).hexdigest()[:2]`
- each `<shard>.json` is a direct JSON object mapping anchor strings to `AnchoryRecord` objects
- keys are sorted and files are pretty-printed with a terminal newline for deterministic diffs
- empty depots and absent shards read as empty dictionaries
- directories and shard files are created lazily on the first registration
- arbitrary anchor text never becomes a path component
- the first format has no manifest; the `global/` path is the format boundary and future migrations must be explicit

### Anchory.Mutation.Contract

- `AnchoryDepot.register(anchor, record)` creates a missing entry and rejects reuse
- `AnchoryDepot.resolve(anchor)` returns the record or `None`
- `AnchoryDepot.amend(anchor, record)` replaces an existing record and rejects a missing anchor
- `AnchoryDepot.query(prefix=None)` returns deterministic anchor-sorted entries
- `AnchoryDepot.check()` reports malformed shards, invalid record values, and keys filed in the wrong shard
- there is no generic set, upsert, or delete operation
- application code and agents must not mutate Anchory files directly
- library exceptions distinguish invalid input, duplicate anchors, missing anchors, and corrupt depots

### Anchory.Persistence.Safety

- a persistent lock file inside the depot coordinates all library access
- reads use a shared `fcntl.flock`; mutations use an exclusive lock
- mutations perform read-modify-write while holding the exclusive lock
- shard writes use a temporary file in the shard directory followed by `os.replace`
- malformed existing data aborts the operation without rewriting it
- the library cleans temporary files on failure
- Git tracking and lock-file ignore policy belong to the application owning the depot
- Unix advisory locking matches existing `agentos-py` use; cross-platform locking is out of scope unless repository support requirements change

### Anchory.CLI.Surface

- the CLI exposes `register`, `resolve`, `query`, `amend`, and `check` under `agentos anchory`
- every command requires an explicit `--depot` path to the exact Anchory root
- record mutations accept `--record-json` or `--record-file` through the existing JSON input helper
- command output is deterministic JSON suitable for agent and program consumption
- command handlers translate library failures into the existing `CliError` boundary
- the CLI exposes no namespace flag in the first implementation

### Chatlas.Anchory.Boundary

- `agentos-chatlas-py` exposes one helper that resolves `<chatlas-root>/anchory` as an `AnchoryDepot`
- an explicit Chatlas root and the current default Chatlas root produce the same path semantics used by existing Chatlas operations
- no chat record schema or anchor allocation policy enters the core implementation
- no existing Chatlas query behavior changes in this request

## Execution.Plan

### Slice 1 - Core dictionary and exact resolution

- add the Anchory package, public data types, validation errors, shard selection, and `AnchoryDepot.register/resolve`
- path: caller-provided depot -> `global/<hash-prefix>.json` -> anchor dictionary -> opaque record
- RED: behavior tests show registration is unavailable and exact resolution cannot round-trip a JSON record
- GREEN: registration creates the expected shard and a fresh `AnchoryDepot` resolves the identical record
- check: `cd agentos-py && uv run pytest tests/test_anchory.py`
- status: complete

### Slice 2 - Safe mutation and immutable identity

- add shared/exclusive depot locking, atomic shard replacement, duplicate rejection, and amend-only replacement
- path: two writers -> depot lock -> shard read-modify-write -> atomic replace
- RED: concurrent registrations targeting one shard lose data or allow duplicate reuse
- GREEN: both distinct records survive, duplicate registration fails without file changes, amendment requires an existing anchor, and interrupted writes leave valid JSON
- check: focused multiprocessing behavior tests in `tests/test_anchory.py`
- status: complete

### Slice 3 - Query and structural checking

- add deterministic prefix query and depot validation
- path: depot shards -> validated dictionary entries -> sorted `AnchoryEntry` results or structured findings
- RED: cross-shard lookup order, misplaced keys, malformed JSON, and non-object records are not handled consistently
- GREEN: query is deterministic and `check()` reports each structural failure without mutating the depot
- check: focused query and corruption tests in `agentos-py`
- status: complete

### Slice 4 - Umbrella CLI

- add `agentos.anchory.commands`, register it in `agentos-cli`, and document the subsystem in `agentos-py/AGENTS.md`
- path: `agentos anchory ...` -> argparse handler -> `AnchoryDepot` -> JSON output
- RED: umbrella help has no Anchory command and no end-to-end command can round-trip a record
- GREEN: CLI tests cover register, resolve, query, amend, check, duplicate errors, missing anchors, and record-file input
- check: `cd agentos-cli && uv run pytest tests/test_e2e_anchory.py`
- check: reinstall with `uv tool install --reinstall --editable .`, then run `agentos anchory --help`
- status: complete

### Slice 5 - Chatlas depot adapter

- add a Chatlas helper returning `AnchoryDepot(<resolved-chatlas-root>/anchory)`
- path: explicit or default Chatlas root -> Chatlas path resolver -> Anchory public library
- RED: Chatlas has no standard path into its Anchory depot
- GREEN: explicit-root and default-root tests resolve the required path without changing existing Chatlas queries
- check: `cd agentos-chatlas-py && uv run pytest tests/test_anchory_depot.py`
- status: complete

## Acceptance.Signals

- the same anchor may exist independently in two depots
- a duplicate anchor cannot be reused inside one depot's `global` dictionary
- all successful mutations leave deterministic valid JSON after process restart
- concurrent same-shard registrations do not lose records
- records round-trip without Anchory adding application fields
- `agentos anchory` uses only the public Anchory library
- the core package contains no Git or Chatlas imports
- Chatlas resolves its Anchory root as `<chatlas-root>/anchory`
- focused tests and Ruff pass in every touched Python repository

## Deviation.Triggers

- stop if current project support requires non-Unix locking; select and document a cross-platform lock primitive before continuing
- stop if realistic first-use data requires record-level query semantics; align the generic record contract before adding application fields
- stop if hash sharding conflicts with required human-editable Git behavior; do not silently collapse to one global file
- bounce to design if the implementation needs namespaces, deletion, automatic key allocation, or Anchory-managed Git actions

## Impl.Log

- 2026-07-06: first implementation request created from the accepted Anchory system and depot design; execution has not started
- 2026-07-06: repository-wide Ruff remains blocked by checkpoint-preexisting findings in `agentos-py/_DEPRECATED`, `agentos-py/dev`, and `agentos-chatlas-py/dev`; the execution kept them out of scope and verified all touched files clean
