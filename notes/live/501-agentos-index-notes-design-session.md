# Agentos Index Notes Redesign - design-session

## Motivation

Design a unified `Agentos.Index.Notes` system for durable concept notes across Agentos. The session defines Agentos-native primitives for index notes, ontology, writing, numbering, structure, maintenance, and related markdown surfaces.

## Items

- Agentos.Index.Notes: [closed] unified durable concept-note system and its scope
- Agentos.Index.Writing.Principles: [closed] durable note writing philosophy and exclusions
- Index.Note.Style: [closed] desired format and style for stable index notes
- Design.Target.Model: [closed] current explicit design model of a system
- Current.Implementation: [closed] current realized state of a system
- Progress.Gradient: [closed] current best direction of improvement between design and implementation
- Design.Implementation.CoEvolution: [closed] design and implementation evolving together
- Agentos.Index.Ontology.Registry: [closed] dotted concepts, registry role, and concept maturity lifecycle
- Agentos.Ontology.Workflows: [closed] workflows for concept emergence, registration, promotion, rename, and maintenance
- Dotted.Notation: [closed] dotted concept names and parameterized references such as `Maintenance.System:Agentos`
- Maintenance.System: [closed] general maintenance-system concept and doctor model for project surfaces
- Project.CLI: [closed] project-owned command surface for deterministic operations used by agents and humans
- Public.Surface: [closed] stable project-facing surfaces exposed for agents and humans
- Usage.Skill: [closed] standard public usage surface for understanding what a project is and how to use it
- Md.Surface: [closed] markdown design surface for a system, expressed through concepts and md blocks
- Agentos.Dev.Notes: [closed] development-facing markdown surface for working on a system
- Reserved.Notes: [closed] notes reserved for special purposes in Agentos systems
- File.Numbering.Protocol: [closed] numeric filename protocol for files in project surfaces
- TODOS.Note: [closed] lightweight note surface for parking TODO blocks for later use
- Live.Scripts: [closed] live working scripts that mirror live notes for executable surfaces
- Stub.Convention: [closed] minimal incomplete index entries that preserve real concepts without pretending completion
- Canonical.Reference.Implementation: [closed] preferred concrete implementation for an md-defined system, below the md surface in authority
- Agentos.Notes.Structure: [closed] structure of Agentos note surfaces under root folders

## Agentos.Index.Notes

`Agentos.Index.Notes` is the durable concept-note subsystem of an Agentos-style project.

It provides the high-signal markdown surface where important concepts, constraints, rationale, naming conventions, reusable patterns, and steering decisions are preserved so they can guide future work.

Its purpose is to maximize durable capture while continuously improving toward curated coherence. It favors low-friction writing of important material, then relies on review and maintenance to refine that material into a clearer and more coherent concept surface over time.

`Agentos.Index.Notes` is broader than a spec system. It may contain notes that behave like specs, but it also includes principles, ontology-aware concept notes, exclusions, design concepts, and other durable coordination knowledge. It is distinct from live notes, progress tracking, implementation code, and general documentation.

SSOT rule:

- `Agentos.Index.Notes` is the SSOT for public md-surface design knowledge in an Agentos-style project.
- Other public markdown surfaces, such as skills and `AGENTS.md`, should derive their durable design concepts and constraints from the index rather than define separate sources of truth.
- `Usage.Skill` is one example of such a derived public surface: it should derive from index notes rather than introduce parallel durable design truth.
- No significant new concept or durable design rule should live only outside `notes/index/`.
- If a source outside `notes/index/` is repeatedly being used as a source of durable design truth, that material should probably be promoted into `Agentos.Index.Notes`.

Internal concepts:

- `Index.Note` as the durable note unit
- `Index.Block` as the high-signal block unit inside notes
- `Index.Note.Style` as the desired mature note shape
- `Ontology.Registry` as the compact inventory of named concepts
- maintenance workflows that keep the surface coherent over time

## Agentos.Index.Writing.Principles

`Agentos.Index.Writing.Principles` defines the writing judgment for durable index notes.

Index notes should preserve material that changes future judgment: concepts, rationale, constraints, naming conventions, reusable patterns, steering decisions, boundaries, consequences, and explicit exclusions.

They should avoid material whose value is mainly transient, operational, or easily recoverable elsewhere: transcripts, changelogs, progress tracking, task lists, implementation dumps, and generic documentation.

Core principles:

- write for future judgment, not current narration
- preserve rationale, not only conclusions
- make boundaries and exclusions explicit
- prefer durable concepts over local incidents
- keep the surface high-signal and small
- allow rough capture when the material is important
- expect maintenance to improve naming, placement, structure, and compression
- do not let desired style block useful capture

Relationship to style:

- `Agentos.Index.Writing.Principles` governs what is worth saying and why
- `Index.Note.Style` governs the mature shape of how it should be said

## Index.Note.Style

`Index.Note.Style` is the desired stable shape for mature Agentos index notes.

A stable index note is concept-centered, block-structured, high-signal, low-prose, self-locating, refactorable, and loss-checked during compression. It may contain short clarifying prose, but should prefer compact heading-scoped blocks for definitions, constraints, rationale, boundaries, consequences, and anti-patterns.

Working style target:

- concept-centered: one named concept or tight concept cluster
- block-structured: each section has one steering idea
- high-signal: definitions, constraints, rationale, boundaries, consequences
- low-prose: short paragraphs only where they clarify; bullets for lists and constraints
- self-locating: title, concept name, and related concepts are explicit
- refactorable: sections can move without losing meaning
- loss-checked: compression or reformatting should verify that essential meaning was not dropped

Block model:

- `Md.Block` is the general markdown primitive: a portable, heading-scoped markdown unit that can be used by multiple surfaces.
- `Index.Block` is the index-specific use of that primitive: a high-signal block carrying one steering idea inside `Agentos.Index.Notes`.
- Files organize reading; blocks carry meaning.

Style exemplar: `502-agentos-index-notes-draft.md` is the first accepted format test for `Index.Note.Style`.

Current trigger: `004-Agentos.Project.md` is also a useful existing example because it defines one named concept, core terms, identity rules, boundaries, exclusions, and consequences. The style design should distinguish the desired stable index-note shape from temporary or work-in-progress index content that may be refactored later.

## Design.Target.Model

Topic framing: define the current explicit design model of a system.

Current direction: `Design.Target.Model` is the current explicit design model of the system. For Agentos-style projects, this is defined in `Agentos.Index.Notes`. `Agentos.Index.Notes` aims to contain the full design model of the system. If relevant design truth is repeatedly being inferred from other surfaces, that indicates an evolving or unconsolidated state.

## Current.Implementation

Topic framing: define the current realized state of a system.

Current direction: `Current.Implementation` is the current realized system. It may live in code, CLI, skills, data, notes, or any combination depending on project type. In md-only projects, `Design.Target.Model` and `Current.Implementation` may both be carried by notes while still remaining distinct concepts.

## Progress.Gradient

Topic framing: define the current best direction of improvement between design and implementation.

Current direction: `Progress.Gradient` is the current best direction of movement between `Current.Implementation` and `Design.Target.Model`. Being unfinished is acceptable if a credible progress gradient exists.

## Design.Implementation.CoEvolution

Topic framing: define the dynamic by which design and implementation reshape each other during development.

Current direction: `Design.Implementation.CoEvolution` means design and implementation evolve together. Implementation pressure changes the design model, and the design model redirects implementation. The main work unit is the pair `Design.Target.Model` + `Current.Implementation`. Progress means co-developing that pair, not only refining one side.

Agentos-specific rule:

- For Agentos-style projects, `Agentos.Index.Notes` defines `Design.Target.Model`.
- Relevant design truth may temporarily exist in `Agentos.Dev.Notes`, skills, `AGENTS.md`, live notes, or the codebase.
- When that happens, it indicates consolidation debt rather than a competing source of truth.
- The convergence direction is to promote durable design knowledge into `Agentos.Index.Notes`.

## Agentos.Index.Ontology.Registry

Topic framing: define the relationship between the conceptual ontology and the maintained registry.

Current direction: dotted notation implies a named concept. As concepts stabilize, they can be added to an `Ontology.Registry` that gives the big picture of the current ontology surface without requiring a full search.

Registry roles:

- present the full ontology surface at low resolution
- act as the public surface for what concepts exist
- serve as an index to fuller notes when deeper definitions exist

Entry shape:

- one small index block per concept
- one-paragraph definition
- references to fuller notes when they exist
- `###` per concept entry
- `##` group headers for clustering when useful

Inclusion rules:

- all concepts used on index notes should have an entry
- agents can suggest promotion into the registry from chat
- adding entries is user-gated

Relationship to dedicated notes:

- the registry is canonical for concept inventory
- dedicated notes are where deeper concept development can live
- small concepts may live only in the registry when that is enough
- the registry note itself should stay focused on concepts
- the registry format should be documented in a separate note rather than overloaded into the registry surface itself

Scope boundary:

- the registry is not the place for deep treatment of every concept
- it should give the full picture with low resolution

File-system role:

- `ontology.md` is the default registry file
- if the ontology grows too large, additional `*-ontology.md` files may be added
- in that case, `ontology.md` can become a routing index for the ontology surface

## Agentos.Ontology.Workflows

`Agentos.Ontology.Workflows` defines the descriptive lifecycle and operating behaviors for named concepts in an Agentos index surface.

Dotted names signal concepts; `Ontology.Registry` curates them; dedicated notes expand them. Agents infer where a concept is in that lifecycle from repository evidence rather than stored state. During design discussions, agents use the registry when concept identity matters, especially around dotted names or approximate names. During maintenance, agents can perform deeper checks for unregistered concepts, duplicates, stale references, rename drift, and missing index routing.

Registry lookup rule:

- registry lookup is opportunistic, not mandatory for all agent work
- use it when concept identity matters
- avoid turning ordinary work into ontology maintenance when the work does not depend on it

Lifecycle guidance:

- concept emergence through dotted names in ordinary notes
- concept registration in `Ontology.Registry`
- concept promotion into a dedicated note
- concept rename or replacement
- registry maintenance after note changes
- detecting unregistered dotted concepts
- agent lookup of the registry when the user uses approximate names or does not remember the exact concept name

## Dotted.Notation

`Dotted.Notation` identifies named concepts in an ontology surface.

Base rules:

- Dotted names mark ontology concepts, not casual prose.
- Every ontology name has at least two parts.
- Dot depth is flexible and should be natural to the concept.
- Dots provide context, but are not a strict hierarchy or namespace system.
- The definition and relationships live in notes and registry entries, not in the name alone.

`Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept.

Parameterized rules:

- Use `Concept.Name:Target` when the same concept is applied to a different target, project, subsystem, or concrete instance.
- The part before the colon is the concept.
- The part after the colon is the parameter.
- Colon parameters may themselves use dots, as in `Maintenance.System:Example.Project`.
- Conceptually, two `Maintenance.System:*` references are instances of the same concept, not different concepts.
- Parameterized references may appear as examples or references in `Ontology.Registry`, but they are not canonical ontology entries by default unless a later instance-registry concept is introduced.
- Use a new dotted name when the meaning changes; use `Concept.Name:Target` when the same concept is applied to a different target.

Examples:

- `Maintenance.System` names the concept.
- `Maintenance.System:Agentos` means the maintenance system for Agentos.
- `Maintenance.System:Example.Project` means the maintenance system for `Example.Project`.
- `Agentos.Index.Notes` names the Agentos index-notes concept.

## Maintenance.System

`Maintenance.System` defines how a project surface is diagnosed over time.

It coordinates a project-specific doctor skill, subsystem-owned check references, and project CLI commands when deterministic support exists. Checks may be agentic, CLI-supported, or both. The default workflow is diagnosis-first: report issues with evidence and affected subsystem context, discuss priorities with the user, and leave fixes to explicit follow-up workflows.

`Maintenance.System:Agentos` is the Agentos instance. Its likely doctor skill is `agentos-project-doctor`, and its CLI-supported checks are exposed through `Project.CLI:Agentos`, including commands such as `agentos doctor ...`.

Converging model:

- A maintenance system coordinates a project-specific doctor skill, project CLI commands when available, and subsystem-owned checks.
- `agentos-project-doctor` is the first likely doctor skill for `Maintenance.System:Agentos`.
- `agentos doctor ...` is a doctor command exposed by `Project.CLI:Agentos`, not the general maintenance CLI concept itself.
- The doctor skill and supporting CLI commands should be independently useful but aligned around the same maintenance model.
- Subsystems contribute checks through reference files and CLI hooks when appropriate.
- Checks can be agentic, CLI-supported, or both.
- The doctor workflow is diagnosis-first, not fix-first.
- Default output is a chat report that lists problems, evidence, affected subsystems, and likely importance.
- Large or durable findings can become `agentos-artifact-issue-report` artifacts when the user wants a durable issue surface.
- Fixing belongs to follow-up discussion or implementation workflows, not the default doctor pass.

## Project.CLI

Topic framing: define the project-owned command surface that exposes deterministic operations, checks, transformations, and utilities for agents and humans.

Current direction: `Project.CLI` is a general project surface. `Project.CLI:Agentos` is the Agentos instance, concretely the `agentos` CLI. Agentos agentic development workflows should encourage developing a project CLI alongside the project itself so deterministic work can be moved out of direct agent responsibility and into repeatable commands.

## Public.Surface

Topic framing: define the stable project-facing surfaces that agents and humans can rely on.

Current direction: `Project.CLI` is part of a project's `Public.Surface`. Other likely public surfaces may include index notes, skills, documented artifacts, or other stable interfaces exposed for project work.

## Usage.Skill

Topic framing: define a standard public usage surface for understanding what a project is and how to use it.

Current direction: `Usage.Skill` is the public usage surface of a project. It explains what the project is for, what public subsystems or interfaces it exposes, and how an external agent or user should use them. It is not primarily about how to modify or develop the project itself.

Canonical pattern:

- `<project>-usage` is the safe default entry surface for introducing an external agent to a project.
- it should route into deeper usage references and specialized usage skills when needed
- the default minimum is `<project>-usage` plus reference files

Layering:

- the top-level `SKILL.md` is usually a router
- deeper reference files can hold subsystem-specific usage detail
- specialized usage skills may exist for heavier use or manual triggering of subparts of the project

Boundary:

- `Usage.Skill` should explain how to use the project, its CLI, and its public subsystems
- it should not primarily explain how to change or develop the project itself
- for contributor/development work, `AGENTS.md` and `Agentos.Dev.Notes` are the more appropriate surfaces

Source-of-truth rule:

- `Usage.Skill` should derive from `Agentos.Index.Notes` and other canonical public surfaces rather than define independent durable design truth

## Md.Surface

Topic framing: define the markdown design surface for a system.

Current direction: `Md.Surface` is the markdown-implemented part of a project: the part of the system expressed through notes, skills, and other markdown-defined coordination surfaces. It is the system explained through markdown concepts, constraints, relationships, patterns, and intended behavior.

`Md.Surface:Agentos` means the markdown part of the Agentos project itself. In practice this includes all `notes/**`, the skill system, and related markdown coordination surfaces. The existence of this concept is useful for communication because it gives a scoped boundary for work such as review, drift checks, naming cleanup, or consistency checks across the markdown part of a project.

Relation to index notes:

- `Md.Surface` is broader than `Agentos.Index.Notes`.
- `Agentos.Index.Notes` is one major subsystem inside the md surface.
- `notes/index/` is the current primary durable concept-surface pattern inside that subsystem.

## Agentos.Dev.Notes

`Agentos.Dev.Notes` is the internal development markdown surface for a project.

It explains how to develop, modify, inspect, operate, and maintain the project: commands, local conventions, implementation notes, environment assumptions, repository structure, and maintainer workflows. It is not the public design SSOT and not the external usage surface.

Current surface model:

- `AGENTS.md` is the main internal development entry/router
- `notes/dev/` can hold durable development notes that are too detailed or specific for `AGENTS.md`
- `notes/live/` holds transient exploration and live artifacts
- `Usage.Skill` holds external usage orientation

Boundary rule:

- `Agentos.Dev.Notes` is for internal development work
- `Usage.Skill` is for external project usage
- `Agentos.Index.Notes` is for public design truth
- if durable design truth is repeatedly being sourced from `Agentos.Dev.Notes`, it should probably be promoted into `Agentos.Index.Notes`

## Reserved.Notes

`Reserved.Notes` are notes with reserved roles in an Agentos system.

They exist because some markdown files are not just ordinary notes in a folder. They are named surfaces with special responsibilities, stable discovery expectations, and often fixed numeric prefixes.

Core idea:

- a reserved note has a known system purpose
- reserved notes typically use fixed numeric values
- fixed numbers make the note easy to discover and reference across agents, skills, and workflows
- reserved notes can exist in different note surfaces, such as `notes/index/` or `notes/live/`

Current Agentos examples:

- `notes/index/000-index.md` is a reserved index routing note
- `notes/live/010.TODOS.md` is a reserved live TODO note

Related concept:

- `Fix.Live.Note` is a live-note form reserved for collecting stateful data in a known place
- `TODOS.Note` is one concrete `Fix.Live.Note`

## File.Numbering.Protocol

`File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces.

It builds on the shared Agentos file-numbering base: canonical numeric prefixes are three digits, assigned prefixes are stable, gaps are allowed, allocation is append-only, and existing numbered files should not be renumbered.

Purpose:

- numbers provide short handles for files
- numbers provide a stable addressing index even when the descriptive title changes
- file titles may be renamed, but the numeric prefix should remain stable
- stable numbering reduces maintenance cost for links, references, and agent navigation

Current range model:

- `000-099`: reserved files with fixed system roles
- `100-499`: rolling index notes
- `500-999`: rolling other files, including live notes and live scripts

Project-wide uniqueness:

- file numbers should be unique across the relevant project surface
- uniqueness is not only per folder or per note type
- the same numeric prefix should not identify different addressable files inside the same numbered surface

CLI support:

- numbering should be aided by the project CLI
- CLI allocation/checking should preserve append-only behavior and avoid gap-filling
- deterministic checks should help detect duplicate numbers, out-of-range files, and accidental renumbering

Current Agentos applications:

- `Reserved.Notes` use reserved fixed numbers such as `000` and `010`
- `Agentos.Index.Notes` uses rolling index-note numbers in `100-499`
- ordinary live notes use rolling numbers in `500-999`
- `Live.Scripts` also use rolling numbers in `500-999`

## TODOS.Note

`TODOS.Note` is a `Fix.Live.Note` used as a common markdown holding surface for lightweight deferred work.

It collects TODOs, reminders, and follow-up items as small md blocks with minimal status. Its purpose is low-friction capture: when design, maintenance, or implementation work reveals something that should not be handled immediately, it can be parked in the TODO surface for later review.

Core rules:

- each TODO should be one small md block
- TODOs may use a simple status such as `open`, `doing`, `done`, or `dropped`
- the note is stateful, but intentionally lightweight
- it is a common place for reminders, not a full task-management system
- it is not the design SSOT, a progress dashboard, or a replacement for issue reports

Current Agentos pattern:

- `notes/live/010.TODOS.md` is the current TODO surface
- TODO blocks can be added there during design-session, maintenance, or implementation work
- later passes may promote TODOs into issue reports, implementation requests, index-note changes, or remove them when obsolete

## Live.Scripts

`Live.Scripts` are low-friction script-shaped working surfaces for executable or executable-looking project exploration.

They mirror `Live.Notes`, but for script-shaped thinking. Live notes capture markdown thinking; live scripts capture executable drafts, fake or real interface usage, probes, prototypes, demos, checks, experiments, rolling interfaces, and target-surface sketches while the project is still evolving.

Runnable status:

- live scripts may be runnable
- live scripts may be partially runnable
- live scripts may be intentionally fake
- fake scripts are valid when they define a target surface, usage example, or desired interaction
- when useful, live scripts can later become prompts for implementation discussion, such as "what is necessary to make this work?"

Purpose:

- define target interfaces by example
- communicate desired usage or behavior
- stress a design before implementation exists
- support executable exploration when running the script is useful
- create candidate surfaces that may later graduate into `Project.CLI`, tests, demos, docs, or implementation code

Current Agentos pattern:

- live scripts live under `dev/live/`
- ordinary live scripts use the shared `File.Numbering.Protocol`
- their canonical ordinary filename shape is `NNN-short-topic.<ext>`
- `500-999` is the current rolling range for ordinary live scripts

Boundary:

- `Live.Scripts` are not the durable design SSOT
- durable design discovered through live scripts should be promoted into `Agentos.Index.Notes`
- stable reusable project commands should eventually move toward `Project.CLI` or another public implementation surface

## Stub.Convention

`Stub.Convention` allows an intentionally incomplete index entry only when it still carries enough durable signal to be useful.

A stub can reserve a named concept, problem space, or surface area before the design is fully mature. It must make incompleteness explicit, but it should still meet a minimal bar of usefulness.

Minimum bar:

- the concept or problem space is real
- the name or scope is worth preserving
- there is at least a short useful definition
- the incompleteness is explicit
- the stub gives future work a direction

What this is not:

- not a placeholder with only a title
- not a TODO list
- not a design-session substitute
- not a place for many unresolved ideas
- not a dumping ground for early exploration

Minimal index-note form:

```md
## Concept.Name

Status: Stub

Short definition of the concept or problem space in one paragraph.

Known:
- one or two durable facts or constraints

Open:
- one or two questions that explain why this is incomplete
```

Minimal registry form:

```md
### Concept.Name

Status: Stub

One-paragraph definition of the known concept boundary. Open: one sentence naming what is not settled.
```

Boundary:

- a stub must still be an index note or index block
- if it does not contain enough information to guide future judgment, it belongs in a design session, design summary, live note, or `TODOS.Note` instead
- maintenance may later enrich, merge, rename, promote, or remove the stub

## Canonical.Reference.Implementation

Topic framing: define a general design principle for using a preferred concrete implementation as an exemplar for an md-defined system.

Current direction: `Canonical.Reference.Implementation` is a preferred concrete implementation used to illustrate, test, and reduce drift from an `Md.Surface`. It is not the authority. Canonical means preferred reference, not governing source of truth. The md surface defines the intended system; the canonical reference implementation demonstrates one preferred realization; other implementations may diverge when they still satisfy the md surface or have a good reason.

Authority relation:

- `Md.Surface` is the source of truth for the design.
- `Canonical.Reference.Implementation` is the preferred concrete exemplar.
- Other implementations compare against both, but the md surface wins when they disagree.

## Agentos.Notes.Structure

`Agentos.Notes.Structure` defines how Agentos note surfaces are organized under their root folders.

The basic model is root-folder ownership: a note surface owns everything under its root. By default, Agentos uses a flat layout such as `notes/index/NNN-topic.md` or `notes/live/NNN-topic.md`, but complex projects may introduce subfolders without changing the note-surface identity of the files inside them.

Core rules:

- each note surface has a root folder
- files under that root belong to that note surface unless a more specific protocol says otherwise
- flat layout is the default because it is easy to scan and maintain
- subfolders are allowed when they reduce noise or improve navigation
- subfolders should not create a separate note type by themselves
- moving a note into a subfolder should not change its conceptual role

Examples:

- `notes/index/100-agentos-index-notes.md` is an index note
- `notes/index/subsystem/120-example.md` is still an index note
- `notes/live/500-design-session.md` is a live note
- `notes/live/archived/500-old-session.md` is still a live note, but archived for noise reduction

Reserved paths:

- reserved notes typically have fixed paths
- `notes/index/000-index.md` is the reserved index routing note
- `notes/live/010.TODOS.md` is the reserved TODO live note
- fixed paths provide stable discovery for agents, skills, and workflows

Local agent guidance:

- note root folders may contain their own `AGENTS.md`
- local `AGENTS.md` files can remind agents what kind of note surface they are in
- they can state expected behavior, routing, reserved paths, and important constraints
- this is intentionally redundant with higher-level guidance when it improves local agent behavior
- a local `AGENTS.md` inside a note root is part of `Agentos.Dev.Notes`, not a competing design SSOT
- durable design truth should still be promoted into `Agentos.Index.Notes`

Structure principle:

- root folders define note-surface identity
- subfolders organize volume
- reserved notes define stable system entry points

## Notes

- `Agentos.Ontology.Workflows` emerged as a likely dedicated note because the concept lifecycle and maintenance patterns need more than a small section in the ontology registry.
- `Ontology.Registry` is preferred over `Ontology.Note` because the artifact is primarily an inventory and orientation surface, not necessarily the full definition site for every concept.
- Agents should use `Ontology.Registry` actively during discussion: when a user uses an approximate concept name or forgets the exact one, the agent should check for the registered name and introduce it back into the conversation.
- `Agentos.Index.Notes` should preserve low write friction from the existing foundation: useful ideas can be written before they have the desired integrated shape, then refactored by later maintenance passes.
- The desired stable form of an index note and the acceptable work-in-progress capture form are different concerns; this now relates to the broader `Design.Target.Model` / `Current.Implementation` cluster.
- Putting new material in the index is part of the discovery mechanism: once present, it naturally triggers review, exposes misalignments, and gives future agents concrete material to improve.
- Working draft for the future `Agentos.Index.Notes` note: `502-agentos-index-notes-draft.md`.
- Deprecated `agentos-index-mdblock-base` contains reusable prior art, but the redesign separates general `Md.Block` from index-specific `Index.Block`.
- `Maintenance.System:Agentos` introduces a new notation pattern: `Concept.Name:Instance`, where the colon part names the target or instance while preserving the same underlying concept.
- `Project.CLI` is distinct from `Maintenance.System`: maintenance workflows may use CLI commands, but the CLI is a broader public project surface.
- `Canonical.Reference.Implementation` is a general design concept, not Agentos-specific. Agentos workflows can be used to develop systems that have their own md surfaces and reference implementations.
- If a source outside `notes/index/` is repeatedly being used as a source of durable design truth, that material should probably be promoted into `Agentos.Index.Notes`.
- `Ontology.Registry` needs a dedicated maintained note shape: one small block per concept, low-resolution definitions, and routing toward fuller notes.
- the ontology registry note should stay about concepts; the registry format should live in a separate note.
- `Reserved.Notes` names the special-purpose notes with fixed discovery roles, such as `notes/index/000-index.md` and `notes/live/010.TODOS.md`.
- `File.Numbering.Protocol` treats numeric prefixes as stable handles for addressable files, with `000-099` reserved, `100-499` for rolling index notes, and `500-999` for rolling other files such as live notes and live scripts.
- `TODOS.Note` exists to park follow-up work explicitly for later review and reuse.
- `Live.Scripts` mirror live notes for executable drafts, probes, prototypes, demos, checks, or rolling interfaces.
- `Stub.Convention` preserves incomplete but meaningful index concepts while rejecting title-only placeholders and vague dumps.
- `Agentos.Notes.Structure` generalizes note organization around root-folder ownership, optional subfolders, reserved paths, and local `AGENTS.md` guidance.
- registry lookup should be opportunistic rather than mandatory for all agent work.

## End Log

- 2026-05-03: Created initial design-session document with approved topic list and started discussion on `Agentos.Ontology.Workflows`.
- 2026-05-03: Added `Agentos.Maintenance.System` as a design item and clarified that ontology lifecycle stages are explanatory, not explicit per-concept state tracking.
- 2026-05-03: Updated `Agentos.Ontology.Workflows` with converged definition and marked it `needs-approval`.
- 2026-05-03: Added `Index.Note.Style` as a design item and captured low-friction writing versus desired stable shape as an open design concern.
- 2026-05-03: Added `Desired.Outcome` as a general design concept item.
- 2026-05-03: Created `502-agentos-index-notes-draft.md` as a live-note draft of the future `Agentos.Index.Notes` note.
- 2026-05-03: Added first-draft `Index.Note.Style` definition and split `Md.Block` from `Index.Block`.
- 2026-05-03: Added `Dotted.Notation` as a design item and reframed `Agentos.Maintenance.System` as the general `Maintenance.System` concept with `Maintenance.System:Agentos` as an instance reference.
- 2026-05-03: Updated `Index.Note.Style` with converged wording and marked it `needs-approval`; `502-agentos-index-notes-draft.md` is the first accepted format test.
- 2026-05-03: Updated `Dotted.Notation` with base dotted-name rules, `Dotted.Parameterized.Notation`, dotted parameters, registry treatment, and marked it `needs-approval`.
- 2026-05-03: Added `Project.CLI` and `Public.Surface` as design items and clarified that `agentos doctor ...` is a command exposed through `Project.CLI:Agentos`.
- 2026-05-03: Updated `Maintenance.System` with converged definition and marked it `needs-approval`.
- 2026-05-03: Added `Md.Surface` and `Canonical.Reference.Implementation` as general design concept items.
- 2026-05-03: Migrated item states to the newer design-session model: `fresh`, `in-progress`, and `converging`.
- 2026-05-03: Added `Agentos.Dev.Notes` and captured the promotion heuristic for repeated non-index sources of durable design truth.
- 2026-05-03: Moved `Agentos.Index.Notes` to `converging`.
- 2026-05-03: Replaced `Desired.Outcome` with the `Design.Target.Model` / `Current.Implementation` / `Progress.Gradient` / `Design.Implementation.CoEvolution` cluster.
- 2026-05-03: Closed the `Design.Target.Model` / `Current.Implementation` / `Progress.Gradient` / `Design.Implementation.CoEvolution` cluster as sufficient for this session.
- 2026-05-03: Closed `Project.CLI`, `Public.Surface`, `Md.Surface`, and `Canonical.Reference.Implementation` at concept level for this session.
- 2026-05-03: Expanded `Agentos.Index.Notes` into its umbrella subsystem definition, detailed `Agentos.Index.Ontology.Registry`, added the `Agentos.Dev.Notes` boundary rule, and added `TODOS.Note`.
- 2026-05-03: Added `Usage.Skill`, made it derive from `Agentos.Index.Notes`, separated registry concepts from registry-format documentation, and made ontology-registry lookup explicitly opportunistic.
- 2026-05-03: Closed `Agentos.Index.Notes`, `Index.Note.Style`, `Agentos.Index.Ontology.Registry`, `Agentos.Ontology.Workflows`, `Dotted.Notation`, and `Maintenance.System` as sufficient for this session.
- 2026-05-03: Expanded `Usage.Skill` into the public usage-surface model and closed it as sufficient for this session.
- 2026-05-03: Added `Reserved.Notes` as the concept for special-purpose notes with fixed discovery roles, including `000-index.md` and `010.TODOS.md`.
- 2026-05-03: Added `Notes.Numbering.Protocol` as the project-wide md-surface note numbering model with reserved and rolling ranges.
- 2026-05-03: Closed `Reserved.Notes` and `TODOS.Note` as sufficient for this session.
- 2026-05-03: Generalized `Notes.Numbering.Protocol` into `File.Numbering.Protocol` and added `Live.Scripts`.
- 2026-05-03: Closed `Agentos.Dev.Notes` after clarifying it as the internal development markdown surface, distinct from external usage and public design truth.
- 2026-05-03: Closed `File.Numbering.Protocol` as sufficient for the current generalized numbering model.
- 2026-05-03: Closed `Live.Scripts` after defining fake, partial, and runnable scripts as valid script-shaped working surfaces.
- 2026-05-03: Closed `Agentos.Index.Writing.Principles` after defining writing judgment around future judgment, rationale, exclusions, high signal, rough capture, and style separation.
- 2026-05-03: Renamed `Agentos.Index.Structure` to `Agentos.Notes.Structure` and closed it after defining root folders, optional subfolders, reserved paths, and local `AGENTS.md` guidance.
- 2026-05-03: Extracted the external project integration topic into a project-local design summary and removed it from this Agentos design session.
- 2026-05-03: Added and closed `Stub.Convention` as a minimal-completeness rule for incomplete but meaningful index entries.
