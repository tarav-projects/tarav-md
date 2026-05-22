# Package Skill - design-session

## Session.Abstract

- intent: revisit and stabilize the concepts around `Package.Skill` as a self-contained agentic public surface for a package, project, or subsystem
- active focus: clarify the concept set, boundaries, SSOT model, routing model, installation role, and dependency model
- source context: continuation from prior Service.Agent / Package.Skill design discussion
- state: active
- next: revisit the four accepted concept names one by one

## Design.Index

### Package.Skill

- self-contained agentic public surface for a package, project, or subsystem
- like a software package rather than a script: an integrated collection of subsystems for performing a coherent set of tasks
- collects public markdown knowledge, routing, setup instructions, workflows, and agent-facing operating material
- acts as the package-level SSOT for public agentic knowledge
- an implementation of the project in the agentic medium, not a replacement for source code
- one semantic concept that supports compact single-skill and split multi-skill physical layouts
- can expose specialized alias skills as entry points back into the package SSOT

### Package.Skill.Router

- orientation layer inside a `Package.Skill`
- welcomes agents working with the system by showing where package knowledge and capabilities live
- acts as an internal table of contents, not an active dispatcher
- stays transparent to the caller workflow: it does not prompt the caller to take actions or change task flow
- maps task kinds, concepts, workflows, references, services, and alias skills to their package locations
- lets alias skills add workflow intention while pointing back to the package SSOT
- helps agents find the right subsystem without making routing decisions for them

### Package.Skill.Install

- installation layer of a `Package.Skill`
- like an install script: performs whatever setup the package requires
- may create or update package entry points such as alias skills
- may install or check software dependencies, CLIs, references, generated files, or local configuration
- may delegate work to deterministic tools or scripts when available
- belongs to the agentic package surface, but does not make the skill the owner of all implementation code
- should make side effects explicit so the caller can understand what will change

### Package.Skill.Dependency

- dependency declaration surface inside a `Package.Skill`
- can live as a router section or a `references/` file, depending on package size
- describes dependencies needed by the package skill, especially dependencies on other package skills
- covers agentic dependencies: concepts, workflows, routers, install steps, references, or service surfaces provided by another package skill
- external concepts must be referenced with qualified names, such as `<package>-skill/Bla.Concept`
- lets agents know which outside package surfaces may need to be loaded, installed, or consulted

### Package.Agent

- specialized agent qualified to work with a given `Package.Skill`
- mediates interaction between a user-agent and the package, project, or subsystem
- can be defined by a `Package.Skill`; one package skill may define several package agents when needed
- mostly a formal role boundary: the user-agent delegates package-specific work to an agent that knows the package surface
- uses the package skill as its public knowledge and operating surface
- can run general package work or specific package workflows depending on how it is defined

### Package.Skill.Index

- common subsystem of `Package.Skill`
- provides the package's conceptual index surface
- organizes package concepts, names, concept blocks, and reference paths for agent use
- is owned by the package skill, not by a separate SSOT
- can be exposed through an entry skill such as `<package>-index`
- lets agents enter the package through conceptual lookup rather than task workflow

#### appendix

- workflows with recurring conceptual needs should list the index blocks they normally need in their router or reference files
- block lists are collection targets, not a new concept layer
- an `Index.Agent` is a role any capable agent can perform: search the index, collect relevant blocks or appendix material, then continue the task under the gathered concepts
- workflow agents can perform the `Index.Agent` role themselves when a separate specialist agent is unnecessary

### Package.Entry.Skill

- specialized skill that serves as an entry point into a `Package.Skill`
- adds caller intention, workflow framing, or subsystem focus
- points back to the package skill as the SSOT
- may expose a package subsystem such as `Package.Skill.Index` or a package agent call
- does not duplicate package knowledge

### Cited.Duplication

- intentional duplication of authoritative concept material into a non-authoritative surface with an explicit `Concept.Cite` to the origin
- used when local access to repeated context improves agent performance, bootstrapping, workflow execution, package orientation, or readability
- the duplicate may be rewritten, summarized, or adapted to local task shape, but remains non-authoritative
- the cited origin anchors maintenance and gives agents a way to check drift
- disagreement between duplicate and origin is an error that should be surfaced, not silently resolved
- if a cited duplicate clearly mirrors an edited origin, the writer may update the duplicate in the same approved write pass
- unresolved drift or ambiguous disagreement is surfaced as an issue, not silently resolved
- uncited durable concept material in a non-authoritative surface should either be indexed, cited, or treated as unmanaged duplication

#### appendix

- inline citations place provenance at the duplicated idea itself, so agents can inspect the local copy and immediately know where to check authority
- citations are used where they materially help interpretation, verification, maintenance, or navigation
- `Cited.Duplication` lets workflow skills, package routers, entry skills, and package-agent instructions carry known context directly instead of rediscovering it on every run

### Inline.Relatedness

- writing discipline of naturally blending related `Dotted.Name` concepts into concept text
- the goal is not to create explicit related-edge metadata
- when a related concept is already part of the sentence meaning, use its `Dotted.Name`
- use `Concept.Cite` only when a materially important relationship should be visible but does not fit naturally into the sentence
- enriches the index by making concept relationships discoverable inside ordinary writing

### Concept.Cite

- bracket notation for citing concept origins or materially important related concepts when inline mention is not natural
- format: `[Concept.X, Concept.Y]`; page or source qualifiers may be added when needed, e.g. `[Concept.X, Concept.Y[1]]`
- used when the citation changes how an agent should interpret, verify, maintain, or navigate the line
- not used merely because another concept is loosely related
- complements `Inline.Relatedness`: prefer natural inline `Dotted.Name` mentions, cite only when the relation matters but does not read naturally

### Natural.Placement

- principle that each surface holds the facet of a concept that is natural to its function
- primarily governs where authoritative origin material belongs
- the full description of a concept is distributed across surfaces, with each surface contributing the facet natural to it
- cited duplicates can also be naturally placed when local use strongly benefits from repeated content
- duplication is justified when avoiding it would harm bootstrapping, workflow performance, local readability, or agent orientation
- content that feels unnatural in a surface is probably misplaced
- uncited or stale duplication is the anti-pattern, not duplication itself

### Placement.Balance

- maintained alignment state between authoritative origins and their useful local expressions across surfaces
- balanced placement is not absence of repetition
- the system is balanced when authoritative origins live in their natural source surfaces and cited duplicates exist only where locally useful
- duplicates remain balanced when they cite origins and can be found, checked, and updated during maintenance
- diagnostic signal: uncited repeated concept material, stale cited duplicates, or ambiguity about which surface is authoritative
- complementary to `Natural.Placement`: natural placement decides where material belongs; placement balance checks whether distributed material stays aligned

### Index.Writer.Maintenance.Pass

- maintenance check performed when editing an existing authoritative concept block
- starts by finding all mentions and citations of the edited concept across stable markdown surfaces
- checks cited duplicates, workflow copies, package routers, entry skills, and related references for needed updates
- may update clear cited duplicates in the same approved write pass when they mirror the edited origin
- surfaces unresolved drift, ambiguous disagreement, or unclear authority as issues
- prevents index edits from leaving known duplicated or cited material stale

### Workflow.Skill

- skill oriented around executing a recurring workflow
- can include the conceptual framing it needs inline when that improves execution
- uses `Cited.Duplication` to carry known context directly instead of searching the index on every run
- becomes a contextualized execution surface rather than only a thin router
- should cite origin blocks for duplicated concept material
- should still use index search or `Index.Agent` behavior for unknown, custom, or exploratory context needs

### Index.Agent

- role for collecting, interpreting, and returning context from the index
- can be performed by a dedicated specialist agent or temporarily by a workflow agent
- useful for discovery, uncertain queries, custom context extraction, and index-grounded synthesis
- not required as the default prelude when a workflow already knows its needed cited context
- must cite source blocks in returned context so summaries remain traceable and maintainable

## Session.Notes

### Traversal

- [x] 1. `Package.Skill`
- [x] 2. `Package.Skill.Router`
- [x] 3. `Package.Skill.Install`
- [x] 4. `Package.Skill.Dependency`
- [x] 5. `Package.Agent` replacing `Service.Agent`
- [x] 6. relation to `<package>-index`
- [x] 7. relation to `Skill.Export.Package` — parked as unrelated import/export mechanism with confusing name
- [x] 8. small single-skill form vs split package form

## Session.Log

- session opened from prior Package.Skill discussion
- accepted initial namespace: `Package.Skill`, `Package.Skill.Dependency`, `Package.Skill.Install`, `Package.Skill.Router`
- item 1 (`Package.Skill`) reviewed — accepted package-vs-script distinction and package-level SSOT framing
- item 2 (`Package.Skill.Router`) reviewed — router is neutral orientation / internal table of contents; alias skills carry workflow intention
- item 3 (`Package.Skill.Install`) reviewed — install layer may perform real setup like an install script; side effects should be explicit
- item 4 (`Package.Skill.Dependency`) reviewed — dependency knowledge has a formal package surface; external concepts use qualified names such as `<package>-skill/Bla.Concept`
- item 5 reviewed — `Service.Agent` renamed/reframed as `Package.Agent`, a specialized agent qualified to work with a given `Package.Skill`
- item 6 reviewed — `<package>-index` is a `Package.Entry.Skill` into the `Package.Skill.Index` subsystem, not a separate SSOT
- item 7 reviewed — `Skill.Export.Package` is unrelated to `Package.Skill`; it belongs to Agentos skill import/export mechanics and is parked as a confusing name
- item 8 reviewed — compact single-skill and split multi-skill layouts are physical forms of one `Package.Skill` concept
- index loading uncertainty discussed — no new concept added; standard practice is to list needed blocks in workflow/router references and treat `Index.Agent` as a role that workflow agents may perform themselves
- `Cited.Duplication` introduced — cited duplication unlocks richer workflow/package writing while keeping authoritative origins discoverable for maintenance
- index writer implication captured — edits to existing concept blocks need a maintenance pass that at least finds all mentions/citations of the edited concept
- `Natural.Placement` / `Placement.Balance` implication captured — duplication can be naturally placed; the anti-pattern is unmaintainable, uncited, or stale duplication
- workflow and `Index.Agent` implications captured — workflow skills can become contextualized execution surfaces; `Index.Agent` returned context must cite source blocks
- critical-path draft blocks captured: `Cited.Duplication`, `Inline.Relatedness`, `Concept.Cite`, `Natural.Placement`, `Placement.Balance`, `Index.Writer.Maintenance.Pass`, `Workflow.Skill`, `Index.Agent`
- index update written — promoted critical-path changes into public index files and updated `agentos-index-writer` operational guidance
