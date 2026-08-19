# Tarav2 No.Agent.State - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. 149 tests green; `ruff` clean; the depot lints clean at 32 records. Supersedes the `Convergence Addendum` of `633-tarav2-trace-and-review-impl-req.md`, whose `mis_grounding` mechanism the user rejected as an untrusted summary.
- **Scope:** Remove every value in tarav2 that is *merely agent-stated*. Delete `removals.jsonl` and `supersedes`; derive index HEAD/TAIL from presence on a declared `HEAD.Surface`; add a `Landing.Gate` link carrying the approval turn's token round-trip; derive the agent/user split from review evidence; drop the stored `placement.verbatim` claim; put `bless` behind a gate.
- **Governing principle:** the system will **not** carry a value that is merely agent-based. Where a value is irreducibly agent-generated — the line body, its type, its scope, and the `rephrase` equivalence claim — it must sit adjacent to inlined checkable assertions, so talking is harder than being right.
- **Targets:** `tarav2/tarav2-py/src/tarav2/`, its tests, and the seeded `tarav2-md` depot.
- **Out of scope:** Writing a Chat.Index (`placement` stays modelled and uncomputed); shipping `Touched.Data`; a CLI that *mints* gate tokens in a live conversation.
- **Acceptance:** No stored field decides index standing or review standing. Deleting a line is git's business, not the index's. A line on a `HEAD.Surface` without a verified landing gate is a POI; a gated trace on no `HEAD.Surface` is a POI. The `bless` file cannot silence a check without evidence.

## Impl.Index

### No.Agent.State

- [CT] the system will not carry a value which is merely agent-based; where a value must be agent-generated it carries inlined assertions close by, so talking is harder.
- [DC] a better, more auditable structure always displaces an agent definition — presence on a surface displaces a standing field.
- [DF] a `Gate` is a token round-trip: the line names a turn, the user turn carries the token and qualifies as touch, an agent turn carries the same token and contains the line verbatim.
- [DC] review and landing are the same machinery asking different questions, so they are two links over one `GateRef` rather than one link with two meanings.

### Index.Removal

- [CT] deleted lines are tracked on git; the index system does not track them.
- [DC] a parallel removals ledger records an agent's prose reason for a deletion git already records, so it is an invented mechanism and is deleted.
- [DC] `remove` stops refusing and stops asking for a reason; a lost grounded line surfaces through `coverage-converges` as a POI whose resolution is to read the commit.

### Index.Head.Surface

- [DF] a line is in the HEAD if it is on a `HEAD.Surface`; that is what "promoted" means, stated positively rather than as absence.
- [DC] the set of `HEAD.Surface`s is project-tier declared state, because it is the trust root — inferred from path, an agent makes anything current design by creating a file.
- [DC] TAIL is a record with occurrences on no `HEAD.Surface`; no occurrence anywhere remains `Record.Unplaced`, so absence stays readable.
- [DC] `supersedes` is deleted: standing tied to a surface needs no field, and the supersession edge is recoverable from the chat rather than the index.

### Landing.Gate

- [DF] the approval turn is the design-status gate; approving means landing to HEAD.
- [DC] the gate attaches to the trace, not the line, or every rename would need re-approval — the problem the trace already solved for review.
- [DC] demotion stays ungated: protection belongs on what enters current design, and a gate outliving its surface presence already detects a silent demotion.
- [DC] a line on a `HEAD.Surface` whose trace carries no verified gate is an unlicensed promotion and a POI.

### Derived.Review.Split

- [DC] the agent/user split is derived from review evidence rather than stored, so `promote()` and the `index` field both disappear.
- [DC] the store flattens to one folder per tier, because a folder cannot name a standing that only the whole trace can decide.

### Blessing.Evidence

- [CT] a blessing is the one piece of state whose purpose is to stop the checker, so it is the last place an unevidenced agent value may survive.
- [DC] a blessing carries a gate and degrades like review: unverifiable when the archive is absent, revoked and reported when the archive contradicts it.

## Impl.Log

- Index.Presumption: `remove()` drops its grounded-line refusal entirely. The user rejected the recorded-reason mechanism; a hard refusal in the store is the remaining half of the same invention, and it makes the store issue a verdict where the design says the linter reports a POI. `coverage-converges` preserves the guarantee.
- Index.Presumption: the default `HEAD.Surface` pattern is `skills/*/homes/*/chapters/*.md` — chapters are the promoted surface, appendix is depth. Written to `.tarav2/head-surfaces.json` at `init` so changing it is a diff.
- Index.Presumption: `placement.verbatim` is dropped with no replacement. Nothing computes placement yet, so adding a recomputation path now would be tooling ahead of a consumer.
- Resolved during execution: with the general default the 21 seeded lines each reported `Landing.Unevidenced`, truthfully. The depot's declaration was narrowed to `homes/ceo/chapters/*.md` — see *Decisions Taken In Autonomous Mode*. No gate was minted for them.
- Observed off-model layout: the seeded chapter is `homes/agent/chapters/100-design.md`, while `tarav2-md/AGENTS.md` states the agent home is serialized only and carries no authored prose chapters. Under the narrowed declaration this is now consistent — the agent home is where unpromoted agent material lives — but the "no authored prose chapters" sentence in that AGENTS.md is the half that no longer matches.

## Execution.Plan

### Slice 1 — `GateRef`
Replace `ReviewRef` with a general `GateRef` (archive, session, token, user_turn_id, agent_turn_id) and one shared verification helper returning verified / contradicted / unverifiable.
**Check:** review keeps its current behavior through the new type; a fabricated token is contradicted; an absent archive is unverifiable.

### Slice 2 — Delete the removals ledger
Drop `removals.jsonl`, `_record_removal`, `removals()`, the `mis_grounding` parameter, and the grounded-removal refusal. `coverage-converges` loses its excuse set.
**Check:** removing a grounded line raises `Coverage.Shrank`; removing an ungrounded one does not; no removals file is ever written.

### Slice 3 — `HEAD.Surface` registry
`.tarav2/head-surfaces.json` with glob patterns, written by `init`, read by a `HeadSurfaces` resolver.
**Check:** a chapter matches, an appendix does not, an undeclared path does not; a project with no file falls back to the default pattern.

### Slice 4 — Landing gate and derived index standing
Add `links.landing`; delete `supersedes` and `superseding()`. `index_standing` reads occurrences against the `HEAD.Surface` set. `materializable` collapses to `is_trace_head`.
**Check:** a line on a declared head surface derives HEAD; move it off and it derives TAIL; a gated trace on no head surface and an ungated line on one both report.

### Slice 5 — Derived review split
Delete `ReviewIndex` as a stored field and `promote()`. Flatten the store to `<tier>/index/*.json`. Derive the side in `standing.py`.
**Check:** a trace with review evidence derives the user side; every other trace derives the agent side; records round-trip without an `index` key.

### Slice 6 — Drop `placement.verbatim`
**Check:** a placement round-trips with three fields and no claim.

### Slice 7 — Gated blessings
`blessed.json` becomes `{identity: gate}`. A contradicted gate revokes the blessing and reports it.
**Check:** a blessing with an unverifiable gate still silences; a contradicted one does not and raises `Blessing.Unevidenced`.

### Slice 8 — Catalog, CLI, migration
Update the check catalog and resolutions; remove `index promote` and the `--supersedes` / `--review` write flags; add `index gate`. Migrate the 21 seeded records.
**Check:** `tarav2 index linter` runs; every check documents resolutions; the depot reports only the expected `Landing.Unevidenced` set.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | `GateRef` | done | one type, one `verify_gate`; three-valued verdict |
| 2 | Delete removals ledger | done | grounded removal reports `Coverage.Shrank`, writes no file |
| 3 | `HEAD.Surface` registry | done | chapter matches, appendix does not, declaration overrides |
| 4 | Landing gate, derived standing | done | presence derives HEAD; both mismatches report |
| 5 | Derived review split | done | review evidence derives the user side; store flattened |
| 6 | Drop `placement.verbatim` | done | placement round-trips with three fields |
| 7 | Gated blessings | done | contradicted gate revokes; unverifiable still silences |
| 8 | Catalog, CLI, migration | done | 27 checks; 21 records migrated; 11 new lines captured |

## Verification

The fabricated gate is caught twice — once when recorded, once by the linter:

```text
tarav2 index gate ln_0b4a15… --kind landing --token idx-edition:fabricated
  contradicted: the user turn does not carry the gate token

Index.Linter/Gate.Contradicted    landing gate does not hold: the user turn does not carry the token
Index.Linter/Landing.Unhonored    trace carries a landing gate but sits on no HEAD.Surface
```

**Both halves fire.** The token is the evidence and the surface is the state, so a gate that
did not happen and a promotion that did not land are two different findings.

The depot after migration and capture:

```text
tarav2 index linter    clean — 32 record(s), 32 surface line(s), 27 check(s)
tarav2 index record    32 entries, all `G a T *` — grounded, agent side, TAIL, trace head
pytest                 149 passed        ruff  All checks passed
```

Every entry reads TAIL because nothing here has been through an approval gate. That is the
correct reading of this depot, not a defect: the lines are grounded agent material, and the
project HEAD is empty until a user turn says otherwise.

## Decisions Taken In Autonomous Mode

**The seeded depot's `HEAD.Surface` declaration was narrowed to `homes/ceo/chapters/*.md`.**
With the general default the 21 seeded lines each reported `Landing.Unevidenced` — truthfully:
an agent had put them on a chapter with no approval. Narrowing is the third resolution the POI
itself offers, and it makes the two splits line up geographically: the agent home holds
agent-maintained material, the ceo home holds what was promoted. Widen the declaration and the
21 findings come back, which is the point of it being a diff.

**No gate was minted for the existing lines.** Fabricating approval turns for them is the exact
failure this cut exists to prevent.
