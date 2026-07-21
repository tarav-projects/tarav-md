# Surface Alignment Drift Checks

Check whether design knowledge is drifting outside its `Natural.Placement` in the index/appendix system.

## Surfaces To Inspect

- `AGENTS.md`
- `skills/`
- `notes/live/`
- `notes/index/`

## Agentic Check

If the index is adopted, design knowledge should converge toward `Kernel.Block::Index` and `Kernel.Block::Appendix` through promotion.

Look for evidence that another surface holds design knowledge that belongs in the index:

- `AGENTS.md` contains extensive durable concepts rather than local agent guidance
- skills define major project concepts not present in the index
- live notes are repeatedly used as current design surfaces after a design has stabilized
- usage or workflow surfaces introduce rules that conflict with index blocks

## Evidence Standard

Do not make broad accusations.

A finding should cite:

- the surface
- the specific durable-looking rule or concept
- the expected index location or missing concept
- why this looks like displaced design knowledge rather than local guidance

## Expected Findings

- `warn`: design knowledge appears to live only outside the index.
- `warn`: derived surface conflicts with an index block.
- `info`: derived surface correctly routes to index blocks.
- `skip`: no index surface exists, so placement model is not adopted.

> $kw: --from Natural.Placement
