# Tarav2 Line.Trace And Review - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. Linter clean on the migrated depot; 126 tests green; `ruff` clean.
- **Scope:** Port the trace, review, standing, and link designs into tarav2: `label` as the line's public id, `LineScope`, `Line.Trace` with a derived `Trace.HEAD`, index HEAD/TAIL derived from `supersedes` over traces, typed links, trace-level review carried by chat evidence, and the equivalence claim as the one recorded non-checkable assertion.
- **Governing principle:** **Never an agent-set flag.** Every standing is either derived from structure or evidenced in an immutable surface, so defects are detectable.
- **Targets:** `tarav2/tarav2-py/src/tarav2/`, its tests, and the seeded depot.
- **Out of scope:** Shipping `Touched.Data`; Chat.Index materialization mechanics beyond the placement link.
- **Acceptance:** No boolean an agent can set decides anything. `Trace.HEAD`, index standing, and review standing are all computed. The linter detects a same-trace claim whose support changed, a rename claim that is not a rename, and a trace that dropped its review evidence.

## Impl.Index

### No.Agent.Flags

- [CT] the system never accepts an agent-set flag; it demands evidence or assertable structures so defects can be detected.
- [DC] `Trace.HEAD`, index HEAD/TAIL, and review standing are all derived rather than stored.
- [DC] the one thing an agent asserts directly is semantic equivalence within a trace, and it is recorded as a typed claim precisely because it cannot be checked.

### Line.Label

- [DF] the label is the line's public id, uniquely labelling it for readers of the index.
- [CT] the label is not the id; the id is internal to the index, and the label may change while the id does not.
- [DC] the label belongs under `line`, because the surface representation a reader consumes is `type + body + label`.

### Line.Scope

- [DF] `LineScope` is the context a line is evaluated in; a line is an orthogonal part of something larger, and only means something inside its scope.
- [DC] because evaluation requires it, an unresolvable scope puts a line below the bar alongside untyped and ungrounded.

### Line.Trace

- [DF] `line.id` points at a particular indexed line; `trace.id` points at a particular indexed semantic.
- [DC] lines carrying the same semantics are grouped into one trace; a new version is a new line with a new label and body under the same `trace.id`.
- [DF] `Trace.HEAD` is the current version of the line inside its trace, and is distinct from the index HEAD/TAIL axis.
- [DC] `Trace.HEAD` is derived from the trace's predecessor chain, not stored.

### Index.Standing

- [CT] a well-grounded line need not state something true or correct; grounding is immutable, so a grounded line stays well grounded forever.
- [DC] lines are retained because the goal is to index the Touched.Surfaces, not to maintain a set of currently-true statements.
- [DF] index HEAD/TAIL distinguishes lines still valid for the design from lines that are old design; both are well grounded.
- [DC] index standing is a relationship between lines of different traces, and is derived from `supersedes` pointing at a trace.
- [DC] `supersedes` names a trace rather than a line, so supersession survives rewording of the superseded claim.
- [DC] a project index surface materializes only lines that are both `Trace.HEAD` and index HEAD.
- [DC] TAIL lines live on Chat.Indexes and keep their record; removal remains reserved for bad indexing.

### Line.Links

- [DF] an index line carries several link kinds, of which grounding is only one.
- [DC] `grounding` reaches qualifying user turns and carries authority; `placement` reaches the Chat.Index attachment turn and carries location only; `review` reaches the review turn evidence; `supersedes` reaches a trace.
- [DC] placement is the oldest turn containing the line verbatim, agent or user, and falls back to the oldest supporting user turn.
- [DC] placement is stored at landing rather than recomputed, so rewording does not move a line's chat attachment.

### Trace.Review

- [DC] review is detected mechanically: the line claims a review turn, the turn carries the token, an agent turn carries the same token, and that turn contains the verbatim line.
- [DF] the mechanism evidences wording; by proxy the user is taken to have reviewed the line's semantics, and therefore its trace.
- [DC] review is a property of the trace, so every member is semantically reviewed regardless of when it joined.
- [CT] a trace can never drop its reviewed member, because that member is the review's only verifiable evidence.
- [DC] a member with its own review link is reviewed directly; a member inheriting through its trace is reviewed via trace, and the distinction stays visible.

### Index.Convergence

- [CT] the index is a `WIP.Surface`: its bytes are not immutable, and lines may be reworded, retyped, rescoped, relabelled, or deleted.
- [DF] what the design requires is that the index **converges to what is in the Touched.Data**, so grounded coverage only grows.
- [CT] grounding confers protection: an ungrounded line indexes nothing yet and may be eliminated, while a well-formed, typed, grounded line must not be removed.
- [CT] deleting an ungrounded line is a *capability*, not an automatic mechanism; an ungrounded line surfaces a POI, resolved case by case.
- [DC] amending a line to improve index quality is always available.
- [DC] a grounded line whose support never supported the claim may be removed, and that mis-grounding is recorded as an explicit assertion.
- [DC] a POI prescribes no remedy, so every check documents a set of legitimate resolutions rather than a fix.

### Equivalence.Claim

- [DF] joining a trace asserts that the change preserved semantics, and that assertion is recorded rather than implied by writing a trace id.
- [DC] a `rename` claim is mechanically verifiable by token substitution; a `rephrase` claim is agent judgment.
- [DC] a same-trace change that alters the support set is suspect, because a new claim would have needed new evidence.

## Impl.Log

- Index.Presumption: `Trace.HEAD` is derived from an explicit `predecessor` on each non-initial member, which makes the chain checkable for forks and cycles. A stored head flag was rejected under `No.Agent.Flags`.
- Index.Presumption: review-turn verbatim verification degrades to `unverifiable` when the archive is absent, rather than failing the review.
- Deferred: whether a trace can lose reviewed standing (demote vs. split). Split is the expected answer, but nothing depends on it yet.

## Execution.Plan

### Slice 1 — Naming and label
`Scope` → `LineScope`; `config.Scopes` → `Geography`; `anchor` → `line.label`.
**Check:** record round-trips with the label under `line`; no name collision remains.

### Slice 2 — Trace and derived Trace.HEAD
`trace` id, `predecessor`, derived head, chain validation.
**Check:** a two-member trace derives one head; a fork and a cycle are both detected.

### Slice 3 — Links
Typed link set: grounding, placement, review, supersedes, occurrences.
**Check:** each link round-trips; placement accepts an agent turn; grounding does not.

### Slice 4 — Index standing derived from supersedes
Standing computed over traces.
**Check:** superseding a trace demotes every member; rewording the superseded claim keeps it demoted.

### Slice 5 — Trace review with evidence
Review link, direct vs. via-trace, retention of the reviewed member.
**Check:** review propagates across the trace; dropping the reviewed member is a POI.

### Slice 6 — Equivalence claim and its guards
Typed claim; rename verification; support-invariance check.
**Check:** a rename that is not a rename is detected; a same-trace change with new support is flagged.

### Slice 7 — Linter and migration
Promote scope to the bar; add the new checks; migrate the seeded entries.
**Check:** catalog reflects the model; depot clean.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | Naming and label | done | `LineScope`, `Geography`, `line.label`; renders as `type + body + label` |
| 2 | Trace and derived Trace.HEAD | done | head derived from the chain; fork and cycle both detected |
| 3 | Links | done | grounding / placement / review / supersedes / occurrences round-trip |
| 4 | Index standing from supersedes | done | superseding a trace demotes every member, survives rewording |
| 5 | Trace review with evidence | done | direct vs. via-trace; review members identified for retention |
| 6 | Equivalence claim and guards | done | rename verification, support-invariance, predecessor checks |
| 7 | Linter and migration | done | 26 checks; scope on the bar; 21 entries migrated |

## Verification

The review economy, end to end on the live index:

```text
review recorded on ln_0b4a15…                     evidence, not a flag
tarav2 index revise <id> --kind rename            new line, same trace
tarav2 index trace tr_9f71…
  ln_0b4a15…  ^d20260818-6u    direct
  ln_61d659…  ^d20260818-21u   via_trace  HEAD
```

The rename cost no re-review, and the predecessor is retained as the review's only verifiable
evidence.

The guards fire on real defects. With a hand-written review link whose evidence did not hold:

```text
Index.Linter/Review.NotVerbatim          the reviewed line is not verbatim in its agent turn
Index.Linter/Materialization.Standing    superseded wording is on a project surface
Index.Linter/Record.Unplaced             the new Trace.HEAD is materialized nowhere
```

**The fabricated review was caught.** That is the `No.Agent.Flags` principle working: review is
evidence checked against an immutable chat, not a boolean anyone can set.

```text
tarav2 index linter    clean — 21 record(s), 21 surface line(s), 26 check(s)
pytest                 116 passed
ruff check src/ tests/ All checks passed
```

## Defect Found During Execution

`IndexStore.put` still keyed its target root on `record.review` after that field became the
`ReviewRef` link, writing entries into `index/None/` where nothing read them. Surfaced by
verifying a revise round-trip rather than by a test — the successor reported written and was
not on disk. Fixed to key on `review_index`.


## Convergence Addendum

Three further changes, after the WIP-surface discussion sharpened what is actually conserved.

**`IndexStore.remove` now enforces the protection boundary.** Removing an ungrounded entry is
free — it indexes nothing yet. Removing a grounded one is refused unless given a recorded
`mis_grounding` reason, which is appended to `.tarav2/removals.jsonl` with the lost support
refs. That gives the system exactly **two** uncheckable agent assertions, both auditable:
`Equivalence` (this change preserved the meaning) and mis-grounding (this support never
supported this claim). Everything else is derived or evidenced.

**`coverage-converges` makes convergence enforceable rather than aspirational.** It diffs the
grounded coverage in the working tree against the same index at git `HEAD` and reports any
Touched.Data that stopped being covered — excusing exactly the losses the removals log
accounts for. An untracked project degrades to silence, since that is a normal state and not
a defect.

**Every check now documents its resolutions**, and `tarav2 poi explain` prints them:

```text
record-grounded
  bar      yes — typed, scoped, and grounded is the minimum
  resolutions (choose case by case; none is prescribed):
    - ground it — find the support that was always there
    - delete it — it was scratch, and nothing is lost
    - keep it — useful orientation carrying Index.Presumption; grounding stays debt
```

A test asserts no check ships without resolutions, and that all but three offer more than one
— a POI that admits a single answer is the exception, not the shape.

```text
tarav2 index linter    clean — 21 record(s), 21 surface line(s), 27 check(s)
tarav2 index remove <grounded>   refused: would shrink coverage of the Touched.Data
pytest                 126 passed        ruff  All checks passed
```
