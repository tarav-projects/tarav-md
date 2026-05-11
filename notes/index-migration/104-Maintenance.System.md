# Maintenance.System

`Maintenance.System` defines how a project surface is diagnosed over time.

It coordinates project-specific doctor skills, subsystem-owned check references, and project CLI commands when deterministic support exists.

## Default Workflow

The default maintenance workflow is diagnosis-first, not fix-first.

A doctor pass should report issues with evidence and affected subsystem context, then give the user an opportunity to discuss priorities. Fixes belong to explicit follow-up workflows.

Default output should be a chat report that includes:

- problems found
- evidence
- affected subsystems
- likely importance
- suggested next discussion or follow-up work

Large or durable findings may become issue-report artifacts when the user wants a persistent issue surface.

## Check Types

Maintenance checks can be:

- agentic, when the check depends on judgment against a desired outcome
- CLI-supported, when deterministic commands can inspect the project
- mixed, when CLI output supports an agentic diagnosis

Subsystems can contribute their own checks through reference files, doctor skill sections, and CLI hooks.

## Project Skill And CLI Layering

A maintenance system usually has two aligned surfaces:

- a project doctor skill for agentic diagnosis
- a project CLI for deterministic checks and utilities

These surfaces should be independently useful but aligned around the same maintenance model.

`agentos-project-doctor` is the likely doctor skill for `Maintenance.System:Agentos`.

`agentos doctor ...` is a command exposed through `Project.CLI:Agentos`, not the general maintenance concept itself.

## Agentos Instance

`Maintenance.System:Agentos` is the Agentos maintenance-system instance.

Likely responsibilities include checking:

- index-note coherence
- ontology registry completeness
- stale dotted names
- skill drift from index concepts
- file-numbering violations
- migrated legacy surface classification
- stale paths after project moves

## Boundary

`Maintenance.System` finds and reports issues by default.

It is not primarily a fixer, progress tracker, or background automation requirement. Applying fixes should be explicit because maintenance findings often require design judgment.

## Related Concepts

- `Project.CLI`
- `Project.CLI:Agentos`
- `Agentos.Index.Notes`
- `Agentos.Index.Ontology.Registry`
- `File.Numbering.Protocol`
- `Usage.Skill`

## Provenance

Promoted from the closed design session at `../live/501-agentos-index-notes-design-session.md`.

