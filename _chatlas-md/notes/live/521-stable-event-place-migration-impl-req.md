# Stable Event Place Migration - impl-req

## Impl.Abstract

- **scope:** perform the hard-cut migration of the maintained Chatlas runtime and its direct Agentos consumers to the schema-5 stable-event-place model already implemented by Impl.Req 520
- **status:** completed
- **source:** explicit request to perform the migration and the subsequent `NO.LEGACY.ALLOWED` constraint ^c20260809-48u ^c20260809-49u
- **repositories:** `agentos-chatlas-py` for current-model fixtures, query semantics, and migration gates; `agentos-cli` for the direct composition fixture; `agentos-chatlas-md` for package documentation and the execution record; `agentos-md` for maintained Agentos skill consumers; `/Users/pereiro/Documents/chatlas` for the active derived and durable dataset
- **mode:** hard cut — no positional `Event.Ref` reader, session-model-v4 reader, dual writes, translator, compatibility fallback, or automatic reference relocation

### In scope

- replace every active schema-4 `Chatlas.Session.Model` materialization with schema 5 or remove it when its retained raw source cannot currently normalize
- rebuild the disposable Event.Pattern SQLite index under schema 6, which adds normalized `turn_kind` as an indexed semantic axis, and accept only current delta checkpoints
- find and eliminate current tests, examples, and maintained docs that still construct or teach the displaced normal-model fields
- live-resolve every current Chatlas Anchory support member against schema-5 models; unresolved evidence is a migration failure requiring explicit repair, never relocation
- audit every retained Chat.Index and the retained `zip-transcript-summary` product set against current model-derived input
- run the direct composition suite and the complete Chatlas model/invariant gates

### Out of scope

- provider raw archives, session identity, annotations, and source-index rows: these are migration authority, not derived state
- historical notes and explicitly archived/backup directories
- unrelated versioned formats whose payload does not embed the displaced event model; a lower version number in another schema family does not make it a legacy `Chatlas.Session.Model`
- changing evidence meaning to make an audit green

## Impl.Agendix

- **touched (chat):** perform the stable-event-place ecosystem migration ^c20260809-48u
- **touched (chat):** admit no legacy reader, translator, dual-schema mode, or compatibility fallback ^c20260809-49u
- **touched (implementation):** Impl.Req 520 defines schema 5, stable `event_address`, address/hash `Event.Ref`, neutral lineage, `User.Turn.Purity`, current-only cache generations, and the completed Python implementation
- **structural:** `agentos-chatlas-py/src/agentos_chatlas/session_cache.py` owns session-model cache freshness; `event_query.py` owns the disposable SQLite generation; `normalization/session_model/delta.py` owns checkpoint generation
- **structural:** `agentos-chatlas-py/src/agentos_chatlas/anchory.py` live-resolves durable `Normal.Turn.Ref` members; Chat.Index and product commands own their retained-surface audits
- **measured active state:** 12,576 session-model directories: 12,573 schema 4 and 3 schema 5; 12,573 generation-1 manifests and 3 generation-2 `stable-event-place-v1` manifests
- **measured active state:** 3,400 current `chatlas.delta-checkpoint.v2` files; Event.Pattern SQLite metadata at schema 4; 2,973 Anchory records carrying 4,525 support members; 11 retained Chat.Index surfaces; 824 retained zip-transcript product JSON files
- **measured consumer state:** `agentos-cli` is the only direct Python package consumer and its suite passes 70 tests; one composition fixture still constructs `annotations.normal_turn` without semantic `kind`
- **measured durable-ref state:** no persisted `Event.Ref`, `event_hash`, `lineage.on_active_path`, or `extras.final` was found outside disposable session models in the active Chatlas root

## Impl.Index

### Migration.Current.Only

- current model producers and consumers accept only schema 5 and `{event_address, event_hash}`
- migration does not preserve a callable legacy path; incompatible derived artifacts are recomputed from raw authority or removed
- test fixtures are contract consumers and must use the same current schema as production artifacts
- migration success is proved by positive current-schema conformance and a zero-result legacy scan, not by the ability to read old data

### Derived.State.Rebuild

- `agentos chatlas events index` is the corpus-wide materialization driver: rebuilding the complete disposable candidate index necessarily loads authoritative session models and refreshes stale session caches
- schema-5 cache freshness requires session schema 5, manifest schema 2, and materialization revision `stable-event-place-v1`
- current `chatlas.delta-checkpoint.v2` files remain eligible only when their associated current artifact validates; checkpoint reuse failure falls back to full derivation
- any schema-4 cache left after the corpus rebuild belongs to a session that could not rematerialize; remove that derived cache and retain the build failure as the authoritative finding

### Durable.Evidence.Audit

- Anchory members remain `Normal.Turn.Ref`; the migration must resolve all 4,525 members through `User.Turn.Purity`
- a formerly accepted synthetic or injected user-role record must fail rather than be promoted or relocated
- Chat.Index is first-class retained Markdown and is audited in place; it is not deleted with disposable caches
- retained products use their own schema family; freshness is determined from current view input, not inferred from their product schema number

### Consumer.Closure

- Event.Pattern documentation teaches `event_ref`, not retired `event_id`
- user-input selection is described through normalized turn semantics; producer remains an independent attribution axis
- downstream fixtures include `annotations.normal_turn.kind`
- source/test scans reject positional Event.Ref, session-model schemas below 5 in current-model fixtures, active-path/finality fields, and user-turn selection through producer alone

## Execution.Plan

### Vertical.Slice 1 - Freeze hard-cut migration gates

- add focused tests or scan gates for current model fixture schema, semantic normal-turn kind, and absence of displaced reference/lineage/finality fields across maintained source, tests, and package docs
- update stale Event.Pattern and turn-query documentation plus the direct `agentos-cli` composition fixture
- **observable:** maintained executable examples and fixtures express only the schema-5 model
- **check:** focused Chatlas and CLI tests plus a repository legacy scan pass
- **status:** completed

### Vertical.Slice 2 - Rebuild the complete active derived corpus

- run `agentos chatlas events index --json`, allowing the schema-5 cache revision to rematerialize every buildable indexed session and replace the schema-4 Event.Pattern database
- capture build failures without weakening model validation
- remove only remaining incompatible session-model directories after verifying each is derived and failed to rebuild; leave raw/session-index authority untouched
- audit checkpoint schema and discard only malformed, non-current, or orphaned checkpoints proven unusable after cache replacement
- **observable:** active session-model storage contains zero schema-4 artifacts and Event.Pattern SQLite reports schema 6
- **check:** filesystem/schema census and `agentos chatlas events index` report
- **status:** completed

### Vertical.Slice 3 - Validate durable Anchory authority

- enumerate every Chatlas Anchory record and live-resolve every support member against authoritative schema-5 models with a bounded runtime cache
- report anchor, member, and exact failure reason; do not search nearby content or rewrite records automatically
- repair only defects whose intended support is independently evident and whose edit is explicitly justified; otherwise retain a blocking finding
- **observable:** every retained member is an exact current `User.Turn`, or an explicit unresolved finding remains
- **check:** 2,973 records / 4,525 members are accounted for with zero silent skips
- **status:** completed

### Vertical.Slice 4 - Audit retained Chat.Index and product surfaces

- run the read-only Chat.Index audit for all 11 retained identities against their current authoritative tapes
- evaluate every retained `zip-transcript-summary` product's freshness against current view input; regenerate stale derived inputs/products only through their owning product workflow
- do not edit retained narrative merely because event sequence or internal grouping changed
- **observable:** every retained surface is current or has an explicit owner-native stale/failure result
- **check:** complete identity/accounting reports for Chat.Index and product registries
- **status:** completed

### Vertical.Slice 5 - Cross-system completion audit

- run full `agentos-chatlas-py` tests, Ruff, the 21-session invariant and both projection passes, `agentos-cli` tests, Skillware checks, and JSON/diff hygiene
- rerun the current-only filesystem and repository scans after every repair
- prove raw archive/session-index counts were not reduced by derived-state migration
- **observable:** no active legacy model artifact or maintained legacy consumer remains
- **check:** all named gates green; before/after authority counts match; all retained-surface populations are accounted for
- **status:** completed

## Risks And Deviation Triggers

- **authority deletion:** any proposed deletion reaches `raw/`, `index/`, annotations, Anchory, Chat.Index, or committed products. Stop; only proven disposable derived state may be removed automatically.
- **compatibility creep:** a reader accepts positional Event.Ref or session model v4. Remove it rather than carrying transition semantics.
- **silent purity repair:** an invalid support member is moved to similar text. Stop and surface the evidence failure.
- **partial corpus claim:** a narrow recent-session rebuild is used to claim migration of 12,576 artifacts. Continue until the complete census is accounted for.
- **product-schema confusion:** an independent product schema number is classified as legacy solely because it is below 5. Judge its own current contract and current input fingerprint.
- **unbounded collateral edit:** historical notes or backup directories are rewritten to make text search green. Restrict scans to maintained executable/current documentation surfaces.

## Acceptance Signals

- zero active session models have schema other than 5; every surviving manifest is schema 2 with `stable-event-place-v1`
- Event.Pattern SQLite metadata is schema 6 and complete for the post-migration corpus
- no current source, executable fixture, or maintained package documentation accepts or teaches positional Event.Ref, `lineage.on_active_path`, `extras.final`, or producer-only `User.Turn`
- every Chatlas Anchory record and support member is accounted for by exact current-model resolution
- every retained Chat.Index and zip-transcript product is accounted for by its owning currentness/audit workflow
- raw archive and session-index authority populations are unchanged by derived-state cleanup
- all Chatlas, CLI composition, invariant, projection, and Skillware gates are green

## Impl.Log

- Execution authorized and grounded at the current-session gate ^c20260809-50u
- Design resolved the migration as a hard cut. No translation or compatibility implementation is authorized.
- Current automatic invalidation is necessary but insufficient: 12,573 stale schema-4 directories still physically occupy the active Chatlas root, so migration must drive a corpus-wide rebuild and then remove unrebuildable derived remnants.
- Durable migration is primarily verification: active non-derived storage contains no persisted Event.Ref, while Anchory carries turn-level assertions whose exact resolution must be proven under `User.Turn.Purity`.
- Slice 1 closed with public `turn_kind` predicates on Event.Pattern and `turns query`, exact SQLite candidate indexing for that semantic axis, schema-5 fixtures, current Chatlas and Hugentics package documentation, and the direct `agentos-cli` fixture. Maintained Agentos Skillware was rebuilt from source and checks with zero findings.
- Slice 2 rematerialized the complete active corpus: 12,712 session models now report schema 5 and all 12,712 manifests report schema 2 / `stable-event-place-v1`. The schema-6 Event.Pattern database covers 203,646 events across the same 12,712 sessions. The owning materializer discarded 337 provider-private checkpoints that no longer had delta state; the 3,063 surviving checkpoints are all `chatlas.delta-checkpoint.v2`. These caches are derived and the raw authority remains available.
- Slice 3 live-resolved all 2,974 Chatlas Anchory records and all 4,526 support members across 54 referenced sessions with zero failures and no relocation.
- Slice 4 audited all 11 retained Chat.Index surfaces: all owner-native audits succeeded with zero blocking findings; eight tails are current and three are ordinary append-only tails. Per explicit user direction, all 412 retained `zip-transcript-summary` products were status-audited and intentionally left stale; none is missing or invalid, and none was reproduced or rewritten.
- Slice 5 passed 474 Chatlas tests, Ruff, 21 invariant corpus sessions plus the random sweep, both projection gates, comparative projection, 70 direct CLI tests, Skillware checks, JSON validation, and diff hygiene. A forced SQLite `--turn-kind user` query returned the exact expected compaction-corpus user turn.
- Authority accounting is unchanged: 35,174 raw files and 768 session-index files before and after. No raw, index, annotation, Anchory, Chat.Index, or retained product artifact was deleted or rewritten by the migration.
