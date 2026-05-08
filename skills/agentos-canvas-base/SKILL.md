---
name: agentos-canvas-base
description: "Agentos Canvas surface protocol and CLI usage. Use when working with `.canvas` files, creating visual project maps, or when the user mentions canvas, visual graphs, or card relationships."
---

# Agentos Canvas Base

Protocol and usage guidance for the Agentos.Canvas surface — visual project maps built on Obsidian `.canvas` files.

The durable design source is `notes/index/110-Agentos.Canvas.md`. If this skill conflicts with the index, the index wins.

## What Canvas Is

Canvas files are shared visual artifacts: humans edit them in Obsidian, agents operate on them through `agentos canvas` CLI. Canvas files live in `notes/canvas/`.

Canvas is not a replacement for markdown surfaces — it expresses structure and relationships that are easier to read visually.

## Two-Layer Architecture

A single `.canvas` file contains two layers:

- **Model layer** — a top-level `_model` key in the JSON. Owns topology and domain semantics.
- **Canvas layer** — `nodes` and `edges`. What Obsidian reads. Owns text, positions, sizes, colors.

Obsidian preserves unknown JSON fields, so the model lives in the same file.

## Model Format

The `_model` schema is used everywhere — inside canvas files and as the input for `init`:

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

Every card has a TID.Pair in its text:

```md
## auth
> module: auth
```

The type is domain-defined — Agentos.Canvas does not impose type names.

## Edge Identity

Every edge label must be a valid TID.Pair (`type: id`). A TID.Pair on an edge implies a card — it does not require one. If a card with that TID.Pair exists, it elaborates the edge concept.

## CLI Commands

Entry point: `agentos canvas`.

### Create a canvas

```sh
agentos canvas init --model model.json --file notes/canvas/my-map.canvas
```

Errors if file exists unless `--this-is-dangerous` is passed (overwrites all positions).

### Inspect

```sh
agentos canvas show --file notes/canvas/my-map.canvas
agentos canvas card --file notes/canvas/my-map.canvas
agentos canvas card --file notes/canvas/my-map.canvas --card-id auth
agentos canvas card --file notes/canvas/my-map.canvas --card-id auth --text
```

- `show` — prints the full `_model` as JSON.
- `card` — lists all cards as `type: id`. With `--card-id`, returns full card info (model + canvas merged). With `--text`, returns just text content.

### Add cards and edges

```sh
agentos canvas add-card --file my.canvas --card-id auth --card-type module
agentos canvas add-card --file my.canvas --card-id db --card-type module --connect-to auth --edge-id "rel: queries"
agentos canvas add-edge --file my.canvas --from auth --to db --edge-id "rel: queries"
agentos canvas add-edge --file my.canvas --from api --to db --edge-id "rel: contains" --rel-type contains
```

### Render (the compiler)

```sh
agentos canvas render --file my.canvas
agentos canvas render --file my.canvas --apply
```

- Without `--apply` — dry run. Reports errors and pending actions.
- With `--apply` — compiles: `model + old canvas -> new canvas`. Creates missing nodes, rebuilds edges, updates labels, migrates text. Positions and layout are inherited from the old canvas.

## Standard Workflow

The render command is the protocol implementation. A canvas is valid if and only if render reports no errors.

1. Edit the `_model` (via CLI or direct JSON edit)
2. `agentos canvas render --file ...` — check validity
3. Fix errors
4. `agentos canvas render --file ... --apply` — compile
5. Open in Obsidian to arrange layout

## Layout Ownership

Positions and sizes are user-owned. The CLI never overwrites existing positions. New cards get computed initial positions only. Use Obsidian to arrange layout.

## Relationship Types

| Type | Meaning | Render behavior |
|---|---|---|
| `edge` | Flow connection | Canvas edge created |
| `adjacent` | Cards touch borders | Checked by render, not created |
| `contains` | Card inside another | Checked by render, not created |
