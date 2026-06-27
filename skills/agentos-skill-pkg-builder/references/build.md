# agentos-skill-pkg-builder --build

Run the package's derivation relations forward — make each derived span match its source, reconciling drift.

The builder never generates a surface from scratch. Every target already exists; building means reconciling it with its source. See `references/derivation.md` for the manifest and rule format.

## Inputs

- all manifests in `build/derivation/` (or one, with `--manifest`)
- narrow to one runnable file with `--target`

## Pass

1. Load the manifests — each is a `Kernel.Note` of `Derivation.Rule` blocks.
2. For each rule, resolve the source — a `Dotted.Name` block via the index, or a file span.
3. Locate the target span by the rule's locator-hint over the surface's own structure (heading, code fence, `Dotted.Name`) — read the file and find it by common sense.
4. Apply the op: `copy` (verbatim), `projection` (the named structural part), `transform` (reshape by the stated intent).
5. Reconcile only the derived span; leave surrounding hand-written content intact.

## Discipline

- never plant markers or bookkeeping in the runnable surface — addressing is the build side's job
- one owner per target span; if two rules claim it, stop and report the collision
- writing a runnable surface is gated — propose the reconciliation, get approval, then write
- if a locator resolves to zero or several spans, report it instead of guessing
