# agentos-skill-pkg-builder --import-checks

Report whether each declared `Module.Import` still holds. Read-only — never writes. See `references/imports.md` for the manifest and block format.

## Inputs

- all `build/*-imports.md` manifests in the package (or one, with `--manifest`)
- narrow to one consumer file with `--target`

## Pass

0. Run the CPU check and take its pointer/copy verdicts as given:

   ```
   agentos skills imports --package <pkg> [--depot <index-depot>]... [--json]
   ```

   It reports every import: `resolved` / `equal` / `drifted` / `unresolvable` / `skipped-agentic`, plus manifest-name problems (no match, ambiguous).

1. For each `derived` import (the `skipped-agentic` inventory), resolve the target, read the current landing span, and judge against `context:` whether the derived span still faithfully transforms the target.
2. Report drift per import: in-sync, drifted (with what changed), or unresolved.
3. Report landing-span collisions — two imports landing on the same span.

## Output

- the CPU report verbatim, then a per-`derived`-import status list, cited by manifest and consumer
- no edits; reconciliation is the `--build` pass
