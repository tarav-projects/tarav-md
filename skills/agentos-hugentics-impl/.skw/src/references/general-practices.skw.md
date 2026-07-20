# General Implementation Practices

Apply these practices on every execution task.

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

> $kw: derived --from No.Legacy.Allowed
> $kw. --intent the principle as per-change execution practices: replace
> $kw. within scope, no shims or legacy fallbacks unless requested

- Do not add compatibility shims, legacy fallbacks, or migration behavior unless explicitly requested.
- Replace superseded behavior within scope instead of preserving it "just in case."
- Update tests to the accepted design rather than retaining obsolete behavior.
- Avoid feature flags and unrelated refactors.

> $kw. end-derived

## After Each Change

- Run the immediate feedback loop.
- Review the diff for unrelated scope.
- Check that existing behavior outside the intended change remains intact.
