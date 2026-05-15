# Chatlas Produce — impl-req

## Impl.Abstract

- **scope:** two commands — `chatlas produce` (universal produce) and `chatlas run-produce` (agentic batch runner)
- **status:** v1 single-session agent-spawning implemented under `chatlas produce`, needs refactor into the two-command split
- **source:** design discussion — chatlas produce feature, session context

Two commands with distinct roles:

- **`chatlas produce`** — universal produce. Internal views: produces programmatically. External views: outputs the production prompt to the terminal. No agent spawning. Works as a building block for any agent or workflow.
- **`chatlas run-produce`** — chatlas-managed agentic batch runner. Runs a query, iterates prompts from the view, spawns one agent per prompt sequentially as terminal processes.

## Impl.Index

### Two.Command.Split

- `chatlas produce` is the prompt surface — it answers "what needs doing"
  - internal view: runs `workflow.produce(context)` directly (programmatic production, already exists)
  - external view: calls the view's prompt builder and prints the prompt to stdout
  - no agent provider args, no agent spawning
  - usable by any agent — an agent calls `agentos chatlas produce`, reads the prompt, acts on it
  - single-session selectors (same as existing view commands)
- `chatlas run-produce` is the execution surface — it answers "do it with this agent"
  - takes `--agent-provider`, `--profile`, `--model`
  - runs a query (same args as `chatlas query`) → N rows
  - passes rows to the view's prompt iterator → yields prompts
  - for each prompt: resolves agent, runs as terminal process (`process_mode="terminal"`)
  - single-session is just the N=1 case

### Produce.On.Workflow

- the existing `produce(context)` method on `ChatlasViewWorkflow` stays as-is for internal views
- for external views, `produce(context)` currently raises `CliError` — this changes to return the prompt string instead
- the view protocol gains a `produce_prompts(rows) -> Iterator[str]` for the multi-row batch path used by `run-produce`
- `produce` (single) and `produce_prompts` (batch) are related but distinct:
  - `produce` works from a resolved context (single session, used by `chatlas produce` CLI)
  - `produce_prompts` works from raw query rows (N sessions, used by `chatlas run-produce` CLI)
  - for external views, `produce_prompts` yields one prompt per row — each prompt is what `produce` would return for that row

### Prompt.Shape

- for `zip-transcript-agent-summary`, the prompt points at `chatlas-usage/references/producer-zip-transcript-agent-summary.md`
- includes the session selector flags derived from the row (`--identity-hash` preferred)
- `_session_selector_flags()` helper converts row fields to CLI flags

### Agent.Resolution (run-produce only)

- `chatlas run-produce` takes `--agent-provider` (and optionally `--profile`, `--model`) to resolve the agent
- uses existing `resolve_agent()` from `agent/providers.py`
- uses existing `AgentCommandConfig` and `AgentRunConfig` from `agent/run_runtime.py`
- `interaction_mode="non_interactive"` since the prompt is fully specified

### CLI.Shapes

- `agentos chatlas produce --view <view-name> [session selectors] [--explain]`
  - internal view: produces and prints result (JSON)
  - external view: prints the production prompt
- `agentos chatlas run-produce --view <view-name> --agent-provider <provider> [query selectors] [--model ...] [--profile ...] [--dry-run]`
  - query selectors: same set as `chatlas query`
  - `--dry-run`: show prompts and agent commands without executing
  - returns 0 if all agent runs succeed, non-zero otherwise

### Existing.Infra.Reuse

- `resolve_agent()` — agent resolution from config
- `agent.run(command_config, run_config)` — terminal process execution
- `agent.run_dry(command_config)` — dry run support
- `_ensure_available()` — already handles internal produce path
- query selectors — `_add_chatlas_index_selector_arguments` and `_chatlas_index_selector_kwargs`
- producer reference at `chatlas-usage/references/producer-zip-transcript-agent-summary.md`

### Selector.To.Prompt

- prompt builder converts row fields into CLI flag strings for the agent
- prefer `--identity-hash` when available as it is the most stable selector
- `_session_selector_flags()` helper already implemented

## Execution.Plan

### Slice 1 — Prompt builder on view workflow (done)

- added `build_produce_prompt(context) -> str` to the `ChatlasViewWorkflow` protocol
- implemented on `ZipTranscriptAgentSummaryWorkflow` and `ZipTranscriptWorkflow`
- added `_session_selector_flags()` helper
- **changes:** `agentos-py/src/agentos/chatlas/views/core.py`

### Slice 2 — `chatlas_produce` orchestrator + CLI (done, needs refactor)

- added `chatlas_produce()` and CLI `produce` subcommand with agent-spawning
- **needs refactor:** split into `produce` (no agent) and `run-produce` (with agent)

### Slice 3 — Refactor `chatlas produce` to universal produce

- remove agent-spawning from `chatlas_produce()`
- for internal views: call `_ensure_available(context)` — returns the view result (already works)
- for external views: call `workflow.build_produce_prompt(context)` — return the prompt
- update CLI: remove `--agent-provider`, `--profile`, `--model`, `--dry-run` from `produce`
- keep session selectors (single-session, same as `chatlas views get`)
- output: JSON with view result (internal) or prompt string (external)
- **changes:** `chatlas/views/core.py`, `chatlas/commands.py`
- **validation:** `agentos chatlas produce --view zip-transcript --session-id <id>` produces programmatically; `agentos chatlas produce --view zip-transcript-agent-summary --session-id <id>` prints the prompt

### Slice 4 — Add `produce_prompts` iterator to workflow protocol

- add `produce_prompts(rows: list[dict]) -> Iterator[str]` to `ChatlasViewWorkflow` protocol
- `ZipTranscriptAgentSummaryWorkflow.produce_prompts` yields one prompt per row (reuses `_session_selector_flags`)
- `ZipTranscriptWorkflow.produce_prompts` raises `CliError` (internal views don't need batch agent production)
- **changes:** `chatlas/views/core.py`
- **validation:** calling `produce_prompts` with 3 rows yields 3 prompt strings

### Slice 5 — Add `chatlas run-produce` command

- add `chatlas_run_produce()` orchestrator function
  - takes: view name, provider, profile, model, query result rows, dry_run, cwd
  - resolves the workflow
  - calls `workflow.produce_prompts(rows)` → iterator
  - for each prompt: resolve agent, build `AgentCommandConfig`, run as terminal process
  - track per-prompt exit codes, return summary
- add `run-produce` CLI subcommand under `chatlas_subparsers`
  - arguments: `--view`, `--agent-provider`, `--profile`, `--model`, `--dry-run`, query selectors (same as `chatlas query`)
  - handler runs the query, passes rows to `chatlas_run_produce()`
- **changes:** `chatlas/views/core.py`, `chatlas/views/__init__.py`, `chatlas/commands.py`
- **validation:** `agentos chatlas run-produce --view zip-transcript-agent-summary --agent-provider claude-code --dry-run --limit 3` shows 3 prompts and commands

### Slice 6 — End-to-end validation

- `agentos chatlas produce --view zip-transcript --session-id <id>` — internal produce
- `agentos chatlas produce --view zip-transcript-agent-summary --session-id <id>` — prints prompt
- `agentos chatlas run-produce --view zip-transcript-agent-summary --agent-provider codex --profile codex-main --model gpt-5.4-mini --session-id <id>` — single session agent run
- `agentos chatlas run-produce --view zip-transcript-agent-summary --agent-provider claude-code --updated-after 2026-05-14 --limit 3` — batch of 3
- **validation:** all targeted sessions show `fresh` state after completion

## Impl.Log

### 2026-05-15 — Slices 1-2 (v1 single-session agent-spawning)

Implemented initial version with single-session agent-spawning under `chatlas produce`:
- `build_produce_prompt()` on protocol + both workflows
- `chatlas_produce()` orchestrator with terminal agent execution
- CLI wiring as `agentos chatlas produce` with `--agent-provider`
- `_session_selector_flags()` helper for identity_hash/uri/session_id preference
- dry-run and live run tested successfully against real sessions
- pending: refactor into two-command split (`produce` + `run-produce`)
