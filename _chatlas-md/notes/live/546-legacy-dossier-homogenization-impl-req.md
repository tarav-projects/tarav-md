# Homogenize The Legacy Anchor Dossiers Into The Chatlas2 Model - impl-req

## Impl.Abstract

- **Status:** Open. Slice 1 done, slice 3 dissolved, slice 2 written. **Blocked on one decision — see `Anchor.Identity.Fork`.**
- **Intent:** Convert every referenced `chatlas` anchor dossier into the `chatlas2` model, so one grounding format remains and nothing needs the legacy resolver.
- **Source:** `527-chatlas2-normal-model-redesign-design-session.md` — *"Anchor records will be transformed operationally when Chatlas2 cuts over. Migration mechanics are written for the actual data at that moment, checked for completeness, and protected by the depot's Git history rather than maintained as a Chatlas2 subsystem."* This is that transformation.
- **Scope:** 2,364 referenced `^c` anchors carrying 4,432 joinable refs across 44 sessions, spanning four repos.
- **Out of scope:** deleting anything, the `chatlas1` consumer cutover (`545`), the tarav-pkg folder migration (`640`), and grounding anything not already grounded.
- **Grounding:** none minted. The index freeze (`638` Invariant 1) is in force.
- **Acceptance:** every referenced anchor exists in the `chatlas2` namespace; every ref that joins does so exactly; every ref that does not is a reported finding. The `chatlas` namespace is left intact.
- **Disposition (user, 2026-08-19):** *"we are migrating the system, not correcting the data."* The migration moves the format and engine. It does not aim at complete grounding, and a large POI queue afterwards is the system working — provided the right checks fire.

## Why This Exists

`545` originally planned to keep `chatlas/anchory.py` alive until `640` had read the legacy dossiers through it. That preserved two formats to serve one migration and made the retirement *order* load-bearing — the same coupling that stalled the previous merge.

Converting the data once removes the ordering problem instead of sequencing around it. Afterwards `640` reads one format, `545` Slice 5 becomes an ordinary deletion, and no compatibility resolver is ever written.

**The data is kept.** Migration writes the `chatlas2` namespace and leaves `chatlas` untouched; `anchory-backups/` is the existing precedent.

## Impl.Index

### Migration.Shape

- [DF] `Dossier.Homogenization` is the one-time conversion of legacy `chatlas` anchor dossiers into `chatlas2` records, preserving semantics rather than re-deriving them.
- [DC] The dossier envelope is already identical across namespaces — `attachment`, `relationships.support/gates/provenance`, `at` on every member. Only the member coordinates and `app`/`schema` differ, so this is a member-level rewrite, not a re-grounding.
- [CT] A ref that does not join exactly is reported, never snapped onto the nearest candidate.
- [PR] Because the join key is exact, the run is auditable ref by ref instead of trusted in bulk.
- [DC] Completeness is not an acceptance condition. An anchor migrates with the members that join; an incomplete gate is omitted so the linter raises `landing-evidenced` rather than the migration inventing evidence.
- [PR] A POI raised by migrated data is a working check, not migration debt. Suppressing it by loosening the join would convert a visible gap into an invisible falsehood.
- [RJ] No compatibility resolver and no maintained migration subsystem. The script runs, is checked, and is discarded; git history holds the before state.

### Join.Key

- [DF] `Legacy.Support.Join` maps a legacy `{session, turn_id, turn_hash, at}` ref onto a Chatlas2 coordinate by matching the session, the exact event `started_at`, and the resolved turn text.
- [EX] Text alone is ambiguous: on `^c20260712-21u` the member text `"approve"` matches three user messages in the same session.
- [EX] `at` disambiguates exactly — one candidate's `started_at` matched to the millisecond.
- [EX] Dry run over all 4,432 refs: **2,300 exact, 0 ambiguous, 0 partial.** Wherever the join could be attempted it was exact.

### Side.Asymmetry

- [EX] Every user-side ref joined: `support` 1,877/1,877 and `approval_turn` 423/423 exact.
- [EX] Every agent-side ref failed: `proposal_turn` **423/423** no-join. The failure is categorical, not data quality.
- [DC] The cause is structural: a legacy proposal ref addresses the agent turn's *first* event, and that event frequently belongs to no `Chat.Message` at all — `527` scopes `Chat.Message` to *"the primary user-agent message exchange, not everything the harness renders."*
- [EX] Probed on `c20260803-56u`: the event exists at exactly the legacy `at` with `origin: agent`, sits in **zero** `Chat.Message`, and in **exactly one** agent `Chat.Turn` carrying `turn_address` and `turn_hash`.
- [RJ] A migrated gate does **not** gain a `Chat.Turn` reference form. `541` settled the chatlas2 gate shape: *"Gate proposal and approval members are independently resolved messages: proposal is agent-side, approval is user-side."* Changing it to fit the legacy data would bend a current design to a retired one.
- [DC] Instead `Chat.Turn` is the **bridge, not the stored ref**: the legacy event resolves to its containing turn, and that turn's agent `message_ref` is what the migrated gate records. The dossier shape is unchanged.
- [EX] Verified on `c20260803-56u`: the containing agent turn carries exactly one `message_ref`, whose text is the legacy proposal text.
- [PR] `527` licenses the move in the other direction — *"a consumer may expand that message to its containing `Chat.Turn`"* — so turn/message expansion is an ordinary consumer operation, not a new concept invented for the migration.

### Migration.Discipline

Grounded on `521-stable-event-place-migration-impl-req.md`, the prior migration of 4,525 support members. Its rules are inherited rather than restated from scratch.

- [DC] *"Unresolved evidence is a migration failure requiring explicit repair, never relocation."* A ref that does not join is a reported finding, not a ref pointed somewhere plausible.
- [CT] `521`'s named stop-trigger applies verbatim here: *"silent purity repair: an invalid support member is moved to similar text. Stop and surface the evidence failure."*
- [DC] The `Chat.Turn` bridge is therefore keyed on **identity, not similarity**: the legacy ref names its own `turn_id`, the bridge resolves that same turn's agent message, and containment is exact. Text equality is asserted as a *check* on the result and never used to select among candidates.
- [CT] A bridged message whose text does not equal the legacy turn text is a failure, not a near-miss to accept.
- [DC] *"Migration success is proved by positive current-schema conformance and a zero-result legacy scan, not by the ability to read old data."* — `521`, `Migration.Current.Only`.
- [PR] `521` also settled the method this artifact uses: live-resolve every member against current models rather than translating stored coordinates.

### Anchor.Identity.Fork

**Unresolved. Not decided by anything found in the design surfaces, so it is not decided here.**

- [EX] An anchor id carries its namespace prefix: `c…` is the `chatlas` namespace, `d…` is `chatlas2`. `ensure_lossless_namespace` enforces the prefix, so a `c…` id cannot simply be written into the `chatlas2` namespace.
- [EX] `522-index-line-anchor-dossier-migration-impl-req.md` is the closest precedent and migrated **in place**: same anchor ids, same namespace, record schema replaced (`chatlas.support-set.v4–v6` → `chatlas.line-anchor-dossier.v1`). No anchor was reminted and no surface was rewritten.
- [EX] `541` slice 2 records that the runtime already *"composed mixed `c…`/`d…` support, review, line-manifest, approval, drift, and grounding readers"*, so mixed prefixes are an accommodated state rather than a defect.
- The two candidate readings:
  - **In place** — keep the 2,364 `c…` ids and the `chatlas` namespace, replace the record content with the Chatlas2 model. Zero surface edits across four repos. Requires the reader to accept a v2-shaped record under a `c…` anchor.
  - **Remint** — allocate `d…` anchors and rewrite all 2,364 citations in `tarav-md`, `tarav-chatlas-md`, `tarav-py`, and `notes/`. Prefix invariant stays exact; the edit is large and touches code surfaces.
- [PR] In place matches `522`'s precedent and the standing instruction that this migrates the system rather than the data. It is the recommendation, not the decision.

### Blocked.Sessions

- [EX] 9 of 44 sessions do not build in the Normal Model at all, carrying **1,709 refs (39%)**.
- [EX] The dominant cause is `Chatlas2 Codex artifact must contain exactly one native session scope` — a codex artifact holding several `session_meta` records, which chatlas1 reads and chatlas2 refuses. One claude-code session fails artifact recognition separately.
- [DC] This is a Chatlas2 normalizer gap the migration exposed, not a data defect: the sessions are intact and readable by the old model.
- [CT] Fixing `_session_scope` to derive scope positionally cannot move any existing `Event.Address`, because every affected session currently fails to build and therefore has no addresses in use.
- [DC] The migration cannot complete before this is fixed, so it is the first slice.

### Reach

- [EX] Referenced anchors: `tarav-md` 1,867, `tarav-chatlas-md` 423, `tarav-py` 172, `notes/` 13 — 2,364 distinct.
- [DC] `tarav-py`'s 172 are `Skw.Annotation` support on code surfaces, which `640` does not cover. This migration is therefore not a subset of `640`; `640` is a consumer of it.
- [EX] 1,305 of the store's 3,669 dossiers are referenced by nothing. They are neither migrated nor deleted.

## Execution.Plan

### Slice 1 — Teach the Codex normalizer multi-scope artifacts  *(done)*
`_session_scope` became `_session_scopes`: each record takes the scope of the `session_meta` in effect at its position, and records preceding the first take that first scope. An artifact carrying exactly one scope gives every record that scope, which is what holds existing addresses byte-identical.
**Result:** 8 of the 9 blocked sessions now build, recovering 1,635 refs. `new_model_unavailable` 1,709 → 74; the remaining session is one claude-code artifact-recognition failure, unrelated to scope.
**Checks passed:** two new tests — a resumed two-scope artifact normalizes with distinct addresses, and a single-scope artifact reproduces its exact prior addresses (that one passed *before* the change, which is what makes it a guard rather than a restatement). Full suite 2054 green, including the content-addressed conformance corpus, which is the real evidence no stored address moved.

### Slice 2 — The join, as a reusable read-only resolver
One function: legacy ref → `{status, coordinate}` where status is `EXACT`, `AMBIGUOUS`, `NO_JOIN`, or `SESSION_UNAVAILABLE`. User-side refs resolve to `Chat.Message`, agent-side to `Chat.Turn`.
It reads both models and writes nothing.
**Check:** re-run over all 4,432 refs and publish the status histogram. Target after slice 3: 4,358 EXACT with 74 SESSION_UNAVAILABLE named. Anything else is reported before slice 4 runs.

### Slice 3 — *(dissolved: no schema change)*
The original plan added a turn-reference form to the gate. `541` had already settled that both gate sides are messages, so the join bridges through `Chat.Turn` to the turn's agent message instead and the dossier schema is untouched.
Nothing to build. The bridge lives in slice 2's resolver.

### Slice 4 — Convert, in one auditable run
For each referenced anchor, build the `chatlas2` dossier from the legacy one: same `attachment.triplet_hash`, same provenance, joined support members, joined gates. Write to the `chatlas2` namespace under the anchor's existing id.
**Check:** every written dossier parses; support member count matches the legacy dossier exactly; **every bridged agent-side gate asserts text equality against the legacy turn text and fails on mismatch**; the run reports converted / skipped / failed and fails loudly rather than partially.

### Slice 5 — Verify against the source surfaces
For a sample across all four repos, resolve each anchor in both namespaces and assert the support text is identical.
**Check:** text equality on the sample; `tarav index linter` unchanged on `tarav-md`; the `chatlas` namespace byte-identical to before.

### Slice 6 — Hand the result to `640` and `545`
Record in both that one format now stands.
**Check:** `640` Slice 1 reads `chatlas2` dossiers only; `545` Slice 5 is unblocked.

## Slice Status

| # | Slice | Status |
|---|---|---|
| 1 | Codex multi-scope artifacts | **done** |
| 2 | the join resolver | **written**, unrun |
| 3 | turn-ref gate proposal side | **dissolved** — no schema change |
| 4 | the conversion run | blocked on `Anchor.Identity.Fork` |
| 5 | verify against source surfaces | not started |
| 6 | unblock `640` and `545` | not started |

## Impl.Log

- **Dry run, 2026-08-19, before slice 1.** 2,364 anchors / 4,432 refs / 44 sessions: `exact:support` 1,877, `exact:approval_turn` 423, `no_join:proposal_turn` 423, `new_model_unavailable` 1,709. Zero ambiguous, zero partial.
- **After slice 1.** `exact:support` 2,526, `exact:approval_turn` 916, `no_join:proposal_turn` 916, `new_model_unavailable` 74. Still zero ambiguous and zero partial across 3,442 joins.
- The agent-side failure scaled to exactly 100% again on 493 newly-readable refs. A structural diagnosis that survives a doubling of the sample is worth more than one that fit the first sample; slice 3's `Chat.Turn` design is confirmed at scale rather than assumed from one probe.
- The perfect complementarity — user-side 100% exact, agent-side 100% failed — is what identified the cause as structural rather than data quality. A mixed result would have looked like noise and been "fixed" by loosening the join.
- **Deviation from `545`.** `545` framed this as a sequencing constraint (keep the old resolver until `640` reads through it). The user rejected that in favor of migrating the data. `545`'s `Dossier.Homogenization` block records the change; this artifact is its execution.
- **`Index.Presumption`:** slice 1 is assumed safe for existing addresses because affected sessions do not currently build. Verified by reasoning, not yet by running the conformance corpus against the change.
- **Deviation — slice 3 dissolved.** The artifact as written proposed extending the chatlas2 gate with a turn-reference form. `541` had already decided the opposite, and the user's prompt to check the last ref discussions is what caught it before any code was written. The correct reading: the legacy data needs a better *join*, not a changed *schema*. A design that requires the current model to grow a shape is worth re-reading the design notes over.
- **Bridged dry run.** With the `Chat.Turn` bridge: `exact:support` 2,526, `exact:approval_turn` 916, `exact:proposal_turn` 386, `ambiguous:proposal_turn` 490, `no_join:proposal_turn` 40, `new_model_unavailable` 74. The probe did not apply text equality after bridging; `dev/live/546-migrate-legacy-dossiers.py` does, so its ambiguous count should be materially lower.
- **`Index.Presumption`:** the 1,305 unreferenced dossiers are assumed to be genuinely orphaned rather than referenced by a surface the scan missed. The scan covered `*.md` and `*.py` across the project excluding `.skw/`, `_DEPRECATED`, and `.git`.
- **Waiver:** no anchors minted and no backpropagation attempted, per the index freeze.
