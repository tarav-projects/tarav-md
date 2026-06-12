# Chatlas Provider GC - impl-req

## Impl.Abstract

- **scope:** implement first-pass `Provider.GC` in `agentos-chatlas-py` as `agentos chatlas gc --provider <provider>`.
- **status:** implemented and verified.
- **source:** `notes/live/506-chatlas-provider-gc-design-session.md`.
- **intent:** move already-captured provider-home originals out of provider homes so `agentos chatlas update` stops revisiting old captured sessions.
- **non-goal:** do not delete Chatlas raw archive artifacts, view artifacts, annotations, or session index data.
- **first provider pressure:** `copilot-cli`, but the implementation should use provider-family plumbing rather than hard-coding Copilot behavior where avoidable.

## Impl.Index

### Provider.GC.Command.Surface

- add a top-level Chatlas command: `agentos chatlas gc`.
- accepted primary use: `agentos chatlas gc --provider copilot-cli`.
- first-pass filters: `--provider`, `--instance`, and `--session-id`.
- default mode is dry-run/report; `--apply` is required before files are moved.
- add `--older-than`, default `30d`, to leave recent provider-home content untouched.
- support JSON output for automation; human progress should follow existing update-style stderr behavior.
- wire through `agentos_chatlas.commands`, with core behavior in a new implementation module rather than inside provider query.

### GC.Scan.Reuse

- GC must reuse the same provider session discovery logic as Chatlas update.
- selected provider instances should come from existing Chatlas configuration and supported provider families.
- instance filtering should use the existing single-session refresh mechanism: filter selected instances by `agent.instance_id` or `instance`.
- the scan phase discovers current provider-home sessions and accumulates candidates.
- the apply phase operates from the accumulated candidate list; it should not rediscover a different scope.
- current code evidence: `delta_scan.chatlas_delta_scan` calls `selected_provider_instances` and `_discover_instance_sessions`.
- current code evidence: `session_refresh.chatlas_single_session_update` applies the existing `--instance` selection pattern after `selected_provider_instances`.
- implementation may extract shared helpers if that keeps GC aligned with existing update/session-refresh behavior without widening public surface unnecessarily.

### GC.Eligibility.Proof

- a candidate is eligible only when the provider-home source maps to a retained Chatlas raw artifact.
- proof should use Chatlas-owned evidence: raw archive path mapping, raw partition manifests, and indexed backing artifacts where useful.
- eligibility requires exact content hash equality between original provider-home file and retained Chatlas raw copy.
- unknown, unindexed, failed-parse, missing-archive, mismatched, directory, or unsupported-storage originals are skipped.
- recent originals newer than the age cutoff are skipped before movement.
- skip reasons must be explicit in the report.

### GC.Apply.Semantics

- `--apply` moves eligible provider-home originals to Chatlas-owned GC storage; it does not hard-delete.
- destination root: `chatlas_root/gc/`.
- recommended layout: `gc/provider-home/<provider>/<fingerprint>/home/<original-relative-path>`.
- destination collisions are overwritten.
- the command must ensure `/gc/` is present in the Chatlas dataset `.gitignore`.
- moved files should preserve enough original path context to inspect or restore manually.
- successful apply should make a second run report fewer or zero candidates.

### GC.Report.Shape

- every run returns a structured payload.
- include command, status, chatlas root, provider/instance/session filters, `older_than`, apply flag, instances, counters, candidates, moved files, skipped files, failures, and elapsed timing.
- persisted report storage must be Chatlas-owned and outside provider home.
- recommended path: `chatlas_root/manifests/gc/<timestamp>.json`.
- report schema can be pragmatic, but should include a class and schema version if persisted.
- dry-run reports should be sufficient for a user to see exactly what `--apply` would move.

### Implementation.Boundary

- primary package: `agentos-chatlas-py`.
- likely files: `src/agentos_chatlas/gc.py`, `commands.py`, `paths.py`, and tests.
- likely helper reuse: `instance_selection.selected_provider_instances`, `delta_scan.ChatlasProviderInstance`, raw archive source path mapping, and provider session refs/sources.
- avoid changing the semantics of `agentos chatlas update`, `index redo`, raw export/path, or view production.
- if shared helper extraction touches `delta_scan.py` or `raw_archive.py`, keep behavior-preserving tests around existing update/raw flows.

## Execution.Plan

### Slice 1 - Add dry-run GC command skeleton

- add `agentos_chatlas.gc` with a `chatlas_gc(...)` function returning a structured report.
- add CLI parser for `agentos chatlas gc` with `--provider`, `--instance`, `--session-id`, `--older-than`, `--apply`, progress, and JSON output mode.
- path: CLI parser -> core GC function -> empty/scan-only report.
- observable: `agentos chatlas gc --provider codex --output-mode json` returns a valid JSON report without moving files.
- check: targeted CLI/unit test for parser and report envelope.
- status: completed.

### Slice 2 - Reuse provider scanning and accumulate candidates

- scan selected provider instances using the same provider discovery path used by update.
- support provider, instance, and session-id filters in the scan using the existing instance-filtering mechanism already used by single-session refresh.
- gather provider-home source files from discovered session refs.
- apply `--older-than 30d` default cutoff before eligibility proof.
- path: selected provider instances -> discovered sessions -> session sources -> candidate list.
- observable: dry-run report lists scanned instances and candidate/skipped counts from test fixtures.
- check: tests using temporary configured provider homes and deterministic session files.
- status: completed.

### Slice 3 - Prove archive coverage with content hashes

- map each provider-home source to its expected Chatlas raw archive path.
- require the archived raw copy to exist.
- compute content hashes for original and raw copy; candidate is eligible only when hashes match.
- report explicit skip reasons for missing archive, hash mismatch, unsupported storage, directory source, and recent cutoff.
- path: provider source -> raw archive mapping -> hash proof -> eligibility result.
- observable: dry-run separates eligible, recent, missing-archive, and hash-mismatch fixtures correctly.
- check: unit tests for eligibility helper plus an end-to-end dry-run test.
- status: completed.

### Slice 4 - Apply movement into ignored GC storage

- implement `--apply` movement from provider home into `chatlas_root/gc/provider-home/...`.
- preserve original relative path beneath provider home.
- overwrite destination collisions.
- ensure `/gc/` exists in `chatlas_root/.gitignore`.
- persist a Chatlas-owned GC report, recommended under `manifests/gc/`.
- path: eligible candidate list -> destination path -> move -> persisted report.
- observable: original provider file is gone, GC file exists, raw archive file remains, `.gitignore` contains `/gc/`.
- check: apply-mode test with temp Chatlas root and provider home.
- status: completed.

### Slice 5 - Validate integration with update and raw recovery

- after GC apply, run query/export/raw-path style checks against the retained Chatlas raw archive where fixtures allow it.
- ensure `agentos chatlas update` behavior is not regressed for ordinary sessions.
- ensure `agentos chatlas index redo` remains conceptually compatible with raw archive retention.
- path: update copies raw -> GC moves provider original -> raw/query/export still use Chatlas raw.
- observable: raw-path/export tests still point at `chatlas_root/raw`, not provider home or GC storage.
- check: existing e2e tests plus new GC integration test.
- status: completed.

## Validation

- run targeted tests while developing:
  - `uv run pytest tests/test_e2e_chatlas.py -q`
  - `uv run pytest tests/test_chatlas_gc.py -q` if a dedicated test file is added.
- run broader package tests before completion:
  - `uv run pytest`
- run formatting/linting only if the repository already expects it for touched files:
  - `uv run ruff check src tests`

## Risks

- provider source refs may include directory or non-file storage; skip rather than infer behavior.
- instance filtering already exists in the single-session refresh path; GC should reuse that mechanism instead of creating a new selection convention.
- hash reads may be expensive on large histories; acceptable for first-pass cleanup because movement is destructive-adjacent.
- age cutoff semantics depend on available timestamps; use source file mtime unless a provider session timestamp is clearly more reliable in the existing model.
- modifying `.gitignore` touches the Chatlas dataset repo, not the code repo; tests should exercise this in a temp dataset root.

## Deviation.Triggers

- stop and realign if provider discovery does not expose enough source path information to map originals to raw archive paths.
- stop and realign if `copilot-cli` stores session originals in a structure where moving individual source files breaks provider invariants beyond scan performance.
- stop and realign before changing existing `agentos chatlas update` behavior outside shared helper extraction.
- stop and realign before deleting any source instead of moving it.

## Acceptance.Signals

- `agentos chatlas gc --provider copilot-cli` performs a dry run and reports candidates without moving files.
- `agentos chatlas gc --provider copilot-cli --apply` moves eligible old originals into `chatlas_root/gc/`.
- recent provider-home content is retained by default.
- only content-hash-matching originals are moved.
- `/gc/` is ensured in the Chatlas dataset `.gitignore`.
- Chatlas raw archive remains the backing source for query/export/raw-path workflows.

## Impl.Log

- 2026-06-08: Impl.Req created from `506-chatlas-provider-gc-design-session.md`; execution not started.
- 2026-06-08: User clarified that GC instance filtering should use the mechanism already in place.
- 2026-06-08: Execution found provider sources can include shared non-transcript files; first-pass GC should move transcript file sources only and skip other roles to avoid breaking provider discovery.
- 2026-06-08: User clarified GC should move all Chatlas provider read-targets for eligible sessions; implementation now promotes safe session directories such as Copilot `session_root` while still skipping locator-backed shared files.
