> $kw: ^implementation-preferences-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract

# Implementation.Preferences.Knowledge.Module

> $kw: --dev-from references/index-context-assembly.skw.md

> $kw: ^preferences-cited-concepts --cite Impl.Req

Apply these preferences across implementation work — while designing an `Impl.Req` as much as while executing one. Several are design decisions the plan commits to, not execution mechanics.

## Simplicity

- Prefer simple over clever.
- Prefer flat over nested.
- Prefer explicit data flow and dependencies.

## Naming And Structure

- Name things for what they do or hold.
- Match repository naming conventions.
- Keep units focused.
- Prefer composition over inheritance.

## Dependencies And Tests

- Do not add dependencies without clear justification.
- Prefer existing or standard-library facilities when adequate.
- Test durable public behavior rather than implementation details.
- Add tests when the implementation design calls for them.

## Design Principles

> $kw: ^convergent-justification
> --note [DF] convergent justification is the property that a design element has several independent reasons to exist ^d20260819-30u

- **Prefer the candidate with more than one independent reason.** A design element that serves several purposes is carved at a joint; one that serves exactly one is fragile — weaken that reason and it becomes ceremony.
- The reasons must be **independent**: each still standing if the others were removed. Otherwise the test degrades into post-hoc defence of whatever already exists.
- Applied in reverse it is a deletion test. An element whose single justification has been absorbed elsewhere is no longer earning its place.

> $kw: ^verification-cost --derived --from Constraint.Steering
> --intent the graded-checkability gradient stated as a design-time
> --cont preference: choose the candidate whose claims something cheap can check

- **Prefer the candidate whose claims are cheap to check.** Verification cost is a design axis, not an afterthought: a design that must be trusted costs more forever than one whose assertions a check can walk.
- A value something else already computes cheaply is not a design variable — it is an uncomputed value, and storing it invents a way to be wrong.
- Where a claim must be asserted, put checkable assertions next to it so the assertion is harder to make than the truth.

> $kw. end

> $kw: ^producer-shapes-output --derived --from Producer.Aids.Checker
> --intent the principle as an implementation-design preference:
> --cont shape the product so its check stays trivial

- **`Producer.Aids.Checker`: shape the output so the check stays trivial** rather than making the checker clever. Structuring is paid once by the producer; the check then runs cheaply, every time, forever.
- A check that must be smart to be useful is a signal the product is under-structured.

> $kw. end

> $kw: ^documentation-points
> --note [DC] documentation points at the implementation rather than describing it ^d20260819-31u

- **Point, do not describe.** A prose description of what code does is a stored copy of a computable fact with nothing asserting it still holds; it drifts silently, and drifted documentation is worse than none because it stops the reader from looking.
- Say *why* the constraint exists — that is nowhere in the code and never will be. Let the body say *what*.
- A pointer only beats a description if it **narrows**: `linter.py:326` costs one read, "read the linter" costs a scan.
