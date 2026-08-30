# Issue Maintenance Workflow

Use this workflow when input resolves to an existing `Issue.Block` or the User
wants to enrich, reconsider, implement around, or resolve an Issue.

## Contextualize

Render the Issue ship, its contributing Lines, support, Assertion standing,
current projected state, and nearby Model context. Expand into supporting chat
material only as needed. Treat the Issue as a temporary organizational surface,
not as the authority behind its content.

## Mutations

Apply changes through ordinary typed Annotation capture:

- add a supported Line when the User touches another relevant facet;
- issue a new Line edition when the semantic lineage continues with changed
  wording;
- attach further support through a support Annotation;
- add or correct Object.Type annotations when needed; or
- propose an `Issue.Line.Resolve` when the User decides the concern is
  resolved.

A Resolve Line must be presented and approved through a passing
`Verbatim.Gate`. An unreviewed or failing Resolve Annotation remains writable
but does not close the projected Issue. Resolving an Issue does not delete or
rewrite its earlier material.

Keep implementation coordination on an `Impl.Req` live note and supported
implementation decisions in its `Impl.Req.Block`. Link or mention the Issue as
context; do not turn the Issue into an Agent-only execution log.
