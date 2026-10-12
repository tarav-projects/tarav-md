# Checks, providers, and runners

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
64298cbc = claude-code:9da4cef5-68b7-4d17-8a06-1351ca51e82f @64298cbc8db2e7aa971e0828653c07bcb483cfed40931fdf87d5abe7ce1c60b3
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## Shared mechanics

### Bound Checks namespace — 2026-10-07

The User selected `project.checks.run()` and liked a shared Checks namespace on CheckProvider, so Projects, Workspaces, and other providers use the same path. A provider's `Checks.suite()` declares the bound suite without running it; `checks.run()` executes that suite. Independent contributors to one Checks namespace require an explicit combined suite; namespace inheritance alone does not merge their checks.
<!-- tarav.breadcrumb ff5b0b1ced925dab86407678adee97a202917a64a7edffe1bd0864eed106758b -->

The Python implementation moved concrete providers and maintained callers to the namespace. See [Impl.Req 866](../../../tarav-py/notes/live/866-project-capability-paths-impl-req.md).
<!-- tarav.breadcrumb 75b5f7a7bdba2aef95d1fb8feb08a6e5badf3beae69e77db7f701189631426db -->


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

## POI integration refinement — design

Checks and POIs are the fundamental objects for audit integration. A
CheckProvider is optional: its role is to expose checks from a subject, not
to be a prerequisite for constructing and running a Check directly. The
Check class provides an inspectable explanation of its produced CheckPOIs.
The Checks and POI systems can co-evolve to fit the audit rather than forcing
the audit into an unsuitable workflow.
<!-- tarav.breadcrumb df023e7b391b95d9ab78a75220150b6e76aad224bd53d42ddec474a600cd3b34 -->
<!-- tarav.breadcrumb 4a2fab9f4e4ed4fd06d9a4003295e12f6f02e43e5d27ee65147980499e81de1e -->

The proposed `CheckPOI` belongs with Checks and inherits the general POI base.
`NotificationPOI` covers visible operations such as appending a Breadcrumb
location observation, without inventing a Check for that notification. POIs
are neutral points of interest. Checks raise failure POIs by default, but
that convention does not make every POI negative. See
[POI semantics](poi-system.md#points-of-interest-not-inherently-problems).
This refinement is not yet an implementation report.
<!-- tarav.breadcrumb e4feaf5014aefd477b798ce4e1be461ec843b28b844cd0d7b292105ff006afdd -->
<!-- tarav.breadcrumb 7d97e92fff9e958ab49d80eba5feadfee76389b99e0241da2992024c0a922ab8 -->
<!-- tarav.breadcrumb bd34277c6e9b3d81519d6879f34aafa660b3bbb60f997c44dadffce0b5a84c40 -->
<!-- tarav.breadcrumb 5c615d4bc8679f1717e53b898547adb84d9dc84a455b6ca3f65a1dae353c175e -->

## Implemented foundation — 2026-09-30

`tarav.l1.checks` now provides `Check`, `CheckProvider`, `CheckResult`, and
`run_checks`. A Check can run alone; a result snapshots its data and POIs.
Inspecting `result.pois()` emits nothing. The consumer may explicitly emit a
POI to a collector or invoke the POI's `.error()` method. SKW supplies three
reading checks through `SkwSkill.checks` and uses their results for its CLI
POI report. See the [Checks code](../../../../tarav-py/src/tarav/l1/checks/__init__.py)
and [SKW integration](../../../../tarav-py/src/tarav/l2/skw/reading_checks.py).
<!-- tarav.breadcrumb 5922aa58ced6a537d3d235fbbdeafe6c947c6d2f859c67fc3299fe7ee9f82fd2 -->

## SituationCheck

SituationCheck is an optional Check specialization that evaluates only a
situation supplied before execution. Any additional data required by evaluation
must first be captured in that situation. The flow is Situation → Check → POI:
detection and POI identity share the same description, rather than independently
selecting inputs that can disagree.
<!-- tarav.breadcrumb d052cf7a461c9b5fb2e364074b90cda15e32eed9f24e4cfebf61f63b44574d66 -->

Use a general Situation based on LiteRecord; a new situation class for every
check is unnecessary. Specialized checks may define their own situation types
when stronger constraints are useful. Objects can collect their situations and
provide bound checks, but this organizational choice does not forbid direct
construction or other integrations between workflows.
<!-- tarav.breadcrumb 105eb9e025970cf720969a5045ae4bc5316345ecd30c7e129db70b2c8409bda2 -->
<!-- tarav.breadcrumb 2737f2770664d8e4f40038a760395f7ce337445a88cea749aebfdc000e608983 -->

Retain the current iterable `obj.checks` property. Named selection is deferred.
[Request 835](../../../tarav-py/notes/live/835-situation-checks-impl-req.md)
implemented the common mechanics and a bounded SKW freshness integration.
<!-- tarav.breadcrumb 14021d78efd3dbdfaeff4ada1639d5f7d911721889a2208074a314619ba6ff95 -->
<!-- tarav.breadcrumb 5c45c5dcc0ddd05824736d0fbd49fa2ab7e2577702ec6c23ffa4c76514b68111 -->

A Situation defines the scope of acceptance: changing any field may produce a
new POI identity and require another blessing. Situation descriptions need not
be minimal; extra fields may deliberately favor conservative resurfacing.
Separate bound checks should represent independently assessable concerns.
<!-- tarav.breadcrumb c2d9df1ece09957d2b8a6206869b15d41057dc2dc9f6c4c261545466c2dfdb03 -->

`SituationCheck` snapshots and validates its input, exposes it through context,
and rejects a returned `CheckPOI` whose situation differs. SKW now creates
separate generation-input and tracked-context freshness checks before running
them, so evaluation does not reread mutable external inputs.
<!-- tarav.breadcrumb da3da29ce0211b9c054f99b7090f9b8f8e6ab9412554634f4d012ccea5a08ce2 -->

## Reference resolution Checks

A declared Reference can expose an independently runnable Check without a
freshness baseline. Successful resolution produces no failure POI. A broken or
currently unavailable target produces a CheckPOI that retains the declaration,
its owning coordinate, and the available failure reason. This keeps resolution
visible when dependent freshness cannot construct its own situation.
<!-- tarav.breadcrumb 3aa317a1b22789b5ee5fc19c65c8528d27e340883f1ccc13cd2fc419969d5246 -->
<!-- tarav.breadcrumb 0ce78f0cbbc4e89bf5e218c068f5d5fe0cf00f6dd0322fbddae510f687b53c22 -->

SKW implements this contract for typed generation-context References, including
local object-index References and indexed objects that are themselves
References. Loading types the declarations without following their targets;
the bound Check and operations that consume context perform resolution. Existing
reading and loading Checks retain ownership of their own graph edges.

## Project checks: one entry point

A project's tests, in the general sense of checks over the whole project and
not only its code, need one standard place to run, like the tests folder of a
programming language. Linter, checker and test mean nearly the same thing
here; the only semantic is that whatever is put behind the entry point runs
when someone asks for the project's checks. This is Tarav-level, not specific
to one project.
<!-- tarav.breadcrumb 731023327b76c5795a10310b14a052f06988ef6ef5d54ff7caa8f265b59d160d -->
<!-- tarav.breadcrumb 06e735d5e9d501945f9a448731cc25131f016c539ebaa11c439713d3492d02d8 -->

The User chose the name "project checks", not "project tests": every Project
class has a check method that subtypes implement using Tarav's existing Check
and POI primitives. Request
[858](../../../tarav-py/notes/live/858-project-checks-entry-point-impl-req.md)
implemented `TaravProject.check()` (the base raises `NotImplementedError`),
`check_report()`, and `tarav check --project [PATH] [--json]`, which runs
`check()` inside the Project's harness so the Project's own Type is bound.
Selection and cost profiles are not part of the contract yet. md-library and
g70203 do not implement `check()` yet.
<!-- tarav.breadcrumb a214e2894149433f5aca17627bc136be9458184e6cf69aedf76963d68cf860e8 -->
<!-- tarav.breadcrumb 605949b03256233830c468abff2d030266009473e2dcbb57067263a10f4ec37e -->

## The suite holds its run — 2026-10-12

`CheckRun` no longer exists. A suite is a class that holds the code that
runs checks and the results of its one run; it can run filtered, and it has
an identity. The reasons and the consequences for actions are in
[POI visibility, navigation, and blessings](poi-system.md), section "Suites
are detectors that hold their run".
<!-- tarav.breadcrumb f626b0a4e9fa8030c7078e6e6e3579335a26da2f4840f1d54d4d7b8802d24b13 -->

