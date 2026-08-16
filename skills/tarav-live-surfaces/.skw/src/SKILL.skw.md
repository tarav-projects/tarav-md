> $kw: ^agentos-root-reachability --reachable-from @<tarav-pkg>/SKILL.md

---
name: tarav-live-surfaces
description: "Live surface protocols for notes and scripts. USE WHEN the user mentions live-note, live-script, live surface, or needs canonical location, naming, or numbering for notes/live/ or dev/live/."
---

# Agentos Live Surfaces

Minimal protocols for live notes and live scripts — the two numbered live surfaces in an agentos project.

This skill operationalizes `Agentos.Live.Note` and `Agentos.Live.Script` naming and location behavior derived from `File.Numbering.Protocol`. The durable concepts live in `tarav-pkg/design/100-design.md`; operational numbering details live in `tarav-pkg/references/file-numbering-protocol.md`.

This is a `Batchy.Skill`. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.

## Scope

- Define only live surface location and naming.
- Do not define note body structure or script content structure.
- Do not assume a specific programming language for scripts.
- Treat live scripts as alignment surfaces for small code snippets that the user can inspect and critique. Runnable status is optional.

## Live Notes

- Store live notes in `notes/live/`.
- Canonical filename pattern: `NNN-short-topic.md`.
- `NNN` must be zero-padded 3 digits.
- Numeric prefixes are stable note handles and must not be changed after assignment.
- Gaps are allowed. Do not renumber existing notes to fill gaps.

## Live Scripts

- Store live scripts in `dev/live/`.
- Canonical filename pattern: `NNN-short-topic.<ext>`.
- `NNN` must be zero-padded 3 digits.
- Use the extension that matches the project language or execution model.
- Numeric prefixes are stable handles and must not be changed after assignment.
- Gaps are allowed. Do not renumber existing scripts to fill gaps.
- `dev/live/archive/` may be used as an archive location for rolled scripts.

## Numbering Ranges

Agentos note numbering uses a project-wide md-surface protocol:

- `000-099`: reserved notes with fixed system roles
- `100-499`: rolling index notes
- `500-999`: rolling other notes, including ordinary live notes and live scripts

Live surface implications:

- Ordinary agent-created live notes and scripts should use `500-999`.
- Reserved surfaces may use fixed values in `000-099`.
- Example reserved live notes: `notes/live/010.TODOS.md`, `notes/live/011.ISSUES.md`, `notes/live/012.NOTEBOOK.md`.
- Numbers should be unique across the project md surface, not only inside their folder.

## Prefix CLI

- Tool: `tarav stdlib prefix next`
- Agents can call this directly from the terminal.
- Purpose: print the next ordinary prefix as 3 digits.
- Empty/no-match behavior: print `500`.
- Allocation route: `500-999`.
- Default project scan scope: `notes` and `dev/live`.
- If `tarav stdlib prefix` fails, stop and ask the user how to resolve the project target. Do not assign a prefix by manual inspection.

### Live Note Allocation

```sh
tarav stdlib prefix next --project-base <project-root-basename> --target notes/live
```

### Live Script Allocation

```sh
tarav stdlib prefix next --project-base <project-root-basename> --target dev/live
```

### Outside the Project Tree

Use explicit project path when the caller is outside the intended project tree:

```sh
tarav stdlib prefix next --project /path/to/project --project-base <project-root-basename> --target <path>
```

In nested workspaces or sibling repositories, do not use `--project .` unless `.` is the actual initialized project root. Use `--project-base` so allocation fails if the wrong project was resolved.

> $kw: --from Agentos.Live.Note
> $kw: --from Agentos.Live.Script
> $kw: --from Batchy.Skill
> $kw: --from File.Numbering.Protocol
