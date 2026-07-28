# 514 — Stable Event Addressing — Impl.Req

## Impl.Abstract

**Scope.** Give `Chatlas.Session.Model` a canonical `event_hash`, define the `<hash>:<idx>` reference form consumers store to address one event, move `Delta.Normalization` bookkeeping into a declared `extras` namespace, and retire `event_id`.

**Why.** Impl.Req 513 gave *turns* a stable identity and re-keyed every durable reference onto it. Sub-turn addressing was left unsolved: `event_id` is still `"event-" + sequence`, and `Event.Pattern`, `inline`, and `file_edition_pois` genuinely need to address one event, not a whole turn. 513's Slice 5 attempted a straight retirement and was blocked — removing the field breaks an agent-facing DSL with nothing to replace it. This artifact supplies the replacement first.

**Status.** Designed, not started. Supersedes 513's blocked Slice 5.

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

- A reference is a **minimal assertion**, not an identity: `<hash>:<idx>` claims "the event with this hash was at this index". Neither half is stable alone; together they are self-verifying. The index disambiguates what the hash cannot, and the hash validates what the index cannot.
- **The event carries the hash; nothing carries the index.** `event_hash` is a canonical field so consumers never recompute semantics — only chatlas does, which keeps the derivation pinned in one place. The index is computable from the tape and is never stored on an event.
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

### Slice 1 — `extras` region, and close the envelope

- add `extras` to `SEMANTIC_EVENT_ENVELOPE_KEYS`; move `source_hash`, `chain_hash`, `final` under it.
- declare the region in `Chatlas.Session.Model.Contract` by full path, with a null policy ("present where `Delta.Normalization` applies") and an explicit exclusion from projection semantics.
- **RED→GREEN**: a closure test asserting no claude event carries an undeclared top-level key — RED today, since the three provenance keys are leakage right now.
- **Check (corpus)**: `Path.Source.Split.Test` no longer queues the provenance paths as source-split candidates; `Normalization.Coverage` does not count them as chat expressiveness.
- **Observable**: `agentos chatlas update --trust rebuild` produces tapes whose provenance rides under `extras`.

### Slice 2 — `event_hash`

- add the canonical field, populated by all three normalizers, reusing `_canonical_json`.
- contract entry: meaning, `null: never`, and the covered field set stated explicitly — the set *is* the contract, since consumers depend on reproducibility.
- **Check**: re-derive a session twice; every `event_hash` identical. Re-derive after appending to the tail; frozen-prefix hashes unchanged.
- **Check (corpus)**: present on 100% of events for claude *and* codex — the generality bar 513 set. `Path.Source.Split.Test` shows no source split.
- **Check**: measured ambiguity stays near the recorded baseline (~12% live, 0% codex) — a large move means the covered set changed meaning.

### Slice 3 — the reference form

- define `Event.Ref` = `<event_hash>:<index>` plus a schema marker on whatever stores it, so a future revision is a migration rather than archaeology.
- resolution returns the event plus a finding, with the four outcomes: hash matches at index (no finding); hash differs but found elsewhere (drift, repairable POI, repair proposable); hash found nowhere (real desync, never auto-repaired); hash found several times (nearest-to-index wins, still surfaced).
- **RED→GREEN**: a test per outcome, each asserting the finding *and* the returned event.
- **Check**: resolution never mutates a stored reference.

### Slice 4 — consumers, retirement, and docs

- migrate `event_query` (drop and re-derive the sqlite index — it is derived, so no upgrade path), `event_pattern` (predicate and projection move to the reference form), `inline`, `file_edition_pois`, `traceability`, `_views`.
- stop emitting `event_id`; add it to `retired_keys`. Hard break on the DSL — patterns are composed ad hoc, there is no stored corpus.
- **update `agentos-md/skills/agentos-index` `.skw/src` and rebuild in this slice** — not after it.
- **Check**: no emitted event carries `event_id`; contract schema closure passes; all three suites green; default linter byte-clean on both depots.
- **Check (corpus)**: `Normalization.Coverage` unmoved against baseline — retiring a duplicate must not drop information.

### Risks and deviation triggers

- **The covered set and the mutated set growing into each other.** They are disjoint today, so hash placement is free; if a future field is both hashed and mutated post-append, a missed recompute goes stale with no exception raised. Trigger: a standing test recomputing `event_hash` over a materialized tape and comparing every event — a single mismatch is a stop. This is the invariant the plan protects, in place of constraining where the hash is computed.
- **Ambiguity higher than measured on other providers.** copilot is uncorpused. Trigger: if its ambiguity is far from ~12%, record it as provider behavior and continue; do not tune the covered set per provider.
- **`extras` becoming a bag.** Trigger: a second unrelated cluster arriving in `extras` without its own contract entries is the signal to name sub-blocks rather than keep appending.
- **Slice 4 breadth.** 126 references is where 513's Slice 5 stalled. Trigger: if a consumer needs semantics beyond "address one event", stop and record — that consumer wants a different concept, not a renamed field.

### Acceptance signals

- `event_hash` present on every event for claude and codex, stable across re-derivation and across tail growth.
- provenance keys ride under `extras`, declared, and the envelope closure test passes.
- the four resolution outcomes each produce their finding, and no read path mutates a reference.
- `event_id` gone from the model and tombstoned; suites green; linter byte-clean.
- the `agentos-index` skill docs describe the reference form that actually exists, verified by running the documented commands.

## Impl.Log

- (empty — not yet executed)
