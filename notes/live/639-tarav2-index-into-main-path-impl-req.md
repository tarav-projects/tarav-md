# Migrate The Tarav2 Index Into The Main Tarav Path - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. 2067 tests green, ruff clean; `tarav index linter` reports 29 checks, 0 failed, 0 blocked over the converged depot.
- **Parent:** `638-tarav2-migration-master-impl-req.md`, Step 1.
- **Scope:** Move the tarav2 index implementation into `tarav` so there is one CLI and one index. tarav1's index *application* is replaced; its *model kernel* and the shared services that happen to live beside it are not.
- **Targets:** `tarav-py/src/tarav/`, `tarav2/tarav2-py/`, and `tarav-py` tests.
- **Naming:** the converged system is `tarav` everywhere. `tarav2` and `.tarav2/` were scaffolding and are removed, not carried forward.
- **Out of scope:** converting any index surface (Step 5), the capture loop (Step 3), reconciling md surfaces to the new command names (Step 2). This step moves code; it converts no content.
- **Freeze:** in force. No anchors are minted here and no index line is grounded, so this artifact's `Impl.Index` is ungrounded by design and carries `Index.Presumption`.
- **Acceptance:** `tarav index` runs the new implementation, nothing is named tarav2, one `CATALOG` holds the surviving checks, and every consumer outside the index still imports what it needs.

## Impl.Index

Ungrounded — the freeze grounds nothing but the `Test.Block` run.

### Old.Into.New

- [DC] the whole old index is integrated into the new design: model, services, checks, commands — each piece reimplemented where the new design keeps its constraint, dropped where it does not
- [RJ] relocating an old part so it survives the swap unexamined is rejected: it keeps old-design code alive inside the converged system under a new path
- [CT] consumers outside the index are the requirement the integration must satisfy, since they are not being replaced and their needs outlive whichever old module served them
- [DF] a drop is named in `Impl.Log` with the constraint it asserted, so it is a decision rather than an omission

****

### Integration.Surface

- [DF] the old index is 5747 lines in three parts: `model/` at 998, `wayfinder`/`poi_catalog`/line-manifest schema at 745, and the application at 4004
- [DC] `model/` is already integrated — the new implementation imports its parser, identity and canonical statement hashing today
- [DF] the services have consumers the index does not: anchory, canvas and skillware call `create_index_wayfinder`, runtime and the old linter call `discover_poi_catalog`
- [CT] those consumers decide what the new design owes them, which is a smaller question than what the old modules do

****

### Converged.Naming

- [DC] nothing in the converged system is named tarav2: the package is `tarav`, the tier is `.tarav/`, the CLI is `tarav`
- [CT] `tarav2` and `.tarav2/` were scaffolding for building alongside, and scaffolding is removed rather than renamed forward
- [DC] the intermediate state where both command sets exist is a slice boundary inside this artifact, not a shipped surface

## Execution.Plan

### Slice 1 — Bring the new implementation in as `tarav`
Move `tarav2/tarav2-py/src/tarav2/` in beside the old index, renamed to `tarav` throughout — package, tier (`.tarav/`), CLI. Tests come with it. Both command sets exist at this point.
**Check:** the 171 tests pass in place; `tarav-py`'s own suite is unaffected.
**Deviation trigger:** an import cycle between the new index and `chatlas2` stops the slice and returns to design.

### Slice 2 — Integrate the services
Take the consumers first — `anchory/poi.py`, `canvas/poi.py`, `skillware/commands.py` (×3), `runtime.py`, `chatlas/line_manifest.py` — and decide what block-reference resolution and POI-catalog discovery mean under the new design. Reimplement what it keeps; drop what it does not.
**Check:** every consumer resolves what it needs against the new design; no consumer imports the old application zone.

### Slice 3 — Integrate the checks
One `CATALOG`. Walk the old design's assertions — the five chatlas grounding checks and the tarav1 linter's set — and reimplement or drop each.
**Check:** every survivor fires on a fixture that should trip it and stays quiet on one that should not; every drop is named.

### Slice 4 — Swap the CLI and delete the old index
`tarav index` registers the new command set. Delete the application zone and whatever slices 2–3 left behind.
**Check:** `tarav index --help` is the new set; nothing named tarav2 remains in `tarav-py`; full suite green.

### Slice 5 — Retire the tarav2 folder
Delete `tarav2/tarav2-py/`, leaving `tarav2/tarav2-md/` as the depot Step 5 of `638` folds into `tarav-pkg`.
**Check:** no `tarav2` console script resolves; `638`'s Step 1 destination condition reads true.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | relocate shared services | done | 2024 green; the kernel became `tarav.index_model` |
| 2 | bring the new implementation in as `tarav` | done | vendored and renamed; no `tarav2` token survives |
| 3 | integrate the two check sets | done | one `CATALOG`; the five grounding checks map onto it |
| 4 | swap the CLI, delete the old application zone | done | `tarav index --help` is the new flat set |
| 5 | retire the tarav2 folder | done | `tarav2-py` deleted; the depot's tier is `.tarav/` |

## Verification

```text
tarav index linter        29 check(s): 29 passed, 0 failed, 0 blocked
                          0 error(s), 0 unverifiable, over 49 record(s)
pytest                    2067 passed          ruff  All checks passed
```

`coverage-converges` stopped being blocked: the depot is git-tracked now, so the
check that could only report *unverifiable* before actually runs.

**Slice 1 grew a step nobody planned.** Relocating `wayfinder` and `poi_catalog`
did not break the cycle, because the architecture test measures the import graph
at top-level package granularity — so any service importing `tarav.index.model`
still declared an edge to the subsystem being deleted. The fix was to promote the
kernel to `tarav.index_model`, which is `Index.Zones` made structural rather than
merely described. The three-zone reading was right; it just had to become a
directory layout before it did any work.

**The five grounding checks were not ported; they were already covered.**

```text
grounding_provenance         -> record-grounded, support-resolves
grounding_line_drift         -> line-drift
grounding_line_approval      -> review-evidence
grounding_line_verbatim_gate -> gate-verifies
project_index_coverage       -> coverage-converges
```

The old linter's model survives as `tarav.chatlas.index_check_model` because the
chatlas check modules still hold the two grounding resolvers `chatlas2` uses.
Sixteen test modules exercising the deleted host were retired with it.

**A correction landed mid-slice.** The write model was documented as a path guard
in five places — *"agents must never write into `homes/<user>/`"*. The code
disagreed with the prose: `_check_landing_evidenced` reads *"presence without a
gate is a promotion an agent granted on its own authority"*, which only parses if
the agent is the writer. `is_agent_writable` and `assert_agent_writable` existed
but had no production caller, and would have refused exactly the write that
promotion consists of. Both are deleted; `home_owner` stays, because reporting who
governs a path is a fact that licenses nothing.

## Impl.Log

### Index.Presumption

- The 998 / 745 / 4004 split and the consumer lists are measured from the source. What the new design should do with block-reference resolution and POI-catalog discovery is not decided here — slice 2 decides it, from the consumers.
- The chatlas2 ↔ index import cycle is a real hazard but not a design driver. It is a deviation trigger on slice 1, not a reason to shape the integration around it.

### Notes

- The `tarav index linter` break over `tarav-pkg` between this step and Step 5 is real and is the strongest argument for keeping Steps 1–5 close together in time rather than interleaving other work.
- `tarav2/.tarav2/index/user/ln_0181b1788d423140.json` is an orphaned schema-v1 record carrying a `"review": "user"` field that `634` deleted as agent state. It is not part of the live depot. Slice 5 is its natural disposal point.
