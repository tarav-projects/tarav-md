# Chatlas2 design-session support slice - impl-req

## Impl.Abstract

- **scope:** add a provider-neutral primary-text projection to `Chat.Message`; expose pure message discovery, reference resolution, derived-time, and bounded-neighborhood operations; define Chatlas2 support members; and implement only the Anchory preview/register/batch-register/resolve route required by Hugentic design-session capture
- **status:** ready for autonomous execution
- **source:** explicit autonomous implementation request ^c20260816-0u, grounded in Chatlas2 design session 527
- **target:** `tarav-py`, with maintained Chatlas2 guidance in `AGENTS.md`, `ARCHITECTURE.md`, conformance tests, and this implementation request
- **out of scope:** replacing Hugentic capture logic; reconnecting Views, Query, Chat.Index, or other current-Chatlas consumers; migrating old anchor records; gates/provenance authoring; persistent normalized state; global full-text indexes; new Normal Model concepts
- **acceptance:** an agent can find the exact user message that authorized the recent raw-version design capture without provider-native decoding, preview/register/resolve a line dossier backed by a `Chat.Message.Ref`, repeat the registration without duplication, and obtain equivalent behavior for Codex plus both recognized Claude raw-model versions

## Impl.Agendix

- **touched (authorization):** implement this minimal consumer-driven slice through the autonomous Hugentics develop route ^c20260816-0u
- **touched (message promise):** `Chat.Message` is the complete primary user-agent exchange projected over the event tape ^c20260815-4u ^c20260815-7u ^c20260815-8u
- **touched (message identity):** `Chat.Message.Ref` couples stable provider-derived message place with a hash over side and ordered member event hashes ^c20260815-46u
- **touched (stateless resolution):** current artifacts produce the current model; references resolve as `MATCHED`, `AMENDED`, or `MISSING`, while consumers choose policy ^c20260815-40u ^c20260815-42u ^c20260815-43u
- **structural:** design session 527 owns Chatlas2 product design; `src/tarav/chatlas2/` owns the isolated implementation; current Chatlas must not import Chatlas2
- **consumer boundary:** Hugentic design-session capture remains the workflow owner; Chatlas2 supplies provider-neutral grounding primitives biased toward that first consumer

## Impl.Index

### Chat.Message primary text

- every `Chat.Message` carries `text`, a provider-neutral primary transcript projection derived by its compatible raw normalizer
- complete raw/member data remains on the referenced events; `text` is intentionally narrow and need not expose provider envelopes, tool transport, or every content block
- message identity remains side plus ordered member `Event.Hash` values; because those hashes cover normalized event content, text amendments change the message hash without making derived `text` a second identity input

### Pure message operations

- list messages in chronological projection order, optionally filtered by user/agent side
- find messages by side and provider-neutral text, supporting exact and substring matching without decoding raw provider records
- resolve `Chat.Message.Ref` against the current model using the existing three-state standing
- derive a message's diagnostic `at` from its first chronological member event
- return a bounded message neighborhood around a resolved reference; bounds count messages, never raw events
- operations accept a Normal Model value and do not read or mutate storage

### Support member

- the stored support member is exactly `{session, message_address, message_hash, at}`
- `session + message_address + message_hash` is the durable assertion; `at` is redundant diagnostic evidence and never participates in identity or standing
- resolution reports current message data plus diagnostic time comparison when available; only address/hash determine `MATCHED`, `AMENDED`, or `MISSING`
- support registration accepts only currently `MATCHED` user-side messages for this first design-session route

### Minimal Chatlas2 Anchory route

- reuse the existing line-dossier attachment (`canonical_schema`, canonical triplet, triplet hash) and support-relationship shape
- emit a Chatlas2 dossier schema whose `relationships.support.members` are Chatlas2 support members; do not add gates or provenance mechanics in this slice
- provide preview, register, batch preview/register, and resolve operations
- registration is idempotent by exact canonical line attachment plus normalized support members: repeating the same capture returns the existing anchor
- use the shared Anchory depot but an isolated `chatlas2` namespace with its own single-letter prefix so current Chatlas never parses Chatlas2 dossiers as current-Chatlas records
- resolution loads the current Chatlas2 model for each member, presents reference standing, primary text, side, current derived time, and a bounded message neighborhood

### First workflow trial

- locate the exact user message that established opaque Raw.Model.Version identifiers during design-session capture using only Chatlas2 message operations
- preview and register a representative design line, resolve it, then repeat the same registration and prove the anchor is reused
- exercise provider-neutral text and reference operations against Codex, Claude prompt-source (`claude.transcript.1ecc`), and Claude legacy (`claude.transcript.b17b`) fixtures/corpus evidence

## Execution.Plan

### Slice 1 - Provider-neutral text and pure message operations

- add RED tests for text projection in Codex and both Claude mapping families
- add RED pure-operation tests for chronological listing, side/text lookup, ref resolution, derived `at`, and bounded neighborhoods
- implement the smallest normalizer and operations changes that satisfy them
- observable: no consumer needs provider-shape branching to locate a primary message
- check: focused model/provider/message tests and Ruff
- status: pending

### Slice 2 - Support member and Anchory operations

- add RED tests for exact support-member shape, diagnostic-only `at`, dossier preview, idempotent single/batch registration, and three-state resolution
- implement a Chatlas2-isolated namespace and minimal dossier operations using shared Anchory and attachment primitives
- observable: one design line can be grounded, registered, reread, and contextualized through current Chatlas2 data
- check: focused Anchory tests, architecture dependency test, Ruff
- status: pending

### Slice 3 - CLI, workflow trial, and reconciliation

- expose only the message and Anchory commands needed by agentic capture
- trial the recent versioning design evidence, repeat registration, and record read-back/idempotence evidence without editing the design session
- run focused and full Chatlas2 tests, the complete repository suite proportionate to the change, corpus verification, Ruff, Skillware, architecture dependency checks, and `git diff --check`
- update maintained package guidance and this execution log/status
- observable: the complete first-consumer slice works for Codex and both Claude versions while current Chatlas remains untouched
- status: pending

## Impl.Log

- **2026-08-16 — execution gate:** autonomous design and execution of the bounded Chatlas2 support slice were authorized by the exact implementation invocation ^c20260816-0u
- **2026-08-16 — inspected baseline:** normalizers already identify `Chat.Message` and stable refs, but primary text/time remain available only through provider-native event records; current Anchory dossiers store current-Chatlas turn refs and cannot safely accept Chatlas2 records in the same namespace
- **2026-08-16 — isolation decision:** reuse the common depot and Anchory mechanics through a distinct `chatlas2` namespace; namespace separation prevents current Chatlas scans from interpreting the new dossier schema
