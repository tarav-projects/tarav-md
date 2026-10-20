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
<!-- tarav.breadcrumb ff5b0b1ced92 -->

The Python implementation moved concrete providers and maintained callers to the namespace. See [Impl.Req 866](../../../tarav-py/notes/live/866-project-capability-paths-impl-req.md).
<!-- tarav.breadcrumb 75b5f7a7bdba -->


Tarav should provide a workflow for defining and running checks, so each
type or workflow does not need to build its own engine. The structural checks
for [Reader.Context.Path](reader-context-path.md) should use this shared
interface. The existing [POI system](poi-system.md) is itself work in progress;
define the minimal interface and mechanics needed for this use case rather
than treating its current implementation as a fixed contract.
<!-- tarav.breadcrumb acd062a9d8f4 -->
<!-- tarav.breadcrumb 7a0d1da62f6d -->

## Check and CheckProvider

Check types define reusable checking behavior. A `CheckProvider` exposes
checks appropriate to its subjects, through an interface such as `obj.checks`.
Objects can opt into that capability by subtyping the provider base; checks
can be supplied at object, type, or workflow level. Check classes can be
instantiated wherever needed. These are design contracts; the exact collection
API and implementation remain to be defined.
<!-- tarav.breadcrumb a133c03ad07b -->
<!-- tarav.breadcrumb 797985d00c87 -->

Providers instantiate appropriate checks; runners and linters select,
execute, and aggregate them. A linter can collect checks from the objects it
inspects and also construct checks involving multiple subjects that do not
naturally belong to either subject alone. Explicit check pools remain valid.
Definitions and construction should live where their semantics fit best,
while all these sources share the same Check contract.
<!-- tarav.breadcrumb b71fbe6c34fb -->
<!-- tarav.breadcrumb 14925d370e38 -->

## Targeted execution

Checks must be usable independently: instantiate and run a single check,
run the checks exposed by one object, or combine selected checks into a
larger run. Quick and targeted experiments do not require a linter or a
larger workflow. A linter adds selection, orchestration, and reporting around
checks that are already runnable on their own.
<!-- tarav.breadcrumb 7ebc9a1a131a -->
<!-- tarav.breadcrumb 133aeeeca5db -->

## Candidate organization

The agent proposed `tarav.l1.checks` for the common interface, results and
runner, using `tarav.l1.poi` for findings; reading-path declarations would
remain in `tarav.l1.skw.skills`, with concrete shared-interface checks in
`tarav.l2.skw.skills.checks`. This is a proposed package arrangement, not an
inspection of existing APIs. Likewise, `CheckResult`, a bound check collection,
and distinguishing execution failure from a completed check with no findings
are proposed MVP details, not yet finalized schemas.
<!-- tarav.breadcrumb 91edfb2ad3ad -->
<!-- tarav.breadcrumb c067491fc24d -->

## CheckResult as a POI provider

A Check executes and produces a CheckResult. The result contains or can
access everything needed to produce its POI instances, while retaining any
additional data the Checks workflow needs for its own purposes. Model it as
a POI provider. There must not be a parallel finding type duplicating POIs:
the objects describing check findings are POIs themselves. "Finding" can
remain a descriptive name for those POIs.
<!-- tarav.breadcrumb 54e3ca427f15 -->

POIs are a central communication surface for agents and carry the contextual
information needed to investigate an occurrence. A CheckResult can remain
lighter than that agent-facing representation. Producing a POI and raising
it are distinct operations; the raising mechanics and semantics belong to
the POI workflow. Checks integrate with that workflow rather than defining
their own raising system.
<!-- tarav.breadcrumb a4cbea50df39 -->

The resulting design is Check → CheckResult (POI provider) → POI instances
→ raise through POI mechanics. The agent proposed a reusable `POIProvider`
interface owned by the POI workflow, with results either retaining or
constructing POIs when requested. Exact method names, storage, and raising
policy remain open; illustrative `pois()` and `raise_()` calls are not claims
about implemented APIs.
<!-- tarav.breadcrumb 7d28f24f3c1a -->
<!-- tarav.breadcrumb b39c8a6102a3 -->

## POI integration refinement — design

Checks and POIs are the fundamental objects for audit integration. A
CheckProvider is optional: its role is to expose checks from a subject, not
to be a prerequisite for constructing and running a Check directly. The
Check class provides an inspectable explanation of its produced CheckPOIs.
The Checks and POI systems can co-evolve to fit the audit rather than forcing
the audit into an unsuitable workflow.
<!-- tarav.breadcrumb df023e7b391b -->
<!-- tarav.breadcrumb 4a2fab9f4e4e -->

The proposed `CheckPOI` belongs with Checks and inherits the general POI base.
`NotificationPOI` covers visible operations such as appending a Breadcrumb
location observation, without inventing a Check for that notification. POIs
are neutral points of interest. Checks raise failure POIs by default, but
that convention does not make every POI negative. See
[POI semantics](poi-system.md#points-of-interest-not-inherently-problems).
This refinement is not yet an implementation report.
<!-- tarav.breadcrumb e4feaf5014ae -->
<!-- tarav.breadcrumb 7d97e92fff9e -->
<!-- tarav.breadcrumb bd34277c6e9b -->
<!-- tarav.breadcrumb 5c615d4bc867 -->

## Implemented foundation — 2026-09-30

`tarav.l1.checks` now provides `Check`, `CheckProvider`, `CheckResult`, and
`run_checks`. A Check can run alone; a result snapshots its data and POIs.
Inspecting `result.pois()` emits nothing. The consumer may explicitly emit a
POI to a collector or invoke the POI's `.error()` method. SKW supplies three
reading checks through `SkwSkill.checks` and uses their results for its CLI
POI report. See the [Checks code](../../../../tarav-py/src/tarav/l1/checks/__init__.py)
and [SKW integration](../../../../tarav-py/src/tarav/l2/skw/reading_checks.py).
<!-- tarav.breadcrumb 5922aa58ced6 -->

## SituationCheck

SituationCheck is an optional Check specialization that evaluates only a
situation supplied before execution. Any additional data required by evaluation
must first be captured in that situation. The flow is Situation → Check → POI:
detection and POI identity share the same description, rather than independently
selecting inputs that can disagree.
<!-- tarav.breadcrumb d052cf7a461c -->

Use a general Situation based on LiteRecord; a new situation class for every
check is unnecessary. Specialized checks may define their own situation types
when stronger constraints are useful. Objects can collect their situations and
provide bound checks, but this organizational choice does not forbid direct
construction or other integrations between workflows.
<!-- tarav.breadcrumb 105eb9e02597 -->
<!-- tarav.breadcrumb 2737f2770664 -->

Retain the current iterable `obj.checks` property. Named selection is deferred.
[Request 835](../../../tarav-py/notes/live/835-situation-checks-impl-req.md)
implemented the common mechanics and a bounded SKW freshness integration.
<!-- tarav.breadcrumb 14021d78efd3 -->
<!-- tarav.breadcrumb 5c45c5dcc0dd -->

A Situation defines the scope of acceptance: changing any field may produce a
new POI identity and require another blessing. Situation descriptions need not
be minimal; extra fields may deliberately favor conservative resurfacing.
Separate bound checks should represent independently assessable concerns.
<!-- tarav.breadcrumb c2d9df1ece09 -->

`SituationCheck` snapshots and validates its input, exposes it through context,
and rejects a returned `CheckPOI` whose situation differs. SKW now creates
separate generation-input and tracked-context freshness checks before running
them, so evaluation does not reread mutable external inputs.
<!-- tarav.breadcrumb da3da29ce021 -->

## Reference resolution Checks

A declared Reference can expose an independently runnable Check without a
freshness baseline. Successful resolution produces no failure POI. A broken or
currently unavailable target produces a CheckPOI that retains the declaration,
its owning coordinate, and the available failure reason. This keeps resolution
visible when dependent freshness cannot construct its own situation.
<!-- tarav.breadcrumb 3aa317a1b227 -->
<!-- tarav.breadcrumb 0ce78f0cbbc4 -->

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
<!-- tarav.breadcrumb 731023327b76 -->
<!-- tarav.breadcrumb 06e735d5e9d5 -->

The User chose the name "project checks", not "project tests": every Project
class has a check method that subtypes implement using Tarav's existing Check
and POI primitives. Request
[858](../../../tarav-py/notes/live/858-project-checks-entry-point-impl-req.md)
implemented `TaravProject.check()` (the base raises `NotImplementedError`),
`check_report()`, and `tarav check --project [PATH] [--json]`, which runs
`check()` inside the Project's harness so the Project's own Type is bound.
Selection and cost profiles are not part of the contract yet. md-library and
g70203 do not implement `check()` yet.
<!-- tarav.breadcrumb a214e2894149 -->
<!-- tarav.breadcrumb 605949b03256 -->

## The suite holds its run — 2026-10-12

`CheckRun` no longer exists. A suite is a class that holds the code that
runs checks and the results of its one run; it can run filtered, and it has
an identity. The reasons and the consequences for actions are in
[POI visibility, navigation, and blessings](poi-system.md), section "Suites
are detectors that hold their run".
<!-- tarav.breadcrumb f626b0a4e9fa -->

## Named completion checkpoints — 2026-10-20

A suite may finish while one conditional producer never scanned for its Checks.
For dynamic findings, the User wants named checkpoints placed after the scan
and returned by the suite run. The checkpoint is the local assertion that the
suite reached that producer; zero generated Checks has meaning only when this
assertion is present. An absent POI can take an Action's `gone` path only when
the checkpoint responsible for that Check Type was reached and its executed
Checks completed. A skipped scan leaves the Action open as `not run`.
<!-- tarav.breadcrumb ac4d808fc231 -->
<!-- tarav.breadcrumb 989482cffd36 -->

In [request 938](../../../tarav-py/notes/live/938-suite-checkpoints-impl-req.md),
`CheckSuite` declares the Check Types certified by each named checkpoint and
its producer yields `SuiteCheckpoint(name)` after the scan. The run records
which names it reached. The Action event retains the relevant checkpoint; the
current suite declaration also governs an already-open Action whose event was
created before that declaration. Focused tests cover a skipped scan, a failed
Check, an empty completed scan, reset, and sibling suite isolation.

