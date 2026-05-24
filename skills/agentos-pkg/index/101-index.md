> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

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
- imported skills may include `Package.Skill` roots and `Package.Aux.Skill` aliases into package subsystems or workflows
- `agentos skills ...` is a project command — uses `Agentos.Project` targeting

****

## Usage.Surface

- `Usage.Surface` is the usage-useful subset of `Public.Surface`
- the surfaces that help external agents and humans understand how to use a project
- includes skills, CLI help, index notes, and other documentation surfaces
- not every surface in `Public.Surface` is equally usage-centric by design

****

## Usage.Skill

- `Usage.Skill` is a deprecated standalone orientation pattern for Agentos packages
- package roots now provide general usage and orientation through `Package.Skill` and `Package.Skill.Router`
- existing usage skills should be absorbed into package index, appendix, references, or package-root `SKILL.md` surfaces according to `Natural.Placement`
- operational workflow guidance should live in focused `Package.Aux.Skill` or `Workflow.Skill` surfaces instead of a general usage skill
- old usage skills may remain only as compatibility or migration surfaces until current routes stop depending on them

****

## Package.Skill

- `Package.Skill` is a self-contained agentic public surface for a package, project, or subsystem
- like a software package rather than a script: an integrated collection of subsystems for a coherent task area
- collects public markdown knowledge, routing, setup guidance, workflows, references, and agent-facing operating material
- acts as the package-level orientation and routing surface for public agentic knowledge
- supports compact single-skill and split multi-skill layouts under the same semantic concept
- may expose `Package.Aux.Skill` surfaces that add caller intention while pointing back to the package root or subsystem

****

## Package.Aux.Skill

- `Package.Aux.Skill` is a specialized skill associated with a `Package.Skill` but not itself the package root
- adds caller intention, workflow framing, operational behavior, subsystem focus, or convenience access without becoming a separate package root
- points back to the package root or package subsystem that provides the durable context
- may act as an entry point, alias, `Aux.Workflow.Skill`, install helper, doctor, test runner, or package-agent launcher
- should duplicate package knowledge only through `Cited.Duplication`
- can be workflow-neutral or operational depending on whether it orients the caller or runs a specific workflow

****

## Workflow.Neutral.Skill

- `Workflow.Neutral.Skill` provides orientation or package context without steering the caller into a workflow
- loading it should not change the caller's current task, action mode, or execution path
- contains information, routing, boundaries, and references rather than commands or task procedures
- useful for `Package.Skill` roots because package roots welcome many caller intentions transparently
- contrasts with `Aux.Workflow.Skill`, which intentionally guides a recurring task

****

## Package.Skill.Index

- `Package.Skill.Index` is the conceptual index subsystem of a `Package.Skill`
- organizes package concepts, names, concept blocks, appendix pages, and reference paths for agent use
- is part of the package skill rather than a separate package
- can be exposed through a `Package.Aux.Skill` such as `<package>-index`
- lets agents enter the package through conceptual lookup rather than a task workflow

****

## Package.Skill.Router

- `Package.Skill.Router` is the orientation layer inside a `Package.Skill`
- acts as an internal table of contents for package knowledge and capabilities
- stays transparent to caller workflow: it helps the caller find surfaces without prompting a task-flow change
- maps task kinds, concepts, workflows, references, package agents, install surfaces, and auxiliary skills to their package locations
- lets `Package.Aux.Skill` aliases carry workflow intention while the package router remains neutral

****

## Package.Skill.Dependency

- `Package.Skill.Dependency` is the package surface that declares dependencies needed by a `Package.Skill`
- may live as a `Package.Skill.Router` section or as a `references/` file, depending on package size
- covers agentic dependencies: concepts, workflows, routers, install steps, references, or service surfaces provided by another package skill
- external concepts should use qualified names when crossing package boundaries, for example `<package>-skill/Bla.Concept`
- gives agents a formal place to discover which outside package surfaces may need to be loaded, installed, or consulted

****

## Package.Skill.Install

- `Package.Skill.Install` is the installation layer of a `Package.Skill`
- like an install script: performs the setup the package requires
- may create or update auxiliary skills, package-local indexes, references, generated files, software dependencies, CLIs, or local configuration
- may delegate deterministic parts to tools or scripts when available
- belongs to the agentic package surface, but does not make the skill the owner of all implementation code
- should make side effects explicit before changing files

****

## Package.Agent

- `Package.Agent` is a specialized agent qualified to work with a given `Package.Skill`
- mediates package-specific work between a caller agent and the package, project, or subsystem
- can be defined by a package skill; one package may define several package agents when distinct roles are useful
- uses the package skill as its public knowledge and operating surface
- can run general package work or specific package workflows depending on its definition

****

## Aux.Workflow.Skill

- `Aux.Workflow.Skill` is a `Package.Aux.Skill` oriented around executing a recurring workflow
- it is the non-workflow-neutral counterpart: loading it steers the caller into a specific operation
- can include the conceptual framing it needs inline when that improves execution
- uses `Cited.Duplication` to carry known context directly instead of searching the index on every run
- becomes a contextualized execution surface rather than only a thin router
- should cite origin blocks for duplicated concept material
- should still use index search or `Index.Agent` behavior for unknown, custom, or exploratory context needs
- contrasts with `Workflow.Neutral.Skill`, which provides orientation without steering the caller's current task
- may be deployed from a `Package.Skill.UsagePattern` when a hot path deserves its own skill surface

****

## Skill.Explicit.Args

- `Skill.Explicit.Args` is the set of arguments a skill needs from the caller to operate
- like non-zero-arg functions: some skills need data before they can do useful work
- skills with explicit args should declare them in the skill description and in a dedicated section of the skill body
- the description should advertise args so an agent knows what to provide before loading
- the skill body should clarify behavior when args are missing: orient (workflow-neutral), ask, or noop — never guess
- zero-arg call on a workflow-neutral skill with explicit args: the skill loads its orientation context but does not perform an operation
- zero-arg call on an operational skill with explicit args: noop or orient, never assume a target
- examples: `agentos-testground` needs a target package; `agentos-index-test` needs a target project

****

## Package.Skill.UsagePattern

- `Package.Skill.UsagePattern` is a named situation/response pair that captures a common or important usage path through a package
- like a compiler hot path: the package identifies frequent usage situations and provides an optimized, documented route for each
- each pattern has: a trigger situation (what the user asks or needs) and an expected agent behavior path (which surfaces get loaded, in what order, and what the agent produces)
- patterns live in the package's `usage-patterns/` folder as named objects
- from a usage pattern, a package can optionally deploy: a router entry in `Package.SKILL`, an `Aux.Workflow.Skill`, or a testground test
- patterns do not replace the general path — the `Package.SKILL` decision router remains the fallback for situations not captured as a pattern
- new patterns emerge from real usage: chatlas transcripts, repeated user questions, observed agent failures, or reality-weighted test results
- a usage pattern is testable by nature: the situation is the test prompt, the expected behavior path is the behavior tiers

****

## Package.Skill.UsagePattern.Test

- `Package.Skill.UsagePattern.Test` evaluates whether the package delivers the expected behavior for a named usage pattern
- the test prompt is derived from the pattern's situation; the behavior tiers are derived from the pattern's expected response path
- tests run through the `agentos-testground` system: isolated CLI session, chatlas trace capture, tier evaluation
- because the pattern already defines situation and response, generating a test is nearly mechanical
- test results feed back into pattern refinement: if the agent fails, the pattern documentation or the package surfaces may need improvement
- patterns without tests are still useful as documentation; patterns with tests are verified documentation

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
