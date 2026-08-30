# Implementation Practices

Apply these practices while designing and executing implementation work.

## Before Editing

- Read project and target-area instructions first.
- Inspect the target files, tests, types, and consumers before changing an
  interface.
- Match established codebase patterns unless the accepted design changes them.

## Writing Code

- Implement the minimum coherent change that satisfies the request.
- Prefer existing surfaces over unnecessary new abstractions.
- Validate at system boundaries.
- Add comments only where the reason is not self-evident.
- Do not add compatibility shims, legacy fallbacks, migrations, feature flags,
  or unrelated refactors unless the request requires them.

## Feedback

- Run the immediate feedback loop after each vertical slice.
- Review the diff for unintended scope.
- Verify behavior outside the intended change remains intact.
- A defect found manually owes the suite a test for the durable constraint it
  revealed, not merely for the one incident.

