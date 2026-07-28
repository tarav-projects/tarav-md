# 513 — Normal.Turn Identity + Anchory v2 — Impl.Req

## Impl.Abstract

**Scope.** Give `Chatlas.Session.Model` a stable, provider-general turn identity (`Normal.Turn`), make user-turn grouping faithful to actual user authorship, re-key `Chatlas.Anchory` records onto that identity, migrate the existing anchor corpus, and repoint the index linter's turn resolution.

**Why.** Anchory members identify turns by `event_id`, which is a tape ordinal (`"event-" + sequence`). Re-materializing an open session re-segments the tape and reassigns ordinals, so landed anchors silently come to point at other turns. Observed: 31 `Anchor.Turn.Missing` linter errors across 4 anchors; root cause traced to positional reassignment with timestamps stable.

**Status.** Designed, not started.

**Source context.** Design session captured into `agentos-chatlas-pkg/design/100-design.md`: new blocks `Event.Grouping` and `Normal.Turn`; amended `Session.Event.Tape`, `Chatlas.Anchory`, `Chatlas.Session.Model`.

**Out of scope.**
- copilot-cli normalizer parity (open extension per `Chatlas.Session.Model.Tests`); design must not block on it.
- a separate request/response-cycle grouping — `interaction_ref` is *renamed* to `turn_id` and kept as the turn grouping here; a distinct cycle grouping is a later concept if wanted.
- retiring `Chat.Support.Set` member semantics (still user turns, still ordered, still relevance-sorted).
- the deferred grounding of the five design lines landed this session (blocked on Slice 3; see Impl.Log).

## Impl.Index

### Current.State

- **the turn grouping already exists.** Both normalizers compute `interaction_ref`, and the contract already declares its meaning as *"neutral reference to the user interaction (turn) the event belongs to"* (`agentos-chatlas-py/references/normal-model.contract.json`). It is positional (`interaction-N`), not identity — and misnamed for what it is.
- **the corpus is ready as a test set.** `agentos-chatlas-py/dev/user-script-invariant-test/` holds the `User.Script.Invariant` scripts, 11 accepted provider sessions joined by `identity_hash` (`primes-utility`: 4 codex + 7 claude), the engines (`validate.py`, `projection.py`, `path_source_split.py`, `coverage.py`, `comparative_projection.py`), and the verdict memory (`path-verdicts.md`, `divergence-notes.md`, `coverage-baseline.md`).
- **the boundary rules already differ per provider.** claude: `_claude_record_starts_interaction` in `normalization/session_model/_claude.py:889` — a visible user message that is not tool evidence. codex: `interaction_refs_by_turn_id` in `normalization/session_model/_codex.py:1160` — inherits native `turn_id` wholesale.
- **native handles are populated and survive materialization.** On the `primes-utility` corpus: codex carries `native.turn_id` on 100/101 events; claude carries `native.parent_uuid` (75), `native.message_id` (37), `native.request_id` (37).
- **`event_id` is a stringified duplicate of `sequence`.** `normalization/session_model/events.py:210` emits `f"event-{sequence}"` beside `sequence`; the contract entry says so outright (*"tape-local event identifier, equal to 'event-<sequence>'"*).
- **the contract already tombstones sibling keys.** `retired_keys` holds `$.chat.events[*].message_id` and `$.chat.events[*].request_id` as *"loose provider id at envelope level — converged into native.*"* — precedent for the `event_id` retirement.
- **126 `event_id` references across 15 files**; producers are the 6 normalizer files, consumers are `anchory.py`, `event_query.py`, `event_pattern.py`, `inline.py`, `index_checks.py`, `file_edition_pois.py`, `traceability.py`, `_views.py`, plus `agentos-py/src/agentos/skillware/edition_history.py`.

### Hard.Evidence

- **Cross-provider convergence already holds for clean runs.** On the `User.Script.Invariant` `primes-utility` script, claude and codex both yield exactly the 7 canonical user turns, verbatim-identical, each in its own `interaction_ref` (1–7), with injected AGENTS.md / `environment_context` content excluded from user message events on both sides. The grouping semantic is therefore reachable generally; what is missing is a stable *name* for it.
- **Codex over-merges at the raw level.** In `rollout-…-019f133f-….jsonl`, 8 user records carry only 7 distinct `turn_id`s: the injected instructions record and the first real prompt share one `turn_id`. Inheriting native grouping unrefined is therefore unsafe as a general rule, even though this particular case is already handled downstream.
- **Claude over-splits and mislabels.** A slash-command invocation produces three `role=user` message events at one timestamp, each with its own `interaction_ref` (62/63/64), and `producer.type` is assigned wrongly: the record holding the user's typed arguments is `{name: command, type: system}` while the injected skill body is `{type: human}`. This is an `Unjustified/lossy` normalizer defect in the `Faithfulness.Verdict` sense.
- **Anchor corpus audit (397 members / 394 anchors / 22 sessions).** Before repair: 391 resolved correctly, 5 drifted but uniquely recoverable by `at`+role, 1 ambiguous. All 6 defects belonged to a single still-open session; every closed session's anchors were intact. After the repair pass: 397/397 resolve to their stored user turn.
- **Only 3 of 397 members carry `types` cargo** — the approval-turn machinery is young, so the v2 format change lands cheaply.

### Design.Decisions

- `Normal.Turn` is not a new field: it is `interaction_ref` renamed to `turn_id` and given a stable identity plus an enforced purity rule. The contract already claims turn semantics for it; this work makes the claim true.
- canonical `$.chat.events[*].turn_id` deliberately shares a name with source-native `$.chat.events[*].native.turn_id` (codex). The contract entry must state explicitly that the canonical field is the model's own identity — seeded from native handles, never equal to one by contract — or a reader will take it for a provider passthrough, the very failure `retired_keys` records for envelope-level `message_id`.
- the `User.Script.Invariant` corpus is the primary test instrument, not a convenience. It is the only surface holding the *same* user script across providers, so it is the only thing that can distinguish "the mechanism is general" from "it happens to work on claude". Every slice that touches normalization asserts against it.
- Turn identity is sourced by a general rule, not a shared value. Each `Raw.Normalizer` maps its native handle onto the model's semantic (codex `turn_id`; claude message/parent uuid). Cross-provider identity *equality* is explicitly not a goal — only generality of the mechanism.
- A native grouping that over-merges is refined, never inherited. A provider offering no handle gets a synthesized identity; synthesis is the fallback, not the primary path.
- `producer.type` is the purity classifier for user turns. A user turn admits only human-produced content; command wrappers, system reminders, and injected skill bodies are excluded. Fixing the misassignment is in scope because purity depends on it.
- `event_id` is retired to a contract tombstone; `sequence` remains the sole positional field. Retirement lands *after* migration, since the migration pass reads v1 records keyed on `event_id`.
- Migration is a re-key, not an amend of meaning: each v1 member resolves once against its materialization and is rewritten to that turn's identity, preserving the anchor's hint and cargo.
- The linter is repointed rather than relaxed. The 31 errors were the check working correctly; the fix is a stable key, not a weaker assertion.

### Impl.Agendix

**index → touched** (blocks this implementation must honor, `agentos-chatlas-pkg/design/100-design.md`):

- `Event.Grouping` — tape is SSOT; a grouping is a tag, never a container; groupings are open and orthogonal; partial by nature; a stability contract binds only a grounded grouping.
- `Normal.Turn` — chat-semantic grouping; boundary per turn kind; user-turn purity; identity carries the stability contract; normalizers map native handles; identity not interpretation.
- `Session.Event.Tape` — `sequence` is the only positional field; `event_id` retired; durable references key on a grouping with a stability contract.
- `Chatlas.Anchory` — record format `chatlas.support-set.v2`, members keyed on `Normal.Turn` identity.
- `Chatlas.Session.Model` — the model carries chat data, never a consumer's interpretation.
- `Chatlas.Session.Model.Tests`, `Normalization.Pipeline::Chatlas.Session.Model` — the corpus engines and their three-way triage.
- `agentos-pkg` `Normalization.Pipeline-appendix`: `Under.Normalization`, `Model.Fragment` (topological, not positional), `Normal.Model.Contract`, `Projection.Test`.

**chat → touched**: deliberately empty. Minting anchors now would register v1 records keyed on `event_id` against a still-open session — manufacturing exactly the drift this artifact retires. Chat grounding for this work is deferred to after Slice 3 and recorded in `Impl.Log`.

## Execution.Plan

### Slice 1 — user-turn purity

Make `producer` classification faithful, so "which event is the user" has a trustworthy answer before anything keys on it.

- correct the claude marker table so command wrappers and system reminders classify `producer.type: system`, and the record carrying the user's typed content classifies `human`.
- assert the rule generally: a user turn admits only human-produced content.
- **RED→GREEN**: a test over the known slash-command triple asserts exactly one human-produced user event; RED against current classification.
- **Check (corpus)**: `validate.py`'s acceptance filter still passes on all 11 accepted sessions — user turns stay verbatim-identical and in order. A purity change that breaks the acceptance filter is a normalization error by construction, so the corpus is the guard against over-filtering.
- **Check**: on `primes-utility`, user-turn counts equal the script's 7 on both providers; the triple collapses to one human turn.
- **Observable**: `agentos chatlas views inline --filter turns` no longer surfaces injected records as user turns.

### Slice 2 — turn_id: rename and stable identity

- rename `interaction_ref` to `turn_id` across model, contract, and consumers; tombstone the old key.
- give it a stable value: the contract entry declares it the model's own turn identity — seeded from native handles, never contractually equal to one — with its null policy for non-turn-bearing events.
- populate it in both normalizers from their native handles (codex `native.turn_id`, claude message/parent uuid), refining any native grouping that over-merges; synthesize where no handle exists.
- **Check**: re-materialize a session at two different tail states; every `turn_id` is unchanged (the direct regression test for the original defect).
- **Check (corpus)**: `Projection.Test` over `primes-utility` — the path resolves for all turn-bearing events on claude *and* codex, absences justified; `Path.Source.Split.Test` shows no source split on it, which is the mechanical proof the mechanism is general rather than provider-shaped.
- **Observable**: `turn_id` present and stable in `session-model.json`.

### Slice 3 — anchory chatlas.support-set.v2

- member key becomes `<session>:<turn-identity>`; `at` retained for readability and integrity checking.
- update register / resolve / amend and the `--member` CLI surface; `types` cargo (`verbatim_turn`, `approval_turn`) moves to turn refs.
- **RED→GREEN**: registering an ordinal-keyed member is rejected; resolving a v2 record returns the intended turn.
- **Check**: a v2 anchor minted against an open session still resolves after further session growth.

### Slice 4 — corpus migration

- one offline pass over all 394 anchors / 397 members: resolve each v1 member against its materialization, write the v2 turn identity, preserve hint, order, and `types`.
- re-audit `c20260726-6u` under the Slice 1 classifier — it is the one member whose correct target the v1 format could not express (currently re-keyed provisionally to the record holding the user's typed args).
- **Check**: 397/397 resolve post-migration; a forced re-materialization changes no resolution.
- **Observable**: no `chatlas.support-set.v1` record remains in the depot.

### Slice 5 — event_id retirement

- stop emitting `event_id`; add it to `retired_keys` beside the existing `message_id` / `request_id` tombstones.
- migrate the consumer surfaces (`event_query`, `event_pattern`, `inline`, `file_edition_pois`, `traceability`, `_views`, `edition_history`) onto `sequence` for order and turn identity for reference.
- **Check**: contract schema-closure passes; no emitted event carries `event_id`; full suite green.
- **Check (corpus)**: `coverage.py` against `coverage-baseline.md` — retiring a duplicate key must not move `Normalization.Coverage`; a drop means real information was dropped with it.

### Slice 6 — linter turn resolution

- repoint `index_checks.py` (grounding provenance, `Line.Approval`, `Line.Verbatim.Gate`) at v2 turn identity.
- **Check**: default linter run over `agentos-pkg` and `agentos-chatlas-pkg` is byte-clean; the `Anchor.Turn.Missing` class cannot be produced by re-materialization alone.

### Slice 7 — end test: the system grounds its own design

The closing proof, and the two cases the artifact left open. Both are end-to-end exercises of everything above, not cleanup.

- **ground the five design lines landed this session** — `Event.Grouping`, `Normal.Turn`, and the amendments to `Session.Event.Tape`, `Chatlas.Anchory`, `Chatlas.Session.Model` — by minting v2 anchors against this session's approval turns and tagging the lines. This is the full loop: a live, still-growing session, a tokenized approval turn, a v2 record, a passing `Line.Verbatim.Gate`.
- **resolve `c20260726-6u`** under the Slice 1 classifier and confirm its member. It is the one case in the 397 that v1 structurally could not express, so a correct answer here is the evidence that v2 expresses what v1 could not.
- **Check**: the five lines resolve through `agentos chatlas views inline --anchor <anchor> --filter turns` to their actual approval turns.
- **Check**: re-run the full 397-member audit after the session has grown further; still 397/397, including the anchors minted in this slice.
- **Acceptance**: an anchor minted during an open session survives that session continuing — the exact thing that was impossible when this work started.

### Risks and deviation triggers

- **Live-session churn.** Migration reads materializations that may re-segment mid-pass. Trigger: run migration against sessions quiesced, and re-audit after.
- **Purity regressions elsewhere.** Slice 1 changes what counts as a user turn, which can move existing anchors' targets. Trigger: if the post-Slice-1 audit shows any of the 397 members no longer resolving to a human turn, stop and reconcile before Slice 3.
- **copilot-cli.** Not covered by the corpus. Trigger: if its normalizer has no usable handle, take the synthesized path and record it, do not block.
- **`types` cargo.** Only 3 members carry it; if that grows before Slice 4, extend the migration rather than hand-fixing.

### Acceptance signals

- turn identities stable across re-materialization of an open session (Slice 2 check is the direct answer to the originating defect).
- 397/397 anchors resolve after migration, and continue to resolve after a forced re-materialization.
- default linter output byte-clean; the drift error class is structurally unreachable.
- `primes-utility` corpus: 7 user turns per session on both providers, no injected record among them; `Path.Source.Split.Test` reports no source split on `turn_id`.
- **end test (Slice 7)**: the five design lines this work was designed from are themselves grounded through v2 anchors minted in a live session, and those anchors still resolve after the session grows.

## Impl.Log

- **Deferred grounding.** Five design lines landed this session (`Event.Grouping`, `Normal.Turn`, plus amendments to `Session.Event.Tape`, `Chatlas.Anchory`, `Chatlas.Session.Model`) carry no `Chat.Support.Set`. Minting under v1 against a live session would have created the defect the artifact retires. Promoted to Slice 7: grounding them is the end test, not cleanup.
- **Provisional anchor.** `c20260726-6u` was re-keyed to the event holding the user's typed command arguments, which conflicts with the current `producer.type: human` label on a sibling injected record. Slice 1 decides it, Slice 4 migrates it, Slice 7 confirms it — it is the corpus's one v1-inexpressible member and therefore part of the end test.
- **Pre-existing repair.** The 6 drifted members were amended before this artifact was written, bringing the corpus to a uniform 397/397. That repair is a snapshot under v1, not a fix — it holds only until the next re-segmentation.
