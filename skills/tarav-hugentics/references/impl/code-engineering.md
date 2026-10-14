# Code Engineering

Load this module for every implementation phase that designs, reviews, or
changes product code. It owns the code method: how a change is shaped, sliced,
written, and proven. The phase module keeps the knowledge surface, live note,
Breadcrumb capture, Wiki capture, and evidence commits; nothing here replaces
or relaxes those contracts.

Named practices are steering vocabulary. When one shapes a decision, name it
and the choice it changed in the live note or report.

## Before Editing

- Read project and target-area instructions first.
- Inspect the target files, tests, types, consumers, and worktree before
  changing an interface.
- Match established codebase patterns unless the accepted design changes them.
- Confirm that targets still exist and planned checks are runnable.

## Shaping the Change

Settle these during Design and record them in the Execution.Plan:

- **Data shape first.** Name the core types, records, and structures before
  any logic, and trace their dominant access paths. Encode repeated rules in
  one structure, such as a typed model, state machine, registry, or
  discriminated union, instead of scattered conditionals. Do not force an
  abstraction onto code that is already clear, local, and unlikely to grow.
- **Subtract before adding.** Name the dead code, obsolete paths, and
  redundant surfaces the change can delete, and sequence that removal before
  construction.
- **Boundary discipline.** Validate, parse, and handle errors where data
  crosses a system boundary, such as CLI arguments, files, and external APIs.
  Trust typed data inside. Keep logic in functions the shell only calls.
- **Work kind.** Classify each slice as feature, bug fix, refactor, or
  performance work; each kind carries its own proof below.

## Vertical Slices

Plan the work as ordered vertical slices. Each slice delivers one observable
result, ends in a check that can be rerun, and leaves the product in a
known-good state. Do not advance past a slice whose check is red.

Order slices so the sequence argues for the change: a failing check before its
fix, a removal before the reshape, a baseline before the treatment, and shared
scaffolding such as types or test fixtures before the features that use it.

A plan is ready for execution when:

- scope and out-of-scope are explicit;
- current product state was inspected and cited;
- the core data shape is named;
- every slice has a work kind, an observable result, and a check;
- dependencies, ordering, risks, and deviation triggers are explicit; and
- no unresolved User decision is hidden inside an execution step.

Close gaps yourself where possible. Do not pad the plan merely to satisfy the
list.

## Writing Code

- Implement the minimum coherent change that satisfies the request.
- Prefer existing surfaces over new abstractions; three similar statements
  beat a premature abstraction.
- Prefer simple, flat, and explicit data flow. Keep units focused and
  dependencies justified.
- Name things for what they do or hold and follow repository conventions.
- Add comments only where the reason is not self-evident.
- Do not add compatibility shims, legacy fallbacks, migrations, feature flags,
  or unrelated refactors unless the request requires them. When a new internal
  API replaces an old one, migrate its callers and delete the old API in the
  same change.
- Prefer design elements supported by more than one independent reason.
- Prefer claims that are cheap to check; shape producer output so the checker
  can remain simple.
- Point to precise source surfaces instead of storing descriptions of facts the
  code already computes. Explain why a constraint exists; let the code show
  what it does.

## Slice Loop

For each slice, in Execution.Plan order:

1. Read the exact target surfaces.
2. Establish the failing or baseline evidence that the slice's work kind
   calls for.
3. Make the minimum coherent change.
4. Run the slice check and the relevant existing tests.
5. Review the diff for unintended scope and verify that behavior outside the
   intended change remains intact.
6. Record the check and its observed result.

The phase module places its capture steps around this loop. Do not write all
tests up front; keep every slice independently observable and reviewable.

## Proof by Work Kind

- **Feature.** Prove the new behavior through the surface its users call.
- **Bug fix.** Reproduce the defect first, on the surface where it occurs.
  Trace it to its root cause by forming hypotheses and eliminating them with
  runtime evidence; instrument rather than guess. Fix the cause, not the
  symptom: a guard that silences the failure is not a fix. Where a cheap local
  test path exists, write the regression test first and confirm that it fails
  for the intended reason before fixing. Look for the same pattern elsewhere.
  A change the evidence did not justify does not ship.
- **Refactor.** Preserve behavior. Establish passing checks before the change
  and show that the same checks pass after it.
- **Performance.** Capture a baseline before the change. Before trusting a
  measured number, name what limits it and rule out that it measured
  something other than the intended work.

## Proving It Works

- Verify the real artifact through its real surface. A successful build, an
  agent self-report, or derived state is not proof of behavior.
- Prefer a scripted check a reviewer can rerun over a one-time inspection.
- An inconclusive check, or a check on the wrong surface, is not a pass;
  report it as such.
- When a check fails unexpectedly, suspect the observation method before the
  system.
- Label each claim about behavior as measured, inferred, or a guess.

## Tests

- Test durable public behavior: call the subject the way its users do with a
  concrete input and assert the literal expected result or effect.
- Rewrite or delete a test that would still pass if the subject returned
  nothing or a wrong value, such as loose truthiness checks, call-only
  assertions, expected values computed by the subject, or restated constants.
- Prefer no new test over a bad one: one that mostly tests mocks, depends on
  timing or global state, or needs expensive infrastructure for a small fix.
  Use the closest executable check instead and say why.
- Do not change a test to match a wrong implementation, or weaken an
  assertion without a stated behavioral reason.
- A defect found manually owes the suite a test for the durable constraint it
  revealed, not merely for the one incident.

## When Fixes Fail

When two fixes that share one assumption fail the same check, stop fixing.
Write down the assumption every failed fix made, gather evidence about it, and
question it before the next attempt. Record the premise and its evidence in
the implementation log.

When the same correction recurs, prefer encoding it as a type, check, or
script over adding another instruction.

## Reporting Evidence

Report evidence, not only outcomes. Name each check, what it showed before the
change when the work kind requires that, and what it shows after. When
failing-before evidence could not be produced, say why and name the closest
check used instead.

