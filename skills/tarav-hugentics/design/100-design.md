> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Product.Design.Session

- [DF] `Target.Product` is the intended result that gives design work its purpose ^c20260729-267u
- [CT] a `Target.Product` is identified by its intended outcome rather than by one required artifact kind ^c20260729-54u
- [EX] a design, system, artifact, surface edition, implementation, or decision may each be a `Target.Product` ^c20260729-295u
- [DF] `Product.Design.Session` is an alignment session organized around advancing a `Target.Product` ^c20260729-264u
- [DC] `What.Design`, `How.Design`, and `Impl.Exec` are general concerns available within the session ^c20260729-180u
- [CT] those concerns are not a mandatory three-step pipeline ^c20260729-158u
- [DC] a workflow exposes only the concerns that remain unresolved for its product ^c20260729-191u
- [DC] a concern may already be resolved by `Touched.Data`, a skill contract, or another stable surface ^c20260729-183u
- [FR] resolved concerns may remain implicit while the workflow advances through the others ^c20260729-317u
- [DC] reconciliation may reopen an earlier concern when later work exposes a design gap ^c20260729-226u
- [PR] the concerns form an abstraction gradient without imposing a rigid execution sequence ^c20260729-351u
- [DC] `Touched.Decision.Cycle` governs decisions inside every exposed concern ^c20260729-174u

****

## Hugentic.Capture.Workflow

- [DF] `Hugentic.Capture.Workflow` is the primary user-facing alignment workflow for turning active conversation and adjacent evidence into maintained durable state ^c20260731-201u
- [DC] the workflow may target `Touched.Index`, `Design.Req`, or `Index.Agendix` without changing its conversational loop ^c20260731-185u
- [DC] its general loop contextualizes, proposes and discusses, approves where required, lands through the target surface, and reconciles the resulting state ^c20260731-162u
- [CT] changing the target changes the landing surface and applicable gate, not the identity of the workflow ^c20260731-76u
- [CT] explicit `Batchy.Skill.Flag`s may configure the target or focus, while conversation and declared defaults may resolve rows that permit automatic discovery ^c20260731-80u

****

## Design.Req

- [DF] `Design.Req` is a live artifact for accumulating large or unstable What/How design state before that state becomes suitable for a stable surface ^c20260731-196u
- [PR] it lets extensive design evolve without forcing the main index to absorb unstable material prematurely ^c20260731-235u
- [CT] it is not limited to pairing with an `Impl.Req`; its design may promote into the index, fork into implementation work, or do both ^c20260731-88u
- [DC] its only required lifecycle status values are `Open` and `Closed` ^c20260731-163u
- [CT] while its status is `Open` and its workflow is active, the agent maintains the artifact from the evolving conversation and workflow state ^c20260731-112u
- [CT] completing work requires a maintenance pass that records the resulting design, approvals, promotions, and remaining open material before closure ^c20260731-77u
- [DC] closure is initially user-gated; reopening is permitted, and every later completion repeats maintenance before returning to `Closed` ^c20260731-142u

****

## Design.Req.Promotion

- [DF] `Design.Req.Promotion` is an `Alignment.Loop.Interruptions` branch that temporarily retargets `Hugentic.Capture.Workflow` from a `Design.Req` to the index, an `Impl.Req`, or both ^c20260731-195u
- [DC] the agent may propose landing already-approved material, inspect applicable approved clusters, or continue discussion and approval before proposing the target landing ^c20260731-175u
- [CT] source approval never bypasses the target surface gate; verbatim-preserved material may be reused as a proposal, but its target landing remains separately gated ^c20260731-102u
- [DC] the typical sequence promotes stable design into the index before implementation work begins, keeping product and index surfaces aligned ^c20260731-184u
- [CT] promotion completion includes maintaining the source `Design.Req` to record what was approved or landed before its closing gate is offered ^c20260731-97u
