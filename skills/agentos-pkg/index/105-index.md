> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Usage.Workflow

- `Usage.Workflow` is a self-sufficient operational doc file for a named usage situation
- each workflow file carries everything an agent needs to operate in that situation — cited duplication from the index is expected
- one file per workflow — adding a workflow means adding a file, not restructuring existing ones
- workflows are independent by default — overlap is accepted and managed through `Cited.Duplication`
- when reuse is obvious and stable, a workflow may load another workflow's file rather than duplicate — but only when the dependency is clear and unlikely to change
- the index is the knowledge accumulator; workflow files are operational projections of that knowledge onto specific situations
- workflow files live in the package's `usage-workflows/` folder
- a workflow file is `Workflow.Neutral` — it informs the agent about how to operate in a situation, the caller decides when to enter it
- discovery: the package `SKILL.md` or relevant `Package.Aux.Skill` lists available workflows with one-line situation descriptions
- each workflow has: a situation trigger (when this workflow applies), the operational knowledge needed, and cited index concepts for grounding
- workflows emerge from real usage — chatlas transcripts, repeated patterns, observed agent friction
- flexibility over efficiency — workflows are append-friendly now, rationalizable later from usage data

### meta

- related: `Package.Skill.UsagePattern`, `Cited.Duplication`, `Natural.Placement:Skills`, `Aux.Workflow.Skill`
