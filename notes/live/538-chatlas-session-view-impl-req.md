# 538 — chatlas-session internal view — Impl.Req

## Impl.Abstract

| Field | Value |
|---|---|
| Status | ready |
| Scope | New `chatlas-session` internal view that caches the full session model JSON per session |
| Source | In-chat design discussion (this session) — performance issue with `chatlas recents` |
| Target package | `agentos-chatlas-py` (`agentos_chatlas`) |

### Intent

`build_chatlas_session_model_from_index_row(row)` is expensive (file I/O + full JSON parse) and is called repeatedly by 5 consumers with no caching. Add a `chatlas-session` internal view that caches the full session model as a JSON artifact in the views infrastructure. All consumers that currently call `build_chatlas_session_model_from_index_row` should use the cached view instead.

### Key design decisions

- **Do not change `build_chatlas_session_model_from_index_row`** — it stays as-is. The view is built on top.
- **Internal view** — self-produces via `_ensure_available` like `zip-transcript`.
- **Not updated by `chatlas update`** — produced on demand only, when a consumer needs it.
- **All current consumers should use it** — `recents`, `query` text filters, `export`, `zip-transcript` view, and the `delta_scan` summary builder.
- Artifact: `session-model.json` — the full session model dict.
- Fingerprint: SHA256 of the raw backing artifact content (already available as `identity_hash` in the index row — same raw files, same model). If `identity_hash` is not reliable for this purpose, fall back to building + hashing.

### Callers to migrate

| Caller | File | Migration |
|---|---|---|
| `_extract_last_user_turns` | `recents.py` | Use cached view |
| `_row_matches_standard_model_filters` | `query.py` | Use cached view |
| `chatlas_export_session_model` | `session_model/_model.py` | Use cached view |
| `_zip_transcript_payload` | `views/core.py` | Use cached view |
| `_session_index_summary` | `delta_scan.py` | Keep as-is (runs at index build time, before views exist) |

Note: `delta_scan._session_index_summary` runs during index materialization. At that point the session row is being constructed — there's no view cache yet. This caller stays unchanged.

## Impl.Index

### Block: view workflow pattern

The existing `ZipTranscriptWorkflow` class (views/core.py:459-559) is the reference pattern for an internal view:
- `name`, `kind="internal"`, `description`, `artifact_contract`
- `current_status()` — reads manifest, computes current fingerprint, compares to observed
- `produce()` — builds artifact, writes to slot via `_replace_slot_with_files`
- `production_instructions()` — returns `{"mode": "internal", "action": "auto-produce"}`
- `build_produce_prompt()` / `prepare_agent_production()` — raise `CliError` (not applicable for internal views)

`_ensure_available()` (line 435) auto-produces internal views when missing or stale.

### Block: fingerprint strategy

The fingerprint determines when the cached session model is stale. Options:
- **A) `identity_hash` from the index row** — already computed, zero cost. But `identity_hash` is a content hash of the raw backing artifacts. If the session model normalization code changes, the cached model is stale but `identity_hash` hasn't changed.
- **B) Build the model and hash it** — always correct, but defeats the caching purpose for freshness checks.

Recommendation: **Use option A** (`identity_hash`). The session model normalization code rarely changes, and when it does, `chatlas index redo` or clearing the view cache handles it. The freshness check must be zero-cost to make the view worthwhile.

### Block: consumer helper

Add a helper function `load_chatlas_session_model(row, *, chatlas_root)` that:
1. Builds a `ChatlasViewContext` for `chatlas-session` from the row
2. Calls `_ensure_available` (which auto-produces if missing/stale)
3. Reads and returns the cached `session-model.json`

This helper is what consumers call instead of `build_chatlas_session_model_from_index_row`.

### Block: zip-transcript dependency chain

Currently `zip-transcript` depends on `source-session` (the raw index row). After this change:
- `chatlas-session` depends on `source-session` (via `identity_hash`)
- `zip-transcript` can optionally depend on `chatlas-session` instead of rebuilding from raw — but this is optimization, not required for slice 1

Keep `zip-transcript` unchanged in slice 1. Migrate it in a later slice.

## Execution.Plan

### Slice 1 — `SessionModelWorkflow` class + registration

**What changes**: New `SessionModelWorkflow` class following the `ZipTranscriptWorkflow` pattern. Artifact: `session-model.json`. Fingerprint: `identity_hash` from the source row. Register in `_registered_workflows()`.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/views/core.py` — add `SessionModelWorkflow` class, add `_SESSION_MODEL_ARTIFACT` constant, register in `_registered_workflows()`

**Observable result**: `agentos chatlas views list` shows `chatlas-session`. `agentos chatlas views get --view chatlas-session --session-id <id>` produces and returns the cached session model.

**Validation**: Run `agentos chatlas views list`, confirm `chatlas-session` appears. Run `views get` for a session, confirm artifact is created. Run again, confirm it returns `fresh` without rebuilding.

### Slice 2 — Consumer helper `load_chatlas_session_model`

**What changes**: Add `load_chatlas_session_model(row, *, chatlas_root=None)` to `views/core.py`. This function builds the context, calls `_ensure_available`, reads the cached JSON, and returns the session model dict. Export from `views/__init__.py`.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/views/core.py` — add `load_chatlas_session_model`
- `agentos-chatlas-py/src/agentos_chatlas/views/__init__.py` — export

**Observable result**: `from agentos_chatlas.views import load_chatlas_session_model` works in Python REPL. Returns same dict as `build_chatlas_session_model_from_index_row`.

**Validation**: Compare output of both functions for same row — must be identical.

### Slice 3 — Migrate `recents.py`

**What changes**: `_extract_last_user_turns` calls `load_chatlas_session_model` instead of `build_chatlas_session_model_from_index_row`.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/recents.py`

**Observable result**: `agentos chatlas recents --limit 10` is fast on second run (cache hit).

**Validation**: Time two consecutive runs. Second run should be significantly faster.

### Slice 4 — Migrate `query.py`

**What changes**: `_row_matches_standard_model_filters` calls `load_chatlas_session_model` instead of `build_chatlas_session_model_from_index_row`.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/query.py`

**Observable result**: `chatlas query --user-contains "something"` benefits from cache on repeated queries.

**Validation**: Run query with text filter, confirm results unchanged.

### Slice 5 — Migrate `session_model/_model.py` (export)

**What changes**: `chatlas_export_session_model` calls `load_chatlas_session_model` instead of `build_chatlas_session_model_from_index_row`.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/session_model/_model.py`

**Observable result**: `agentos chatlas export --session-id <id>` uses cache.

**Validation**: Compare export output before and after — must be identical.

### Slice 6 — Migrate `zip-transcript` view

**What changes**: `_zip_transcript_payload` reads from `chatlas-session` view instead of calling `build_chatlas_session_model_from_index_row` directly. The `zip-transcript` fingerprint can reuse the `chatlas-session` fingerprint since it's derived from the same source.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/views/core.py`

**Observable result**: `zip-transcript` production reuses cached session model.

**Validation**: Produce `zip-transcript` for a session, confirm output is unchanged.

### Risks

- **Circular import**: `load_chatlas_session_model` lives in `views/core.py` but consumers are in `query.py`, `recents.py`, `session_model/`. Since `views/core.py` already imports from `session_model`, adding an import from `query.py → views` may create a cycle. Mitigate by keeping the helper import lazy or placing it in a separate module.
- **Disk space**: Cached session models are large JSON files. Acceptable trade-off for speed.

## Impl.Log

(empty — not yet executed)
