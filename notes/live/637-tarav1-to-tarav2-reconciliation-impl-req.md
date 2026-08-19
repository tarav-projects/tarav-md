# Tarav1 → Tarav2 Reconciliation, First Cut - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. 171 tests green; `ruff` clean; the rehearsal imports 29 lines and reports exactly the expected debt.
- **Scope:** Begin the merge. Give tarav2 an importer that brings a tarav1-layout depot's `Index.Notes` into its own layout and `Serialized.Index`, plus the two ergonomic fixes the last audit surfaced. Rehearse on `tarav-hugentics` — one chapter, 29 lines.
- **Governing principle:** the cut is *flipping which system is the entry point*, not rewriting what works. tarav2 already depends on tarav1 for everything the model did not change.
- **Targets:** `tarav2/tarav2-py/`, and a scratch project for the rehearsal. **tarav1 is not modified** — the importer reads and copies, never moves.
- **Out of scope:** grounding the imported lines (the `^c` question); the capture loop; `Chat.Index`; multi-depot label namespaces.
- **Acceptance:** a tarav1 depot's chapters become tarav2 records and tarav2-layout notes in one command, with no tarav1 file touched. `index revise` tells the agent which note to edit. A home that carries no `Index.Notes` stops raising `Record.Unplaced`.

## Impl.Index

### Label.Namespace

- [DC] labels stay unique per **store**, not per depot; resolution is then unambiguous with no namespace axis to maintain.
- [DC] migration collisions are resolved by `relabel`, which already exists because the label is a public id the id does not follow.
- [CT] this is stronger than tarav1's per-depot uniqueness, so importing many depots into one store cannot produce an ambiguous reference.

### Depot.Import

- [DF] importing a tarav1 depot means copying its chapter notes into tarav2's home layout and minting a record for every kernel line.
- [DC] tarav1's layout is read by the importer and not supported afterwards; the system converges on one layout rather than carrying two.
- [DC] imported material lands on the **agent side**, because tarav1's review evidence is `^c` anchors that no active workflow resolves.
- [CT] promotion of imported lines to a `HEAD.Surface` stays a separate gated act; migration never confers reviewed standing.
- [DC] imported lines arrive ungrounded and raise `Line.Ungrounded` and `Anchor.LegacySigil`; both are expected debt, not import failures.

### Surface.Sync

- [DC] `index revise` mints a record whose note is stale by construction, so it prints the exact surface edit rather than leaving the agent to find it.
- [DF] a home declares whether it carries `Index.Notes`; a home that does not is `Serialized.Index` only.
- [DC] `record-placed` reads that declaration, so a serialized-only home stops reporting every entry as unplaced.

## Impl.Log

- Index.Presumption: the rehearsal imports into the **agent home** of a scratch project. Landing imported content on a `HEAD.Surface` would claim a gate that does not exist.
- Index.Presumption: the importer preserves original labels where they do not collide. Keeping `^c` labels makes the legacy visible to `anchor-legacy-sigil` instead of erasing the fact that these lines came from an unresolvable era.
- Deferred: `^c` grounding. Registering a `chat-legacy` `Touch.Authority.Manifest` is the designed answer and is a decision of its own.
- Step 1 of the agreed sequence collapsed on inspection: tarav2 never called anchory. It mints its own labels and writes complete records already.

## Execution.Plan

### Slice 1 — `index revise` points at the edit
Print the note path, the line to replace, and its replacement, all derived from the predecessor and the scope.
**Check:** revising a line prints a surface edit that resolves to a real file and a real line.

### Slice 2 — Serialized-only homes
`.tarav2/homes.json` declares which homes carry `Index.Notes`; `record-placed` respects it.
**Check:** a record scoped to a notes-less home raises nothing; the same record in a notes-carrying home raises `Record.Unplaced`.

### Slice 3 — `tarav2 index import`
Read a tarav1-layout depot (`<depot>/design/NNN-design.md`), copy each chapter into `skills/<depot>/homes/<home>/chapters/`, mint a record per kernel line, relabel on collision.
**Check:** every imported line has a record; labels are unique in the store; no source file is modified.

### Slice 4 — Rehearse on `tarav-hugentics`
Import into a scratch project and lint.
**Check:** 29 lines imported; findings are exactly the expected debt classes.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | `index revise` points at the edit | done | prints note path, line to replace, replacement — resolved from the scope |
| 2 | Serialized-only homes | done | `.tarav2/homes.json`; `record-placed` skips a notes-less home |
| 3 | `tarav2 index import` | done | 29 records, unique labels, no source file modified |
| 4 | Rehearse on `tarav-hugentics` | done | findings are exactly `Line.Ungrounded` ×29 and `Anchor.LegacySigil` ×29 |

## Verification

The rehearsal ran in a scratch project against the live `tarav-hugentics` depot:

```text
imported tarav-hugentics -> homes/agent
  skills/tarav-hugentics/homes/agent/chapters/100-design.md
  29 line(s) recorded, 1 chapter(s)
  nothing grounded, nothing promoted

Index.Linter/Anchor.LegacySigil  (29)
Index.Linter/Line.Ungrounded     (29)
29 check(s): 26 passed, 2 failed, 1 blocked   58 error(s), 0 unverifiable
```

`git status` in tarav1 was empty afterwards: the importer reads and copies only.

**The rehearsal found a real defect.** The first run added `Landing.Unevidenced` x29 — the
default `HEAD.Surface` pattern `skills/*/homes/*/chapters/*.md` matches *every* home, so
imported material claimed promoted standing the moment it arrived. Fixed by rule in
`HeadSurfaces.contains()`: a path under `homes/agent` is never a `HEAD.Surface`, because the
agent home is where unpromoted material lives and promotion *is* the move out of it.

That rule retires a decision taken in autonomous mode in `634`, which narrowed `tarav2-md`'s
declaration to `homes/ceo/chapters/*.md` by hand to silence the same 21 findings. The
declaration has been reverted to the default and the depot still lints clean:

```text
29 check(s): 28 passed, 0 failed, 1 blocked   0 error(s)   over 49 record(s)
```

A hand-narrowed declaration and a rule are not the same fix: the first silenced one depot, the
second states why the finding was wrong everywhere. Per *a defect found by hand owes the suite
a test*, the exclusion is asserted by `test_the_agent_home_is_never_a_head_surface`, not by
the depot's config.
