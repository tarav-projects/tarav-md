# Chatlas Provider GC - design-session

## Session.Abstract

- Session started on 2026-06-08.
- Design target: make provider-home cleanup a first-class Chatlas subsystem.
- Working name: `Provider.GC`.
- Primary user pressure: `copilot-cli` has many already-captured native sessions, and revisiting old provider-home originals slows `agentos chatlas update`.
- Accepted command shape: `agentos chatlas gc --provider copilot-cli`.
- Core design stance: Chatlas may garbage-collect provider-home originals only when Chatlas' own indexed/archive documents prove the retained copy already exists.
- Artifact scope: design alignment only; implementation request and code changes are follow-on work.

## Design.Index

### Provider.GC

- `Provider.GC` is a Chatlas maintenance subsystem for deleting provider-home originals that Chatlas has already captured.
- It treats provider homes as ingestion sources, not the long-term retained dataset, once Chatlas raw archive coverage is proven.
- It exists to make normal update paths faster by shrinking old provider-home scan surfaces.
- It is provider-scoped first: the motivating first provider is `copilot-cli`.
- It belongs to Chatlas itself because Chatlas already owns the documents, index rows, raw backing artifacts, and checks needed to decide eligibility.
- It is not a provider query subcommand; it is a top-level Chatlas maintenance command.

### Chatlas.GC.Command

- Accepted CLI shape: `agentos chatlas gc --provider copilot-cli`.
- `--provider` is required for the first design pass.
- The command should use the same provider-family choices and output conventions as existing Chatlas commands.
- The command should default to a report-oriented mode before destructive behavior is allowed.
- Recommended destructive gate: require an explicit apply flag, such as `--apply`, before moving provider-home files.
- The command should support JSON output so deletion candidates and results can be audited or scripted.

### GC.Eligibility

- A provider-home original is eligible only when Chatlas can map it to a retained Chatlas raw artifact.
- The primary proof source should be Chatlas' indexed backing artifact data and raw archive paths, not an ad hoc filename heuristic.
- Eligibility should compare the provider original against the archived raw copy using the checks Chatlas already records or can derive.
- Eligibility requires exact content hash equality between the provider-home original and the retained Chatlas raw copy.
- Existing update mechanics already copy native source artifacts into `chatlas_root/raw/<provider>/<fingerprint>/home/...`.
- Existing raw path/export commands already expose indexed backing artifacts, which makes them the natural eligibility surface.
- Unknown, unindexed, failed-parse, missing-archive, or mismatched originals are not delete candidates.
- Provider-home directories are never eligible as directories unless every contained original has been resolved and deletion of the empty directory is explicitly safe.

### GC.Scan.Model

- GC should reuse the same provider scanning logic as Chatlas update.
- GC runs in two phases: scan provider sessions and accumulate candidates, then apply movement for eligible candidates.
- The scan phase is the authority for what currently exists in provider home.
- The apply phase should operate from the accumulated candidate list rather than rediscovering a different scope.
- This keeps GC aligned with the update path and avoids a second provider interpretation layer.

### GC.Age.Cutoff

- GC should leave recent provider-home content untouched by default.
- Default policy: keep one month of provider-home content.
- Recommended CLI shape: `--older-than 30d`, defaulting to `30d`.
- The cutoff applies before candidate movement; recent captured originals remain in provider home.
- The cutoff makes first-pass bulk cleanup safer while still removing very old scan burden.

### GC.Safety

- `Provider.GC` must never delete the only known copy of a session.
- Dry-run/report mode is the default posture.
- Apply mode should move only the exact provider-home files that passed eligibility.
- First-pass `Provider.GC` should not hard-delete provider-home originals.
- In this design, "clean" means moving provider-home originals out of the provider scan path into Chatlas-owned GC storage.
- GC should avoid mutating Chatlas raw archive, session index, view artifacts, annotations, or caches except for writing its own report.
- GC should be idempotent: after a successful apply, a second run should report fewer or zero candidates without error.

### GC.Storage

- GC storage should live under the Chatlas dataset root, not under the provider home.
- Recommended destination root: `chatlas_root/gc/`.
- The dataset `.gitignore` should ignore `/gc/`.
- The GC command should ensure `/gc/` is ignored.
- Moved provider-home originals should preserve enough path context to restore or inspect them later.
- Recommended first-pass layout: `gc/provider-home/<provider>/<fingerprint>/home/<original-relative-path>`.
- Apply mode may overwrite an existing GC destination.
- GC storage is a cleanup holding area, not the retained Chatlas raw archive.

### GC.Report

- Every run should produce a structured report.
- Report fields should include provider selection, instance selection, scanned originals, eligible candidates, skipped originals, applied deletions, failures, and elapsed timing.
- Skipped rows should carry reasons such as `not_indexed`, `archive_missing`, `metadata_mismatch`, `unsupported_storage_kind`, or `apply_not_requested`.
- Apply runs should record enough detail to understand what was moved without needing the provider home to still exist.
- Report persistence should live under Chatlas-owned state, not in the provider home; exact path and schema are implementation decisions.

### Update.Performance

- The direct performance win is reducing old native sessions discovered by provider scans.
- The design intentionally removes old provider-home originals rather than teaching every update to ignore them.
- This keeps `agentos chatlas update` simpler: provider discovery sees less old material, while Chatlas raw archive remains the retained corpus.
- `agentos chatlas index redo` remains the recovery/rebuild path from copied raw artifacts.

### Provider.GC.Boundary

- In scope: provider-home originals that are already archived by Chatlas.
- In scope: provider filters and later instance/session filters if implementation needs them.
- In scope: reports and deletion eligibility checks.
- Out of scope: deleting Chatlas raw archive artifacts.
- Out of scope: deleting sessions that are only present in provider home.
- Out of scope: changing view materialization or annotation semantics.

## Session.Notes

- User rejected `agentos chatlas provider gc copilot-cli`.
- User accepted options-based syntax: `agentos chatlas gc --provider copilot-cli`.
- The current implementation already has raw archive manifests and copied source path mapping in `agentos_chatlas.raw_archive`.
- The current update path discovers provider sessions, copies changed sources into Chatlas raw, then derives session index rows from the copied raw artifacts.
- The command should probably be implemented in `agentos-chatlas-py` as a new module rather than buried inside provider query, with CLI registration in `agentos_chatlas.commands`.
- Likely implementation neighbors: `raw_archive.py`, `delta_scan.py`, `core.py`, `commands.py`, and provider/session source references from `agentos.agent.primitives`.
- Accepted: first-pass apply mode moves eligible provider-home originals into a Chatlas-owned `.gitignored` GC folder; it does not hard-delete.
- Accepted: eligibility uses exact content hash equality.
- Accepted: GC reuses update scanning logic, accumulates candidates, then applies movement.
- Accepted: default age cutoff keeps one month of provider-home content; recommended CLI is `--older-than 30d`.
- Accepted: first pass supports `--provider`, `--instance`, and likely `--session-id`.
- Accepted: GC destination collisions may overwrite.
- Accepted: command ensures `/gc/` is present in the Chatlas dataset `.gitignore`.
- Open implementation question: exact persisted report path and schema version.

## Session.Log

- 2026-06-08: User proposed `Provider.GC` to delete already-captured provider-home originals for faster Chatlas updates, motivated by large `copilot-cli` history.
- 2026-06-08: User clarified the command shape should be options-based: `agentos chatlas gc --provider copilot-cli`.
- 2026-06-08: Created artifact-backed design session in `agentos-chatlas-md/notes/live/`.
- 2026-06-08: User clarified that clean means moving eligible originals to a Chatlas-owned `.gitignored` folder, not hard deletion.
- 2026-06-08: User accepted hash-based eligibility, update-aligned scanning, one-month default cutoff, overwrite-on-collision, and ensuring `/gc/` in `.gitignore`.
