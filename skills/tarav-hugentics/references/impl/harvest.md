# Implementation Harvest Workflow

Load this module only for `--impl --harvest` or `--impl-harvest`.

Harvest banks the implementation work that is ready now and parks what still
needs design. It selects one coherent candidate and routes it through Develop;
it does not design or edit by itself.

## Readiness Judgment

Readiness is a ranking rather than a mechanical classifier:

- **touched** — the candidate rests on actual User decisions, corrections, or
  requests, not only an Agent summary;
- **clear** — remaining choices are ordinary implementation details rather
  than unresolved User-facing design variables; and
- **grounded drift** — current product evidence shows a concrete mismatch with
  that touched material.

When uncertain whether a User decision remains open, park the candidate.

## Scan

Build candidates from the intersection of:

- the current conversation and relevant Project Model material; and
- current implementation evidence and available POIs.

Each candidate is one coherent implementation unit with an observable result:
the scope suitable for one live-note Impl.Req and one `Impl.Req.Block`.

## Candidate Checkpoint

In Interactive mode, present the best-ready candidate, why it ranks highest,
and the parked runners-up with their unresolved questions. Wait for the User to
approve, redirect, or reshape the selection.

In Autonomous mode, select the top-ranked candidate, retain the ranking and
parked set in the produced live note, and continue without a checkpoint.

## Delegation

Pass the selected candidate and its exact User-Touched provenance to
[`develop.md`](develop.md) under the same `Alignment.Mode`. Do not replace the
supporting conversation and Diagram references with a free-standing summary.

Select one candidate per run. The parked set remains visible design backlog;
it is not silently discarded.

## Completion

Report the selected candidate, why it was ready, the resulting Impl.Req path
and Block, the implemented result, and the parked candidates.

