# Agentos Ontology Registry

Low-resolution registry of named concepts in the Agentos markdown design surface.

This registry is for orientation and concept lookup. It records what concepts exist, gives each one a compact definition, and points to fuller notes when they exist. It is not the place for deep treatment of every concept.

## Core Agentos Concepts

### Agentos

Agentos is an operating system for agent-oriented work: a modular but integrated set of conventions, workflows, tools, notes, skills, and public surfaces for developing and using projects with agents.

### Agentos.Stack

`Agentos.Stack` is the abstract Agentos model a project can adopt: project identity, notes, skills, public surfaces, maintenance, CLI hooks, ontology, live surfaces, and related workflow primitives.

### Agentos.Implementation

`Agentos.Implementation` is the concrete implementation of Agentos itself. It includes components such as `agentos-md`, `agentos-py`, and future repos or packages that implement the Agentos framework.

### Agentos.Project

`Agentos.Project` is a concrete project that adopts `Agentos.Stack`. It is detected by `.agentos/project.json` and can be inspected by Agentos commands and workflows. See `105-Agentos.Project.md`.

### Agentos.Project.Marker

`Agentos.Project.Marker` is the canonical filesystem proof that a directory is an `Agentos.Project`: `.agentos/project.json`. See `105-Agentos.Project.md`.

### Agentos.Project:agentos-py

`Agentos.Project:agentos-py` means `agentos-py` viewed as a concrete project adopting the Agentos project model.

### Project.Discovery.System

`Project.Discovery.System` resolves commands and workflows to an `Agentos.Project` target while separating project identity, discovery mechanics, and command policy. See `105-Agentos.Project.md`.

### Agentos.Project.Doctor

`Agentos.Project.Doctor` is a diagnosis-first workflow for evaluating how well a concrete `Agentos.Project:<target>` conforms to `Agentos.Stack`. See `108-Agentos.Project.Doctor.md`.

### Agentos.Implementation:agentos-py

`Agentos.Implementation:agentos-py` means `agentos-py` viewed as part of the concrete implementation of Agentos.

### Agentos.Skills

`Agentos.Skills` defines skill selection, routing, and import behavior for Agentos projects. See `106-Agentos.Skills.md`.

### Agentos.Mission

`Agentos.Mission` is a lightweight coordination surface for named blocks of work. It is opt-in coordination, not a full project-management system. See `107-Agentos.Mission.md`.

### Hugentic

`Hugentic` describes a system, surface, workflow, or project designed for the human-agentic interface: humans and agents coordinating, exchanging context, making decisions, and co-working through explicit surfaces.

### Agentos.Soft.Subsystem

`Agentos.Soft.Subsystem` is a named responsibility area inside `Agentos.Stack`. It is an orientation surface, not a hard ownership container; components may participate in multiple soft subsystems.

### Agentos.Subsystem.Model

`Agentos.Subsystem.Model` defines how Agentos subsystems are named, documented, related, and represented as overlapping conceptual responsibility areas rather than folder, repo, package, or command ownership boundaries.

### Agentos.Subsystem.Registry

`Agentos.Subsystem.Registry` is the subsystem namespace/subregistry inside `Agentos.Index.Ontology.Registry`. It gives a low-resolution map of subsystem concepts and can live as a `## Subsystems` section or a linked-out index note if it grows.

## Subsystems

### Agentos.Hugentic.Flow

`Agentos.Hugentic.Flow` is the human-agent project-development subsystem. It includes workflows and surfaces such as design sessions, durable index notes, live notes, TODO notes, project doctor passes, artifact handoffs, and related workflow skills. See `001-Agentos.Hugentic.Flow.md`.

### Agentos.Project.System

`Agentos.Project.System` is the subsystem for project identity, discovery, targeting, and project-scoped Agentos behavior. See `105-Agentos.Project.md`.

### Agentos.Skill.System

`Agentos.Skill.System` is the subsystem for reusable agent behaviors, skill routing, profile selection, import, and project-local skill depots. See `106-Agentos.Skills.md`.

### Agentos.CLI.System

`Agentos.CLI.System` is the subsystem for deterministic command surfaces that support humans, agents, scripts, and other Agentos workflows.

### Agentos.Chatlas

`Agentos.Chatlas` is the subsystem for working with chat-session data as a durable project resource for continuity, audit, and history-aware workflows.

### Agentos.Tape.System

`Agentos.Tape.System` is the subsystem for tape-like durable traces and structured records used by Agentos workflows.

### Agentos.Forum

`Agentos.Forum` is the subsystem for shared local communication surfaces that support multi-agent or asynchronous coordination.

### Agentos.Iterante

`Agentos.Iterante` is the subsystem for iterative agent execution workflows that can support or automate Agentos work.

### Design.Target.Model

`Design.Target.Model` is the current explicit design model of a system. In Agentos-style projects, it is defined in `Agentos.Index.Notes`.

### Current.Implementation

`Current.Implementation` is the current realized state of a system. It may live in code, CLI, skills, data, notes, or any combination depending on the project type.

### Progress.Gradient

`Progress.Gradient` is the current best direction of movement between `Current.Implementation` and `Design.Target.Model`. Being unfinished is acceptable when a credible gradient exists.

### Design.Implementation.CoEvolution

`Design.Implementation.CoEvolution` is the development dynamic where design understanding and implementation reshape each other. Progress means co-developing `Design.Target.Model` and `Current.Implementation`.

## Markdown Surfaces

### Md.Surface

`Md.Surface` is the markdown-implemented part of a project: the system as expressed through notes, skills, and other markdown-defined coordination surfaces. See `101-Md.Surface.md`.

### Md.Surface:Agentos.Stack

`Md.Surface:Agentos.Stack` is the markdown design surface for the abstract Agentos stack model, currently centered in `agentos-md` and including notes, skills, and related markdown coordination surfaces.

### Md.Surface:Agentos.Implementation

`Md.Surface:Agentos.Implementation` is the markdown surface about the concrete implementation of Agentos itself when that needs to be distinguished from the abstract stack model.

### Agentos.Index.Notes

`Agentos.Index.Notes` is the durable concept-note subsystem of an Agentos-style project and the SSOT for public markdown-surface design knowledge. See `100-Agentos.Index.Notes.md`.

### Index.Note

`Index.Note` is a durable note unit inside `Agentos.Index.Notes`, usually centered on one named concept or a tight concept cluster.

### Index.Block

`Index.Block` is the index-specific use of `Md.Block`: a high-signal block carrying one steering idea inside an index note.

### Md.Block

`Md.Block` is a general markdown primitive: a heading-scoped markdown unit that can be moved, referenced, reviewed, or reused across markdown surfaces.

### Index.Note.Style

`Index.Note.Style` is the desired mature shape for stable index notes: concept-centered, block-structured, high-signal, low-prose, self-locating, refactorable, and loss-checked.

### Agentos.Index.Writing.Principles

`Agentos.Index.Writing.Principles` defines the judgment for what belongs in durable index notes: concepts, rationale, constraints, naming conventions, reusable patterns, steering decisions, boundaries, consequences, and exclusions.

### Agentos.Index.Ontology.Registry

`Agentos.Index.Ontology.Registry` is the maintained concept inventory for an Agentos index surface. The default registry file is `ontology.md`; larger projects may split into additional `*-ontology.md` files.

### Agentos.Ontology.Workflows

`Agentos.Ontology.Workflows` describes how concepts emerge, get named, enter the registry, receive dedicated notes, get renamed, and are maintained through agent discussion and maintenance work.

### Agentos.Dev.Notes

`Agentos.Dev.Notes` is the internal development markdown surface for how to develop, modify, inspect, operate, and maintain a project. It is distinct from public usage and durable design truth.

### Agentos.Notes.Structure

`Agentos.Notes.Structure` defines note-surface organization by root-folder ownership, optional subfolders, reserved paths, and local `AGENTS.md` guidance.

### Reserved.Notes

`Reserved.Notes` are notes with fixed system roles and stable discovery expectations, such as `notes/index/000-index.md` and `notes/live/010.TODOS.md`.

### TODOS.Note

`TODOS.Note` is a lightweight reserved live note for parking TODO blocks and deferred work without turning the index into progress tracking.

### Live.Scripts

`Live.Scripts` are script-shaped working surfaces for executable or executable-looking exploration, including runnable scripts, partial scripts, fake target-surface sketches, probes, prototypes, demos, and checks.

### Stub.Convention

`Stub.Convention` allows incomplete index entries only when they still contain minimal durable signal: a real concept boundary, short definition, explicit incompleteness, and useful direction for future work.

## Naming And References

### Dotted.Notation

`Dotted.Notation` identifies named concepts in an ontology surface. Dotted names mark concepts, not casual prose. See `102-Dotted.Notation.md`.

### Dotted.Parameterized.Notation

`Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept, using `Concept.Name:Target`.

## Project Surfaces

### Project.CLI

`Project.CLI` is a project-owned command surface for deterministic operations, checks, transformations, and utilities used by agents and humans.

### Project.CLI:Agentos

`Project.CLI:Agentos` is the Agentos CLI, exposed through the `agentos` command.

### Public.Surface

`Public.Surface` is the set of stable project-facing surfaces that agents and humans can rely on, such as a project CLI, usage skills, index notes, and documented artifacts.

### Usage.Skill

`Usage.Skill` is a public usage surface that explains what a project is, what public interfaces it exposes, and how an external agent or user should use them.

### Canonical.Reference.Implementation

`Canonical.Reference.Implementation` is a preferred concrete implementation used as an exemplar for an md-defined system. It is not the authority; the markdown surface remains the source of truth.

## Maintenance And Numbering

### Maintenance.System

`Maintenance.System` defines how a project surface is diagnosed over time through doctor skills, subsystem checks, and deterministic CLI support when available. See `104-Maintenance.System.md`.

### Maintenance.System:Agentos

`Maintenance.System:Agentos` is the Agentos instance of `Maintenance.System`, likely centered on an `agentos-project-doctor` skill and `agentos doctor ...` CLI checks.

### Doctor.Check

`Doctor.Check` is one test-like evaluation inside a doctor workflow. It returns a structured outcome such as `pass`, `fail`, `warn`, `skip`, or `unknown`, with evidence.

### Doctor.CLI

`Doctor.CLI` is the deterministic executable doctor layer. It runs repeatable checks and should be useful by itself for humans, shell scripts, CI, and skills.

### Doctor.Skill

`Doctor.Skill` is the agentic doctor layer. It can define checks, call `Doctor.CLI`, interpret mixed results, and synthesize diagnosis reports.

### File.Numbering.Protocol

`File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces. See `103-File.Numbering.Protocol.md`.
