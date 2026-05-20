# 537 — chatlas recents — Impl.Req

## Impl.Abstract

| Field | Value |
|---|---|
| Status | ready |
| Scope | New `agentos chatlas recents` command — human-readable summary of recent sessions with last user turn(s) |
| Source | In-chat design discussion (this session) |
| Target package | `agentos-chatlas-py` (`agentos_chatlas`) |

### Intent

Add a convenience command that prints a chronological summary of sessions updated in a recent window. Each entry shows timestamp, provider, identity hash, and the last N visible user turn(s). Default output is human-readable text; `--json` switches to machine-readable.

### Key design decisions

- Standalone command: `agentos chatlas recents` (not an alias or flag on `chatlas query`).
- Reuses `chatlas_query` pipeline internally — computes `updated_after` from `--days`.
- `--days N` flag, default 3.
- `--last-turns N` flag, default 1 — controls how many trailing user turns to include per session.
- Chronological order: `sort=oldest`.
- Human-readable default, `--json` for JSON output.
- Last user turn(s) truncated to 200 chars by default; `--full` disables truncation.
- Full `identity_hash` included (actionable for follow-up commands).

## Impl.Index

### Block: query pipeline reuse
- `chatlas_query()` in `core.py` already accepts `updated_after`, `sort`, `limit`, `min_user_turns`.
- `recents` computes `updated_after = now - days` as ISO 8601 and passes `sort="oldest"`.
- No changes needed to the query engine.

### Block: user turn extraction
- `_visible_message_texts(session_model, roles={"user"})` in `query.py` already extracts all visible user turns from a session model.
- `build_chatlas_session_model_from_index_row(row)` builds the session model from a full index row.
- `recents` needs full rows (`row_shape="full"`) to build session models for turn extraction.
- Last N turns = `user_texts[-last_turns:]`.

### Block: human output format
- One block per session, separated by blank line:
  ```
  2026-05-17 14:32  codex  sha256:6726da7e725a862b24adb815dddd4b701388dd3897986b94dd72de596429a97c
    "refactor the auth module to use JWT tokens"
  ```
- Timestamp is `updated_at` truncated to minute precision.
- When `--last-turns` > 1, each turn on its own indented line.
- Truncation appends `…` when text exceeds limit.

### Block: CLI wiring
- New subcommand `recents` registered in `register_chatlas_commands`.
- Flags: `--days` (int, default 3), `--last-turns` (int, default 1), `--full` (store_true), `--json` (store_true).
- Also accepts `--provider` for filtering (reuse `_add_chatlas_provider_argument`).
- Also accepts `--min-user-turns` (reuse; useful to skip empty sessions).
- Also accepts `--limit`.

## Execution.Plan

### Slice 1 — Core function `chatlas_recents` + human formatter

**What changes**: New function `chatlas_recents()` in `agentos_chatlas/recents.py`. Takes `days`, `last_turns`, `truncate_length`, `providers`, `min_user_turns`, `limit`. Calls `chatlas_query()` with computed `updated_after` and `sort="oldest"`, `row_shape="full"`. Iterates rows, builds session model, extracts last N user turns, returns structured result. Companion `format_chatlas_recents_text()` formats the human output.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/recents.py` — new file
- `agentos-chatlas-py/src/agentos_chatlas/core.py` — add `chatlas_recents` facade (thin delegation)

**Observable result**: `from agentos_chatlas.core import chatlas_recents; print(chatlas_recents(days=3))` returns structured data with last user turns.

**Validation**: Python REPL — call with `days=1`, confirm rows come back with `last_user_turns` populated. Call `format_chatlas_recents_text()` and inspect text output.

### Slice 2 — CLI registration

**What changes**: Wire `agentos chatlas recents` subcommand in `commands.py`.

**Files**:
- `agentos-chatlas-py/src/agentos_chatlas/commands.py` — add `_cmd_chatlas_recents`, register `recents` subparser with `--days`, `--last-turns`, `--full`, `--json`, `--provider`, `--min-user-turns`, `--limit`.

**Observable result**: `agentos chatlas recents` prints human-readable output. `agentos chatlas recents --json` prints JSON. `agentos chatlas recents --days 1 --last-turns 3 --full` shows 3 full user turns per session from last day.

**Validation**: Run all flag combinations against live chatlas data and inspect output.

## Impl.Log

(empty — not yet executed)
