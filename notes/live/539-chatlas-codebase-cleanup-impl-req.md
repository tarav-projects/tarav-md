# 539 — chatlas codebase cleanup — Impl.Req

## Impl.Abstract

| Field | Value |
|---|---|
| Status | done |
| Scope | Consolidate duplicated helpers, remove `_experimental_` prefixes, clean up dead code and DRY violations across `agentos-chatlas-py` |
| Source | Full codebase audit (6 parallel agents, 30 findings) — in-chat session |
| Target package | `agentos-chatlas-py` (`agentos_chatlas`) |

### Intent

The chatlas codebase has accumulated cross-cutting DRY violations, inconsistent naming, and dead code across its ~18K lines. The most impactful issues:

1. `_string_or_none()` defined 7 times with behavioral inconsistency (some strip/reject empty, some don't)
2. `_visible_message_texts()` + `_content_text()` duplicated between `query.py` and `delta_scan.py`
3. `_dict_list()` and `_string_list()` duplicated between `session_model/_shared.py`, `session_model/_views.py`, and `views/core.py`
4. `_experimental_` prefix on 10+ stable functions in `session_model/`
5. Dead code, missing `__all__` entries, and unnecessary thin wrappers

This impl-req covers the highest-value, lowest-risk cleanup work. It deliberately excludes module decomposition (splitting `delta_scan.py` or `views/core.py` into smaller files) — those are larger changes that deserve separate design sessions.

### Key design decisions

- **New shared module**: `agentos_chatlas/_payload_helpers.py` — single source of truth for `_string_or_none`, `_dict_list`, `_string_list`, `_visible_message_texts`, `_content_text`. All current call sites import from here.
- **Canonical `_string_or_none` behavior**: returns `value` if `isinstance(value, str) and value` (rejects empty strings). This matches `_shared.py` semantics. The `_views.py` variant that accepts empty strings is a bug — no caller relies on that behavior.
- **`_experimental_` removal**: drop the prefix from all functions in `session_model/_model.py` and `session_model/_shared.py`. These are stable.
- **Do not touch**: module decomposition, `core.py` facade assessment, `commands.py` argument helpers consolidation, `__init__.py` lazy loading. Those are separate concerns.

## Impl.Index

### Block: shared helpers location

The duplicated functions need a single home. Options:
- **A) `session_model/_shared.py`** — already has most of them, but it's a `session_model` internal module. Importing from `session_model._shared` in `query.py` or `views/core.py` crosses package boundaries.
- **B) New top-level `_payload_helpers.py`** — clean import path, no boundary violation.
- **C) Existing `_cache_io.py`** — wrong semantic scope.

Recommendation: **B**. New `agentos_chatlas/_payload_helpers.py`. The functions are generic payload inspection helpers used across the entire package. The `session_model/_shared.py` copies become imports from the new module.

### Block: _string_or_none behavioral consolidation

7 definitions exist. Behavioral split:
- **Strict** (`_shared.py`, `core.py`, `index_stats.py`, `index_doctor.py`, `index_query.py`): `isinstance(value, str) and value` — rejects empty strings
- **Loose** (`_views.py`, `query.py`): `isinstance(value, str)` — accepts empty strings

The strict variant is correct. Empty strings should be treated as None in payload inspection. The `_views.py` variant was a copy-paste drift. Consolidate on strict.

### Block: _visible_message_texts deduplication

Defined identically in `query.py:190` and `delta_scan.py:877` (plus helper `_content_text`). Both extract visible message texts from a session model by role. `recents.py` imports the `query.py` version as a private cross-module import.

Move to `_payload_helpers.py`. All three call sites import from there.

### Block: _experimental_ prefix scope

In `session_model/_model.py`:
- `_experimental_normalize_provider_raw` → `_normalize_provider_raw`
- `_experimental_session_payload` → `_session_payload`
- `_experimental_session_hashes` → `_session_hashes`
- `_experimental_agent_instance_payload` → `_agent_instance_payload`
- `_experimental_source_payloads` → `_source_payloads`
- `_experimental_source_payload` → `_source_payload`

In `session_model/_shared.py`:
- `_ExperimentalNormalizationResult` → `_NormalizationResult`
- `_experimental_normalization_metadata` → `_normalization_metadata`
- Plus any other `_experimental_` functions

In provider normalizers (`_claude.py`, `_codex.py`, `_copilot.py`):
- `_experimental_normalize_*_session` → `_normalize_*_session`

All are private (`_` prefix), so no external API change. The `session_model/__init__.py` lazy loader does not export any `_experimental_` names.

### Block: dead code and missing exports

- `views/core.py`: `_session_selector_flags()` — appears unused. Verify with grep before deleting.
- `views/core.py`: `_zip_transcript_fingerprint()` — trivial wrapper over `_session_model_fingerprint()`. Inline at call sites.
- `core.py`: `format_chatlas_doctor_markdown` missing from `__all__`. Add it.
- `session_model/_model.py`: `build_chatlas_session_model_from_index_row` is a thin wrapper over `_build_session_model`. Keep — it's a public API entry point used by `views/core.py` and `delta_scan.py`.

## Execution.Plan

### Slice 1 — Create `_payload_helpers.py` with canonical helpers

**What changes**: New file `agentos_chatlas/_payload_helpers.py` containing:
- `_string_or_none(value) -> str | None` (strict: rejects empty)
- `_dict_list(value) -> list[dict]`
- `_string_list(value) -> list[str]`
- `_visible_message_texts(session_model, *, roles) -> list[str]`
- `_content_text(value) -> str`

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/_payload_helpers.py` — new file

**Observable result**: `from agentos_chatlas._payload_helpers import _string_or_none` works in Python REPL.

**Validation**: Import all 5 functions, verify signatures match the canonical versions.

### Slice 2 — Migrate `_string_or_none` callers

**What changes**: Replace all 7 local definitions with imports from `_payload_helpers`. Delete the local definitions.

**Files** (each gets import swap + definition deletion):
- `query.py`
- `core.py`
- `index_query.py`
- `index_stats.py`
- `index_doctor.py`
- `session_model/_shared.py`
- `session_model/_views.py`

**Observable result**: `grep -r "def _string_or_none" src/agentos_chatlas/` returns only `_payload_helpers.py`.

**Validation**: Run `uv run python -c "from agentos_chatlas.core import chatlas_query"` and similar imports to verify no breakage.

### Slice 3 — Migrate `_dict_list` and `_string_list` callers

**What changes**: Replace definitions in `session_model/_shared.py`, `session_model/_views.py`, and `views/core.py` with imports from `_payload_helpers`.

**Files**:
- `session_model/_shared.py`
- `session_model/_views.py`
- `views/core.py`

**Observable result**: `grep -r "def _dict_list" src/agentos_chatlas/` returns only `_payload_helpers.py`.

**Validation**: Import check on affected modules.

### Slice 4 — Migrate `_visible_message_texts` and `_content_text` callers

**What changes**: Replace definitions in `query.py` and `delta_scan.py` with imports from `_payload_helpers`. Update `recents.py` to import from `_payload_helpers` instead of `query.py`.

**Files**:
- `query.py` — delete definitions, add import
- `delta_scan.py` — delete definitions, add import
- `recents.py` — change import source from `query` to `_payload_helpers`

**Observable result**: `grep -r "def _visible_message_texts" src/agentos_chatlas/` returns only `_payload_helpers.py`. `recents.py` no longer imports private functions from `query.py`.

**Validation**: `uv run python -c "from agentos_chatlas.recents import run_chatlas_recents"` succeeds.

### Slice 5 — Remove `_experimental_` prefix from `session_model/`

**What changes**: Rename all `_experimental_`-prefixed functions and classes in `session_model/_model.py`, `session_model/_shared.py`, `session_model/_claude.py`, `session_model/_codex.py`, `session_model/_copilot.py`. Update all internal references.

**Files**:
- `session_model/_model.py` — rename ~10 functions + update all call sites
- `session_model/_shared.py` — rename `_ExperimentalNormalizationResult` → `_NormalizationResult`, rename helper functions
- `session_model/_claude.py` — rename exported function
- `session_model/_codex.py` — rename exported function
- `session_model/_copilot.py` — rename exported function

**Observable result**: `grep -r "_experimental_" src/agentos_chatlas/session_model/` returns no matches.

**Validation**: `uv run python -c "from agentos_chatlas.session_model import build_chatlas_session_model_from_index_row"` succeeds. `agentos chatlas export --session-id <any-id>` produces valid output.

### Slice 6 — Dead code and missing exports cleanup

**What changes**:
- Delete `_session_selector_flags()` from `views/core.py` (verify unused first)
- Inline `_zip_transcript_fingerprint()` at its call sites in `views/core.py` (it's just `_session_model_fingerprint(session)`)
- Add `format_chatlas_doctor_markdown` to `core.py` `__all__`

**Files**:
- `views/core.py`
- `core.py`

**Observable result**: Dead functions removed, `__all__` complete.

**Validation**: `uv run python -c "from agentos_chatlas.core import format_chatlas_doctor_markdown"` works. Grep confirms deleted functions have no remaining references.

### Risks

- **Import cycles**: `_payload_helpers.py` must not import from any chatlas module that imports it back. The helpers are pure functions operating on dicts — no chatlas imports needed.
- **`_string_or_none` behavioral change**: The `_views.py` callers switch from loose to strict. If any view projection relies on empty strings being preserved, behavior changes. Low risk — view projections extract from session models where empty strings are not meaningful.
- **`_experimental_` rename breadth**: Touches 5 files in `session_model/`. All renames are private symbols, but the diff is large. Careful with find-and-replace to avoid partial matches.

### Out of scope

- `delta_scan.py` decomposition (1336 lines, needs its own design session)
- `views/core.py` decomposition (1441 lines, needs its own design session)
- `core.py` facade assessment (whether pass-through wrappers add value)
- `commands.py` argument helper consolidation
- `session_model/__init__.py` lazy loading simplification
- `_process_provider_instance()` decomposition in `delta_scan.py`
- Silent `except Exception` error handling improvements

## Impl.Log

### 2026-05-21 — all 6 slices executed

- **Slice 1**: Created `_payload_helpers.py` with 5 canonical helpers. `_string_or_none` uses strict variant (`isinstance(value, str) and value`) — no whitespace stripping. The `_shared.py` strip-and-reject variant was a behavioral deviation; no caller depends on stripping.
- **Slice 2**: Migrated `_string_or_none` from 7 files. All definitions deleted, replaced with imports.
- **Slice 3**: Migrated `_dict_list` and `_string_list` from 3 files (`_shared.py`, `_views.py`, `views/core.py`).
- **Slice 4**: Migrated `_visible_message_texts` and `_content_text` from `query.py` and `delta_scan.py`. Updated `recents.py` to import from `_payload_helpers` instead of `query.py`.
- **Slice 5**: Removed all `_experimental_` prefixes across 6 files (`_model.py`, `_shared.py`, `_claude.py`, `_codex.py`, `_copilot.py`, `_transcript.py`). Zero `_experimental_` references remain.
- **Slice 6**: Deleted dead `_session_selector_flags()`, inlined `_zip_transcript_fingerprint()` → `_session_model_fingerprint()`, added `format_chatlas_doctor_markdown` to `core.py` `__all__`.

**Deviations**: The `_shared.py` `_string_or_none` was a 3rd behavioral variant (strip + reject empty) not noted in the original impl-req analysis. Resolved by adopting the strict no-strip variant as canonical per alignment discussion.

**No remaining work.**
