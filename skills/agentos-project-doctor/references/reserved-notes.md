# Reserved Notes Checks

Check reserved Agentos note surfaces.

## Deterministic Checks

When `notes/live/` exists:

- if a TODO note exists, check that it uses `notes/live/010.TODOS.md`
- if a near-standard TODO note alternative exists, treat it as overlapping live-note behavior
- if an issues note exists, check that it uses `notes/live/011.ISSUES.md`
- if a near-standard issues note alternative exists, treat it as overlapping live-note behavior

When `notes/index/` exists:

- check for `notes/index/001-index.md`

When `skills/agentos-pkg/index/` exists:

- check for `skills/agentos-pkg/index/000-index.md`

## Agentic Checks

- TODO notes are optional. Do not warn when no TODO note exists.
- If a TODO note exists, warn when it does not use the reserved `010.TODOS.md` path.
- Issues notes are optional. Do not warn when no issues note exists.
- If an issues note exists, warn when it does not use the reserved `011.ISSUES.md` path.
- Do not require every project to use live notes.
- Do not inspect TODO content as progress tracking unless explicitly asked.
- Do not inspect issues-note content as issue triage unless explicitly asked.

## Expected Findings

- `fail`: active index exists but reserved routing table is missing.
- `warn`: a TODO note exists under `notes/live/` but does not use the reserved `010.TODOS.md` path.
- `warn`: an issues note exists under `notes/live/` but does not use the reserved `011.ISSUES.md` path.
- `skip`: relevant note surface is absent.
- `pass`: existing reserved notes use the expected paths.
