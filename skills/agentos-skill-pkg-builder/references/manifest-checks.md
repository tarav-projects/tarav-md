# agentos-skill-pkg-builder --manifest-checks

Report whether each declared `Derivation.Rule` still holds. Read-only — never writes. See `references/derivation.md` for the manifest and rule format.

## Inputs

- all manifests in `build/derivation/` (or one, with `--manifest`)
- narrow to one runnable file with `--target`

## Pass

1. Load the manifests — each is a `Kernel.Note` of `Derivation.Rule` blocks.
2. For each rule, resolve the source and read the current target span (locate it over the surface's own structure).
3. Compare the current target against what the rule would now produce from the source.
4. Report drift per rule: in-sync, drifted (with what changed), or unresolved (locator matched zero or several spans).
5. Report span-ownership collisions — two rules claiming the same target.

## Output

- a per-rule status list, cited by manifest and target
- no edits; reconciliation is the `--build` pass
