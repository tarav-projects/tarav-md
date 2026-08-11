# Line.Type::GR Tooling Retirement — Impl.Req

## Impl.Abstract

- retire the last tooling and citation remnants of `Line.Type::GR` after the design-side retirement landed: the vocabulary is now seven act codes (`DF`, `DC`, `CT`, `RJ`, `PR`, `FR`, `EX`)
- design source: this session's `--index --edit` landing under `idx-edition:6b3f0a27` — `## Line.Type::GR` removed from `agentos-md/skills/agentos-pkg/design/106-design.md`, router row updated in `000-INDEX.md`
- cause of the retirement: `GR` typed lines inside `Grounding.Head` evidence boards, a block-grounding axis retired in July 2026 (`notes/live/594-grounding-retirement-tooling-impl-req.md`, executed 2026-07-18). Grounding became a line property; the type was left behind as an orphan of that retirement and never acquired a second use — zero `GR` lines exist across 1950 typed lines project-wide
- two halves, and they are gated differently: (1) `agentos-py` linter code still accepts `GR` as an act code and ships a `GR`-specific check; (2) live md surfaces still cite the retired type, and two of those citations are themselves gated Index lines
- out of scope: historical `Impl.Req` notes under `notes/live/` (571, 574, 577, 579, 594, 611) — they are the record of what happened and are not linted
- status: designed 2026-08-11, awaiting readiness approval

## Impl.Index

### Current.State (inspected 2026-08-11)

**agentos-py — the check and its code path**

- `src/agentos/index/_linter_parser_checks.py:30` — `LINE_TYPE_GR_MISSING_ANCHOR = "Index.Linter/Line.Type.GR.MissingAnchor"`
- `src/agentos/index/_linter_parser_checks.py:49` — `_LINE_TYPE_ACT_CODES = ("DF", "DC", "CT", "RJ", "PR", "FR", "EX", "GR")`
- `src/agentos/index/_linter_parser_checks.py:104-112` — the `if code == "GR" and not any(span.kind == "anchor" …)` branch emitting a warning
- `src/agentos/index/linter.py:54` — imports the constant
- `src/agentos/index/linter.py:186` — re-exports it in `__all__`
- `tests/test_index_linter_lines.py:40` — asserts the code appears in a fixture's findings

**agentos-md — gated Index surfaces**

- `skills/agentos-pkg/poi/101-poi.md:45` — the `## Index.Linter/Line.Type.GR.MissingAnchor` POI class block (3 kernel lines)
- `skills/agentos-pkg/000-INDEX.md:14` — the `poi/101-poi.md` router row names that class
- `skills/agentos-pkg/appendix/Index.Linter-appendix.md:121` — a typed `[DC]` kernel line: *"core `Line.Type` checks run without chatlas: bracket syntax, known act codes, `[GR]` trailing anchor (warnings); …"*

**agentos-md — skillware sources (built surfaces, never edit the built file)**

- `skills/agentos-hugentics/.skw/src/references/type.skw.md:39` — vocabulary table row `| cite | \`GR\` | accounts what an anchored evidence neighborhood grounds, anchor trailing |`
- `skills/agentos-hugentics/.skw/src/references/check.skw.md:56` — prose naming the `[GR]` trailing-anchor check
- `skills/agentos-hugentics/.skw/src/references/search.skw.md:55` — prose listing `[GR]` among the type acts
- built counterparts: `skills/agentos-hugentics/references/{type,check,search}.md`

### Design.Decisions

- **`GR` leaves `_LINE_TYPE_ACT_CODES` rather than keeping a deprecation branch.** A residual `[GR]` line then reports as `Index.Linter/Line.Type.UnknownCode` (warning), which is the accurate statement once the type is retired. Verified safe: zero `[GR]` typed lines exist on any surface, so nothing regresses into a warning today.
- **The `GR`-missing-anchor check is deleted, not disabled.** Its subject no longer exists; a default-off check for a retired code is dead configuration.
- **The POI class block is removed from `poi/101-poi.md`.** A POI class documents a finding the linter can emit; once the check is gone the class documents nothing. Surface history preserves it (`Demoted.Index.Line` ^c20260729-233u).
- **The two Index-surface edits go through the `--edit` gate, not through execution.** `poi/101-poi.md` and `appendix/Index.Linter-appendix.md` are gated Index surfaces; an implementation slice may not self-write them. Slice 4 pauses and routes them through a proposal/approval/landing cycle.
- **Skillware is edited at source and rebuilt.** `references/*.md` are managed build outputs; editing them directly produces drift the skillware check reports.
- **Ordering: code first, surfaces second.** The appendix line and the POI class describe linter behavior; revising them before the behavior changes would make the Index describe something untrue, however briefly.

### Open.Space

- whether `Line.Type.UnknownCode` should carry a friendlier message for codes known to have been retired — no touch on this, left provisional and unimplemented

## Execution.Plan

### Slice 1 — remove the GR check from the linter (RED → GREEN)

- **RED**: `tests/test_index_linter_lines.py` — replace the `Index.Linter/Line.Type.GR.MissingAnchor` assertion at :40 with the retirement behavior: a fixture line `- [GR] some body` now reports `Index.Linter/Line.Type.UnknownCode`, and `Line.Type.GR.MissingAnchor` appears in no findings. Confirm it fails against current code.
- drop `GR` from `_LINE_TYPE_ACT_CODES` (:49)
- delete the `if code == "GR" …` branch (:104-112) and the `LINE_TYPE_GR_MISSING_ANCHOR` constant (:30)
- remove the import (`linter.py:54`) and the `__all__` entry (`linter.py:186`)
- **check**: `uv run pytest tests/test_index_linter_lines.py` green; `grep -rn "GR_MISSING_ANCHOR\|Line.Type.GR" src/ tests/` returns nothing
- **observable result**: the linter's known act codes are the seven live types

### Slice 2 — full suite and depot regression

- **check**: `uv run pytest` green in `agentos-py`
- **check**: `agentos index linter --depot agentos-md/skills/agentos-pkg` — finding counts unchanged except the retired class, and the pre-existing `Index.Linter/Block.TooLong` error at `design/113-design.md:5` (another session's, not this work) still the only error
- **check**: same for `agentos-md/skills/agentos-hugentics` and the chatlas depot
- **deviation trigger**: any new error, or a warning-count change not attributable to the retired check → stop and record in `Impl.Log`

### Slice 3 — skillware sources and rebuild

- edit `.skw/src/references/type.skw.md:39` — delete the `cite | GR` row; the table becomes seven rows
- edit `.skw/src/references/check.skw.md:56` — drop `` `[GR]` trailing anchor `` from the listed parser-backed checks
- edit `.skw/src/references/search.skw.md:55` — drop `` `[GR]` cites evidence `` from the act summary
- rebuild the skill package through the Skillware build surface
- **check**: skillware drift check clean; `grep -rn "\[GR\]\|Line.Type::GR" skills/agentos-hugentics/` returns nothing in either source or built surfaces
- **observable result**: an agent loading `--type` sees a seven-type vocabulary

### Slice 4 — gated Index surface edits (PAUSES for approval)

Not self-written. Propose through `Index.Edition.Turn`, take `::approve <token>`, then land:

- `poi/101-poi.md` — remove the `## Index.Linter/Line.Type.GR.MissingAnchor` block
- `000-INDEX.md` — drop that class from the `poi/101-poi.md` router row
- `appendix/Index.Linter-appendix.md:121` — revise the `[DC]` line to drop the `[GR]` trailing-anchor clause; the line keeps its anchor and its meaning is otherwise unchanged, so judge whether the amendment preserves the semantic support edge (`^c20260810-21u`) or creates a successor reference (`^c20260810-20u`)
- **check**: `agentos index linter --depot agentos-md/skills/agentos-pkg` clean of new findings; `--anchor` scoped `line-approval` and `line-verbatim-gate` on any re-anchored line, run with `--show-passed` so a silent zero-finding result is distinguishable from a check that never ran
- **observable result**: no live surface in either depot names `Line.Type::GR`

### Acceptance

- `grep -rn "Line.Type::GR\|Line.Type.GR.MissingAnchor\|\[GR\]" agentos-md/skills/ agentos-py/src/ agentos/py/tests/` returns only historical `notes/live/` hits
- both md depots lint with no new findings
- `agentos-py` suite green
- skillware check clean

## Impl.Log

- 2026-08-11: designed. Scope confirmed by direct inspection of all six named files.
