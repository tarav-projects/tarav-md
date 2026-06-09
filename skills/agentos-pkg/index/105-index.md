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

****

## Kernel.Block:Grounding

- `Kernel.Block:Grounding` is the standard `### grounding` section of a kernel block
- it is the block-local expression of a `Chat.Grounding` relationship
- it sits alongside fundamentals, `### appendix`, and `### meta` as a normal block section
- it groups `Grounding.Entry` rows by lightweight role labels
- `*HEAD*` marks active current grounding for the block
- multiple `*HEAD*` rows are allowed when several chat refs jointly define the current view
- historical grounding belongs in appendix depth, not compressed index grounding

****

## Grounding.Entry

- `Grounding.Entry` is one citation row inside `### grounding`
- it resolves to one direct `Chat.Ref`
- it includes a short evidence note explaining what the cited chat establishes for the block
- its grounding role comes from the group it appears under
- `*HEAD*` entries identify active chat evidence still considered current for the block
- historical entries are placed in the block's appendix surface, not compressed index grounding

****

## Grounding.DRIFT

- `Grounding.DRIFT` is an explicit marker that a grounded block needs alignment discussion
- it only marks `*HEAD*` grounding rows
- it signals that alignment must be performed on this block/grounding
- it does not encode the drift reason; the evidence note carries the reason
- its canonical form is a `DRIFT:` prefix on the affected `*HEAD*` row
- the resolution happens on `Chat.Surface` and can become the new `*HEAD*` grounding

****

## Grounding.History

- `Grounding.History` is accumulated older chat evidence for a grounded topic
- it belongs in the topic's appendix surface
- it preserves alignment evolution, rejected directions, superseded views, and drift resolutions
- it does not override `*HEAD*` grounding in the index block
- it can grow freely under appendix constraints

****

## Grounding.Context.Injection

- `Grounding.Context.Injection` is selected prior chat context made available through grounded kernel blocks
- the citation is the durable pointer; the injected context is what improves current agent judgment
- injection happens by loading a grounded index/appendix block in a workflow that needs its evidence
- injected context should be relevant enough to affect judgment, not merely adjacent
- grounded blocks make prior work reusable without requiring the user to re-explain settled context

****

## Grounding.Retrieval.Boundary

- retrieval finds candidate chat evidence
- grounding selects and cites accepted evidence on a kernel block
- retrieval quality affects grounding quality, but retrieval mechanics are not the definition of grounding
- search engines, vector databases, keyword indexes, and session queries are candidate-discovery mechanisms
- grounding does not depend on a specific retrieval backend

****

## Topic.Identity

- `Topic.Identity` is kernel block identity in the index/appendix system
- a grounding topic is a `Kernel.Block:Index` or `Kernel.Block:Appendix` subject
- if a subtopic inside a block needs independent grounding, it should become its own kernel block
- `Topic.HEAD` is scoped to one grounded kernel block topic
- other surfaces cite grounded blocks instead of inventing separate grounding topics

****

## Topic.HEAD

- `Topic.HEAD` is the most recent grounded chat view for a topic
- the topic is the identity of a grounded index/appendix kernel block
- it is the grounding anchor for the block's current user/agent alignment state
- drift is measured against `Topic.HEAD`, not against every older grounded chat
- older grounded chats remain useful history, but do not override the current view
- `Topic.HEAD` can be updated by finding a more recent grounded chat or by discussing the topic again in chat

****

## Designer.Turn.Kernel.Form

- `Designer.Turn.Kernel.Form` is how a `What.Design.Session` turn is shaped when working a defined subject
- the designer communicates in `Kernel.Writing` — orthogonal bullet lines, each an independent fundamental point, direct language
- a turn working a defined subject proposes a `Kernel.Block:Design`: an H2 `Dotted.Notation` heading, orthogonal fundamentals, and an optional `### meta` for open items
- a question turn pairs the block with the question — the `Kernel.Block:Design` as actionable intro, then `Question / Why-now / Recommended-answer / Evidence`
- every new question on a defined subject is accompanied by its block; pure openers are exempt because they create the first subject
- discussion rounds re-render the same block with the change; open points live under `### meta` as `open:` lines
- the in-chat block and the artifact's `Design.Index` block are one object — capture only adds gating

### meta

- related: `Kernel.Writing`, `Kernel.Block:Design`, `Alignment.User.Turn`, `What.Design.Session`
