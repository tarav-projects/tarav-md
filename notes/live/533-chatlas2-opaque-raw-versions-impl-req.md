# Chatlas2 opaque Raw.Model.Version identifiers and Claude split - impl-req

## Impl.Abstract

- **scope:** replace Chatlas2's ordinal-looking raw-version identifiers with opaque arbitrary identifiers; split Claude transcripts into `promptSource` and pre-`promptSource` mapping families; dispatch each recognized family to a compatible simple normalizer; and keep stable event/message addresses independent of raw-version labels
- **status:** implemented and verified; changes remain uncommitted after the mandatory checkpoints
- **source:** Chatlas2 design session 527 plus the explicit autonomous develop request ^c20260815-66u
- **target:** `tarav-py`, with maintained Chatlas2 guidance in `AGENTS.md`, `ARCHITECTURE.md`, the conformance corpus metadata, and this implementation request
- **out of scope:** current-Chatlas consumer migration; compatibility aliases for the superseded experimental numeric identifiers; provider/CLI-version dispatch; automatic registration of a private historical artifact without the corpus workflow's human safety review
- **acceptance:** Codex and both Claude raw mapping families receive opaque non-ordinal identifiers; Claude version recognition selects one direct mapping adapter; historical Claude user messages without `promptSource` become `User.Event`/`Chat.Message` data without admitting known harness/tool records; changing only a raw-version identifier cannot move an `Event.Address` or `Chat.Message.Address`; all existing corpus captures and focused tests pass

## Impl.Agendix

- **touched (authorization):** implement the raw-version renames and the new Claude raw version through the autonomous Hugentics develop route ^c20260815-66u
- **touched (identifier semantics):** `Raw.Model.Version` names are arbitrary opaque identities and do not imply succession ^c20260815-65u
- **touched (partition):** raw fragments are partitioned by compatible mapping structure so each normalizer keeps direct raw-to-normal mappings; normalizers for separate partitions may share mechanical readers and builders ^c20260815-59u ^c20260815-55u ^c20260815-56u
- **touched (evolution):** Normal Model evolution may refine a raw-version partition when newly required mappings expose relevant raw differences ^c20260815-60u ^c20260815-61u ^c20260815-62u
- **touched (identity):** raw-version identity is dispatch/provenance metadata and does not participate in stable event or message address identity ^c20260815-64u
- **structural:** design session 527 owns the Chatlas2 product design; `src/tarav/chatlas2/` owns the isolated experimental implementation; current Chatlas must not import Chatlas2
- **open space:** the opaque suffixes are allocated once for this experiment and checked for uniqueness; no registry or sequence allocator is introduced until another consumer needs one

## Impl.Index

### Opaque Raw.Model.Version identifiers

- replace `codex.rollout.v1` with `codex.rollout.5f98`
- replace the current Claude `promptSource` mapping family with `claude.transcript.1ecc`
- assign the historical no-`promptSource` mapping family `claude.transcript.b17b`
- suffixes are arbitrary lowercase random tokens with no ordering, compatibility, or replacement semantics
- identifiers are immutable dispatch/provenance values; no numeric aliases or migration shim remains in the experimental package

### Claude recognition and normalization

- common Claude transcript validation remains one shared reader/validator
- an artifact containing a transcript user record with a `promptSource` field is recognized as `claude.transcript.1ecc`; a structurally valid Claude transcript with no such field is recognized as `claude.transcript.b17b`
- `ClaudePromptSourceRawNormalizer` maps primary user messages directly from `promptSource in {typed, queued}`
- `ClaudeLegacyRawNormalizer` maps primary user messages from the older role/content structure while excluding tool-result transport, compact summaries, and known system/local-command injections; command records carrying explicit user arguments remain user messages
- both adapters reuse event construction, chronological preservation, message finalization, and conservative loaded-context machinery without branching on raw version inside either mapping rule

### Dispatch and stable identity

- the pipeline selects a normalizer from the recognized `Raw.Model.Version`, rather than assigning one provider-wide normalizer that branches internally
- Versioners remain provider-selected; normalizers remain version-selected
- remove `raw_model_version` from `compute_event_address` and `compute_chat_message_address` inputs and canonical address bodies
- provider, native session scope, and provider-owned place continue to define stable address position; version labels remain visible on source metadata only

### Conformance and archive evidence

- rename every stored corpus artifact's recognized version and update maintained corpus documentation without rewriting immutable artifact bytes
- existing 21 captures must verify and normalize under the renamed adapters
- synthetic boundary fixtures cover the older Claude record mapping without introducing private corpus material
- a read-only full-archive pass reports recognition counts by new identifier and normalizes representative artifacts from both Claude partitions
- preparing or registering a real historical `claude.transcript.b17b` corpus artifact remains an explicit operator-reviewed ingress action

## Execution.Plan

### Slice 1 - Make raw-version names opaque and address-independent

- add RED tests asserting the three exact opaque identifiers and proving address equality across raw-version label changes
- rename Codex and current Claude constants and remove raw version from event/message address derivation
- update callers, exports, corpus metadata, and maintained guidance; add no compatibility constants
- observable: no `codex.rollout.v1` or `claude.transcript.v1` remains in maintained Chatlas2 code/corpus guidance, and stable addresses do not change when dispatch metadata changes
- check: event-ref, message-ref, Codex pipeline, corpus tests, Ruff
- status: complete

### Slice 2 - Split Claude recognition and direct normalizers

- add RED tests for prompt-source recognition, legacy recognition, ambiguous/malformed rejection, compatible normalizer declarations, legacy user-message inclusion, and harness/tool exclusion
- implement the two Claude identifiers, artifact recognition, shared mechanics, two direct normalizers, and version-based pipeline dispatch
- observable: both Claude families normalize chronologically; ordinary legacy user text becomes `User.Event` and `Chat.Message`, while known nonhuman user-role transports remain agent-side and outside `Chat.Message`
- check: Claude pipeline tests, pipeline/corpus tests, Ruff
- status: complete

### Slice 3 - Reconcile corpus, archive behavior, and maintained surfaces

- update corpus registry/readme plus `AGENTS.md`, `ARCHITECTURE.md`, exports, and code annotations
- run corpus verify/check, all Chatlas2 and architecture tests, repository tests proportionate to the change, Ruff, Skillware, and `git diff --check`
- run both Versioners against the full current raw archive and normalize representative Claude artifacts from each recognized partition
- observable: corpus is hermetic and green; archive recognition is reported by opaque identifier; current Chatlas has no reverse dependency on Chatlas2
- check: documented CLI corpus commands, focused/full pytest, architecture dependency check, archive audit, diff review
- status: complete

## Impl.Log

- **2026-08-15 — design gate:** arbitrary non-successional raw-version names were selected and grounded ^c20260815-65u
- **2026-08-15 — execution gate:** autonomous design and execution were authorized by the exact develop invocation ^c20260815-66u
- **2026-08-15 — inspected baseline:** one provider-wide Claude normalizer recognizes all structurally valid transcripts as `claude.transcript.v1` but maps user messages only through `promptSource`; event and message addresses still include raw-version identity despite the later stable-address decision
- **2026-08-15 — identifiers:** allocated `5f98`, `1ecc`, and `b17b` as arbitrary collision-checked experimental suffixes; their spelling carries no semantic order
- **2026-08-15 — durable handoff:** Impl.Req 533 was re-read cold; the source-design and execution-gate anchors resolve, and the plan remains executable without chat context
- **2026-08-15 — checkpoints:** mandatory pre-edit checkpoints captured the complete `tarav-py` worktree at `73ee575` and the Chatlas design surfaces at `b72faac`
- **2026-08-15 — slice 1:** replaced the experimental numeric-looking identifiers with `codex.rollout.5f98` and `claude.transcript.1ecc`; removed raw-version identity from Event and Chat.Message address inputs; and updated exports, callers, tests, conformance metadata, and maintained guidance without compatibility aliases
- **2026-08-15 — slice 2:** added `claude.transcript.b17b`, artifact recognition by mapping structure, separate prompt-source and legacy direct normalizers, and version-selected dispatch; shared mechanics remain version-agnostic, while legacy fixtures prove ordinary and command-argument user input is retained and known harness/tool traffic is excluded
- **2026-08-15 — corpus:** all 21 immutable artifacts verify and normalize under their opaque identifiers (21 passed, 0 failed, 0 unsupported); registering a real `b17b` artifact remains the documented operator-reviewed ingress step
- **2026-08-15 — archive acceptance:** the live archive scan recognized 6,353 Codex artifacts as `5f98`, 2,950 Claude artifacts as `1ecc`, and 3,038 Claude artifacts as `b17b`; 14 Codex and 40 Claude files remained null; representative real artifacts from both Claude partitions normalized successfully
- **2026-08-15 — verification:** Ruff and diff checks passed; focused Chatlas2 plus architecture tests passed (40); the full repository suite passed (1,941); Skillware reported its existing 30 project findings and none target Chatlas2; no current-Chatlas reverse dependency on Chatlas2 was introduced
