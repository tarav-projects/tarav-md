# File.Numbering.Protocol

`File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces.

The protocol treats numeric prefixes as stable handles. The descriptive title may change, but the numeric prefix should not be renumbered once assigned.

## Purpose

Numbers provide:

- short handles for files
- stable addressing even when titles improve
- lower maintenance cost for links and references
- easier navigation for humans and agents
- deterministic support for allocation and validation

## Base Rules

- canonical numeric prefixes use three digits
- assigned prefixes are stable
- gaps are allowed
- allocation is append-only
- do not fill old gaps just because they exist
- do not renumber existing files to make the sequence cleaner

## Current Range Model

- `000-099`: reserved files with fixed system roles
- `100-499`: rolling index notes
- `500-999`: rolling other files, including live notes and live scripts

The range model is current Agentos design, not a universal markdown rule for every project.

## Project-Wide Uniqueness

File numbers should be unique across the relevant project surface.

The same numeric prefix should not identify two different addressable files inside the same numbered surface. This matters because numeric prefixes are used as stable shortcuts and addressing handles, not just local sorting decorations.

## CLI Support

The protocol should be aided by `Project.CLI`.

For Agentos, `agentos prefix` already exists as a deterministic helper. The desired direction is project-wide checking and allocation support for numbered surfaces, including:

- duplicate numeric prefixes
- range violations
- accidental renumbering
- append-only allocation behavior
- transitional checks while legacy surfaces are still being migrated

## Current Agentos Applications

- `notes/index/000-index.md` is a reserved routing note.
- `notes/live/010.TODOS.md` is a reserved TODO note.
- new stable index notes should use `100-499`.
- ordinary live notes should use `500-999`.
- ordinary live scripts should use `500-999`.

## Related Concepts

- `Reserved.Notes`
- `Agentos.Index.Notes`
- `TODOS.Note`
- `Live.Scripts`
- `Project.CLI`

## Provenance

Promoted from the closed design session at `../live/501-agentos-index-notes-design-session.md`.

