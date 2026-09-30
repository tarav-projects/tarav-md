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
