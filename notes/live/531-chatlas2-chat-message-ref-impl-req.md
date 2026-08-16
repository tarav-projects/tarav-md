# Chatlas2 Chat.Message identity - impl-req

## Impl.Abstract

- **scope:** finalize `Chat.Message.Address`, `Chat.Message.Hash`, and `Chat.Message.Ref`; strengthen the Codex user-message completeness contract; and verify chronological retention across the included Codex corpus
- **status:** implemented and verified
- **source:** Chatlas2 design session 527 plus the explicit autonomous develop request ^c20260815-46u
- **target:** `tarav-py`, with the settled one-way dependency: Chatlas2 may read current Chatlas models and anchor records, while current Chatlas must never import Chatlas2
- **out of scope:** anchor-record migration mechanics or schemas; mutating the live Anchory depot; reconnecting current Views, Query, Chat.Index, manifests, or recents; promoting Chatlas2 into current Chatlas; another provider normalizer; compatibility aliases for superseded experimental `message_id` fields
- **acceptance:** every presented `Chat.Message` has a stable address and current-state hash; stored message refs resolve as `MATCHED`, `AMENDED`, or `MISSING`; every recognized Codex corpus capture preserves its exact scripted user messages and chronological event union

## Impl.Agendix

- **touched (authorization):** implement the four accepted Chatlas2 pre-merge requirements through the autonomous Hugentics develop route ^c20260815-46u
- **touched (message projection):** `Chat.Message` is the complete primary user-agent message projection over retained events, not a replacement event spine ^c20260815-4u ^c20260815-7u ^c20260815-8u
- **touched (origin promise):** user-side versus agent-side classification is asserted only when reliable, and claimed user messages contain only user-origin events ^c20260815-2u ^c20260815-3u ^c20260815-5u
- **touched (reference pattern):** stable logical place and current normalized state remain separate, and stored refs carry drift validation ^c20260815-37u ^c20260815-38u ^c20260815-39u
- **touched (retention):** normalization reviews every relevant artifact, preserves uncertainty, and presents the chronological union ^c20260814-17u ^c20260814-18u ^c20260814-19u
- **structural:** design session 527 owns the product design; this request realizes its open `Chat.Message.Address`, `Chat.Message.Hash`, and `Chat.Message.Ref` direction without expanding the canonical semantic floor
- **open space:** existing anchor data will be transformed operationally against the actual cutover shapes, with Git providing recovery and explicit completeness checks validating the result

## Impl.Index

### Chat.Message.Address

- every normalized `Chat.Message` has one full SHA-256 `message_address`
- the address is a domain-separated provider-derived place with provider, `Raw.Model.Version`, native session scope, and provider-owned message place
- Codex rollout v1 uses the nonblank record ordinal as its message place, parallel to but distinct from the event address namespace
- message content, side, event hashes, source paths, native item identifiers, and chronological presentation order do not affect the address

### Chat.Message.Hash

- every normalized `Chat.Message` has one full SHA-256 `message_hash`
- the hash covers the asserted side and ordered member `Event.Hash` values
- address, class label, provenance, source paths, and redundant anchor metadata are excluded
- content, classification, order, or grouping amendment changes the hash; native-id-only event drift does not

### Chat.Message.Ref

- the canonical stored assertion is exactly `{message_address, message_hash}`
- `chat_message_ref(message)` constructs it and `resolve_chat_message_ref(messages, ref)` presents `MATCHED`, `AMENDED`, or `MISSING`
- `Chat.Message` itself carries address, hash, side, and ordered `event_refs`; the superseded experimental `message_id` field is removed
- message annotations are unique by address and are ordered by their first member event on the chronological tape

### Chat.Message completeness

- every asserted user `Chat.Message` resolves only to `User.Event` members; every asserted agent message resolves only to `Agent.Event` members
- the Codex normalizer emits exactly one user message for every recognized primary user message after filtering known harness injections and duplicate provider renderings
- conformance validation compares the complete ordered user-message projection with the immutable script specification and rejects side/origin disagreement, unresolved refs, duplicate message addresses, or nonchronological tape output

### Chatlas2 Normal Model v3

- replacing experimental `message_id` with message address/hash advances the experimental Normal Model to `schema_version: 3`
- corpus validation requires exact self-resolution for every `Chat.Message.Ref` and `Event.Ref`
- the public Python surface exports message identity/ref/resolution; no new CLI is required for this pre-merge slice

## Execution.Plan

### Slice 1 - Establish Chat.Message identity and resolution

- add RED tests proving content amendment preserves message address and changes message hash, native-id-only drift preserves the hash, ordered member hashes matter, and stored refs resolve to all three standings
- implement provider-neutral Chat.Message address/hash/ref primitives and give the Codex normalizer an explicit message place
- migrate assembly from `message_id` joins to `message_address`, finalize message hashes from current event refs, and advance the experimental model schema
- observable: every normalized message self-resolves and no `message_id` field remains
- check: focused message-ref and Codex pipeline tests plus Ruff
- status: complete

### Slice 2 - Enforce user-message and corpus completeness

- add RED boundary tests rejecting side/origin mismatch, duplicate message addresses, unresolved membership, and incomplete or reordered scripted user projections
- strengthen conformance validation and signatures around message address/hash while retaining exact user-message comparison and chronological tape checks
- run the complete included corpus and report recognized, unsupported, and failed counts
- observable: all included Codex captures reproduce exact scripted user messages and all retained event tapes remain chronological; unsupported providers remain explicit
- check: Chatlas2 corpus tests and `tarav chatlas2 corpus verify|check`
- status: complete

### Slice 3 - Reconcile maintained surfaces and verify the slice

- update Chatlas2 exports, `AGENTS.md`, `ARCHITECTURE.md`, and design session 527 to describe Normal Model v3 and message references
- review the diff for accidental current-Chatlas imports of Chatlas2 or live-anchor mutations
- observable: maintained guidance matches code and the experimental boundary remains directional
- check: all Chatlas2 tests, architecture tests, full relevant repository suite, Ruff, `git diff --check`, Skillware, and CLI normalize/corpus smoke
- status: complete

## Impl.Log

- **2026-08-15 — design gate:** autonomous design and execution authorized by the exact user invocation ^c20260815-46u
- **2026-08-15 — inspected baseline:** Chatlas2 Normal Model v2 already presents Event.Ref-backed messages and exact scripted user-message corpus checks, but messages still use contentless internal `message_id` values
- **2026-08-15 — durable handoff:** Impl.Req 531 was re-read cold before execution; the implementation gate and source-design anchors resolve
- **2026-08-15 — checkpoints:** mandatory pre-edit checkpoints captured the complete `tarav-py` worktree at `faf646b` and the Chatlas design surfaces at `dc1f10f`
- **2026-08-15 — slice 1:** added provider-neutral Chat.Message address/hash/ref/resolution, replaced experimental `message_id` joins with message addresses, finalized hashes from ordered member Event.Hash values, and advanced the Normal Model to v3
- **2026-08-15 — slice 2:** conformance validation now rejects duplicate message places, invalid state hashes, unresolved membership, nonchronological message projection, and side/origin disagreement; all 21 artifacts verify, with 10 Codex captures passing, 11 Claude captures explicitly unsupported, and zero failures
- **2026-08-15 — correction:** removed the experimental anchor-migration module, tests, exports, and predeclared record schemas; migration is an operational cutover task protected by Git and checked directly for data completeness
- **2026-08-15 — live-session differential:** current Chatlas and Chatlas2 each present 72 user messages for the active session, with no message missing or additional in either projection
- **2026-08-15 — verification:** 29 focused Chatlas2/architecture tests and the complete 1,930-test repository suite pass after removing migration mechanics; focused Ruff, `git diff --check`, corpus verify/check, public imports, and the live normalize CLI smoke pass
- **2026-08-15 — known baselines:** repository-wide Ruff still reports the pre-existing unused `local_storage_paths` import in `src/tarav/skills/routing.py`; project Skillware still reports 30 unrelated POIs and no Chatlas2 POIs
- **2026-08-15 — outcome:** all acceptance signals are satisfied; implementation and design updates remain uncommitted after the mandatory checkpoints for user review
