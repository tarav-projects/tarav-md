# Checks, providers, and runners

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Shared mechanics

Tarav should provide a workflow for defining and running checks, so each
type or workflow does not need to build its own engine. The structural checks
for [Reader.Context.Path](reader-context-path.md) should use this shared
interface. The existing [POI system](poi-system.md) is itself work in progress;
define the minimal interface and mechanics needed for this use case rather
than treating its current implementation as a fixed contract.
<!-- tarav.breadcrumb acd062a9d8f4d766726a149f245c44d6cb2e6978a20ab54143b2c4cf29357762 -->
<!-- tarav.breadcrumb 7a0d1da62f6d2e5fb7f432d7ac984462354a5cc6d37762f09bf5b999ca81d8c6 -->

## Check and CheckProvider

Check types define reusable checking behavior. A `CheckProvider` exposes
checks appropriate to its subjects, through an interface such as `obj.checks`.
Objects can opt into that capability by subtyping the provider base; checks
can be supplied at object, type, or workflow level. Check classes can be
instantiated wherever needed. These are design contracts; the exact collection
API and implementation remain to be defined.
<!-- tarav.breadcrumb a133c03ad07b0da1cf520789815683a581e35e980d11f0e51fd11eb3bd37e213 -->
<!-- tarav.breadcrumb 797985d00c878dc46db7b48ee42fdd5038885a2d6654a33845801c2b9417fdb5 -->

Providers instantiate appropriate checks; runners and linters select,
execute, and aggregate them. A linter can collect checks from the objects it
inspects and also construct checks involving multiple subjects that do not
naturally belong to either subject alone. Explicit check pools remain valid.
Definitions and construction should live where their semantics fit best,
while all these sources share the same Check contract.
<!-- tarav.breadcrumb b71fbe6c34fb4ae172b0d91b3f2cde2180aa22e083b279b6fab510eeceff29d5 -->
<!-- tarav.breadcrumb 14925d370e38c9acc310712d748d432fa68482c0b16de1cf052d04f23992fe06 -->

## Targeted execution

Checks must be usable independently: instantiate and run a single check,
run the checks exposed by one object, or combine selected checks into a
larger run. Quick and targeted experiments do not require a linter or a
larger workflow. A linter adds selection, orchestration, and reporting around
checks that are already runnable on their own.
<!-- tarav.breadcrumb 7ebc9a1a131a4303e333913288f5712aa2cce99f080fa6ec83668dd344c257ea -->
<!-- tarav.breadcrumb 133aeeeca5db59cc4446c5fca370946081387eb96e6bc05b075d020221bfa8fa -->

## Candidate organization

The agent proposed `tarav.l1.checks` for the common interface, results and
runner, using `tarav.l1.poi` for findings; reading-path declarations would
remain in `tarav.l1.skw.skills`, with concrete shared-interface checks in
`tarav.l2.skw.skills.checks`. This is a proposed package arrangement, not an
inspection of existing APIs. Likewise, `CheckResult`, a bound check collection,
and distinguishing execution failure from a completed check with no findings
are proposed MVP details, not yet finalized schemas.
<!-- tarav.breadcrumb 91edfb2ad3ad57d9db35f1c3d9968ed744b6bf1f068a1d87897390b6a04723a8 -->
<!-- tarav.breadcrumb c067491fc24da4e56365c88701f65e07a6ada5fd99fbace9f17a5f914cff4ae0 -->

## CheckResult as a POI provider

A Check executes and produces a CheckResult. The result contains or can
access everything needed to produce its POI instances, while retaining any
additional data the Checks workflow needs for its own purposes. Model it as
a POI provider. There must not be a parallel finding type duplicating POIs:
the objects describing check findings are POIs themselves. "Finding" can
remain a descriptive name for those POIs.
<!-- tarav.breadcrumb 54e3ca427f15223cce5265810a9e4009c153fb93d4a32a50e3ba3d7791e58e8a -->

POIs are a central communication surface for agents and carry the contextual
information needed to investigate an occurrence. A CheckResult can remain
lighter than that agent-facing representation. Producing a POI and raising
it are distinct operations; the raising mechanics and semantics belong to
the POI workflow. Checks integrate with that workflow rather than defining
their own raising system.
<!-- tarav.breadcrumb a4cbea50df393d0c57aa8c3ce0ad016d66ed1dad6a7e9d471fb61ff230cbe919 -->

The resulting design is Check → CheckResult (POI provider) → POI instances
→ raise through POI mechanics. The agent proposed a reusable `POIProvider`
interface owned by the POI workflow, with results either retaining or
constructing POIs when requested. Exact method names, storage, and raising
policy remain open; illustrative `pois()` and `raise_()` calls are not claims
about implemented APIs.
<!-- tarav.breadcrumb 7d28f24f3c1a83ecfeae3e2cd778b6b5a9aed39493936b2beee4f3dfcb6fb913 -->
<!-- tarav.breadcrumb b39c8a6102a3d6fbf1a0ddbe4c22b8f0e63efd7cb00499e7fb2622bed1e86d4b -->

## Implemented foundation — 2026-09-30

`tarav.l1.checks` now provides `Check`, `CheckProvider`, `CheckResult`, and
`run_checks`. A Check can run alone; a result snapshots its data and POIs.
Inspecting `result.pois()` emits nothing. The consumer may explicitly emit a
POI to a collector or invoke the POI's `.error()` method. SKW supplies three
reading checks through `SkwSkill.checks` and uses their results for its CLI
POI report. See the [Checks code](../../../../tarav-py/src/tarav/l1/checks/__init__.py)
and [SKW integration](../../../../tarav-py/src/tarav/l2/skw/reading_checks.py).
<!-- tarav.breadcrumb 5922aa58ced6a537d3d235fbbdeafe6c947c6d2f859c67fc3299fe7ee9f82fd2 -->
