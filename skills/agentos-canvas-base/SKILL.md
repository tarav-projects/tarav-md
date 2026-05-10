---
name: agentos-canvas-base
description: "Agentos Canvas surface protocol and CLI usage. Use when working with `.canvas` files, creating visual project maps, or when the user mentions canvas, visual graphs, or card relationships."
---

# Agentos Canvas Base

Protocol and usage guidance for the Agentos.Canvas surface — visual project maps built on Obsidian `.canvas` files, extended with the Agentos.Canvas model layer.

The durable design source is `notes/index/110-Agentos.Canvas.md`. If this skill conflicts with the index, the index wins.

## What Canvas Is

Canvas files are shared visual artifacts: humans edit them in Obsidian, agents operate on them through the `agentos canvas` CLI or by editing the JSON directly.

Canvas is not a replacement for markdown surfaces — it expresses structure and relationships that are easier to read visually.

## Location And Naming

- Canvas files live in `notes/canvas/`.
- Canonical filename pattern: `NNN-short-topic.canvas`.
- `NNN` must be zero-padded 3 digits.
- Numeric prefixes are stable handles and must not be changed after assignment.
- Gaps are allowed. Do not renumber existing files to fill gaps.
- Note numbers should be unique across the project md surface, not only inside `notes/canvas/`.
- Allocate the next prefix via `agentos stdlib prefix next --project-base <project-root-basename> --target notes/canvas`.
- If `agentos stdlib prefix` fails, stop and ask the user how to resolve the project target. Do not assign a prefix by manual inspection.

## Obsidian Canvas Format

Read `references/obsidian-canvas-format.md` for the full Obsidian `.canvas` JSON format specification: node types, edge fields, coordinate system, color presets, and safe editing practices.

Key points:

- A `.canvas` file is JSON with `nodes` (cards) and `edges` (connections).
- Obsidian preserves unknown top-level keys and unknown fields on nodes/edges.
- Node types: `text`, `file`, `link`, `group`.
- Positions (`x`, `y`) are user-owned layout. Never overwrite existing positions unless explicitly intended.

## Two-Layer Architecture

A single `.canvas` file contains two layers:

- **Model layer** — a top-level `_model` key in the JSON. Owns topology (what exists, how it connects) and domain semantics (types, metadata). Obsidian ignores it.
- **Canvas layer** — `nodes` and `edges`. What Obsidian reads. Owns text content, positions, sizes, colors.

### SSOT By Concern

| Concern | Authority |
|---|---|
| Topology (cards, relationships) | Model layer |
| Domain semantics (types, metadata) | Model layer |
| Text content | Canvas layer |
| Positions, sizes, colors | Canvas layer |

## Model Format

The `_model` schema is used inside canvas files and as the input for `agentos canvas init`:

```json
{
  "cards": [
    {"id": "auth", "type": "module"},
    {"id": "db", "type": "module"}
  ],
  "relationships": [
    {"from": "auth", "to": "db", "type": "edge", "id": "rel: queries"}
  ]
}
```

Cards have `id` + `type` (TID.Pair). Relationships have `from`, `to`, `type` (edge/adjacent/contains), and `id` (must be a valid TID.Pair).

## Card Identity

Every card has a TID.Pair in its text as a blockquote declaration:

```md
## card title
> type: card-id
description text
```

The type is domain-defined — Agentos.Canvas does not impose type names.

## Edge Identity

Every edge label must be a valid TID.Pair (`type: id`). A TID.Pair on an edge implies a card — it does not require one. If a card with that TID.Pair exists, it elaborates the edge concept.

## Semantic Model: State-Transition Graph

The Agentos.Canvas model for workflow graphs is a state-transition graph:

- **Cards are state descriptors** — what the world looks like after an action. Named in past tense: "project oriented", "paragraphs checked", "layout risk classified".
- **Edges are operator-labeled actions** — who does what to move between states. The arrow says *who acts*. The card says *what happened*.

### The Prompt/Submit Rhythm

For Iterante mission workflows, the flow alternates between two actors:

- **Iterante** — the whole runtime side (CLI + mission.py + git)
- **Agent** — the AI doing the work

Each mission step produces a pair:

```
--iterante: prompt--> [task card] --agent: submit--> [result card]
```

The task card describes what Iterante asks. The result card describes what the agent produced. Each card earns its space by carrying information the arrow label alone cannot.

### Operator Verb Vocabulary

| Arrow | Actor | Meaning |
|---|---|---|
| `iterante: render` | Iterante | render mission instructions |
| `iterante: checkpoint` | Iterante | git commit project state |
| `iterante: prompt` | Iterante | open task for agent |
| `iterante: poll` | Iterante | structured-answer request |
| `iterante: ask` | Iterante | binary branch question |
| `iterante: evaluate` | Iterante | program-internal decision point |
| `iterante: loop` | Iterante | program routes back |
| `iterante: advance` | Iterante | program routes forward |
| `agent: submit` | Agent | complete task or poll |
| `agent: answer-yes` | Agent | resolve branch: yes |
| `agent: answer-no` | Agent | resolve branch: no |

### Card Types

| Type | Meaning |
|---|---|
| `content` | State descriptor — what the world looks like after an action |
| `question` | Decision-point state — waiting for resolution |

### Two Branch Types

- **Agent-answered branch:** `iterante: ask` going in, `agent: answer-yes` / `agent: answer-no` going out. The agent decides.
- **Program-decided branch:** `iterante: evaluate` going in, `iterante: loop` / `iterante: advance` going out. The program decides. No agent involvement.

The visual difference tells you at a glance who is deciding.

### Faithfulness Rule

The canvas mirrors mission.py structure faithfully. If a branch doesn't exist in mission.py, it doesn't exist on the canvas. The canvas is a structural mirror, not aspirational design.

## Relationship Types

| Type | Meaning | Render behavior |
|---|---|---|
| `edge` | Flow connection | Canvas edge created |
| `adjacent` | Cards touch borders | Checked by render, not created |
| `contains` | Card inside another | Checked by render, not created |

## CLI Commands

Entry point: `agentos canvas`.

| Command | Purpose |
|---|---|
| `init --model ... --file ...` | Create canvas from model JSON |
| `show --file ...` | Print `_model` as JSON |
| `card --file ...` | List cards or query one |
| `add-card --file ... --card-id ... --card-type ...` | Add card to model + canvas |
| `add-edge --file ... --from ... --to ... --edge-id ...` | Add relationship |
| `render --file ...` | Dry run: report errors and pending actions |
| `render --file ... --apply` | Compile: model + old canvas → new canvas |

## Standard Workflow

1. Edit the `_model` (via CLI or direct JSON edit)
2. `agentos canvas render --file ...` — check validity
3. Fix errors
4. `agentos canvas render --file ... --apply` — compile
5. Open in Obsidian to arrange layout

## Layout Ownership

Positions and sizes are user-owned. The CLI never overwrites existing positions. New cards get computed initial positions only. Use Obsidian to arrange layout. `--this-is-dangerous` is required for position-destructive operations like re-init.

## Visual Conventions

- **Question cards** — color `"3"` (yellow) for decision points
- **Loop/edge cards** — color `"6"` (purple) for connective tissue
- **Manuscript work cards** — color `"5"` (cyan) for the active work section
- **Event cards** — color `"4"` (green) for triggers
