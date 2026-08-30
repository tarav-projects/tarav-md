# Issue Audit Workflow

This is the read-only `tarav-hugentics --issues --audit` route.

Resolve the Project Model and inspect relevant `Issue.Block` projections. Show
a compact list containing each Issue label, shortened ship UUID, projected
open or closed state, the newest useful Line wording, and relevant POIs.

When a query identifies one Issue, render that Issue and its evidence rather
than listing the whole Model. When no query is supplied, prioritize open Issues
and POIs that are useful to the current collaboration.

Do not bootstrap a missing Model, create a Capture.Manifest, mutate Diagram
records, or advertise approval and landing commands. Audit findings may suggest
a subsequent Parking or Maintenance run, but they do not authorize it.
