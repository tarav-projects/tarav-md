# agentos-skill-pkg-builder --build

Make the package's Skillware-managed surfaces match their sources.

The builder never generates a surface from scratch. Building means compiling the `.skillware/src/` sources and reconciling drift. See `references/skillware.md` for the src and recipe format.

## Pass

1. Run the deterministic compile:

   ```
   agentos skillware build --skill <path>
   ```

   It refreshes `copy` bodies in src, compiles every `.skw.md` to its target, and writes the lock. `derived` bodies pass through as materialized.

2. Run `agentos skillware check`. If it flags `derived-stale` recipes, do the agentic part: re-derive those bodies in src per their `from:` targets and `intent:` (see `references/skillware-checks.md`), then rebuild.

## Discipline

- all work happens in src — never edit a compiled file directly
- src edits are workspace edits; content changes reach the runnable surface only through `build`
- writing to src for a gated package still follows the package's own edit gates — propose, get approval, then re-derive and rebuild
