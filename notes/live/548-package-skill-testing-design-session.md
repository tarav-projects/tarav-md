# Package Skill Testing - design session

## Session.Abstract

- intent: design an MVP for `Package.Skill.Testing`, starting from `agentos-pkg` index entry-path behavior
- current goal: establish the concept namespace and general structure before designing runner details
- active focus: define the top-level subsystem concepts and keep the MVP grounded in realistic agent usage patterns
- state: in progress
- next: decide the first MVP shape for `agentos-pkg-test-ground` and one usage-pattern test

## Design.Index

### Package.Skill.Testing

- `Package.Skill.Testing` is the subsystem for testing how agents use a `Package.Skill`
- it tests agent behavior at package boundaries: orientation, routing, concept discovery, workflow entry, cited context collection, and operational skill handoff
- it is not primarily code testing; it is agentic behavior testing
- test targets may include the package root `SKILL.md`, auxiliary skills, package index, references, local project instructions, and controlled project environments
- the core question: when an agent enters through this package surface, does it do the right kind of work with acceptable cost and reliability?

### Package.Skill.TestGround

- `Package.Skill.TestGround` is a controlled test project that simulates an external project working with the tested `Package.Skill`
- it gives `Package.Skill.Testing` a realistic project environment where agents must discover, load, and use the package skill as they would outside the package's own implementation repository
- it can control visible skills, `AGENTS.md`, local index state, package imports, fixture files, and task prompts
- it exists when prompt-only tests are not enough because the environment itself is part of the behavior being tested
- example: `agentos-pkg-test-ground` is the first concrete `Package.Skill.TestGround` for testing `agentos-pkg`

### Package.Skill.EntryPath.Test

- `Package.Skill.EntryPath.Test` evaluates how an agent enters and navigates a package skill
- it compares different entry paths, such as package root only, auxiliary skill, project `AGENTS.md`, or no explicit skill mention
- it measures whether the agent finds the right surfaces and performs the task without excessive context loading or hallucinated protocol
- it is a standard recommended test type, not a restriction; package authors can define other test shapes

### Package.Skill.Entry.Path

- `Package.Skill.Entry.Path` describes how a fresh agent session gets enough package guidance into context to work with a `Package.Skill`
- it is not only a file or skill; it is the activation route from a new session to usable package orientation
- entry paths can be automatic, semi-automatic, or user-directed
- the test question is whether the agent can find the package map, index, auxiliary skills, and workflow-neutral orientation without needing hidden session knowledge

### Entry.Surface

- `Entry.Surface` is a context-bearing surface that can introduce a package system to an agent
- entry surfaces matter because different agent runtimes expose different initial context
- a robust `Package.Skill` should work through more than one `Entry.Surface`, but it does not need to duplicate everything everywhere
- each `Entry.Surface` should provide a small orientation and route the agent toward richer package guidance

### Entry.Path.Placement

- `Entry.Path.Placement` applies `Natural.Placement` to package entry guidance
- each `Entry.Surface` should contain the guidance that is natural for that surface, even when that creates some useful redundancy
- `AGENTS.md` routes: it tells the agent which package skill matters for this project
- `Skill.Description` advertises: it helps the agent recognize when the skill should be loaded
- `User.Load` commands: they directly name the package or skill surface to load
- `Package.Skill` entry body or reference guide orients: it gives the workflow-neutral system map after the package is loaded
- redundancy is acceptable when it improves agent entry reliability, but repeated content should remain short, aligned, and route back to richer package surfaces when needed

### Package.Driver

- `Package.Driver` is the minimal context payload needed for an agent to use a package
- it tells the agent what the package is, how to orient, what major subsystems exist, and where to go next
- it should be small enough to place early in context
- it should be workflow-neutral: installing the driver should not force the caller into a workflow
- it can be distributed across multiple `InContext.Surface`s
- `Package.SKILL` is the canonical package-owned `Package.Driver` surface
- `Package.SKILL` should contain the complete `Package.Driver`
- other `InContext.Surface`s can duplicate, route to, advertise, or trigger installation of the driver, but they should be auxiliary to `Package.SKILL`
- this matters because a user may load a package skill inside a project that has no package-aware `AGENTS.md`
- all real installation paths should be able to converge on `Package.SKILL`

### Agentos.Pkg

- `Agentos.Pkg` is the short name for `Package.Skill:Agentos`
- it is the core package skill for the Agentos system
- in the current implementation, `Agentos.Pkg` lives at `agentos-md/skills/agentos-pkg/`
- the implementation location is not the package identity: `Agentos.Pkg` is not the same thing as `agentos-md`
- `Agentos.Pkg` is the package context that should orient agents to Agentos concepts, public skills, index, Hugentics workflows, project model, and shared operating surfaces

### Package.Driver:Agentos.Pkg

- `Package.Driver:Agentos.Pkg` is the minimal context payload needed for an agent to use `Agentos.Pkg`
- it should orient the agent to Agentos package identity, major subsystems, public and auxiliary skills, Agentos Index entry path, Hugentics workflow map, live-note/live-script surfaces, project model, and package-skill conventions
- it should be workflow-neutral
- it should not force index loading, design-session loading, implementation workflow loading, or any other operation
- in the current implementation, this driver should be complete in `agentos-pkg/SKILL.md`
- some driver content can be duplicated into `AGENTS.md` or skill descriptions for `InContext.Installation`, but those surfaces are auxiliary to `Package.SKILL:Agentos.Pkg`

### InContext.Installation

- `InContext.Installation` means the package's `Package.Driver` is present in the active agent context
- it is a context state, not a separate package artifact
- installation can happen through any `InContext.Surface`: `AGENTS.md`, skill descriptions, `Package.SKILL`, references, user-provided context, or subagent-returned context
- auto-installation happens when enough of the `Package.Driver` is placed on autoloaded surfaces
- on-demand installation happens when the user or agent explicitly loads a package skill or driver surface
- installation paths can start from `AGENTS.md`, skill descriptions, explicit user load, or user intent recognition
- these paths should converge on `Package.SKILL` when the package driver is not already in context

### InContext.Installation:Agentos.Pkg

- `InContext.Installation:Agentos.Pkg` means `Package.Driver:Agentos.Pkg` is present in the active agent context
- for `agentos-project`, this is the desired fresh-session state
- primary path: `AGENTS.md -> load agentos-pkg -> Package.SKILL:Agentos.Pkg`
- direct user path: `User.Load:agentos-pkg -> Package.SKILL:Agentos.Pkg`
- discovery path: `Skill.Description:agentos-pkg -> Package.SKILL:Agentos.Pkg`
- intent path: `User.Intent -> recognition -> agentos-pkg -> Package.SKILL:Agentos.Pkg`
- all paths converge on `Package.SKILL:Agentos.Pkg`
- root `AGENTS.md` helps install the driver, but is not part of the driver's completeness contract
- `agentos-index` should stay conditional: load it when the task needs index-grounded context, writing, diagnosis, testing, maintenance, or the `Index.Agent` role

### Package.SKILL

- `Package.SKILL` is the root `SKILL.md` entry body for a `Package.Skill`
- it is the canonical package-owned `Package.Driver` surface
- it assumes the agent knows nothing about the package beyond the `Package.Skill` skill description
- its job is to provide minimal workflow-neutral context, introduce major subsystems, and route the agent toward more specific surfaces
- routing is one function of `Package.SKILL`, but not the whole concept
- `Package.SKILL` should be self-sufficient once loaded
- it should not require a package-aware `AGENTS.md` to complete the package driver
- it should contain the complete `Package.Driver`, even when some driver content is duplicated into `AGENTS.md` or skill descriptions
- it should stay transparent to the caller workflow: it orients and routes without prompting the caller to change task flow

### InContext.Surface

- `InContext.Surface` is a skill, reference, index page, appendix, `AGENTS.md`, or other context surface whose relevant guidance is already present in the current agent context
- package guidance should treat in-context surfaces as reusable context, not as something to reload every time they are mentioned
- before loading a referenced surface, the agent should check whether the relevant guidance is already available in context
- if it is already in context, the agent should continue from the existing context and load only missing details needed for the current task
- this keeps package routing efficient and reduces context duplication without preventing useful `Entry.Path.Placement` redundancy

### InContext.Surface:AGENTS.md

- `InContext.Surface:AGENTS.md` means project guidance from an `AGENTS.md` file is already present in the active agent context
- for a project that has an installed or relevant `Package.Skill`, `AGENTS.md` should include a short package guidance section
- the section should route to the package skill and any primary auxiliary skill needed for common project work
- it should not duplicate the package manual; it should identify the package entry point and when to use it
- in multi-project repositories, root `AGENTS.md` should route broadly, while nested project `AGENTS.md` files can give stronger package-specific guidance
- for `agentos-project`, this means root `AGENTS.md` should route to `agentos-pkg` instead of deprecated `agentos-usage`, and `agentos-md/AGENTS.md` should keep its stronger `agentos-pkg` / `agentos-index` guidance

### InContext.Surface:Package.SKILL

- `InContext.Surface:Package.SKILL` means the package root `SKILL.md` guidance is already present in the current agent context
- when this surface is in context, the agent should not reload the package skill just because the package is mentioned again
- the agent should use the existing `Package.SKILL` context as the package orientation baseline
- if the current task needs more detail, the agent should load the specific referenced skill, reference file, index page, or appendix that is missing

### InContext.Surface:Package.Aux.Skill

- `InContext.Surface:Package.Aux.Skill` means a package auxiliary skill has already contributed its relevant guidance to the current context
- when this surface is in context, the agent should reuse it for the current subsystem instead of re-triggering the same auxiliary skill
- auxiliary skill context can still route to deeper references when the task needs detail not already present
- this matters for skills like `agentos-index`, where repeated mentions are common during index work

### InContext.Surface:Reference

- `InContext.Surface:Reference` means a package reference file has already been read for the current task
- when this surface is in context, agents should rely on the already-loaded reference for stable instructions and avoid re-reading it unless there is a reason to check freshness, exact wording, or omitted sections
- references are useful as reusable context because they often contain the detailed version of guidance introduced by `Package.SKILL`

### InContext.Surface:Index.Page

- `InContext.Surface:Index.Page` means an index page has already been loaded into context
- agents should treat its blocks as available concept context and avoid reloading the same page for every concept mention
- if the task needs a block that may live elsewhere, the agent can search or load additional index pages instead of reloading the same one
- this helps `Index.Agent` work stay efficient while preserving multi-index and appendix navigation

### InContext.Surface:Appendix

- `InContext.Surface:Appendix` means an appendix page has already been loaded for deeper concept or protocol detail
- agents should reuse it when the current task depends on that detail
- if only a summary is needed later, the agent can cite or mention the appendix-backed concept without reloading the appendix
- appendix loading should remain task-driven because appendix pages can be larger and more specialized than index blocks

### Skill.Load.Idempotence

- `Skill.Load.Idempotence` means package and auxiliary skill guidance should be safe to encounter more than once
- skill descriptions can say when a skill should be loaded, but the stronger loading discipline belongs in `Package.SKILL` and in auxiliary skills that route to other surfaces
- a skill mention is not by itself an instruction to reload the skill
- route wording should make it natural for agents to reuse `InContext.Surface` context and only load missing surfaces when needed
- example wording: when this file mentions another skill or reference, load it only if its relevant guidance is not already in context

### Entry.Surface:AGENTS.md

- `Entry.Surface:AGENTS.md` is the project-local auto-loaded guidance surface
- it should route the agent to the relevant `Package.Skill` when the project is meant to work with that package
- it is useful because many agent systems load it automatically before the user asks anything
- it should stay short and project-specific: this project uses a package skill, and this is the package guidance to load first

### Entry.Surface:Skill.Description

- `Entry.Surface:Skill.Description` is the skill metadata loaded into the agent's available-skill context
- it improves visibility before the skill body is loaded
- it should explain what the skill is for, when to load it, and what kind of package orientation it provides
- it should not carry the full system model; its job is discovery and correct selection

### Entry.Surface:User.Load

- `Entry.Surface:User.Load` is explicit user activation of a package or skill surface
- it means the user directly names the load target, such as `load agentos-pkg skill`, `$agentos-pkg`, or `load /agentos-pkg`
- it is stronger than ordinary task intent because the agent does not need to infer which package surface should be loaded
- it should enter through the same `Package.Skill` orientation path as automatic or skill-description-based loading

### Entry.Signal:User.Intent

- `Entry.Signal:User.Intent` is when the user asks for something that implies a package system, but does not directly name the load target
- examples: `use the index`, `write this into the Agentos index`, or `run an Agentos package test`
- this requires the agent to recognize the intent from already-visible context, skill descriptions, `AGENTS.md`, or prior session knowledge
- it is useful, but weaker than `Entry.Surface:User.Load` because recognition can fail if the entry context is poor

### Package.Skill.UsagePattern.Test

- `Package.Skill.UsagePattern.Test` evaluates realistic package usage tasks
- example: given a natural paragraph, produce a candidate `Kernel.Block:Index`
- these tests are stronger than recall tests because they exercise discovery, interpretation, placement, and output quality together
- it is a standard recommended test type, not a restriction; package authors can define other test shapes

### agentos-pkg-test-ground

- `agentos-pkg-test-ground` is the proposed first `Package.Skill.TestGround`
- purpose: test how agents discover and use `agentos-pkg` and its Agentos Index entry path
- initial concern: a new session may not know how to interact with `agentos-pkg` or the index unless the entry path is clear
- first useful benchmark should compare startup paths, such as `agentos-pkg` only, index-specific auxiliary skill, project `AGENTS.md`, and natural context only

### Usage.Pattern:Kernel.Block.Authoring

- first candidate usage-pattern test
- prompt shape: provide a natural paragraph about a concept and ask the agent to produce a candidate `Kernel.Block:Index`
- expected behavior: agent discovers block-writing guidance, produces a compact concept block, cites or mentions relevant concepts, and explains placement/write discipline when appropriate
- test should inspect both output quality and how the agent found the relevant package/index context

### Reality.Weighted.Index.Optimization

- `Reality.Weighted.Index.Optimization` uses real package chat transcripts as evidence for improving an index
- chats reveal how agents and users actually search for, use, miss, duplicate, or misunderstand package concepts
- agents can extract usage-pattern tests from package usage/building transcripts
- extracted tests can be weighted by observed frequency, so recurring real situations matter more than rare synthetic ones
- the current index and agent entry paths can be evaluated against this weighted test set
- the result is an integrated performance score for the index as an agent-facing navigation system

### Index.Layout.Optimization

- `Index.Layout.Optimization` lets an agent propose index layout changes to improve retrieval and usage performance
- it can move blocks between index pages and appendix pages
- it can group blocks under namespace blocks
- it cannot delete blocks
- it cannot create arbitrary concept blocks during layout optimization
- it may create `Namespace.Block`s whose purpose is to group existing blocks and improve navigation
- the optimization target is improved agent performance on reality-weighted index tests, not aesthetic neatness
- this can generate reality-based grouping by discovering useful index structure from real workflows while staying constrained by index discipline

## Session.Notes

- current design preference: start by establishing the `Package.Skill.Testing` namespace instead of immediately designing a runner
- avoid over-specifying the implementation while the general structure is still forming
- existing surfaces found:
    - `skills/agentos-pkg/references/test-system.md`
    - `skills/agentos-pkg/testing/activation-recall-01.md`
    - `skills/agentos-index-test/SKILL.md`
- existing tests are activation/recall oriented; the new design should move toward usage-pattern behavior tests
- future direction: package chat transcripts can become a source of reality-weighted usage-pattern tests and index layout optimization signals

## Session.Log

- started from discussion about testing whether `agentos-pkg` gives agents sufficient index-entry guidance
- subagent probe found the new package entry path effective, with one path-relative ambiguity that was fixed
- session shifted from index-entry probing to designing an MVP for package-skill testing infrastructure
- accepted namespace direction: `Package.Skill.Testing`
- captured entry path placement, loaded-surface discipline, and reality-weighted index optimization as related design concepts
