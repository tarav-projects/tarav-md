# Authority Drift Checks

Check whether durable design truth is drifting outside `Agentos.Index.Notes`.

## Surfaces To Inspect

- `AGENTS.md`
- `skills/`
- `notes/live/`
- `notes/index/`

## Agentic Check

If `notes/index/` exists, durable design truth should converge there.

Look for evidence that another surface is becoming an independent design source of truth:

- `AGENTS.md` contains extensive durable concepts rather than local agent guidance
- skills define major project concepts not present in `notes/index/`
- live notes are repeatedly used as current authority after a design has stabilized
- usage or workflow surfaces introduce rules that conflict with index notes

## Evidence Standard

Do not make broad accusations.

A finding should cite:

- the surface
- the specific durable-looking rule or concept
- the expected index location or missing registry concept
- why this looks authoritative rather than local guidance

## Expected Findings

- `warn`: durable design truth appears to live only outside `notes/index/`.
- `warn`: derived surface conflicts with an index note.
- `info`: derived surface correctly routes to index notes.
- `skip`: no index surface exists, so authority model is not adopted.

