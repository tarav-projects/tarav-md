> $kw: ^implementation-practices-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract

# Implementation.Practices.Knowledge.Module

Apply these practices on every implementation task.

## Before Editing

- Read the target files first.
- Match existing codebase patterns instead of introducing new conventions.
- Check related tests, types, and consumers before changing an interface.

## Writing Code

- Implement the minimum change that satisfies the request.
- Prefer editing existing files over creating unnecessary surfaces.
- Avoid abstractions for a single use case.
- Validate at system boundaries.
- Add comments only where logic is not self-evident.

## Moving Forward

> $kw: --derived --from No.Legacy.Allowed
> --intent the principle as per-change execution practices: replace
> --cont within scope, no shims or legacy fallbacks unless requested

- Do not add compatibility shims, legacy fallbacks, or migration behavior unless explicitly requested.
- Replace superseded behavior within scope instead of preserving it "just in case."
- Update tests to the accepted design rather than retaining obsolete behavior.
- Avoid feature flags and unrelated refactors.

> $kw. end

## After Each Change

- Run the immediate feedback loop.
- Review the diff for unrelated scope.
- Check that existing behavior outside the intended change remains intact.

> $kw: ^defect-owes-a-test
> --note [DC] a defect found by hand owes the suite a test, because a wrong system with a green suite means the test is missing ^d20260819-32u

- **A defect found by hand owes the suite a test.** A wrong system with a green suite does not mean the suite passed; it means the test is missing. Fixing the line and moving on leaves the constraint the defect revealed unguarded.
- The test asserts the constraint, not the incident: what the defect proved must always hold, stated so the next violation of it also fails.
