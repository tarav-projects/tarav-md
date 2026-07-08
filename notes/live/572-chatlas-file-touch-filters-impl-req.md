# Chatlas File-Touch Filters — Impl.Req

## Impl.Abstract

- **Goal**: answer "which sessions read/wrote a given file" and "where in the session" from the normal model — `--file-read` / `--file-write` / `--file-touched` on `chatlas query` (which sessions) and `views inline` (which invocations/events).
- **Scope**: a file-touch extractor over `chat.tool_invocations` in model-space code; the three flags on both surfaces; substring path matching; explicit-path tools only.
- **Out of scope**: Bash command-string parsing (the long tail — a `git commit` or `rm` via Bash is invisible to v1; documented blind spot, added when workflows demand); finer verbs (create/modify/delete — "write" means a mutating tool invocation carried the path, nothing finer, user decision); provider tool vocabularies beyond what the normal model already carries.
- **Repos**: `agentos-chatlas-py` only (`normalization/session_model/` new extractor module, `query.py`, `inline.py`, `commands.py`, `tests/test_e2e_chatlas.py`); `agentos-chatlas-md` reference/index updates in the final slice.
- **Source**: this design session — live verification that `chat.tool_invocations` carries `tool_name`, `input.arguments.file_path`, `output`, timestamps, `event_refs` (709 invocations in session `9d194db7…`; the 563-note Write recovered with full path and events); index concepts `Chatlas.Session.Model`, `Chatlas.Query.Envelope`, `Chatlas.View`, `Chatlas.Filter`.
- **Status**: implemented (2026-07-08); all three slices, suite 131 green, live-verified (563-note writer found, mentioner excluded)

## Impl.Index

### Touch.Semantics
- a *touch* is a tool invocation whose explicit path argument matches the query path
- tool classes: read = `Read` (and read-shaped tools with explicit path args); write = `Write`, `Edit`, `NotebookEdit`; touched = union
- the tool→class and tool→path-argument knowledge lives in ONE table in the extractor module — extending coverage is a table edit, not logic
- path matching is substring, consistent with the `*-contains` filter family — `--file-write "filters.py"` matches the absolute path in the invocation
- Bash and command-string tools are out: v1 reports only explicit-path touches; the blind spot is documented in the reference

### Extractor.Contract
- new module in `normalization/session_model/` (model-space code owns model-space operations, same placement rationale as `filters.py`)
- `file_touch_invocations(session_model, path, mode)` → the matching `tool_invocations` rows; `mode ∈ {read, write, touched}`
- pure read; no new output shape — results are existing model rows

### Query.Surface
- `--file-read <path>`, `--file-write <path>`, `--file-touched <path>` on `agentos chatlas query` — standard-model filter layer of `Chatlas.Query.Envelope` (same layer as `--message-contains`), so scan limits and count accounting apply unchanged
- flags may repeat/combine like the other contains-filters; a session matches when any invocation matches
- rows returned unchanged (model-closed) — no bespoke resolution payload

### Inline.Surface
- same three flags on `views inline` — select the matching invocations' `event_refs` and keep only those events in the fragment (the touching moments), then normal view/filter pipeline applies
- composes with `--around`, `--radius`, `--filter`, `--anchor` like every other selection
- selection flags already imply `--view events` when no view is named; file-touch flags join that rule

### Grounding.Tie
- a file-touch is `Hard.Evidence` linking a session to a code surface — the code-side analogue of chat anchors; `--file-touched` + `views inline` = "find the evidence turn" for code changes, feeding the same `Index.Linking` pipeline

## Execution.Plan

### S1 — Extractor + query flags (test-first)
- what changes: extractor module with the tool table; three flags in `query.py`/`commands.py` at the standard-model filter layer
- RED (`tests/test_e2e_chatlas.py`; fixtures need tool-invocation events — extend the codex rollout writer or add a fixture with Read/Write invocations): `--file-write <basename>` matches only the writing session; `--file-read` matches only the reading one; `--file-touched` matches both; substring matching (basename hits absolute path); a session merely *mentioning* the path in prose does NOT match; unknown/no-touch path → empty result, well-formed envelope
- check: suite green; live: `agentos chatlas query --file-write "563-anchor-system-handoff" --field identity_hash` returns exactly this session (the 568-executer session mentioned it but never wrote it)
- observable: mention vs touch distinguished — the query the old filters could not answer

### S2 — Inline surface
- what changes: the three flags on `views inline`; selection keeps events referenced by matching invocations
- RED: `views inline --identity-hash <H> --file-write <path>` returns only the writing invocation's events; composes with `--filter slim`; no-match → empty well-formed fragment
- check: suite green; live: the 563-note Write moment retrievable as a fragment
- observable: "where in the session was this file touched" is one command

### S3 — Surfaces + docs
- what changes: `chatlas-commands.md` gains a "File Touch Workflow" section (with the Bash blind-spot note); `agentos-index` `link.md`/`ground.md` mention the code-side evidence path where natural; propose (gated, do not self-write) a `[DC]` line for the chatlas index — e.g. on `Chatlas.Query.Surface`: file-touch filters answer which sessions touched a file from the normal model
- check: reference examples runnable as written

### Acceptance signals
- `query --file-touched <path>` returns touching sessions only (mentions excluded); `views inline --file-touched <path>` returns the touching moments as model fragments
- full `agentos-chatlas-py` suite green; `No.Regression.Tests.Allowed` respected

### Risks / deviation triggers
- fixture realism: the codex rollout fixture writer may not produce tool-invocation records — if extending it balloons, add a dedicated fixture file rather than weakening assertions
- tool-name variance across providers: the table starts from what the normal model actually carries (inspect fixtures + live sessions); unknown tools simply never match — silent, safe
- if invocation→`event_refs` linkage proves incomplete for some provider, stop and surface — that is a normalization gap, not open space

## Impl.Log

- 2026-07-08: executed in `Alignment.Mode:Autonomous`; 6 new behavior tests; fixture writer extended with `tool_calls` (codex `function_call`/`function_call_output` pairs).
- open-space decision (S1): query flags are repeatable with AND semantics across repeats, matching the `*-contains` family convention.
- open-space decision (S2): inline file-touch flags are single-valued (one path per flag) — the inline surface selects one file's moments; widen only on demand.
- open-space decision (S2): inline selection keeps exactly the events in the matching invocations' `event_refs` (call + output events); message events are naturally excluded unless referenced.
- deviation: none — plan followed as written; the fixture-realism risk did not fire (rollout writer extension was small).
- gated follow-up proposed to the user (not self-written): a `[DC]` line on `Chatlas.Query.Surface` for file-touch filters.
- 2026-07-08 follow-up (user-requested after a live blind-spot hit): recall tier added — `--tool-contains` (+ `--tool-name`) on query and views inline; substring over the whole invocation, no verb claim, the reader judges. Two-tier model: semantic file-touch (precise verb, limited coverage) over general tool-contains (total coverage, reader-judged). 2 new tests; suite 133 green. The gated `[DC]` for `Chatlas.Query.Surface` was written to its appendix per user instruction.
