---
name: agentos-live-note-base
description: Define the live-note protocol for path and filename conventions. Use when the user mentions `live-note` or needs the canonical live-note location and numbering workflow. Uses `agentos` to allocate the next live-note prefix.
---

# Agentos Live Note Base

Minimal protocol for live notes.

This skill operationalizes live-note naming and location behavior derived from `notes/index/103-File.Numbering.Protocol.md`. The index note is the durable design source; this skill is workflow guidance.

## Scope
- This skill defines only live-note location and naming.
- This skill does not define note body structure.
- This skill follows the current `File.Numbering.Protocol` direction, but does not claim the repository is fully migrated to project-wide numbering yet.

## Live Note Protocol
- Live notes must be stored in `notes/live/`.
- Canonical ordinary live-note filename pattern: `NNN-short-topic.md`.
- `NNN` must be zero-padded 3 digits.
- Numeric prefixes are stable note handles and must not be changed after assignment.
- Gaps are allowed. Do not renumber existing notes to fill gaps.

## Numbering Ranges

Agentos note numbering is moving toward a project-wide md-surface protocol:

- `000-099`: reserved notes with fixed system roles
- `100-499`: rolling index notes
- `500-999`: rolling other notes, including ordinary live notes

Live-note implications:

- Ordinary agent-created live notes should use `500-999`.
- Reserved live notes may use fixed values in `000-099`.
- Example reserved live note: `notes/live/010.TODOS.md`.
- Note numbers should be unique across the project md surface, not only inside `notes/live/`.

## Migration Status

- Current CLI allocation is project-aware through `agentos prefix next --project <project> --target notes/live`.
- The default project prefix policy scans numbered Agentos surfaces under `notes` and `dev/live`, then allocates from the rolling `500-999` route for `notes/live`.
- Reserved names such as `010.TODOS.md` are manually assigned fixed-role prefixes. They are part of the numbering system but not ordinary allocator output.
- Full consistency checks for duplicate numeric prefixes, range violations, and reserved-prefix drift are future `prefix doctor` or equivalent work.

## Prefix CLI
- Tool: `agentos prefix next`
- Agents can call this directly from the terminal.
- Purpose: print the next ordinary live-note prefix as 3 digits.
- Empty/no-match behavior: print `500`.
- Allocation route: `500-999`.
- Target: `notes/live`.
- Default project scan scope: `notes` and `dev/live`.

## Usage
Run from the initialized Agentos project root:

```sh
agentos prefix next --project . --target notes/live
```

Explicit project target:

```sh
agentos prefix next --project /path/to/repo --target notes/live
```
