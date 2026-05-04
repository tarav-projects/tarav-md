# Reserved Notes Checks

Check reserved Agentos note surfaces.

## Deterministic Checks

When `notes/live/` exists:

- check for `notes/live/010.TODOS.md`

When `notes/index/` exists:

- check for `notes/index/000-index.md`

## Agentic Checks

- Missing `010.TODOS.md` is a warning only when the project appears to use live notes as an Agentos surface.
- Do not require every project to use live notes.
- Do not inspect TODO content as progress tracking unless explicitly asked.

## Expected Findings

- `fail`: active `notes/index/` exists but reserved index router is missing.
- `warn`: active `notes/live/` exists but reserved TODO note is missing.
- `skip`: relevant note surface is absent.
- `pass`: reserved notes exist for observed active note surfaces.

