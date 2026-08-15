# Chatlas2 Chat.Message identity and anchor migration - impl-req

## Impl.Abstract

- **scope:** finalize `Chat.Message.Address`, `Chat.Message.Hash`, and `Chat.Message.Ref`; strengthen the Codex user-message completeness contract; verify chronological retention across the included Codex corpus; and implement a pure, fail-closed migration from current turn-backed Chatlas anchor records to message-backed record drafts
- **status:** ready for execution
- **source:** Chatlas2 design session 527 plus the explicit autonomous develop request ^c20260815-46u
- **target:** `tarav-py`, with the settled one-way dependency: Chatlas2 may read current Chatlas models and anchor records, while current Chatlas must never import Chatlas2
- **out of scope:** mutating the live Anchory depot; reconnecting current Views, Query, Chat.Index, manifests, or recents; promoting Chatlas2 into current Chatlas; another provider normalizer; compatibility aliases for superseded experimental `message_id` fields
- **acceptance:** every presented `Chat.Message` has a stable address and current-state hash; stored message refs resolve as `MATCHED`, `AMENDED`, or `MISSING`; every recognized Codex corpus capture preserves its exact scripted user messages and chronological event union; current generic support-set and line-dossier records can be transformed into validated message-backed drafts only when each old turn resolves to one exact new user message

## Impl.Agendix

- **touched (authorization):** implement the four accepted Chatlas2 pre-merge requirements through the autonomous Hugentics develop route ^c20260815-46u
- **touched (message projection):** `Chat.Message` is the complete primary user-agent message projection over retained events, not a replacement event spine ^c20260815-4u ^c20260815-7u ^c20260815-8u
- **touched (origin promise):** user-side versus agent-side classification is asserted only when reliable, and claimed user messages contain only user-origin events ^c20260815-2u ^c20260815-3u ^c20260815-5u
- **touched (reference pattern):** stable logical place and current normalized state remain separate, and stored refs carry drift validation ^c20260815-37u ^c20260815-38u ^c20260815-39u
- **touched (retention):** normalization reviews every relevant artifact, preserves uncertainty, and presents the chronological union ^c20260814-17u ^c20260814-18u ^c20260814-19u
- **structural:** design session 527 owns the product design; this request realizes its open `Chat.Message.Address`, `Chat.Message.Hash`, and `Chat.Message.Ref` direction without expanding the canonical semantic floor
- **open space:** the first migration bridge compares the old resolved visible-user message with new user `Chat.Message` candidates by exact session, timetag, and text; it is a pre-cutover proof primitive, not a live depot mutation command

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

### Anchor record migration

- current anchor records remain the source input and are not amended by this implementation
- migrated generic support records use `chatlas.support-set.v4`; migrated line dossiers use `chatlas.line-anchor-dossier.v2`; `app: chatlas`, hints, attachment assertions, relationship topology, member types, gates, and provenance are preserved
- every migrated turn-ref position becomes `{session, message_address, message_hash, at}`; `session` and `at` are redundant diagnostic context around the canonical `Chat.Message.Ref`
- migration first resolves and validates the old `Normal.Turn.Ref` against the supplied current Chatlas model, extracts its visible user text, then requires exactly one new user `Chat.Message` with the same timetag and exact text
- missing, amended, non-user, or ambiguous source/target evidence fails closed; no fuzzy text matching, position guessing, live depot writing, or compatibility fallback is included

### Chatlas2 Normal Model v3

- replacing experimental `message_id` with message address/hash advances the experimental Normal Model to `schema_version: 3`
- corpus validation requires exact self-resolution for every `Chat.Message.Ref` and `Event.Ref`
- the public Python surface exports message identity/ref/resolution and pure anchor-record migration primitives; no new CLI is required for this pre-merge slice

## Execution.Plan

### Slice 1 - Establish Chat.Message identity and resolution

- add RED tests proving content amendment preserves message address and changes message hash, native-id-only drift preserves the hash, ordered member hashes matter, and stored refs resolve to all three standings
- implement provider-neutral Chat.Message address/hash/ref primitives and give the Codex normalizer an explicit message place
- migrate assembly from `message_id` joins to `message_address`, finalize message hashes from current event refs, and advance the experimental model schema
- observable: every normalized message self-resolves and no `message_id` field remains
- check: focused message-ref and Codex pipeline tests plus Ruff
- status: pending

### Slice 2 - Enforce user-message and corpus completeness

- add RED boundary tests rejecting side/origin mismatch, duplicate message addresses, unresolved membership, and incomplete or reordered scripted user projections
- strengthen conformance validation and signatures around message address/hash while retaining exact user-message comparison and chronological tape checks
- run the complete included corpus and report recognized, unsupported, and failed counts
- observable: all included Codex captures reproduce exact scripted user messages and all retained event tapes remain chronological; unsupported providers remain explicit
- check: Chatlas2 corpus tests and `tarav chatlas2 corpus verify|check`
- status: pending

### Slice 3 - Define and test fail-closed anchor migration

- add RED tests for generic support-set and line-dossier migration, including support members, gate turn refs, member types, attachment, and provenance preservation
- add negative tests for old-ref drift, absent target, side mismatch, timestamp mismatch, and ambiguous exact target evidence
- implement pure current-record to message-record draft migration using explicit old/new session models and no persistence
- observable: a real-shape current anchor record can be transformed deterministically into the new record shape, while uncertain mappings fail without output
- check: focused migration tests and reverse-dependency architecture check
- status: pending

### Slice 4 - Reconcile maintained surfaces and verify the slice

- update Chatlas2 exports, `AGENTS.md`, `ARCHITECTURE.md`, and design session 527 to describe Normal Model v3, message references, and migration boundary
- review the diff for accidental current-Chatlas imports of Chatlas2 or live-anchor mutations
- observable: maintained guidance matches code and the experimental boundary remains directional
- check: all Chatlas2 tests, architecture tests, full relevant repository suite, Ruff, `git diff --check`, Skillware, and CLI normalize/corpus smoke
- status: pending

## Impl.Log

- **2026-08-15 — design gate:** autonomous design and execution authorized by the exact user invocation ^c20260815-46u
- **2026-08-15 — inspected baseline:** Chatlas2 Normal Model v2 already presents Event.Ref-backed messages and exact scripted user-message corpus checks, but messages still use contentless internal `message_id` values and no current anchor-record migration primitive exists
- **2026-08-15 — migration boundary:** this slice produces validated record drafts only; live Anchory depot mutation belongs to the later Chatlas consumer cutover
