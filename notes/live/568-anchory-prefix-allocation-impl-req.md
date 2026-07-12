# Anchory Prefix Allocation — Impl.Req

## Impl.Abstract

- **Goal**: let agents mint anchors without racing — `register` allocates the next `<prefix>-<N>` key atomically and returns the full anchor for line tagging.
- **Scope**: `AnchoryDepot.register` prefix mode + `agentos anchory register --prefix` CLI; docs refresh; `agentos-index` `link.md` planned-CLI note flip.
- **Out of scope**: a `next` advisory peek (user decision: implement only if actual workflows demand it); chatlas-side anchor digestion (`query --anchor`, turn search — `notes/live/567`, separate req); namespaces; storage format; `exists`/`anchors` read surfaces (owned by `565-anchory-read-surfaces-impl-req.md`).
- **Repos**: code in `agentos-py` (`src/agentos/anchory/core.py`, `src/agentos/anchory/commands.py`, `tests/test_anchory.py`); CLI parser behavior also has e2e coverage in `agentos-cli/tests/test_e2e_anchory.py` — both repos are in scope. The `agentos` executable is owned by `agentos-cli`; CLI changes require `uv tool install --reinstall --editable .` from `agentos-cli/` (per `agentos-py/AGENTS.md`).
- **Source**: this design session (first end-to-end linking run); `notes/live/567-linking-cli-follow-ups-parking.md` item 1; index concepts `Anchory.System`, `Chatlas.Anchory`, `Index.Linking`.
- **Status**: implemented

## Impl.Index

### Current.State *(inspected, cited)*
- `AnchoryDepot.register(anchor, record)` requires an exact key and raises `AnchorExistsError` on collision (`core.py:77`)
- allocation today is caller-side: `query --prefix` then `register`, a race window the first live run hit around manually
- storage shards by `sha256(anchor)[:2]` (`core.py:228`) — prefix scans iterate all shards, as `query(prefix=…)` already does (`core.py:107`)
- all mutation runs under one depot-wide `flock` (`core.py:207`) — an exclusive section spanning scan+write is already the locking model

### Allocation.Contract
- `AnchoryDepot.register(record, *, anchor=None, prefix=None)` — exactly one of `anchor`/`prefix`; both or neither is `InvalidAnchoryInputError`
- prefix mode: under the exclusive lock, collect existing anchors matching exactly `re.escape(prefix) + r"-(\d+)$"` — never `startswith`, so adjacent prefixes cannot interfere — allocate `N = max + 1` (`0` when none), write, return the `AnchoryEntry` carrying the allocated anchor
- max+1, never gap-filling — gaps are irrelevant (user decision); an allocated-looking key must never be re-mintable
- anchors under the prefix that do not end in `-<integer>` are ignored by allocation, not errors
- the joiner is fixed `-`; anchory stays application-agnostic — date prefixes are a Chatlas convention, not an anchory rule
- exact-anchor mode is unchanged, including `AnchorExistsError` semantics
- the signature change `register(record, *, anchor=None, prefix=None)` is breaking versus `register(anchor, record)` — accepted under `No.Legacy.Allowed`; ALL internal callers and tests update in the same pass, including any register callsites in `agentos-chatlas-py`

### CLI.Surface
- `agentos anchory register --depot … (--anchor A | --prefix P) (--record-json … | --record-file …)`
- `--anchor` and `--prefix` are argparse-mutually-exclusive, one required
- output is the same registration payload as today, carrying the allocated anchor — the agent tags its line from it
- help text states allocation is atomic and returns the anchor

### Scope.Boundary
- no `next` command: what the actual workflows demand decides later additions
- no changes to `resolve`/`query`/`amend`/`check`/`scan`
- no coordination needed with 565 (`exists`/`anchors`): read-only surfaces, disjoint diff areas; if it lands first, allocation may reuse its key-listing helper opportunistically

## Execution.Plan

### S1 — Library prefix allocation (test-first)
- what changes: `register` signature gains keyword `prefix`; allocation logic inside the existing exclusive-lock section
- RED (`tests/test_anchory.py`): empty prefix allocates `-0`; existing `-0`/`-1` allocates `-2`; gap (`-0`,`-2` present) allocates `-3` not `-1`; non-integer suffixes under the prefix ignored; adjacent prefix isolation (`2026` never sees `20260708-0`); `anchor`+`prefix` together and neither both raise `InvalidAnchoryInputError`; returned entry carries the allocated anchor and normalized record; concurrency: two simultaneous `register(prefix=…)` callers (threads or processes against one depot) always yield distinct anchors
- GREEN: minimal allocation implementation
- check: new tests pass; full `test_anchory.py` green; exact-anchor behavior untouched

### S2 — CLI `--prefix`
- what changes: `commands.py` register parser gains the mutually exclusive group; handler routes to the new keyword
- RED: CLI-level test — register via `--prefix` on a tmp depot prints payload with allocated anchor; second call allocates the next key; `--anchor`+`--prefix` exits with a usage error; e2e parser coverage added in `agentos-cli/tests/test_e2e_anchory.py` alongside the existing cases
- check: suite green; `agentos anchory register --prefix …` verified against a scratch depot after `agentos-cli` editable reinstall

### S3 — Docs + skill-surface flip
- what changes: `agentos-py/AGENTS.md` — the CLI-surface notes AND the design statement at the allocation boundary (it currently says applications own anchor allocation; prefix allocation now moves into Anchory — the ownership line must be rewritten, not just the command list); `agentos-md/skills/agentos-index/references/link.md` — replace the "target CLI (planned)" allocation note with the real command as the primary path (query-then-retry drops out); `notes/live/567` item 1 marked done
- check: `link.md` pipeline step 3 reads as a single command; no remaining "planned" wording for allocation

### Acceptance signals
- an agent can mint a tagged-ready anchor with one command: `agentos anchory register --depot <chatlas-root>/anchory --prefix <YYYYMMDD> --record-json '…'`
- two concurrent prefix registrations never yield the same anchor (serialized by the depot lock)
- full `agentos-py` and `agentos-cli` suites green; `No.Regression.Tests.Allowed` respected

### Risks / deviation triggers
- if 565 lands mid-flight and touches `register` or shard iteration, rebase on it rather than duplicating helpers
- if prefix scanning over all shards proves slow on large depots, note it in `Impl.Log` and leave optimization out — correctness first, the depot is small today

## Impl.Log

- 2026-07-08: Executed in `Alignment.Mode::Autonomous`. Deviation: the execution module's git checkpoint could not be created because the umbrella root is not a git repo and project instructions prohibit commits without an explicit commit request; proceeded without a checkpoint and left changes uncommitted. Pre-existing dirty changes were present in related Anchory/CLI/Chatlas areas; inspected and preserved them.
- 2026-07-08: Implemented `AnchoryDepot.register(record, *, anchor=None, prefix=None)` with exactly-one identity validation, exact regex prefix allocation under the existing exclusive depot lock, max+1 suffix selection, and no gap filling. Updated internal exact-anchor callsites/tests to the breaking keyword-only contract.
- 2026-07-08: Added CLI `agentos anchory register --prefix`, e2e coverage in `agentos-cli`, refreshed the installed `agentos` tool with `uv tool install --reinstall --editable .`, and verified prefix allocation against a scratch depot.
- 2026-07-08: Updated `agentos-py/AGENTS.md`, `agentos-index/references/link.md`, and `notes/live/567-linking-cli-follow-ups-parking.md`. Verification: `agentos-py` `uv run pytest` passed (274), `agentos-cli` `uv run pytest` passed (56), focused Ruff checks passed for touched Anchory and CLI test files.
- 2026-07-08: Adjacent Chatlas verification: `agentos-chatlas-py` `uv run pytest tests/test_anchory_depot.py` passed (2). `agentos index linter --depot agentos-md/skills/agentos-index` was attempted but is not applicable because `agentos-index` is a runnable skill/reference surface, not a lintable index depot with chapter/router files.
