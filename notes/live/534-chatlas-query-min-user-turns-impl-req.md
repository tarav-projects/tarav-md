# Chatlas Query — min-user-turns filter — impl-req

## Impl.Abstract

- **scope:** add `--min-user-turns` filter to `chatlas query` and switch `chatlas run-produce` to use `chatlas query` (gaining all query filters)
- **status:** ready for execution
- **source:** discussion in chatlas-produce implementation session

## Impl.Index

### Standard.Model.Turn.Count.Filter

- `chatlas query` already has standard-model filters (`--user-contains`, `--assistant-contains`, `--message-contains`) that build the session model per candidate
- `_row_matches_standard_model_filters` in `chatlas/query.py` is the entry point — it builds the session model, extracts visible messages, and checks filters
- the user turn count is the length of `_visible_message_texts(session_model, roles={"user"})` — already computed when other standard-model filters are active
- when `min_user_turns` is the only standard-model filter, the session model still needs to be built (same cost as `--user-contains`)
- the guard at line 120 (`if not user_contains and not assistant_contains and not message_contains: return True`) needs to include `min_user_turns`

### Run.Produce.Query.Switch

- `chatlas run-produce` currently calls `chatlas_index_query()` which returns raw index rows — no standard-model filtering
- switching to `chatlas_query()` gives access to all query filters: `--raw-contains`, `--user-contains`, `--assistant-contains`, `--message-contains`, `--scan-limit`, and the new `--min-user-turns`
- **key issue:** `chatlas_query` returns normalized rows via `_normalized_session_row()` which drops `identity_hash` and `instance` — but `run-produce` needs `identity_hash` for prompt building via `_session_selector_flags()`
- **fix:** add `identity_hash` and `instance` to `_normalized_session_row()` — these are stable index fields that downstream consumers need

### CLI.Query.Args.Reuse

- `chatlas query` CLI has its own argument block (lines 488–571 of `commands.py`) — not factored into a reusable helper like `_add_chatlas_index_selector_arguments`
- `run-produce` currently uses `_add_chatlas_index_selector_arguments` (index-level selectors)
- after the switch, `run-produce` needs the full query argument set: index selectors + `--scan-limit` + `--raw-contains` + `--user-contains` + `--assistant-contains` + `--message-contains` + `--min-user-turns`
- extract a `_add_chatlas_query_selector_arguments` helper from the `chatlas query` registration block, reuse in both `chatlas query` and `chatlas run-produce`

## Execution.Plan

### Slice 1 — Add `min_user_turns` to `run_chatlas_query`

- add `min_user_turns: int | None = None` parameter to `run_chatlas_query()` and `chatlas_query()`
- pass it through to `_row_matches_standard_model_filters`
- in `_row_matches_standard_model_filters`: include `min_user_turns` in the early-return guard; when set, count `len(user_texts)` and reject if below threshold
- add `min_user_turns` to the `filters` dict in the query result
- **changes:** `chatlas/query.py`, `chatlas/core.py`
- **validation:** `uv run python -c "from agentos.chatlas.core import chatlas_query; r = chatlas_query(sort='newest', limit=5, min_user_turns=3); print(r['returned_row_count'])"` returns fewer rows than without the filter

### Slice 2 — Add `identity_hash` and `instance` to normalized query rows

- add `identity_hash` and `instance` to `_normalized_session_row()` in `chatlas/query.py`
- **changes:** `chatlas/query.py`
- **validation:** query result rows now include `identity_hash` field

### Slice 3 — Extract `_add_chatlas_query_selector_arguments` helper

- extract the query-specific arguments (`--scan-limit`, `--raw-contains`, `--user-contains`, `--assistant-contains`, `--message-contains`) plus the new `--min-user-turns` into `_add_chatlas_query_selector_arguments` in `commands.py`
- this helper calls `_add_chatlas_index_selector_arguments` first, then adds the query-level args
- add a `_chatlas_query_selector_kwargs` helper that extends `_chatlas_index_selector_kwargs` with the query-level fields
- refactor `chatlas query` CLI registration to use the new helper
- **changes:** `chatlas/commands.py`
- **validation:** `agentos chatlas query --help` output unchanged (plus `--min-user-turns`)

### Slice 4 — Switch `run-produce` to use `chatlas_query`

- change `_cmd_chatlas_run_produce` to call `chatlas_query()` instead of `chatlas_index_query()`
- use `_add_chatlas_query_selector_arguments` and `_chatlas_query_selector_kwargs` for the `run-produce` subcommand
- **changes:** `chatlas/commands.py`
- **validation:** `agentos chatlas run-produce --help` shows `--min-user-turns`, `--user-contains`, etc.; `agentos chatlas run-produce --view zip-transcript-agent-summary --dry-run --min-user-turns 3 --sort newest --limit 2` shows prompts only for sessions with 3+ user turns

## Impl.Log

(empty — not yet started)
