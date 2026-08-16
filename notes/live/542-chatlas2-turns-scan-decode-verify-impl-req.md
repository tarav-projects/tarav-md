# Chatlas2 Turns and Scan.Decode.Verify - impl-req

## Impl.Abstract

- **Status:** Implemented and verified.
- **Scope:** Add the shallow `Chat.Turn` projection to Chatlas2, materialize compact turn records in the Normal Model cache, hydrate selected turns on demand, and apply `Scan.Decode.Verify` to cached JSONL reads.
- **Source design:** `527-chatlas2-normal-model-redesign-design-session.md`, especially `Chat.Turn`, `Normal.Model.Cache`, and `Scan.Decode.Verify` (`d20260816-22u` through `d20260816-36u`).
- **Authorization:** The current autonomous develop invocation is grounded by `d20260816-37u`.
- **Out of scope:** Deep interpretation of tools, reasoning, compactions, forks, or harness records; new raw-model versions; Chatlas1 consumer cutover; persistent migration machinery; Copilot normalization.
- **Acceptance:** Codex and both Claude raw families produce conservative user/agent turns containing every `Chat.Message`; caches expose independent turn JSONL; selected turns hydrate without loading the full model; textual prefilters never determine semantic truth or risk false-negative query results.

## Impl.Index

### Chat.Turn.Projection

- A `Chat.Turn` is a shallow side-resolved grouping over the existing event tape, not another event spine or a parser for provider-specific semantics.
- After the lossless multi-artifact event union, assembly derives maximal contiguous runs of resolved `user` or `agent` events; unresolved events break runs and remain ungrouped.
- A turn address derives from provider, session scope, and the stable address of its first member event. Deriving turns after the event union prevents a shorter overlapping artifact from truncating a longer continuation.
- Every message event must resolve into exactly one same-side containing turn. A turn may contain zero, one, or several messages.
- Compact turn records carry ordered `Event.Ref` and `Chat.Message.Ref` membership. `Chat.Turn.Hash` covers side, ordered event state, and ordered opaque payload digests.
- Each event carries a provider-neutral opaque payload digest computed from its complete native JSON record. The digest is excluded from `Event.Hash` and `Chat.Message.Hash`, preserving their existing narrower semantics while making whole-turn drift observable.

### Turn.Cache.And.Hydration

- Normal Model schema advances for `annotations.chat_turns`; cache schema advances for `chat-turns.jsonl` and its count.
- Message cache records remain rich in parsed transcript text. Turn cache records remain compact and retain refs rather than duplicating event or raw payload objects.
- A selected turn can be resolved by turn address or containing message address. Hydration loads only its member events and messages, then reads only the cited raw source lines to expose opaque observations.
- Hydration is a disposable read projection; it does not attach raw data to the cached Normal Model.

### Scan.Decode.Verify

- The JSONL reader accepts an optional raw-line candidate scan, decodes only accepted candidates, and yields only JSON objects.
- Candidate scans compose exact serialized literals first and a compiled regular expression only when broader address selection needs it.
- Message side/text filters, turn side/address filters, and multi-event selection verify every candidate against the decoded object.
- Query limits count verified matches only. When no safe complete textual candidate can be formed, the reader decodes every line.

### Compatibility.And.Surface

- Chatlas2 is experimental: replace schema-v5 cache/model expectations with schema v6 rather than adding compatibility shims.
- Add a minimal `tarav chatlas2 turns list|get` surface; `get --hydrate` returns the selected compact turn plus member messages, events, and cited native observations.
- Preserve current message grounding behavior and existing Chatlas2 Anchory records; this pass introduces no anchor migration mechanism.
- Update Chatlas2 package exports, corpus validation/signatures, focused tests, CLI tests, and the maintained Chatlas2 section of `tarav-py/AGENTS.md`.

## Impl.Agendix

- **Touched chat authorization:** `d20260816-37u`.
- **Touched design:** `Chat.Turn` (`d20260816-22u`–`d20260816-28u`), cache split and hydration (`d20260816-29u`–`d20260816-31u`), and `Scan.Decode.Verify` (`d20260816-32u`–`d20260816-36u`).
- **Structural source:** `527-chatlas2-normal-model-redesign-design-session.md`.
- **Current implementation evidence:** `tarav-py/src/tarav/chatlas2/{model,pipeline,cache,codex,claude,messages,views,commands}.py` and `tarav-py/tests/chatlas2/`.

## Execution.Plan

### Vertical.Slice.1 — Turn model and provider normalization

- **Status:** Complete.

- **RED:** Add focused Codex and Claude tests proving same-side turn grouping, message containment, unresolved-event exclusion, stable turn refs, and whole-turn payload drift.
- **GREEN:** Add turn identity/hash/ref operations, extend `NormalFragment`, derive turn candidates in both provider normalizers through shared shallow grouping, and finalize/deduplicate turns in the pipeline.
- **Check:** Run turn-ref, Codex, Claude, pipeline, and corpus model tests.
- **Risk:** A generic grouping rule may claim an association unsupported by provider evidence. Deviation trigger: a corpus specimen shows a resolved-origin adjacency that is not a defensible conversational-turn grouping.

### Vertical.Slice.2 — Cache, Scan.Decode.Verify, and hydration

- **Status:** Complete.

- **RED:** Add cache tests proving `chat-turns.jsonl`, verified-match limits, skipped decode for safe non-candidates, exact fallback behavior, selected member reads, and raw-line hydration.
- **GREEN:** Add the reusable JSONL scan/decode/verify reader, extend the cache reader/materializer, and implement compact turn lookup plus on-demand hydration.
- **Check:** Run Chatlas2 cache, message, and turn operation tests.
- **Risk:** JSON escaping can make a textual filter incomplete. Deviation trigger: a query cannot derive an encoded literal guaranteed to occur in every semantic match; that path must decode all lines.

### Vertical.Slice.3 — Public surface and reconciliation

- **Status:** Complete.

- **RED:** Add CLI tests for turn listing, message-to-turn lookup, hydration, and unchanged message/view behavior.
- **GREEN:** Register `tarav chatlas2 turns list|get`, export the new primitives, advance corpus validation/signatures, and update maintained architecture guidance.
- **Check:** Run all `tests/chatlas2`, Ruff on changed Python files, and representative live Codex/Claude reads.
- **Acceptance signal:** The complete Chatlas2 suite passes; existing message grounding remains functional; a live turn can be located from a message and hydrated without materializing the complete model in memory.

## Impl.Log

- **2026-08-16:** Implementation request produced from the grounded Chatlas2 design and current cache/normalizer implementation. No hidden compatibility or migration layer is planned.
- **2026-08-16:** Checkpointed all pre-execution changes in `tarav-chatlas-md` (`29a51e6`) and `tarav-py` (`b812f44`), then entered execution through `d20260816-37u`.
- **2026-08-16:** During RED/GREEN work, moved turn derivation from individual normalized fragments to the final chronological event union. A continuation specimen proved that per-fragment turns could retain the shorter overlapping artifact and omit later events from the turn even though the event tape itself was complete.
- **2026-08-16:** Implemented schema-v6 `Chat.Turn`, whole-turn opaque payload drift, cache schema v2 with `chat-turns.jsonl`, selected hydration, `Scan.Decode.Verify`, CLI turn reads, corpus validation, tests, and maintained architecture guidance.
- **2026-08-16:** Reconciliation passed: 83 Chatlas2/architecture tests, Ruff checks, Skillware grounding checks for touched Chatlas2 files, and representative live Codex and Claude turn reads including message-to-turn hydration.
