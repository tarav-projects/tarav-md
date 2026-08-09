# Stable Event Place Model - impl-req

## Impl.Abstract

- **scope:** align `agentos-chatlas-py` with the landed stable-event-place, neutral-lineage, best-effort-closure, and `User.Turn.Purity` design; migrate the durable `Event.Ref` shape and its consumers; update the Skillware-owned Hugentics event-addressing documentation
- **status:** ready for implementation
- **source:** landed Chatlas design in `skills/agentos-chatlas-pkg/design/100-design.md`, current Python mechanics and contract inspection, and the explicit implementation-design request ^c20260809-9u
- **repositories:** `agentos-chatlas-py` for mechanics and contract; `agentos-md` for the Skillware source and rebuilt Hugentics reference; this note remains in `agentos-chatlas-md`
- **compatibility:** hard schema/cache generation change for disposable session-model artifacts and event-query indexes; preserve existing `Normal.Turn.Ref` assertions by not changing hashed event content merely to identify `User.Turn`

### In scope

- required opaque `event_address` on every normalized event, derived by each provider normalizer from its own stable raw evidence
- `Event.Ref = {event_address, event_hash}` plus optional escaping context such as `session` and `at`; `sequence` remains presentation/order only
- provider conformance for `Event.Amendment` and `Event.Append`
- neutral lineage edges over first-class events, with no Chatlas-owned active/default/abandoned path status
- provider-evidenced rollback events only; no rollback fabricated merely because a branch exists
- optional `closed.estimate` as normalizer-owned best effort; removal of `extras.final` and finality-dependent model semantics
- cache freshness over raw observation plus model/normalizer revision
- explicit `User.Turn` kind/membership derived from the user-input boundary, not transport role or `producer.type == "human"`
- generated documentation rebuilt from `agentos-md/skills/agentos-hugentics/.skw/src/references/link.skw.md`

### Out of scope

- a universal raw-coordinate schema for every provider
- consumer policies that choose an active, preferred, or default lineage path
- guaranteed event completion/finality
- rewriting `notes/live/514-event-addressing-impl-req.md`; it is historical provenance for the displaced positional model, not current documentation
- renaming the entire `producer.type` vocabulary in this change; `User.Turn` attribution is decoupled from that field so the purity fix does not invalidate all existing `Event.Hash` and `Normal.Turn.Ref` assertions

## Impl.Agendix

- **touched (chat):** implementation-design and artifact-write authorization ^c20260809-9u
- **touched (index):** `Session.Event.Tape` establishes stable event places and current-state materialization (`100-design.md`, `Session.Event.Tape`) ^c20260807-37u
- **touched (index):** `Event.Address`, `Event.Ref`, `Event.Amendment`, and `Event.Append` define the address/hash split and provider-owned invariants ^c20260807-9u ^c20260807-16u ^c20260807-23u ^c20260807-35u
- **touched (index):** `Event.Closed.Estimate`, `Session.Model.Artifact`, and `Normalization.Delta.Checkpoint::Chatlas` reject finality guarantees and keep reuse policy outside the normal model ^c20260807-38u ^c20260807-50u ^c20260807-56u
- **touched (index):** `Session.Lineage`, `Lineage.Branch`, and `Lineage.Rollback` preserve every path without active-path semantics ^c20260806-111u ^c20260808-41u ^c20260807-63u
- **touched (index):** `Compaction.Event`, `Compaction.Summary`, and `User.Turn.Purity` keep generated recap text outside user input authority ^c20260806-100u ^c20260806-105u ^c20260809-2u
- **structural:** `references/normal-model.contract.json` declares the emitted Python model; provider assemblers and consumers must close against it
- **structural:** `.skw/src/references/link.skw.md` derives `references/link.md`; only the source is hand-edited, then `agentos skw build` regenerates the runnable surface
- **structural:** session-model artifacts, delta checkpoints, and SQLite event-query indexes are derived and may be invalidated rather than migrated in place
- **open space:** each provider owns its precise address seed; implementation must record the chosen native coordinate and fragment discriminator in code and conformance tests, without promoting that recipe into the universal model contract

## Impl.Index

### Event.Place.Identity

- `event_address` identifies the stable place; `event_hash` asserts the currently observed content at that place; `sequence` orders the current tape
- address input cannot contain mutable event content, `event_hash`, annotations, lifecycle estimates, or tape position
- a provider address recipe combines its stable native/raw coordinate with a stable fragment discriminator whenever one raw record emits several events
- the serialized address is an opaque, domain-separated deterministic hash; provider-specific seed material remains normalizer implementation detail
- address collisions within one session are a normalizer failure, never repaired by adding sequence

### Event.Ref.Resolution

- the stored canonical object carries `event_address` and `event_hash`; `session` is required when the reference escapes the containing session
- the built-in resolver looks up by address, then compares the asserted hash; it does not scan by hash, relocate by sequence, or offer positional repair
- its API may report `MATCHED`, `AMENDED`, and `MISSING`; these are Chatlas resolver behavior, not mandatory consumer vocabulary in the normal-model contract
- the string form is presentation sugar over address plus hash and never becomes the stored model

### Amendment.Append.Conformance

- an amendment fixture changes raw evidence for already-detected event places and must preserve the complete ordered address sequence and event count; covered content changes must change `event_hash`
- an append fixture adds provider-native evidence and must preserve the prior address sequence as an exact prefix
- classification remains provider-owned; no generic comparison algorithm claims that an insertion, removal, or reorder is an amendment/append

### Neutral.Lineage

- an event may carry an origin `Event.Ref`; several continuations sharing one origin express a branch without a synthetic branch event
- every event stays in recording chronology on its own tape and keeps equal first-class standing
- Claude `parentUuid`/`logicalParentUuid` edges may produce branch relations, but never `on_active_path`, abandoned counts, or a fabricated `lineage.rollback`
- Codex `thread_rolled_back` remains a chronological rollback event because the provider recorded the operation; it references the evidenced origin when the native rollback coordinates make that origin derivable
- cross-session compaction/continuation uses session-qualified refs and `Session.Identity`; it links tapes without copying predecessor events into the continuation
- `Compaction.Summary` remains a provider/assistant-produced system-role message outside `User.Turn`

### User.Turn.Purity.Projection

- `annotations.normal_turn` gains an explicit semantic kind (`user` or `assistant`) alongside its id
- only normalizer-confirmed user-input events receive `kind: user`; injected, provider-generated, assistant-generated, preset, control-only, and synthetic recap records remain first-class events without user-turn membership
- queries, Anchory support resolution, Chat.Index, recents, tagging, and other user-turn consumers select the normalized turn kind rather than `producer.type == "human"`
- adding the annotation does not change `Event.Hash`; existing turn hashes and support assertions remain valid when event content is otherwise unchanged

### Closed.Estimate.And.Delta

- optional `closed.estimate: bool` is model metadata at the observed raw horizon; absence means the normalizer has no estimate
- `closed` is excluded from `Event.Hash` and cannot affect address, event count, or order
- `extras.final` and `event_is_final` are retired from model data and tests
- source and chain hashes remain derivation/integrity metadata; the checkpoint, not the event, stores reuse boundaries and heuristic state
- delta normalization may reuse a verified prefix and revisit a bounded suffix, but the served `events.jsonl` is always the complete current tape with one state per address
- delta output must equal full derivation and must preserve the address invariants before it is accepted

### Materialization.Freshness

- the cache manifest compares both raw-source fingerprint and a materialization revision representing the applicable schema/contract and normalizer generation
- unchanged raw files cannot keep a semantically stale model fresh after the materialization revision changes
- schema, checkpoint, and SQLite generations are bumped together where their stored shapes change; incompatible derived data is rebuilt, not adapted silently

## Execution.Plan

### Vertical.Slice 1 - Freeze the new contract with RED tests

- update `references/normal-model.contract.json` and envelope closure expectations for `event_address`, address-based refs, optional `closed.estimate`, semantic normal-turn kind, and neutral lineage origin refs
- tombstone positional Event.Ref fields, `lineage.on_active_path`, and `extras.final`; keep `sequence` as required ordering metadata
- advance the session-model schema generation and add contract tests that fail on the current implementation
- **observable:** fixtures express the new object shapes and the old positional/finality/active-path fields are rejected
- **check:** targeted contract, envelope, Event.Ref, Normal.Turn, lineage, compaction, artifact, and cache tests are RED for the intended reasons
- **status:** not started

### Vertical.Slice 2 - Assign stable provider-owned event addresses

- introduce the shared opaque-address hashing primitive and require each provider event assembler to supply a stable native/raw seed plus fragment discriminator
- implement and document address recipes for Claude, Codex, and Copilot using native identifiers where present and stable source coordinates as explicit fallbacks
- assign and uniqueness-check addresses before any projection or stored `Event.Ref` is built
- add per-provider amendment and append conformance pairs; include multi-event raw records so fragment identity is exercised
- **observable:** content amendment changes the affected hash without changing address count/order; raw append preserves the previous address sequence as an exact prefix
- **check:** provider conformance tests plus full-tape uniqueness and deterministic re-derivation tests pass
- **deviation trigger:** any provider can only distinguish two event places using mutable content or final sequence; stop and record the raw-model gap instead of weakening the address invariant
- **status:** not started

### Vertical.Slice 3 - Migrate Event.Ref and every address consumer

- replace the positional implementation in `event_ref.py` with address lookup plus hash assertion; remove drift/ambiguity relocation and positional repair behavior
- migrate model-run, tool-invocation, compaction, traceability, view, pattern, inline, file-edition, and public query references to `{event_address, event_hash}`
- change intra-materialization joins to address maps; retain `sequence` only for sorting, display, neighborhoods, and diagnostics
- advance the disposable SQLite event-query schema to key candidates by `(session_identity, event_address)` while retaining sequence as an ordering column
- invalidate old session artifacts/query indexes and reject legacy positional refs at the contract boundary
- **observable:** all stored refs resolve against their own authoritative tape, and amending event content produces an address hit with a failed hash assertion rather than drift
- **check:** Event.Ref unit tests cover matched/amended/missing, non-mutation, malformed legacy refs, stored-reference closure, and scan/SQLite parity
- **status:** not started

### Vertical.Slice 4 - Replace active-path lineage with neutral origin relations

- replace Claude fork marking/injected rollback logic with origin refs derived from `parentUuid`/`logicalParentUuid`; preserve all branches without status labels
- retain Codex `thread_rolled_back` as provider-evidenced `lineage.rollback` and attach the origin ref when its native rollback facts support one
- express compaction summary/retained refs with address-based Event.Ref and add cross-session continuation fields only when provider evidence resolves a `Session.Identity`
- update `dev/user-script-invariant-test` projections, findings, and validation from active/abandoned expectations to neutral first-class branch topology
- add a two-session compaction-continuation fixture because the current invariant corpus explicitly leaves this case uncovered
- **observable:** `A → B → C` and `A → D` are both traversable; no event is active/default/abandoned; Claude branching alone creates no rollback event; native Codex rollback remains on tape
- **check:** rollback/fork invariant sessions, compaction sessions `019fd977-c106-7830-a17b-62d074a4bfa3` and `add4201e-3543-47d8-9914-aa1fc4fec86e`, and focused lineage/compaction tests pass
- **status:** not started

### Vertical.Slice 5 - Make User.Turn purity explicit and consumer-safe

- extend normal-turn annotations with semantic kind and update final grouping to use provider-normalizer input attribution, not raw role or producer vocabulary
- migrate every user-turn consumer currently filtering `producer.type == "human"` to the explicit normalized `User.Turn` semantic
- retain excluded content on tape under its normalized producer/role and verify it cannot satisfy user-turn query or Anchory support lookup
- update purity test names and prose from human-authorship claims to user-input-boundary claims
- **observable:** exact user input is queryable as `User.Turn`; compaction summaries, skill bodies, reminders, presets, and control-only invocations never match as user turns
- **check:** `test_user_turn_purity.py`, compaction tests, turn-query tests, Anchory resolution tests, Chat.Index tests, and existing support refs remain GREEN without hash amendment
- **deviation trigger:** if a proposed purity change alters an existing event’s hashed content rather than grouping metadata, stop and justify the compatibility cost before proceeding
- **status:** not started

### Vertical.Slice 6 - Remove finality from the model and rebase delta/cache policy

- remove `extras.final`, `event_is_final`, finality wording, and final-boundary assumptions from provenance, artifact, delta code, and tests
- add optional provider-derived `closed.estimate`, excluded from event hash, with absence for unknown
- move the reusable-prefix boundary and heuristic inputs entirely into a new delta-checkpoint generation; verify source hashes and a bounded suffix before reuse according to trust tier
- validate spliced output against full derivation and address invariants; fall back to full derivation on any mismatch
- add a materialization revision to the cache manifest and freshness check so normalizer/contract changes invalidate unchanged raw input
- update artifact documentation to describe a rewriteable complete current tape, not append-only JSONL or frozen lines
- **observable:** no served event claims finality; unchanged raw data rematerializes after revision change; delta and full output are identical
- **check:** provenance, delta, artifact, session-cache, amendment/append, source-mutation, and revision-invalidation tests pass
- **status:** not started

### Vertical.Slice 7 - Rebuild documentation and run the complete gates

- update `agentos-md/skills/agentos-hugentics/.skw/src/references/link.skw.md` so `Event.Ref` documentation teaches stable address plus asserted hash and no positional relocation
- run `agentos skw build --skill skills/agentos-hugentics`, then `agentos skw check --skill skills/agentos-hugentics`; never hand-edit the generated `references/link.md`
- update current code docstrings and the normal-model contract; leave Impl.Req 514 untouched as historical evidence
- run targeted suites first, then the complete `agentos-chatlas-py` suite and the user-script invariant corpus
- **observable:** generated Hugentics docs, Python behavior, contract, fixtures, and query surfaces describe the same address semantics
- **check:** `uv run pytest`; `uv run python dev/user-script-invariant-test/validate.py --skip-sweep`; `agentos skw check --skill skills/agentos-hugentics`; repository diffs contain no unintended generated/manual drift
- **status:** not started

## Risks And Deviation Triggers

- **address instability:** a seed includes mutable content, sequence, or an unstable ordinal. Stop on the first amendment/append counterexample; do not patch it with repair-on-read.
- **fragment collision:** one provider record emits multiple same-kind events without a stable discriminator. Treat this as a provider address-recipe defect.
- **silent reference compatibility:** accepting `{event_hash, sequence}` beside the new shape would preserve ambiguous semantics. Reject legacy refs and rebuild derived stores.
- **lineage policy leakage:** any `active`, `current`, `default`, `preferred`, `abandoned`, or equivalent status enters canonical lineage. Stop and move that policy to the consumer.
- **fabricated rollback:** a branch alone causes a rollback event. Stop; only a provider operation record may create `Lineage.Rollback`.
- **purity/hash churn:** identifying `User.Turn` by changing producer/content invalidates durable assertions. Use annotation semantics unless a separately authorized producer-vocabulary migration is designed.
- **heuristic promoted to truth:** checkpoint reuse or `closed.estimate` is described as guaranteed finality. Stop and restore best-effort/fallback semantics.
- **cross-session evidence gap:** a continuation cannot be resolved to a session identity from provider evidence. Preserve native evidence without inventing a link.

## Acceptance Signals

- every canonical event has one deterministic, session-unique `event_address`; every tape keeps strictly increasing `sequence`
- representative provider amendments preserve address sequence and count; representative appends preserve the old address sequence as an exact prefix
- every stored `Event.Ref` carries address plus asserted hash and resolves without positional search or repair
- address-stable content change is observable as an amended assertion; absent address is observable as missing
- no canonical event contains `extras.final` or `lineage.on_active_path`; no branch is assigned path status
- Claude forks preserve both branches without fabricating rollback; provider-recorded Codex rollback remains first-class
- compaction summary text cannot enter a `User.Turn` or satisfy a user-turn query; every accepted invariant-script user input remains exact and first-class
- session artifacts refresh when either raw observation or materialization revision changes
- delta output equals full derivation and falls back safely when verification fails
- Skillware source and generated Hugentics `Event.Ref` documentation agree with the Python contract
- targeted suites, full `uv run pytest`, invariant corpus, and `agentos skw check` are GREEN

## Impl.Log

- Design inspection found the current implementation still addresses events by `{event_hash, sequence}`, relocates by hash after positional drift, persists `extras.final`, derives Claude active/abandoned status plus synthetic rollback, and identifies user turns through `producer.type == "human"`.
- Compatibility decision: add explicit normalized turn kind rather than rename producer values in this request. Because producer participates in `Event.Hash`, a vocabulary rename would invalidate every affected `Normal.Turn.Ref` and support record; that is a separate migration, not a hidden purity implementation step.
- Documentation decision: the maintained stale surface is the Hugentics Skillware `link` source. Impl.Req 514 remains unchanged because it records the historical design and execution that this request supersedes.
