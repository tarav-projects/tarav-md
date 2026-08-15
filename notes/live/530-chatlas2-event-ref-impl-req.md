# Chatlas2 Event References - impl-req

## Impl.Abstract

- **scope:** implement the settled Chatlas2 `Event.Address`, `Event.Hash`, `Event.Ref`, and stateless `Event.Ref.Resolution` design across the Codex normalizer, chronological assembler, annotations, corpus checks, and public Python surface
- **status:** implemented and verified
- **source:** Chatlas2 design session 527, especially its grounded `Event.Ref` block, plus the explicit autonomous develop request ^c20260815-45u
- **target:** `tarav-py`; maintain the existing one-way dependency in which Chatlas2 may use current Chatlas but current Chatlas never imports Chatlas2
- **out of scope:** `Chat.Message.Ref`; persistent normalized history; cross-run observation storage; another provider normalizer; reference-repair policy; an Event.Ref CLI; compatibility aliases for the superseded `event_id` model
- **acceptance:** normalized Codex events expose stable content-independent addresses and content hashes; annotations carry resolving Event.Ref objects; a stored reference resolves as `MATCHED`, `AMENDED`, or `MISSING` against only the supplied current model; corpus and repository checks remain green

## Impl.Agendix

- **touched (authorization):** implement the newly settled design through the autonomous Hugentics develop route ^c20260815-45u
- **touched (event address):** `Event.Address` is a stable opaque provider-derived logical place, independent of event content and chronological presentation position ^c20260815-37u
- **touched (event hash):** `Event.Hash` asserts the event's current normalized content while excluding address, annotations, native identifiers, and provenance ^c20260815-38u
- **touched (event ref):** `Event.Ref` couples address and hash to carry drift validation ^c20260815-39u
- **touched (statelessness):** current raw artifacts produce the current Normal Model without normalized state across runs ^c20260815-40u
- **touched (resolution):** Chatlas compares a stored reference with the current model and presents `MATCHED`, `AMENDED`, or `MISSING`; consumers own policy ^c20260815-41u ^c20260815-42u ^c20260815-43u
- **touched (rejection):** Chatlas2 does not retain earlier normalized event states merely to explain amendments; Raw Archive Git history remains the debugging surface ^c20260815-44u
- **touched (implementation):** current Chatlas2 uses one content-and-position-derived `event_id` throughout `codex.py`, `pipeline.py`, and `corpus.py`; 12 focused Chatlas2 tests and Ruff are green before this change
- **structural:** `527-chatlas2-normal-model-redesign-design-session.md` owns the design; this request form-fits it into executable slices without promoting the live design into the stable Index
- **open space:** the first Codex address recipe uses the native rollout session id plus nonblank-record ordinal, domain-separated by provider and `Raw.Model.Version`; it is provisional to `codex.rollout.v1` and deliberately fails toward separate places when raw coordinates move

## Impl.Index

### Chatlas2.Event.Address

- every normalized event has one full SHA-256 `event_address`
- the common address primitive hashes a versioned envelope containing provider, `Raw.Model.Version`, provider-native session scope, and provider-owned raw place
- the Codex v1 raw place is the nonblank JSON record ordinal; source path, normalized content, annotations, timestamps, native item identifiers, and tape order are excluded
- equal record places across retained copies of one Codex rollout therefore fold; a moved or unprovable place remains a separate event

### Chatlas2.Event.Hash

- every normalized event has one full SHA-256 `event_hash`
- the hash covers class, origin, start timetag, and retained raw record content after removing provider-native identifier fields
- address, annotations, observation/source provenance, and native identifiers do not affect the hash
- substantive content amendment at the same address changes the hash; native-id-only drift does not

### Chatlas2.Event.Ref

- the stored form is exactly `{event_address, event_hash}`
- `event_ref(event)` constructs the assertion from one current event
- `resolve_event_ref(events, ref)` returns a small Chatlas-presented resolution carrying standing plus the currently addressed event when present
- comparison is exact over the full current hash; Chatlas2 adds no prefix negotiation, relocation search, repair, or policy

### Chatlas2.Event.Ref.Resolution

- `MATCHED` means the current tape contains the address and its hash equals the stored assertion
- `AMENDED` means the current tape contains the address with another current hash
- `MISSING` means the current tape does not contain the address
- resolution consumes only its explicit current event tape and stored reference; it never reads Git or another normalization run

### Chatlas2.Annotation.References

- `Chat.Message` uses `event_refs` instead of `event_ids`
- `Agent.Loaded.Context` uses `agent_event_ref` and member `event_refs`
- fragment normalization may carry address-only internal joins, but the assembled public model finalizes every annotation against current event hashes
- no legacy `event_id`, `event_ids`, or `agent_event_id` aliases survive in the Chatlas2 Normal Model

### Chatlas2.Current.Fold

- same address plus same hash merges current input observations
- same address plus different hash is one amended logical place; the active index-row artifact supplies the presented current state while all current input source references remain on the folded event
- events unique to any recognized retained artifact always survive the union
- this fold is stateless: it does not retain a state merely because an earlier normalization run presented it

### Chatlas2.Normal.Model.V2

- the incompatible reference shape advances the experimental Normal Model to `schema_version: 2`
- the conformance validator requires unique addresses, full event hashes, and exact resolution of every annotation Event.Ref
- specimen comparison remains insensitive to anonymized native identity while preserving event, message, and loaded-context topology
- the inspectable normalize CLI changes only its JSON model shape; no new command is added

## Execution.Plan

### Slice 1 - Establish Event.Ref primitives and Codex address/hash behavior

- add RED tests proving content amendment preserves address and changes hash, native-id-only drift preserves hash, and stored references resolve to all three standings without retained history
- add a focused provider-neutral `chatlas2.event_ref` module and replace the Codex `event_id` recipe with explicit address and hash derivation
- observable: independently normalized old/current artifacts produce the same address, different state hashes, and stateless `AMENDED` resolution
- check: focused Codex pipeline tests and Ruff
- status: complete

### Slice 2 - Fold current artifacts and migrate annotations

- add RED tests for same-address exact folding, active-artifact amendment presentation, observation retention, chronological ordering, and resolving annotation refs
- update the assembler to key by address, merge observations, select the current state from the active index-row source on amendment, and finalize all annotation members as Event.Ref objects
- remove the superseded Chatlas2 identifier fields and advance the model schema version
- observable: model JSON contains no legacy event-id fields and every annotation reference resolves `MATCHED`
- check: focused pipeline and CLI tests; diff review for current-Chatlas reverse dependencies
- status: complete

### Slice 3 - Migrate conformance checks and maintained documentation

- update corpus validation, signature comparison, and user-message projection to consume Event.Ref membership and reject missing, amended, or duplicate-address topology
- update Chatlas2 exports plus maintained `AGENTS.md` and `ARCHITECTURE.md` descriptions of the Normal Model contract
- observable: all included Codex specimens still reproduce exact user messages and all Claude specimens remain explicitly unsupported
- check: all Chatlas2 tests, corpus `verify|check`, architecture tests, full relevant repository suite, Ruff, Skillware, and installed CLI smoke
- status: complete

## Impl.Log

- **2026-08-15 — execution gate:** autonomous design and execution authorized by the explicit develop invocation ^c20260815-45u
- **2026-08-15 — baseline:** 12 focused Chatlas2 tests pass and Ruff reports no findings before implementation
- **2026-08-15 — design-reality audit:** the existing `event_id` hashes `{record_index, record}`, so a content amendment changes identity and cannot produce the settled `AMENDED` standing; annotations and corpus validation are the complete known consumer set
- **2026-08-15 — address recipe:** Codex rollout record ordinal is the smallest stable logical place available in `codex.rollout.v1`; native rollout session id supplies scope, while moved records deliberately fail toward retention
- **2026-08-15 — durable handoff:** Impl.Req 530 was re-read cold after writing; its authorization and all eight source-design anchors resolve, and every slice has an observable check
- **2026-08-15 — checkpoint:** the mandatory pre-edit `tarav-py` checkpoint captured the complete existing worktree at commit `d07bb9f`; Event.Ref implementation changes remain uncommitted after this boundary
- **2026-08-15 — slice 1:** added provider-neutral address/hash/reference/resolution primitives and changed Codex fragment normalization to scope record-place addresses by native session plus Raw.Model.Version; RED failed on missing addresses, then three focused tests and Ruff passed
- **2026-08-15 — slice 2:** changed assembly to fold by address, let the active index-row artifact present current state, retain all current input source observations, emit schema v2, and finalize message/context membership as full Event.Ref objects; the RED pipeline failures became six passing focused pipeline/CLI tests
- **2026-08-15 — slice 3:** migrated corpus validation and specimen projection to Event.Ref topology, exported the reference primitives, documented Normal Model v2, and added a RED-to-GREEN guard preventing archived message annotations from being relabeled onto an amended current non-message event
- **2026-08-15 — conformance:** all 21 included artifacts verify; 10 Codex captures normalize successfully, 11 captures remain explicitly unsupported, and none fail
- **2026-08-15 — verification:** 17 Chatlas2 tests, 8 architecture tests, and the complete 1,926-test repository suite pass; focused Chatlas2 Ruff, `git diff --check`, Skillware, installed `tarav chatlas2` help, and public module imports also pass
- **2026-08-15 — known baseline:** repository-wide Ruff remains blocked by the pre-existing unused `local_storage_paths` import in `src/tarav/skills/routing.py`; that checkpointed, unrelated file was not changed by this implementation
- **2026-08-15 — outcome:** acceptance is satisfied with no implementation blockers; post-checkpoint Event.Ref work remains uncommitted
