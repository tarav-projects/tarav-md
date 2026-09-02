# Issue Workflow Router

This module routes `tarav-hugentics --issues` over addressable
`Issue.Block`s in the Project's configured Diagram.Model. Parking is a
workflow for creating an Issue, not another storage system or Object.Type.

## Routing

Resolve exactly one workflow:

1. `--audit` selects the read-only Audit workflow.
2. `--park` explicitly selects Parking.
3. Input that resolves to an existing `Issue.Block` selects Maintenance.
4. Other actionable input defaults to Parking.
5. With neither input nor actionable conversational context, give a compact
   orientation and stop.

Load only the selected module:

- Parking: [`issues/park.md`](issues/park.md)
- Maintenance: [`issues/maintain.md`](issues/maintain.md)
- Audit: [`issues/audit.md`](issues/audit.md)

## Shared Contract

- Every retained concern is an `Issue.Block`; there is no `Parking.Note`
  Diagram object or separate note store.
- Issues may represent ideas, reminders, questions, opportunities, defects,
  migrations, contradictions, or other temporary concerns.
- The workflow preserves the interrupted foreground task and returns to it
  after a bounded parking operation.
- Issue content is ordinary supported User-Touched capture. A Block
  declaration itself does not require a Support.Set.
- `Issue.Block` owns its allowed Line.Type vocabulary and state projection.
- An Issue is open until its ship contains a passing reviewed
  `Issue.Line.Resolve`. Additional Lines do not stale that resolution.
- An open Issue is valid Diagram state and surfaces an Issue POI; the POI is
  guidance, not a mutation blocker.
- Issue history remains in its Block and Line Ships after resolution.
- Use the shared capture mechanics, Gates, Assertion.Engine, and landing
  contract from [`capture.md`](capture.md). Do not create Issue-specific Tarav
  CLI actions when typed Ship capture already expresses the operation.

## Presentation

When proposing or rendering an Issue, identify its Model, Block label and ship
UUID when known, `Block.Type: Issue.Block`, relevant Line.Types, current
projected state, and visible POIs. Labels aid conversation; UUIDs remain the
mechanical identity.
