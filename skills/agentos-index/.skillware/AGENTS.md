# .skillware — Skillware Build Surface

- this folder is the Skillware build surface of the skill above it
- the skill's Skillware-managed files are compiled from `src/**/*.skw.md` — NEVER edit those targets by hand
- to change managed content: edit the src file, then run `agentos skillware build --skill <skill-root>`
- to inspect drift (read-only): `agentos skillware check --skill <skill-root>`
- `lock.json` and this `AGENTS.md` are engine-owned and overwritten on every build
- for the full Skillware discipline, load the `agentos-skillware` skill
