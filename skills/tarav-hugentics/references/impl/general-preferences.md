# Implementation.Preferences.Knowledge.Module

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

- **Prefer the candidate with more than one independent reason.** A design element that serves several purposes is carved at a joint; one that serves exactly one is fragile — weaken that reason and it becomes ceremony.
- The reasons must be **independent**: each still standing if the others were removed. Otherwise the test degrades into post-hoc defence of whatever already exists.
- Applied in reverse it is a deletion test. An element whose single justification has been absorbed elsewhere is no longer earning its place.

- **Prefer the candidate whose claims are cheap to check.** Verification cost is a design axis, not an afterthought: a design that must be trusted costs more forever than one whose assertions a check can walk.
- A value something else already computes cheaply is not a design variable — it is an uncomputed value, and storing it invents a way to be wrong.
- Where a claim must be asserted, put checkable assertions next to it so the assertion is harder to make than the truth.

- **`Producer.Aids.Checker`: shape the output so the check stays trivial** rather than making the checker clever. Structuring is paid once by the producer; the check then runs cheaply, every time, forever.
- A check that must be smart to be useful is a signal the product is under-structured.

- **Point, do not describe.** A prose description of what code does is a stored copy of a computable fact with nothing asserting it still holds; it drifts silently, and drifted documentation is worse than none because it stops the reader from looking.
- Say *why* the constraint exists — that is nowhere in the code and never will be. Let the body say *what*.
- A pointer only beats a description if it **narrows**: `linter.py:326` costs one read, "read the linter" costs a scan.
