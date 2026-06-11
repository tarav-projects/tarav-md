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

****

## RED.GREEN.Test.Suite

- `RED.GREEN.Test.Suite` is the set of RED/GREEN-style tests an `Impl.Req` calls for, written test-first to drive the implementation
- an `Impl.Exec` `Development.Principle`: the `Impl.Req` specifies the suite; the executer builds it test-first — each test goes RED (fails) then GREEN (minimal code passes), one at a time
- never write all tests up front: bulk tests assert imagined shape and pass when behavior breaks
- it is not the only tests — it is the implementation-driving core; more tests may be added later, including at the end
- `No.Regression.Tests.Allowed` governs all tests including this suite — keep it core-feature, e2e, and durable-contract focused, not regression slop
- `Test.At.Boundaries` governs what each test asserts — public behavior that survives a refactor
- rationale: writing the test before the code prevents retrofit tests that merely rubber-stamp the implementation

****

## Alignment.Mode

- `Alignment.Mode` is an argument accepted by hugentic skills: its name is `Alignment.Mode`, its type is the value enum below
- it governs one axis only — the `Alignment.Checkpoint` axis: who resolves each declared checkpoint
- `Interactive` (default) — checkpoints are alignment opportunities; the agent may prompt the user at each
- `Autonomous` — no user prompting; the agent carries the process and resolves every checkpoint itself
- it is one skill axis, not a global control model — a skill may carry other independent axes
- a caller wanting "autonomous within a phase, one confirm at a boundary" owns that boundary as its own declared `Alignment.Checkpoint` and invokes downstream skills in `Autonomous`

****

## Alignment.Checkpoint

- `Alignment.Checkpoint` is a declared point in a skill workflow where the agent checks something before proceeding
- it is a checkpoint because it can be an alignment opportunity — a place where the human could meaningfully weigh in
- a decision the agent always resolves alone is not a checkpoint; it is just a normal workflow step
- every checkpoint sits at an explicit declared position; it may carry an optional activation condition deciding whether it fires when reached (e.g. "design did not fit reality") — a gated positional checkpoint, not a separate kind
- the check always runs; `Alignment.Mode` decides who resolves it — `Interactive` may prompt the user, `Autonomous` resolves alone
- checkpoints are declared explicitly, so a skill's alignment surface is inspectable up front
- discipline: the agent must not invent checkpoints and must not stop execution outside a declared one — no ad-hoc halts
- deviation (design-reality mismatch) is handled at a declared checkpoint via an activation condition, not as an anywhere-interrupt
- `Alignment.Checkpoint:<Name>` names a specific checkpoint, such as `Alignment.Checkpoint:Readiness`

****

## Alignment.Checkpoint:Readiness

- `Alignment.Checkpoint:Readiness` is a named `Alignment.Checkpoint` placed right before the `Impl.Req` is written, after research and understanding
- its purpose is a final alignment pass at the point of maximum understanding: the agent asks for whatever it still needs to produce a good `Impl.Req` — design clarifications, missing feedback loops, missing inputs — not only design questions
- it is a gap-detector and needs gate, not a documentation mandate — it must not bloat the `Impl.Req`
- bounded: the user stays in-loop as long as they want; then the agent finishes the `Impl.Req` with all accumulated feedback
- governed by `Alignment.Mode` like any `Alignment.Checkpoint`
- its operational definition — the readiness checklist and the resolve-then-raise flow — lives by construction in the skill that declares the checkpoint, not here

****

## Alignment.Checkpoint:Executable

- `Alignment.Checkpoint:Executable` is a named `Alignment.Checkpoint` the executer runs at execution entry, before the git checkpoint and first edit
- it confirms the `Impl.Req` is still executable in the current environment: targeted files and symbols exist, named feedback loops run, the code matches the plan's assumptions, and the plan is followable cold
- it complements `Alignment.Checkpoint:Readiness` — readiness asks "is this a good plan to write?" at design time; executable asks "is this still runnable now?" at execution time, catching drift since the `Impl.Req` was written
- governed by `Alignment.Mode`: `Interactive` raises unresolved mismatches before editing; `Autonomous` records them and proceeds only if faithful, aborting if the plan is no longer executable
- it is a light "still executable?" gate, not a re-run of the readiness checklist; its operational definition lives in the executer skill that declares it

****

## Name.As.Index

- `Name.As.Index` is the property that a `Dotted.Name` is a bidirectional key across all surfaces, not only a forward pointer to a definition
- forward: name → its `Kernel.Block:Index` definition
- reverse: name → every surface that mentions it — the mention registers that text as being about the concept
- makes natural-text surfaces findable and indexable by concept through plain search, with no hand-maintained concept→surface table
- makes `Cited.Duplication` maintainable: enumerate mentions to detect and align drift — the mechanism `Index.Writer.Maintenance.Pass` already relies on
- the `Soft.Programming.Language` symbol resolves both ways: name→definition and name→usages
- depends on `Dotted.Notation` discipline — only named concepts are reverse-findable; casual prose is not

### meta

- related: `Dotted.Notation`, `Cited.Duplication`, `Inline.Relatedness`, `Index.Writer.Maintenance.Pass`, `Soft.Programming.Language`

****

## Not.A.Wall.Of.Text

- `Not.A.Wall.Of.Text` is an alignment anti-pattern: presenting too much un-aligned content in one turn
- alignment is per-chunk — a wall forces the human to rubber-stamp or disengage (false convergence)
- soft budget ≈ 1–3 blocks / one decision per `Alignment.Maintenance.Turn`
- bounds breadth presented, not depth available — depth stays one pull away (`Appendix.Discovery`)
- exception: content the user explicitly pulls (a requested status print, async artifact) is not a wall

### meta

- related: `Alignment.Maintenance.Turn`, `Hugentic.Alignment`, `Appendix.Discovery`
