# Index Reindex — design-session

## Session.Abstract

- intent: rebuild the Agentos Index from scratch using `Index.Block.Syntax`, evolving the conceptual model along the way
- active focus: `Design.Session` concept family — file plan for 121, 122, 123
- references: `517-index-migration-protocol.md`, `513-The.Agentos.Index.md`, `skills/agentos-index/`, `skills/agentos-design-session/`
- state: active
- next: draft `121-Design.Session.md`

## Design.Index

### Index.Migration.Protocol

- `Index.Migration.Protocol` is the operational protocol for the index reindex process
- see `517-index-migration-protocol.md`

#### meta

- status: settled

### Index.Block.Findability

- `Index.Block.Findability` is a field in the `### index` section of an `Index.Block`
- populated only on evidence of search misses, not as a summary of the block content
- during initial block creation, findability should be empty by default

#### meta

- status: settled — promoted

### Reindex.Not.Migration

- this process is a reindex, not a strict migration
- the old index is one source for building the new — `513-The.Agentos.Index.md` is more current
- we do not need to keep the same layout, concept design, or groupings

#### meta

- status: settled

### No.Fixed.Authority.Hierarchy

- the old fixed authority chain (`Md.Surface` → `Canonical.Reference.Implementation` → other impls) is dropped
- when surfaces drift, it is a context-dependent judgment call
- the system aims for alignment, not authority

#### meta

- status: settled — promoted into `Stable.Surface` block

### Ontology.Granularity

- the ontology is a high-level concept map — not every sub-concept needs its own entry
- a parent concept is the entry point; sub-concepts are findable through the note

#### meta

- status: settled

### Stable.Surface.Equal.Authority

- all `Stable.Surfaces` have equal authority — no surface is more important than another
- the index is special in function but not in authority

#### meta

- status: settled — promoted into `100-Agentos.Surfaces.md`

### Context.Minimal.Surface

- `Context.Minimal.Surface` is the set of files from a project that agents must ALWAYS load at session start
- measurable — `Agentos.CLI` can compute total tokens and report breakdown
- creates a budget constraint and optimization feedback loop

#### appendix

Agents have finite context windows — what you preload matters. Too much = waste and unfocused agent. Too little = lost agent that keeps asking questions or making wrong assumptions.

The minimal surface is the "boot sequence" — what the agent loads before it can do anything useful. Keeping it small and high-signal is a maintenance concern.

For Agentos, the minimal surface would likely include: `AGENTS.md` files, `000-index.md`, `001-ontology.md`, `002-surfaces.md`.

Possible CLI: `agentos context minimal`, `agentos context minimal --size`, `agentos context minimal --budget <tokens>`.

#### meta

- status: working — captured in `522`, not yet promoted

### Agentos.Mission.Parked

- `Agentos.Mission` (old source 107) is parked — no longer relevant for the new index
- superseded by Iterante as the coordination layer

#### meta

- status: parked

### Design.Session.File.Plan

- `Design.Session` concept family will be indexed across three files:
  - `121-Design.Session.md` — container: `Design.Session`, sub-concepts: `Session.Runtime.Loop` (`User.Assistant.Turn`, `Session.Maintenance.Turn`), `InChat.Design.Session`, `Artifact.Design.Session`
  - `122-Alignment.Space.md` — container: `Alignment.Space`, sub-concepts: `Design.Alignment.Core`, `Design.Open.Space`, `Delegation.Frontier`, `Alignment.Sufficiency`, `Hard.Evidence`
  - `123-Impl.Req.md` — container: `Impl.Req`, sub-concepts: `Vertical.Slice`, `Deep.Modules`, `No.Legacy.Allowed`, (more later)
- `User.Gated.Trigger` and `User.Gated.Writing` go to `100-Agentos.Surfaces.md` — they are general surface-authority concepts
- old source `111-Design.Session.md` is architecturally stale but its alignment-state concepts are alive
- old Core.Design / TODO.Design split is dead
- `Design.Index` and `Design.Index.Block` stay in `114` — they are index-notes concepts, not Design.Session concepts

#### meta

- status: settled
- evidence:
  - user confirmed gates are general, not Design.Session-specific
  - user chose `100-Agentos.Surfaces.md` as home for gates (option C)
  - user confirmed `Hard.Evidence` belongs in `122`

### Design.Session.Fundamentals

- `Design.Session` is a scoped human-agent convergence surface for design work
- the session does real work (design, problem-solving, issue resolution) while progressively enriching alignment between user and agent
- the interview loop (question → discussion → consolidation) is the fundamental strategy: direct questions produce evidence of alignment, consolidation makes it durable
- the agent maintains session progress and content; the user controls advancement and settles material
- session content aims to be `Hard.Evidence`-based as much as possible — evidence-based arguments have priority over agent assumptions
- the goal is to fill `Design.Alignment.Core` with evidence-based facts — more is welcome, but the core alignment space is the priority
- the interview protocol (one question at a time, agent organizes, user advances, agent recommends) belongs in the parent `Design.Session` fundamentals, not in `Session.Runtime.Loop`
- `Design.Session` is a staging area for `Stable.Surface` changes — session content is expected to become part of stable surfaces through implementation
- the move from design session state to stable surface is the implementation — can happen multiple ways: other agents read the artifact and implement in parallel, session emits `Impl.Req`s, direct surface updates from the session
- not a `Stable.Surface` itself — a strong signal for change that provides a clear substrate to align implementation against
- optimized for high-signal alignment data — can support operational work (migration, triage) when it produces alignment, but should not become a general-purpose work log
- does not replace index notes or skills — those are the destinations

#### meta

- status: settled
- evidence:
  - user confirmed convergence wording
  - user clarified alignment is the method, not the purpose — the session does real work
  - user defined `Hard.Evidence.Based` and its priority
  - user confirmed goals stay in fundamentals, not a separate sub-concept
  - user confirmed staging area framing — design session as strong signal for change, not a stable surface

### Hard.Evidence.In.Meta

- `Design.Index.Block` `#### meta` sections can include an `evidence:` list
- the evidence entries are summary pointers to where the evidence lives, not the evidence itself
- the agent should have access to the evidence and can check it at any time
- format is lightweight and trust-based — no need to be super specific

```md
#### meta

- status: settled
- evidence:
  - user reply (this session)
  - `agentos index doctor` output confirmed no conflicts
```

#### meta

- status: settled
- evidence:
  - user confirmed format and lightweight approach

### User.Gates.Placement

- `User.Gated.Trigger` and `User.Gated.Writing` are general surface-authority concepts, not Design.Session-specific
- they belong in `100-Agentos.Surfaces.md` alongside `Stable.Surface.Equal.Authority`
- Design.Session uses them but does not own them

#### meta

- status: settled
- evidence:
  - user confirmed gates are general
  - user selected option C (`100-Agentos.Surfaces.md`) over Alignment.Space or a new note

### Session.Runtime.Loop.Design

- `Session.Runtime.Loop` is the general workflow the agent tries to make the session follow
- main flow: `Design.Alignment.Question` → `Design.Enrichment.Discussion` → `Design.Consolidation` → ...
- interruptions are named branches that pause the main flow at any point
- `User.Assistant.Turn` — user drives, agent follows (`Design.Enrichment.Discussion` phase)
- `Session.Maintenance.Turn` — agent drives one session move (`Design.Alignment.Question`, `Design.Consolidation`, state update)
- mode switching is user-gated — agent may suggest, never silently switch
- `Design.Status.Report` — structured checkpoint that summarizes session state
  - delta-oriented: reactive to context, don't repeat still-valid reported state
  - serves multiple roles: status checkpoint, consolidation output, session state summary
  - works in both `InChat.Design.Session` and `Artifact.Design.Session`
  - used sparingly at natural consolidation points
  - in InChat sessions, `Design.Consolidation` = printing a `Design.Status.Report`
- `Session.Interruptions` — catalog of named branches the user can take:
  - `Capture.Audit`, `Consolidation.Plan`, `Artifact.Upgrade`, `Impl.Req.Handoff`, `Session.Split`, `Close.Topic`, `Park.Topic`
- the interruption catalog gives the user a vocabulary to communicate with the agent — each name triggers a known response shape
- after an interruption, return to the main flow unless the user chooses another move

#### meta

- status: settled
- evidence:
  - user confirmed framing: main flow + interruptions as branches
  - user named the steps: Design.Alignment.Question, Design.Enrichment.Discussion, Design.Consolidation
  - user promoted Design.Status.Report out of interruptions into Session.Runtime.Loop
  - skill `session-interruptions.md` already catalogs the interruptions operationally

### Design.Session.Backends

- `InChat.Design.Session` and `Artifact.Design.Session` are two backends for the same session
- both run the same `Session.Runtime.Loop` — the backend doesn't change the workflow, only where consolidated state is captured
- upgrade path: InChat → Artifact when state becomes too large, important, or needs future handoff — upgrade is user-gated, never automatic
- `InChat.Design.Session` — default backend
  - the chat is the substrate, the agent organizes it into design-session form
  - flexibility is the priority — no file overhead, no formal sections required every turn
  - the agent must always track session state even when not printing it
  - design state lives across explicit chat turns and strategic `Design.Status.Report` prints
  - can't waste tokens on session organization overhead — the agent needs to actually work
- `Artifact.Design.Session` — file-backed backend
  - state lives in a `*-design-session.md` file
  - durable, handoff-ready
  - adds `Session.Notes` and `Session.Log` to `Session.Abstract` and `Design.Index`
  - artifact writes are user-gated

#### meta

- status: settled
- evidence:
  - user confirmed backends are conceptually clear
  - user defined InChat essence: flexibility, chat as substrate, strategic reports
  - user confirmed Design.Status.Report works in both backends with same properties

### Development.Model.Design

- the Agentos development philosophy is built on four foundational concepts: `Design.Target.Model`, `Current.Implementation`, `Progress.Gradient`, `Design.Implementation.CoEvolution`
- these are upstream of `Design.Session` and upstream of `Surfaces` — they describe how Agentos thinks about development itself
- proposed file: `124-Development.Model.md`
- `Design.Target.Model` — the current explicit design model of a system
  - does not live only in the index — the index is a map of that model and holds part of its content
  - other surfaces hold design data too: `Index.Appendix`, skills, etc.
  - the index is still the entry point for building the design model because it links out to the other surfaces
  - DTM is a distributed model, with the index as the discovery layer
- `Current.Implementation` — the current realized state of a system; may live in code, CLI, skills, data, notes, or any combination
- `Progress.Gradient` — the current best direction of movement between `Current.Implementation` and `Design.Target.Model`
  - the project is never finished — working is moving in the direction of the gradient
  - being unfinished is acceptable when a credible gradient exists
  - related to but distinct from `Placement.Balance` (spatial equilibrium) — `Progress.Gradient` is directional/temporal
- `Design.Implementation.CoEvolution` — design and implementation reshape each other; progress means co-developing both

#### meta

- status: settled
- evidence:
  - user confirmed all four concepts are alive and fundamental
  - user corrected DTM: does not live only in the index, index is the map and discovery layer
  - user confirmed Progress.Gradient semantic: project is never finished, working = moving along the gradient
  - `Natural.Placement` and `Placement.Balance` already in `100-Agentos.Surfaces.md`

### Impl.Req.Artifact.Structure

- `Impl.Req` artifact uses four sections: `Impl.Abstract`, `Impl.Index`, `Execution.Plan`, `Impl.Log`
- `Impl.Abstract` is fully agent-maintained — the agent must evaluate changes to it on each design change
- `Impl.Index` uses `Design.Index.Block` format — same block format, evidence tracking, and alignment semantics
- fundamentals produced through focused implementation-scoped alignment discussion
- `Execution.Plan` structured as ordered vertical slices with validation and status
- `Impl.Log` for implementer progress tracking

#### meta

- status: settled
- evidence:
  - user chose `Impl.Index` name over `Design.Index` for implementation scope
  - user confirmed artifact structure should align with Design.Session format
  - user confirmed `Impl.Abstract` is fully agent-maintained

### Impl.Req.Agent.Chain

- three-agent chain: `conceptual.designer.agent` → `impl.designer.agent` → `impl.executer.agent`
- each can be one or several agents
- all agents should have `Development.Principles` loaded
- `impl.executer.agent` runs minimal re-alignment from `Impl.Index` before starting
- multiple `Impl.Req` can spawn from one design session for different parts

#### meta

- status: settled
- evidence:
  - user defined the three-agent chain and re-alignment step
  - user confirmed Impl.Req as Alignment.Surface for implementation

### Alignment.Session.Design

- `Alignment.Session` is a general pattern available to hugentic workflows for human-agent alignment
- not a mandatory base — a pattern workflows can use and specialize

#### Conceptual.Space

- `Conceptual.Space` is the common space all surfaces live in — every design decision, implementation choice, naming convention is a dimension
- synonym: `Alignment.Space`
- each surface occupies a region in this space
- alignment is the process of moving two points/objects in this space closer together
- settled = high density, evidence-backed region
- open = low density, known but unexplored
- rejected = explicitly excluded

#### Alignment Types

- `Forward.Alignment` — moving the design point to a new place in the `Conceptual.Space` (adding features, evolving design)
- `Internal.Alignment` — for a given design state, moving all other surfaces to follow the design point (keeping surfaces in sync)
- `Hugentic.Alignment` — bringing human and agent to shared understanding of where they are and where they're going in the space

#### Axis Model

- `Alignment.Hugentic.Axis` — dimensions of the `Conceptual.Space` that need human-agent convergence; each workflow defines its own set
- `Alignment.Agentic.Axis` — dimensions the agent can resolve autonomously
- replaces the old `Alignment.Focus` concept — the hugentic axes *are* the focus
- replaces `Design.Alignment.Core` — which was the design-session-specific set of hugentic axes

#### Alignment.Loop

- `Alignment.Loop` — the machinery for achieving `Hugentic.Alignment` along the `Alignment.Hugentic.Axis`
- three steps, parameterized by workflow: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`
- parameterized naming: `Alignment.Question:Design`, `Alignment.Question:Impl`, `Alignment.Question:Exec`
- "Realignment" dropped as prefix — lightweight alignment is just a qualified `Alignment.Loop` (e.g. light)

#### Turn Modes

- `Alignment.User.Turn` — user drives, agent follows
- `Alignment.Maintenance.Turn` — agent drives, picks one move
- turn switching is user-gated (general rule)

#### Alignment.Backend

- two variants: `InChat` (state in chat) / `Artifact` (state in file)
- not all workflows offer both

#### Concept Merges

- `Session.Runtime.Loop` → `Alignment.Loop:Design`
- `Design.Alignment.Question` / `Design.Enrichment.Discussion` / `Design.Consolidation` → `Alignment.Question:Design` / `Alignment.Discussion:Design` / `Alignment.Consolidation:Design`
- `User.Assistant.Turn` / `Session.Maintenance.Turn` → `Alignment.User.Turn` / `Alignment.Maintenance.Turn`
- `InChat.Design.Session` / `Artifact.Design.Session` → `Alignment.Backend:InChat:Design` / `Alignment.Backend:Artifact:Design`
- `Impl.Alignment.Loop` → `Alignment.Loop:Impl`
- `Realignment.Loop` → `Alignment.Loop:Exec` (light)
- `Design.Alignment.Core` → `Alignment.Hugentic.Axis:Design`
- `Design.Open.Space` → sparse region of `Conceptual.Space`

#### Phase Semantic Roots

- `What.Design` — phase 1, working on the conceptual model (was `Fundamentals Design`)
- `How.Design` — phase 2, planning the path to reach it (was `Implementation Design`)
- `Impl.Exec` — phase 3, walking the path (was `Implementation Execution`)
- concept names build from these roots (e.g. `What.Design.Session`, `Alignment.Loop:What`)

#### Concept Eliminations

- `Alignment.Focus` — replaced by `Alignment.Hugentic.Axis`
- `Realignment` as prefix — dropped

#### Concept Redefinitions (keep, redefine from fundamentals)

- `Design.Implementation.CoEvolution` — the rhythm of `Forward.Alignment` then `Internal.Alignment`, co-developing design and implementation surfaces
- `Progress.Gradient` — the combined direction of `Forward.Alignment` + `Internal.Alignment` at any point
- `Conceptual.Space` is primary, `Alignment.Space` is synonym

#### meta

- status: working
- evidence:
  - user confirmed general pattern, not mandatory base
  - user confirmed parameterized naming over concept explosion
  - user confirmed Alignment.User.Turn / Alignment.Maintenance.Turn as the two turn concepts
  - user confirmed dropping Realignment — qualify as light on the workflow instead
  - user confirmed Conceptual.Space as the common space, Alignment.Space as synonym
  - user confirmed three alignment types: Forward, Internal, Hugentic
  - user confirmed Alignment.Hugentic.Axis replaces Alignment.Focus and Design.Alignment.Core
  - user confirmed Alignment.Agentic.Axis for agent-autonomous dimensions
  - user confirmed Design.Implementation.CoEvolution and Progress.Gradient keep but redefine from fundamentals
  - user confirmed phase semantic roots: What.Design, How.Design, Impl.Exec

### Development.Principles.File.Plan

- `Deep.Modules`, `Agent.Navigable.Codebase`, and other shared development quality principles will move to `125-Development.Principles.md`
- these are not Impl.Req-specific — they are shared principles loaded by all agents in the implementation chain
- `Vertical.Slice`, `No.Legacy.Allowed`, `Test.At.Boundaries` stay in `123` as they are both principles and Impl.Req structural guidance

#### meta

- status: settled
- evidence:
  - user distinguished local/every-impl principles from high-level/occasional principles
  - user confirmed both impl-req writer and executor must have principles loaded

### No.Legacy.Override

- `No.Legacy.Allowed` can only be overridden by an explicit statement
- ignoring this is one of the main causes of poor quality implementation results

#### meta

- status: settled
- evidence:
  - user stated this as a key quality constraint

### Index.Block.Body.Rationale

- if an example or code is in a block body, it's fundamental to understanding the concept
- the old 513 four-layer model (heading → fundamentals → extra → index section) is simplified to three layers (heading → body → sections)
- everything in the body is fundamental by definition — if it's not fundamental, it doesn't belong in the block

#### meta

- status: settled — promoted into `Index.Block` in `114`

## Session.Notes

- migration progress: source files 100-106 processed, 107 parked, 108-110 + 112-113 pending triage
- 111 (Design.Session) being reindexed as 121-123
- `Design.Target.Model` family triaged: all four concepts alive, proposed for `124-Development.Model.md`
- `--project-base` must be used with all `agentos stdlib prefix next` calls — discovered during session
- correct invocation: `agentos stdlib prefix next --project /Users/pereiro/projects/agentos-project/agentos-md --project-base agentos-md --target <target>`

## Session.Log

- bootstrapped migration: moved `notes/index/` → `notes/index-migration/`, created fresh index
- Tier 1 complete: `000-index.md`, `001-ontology.md`, `002-surfaces.md` reserved notes set up
- migrated source files: 100 (Index.Notes), 101 (Md.Surface), 102 (Dotted.Notation), 103 (File.Numbering), 104 (Maintenance), 105 (Project), 106 (Skills)
- new concepts emerged during migration: `Natural.Placement`, `Placement.Balance`, `Index.Concept.Coverage`, `Index.Block.Outlinks`, `Context.Minimal.Surface`
- design pivot: old SSOT model dropped in favor of `Stable.Surface.Equal.Authority`
- design pivot: reframed migration as reindex — old index is one source, not the template
- upgraded to `Artifact.Session`
- updated artifact structure: `Session.Index` → `Design.Index`, `Session.Docs` removed, blocks converted to `Design.Index.Block` format
- parked `Agentos.Mission` (107) — superseded by Iterante
- settled file plan for Design.Session concept family: 121 (Design.Session), 122 (Alignment.Space), 123 (Impl.Req)
- settled Design.Session fundamentals wording — convergence surface, interview loop, alignment enrichment as method not purpose
- settled `Hard.Evidence` as general concept, placed in `122-Alignment.Space.md`
- settled `User.Gated.Trigger` / `User.Gated.Writing` move to `100-Agentos.Surfaces.md`
- settled evidence-in-meta format for `Design.Index.Block` — lightweight summary pointers
- settled interview protocol lives in parent `Design.Session` fundamentals, not in `Session.Runtime.Loop`
- updated `Design.Session.File.Plan` — removed gates from 121, added `Hard.Evidence` to 122
- settled `Session.Runtime.Loop` framing — main flow (Design.Alignment.Question → Design.Enrichment.Discussion → Design.Consolidation) with interruption branches as user vocabulary
- settled `Design.Status.Report` as `Session.Runtime.Loop` sub-concept — promoted out of interruptions
- settled `InChat.Design.Session` and `Artifact.Design.Session` backend concepts
- settled `Design.Target.Model` family: DTM (expanded — distributed model, index as discovery layer), Current.Implementation, Progress.Gradient (project never finished), Design.Implementation.CoEvolution — proposed for `124-Development.Model.md`
- settled Design.Session as staging area for Stable.Surface changes — strong signal for change, not a stable surface itself
- drafted and wrote `121-Design.Session.md` — Design.Session, Session.Runtime.Loop, InChat.Design.Session, Artifact.Design.Session
- updated `000-index.md` and `001-ontology.md` with new entries
- drafted and wrote `124-Development.Model.md` — Design.Target.Model, Current.Implementation, Progress.Gradient, Design.Implementation.CoEvolution
- updated `000-index.md` and `001-ontology.md` with 124 entries
- drafted and wrote `123-Impl.Req.md` — Impl.Req (implementation plan design surface), Vertical.Slice, No.Legacy.Allowed, Test.At.Boundaries, Deep.Modules, Agent.Navigable.Codebase
- updated `000-index.md` and `001-ontology.md` with 123 entries
- expanded `Vertical.Slice` fundamentals in `123-Impl.Req.md` and created `notes/appendix/123-Impl.Req.md` with appendix
- settled Impl.Req artifact structure: Impl.Abstract (agent-maintained), Impl.Index, Execution.Plan, Impl.Log
- settled three-agent chain: conceptual.designer → impl.designer → impl.executer
- settled Impl.Req as Alignment.Surface for implementation — fundamentals produced through focused discussion
- settled Deep.Modules and Agent.Navigable.Codebase move to `125-Development.Principles.md`
- settled No.Legacy.Allowed override requires explicit statement — ignoring it is a main cause of poor quality
- removed Deep.Modules and Agent.Navigable.Codebase from `123-Impl.Req.md`
