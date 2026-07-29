# 514 — Stable Event Addressing — Impl.Req

## Impl.Abstract

**Scope.** Give `Chatlas.Session.Model` a canonical `event_hash`, define the `Event.Ref` object consumers store to address one event, move `Delta.Normalization` bookkeeping into a declared `extras` namespace, and replace `event_id` with `Event.Ref` at every reference site before retiring it.

**Why.** Impl.Req 513 gave *turns* a stable identity and re-keyed every durable reference onto it. Sub-turn addressing was left unsolved: `event_id` is still `"event-" + sequence`, and `Event.Pattern`, `inline`, and `file_edition_pois` genuinely need to address one event, not a whole turn. 513's Slice 5 attempted a straight retirement and was blocked — removing the field breaks an agent-facing DSL with nothing to replace it. This artifact supplies the replacement first.

**Status.** Fully executed and independently verified. Slices 1–7 are complete: stored references, query/selection surfaces, skill documentation, derived SQLite addressing, and the canonical event envelope all use `Event.Ref`; `event_id` is retired. Suites green: `agentos-chatlas-py` 248, `agentos-py` 551, `agentos-cli` 62. Corpus GREEN. Index and Skillware checks are byte-clean on both depots.

Slices 5–7 were executed across two concurrent sessions and then re-checked from scratch by a third party to the implementation — 4,013/4,013 stored refs `MATCHED` over three providers, and the drift check confirmed to fire rather than merely to exist. The verification pass corrected an unreproducible coverage claim, an overstated session count, and one latent defect; see **Slices 5–7 — independent verification** in the `Impl.Log`.

**Source context.** Design discussion anchored at `^c20260728-4u`. Concepts landed in 513: `Event.Grouping`, `Normal.Turn`, the `Session.Event.Tape` amendments, and the `Chatlas.Session.Model` boundary line.

**Out of scope.**
- turn-level addressing — `Chat.Support.Set` members stay on `turn_id`; the turn remains the grounding unit and nothing here re-opens it.
- populating `Delta.Normalization` for codex. The provenance fields are claude-only *because* delta normalization is claude-only; this artifact relocates and declares them, it does not generalize the delta layer.
- repairing stale references automatically on read paths.

## Impl.Index

### Current.State

- `event_id` is emitted at `normalization/session_model/events.py:210` as `f"event-{sequence}"`, beside `sequence` — 126 references across 15 files.
- consumers needing sub-turn addressing: `event_query.py` (a sqlite index keyed `(session_identity, event_id)`), `event_pattern.py` (the `Event.Pattern` DSL — an `event_id` predicate and an `event_ids` projection), `inline.py`, `file_edition_pois.py`, `traceability.py`, `_views.py`.
- `agentos-py`'s `edition_history.py` already moved to `turn_id` in 513 and needs nothing here.
- `source_hash`, `chain_hash`, and `final` are attached by `attach_tape_provenance`, called only from `_claude.py` and `delta.py`; `claude_delta_normalization_result` is the only delta implementation.
- **those three keys are absent from `SEMANTIC_EVENT_ENVELOPE_KEYS`** — by the model's own closure rule they are envelope leakage on every claude event today.
- events are mutated after `SemanticEventBuilder.append`, but only in fields the digest does not cover: `tool_invocation_ref` (per-provider post-passes), `model_run_ref`, `lineage` (`_claude_mark_fork_lineage`), `native`, and the provenance keys. Audited across `normalization/` — no post-append write touches `kind`, `producer`, `payload`, or `timestamp`.
- `_canonical_json` in `provenance.py` already pins a canonical encoding (sorted keys, tight separators, `ensure_ascii=False`, `allow_nan=False`).

### Hard.Evidence

- **`source_hash` cannot serve as an event digest, for two independent reasons.** It is not unique: on the live design session 5070 events yield 3242 distinct values, with **2954 events (58%) colliding**, because fan-out means several events derive from one raw record — it answers "which raw produced this", not "which event is this". And it is not universal: coverage is 89/89 on claude and **0/101 on codex**, as are `chain_hash` and `final`.
- **Content genuinely repeats, so no digest can be unique.** Measured ambiguity for a purpose-built digest over `kind + producer + payload + timestamp`: claude 12/89 (13.5%), codex 0/101, live session 629/5070 (12.4%). Composite keys do not close it (`source_hash + kind` → 623 colliding; `+ turn_id` → 520). The repeats are real — identical tool calls, identical usage records — so ambiguity is a designed resolution path, not a defect.
- **Adding `native` to the digest buys nothing.** Live 629 → 623 (0.1pp), corpus unchanged. Excluded on the evidence rather than on principle.
- **Drift is structurally bounded to the tape's tail.** `Delta.Normalization` freezes a prefix and recomputes only the volatile tail. The 513 audit matched: 0 drift across 391 closed-session anchor members, 6/6 in the one live session. An index is therefore a sound fast path with a bounded failure region.
- **Schema markers make migration mechanical.** 513's v1→v2 anchory migration was detectable, scriptable, and verifiable purely because every record carried a `schema` field.

### Design.Decisions

- A reference is a **minimal assertion**, not an identity: an `Event.Ref` claims "the event with this digest was at this sequence". Neither half is stable alone; together they are self-verifying. The sequence disambiguates what the digest cannot, and the digest validates what the sequence cannot.
- **An `Event.Ref` is an `event_id` plus a change-check** — the same positional address, plus the ability to notice the answer moved. It is therefore an upgrade wherever a reference is stored, not an alternative addressing scheme competing with the local id.
- **The reference is an object; the string is sugar.** A composite packed into `"<hash>:<sequence>"` is a raw-ish encoding posing as canonical, and the model already carries composite references structurally (`source_refs`). The object is also field-additive, which is what a schema marker would otherwise buy.
- **The event carries the digest; the reference carries the position.** `event_hash` is a canonical field so consumers never recompute semantics — only chatlas does, which keeps the derivation pinned in one place.
- **Verification strength is the storer's choice, with a floor.** The stored digest is a prefix, so short and full are one dial rather than two hashes; 8 bytes is the minimum, because below it the check still reads as safety while providing almost none.
- `event_hash` is **core model semantics, not `extras`** — it is a property of the chat event, in the same category as `turn_id`. Keeping it canonical is what stops `extras` absorbing identity on its first use.
- The digest covers `kind + producer + payload + timestamp`, excluding `sequence`/`event_id` (positional — including them recreates the original defect), `source_refs` (raw indices shift), the provenance fields (segmentation-sensitive and claude-only), `turn_id` (would couple event identity to turn grouping, so a purity change would move hashes), and `native` (measured worthless).
- **Where it is computed is free today**, and the plan does not mandate a placement. Every post-append mutation writes `tool_invocation_ref`, `model_run_ref`, `lineage`, `native`, or the provenance keys — none of which the digest covers — so the mutated set and the hashed set are disjoint. Compute at append or in a later pass; a mutated event simply recomputes if the sets ever meet. What the plan does mandate is the **detection**: the covered and mutated sets could intersect later (someone adds `outcome` to the digest, or a post-pass starts touching `payload`), and a missed recompute then goes stale silently. The invariant is enforced by test, not by placement.
- **`extras` is a declared namespace for content that is not about chat semantics** — optional on any model object, contract-declared by full path (`$.chat.events[*].extras.source_hash`), excluded from projection semantics like the existing annotation-class region. `Delta.Normalization` bookkeeping is about how the model was computed, not about the conversation; this is the same boundary as "the model carries chat data, never a consumer's interpretation", drawn from the upstream side.
- A failed assertion is a **POI, not an error** — matching how duplicate-anchor detection already behaves: surface it, never auto-resolve. Resolution may return the repaired event alongside the finding, but a read path never rewrites a stored reference; repair stays an explicit act, as with `amend`.
- **Placement is revisable, bindings are not.** Where a field lives can change later — `retired_keys` exists for exactly that. What durable references bind to cannot. That is the whole lesson of `event_id`: the field was fine, pointing something durable at it was not.

### Impl.Agendix

**chat → touched**: `^c20260728-4u` — the ordered support set for this design: the `--design` ordering turn, the `<hash>:<idx>` locator decision, the event-versus-reference split, `event_hash` as a model field, and the `extras` namespace plus the robustness-to-change principle.

**index → touched** (`agentos-chatlas-pkg/design/100-design.md` unless noted):

- `Session.Event.Tape` — `sequence` is the only positional field; durable references key on a grouping carrying a stability contract.
- `Event.Grouping`, `Normal.Turn` — the turn layer this builds under; `turn_id` bounds nothing here but defines what a turn member is.
- `Chatlas.Session.Model` — the model carries chat data, never a consumer's interpretation; `extras` extends that boundary upstream.
- `Chatlas.Session.Model.Contract`, `Chatlas.Session.Model.Tests`, `Delta.Normalization::Chatlas`, `Normalization.Pipeline::Chatlas.Session.Model`.
- `agentos-pkg` `Normalization.Pipeline-appendix`: `Normal.Model.Contract` (regions, retired keys, null policy), `Model.Fragment` (topological, not positional; partial by definition), `Under.Normalization`, `Inline.Raw.Source`, `Projection.Test`, `Path.Source.Split.Test`, `Normalization.Coverage`.

## Execution.Plan

### Slice 1 — `extras` region, and close the envelope — **DONE**

**Result.** `extras` added to `SEMANTIC_EVENT_ENVELOPE_KEYS` with `event_extras`/`set_event_extra` accessors mirroring the existing `native` pair; `source_hash`, `chain_hash`, `final` moved under it, with `event_is_final`/`event_chain_hash`/`event_stored_source_hash` readers so consumers never reach into the dict. `chain_event_hash` and `strip_tape_provenance` handle the nesting. Contract declares the `extras` region (`$..extras..*`, outside projection semantics) plus the three paths with their null policy. Slim filter drops `extras` wholesale. Tests: `tests/test_event_envelope_closure.py` (2, RED→GREEN); suite 218 green. Corpus: zero undeclared top-level keys on claude and codex; claude 89/89 carry `extras`, codex 0/101 — the null policy holding exactly as declared.

**The corpus harness is GREEN again — 19/19 sessions across all three scripts.** It had been RED throughout Impl.Req 513.

- add `extras` to `SEMANTIC_EVENT_ENVELOPE_KEYS`; move `source_hash`, `chain_hash`, `final` under it.
- declare the region in `Chatlas.Session.Model.Contract` by full path, with a null policy ("present where `Delta.Normalization` applies") and an explicit exclusion from projection semantics.
- **RED→GREEN**: a closure test asserting no claude event carries an undeclared top-level key — RED today, since the three provenance keys are leakage right now.
- **Check (corpus)**: `Path.Source.Split.Test` no longer queues the provenance paths as source-split candidates; `Normalization.Coverage` does not count them as chat expressiveness.
- **Observable**: `agentos chatlas update --trust rebuild` produces tapes whose provenance rides under `extras`.

### Slice 2 — `event_hash` — **DONE**

**Result.** `compute_event_hash` and `EVENT_HASH_FIELDS = (kind, producer, payload, timestamp)` live in `events.py` beside the builder, so all three providers inherit it; `SemanticEventBuilder.append` stamps it. Contract entry states the covered set explicitly and records that the digest is deliberately *not* unique. Tests: `tests/test_event_hash.py` (6, RED→GREEN) — coverage, the standing recompute invariant, stability across re-derivation, stability across tail growth, position-independence under an inserted earlier turn, and sensitivity to changed content. Suite 224 green.

**Corpus:** coverage 89/89 claude, 101/101 codex, 5955/5955 live; recompute reproduces every stored value on all three; ambiguity 13.5% / 0.0% / 12.4% — the recorded baseline, so the covered set means what it meant when it was measured.

- add the canonical field, populated by all three normalizers, reusing `_canonical_json`.
- contract entry: meaning, `null: never`, and the covered field set stated explicitly — the set *is* the contract, since consumers depend on reproducibility.
- **Check**: re-derive a session twice; every `event_hash` identical. Re-derive after appending to the tail; frozen-prefix hashes unchanged.
- **Check (corpus)**: present on 100% of events for claude *and* codex — the generality bar 513 set. `Path.Source.Split.Test` shows no source split.
- **Check**: measured ambiguity stays near the recorded baseline (~12% live, 0% codex) — a large move means the covered set changed meaning.

### Slice 3 — the reference form — **DONE**

**Result.** `src/agentos_chatlas/event_ref.py`: `resolve_event_ref` returns an `EventRefResolution` (outcome, event, finding, repaired_ref) across four outcomes — `MATCHED`, `DRIFTED`, `MISSING`, `AMBIGUOUS`. A repair is always *offered*, never applied. Tests: `tests/test_event_ref.py` (12), including that resolution mutates neither the tape nor the reference. Suite 237 green.

**Reshaped after review — the object is the model, the string is sugar.** The first cut made `"<hash>:<idx>"` primary, which is a composite packed into a delimited string: the raw-ish encoding posing as canonical that `Under.Normalization` warns about, and inconsistent with `source_refs`, which the model already carries as objects (`{line, record_index, source_ref_id}`). The reference is now:

```json
{ "event_hash": "caa55f90bec3cf7e", "sequence": 2042 }
```

- **`sequence`, not a list index** — the reference speaks the model's own coordinates, so its assertion is statable in contract terms. This also removed a real defect: the first cut addressed by 0-based Python list position while the model's positional field is 1-based.
- **`event_hash` is a digest prefix, and its length is the storer's choice** — short is a prefix of full, so strength is one dial rather than two hashes, and a resolver compares only the characters it was given. `EVENT_HASH_MIN_CHARS = 16` (8 bytes) is the floor: below it the check still *looks* like verification while providing almost none, which is worse than no check.
- **`schema`, `session`, `at` are optional**, added only where a reference escapes a context that already supplies them. The object is field-additive, so extension needs no marker — that is what the schema string was buying, and an object provides it structurally.
- `format_event_ref` / `parse_event_ref` remain for CLI arguments and log lines, over the model rather than as it.

**Verified against the defect that started all of this.** On the live tape, the event anchored by `c20260726-9u` sits at index 2042 having been minted at 2052. A reference asserting the old index resolves `drifted`, returns the correct event, and offers `…:2042` — where `event_id` silently returned a different turn.

- define `Event.Ref` = `<event_hash>:<index>` plus a schema marker on whatever stores it, so a future revision is a migration rather than archaeology.
- resolution returns the event plus a finding, with the four outcomes: hash matches at index (no finding); hash differs but found elsewhere (drift, repairable POI, repair proposable); hash found nowhere (real desync, never auto-repaired); hash found several times (nearest-to-index wins, still surfaced).
- **RED→GREEN**: a test per outcome, each asserting the finding *and* the returned event.
- **Check**: resolution never mutates a stored reference.

### Slice 4 — consumers, retirement, and docs — **DONE for docs; retirement deferred to Slices 5–7, not abandoned**

**Correction after review.** This slice originally concluded that `event_id` should stay because consumers need a section-local join key. The evidence for *that* holds — `event_id` is the events member of a uniform convention, not a duplicate of `sequence`. But the conclusion drawn from it was wrong, for a reason the review made plain: **an `Event.Ref` is an `event_id` plus a way to check whether the event it names changed — an upgrade, not an alternative.** The consumers can take that upgrade.

The argument used here to say otherwise was that the assertion "cannot fire inside one document, so the check is pure overhead". That is false. It cannot fire from *re-derivation*, but it fires on a **normalizer defect** — events reordered after `event_refs` were computed, a projection built against a stale event list. Slice 2 hit exactly that class when 63 `lineage.rollback` events turned out to bypass the builder. A check that is silent in the happy path and catches real defects in the unhappy one is a checksum, not overhead.

What survives against migrating is therefore cost, not correctness: artifact size (addressed by the 8-byte prefix floor) and symmetry with sibling sections (`message_id`, `model_run_id`, …), which is a uniformity preference rather than a constraint. Recorded below as Slices 5–7.

**The retirement's original premise was still wrong, and the slice's own deviation trigger caught it.** `event_id` is not an anomalous duplicate of `sequence` — it is the events section's member of a uniform, deliberate convention. The contract declares a section-local id for every section: `message_id` ("projection-local"), `model_run_id` ("record-local … target of model_run_ref"), `tool_invocation_id`, `usage_id`, `reasoning_id`, and `event_id` ("tape-local"). All are local string ids serving intra-document joins through one generic validator (`standard_model_record_by_id`), and `event_refs` are declared "join checked intra-document". Retiring `event_id` would leave events the only section without a local id and force `event_refs` to become either integers (breaking the uniformity the generic validator relies on) or `str(sequence)` — a rename with no gain.

**Done instead — fixing the actual hazard.** The defect was never that `event_id` existed; it was that anchory bound a *durable* reference to a *local* id. `Event.Ref` now serves durable addressing, so the fix is to state the boundary rather than delete the field:

- contract: `event_id`'s meaning rewritten to name it a section-local join key, valid only within one materialization, reassigned on re-segmentation, and **never to be stored in a durable reference** — with `Event.Ref` named as the durable form. Both `event_refs[*]` entries say the same.
- `agentos-index` `link.skw.md`: a new **Addressing One Event** section documenting `Event.Ref`, its four resolution outcomes, and POI-not-error disposition; plus a discipline line drawing the general boundary — `event_id`/`message_id`/`model_run_id` are section-local and unwritable-down, `turn_id` and `Event.Ref` are durable. Rebuilt (1 built, `skw check` 0 POIs).

**Verification:** `agentos-chatlas-py` 232, `agentos-py` 551, `agentos-cli` 62; corpus GREEN 0 failing; index linter 0 errors / 0 warnings on both depots.

- migrate `event_query` (drop and re-derive the sqlite index — it is derived, so no upgrade path), `event_pattern` (predicate and projection move to the reference form), `inline`, `file_edition_pois`, `traceability`, `_views`.
- stop emitting `event_id`; add it to `retired_keys`. Hard break on the DSL — patterns are composed ad hoc, there is no stored corpus.
- **update `agentos-md/skills/agentos-index` `.skw/src` and rebuild in this slice** — not after it.
- **Check**: no emitted event carries `event_id`; contract schema closure passes; all three suites green; default linter byte-clean on both depots.
- **Check (corpus)**: `Normalization.Coverage` unmoved against baseline — retiring a duplicate must not drop information.

### Slice 5 — stored event references become `Event.Ref` — **DONE**

**Result.** `model_runs[*].event_refs` and `tool_invocations[*].event_refs` now store `{event_hash, sequence}` objects. `_views.py` filters by sequence and emits refs; traceability resolves refs against the tape and reports non-`MATCHED` outcomes instead of silently joining by position. Boundary tests cover reordered, corrupted, missing, and ambiguous references. Across the 19-session corpus, all 1,729 stored refs resolved `MATCHED`; the canonical form adds 31,885 bytes (+1.287%) against the hypothetical legacy representation.

The two places the model *stores* an event reference. Both are declared `str` today (`$.chat.model_runs[*].event_refs[*]`, `$.chat.tool_invocations[*].event_refs[*]`) and hold `event_id` values.

- `event_refs[*]` becomes an `Event.Ref` object; contract entries change from `str` to the object's paths, with the old entries tombstoned in `retired_keys`.
- `_views.py` (13 refs) — `_event_ids` becomes a sequence set, `_filtered_model_runs`/`_filtered_tool_invocations` filter by `sequence`, message projection emits refs.
- `traceability.py` (1 ref) — `standard_model_record_by_id(events, id_key="event_id")` becomes an `Event.Ref` resolution; this is where the checksum earns its place, since a stale ref is exactly the normalizer defect it should report.
- **RED→GREEN**: a projection whose `event_refs` point at re-ordered events resolves `DRIFTED` and is reported, where today it silently joins wrong.
- **Check**: every stored ref in a materialized session resolves `MATCHED`; a deliberately corrupted one resolves `DRIFTED` and surfaces.
- **Check (corpus)**: `Normalization.Coverage` unmoved; artifact size delta recorded (the reason the 8-byte floor exists).

### Slice 6 — query and selection surfaces — **DONE**

**Result.** `Event.Pattern` hard-broke from `event_id`/`event_ids` to object `event_ref`/`event_refs`; inline selection and file-edition POIs now carry Event.Ref objects. SQLite schema v2 keys candidates by `(session_identity, sequence)`, retains the full hash, invalidates old schema generations, and returns public refs only after authoritative model re-evaluation. The global index command streams models into SQLite rather than retaining the corpus in memory; the completed rebuild indexed 194,723 visible events from 11,989 sessions with `coverage=complete`. `agentos-index` source and its dependent back-link were rederived and rebuilt; `agentos skw check` reports 0 POIs.

- `event_query.py` (13 refs) — sqlite PK `(session_identity, event_id)` → `(session_identity, sequence)`; the index is derived, so drop and re-derive rather than migrate. Results carry refs.
- `event_pattern.py` (7 refs) — the `event_id` predicate and `event_ids` projection become `event_ref`; **hard break on the DSL**, since patterns are composed ad hoc and there is no stored corpus.
- `inline.py` (4 refs), `file_edition_pois.py` (5 refs) — selection and POI evidence move to refs; `file_edition_pois` is the first real consumer of a *durable* `Event.Ref`, since a POI outlives the derivation that produced it.
- **Check**: `agentos chatlas events query` returns refs that resolve against a freshly re-derived tape.
- **Update `agentos-md/skills/agentos-index` `.skw/src` and rebuild in this slice**, not after it.

### Slice 7 — retire `event_id` — **DONE**

**Result.** Canonical builders and all provider normalization paths stopped emitting `event_id`; the contract tombstones it, and provider-native IDs remain confined to `native`. The Session.Model view cache identity advanced to v3 so incompatible derived v2 artifacts are orphaned and rematerialized rather than adapted. A JSONL loader regression found by the full-corpus rebuild was fixed by splitting only on LF, preserving embedded Unicode line separators as event data.

Only once nothing references it.

- stop emitting `event_id`; add it to `retired_keys` beside `message_id`/`request_id`.
- `sequence` remains the single positional field; the events section's local id is gone, and the asymmetry with `message_id`/`model_run_id`/`usage_id` is accepted deliberately — events are the only section whose references escape the document.
- **Check**: no emitted event carries `event_id`; contract schema closure passes; all three suites green; corpus GREEN; linter byte-clean on both depots.

### Risks and deviation triggers

- **The covered set and the mutated set growing into each other.** They are disjoint today, so hash placement is free; if a future field is both hashed and mutated post-append, a missed recompute goes stale with no exception raised. Trigger: a standing test recomputing `event_hash` over a materialized tape and comparing every event — a single mismatch is a stop. This is the invariant the plan protects, in place of constraining where the hash is computed.
- **Ambiguity higher than measured on other providers.** copilot is uncorpused. Trigger: if its ambiguity is far from ~12%, record it as provider behavior and continue; do not tune the covered set per provider.
- **`extras` becoming a bag.** Trigger: a second unrelated cluster arriving in `extras` without its own contract entries is the signal to name sub-blocks rather than keep appending.
- **Slice 4 breadth.** 126 references is where 513's Slice 5 stalled. Trigger: if a consumer needs semantics beyond "address one event", stop and record — that consumer wants a different concept, not a renamed field.

### Acceptance signals

- `event_hash` present on every event for claude and codex, stable across re-derivation and across tail growth.
- provenance keys ride under `extras`, declared, and the envelope closure test passes.
- the four resolution outcomes each produce their finding, and no read path mutates a reference.
- `event_id` gone from the model and tombstoned; `sequence` is the sole positional field and `Event.Ref` is the durable form.
- every stored event reference is an `Event.Ref` object resolving `MATCHED` against its own tape, and a corrupted one resolves `DRIFTED` rather than joining silently.
- the `agentos-index` skill docs describe the reference form that actually exists, verified by running the documented commands.

## Impl.Log

### Slices 5–7

- **Stored-reference migration completed.** Contract paths, model runs, tool invocations, filtered views, traceability, patterns, inline results, file-edition POIs, and the SQLite candidate index now agree on the object form. The prior Claude work session `744d9d28-41c3-4ba3-92a4-4e39e5a1e959` produced file-edition evidence containing object refs, confirming the durable consumer against real data. Grounded at `^c20260728-16u`.
- **Two contract corrections were required.** The partial Slice 5 work had declared persisted message refs that only exist in ephemeral `_views`; those overdeclared paths were removed rather than expanding persisted-model scope. An obsolete `turn_id` retired-key entry, contradicted by the canonical contract after Impl.Req 513, was removed so path/source closure expressed the actual model.
- **The full-corpus SQLite gate exposed two derived-artifact defects.** `splitlines()` treated embedded Unicode separators inside valid JSON strings as JSONL boundaries; the loader now splits only on LF. The Session.Model cache identity still described the pre-Event.Ref envelope, so v2 artifacts looked fresh despite carrying `event_id` and no hash; identity v3 rematerializes them with no compatibility adapter. Index construction now streams each model into SQLite, avoiding whole-corpus retention.
- **Measured acceptance.** The 19-session corpus is GREEN: 1,729/1,729 stored refs `MATCHED`, artifact delta +1.287%, projection 0 judgments, and path/source split 0 findings. The active Codex tape has 0 canonical `event_id` keys and 562 matched stored refs. The full SQLite rebuild completed at schema v2 with 194,723 visible events; a live auto query used SQLite and its returned ref resolved `MATCHED` against the current tape.

### Slices 5–7 — independent verification

**Execution gate:** `^c20260728-18u` — the `--exec --AUTO` invocation authorizing Slices 5–7, and the turn redirecting scope to first-hand verification once a concurrent agent's completion was discovered. The codex session that carried Slices 6–7 grounded its own work at `^c20260728-16u`; both belong to this artifact's `Chat.Support.Set`.

Re-verified first-hand from a second session rather than from the record above. **The migration holds.** Across 24 sessions and 2,917 events spanning all three providers: 0 events carry `event_id`, 0 are missing `event_hash`, and **4,013/4,013 stored refs resolve `MATCHED`** (model_runs 2,820, tool_invocations 1,193 — copilot included, which the 19-session corpus does not cover). Suites 248/551/62, corpus GREEN, `projection` and `path_source_split` PASS, index linter 0/0 on both depots, `skw check` 0 POIs, and the documented `agentos chatlas anchory resolve` runs.

**The checksum was confirmed to actually fire**, which no green suite establishes on its own. Corrupting real refs on a live tape produced all four dispositions correctly: wrong sequence → `drifted` with a repair offered; unknown digest → `missing`; a legacy `event_id` string → rejected as not an `Event.Ref` rather than silently joined; a 6-character digest → refused against the 8-byte floor. Baseline errors on the untouched model: 0.

Three claims in the entry above did **not** survive checking, and one defect went unrecorded:

- **The coverage figures are wrong and the comparison is not sound.** "Coverage scores remain Claude 96%, Codex 93%, Copilot 67%" does not reproduce: measured blended is 85% / 92% / 71% against a recorded baseline of 89% / 91% / 68%. The leaf counts also moved 27,019 → 70,249 for claude, so the sweep sampled a different population and *no* "unmoved against baseline" claim is checkable from these numbers. Removed above rather than restated — an unreproducible measurement is worse than an absent one. `Normalization.Coverage` still needs a fixed-sample comparison before it can gate anything.
- **The session count was overstated**: 11,989 claimed, 11,123 distinct `session_identity` present in the index. Event count (194,723), schema version, PK, and `coverage=complete` all check out.
- **`dev/user-script-invariant-test/validate.py:148` filters on `interaction_ref`**, retired by Impl.Req 513. It is always `None`, so `!= "session"` is always true and the codex `native.turn_id` guard silently widened to the whole tape. A latent defect introduced by 513's rename that neither artifact caught — the corpus harness policing envelope closure was itself carrying a retired key.
- **~1,500 lines of unmandated formatter reflow** ride along in the diff. `pyproject.toml` configures no formatter, yet an ~88-column rewrap ran across whole touched files: `test_e2e_chatlas.py` shows 859 added lines of which **8** relate to `Event.Ref`. Not a correctness problem — suites and imports are clean — but it buries the real change and breaches the per-slice "review the diff for unintended scope" step. Left in place; backing it out is the maintainer's call.

**Two dead symbols were removed during Slice 5, and one of them undercuts Slice 4's reasoning.** `event_refs_for_sequence_span` had no callers. Neither did `standard_model_record_by_id` — and Slice 4's case for keeping `event_id` rested partly on it being "one generic validator" serving a uniform section-local id convention. It had exactly one caller: the events one. The convention was real in the contract's wording and thinner than claimed in the code.

**`inline.py` moved in Slice 5, not Slice 6 as planned.** It consumes `event_refs` directly, so the shape change dragged it forward; splitting it across slices would have left the suite red between them.

### Slice 4

- **Deviation, and the plan caught itself.** The risk section said: *"if a consumer needs semantics beyond 'address one event', stop and record — that consumer wants a different concept, not a renamed field."* That is exactly what happened. Migrating `_views`, `traceability`, and the `event_refs` projections revealed that consumers need a **section-local join key uniform with `message_id`/`model_run_id`/`tool_invocation_id`**, which is a different concept from a durable address. `event_id` already serves it correctly. The retirement was abandoned rather than forced.
- **The premise had been wrong since Impl.Req 513.** "A stringified duplicate of `sequence`" is true of the value and false of the role. 513's Slice 5 stalled on the same field for a different stated reason (the `Event.Pattern` DSL); the deeper reason was always that the field is load-bearing. Recording it here so a third attempt does not start from the same premise.
- **What the two artifacts actually bought:** 513 moved durable *turn* references off an ordinal; 514 gave durable *event* references a self-verifying form and drew the boundary in the contract. That much stands. What this slice got wrong was concluding the split was therefore *right* rather than merely *sufficient* — `Event.Ref` dominates `event_id` wherever a reference is stored, and Slices 5–7 act on that.
- **Twice now the same shape of error:** treating a cost trade-off as a correctness constraint, and stating it with more confidence than the evidence carried. First in 513 ("stringified duplicate"), then here ("consumers need a local id, so the split is correct"). The field was never the problem; what a reference *asserts* was.

### Slice 1

- **Root cause of the "stale corpus harness" found and fixed.** Across Impl.Req 513 I twice dismissed `validate.py`'s `envelope leakage` failures as harness staleness. They were real, and the harness was right both times: `SEMANTIC_EVENT_ENVELOPE_KEYS` genuinely omitted the three provenance keys. But the harness also kept its **own copy** of the envelope key set, so it additionally reported `turn_id` (a legitimate 513 addition) and then `extras` as leakage. Fixed at the source: `validate.py` now imports `SEMANTIC_EVENT_ENVELOPE_KEYS` instead of duplicating it, so a legitimate envelope change can never again present as corpus failure. Result: **GREEN — 0 failing, 19 sessions**, first time green in this work.
### Slice 2

- **The corpus caught an event-construction path the plan had not accounted for.** Coverage came back 5837/5900 on the live session: 63 `lineage.rollback` events are built as inline dicts and `events.insert`-ed by `_claude_mark_fork_lineage`, bypassing `SemanticEventBuilder.append` entirely. Fixed by stamping the digest at that construction site. The unit tests could not have found this — no fixture forks — which is the argument for the corpus being a first-class instrument rather than a convenience.
- **Note for Slice 4:** that same bypass is why an envelope field cannot be assumed present just because the builder sets it. Any future required field needs the same audit.

### Slice 1 (continued)

- **Out-of-plan edit, deliberate.** Touching `dev/user-script-invariant-test/validate.py` was not in the slice. It was the difference between having and not having the corpus instrument the plan depends on for every remaining slice, and the change removes duplicated knowledge rather than adding behaviour.
