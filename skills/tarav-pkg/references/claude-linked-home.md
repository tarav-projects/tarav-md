# Claude Linked Home

Reference for the intended `Linked.Home` pattern used by Claude homes.

## Model

Claude homes may operate as a `Linked.Home` set:

- one base home owns selected shared subcomponents
- other Claude homes link those subcomponents back to the base home
- each linked home keeps its own local state for the parts that should remain separate

## Intended Shared Set

The intended shared set for each Claude linked home is:

- `CLAUDE.md`
- `projects`
- `settings.json`
- `skills`
- `hooks`

## Why Each One

- `CLAUDE.md` is shared so the homes inherit the same durable agent instructions
- `projects` is shared so project-local state and routing stay aligned across homes
- `settings.json` is shared so runtime behavior and local preferences stay consistent
- `skills` is shared so the same imported skill surface is available from every Claude home
- `hooks` is shared so the same command hooks and automation behavior apply across homes

## Boundary

- this reference defines the intended shared Claude subcomponents, not all home contents
- linked Claude homes still keep local state outside this shared set
- this is Claude-specific operational guidance, not the full definition of `Linked.Home`
