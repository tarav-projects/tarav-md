# Normal Turn Annotations - impl-req

## Impl.Abstract

- **scope:** implement the landed `Event.Annotation`, `Event.Grouping`, `Event.Group.Hash`, `Normal.Turn`, `Normal.Turn.Id`, and `Normal.Turn.Ref` design across Chatlas normalization, query, Anchory, dependent Agentos consumers, materialized models, and the live anchor corpus
- **status:** implemented and verified
- **source:** direct autonomous development request plus the approved Chatlas ontology cluster
- **support set:** execution gate ^c20260731-30u
- **compatibility:** move forward to the new normal-model and support-set schemas; do not retain old-format acceptance paths

## Impl.Agendix

- **touched (index):** `Event.Hash`, `Event.Annotation`, `Event.Grouping`, `Event.Group.Hash`, `Normal.Turn`, `Normal.Turn.Id`, and `Normal.Turn.Ref` in `agentos-chatlas-pkg/design/100-design.md`
- **historical implementation:** `notes/live/513-normal-turn-identity-impl-req.md` established stable interaction IDs and `chatlas.support-set.v2`, but intentionally grouped a user submission and the following assistant response under one identity; this implementation supersedes that grouping
- **active dependency:** uncommitted `Chatlas.Event.Pattern` and `chatlas turns query` work already projects legacy turns; preserve and migrate it
- **dependent repositories:** `agentos-chatlas-py` owns the model and Chatlas support-set runtime; `agentos-py` validates Skillware edition support records; `agentos-cli` supplies end-to-end command tests; `agentos-chatlas-md` owns this artifact; `agentos-md` owns the generated Hugentics linking guidance consumed by grounding workflows
- **live data:** `~/Documents/chatlas/views/chatlas-session`, the event-query SQLite projection, Claude delta checkpoints, and `~/Documents/chatlas/anchory`
- **index reconciliation:** the existing `Chatlas.Anchory` line still names `chatlas.support-set.v2`; implementation must not bypass the Index edition gate, so record the required v3 amendment for a later reviewed index edition

## Impl.Index

### Event.Annotation

- a normalized event may carry an optional top-level `annotations` object
- `annotations.normal_turn.id` assigns the event to one `Normal.Turn`
- the legacy top-level `turn_id` is retired from the neutral event envelope
- annotations do not participate in `Event.Hash`

### Event.Group.Hash

- a group hash is SHA-256 over the ordered full `Event.Hash` values of its member events
- annotation kind, annotation identity, tape position, and other derivation metadata do not participate
- changing group membership changes the hash; relabeling an unchanged group does not

### Normal.Turn

- one human user interaction and the following assistant activity are different groupings
- a user turn contains only events carrying user-supplied data from that interaction; provider, system, harness, tool, and assistant events never join it
- an assistant turn is independently grouped and may contain assistant messages, reasoning, tool activity, run lifecycle, and response-local metrics
- session/context events that are not part of either semantic turn remain unannotated
- attachments carried by a human input event remain part of that user turn

### Normal.Turn.Ref

- the canonical object is `{session, turn_id, turn_hash, at}`
- `turn_id` locates one session-local grouping and `turn_hash` verifies its current ordered content
- `at` is diagnostic/readability metadata and must match the turn landing event
- Chatlas query results and `chatlas.support-set.v3` records emit the canonical object
- CLI member strings may remain input sugar because registration resolves them immediately into the canonical object

### Migration Integrity

- preserve each existing support member by its current human landing event hash before rebuilding models
- after rebuilding, locate that exact event in the same authoritative session and derive its corrected user-turn reference
- migrate tokenized approval cargo references through their referenced event hashes as well; proposal refs must resolve to assistant turns and approval refs to user turns
- never choose a nearby turn when exact evidence is absent or ambiguous; report the record for remediation and leave the pre-migration backup intact

## Execution.Plan

### Slice 1 - Core annotation and reference primitives

- add event annotation helpers, normal-turn lookup/grouping helpers, `Event.Group.Hash`, and `Normal.Turn.Ref` construction and validation
- change the closed event envelope and `SemanticEventBuilder` from required top-level `turn_id` to optional normal-turn annotation
- advance `Chatlas.Session.Model` to schema version 4 and update the normal-model contract
- observable: event hashes remain stable when annotations or turn IDs change, while turn hashes change when ordered membership changes
- check: focused primitive, envelope, artifact, and contract tests
- status: completed

### Slice 2 - Correct every provider normalizer

- annotate independent user and assistant turns for Claude Code, Codex, and Copilot CLI
- preserve provider-native interaction/turn handles only under `native`; derive session-local normal-turn IDs without conflating roles
- update Claude delta resume/checkpoint state so resumed and full derivation produce identical annotations and hashes
- preserve event content, order, source refs, projections, and lineage except where turn grouping is the intended change
- observable: a user message and its assistant response always have different normal-turn IDs; tool activity groups with the assistant turn; non-turn events have no normal-turn annotation
- check: provider fixtures, delta/full equivalence, fork/rollback, and explicit authority regressions
- status: completed

### Slice 3 - Migrate all turn consumers

- update turn query/projection, neighborhoods, filters, index checks, approval-gate evaluation, and any other turn lookup to use shared annotation/grouping helpers
- emit canonical `Normal.Turn.Ref` objects from query results while retaining member-string input sugar only at the CLI boundary
- make tokenized approval cargo carry canonical proposal and approval turn refs rather than string refs
- update command help, examples, contracts, and tests in Chatlas and Agentos consumers
- observable: turn queries return role-pure authoritative groups, and approval checks cannot mistake assistant text for user authority
- check: event/turn query parity, approval checks, Anchory runtime tests, Skillware edition-history tests, and CLI e2e tests
- status: completed

### Slice 4 - Support-set v3 and exact migration tooling

- replace `chatlas.support-set.v2` with v3 members containing `session`, `turn_id`, `turn_hash`, and `at`
- validate both turn identity and group hash on resolve/amend; reject old records rather than silently accepting them
- add a one-shot migration command or live script that snapshots v2 member/cargo event evidence, rebuilds models, rewrites records exactly, and reports unresolved/ambiguous cases
- observable: every newly registered support member is self-verifying, and a changed grouping produces an explicit integrity failure
- check: v2 rejection, v3 registration/resolution/amendment, hash drift, cargo migration, and dry-run migration tests
- status: completed

### Slice 5 - Rebuild and migrate live data

- checkpoint the Anchory depot, snapshot migration evidence, invalidate schema-v3 model artifacts and old delta/event-query caches, then rebuild authoritative session models from raw archives
- migrate the full Anchory corpus and tokenized cargo to v3
- rebuild the disposable Event.Pattern SQLite index only after authoritative models are current
- observable: no schema-v2 support record or schema-v3 session model remains in active storage; every active support member resolves with its turn hash
- check: corpus counts before/after, zero unresolved migration records, full Anchory application check, session-model schema audit, and SQLite/scan parity sample
- status: completed

### Slice 6 - Full verification and operational closeout

- run the complete suites for `agentos-chatlas-py`, `agentos-py`, and `agentos-cli`
- run relevant Skillware/Index checks without editing gated ontology lines
- update this artifact with commands, counts, deviations, residual POIs, and the deferred reviewed Index amendment
- observable: code, generated models, and anchor records all implement one model with no compatibility ambiguity
- check: repository status review and cold re-read against every execution-plan item
- status: completed

## Impl.Log

- execution gate: autonomous implementation request anchored ^c20260731-30u
- inventory found the legacy interaction grouping in all three supported `Chatlas.Session.Model` normalizers, the closed event envelope, schema contract, Claude delta state, turn query, Anchory v2, tokenized approval checks, and Skillware edition-history validation
- migration policy: exact event-hash bridge only; no nearest-turn fallback
- mandatory pre-execution checkpoints: `agentos-chatlas-md` `b0d1802`, `agentos-chatlas-py` `00a5c81`, `agentos-py` `ab87e87`, and `agentos-cli` `5e86abd`
- implemented schema-4 optional `annotations.normal_turn.id`, annotation-independent `Event.Hash`, ordered `Event.Group.Hash`, canonical `Normal.Turn.Ref`, and shared lookup/validation helpers
- corrected Claude Code, Codex, and Copilot CLI to separate human user turns from independently grouped assistant activity; Copilot run events retain provider turn handles under `native` without replacing semantic grouping
- migrated turn query, neighborhoods, approval checks, Anchory, Skillware edition history, CLI help, contracts, and operational Hugentics linking guidance; generated Skillware surfaces rebuilt with zero POIs
- migration evidence snapshot: `/Users/pereiro/Documents/chatlas/anchory-backups/20260731-normal-turn-migration-snapshot.json`; complete pre-write depot backup: `/Users/pereiro/Documents/chatlas/anchory-backups/20260731T141705Z-before-support-set-v3`
- migration rewrote 532 snapshot anchors and 562 support members; the post-migration active corpus contains 533 anchors and 563 members across 37 sessions, all resolving exactly under `chatlas.support-set.v3`
- repeated semantic events exposed that `Event.Hash + at` is not unique: two distinct `approve` turns shared both values. Migration therefore also used the prior `turn_id` coordinate, preserving user IDs and mapping assistant IDs to `<old-id>:assistant`; all 736 member and typed-cargo references validated before write
- rebuilt retained Claude archive indexes so all 36 migration snapshot identities remained mechanically reachable after index reset
- rebuilt the disposable Event.Pattern SQLite surface: 12,065 materialized sessions and 200,792 indexed query events; scan and SQLite returned the same canonical reference for the execution-gate turn
- full materialized-corpus audit: 12,065 schema-4 models, 2,009,358 events, and 87,158 annotated groups; zero legacy top-level `turn_id`, mixed human/non-human grouping, or invalid user-turn findings
- verification: `agentos-chatlas-py` 292 passed, `agentos-py` 592 passed, `agentos-cli` 71 passed; Ruff passed in all three repositories; `agentos skw check --skill skills/agentos-hugentics` reported zero POIs and diagnostics
- deferred reviewed Index amendment: `Chatlas.Anchory` still names `chatlas.support-set.v2`; changing that gated ontology line requires a later tokenized Index edition rather than an implementation-side bypass
