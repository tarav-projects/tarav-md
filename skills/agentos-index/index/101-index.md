> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

## Project.Discovery.System

- `Project.Discovery.System` resolves a command or workflow to an `Agentos.Project` target
- separates three concerns: project identity, project discovery, and command policy
- discovery modes:
    - implicit: parent-walk from start path until `Agentos.Project.Marker` is found
    - explicit: `--project <path>` targets that path; bare `--project` targets current directory
    - `--project-base <basename>` is a safety check — verifies the resolved project root's directory basename matches
- project-aware commands must require at least one explicit selector — must not silently target when all selectors are omitted
- implicit discovery failure must not auto-initialize a project — creation requires explicit user targeting

****

## Agentos.Skills

- `Agentos.Skills` defines skill selection, routing, and import behavior for Agentos projects
- a source contributes discoverable skills: direct path (`{ "path": "..." }`), project-backed (`{ "project": "..." }`), or package
- a profile is an ordered selection of sources plus one or more local depots
- profile resolution: project-local `.agentos/config.json` override → global default profile → hardcoded default
- importing materializes selected skills into depots as managed symlinks
- `agentos skills ...` is a project command — uses `Agentos.Project` targeting

****

## Usage.Surface

- `Usage.Surface` is the usage-useful subset of `Public.Surface`
- the surfaces that help external agents and humans understand how to use a project
- includes skills, CLI help, index notes, and other documentation surfaces
- not every surface in `Public.Surface` is equally usage-centric by design

****

## Usage.Skill

- `Usage.Skill` is a special-purpose, usage-centric skill designed primarily as documentation
- the master `Usage.Skill` of a project coordinates and curates its `Usage.Surface`
    - routes to whichever surface best answers a given question: skills, CLI help, or index notes
    - the opinionated entry point for external agents
- skills can own the source of truth of a topic — the index links out to them

****

## Workflow.Skill

- `Workflow.Skill` is a skill oriented around executing a recurring workflow
- can include the conceptual framing it needs inline when that improves execution
- uses `Cited.Duplication` to carry known context directly instead of searching the index on every run
- becomes a contextualized execution surface rather than only a thin router
- should cite origin blocks for duplicated concept material
- should still use index search or `Index.Agent` behavior for unknown, custom, or exploratory context needs

****

## Skill.Source

- `Skill.Source` is a direct skill root or package-like expansion that contributes discoverable skills
- types: direct path (`{ "path": "..." }`), project-backed (`{ "project": "..." }`), or package (`{ "package": [...] }`)
- project-backed sources scan `<project>/skills` and may publish export packages

****

## Skill.Export.Package

- `Skill.Export.Package` is a named skill package published by a project-backed source

****

## Skill.Profile

- `Skill.Profile` is an ordered selection of sources plus one or more local depots
- resolution: project-local `.agentos/config.json` override → global default profile → hardcoded default

****

## Skill.Depot

- `Skill.Depot` is a project-local directory where imported skill symlinks are materialized
- depots tend to be non-Agentos standard paths — for instance, `.agents/skills`

****

## Selected.Skills

- `Selected.Skills` is the catalog computed from the resolved `Skill.Profile` before depot sync

****

## Imported.Skills

- `Imported.Skills` is the `Selected.Skills` after import syncs depots

****

## What.Design.Session

- `What.Design.Session` is a scoped human-agent convergence surface for design work — the `What.Design` specialization of `Alignment.Session`
- the session does real work (design, problem-solving, issue resolution) while progressively enriching alignment between user and agent
- the interview loop (`Alignment.Question:What` → `Alignment.Discussion:What` → `Alignment.Consolidation:What`) is the fundamental strategy: direct questions produce evidence of alignment, consolidation makes it durable
- the agent maintains session progress and content; the user controls advancement and settles material
- session content aims to be `Hard.Evidence`-based as much as possible — evidence-based arguments have priority over agent assumptions
- the goal is to fill `Alignment.Hugentic.Axis:What` with evidence-based facts — more is welcome, but the core alignment space is the priority
- a staging area for `Stable.Surface` changes — session content is expected to become part of stable surfaces through implementation
- the move from design session state to stable surface is the implementation — can happen multiple ways: other agents read the artifact and implement in parallel, session emits `Impl.Req`s, direct surface updates from the session
- not a `Stable.Surface` itself — a strong signal for change that provides a clear substrate to align implementation against
- optimized for high-signal alignment data — can support operational work (migration, triage) when it produces alignment, but should not become a general-purpose work log
- does not replace index notes or skills — those are the destinations

****

## Alignment.Loop:What

- `Alignment.Loop:What` is the `What.Design` specialization of `Alignment.Loop` — the general workflow the agent tries to make the session follow
- main flow: `Alignment.Question:What` → `Alignment.Discussion:What` → `Alignment.Consolidation:What` → ...
- interruptions are named branches that pause the main flow at any point
- `Alignment.User.Turn` — user drives, agent follows (`Alignment.Discussion:What` phase)
- `Alignment.Maintenance.Turn` — agent drives one session move (`Alignment.Question:What`, `Alignment.Consolidation:What`, state update)
- mode switching is user-gated — agent may suggest, never silently switch
- `Design.Status.Report` — structured checkpoint that summarizes session state
    - delta-oriented: reactive to context, don't repeat still-valid reported state
    - serves multiple roles: status checkpoint, consolidation output, session state summary
    - works in both `Alignment.Backend:InChat:What` and `Alignment.Backend:Artifact:What`
    - used sparingly at natural consolidation points
    - in InChat sessions, `Alignment.Consolidation:What` = printing a `Design.Status.Report`
- `Session.Interruptions` — catalog of named branches the user can take:
    - `Capture.Audit`, `Consolidation.Plan`, `Artifact.Upgrade`, `Impl.Req.Handoff`, `Session.Split`, `Close.Topic`, `Park.Topic`
- the interruption catalog gives the user a vocabulary to communicate with the agent — each name triggers a known response shape
- after an interruption, return to the main flow unless the user chooses another move

****

## Alignment.Backend:InChat:What

- `Alignment.Backend:InChat:What` is the default `What.Design.Session` backend — state lives in chat
- the chat is the substrate, the agent organizes it into design-session form
- flexibility is the priority — no file overhead, no formal sections required every turn
- the agent must always track session state even when not printing it
- design state lives across explicit chat turns and strategic `Design.Status.Report` prints
- can't waste tokens on session organization overhead — the agent needs to actually work

****

## Alignment.Backend:Artifact:What

- `Alignment.Backend:Artifact:What` is the file-backed `What.Design.Session` backend — state lives in a `*-design-session.md` `Live.Note`
- durable, handoff-ready
- adds `Session.Notes` and `Session.Log` to `Session.Abstract` and `Design.Index`
- artifact writes are user-gated
- upgrade path: InChat → Artifact when state becomes too large, important, or needs future handoff — upgrade is user-gated, never automatic
- both backends run the same `Alignment.Loop:What` — the backend doesn't change the workflow, only where consolidated state is captured

****

## Forward.Alignment

- `Forward.Alignment` is moving the design point to a new place in the `Conceptual.Space` — adding features, evolving design, exploring new territory
- the creative act of development: deciding where to go next

****

## Internal.Alignment

- `Internal.Alignment` is keeping all surfaces in sync at the current design state
- for a given design point, moving all other surfaces to follow it
- the maintenance act of development: ensuring coherence across code, index, skills, docs

****

## Hugentic.Alignment

- `Hugentic.Alignment` is bringing human and agent to shared understanding of where they are and where they're going in the `Conceptual.Space`
- the convergence act: achieved through `Alignment.Loop` cycles

****

## Conceptual.Space

- `Conceptual.Space` is the abstract space where alignment occurs — the set of all possible design decisions
- `Alignment.Space` is a synonym
- see also `102-index.md` for `Design.Target.Model` as a point in this space

****

## Alignment.Hugentic.Axis

- `Alignment.Hugentic.Axis` is a dimension of the `Conceptual.Space` that needs human-agent convergence
- each workflow specialization defines its own set of axes
- the axes are the focus of the `Alignment.Loop`

****

## Alignment.Agentic.Axis

- `Alignment.Agentic.Axis` is a dimension the agent resolves autonomously without explicit human convergence
