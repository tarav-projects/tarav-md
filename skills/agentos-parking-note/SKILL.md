---
name: agentos-parking-note
description: "Capture an idea, todo, or issue into a project Parking.Note through a short discussion. Use when the user wants to quickly park a thought without actioning it."
---

# Agentos Parking Note

Short-lived workflow for capturing a thought into a project `Parking.Note`.

The user presents an idea. The agent discusses it briefly, drafts a `Kernel.Block`-style entry, proposes a target file, and writes on approval.

## Activation

Use when the user wants to park an idea, todo, issue, or observation for later. Typical phrases: "park this", "notebook this", "I want to capture an idea", or an explicit `$parking-note` invocation.

## Parking.Note Files

Each project may have these reserved files under `notes/live/`:

| File | Role |
|---|---|
| `012.NOTEBOOK.md` | Catch-all — ideas, observations, design seeds, anything |
| `010.TODOS.md` | Something to do |
| `011.ISSUES.md` | Something wrong |

`012.NOTEBOOK.md` is the default. Nothing is out of place in NOTEBOOK.

## Workflow

1. The user presents whatever they have — a sentence, a paragraph, a vague notion.
2. The agent drafts a block and picks a target file.
3. The agent shows the draft: the proposed block, the target file path, and a follow-up question about something missing or unclear.
4. The user refines, redirects the target, or approves.
5. Repeat until the user approves.
6. The agent writes the block to the target file.

The workflow is short-lived. It ends after the write.

## Block Format

Entries follow `Kernel.Writing` style with relaxed constraints:

- Heading uses `Dotted.Notation` based on the note content (e.g. `## Idea.About.Fish.Based.APIs`)
- Each line describes an independent facet — direct, orthogonal
- No space budget — write as much as the idea needs
- Free to include tags, links, context, or any useful material
- No required metadata fields

Example:

```md
## Fish.Based.APIs

- a single gateway with species-aware routing could unify the aquatic data layer
- the current approach fragments marine endpoints across three services
- simplifying the client SDK is the main motivation
- related to the marine-data project discussion
```

## Draft Presentation

When showing the draft to the user, include:

- The target file as a full path from `~` (e.g. `~/projects/agentos-project/agentos-py/notes/live/012.NOTEBOOK.md`) — removes ambiguity in multi-project workspaces
- The proposed block (heading + body)
- One follow-up question about something missing or unclear

The user may approve, edit the block, or redirect to a different target file.

## File Creation

If the target file does not exist, create it with a minimal header before writing:

- `010.TODOS.md` → `# TODOs`
- `011.ISSUES.md` → `# Live Issues`
- `012.NOTEBOOK.md` → `# Notebook`
