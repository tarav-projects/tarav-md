# agentos-skill-pkg-builder --build

Run the package's import relations forward — make each landing span match its target, reconciling drift.

The builder never generates a surface from scratch. Every consumer already exists; building means reconciling it with its imports. See `references/imports.md` for the manifest and block format.

## Inputs

- all `build/*-imports.md` manifests in the package (or one, with `--manifest`)
- narrow to one consumer file with `--target`

## Pass

1. Load the manifests — each is a `Kernel.Note` of import blocks, one per `Module.Import`.
2. For each import, resolve the target — a `Dotted.Name` block via the index depot, or an `@path` file locator with optional `#region`.
3. Locate the landing span by `lands:` over the surface's own structure (heading, code fence, `Dotted.Name`) — read the file and find it by common sense; omitted `lands:` means the whole file.
4. Apply the binding: `copy` lands the target verbatim; `derived` reshapes it by the `context:` intent; `pointer` lands nothing — it only declares the dependency.
5. Reconcile only the landing span; leave surrounding hand-written content intact.

## Discipline

- never plant markers or bookkeeping in the runnable surface — addressing is the build side's job
- one owner per landing span; if two imports land on it, stop and report the collision
- writing a runnable surface is gated — propose the reconciliation, get approval, then write
- if a locator resolves to zero or several spans, report it instead of guessing
