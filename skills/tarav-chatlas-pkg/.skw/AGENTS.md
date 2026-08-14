# .skw — skw Build Surface

- this folder is the skw build surface of the package above it
- the package's skw-managed files are compiled from `src/**/*.skw.md` — NEVER edit those targets by hand
- to change managed content: edit the src file, then run `agentos skw build --skill <package-root>`
- to inspect drift (read-only): `agentos skw check --skill <package-root>`
- `lock.json` and this `AGENTS.md` are engine-owned and overwritten on every build
- for the full skw discipline, load the `tarav-skillware` skill
