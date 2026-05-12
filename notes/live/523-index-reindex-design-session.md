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

#### meta

- status: settled
- evidence:
  - user confirmed convergence wording
  - user clarified alignment is the method, not the purpose — the session does real work
  - user defined `Hard.Evidence.Based` and its priority
  - user confirmed goals stay in fundamentals, not a separate sub-concept

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

### Index.Block.Body.Rationale

- if an example or code is in a block body, it's fundamental to understanding the concept
- the old 513 four-layer model (heading → fundamentals → extra → index section) is simplified to three layers (heading → body → sections)
- everything in the body is fundamental by definition — if it's not fundamental, it doesn't belong in the block

#### meta

- status: settled — promoted into `Index.Block` in `114`

## Session.Notes

- migration progress: source files 100-106 processed, 107 parked, 108-110 + 112-113 pending triage
- 111 (Design.Session) being reindexed as 121-123
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
