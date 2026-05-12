# Agentos Ontology Registry

## Index.Note

- `Index.Note` is the structural index of `notes/index/`
- lists what files exist in the index folder and how to navigate them
- maps the file tree, not the conceptual model — for concepts see `Index.Ontology.Note`
- reserved at `000-index.md` — stable path, always the entry point for folder orientation

****

## Index.Ontology.Note

- `Index.Ontology.Note` is the concept-space map of the Agentos index
- low-resolution registry: records what concepts exist, gives each a compact definition, points to fuller notes
- organized by `Ontology.Namespaces` — multiple overlapping views over the same concepts
- a concept lives in one file (routed by `Index.Note`) but can appear in multiple namespaces here
- not the place for deep treatment — that lives in concept notes
- reserved at `001-ontology.md` — stable path, always the entry point for concept lookup

****

## Agentos.Index.Notes

- `Agentos.Index.Notes` is the durable concept-note subsystem of an Agentos-style project
- implements the `Agentos.Index` — a `Soft.Programming.Language` for project knowledge
- see `114-Agentos.Index.Notes.md`

****

## Agentos.Index.Writing.Principles

- `Agentos.Index.Writing.Principles` defines what belongs in durable index notes
- all index content is organized as `Named.Concepts` in `Index.Blocks`
- see `114-Agentos.Index.Notes.md`

****

## Md.Surface

- `Md.Surface` is a qualifier for the markdown layer of a target
- see `115-Md.Surface.md`

****

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- see `116-Dotted.Notation.md`

****

## Dotted.Parameterized.Notation

- `Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept
- see `116-Dotted.Notation.md`

****

## File.Numbering.Protocol

- `File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces
- see `117-File.Numbering.Protocol.md`

****

## Maintenance.System

- `Maintenance.System` defines how a project surface is diagnosed over time
- see `118-Maintenance.System.md`

****

## Agentos.Project

- `Agentos.Project` is a concrete project that adopts the `Agentos.Stack` model
- see `119-Agentos.Project.md`

****

## Agentos.AGENTS.md

- `Agentos.AGENTS.md` is the project-local natural-language instruction surface at `.agentos/AGENTS.md`
- see `119-Agentos.Project.md`

****

## Project.Discovery.System

- `Project.Discovery.System` resolves a command or workflow to an `Agentos.Project` target
- see `119-Agentos.Project.md`

****

## Agentos.Skills

- `Agentos.Skills` defines skill selection, routing, and import behavior for Agentos projects
- see `120-Agentos.Skills.md`

****

## Usage.Surface

- `Usage.Surface` is the usage-useful subset of `Public.Surface`
- see `120-Agentos.Skills.md`

****

## Usage.Skill

- `Usage.Skill` is a special-purpose, usage-centric skill designed primarily as documentation
- see `120-Agentos.Skills.md`

****

## Project.Surfaces

- `Project.Surfaces` is a built-in `Ontology.Namespace` for the surfaces the index covers
- see `002-surfaces.md`

****

## Stable.Surface

- `Stable.Surface` is a durable, authoritative surface where a specific facet of project knowledge lives
- see `100-Agentos.Surfaces.md`

****

## Natural.Placement

- `Natural.Placement` is the principle that each surface holds the facet of a concept that is natural to its function
- see `100-Agentos.Surfaces.md`

****

## Index.Concept.Coverage

- the index is the collection point for all `Named.Concepts` in the project's stable surfaces
- see `114-Agentos.Index.Notes.md`

****

## Complete.Index.Block

- `Complete.Index.Block` is an `Index.Block` with an `### appendix` section for extended material
- see `114-Agentos.Index.Notes.md`

****

## Index.Appendix.Block

- `Index.Appendix.Block` is an appendix-only block hosted at `notes/appendix/`
- see `114-Agentos.Index.Notes.md`

****

## Design.Index.Block

- `Design.Index.Block` is a `Complete.Index.Block` used in `Design.Session` artifacts
- see `114-Agentos.Index.Notes.md`

