# Chatlas Produce — impl-req

## Impl.Abstract

- **scope:** new `agentos chatlas produce` command — launches an agent to produce an external chatlas view, supporting batch operation over query results
- **status:** slices 1-3 (v1 single-session) implemented, multi-session iteration in progress
- **source:** design discussion — chatlas produce feature, session context

The goal is a thin CLI launcher: run a query, pass results to the view's prompt iterator, run one agent per yielded prompt as a terminal process. The agent operates the full stage-produce-commit cycle exactly like any external operator.

No Python-side artifact parsing, no output capture, no orchestration beyond prompt building and sequential iteration.

## Impl.Index

### Core.Concept

- `chatlas produce` is a CLI command that automates external view production by delegating to an agent
- the agent is the operator — it runs the existing stage/produce/commit workflow via CLI commands
- the Python side only builds prompts and launches processes
- `process_mode="terminal"` — agent output goes straight to the terminal, no capture

### Query.Driven.Selection

- `chatlas produce` accepts the same query arguments as `chatlas query` — this is the session selection mechanism
- the query returns N rows
- rows are passed to the view's prompt iterator
- there is one path: query → rows → prompt iterator → sequential agent runs
- single-session is just the N=1 case, no special handling

### Prompt.Iterator.On.View

- each `ChatlasViewWorkflow` that supports agent production defines `produce_prompts(rows) -> Iterator[str]`
- the iterator receives the query result rows and yields one prompt per unit of work
- the view decides the mapping — for `zip-transcript-agent-summary`, it yields one prompt per row
- other views could yield differently (e.g., batch, skip already-fresh, etc.)
- the prompt tells the agent which skill/reference to load and which session to target
- for `zip-transcript-agent-summary`, the prompt points at `chatlas-usage/references/producer-zip-transcript-agent-summary.md`
- views that do not support produce raise `CliError`

### Agent.Resolution

- `chatlas produce` takes `--agent-provider` (and optionally `--profile`, `--model`) to resolve the agent
- uses existing `resolve_agent()` from `agent/providers.py`
- uses existing `AgentCommandConfig` and `AgentRunConfig` from `agent/run_runtime.py`
- `interaction_mode="non_interactive"` since the prompt is fully specified

### CLI.Shape

- command: `agentos chatlas produce --view <view-name> --agent-provider <provider> [query selectors] [--model ...] [--profile ...] [--dry-run]`
- query selectors: same set as `chatlas query` (`--uri`, `--identity-hash`, `--session-id`, `--updated-after`, `--limit`, etc.)
- `--dry-run`: show the prompts and agent commands without executing
- returns 0 if all agent runs succeed, non-zero otherwise

### Existing.Infra.Reuse

- `resolve_agent()` — agent resolution from config
- `agent.run(command_config, run_config)` — terminal process execution
- `agent.run_dry(command_config)` — dry run support
- query selectors — same `_add_chatlas_index_selector_arguments` and `_chatlas_index_selector_kwargs` helpers
- the existing producer reference at `chatlas-usage/references/producer-zip-transcript-agent-summary.md` already describes the full agent workflow
- the existing `SKILL.md` at `agentos-session-zip-transcript` already describes the caller contract and subagent prompt shape

### Selector.To.Prompt

- the prompt iterator needs to convert each row's fields into CLI flag strings for the agent
- the agent will use these flags in its own `agentos chatlas views ...` commands
- the selectors come from index row fields like `identity_hash`, `uri`, `session_id`
- prefer `--identity-hash` when available as it is the most stable selector

## Execution.Plan

### Slice 1 — Prompt builder on view workflow (done)

- added `build_produce_prompt(context) -> str` to the `ChatlasViewWorkflow` protocol
- implemented on `ZipTranscriptAgentSummaryWorkflow` and `ZipTranscriptWorkflow`
- added `_session_selector_flags()` helper
- **changes:** `agentos-py/src/agentos/chatlas/views/core.py`

### Slice 2 — `chatlas_produce` orchestrator function (done, needs update)

- added `chatlas_produce()` in `chatlas/views/core.py`
- currently uses `_context_from_selector` (single-session path)
- **needs update:** replace with query-based multi-row path and prompt iterator loop

### Slice 3 — CLI wiring (done, needs update)

- added `produce` subcommand with `--agent-provider`, `--profile`, `--model`, `--dry-run`, session selectors
- **needs update:** selectors should match `chatlas query` capabilities, not just single-session selectors

### Slice 4 — Refactor: prompt iterator and multi-session loop

- rename `build_produce_prompt` to `produce_prompts` on the `ChatlasViewWorkflow` protocol
- signature: `produce_prompts(rows: list[dict]) -> Iterator[str]`
- `ZipTranscriptAgentSummaryWorkflow.produce_prompts` yields one prompt per row
- `ZipTranscriptWorkflow.produce_prompts` raises `CliError`
- update `chatlas_produce()` orchestrator:
  - accept query result rows instead of single-session selectors
  - resolve the workflow
  - call `workflow.produce_prompts(rows)` to get the iterator
  - loop: for each prompt, build `AgentCommandConfig`, run agent, track results
  - return summary with per-session exit codes
- update CLI handler to run the query first, then pass rows to `chatlas_produce()`
- **changes:** `chatlas/views/core.py`, `chatlas/commands.py`
- **validation:** `--dry-run` with `--limit 3` shows 3 prompts; live run processes sessions sequentially

### Slice 5 — End-to-end validation

- run `agentos chatlas produce --view zip-transcript-agent-summary --agent-provider codex --profile codex-main --model gpt-5.4-mini --session-id <id>` — single session
- run `agentos chatlas produce --view zip-transcript-agent-summary --agent-provider claude-code --updated-after 2026-05-14 --limit 3` — batch of 3
- confirm view state is `fresh` for each processed session
- **validation:** all targeted sessions show `fresh` state after completion

## Impl.Log

### 2026-05-15 — Slices 1-3 (v1 single-session)

Implemented initial version with single-session support:
- `build_produce_prompt()` on protocol + both workflows
- `chatlas_produce()` orchestrator with terminal agent execution
- CLI wiring as `agentos chatlas produce` with `--agent-provider` (renamed from `--provider` to avoid conflict with chatlas provider selector)
- `_session_selector_flags()` helper for identity_hash/uri/session_id preference
- dry-run and live run tested successfully against real sessions
- pending: refactor to multi-session prompt iterator (slice 4)
