# Anchory Source Query - impl-req

## Impl.Abstract

- **scope:** add a read-only `agentos anchory scan` command that extracts anchor candidates from a source file with a regex, resolves them against an Anchory depot, and prints the found anchors plus records.
- **status:** implemented
- **source:** user request: `Anchory.Source.Query` scans `--src-file` with `--regex`, extracts anchors, resolves each against `--depot`, prints found anchors plus records, does not mutate, human-friendly output by default, and `--json` returns deterministic machine-readable output.
- **current state:** Anchory has a depot-scoped library and CLI commands for register, resolve, query, amend, and check; current commands print deterministic JSON by default.
- **out of scope:** registering anchors from files, amending records, generating anchors, changing existing command output defaults, scanning directories, pagination, and record predicate filtering.

## Impl.Index

### Anchory.Source.Query

- `Anchory.Source.Query` is a read-only CLI query feed from ordinary text files into Anchory resolution.
- source files remain authoritative; Anchory only reads candidate anchor text from them.
- regex extraction produces ordered matches from the file content.
- extraction uses named capture group `anchor` when present.
- extraction falls back to the first positional capture group when no `anchor` group exists.
- extraction falls back to the whole regex match when no capture groups exist.
- each extracted candidate is resolved through the selected `AnchoryDepot`.
- unresolved candidates stay visible in output with a missing/null record.
- duplicate anchors are collapsed after first occurrence so repeated file mentions do not duplicate resolution output.
- scan order follows first occurrence in the source file.
- the command performs no depot mutation.

### Anchory.Scan.CLI

- command: `agentos anchory scan --depot <path> --src-file <path> --regex <pattern> [--json]`
- `--depot` selects the exact Anchory depot root, matching existing Anchory commands.
- `--src-file` selects one text file to scan.
- `--regex` is a Python regular expression.
- default output is human-friendly for terminal use.
- `--json` prints deterministic machine-readable output.
- JSON payload includes `depot`, `src_file`, `regex`, `count`, and `matches`.
- each match includes `anchor`, `record`, and source location metadata sufficient for a user to find the source mention.
- invalid regex, unreadable source file, invalid anchor, or corrupt depot errors cross the existing `CliError` boundary.
- existing Anchory commands keep their current JSON-by-default behavior.

## Execution.Plan

### Slice 1 - Source extraction primitive

- add a small source-scan helper in the Anchory implementation surface that accepts source text and regex text and returns first-occurrence anchor candidates with line/column metadata.
- path: `src-file` bytes/text -> regex matches -> candidate anchors -> ordered scan matches.
- RED: focused unit tests show named-group, first-capture, whole-match, de-duplication, and line/column behavior are unavailable.
- GREEN: helper returns deterministic scan matches without reading or mutating an Anchory depot.
- check: `cd agentos-py && uv run pytest tests/test_anchory.py`
- status: complete

### Slice 2 - CLI scan command

- add `agentos anchory scan --depot --src-file --regex [--json]`.
- default output should be readable text listing each anchor and either its JSON record or a missing marker.
- `--json` should print deterministic JSON containing all matches and records.
- path: CLI args -> source extraction -> `AnchoryDepot.resolve` -> renderer.
- RED: e2e tests show `scan` is absent and `--json`/human output cannot be produced.
- GREEN: scan resolves found anchors, shows missing anchors, preserves first occurrence order, and leaves the depot unchanged.
- check: `cd agentos-cli && uv run pytest tests/test_e2e_anchory.py`
- status: complete

### Slice 3 - Guidance and installed CLI verification

- update `agentos-py/AGENTS.md` if the documented Anchory surface needs the new read-only source-query command.
- reinstall the editable CLI so `agentos anchory scan --help` is available through the installed executable.
- inspect `agentos anchory scan --help`.
- run focused Ruff checks on touched Python files.
- status: complete

## Acceptance.Signals

- `agentos anchory scan --depot <path> --src-file bla.md --regex '<pattern>'` works without `--json`.
- default output is human-friendly and includes found anchors plus records.
- `--json` returns deterministic machine-readable output.
- named capture group `anchor` is supported.
- first positional capture group is supported.
- whole-match extraction is supported when no groups exist.
- repeated source mentions are de-duplicated by anchor after first occurrence.
- missing anchors are reported without failing the command.
- the command does not register, amend, or otherwise mutate depot files.
- existing Anchory commands keep their current output policy.
- focused tests and Ruff pass for touched surfaces.

## Deviation.Triggers

- stop if source scanning requires Anchory to own application record semantics.
- stop if this needs multi-file traversal or directory scanning.
- stop if source regions need durable anchor registration rather than read-only resolution.
- stop if the output policy change is requested for all Anchory commands instead of only `scan`.

## Impl.Log

- 2026-07-07: Impl.Req created for `Anchory.Source.Query`. Design decision: the first command is `agentos anchory scan`; it is read-only, human-friendly by default, and JSON only under `--json`. Existing commands keep JSON defaults to avoid a broader CLI policy migration.
- 2026-07-07: Implemented in `Alignment.Mode::Autonomous`. Deviation: the execution workflow's checkpoint commit was not created because root project guidance says never commit without an explicit commit request; work was left uncommitted. Verification: `agentos-py` `uv run pytest tests/test_anchory.py` passed (11), `agentos-cli` `uv run pytest tests/test_e2e_anchory.py` passed (5), Ruff passed on touched Python files, `uv tool install --reinstall --editable .` refreshed the installed CLI, and `agentos anchory scan --help` plus live human/JSON scan examples succeeded.
