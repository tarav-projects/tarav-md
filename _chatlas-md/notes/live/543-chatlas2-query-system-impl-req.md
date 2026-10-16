# Chatlas2 Query System - impl-req

## Impl.Abstract

- **scope:** add the first small Chatlas2 query system: `Session.Query` selects chats through the existing Session.Index, and `Chat.Query` finds authoritative `Chat.Message` records first within one session and then across a bounded Session.Query result set
- **status:** implemented and verified
- **source:** accepted query design and autonomous develop request in the current Chatlas2 design session
- **support set:** query scope, simplicity boundary, and autonomous authorization ^c20260816-64u
- **final validation MVP:** migrate `tarav-chatlas-my-session-id` from Chatlas1 discovery to the new Chatlas2 query path and use it to resolve this running session
- **out of scope:** Event.Pattern, tool/file-touch semantics, raw-artifact text search, SQLite or another global content index, a generic query DSL, Copilot normalization, compatibility aliases, or expanding the Chatlas2 Normal Model

## Impl.Agendix

- **touched (index):** `Chatlas.Query.Surface` — preserve the separation between cheap session selection and authoritative content matching
- **touched (index):** `Normalization.Pipeline::Chatlas.Session.Model` — query results come from the current cached Normal Model, never candidate rows
- **touched (index):** `Event.Ref` — returned message and turn references carry place plus current-state drift validation
- **touched (chat):** retain only useful Chatlas1 behavior inside Chatlas2's narrow message/turn promises; begin with one-session message query, then apply it to a Session.Query result set ^c20260816-64u
- **structural:** Session.Query reuses current Chatlas Session.Index mechanics; Chat.Query composes the transparent Chatlas2 Normal Model cache and `Scan.Decode.Verify`
- **open space:** no persistent cross-session full-text index is introduced; later performance evidence may justify one

## Impl.Index

### Query.Boundary

- `Session.Query` answers which chats are in scope using provider-neutral session metadata: identity, provider, project, activity time, sorting, and limits.
- `Chat.Query` answers which `Chat.Message` records match inside that selected session set.
- The single-session form and multi-session form use the same message predicate and result model.
- Chat.Query accepts only Chatlas2-supported provider families and reports sessions it cannot normalize instead of silently claiming complete coverage.

### Chat.Message.Query

- The primary subject is `Chat.Message`; turns are an optional containing-group projection, not a second text interpretation.
- Predicates cover user/agent side, exact/contains/regex/verbatim text, message time bounds, and message address.
- Every result carries session identity, `Chat.Message.Ref`, diagnostic `at`, and optionally the containing `Chat.Turn.Ref`.
- Results are deterministic and chronological by default; reverse chronology is an explicit projection.
- Limits count decoded, semantically verified matches only.

### Query.Authority

- Cached JSONL line scans may select candidates but cannot establish matches.
- Safe literal scans are preferred; broader or case-insensitive predicates may decode more records to avoid false negatives.
- Current Normal Model records are the only public result authority.
- Cache validation and recomputation remain transparent to query consumers.

### Self.Session.Validation

- A direct harness-provided native session ID remains the cheapest trustworthy path.
- Neutral identity enrichment uses Session.Query, never Chatlas1 query.
- When no direct ID exists, the skill bounds candidates with Session.Query and intersects Chat.Query matches for distinctive verbatim user fragments.
- The skill keeps large query payloads out of agent context and surfaces only the unique resolution or explicit ambiguity.

## Execution.Plan

### Vertical.Slice.1 - Session.Query

- **RED:** add service and CLI tests for exact identity/session selection plus provider/project/activity/sort/limit filtering and compact provider-neutral rows.
- **GREEN:** implement a thin Chatlas2 Session.Query over existing Session.Index mechanics and expose it beneath `tarav chatlas2 sessions query`.
- **observable:** callers can obtain a bounded set of Chatlas2-capable sessions without constructing Normal Models.
- **check:** focused query and CLI tests; existing Chatlas2 cache selection remains unchanged.
- **status:** complete

### Vertical.Slice.2 - Single-session Chat.Query

- **RED:** test side, exact/contains/regex/verbatim, before/after, address, chronological order, verified limits, refs, and containing-turn projection.
- **GREEN:** extend the cached message reader only where safe candidate selection is possible; add an authoritative query service and `tarav chatlas2 chat query` exact-session path.
- **observable:** one query returns stable message evidence without loading unrelated opaque turn payloads.
- **check:** focused cache/query/CLI tests against both Codex and Claude conformance sessions.
- **status:** complete

### Vertical.Slice.3 - Session-set Chat.Query

- **RED:** test the same message predicate across a bounded Session.Query result set, deterministic global ordering, result limits after verification, and explicit per-session normalization failures.
- **GREEN:** compose Session.Query rows with cache-transparent per-session readers without retaining complete Normal Models.
- **observable:** a distinctive user fragment locates messages across recent selected chats while preserving exact session and message refs.
- **check:** multi-session fixtures covering Codex and both Claude raw versions.
- **status:** complete

### Vertical.Slice.4 - Self-session discovery MVP

- **RED:** audit `tarav-chatlas-my-session-id` for every Chatlas1 command and add a documentation/command contract check that rejects those dependencies.
- **GREEN:** rewrite direct enrichment and fallback discovery around Chatlas2 Session.Query and Chat.Query, retaining inline execution, bounded payload handling, and ambiguity safety.
- **observable:** the updated skill resolves this running Codex session and its neutral identity using only the harness plus Chatlas2 query commands.
- **check:** run the documented direct path and a forced fallback fragment intersection; confirm both identify `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8` / `bc3e97379260c6592f1ac7cc4cad0c8fc0f355719898e6a6464d5f6583ec7577` without invoking `tarav chatlas`.
- **status:** complete

### Vertical.Slice.5 - Reconciliation

- update maintained Chatlas2 architecture guidance, package exports, and the Impl.Req status/log.
- run focused tests, all `tests/chatlas2`, architecture checks, Ruff, CLI help, live Codex/Claude queries, and the self-session MVP.
- inspect the complete diff without altering unrelated uncommitted Chat.Index work.
- **status:** complete

## Impl.Log

- **2026-08-16:** Execution gate: the autonomous develop invocation is grounded through Chatlas2 message support ^c20260816-64u.
- **2026-08-16:** Before implementation edits, checkpointed the complete existing state in `tarav-py` (`4c1e1f3`) and `tarav-chatlas-md` (`ae76a2a`) as required by the execution workflow.
- **2026-08-16:** The user added `tarav-chatlas-my-session-id` as the final validation MVP after identifying its stale Chatlas1 enrichment path; incorporated as the last functional slice rather than a separate implementation request.
- **2026-08-16:** Implemented bounded Session.Query and authoritative single-/multi-session Chat.Message query without adding Event.Pattern, provider tool semantics, raw search, or another persistent index.
- **2026-08-16:** Migrated `tarav-chatlas-my-session-id` to Chatlas2-only discovery. Both its direct harness-ID path and forced two-fragment fallback resolved the running session to `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8` / `bc3e97379260c6592f1ac7cc4cad0c8fc0f355719898e6a6464d5f6583ec7577`.
- **2026-08-16:** Reconciliation passed: 12 focused query tests, 99 Chatlas2/architecture tests, Ruff, CLI help, no executable Chatlas1 command in the self-session skill, and live message queries over Codex plus Claude `1ecc` and legacy `b17b` sessions.
