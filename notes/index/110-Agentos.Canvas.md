# Agentos.Canvas

`Agentos.Canvas` is a surface for human/agent collaboration — visual, built on Obsidian `.canvas` files. It sits alongside `notes/live`, `notes/index`, and other Agentos surfaces as a specialized medium for expressing structure and relationships visually.

---

## What Agentos.Canvas Is

`Agentos.Canvas` is the Agentos surface type for visual graphs. Canvas files are shared artifacts: humans edit them in Obsidian; agents operate on them through the `agentos canvas` CLI.

Canvas is not a replacement for markdown surfaces — it is a complement. It expresses structure and relationships that are easier to read visually than in prose or lists.

## Surface Location

Canvas files live in `notes/canvas/`, a sibling directory to `notes/live/` and `notes/index/`.

## Agentos.Canvas.Graph.Model

`Agentos.Canvas.Graph.Model` is the semantic graph language for Agentos Canvas files.

### TID.Pair

The atomic identity primitive is the **TID.Pair**: a `type: id` declaration.

```
node: my-cli
edge: cli-to-missions
```

Every entity in a canvas has a TID. Types are implicit — derived from context or declared inline.

### Implicit Types

- Node card → type `node` (declared via `> node: <id>` blockquote)
- Edge card → type `edge` (declared via `> edge: <id>` blockquote)
- Labeled edge → type `edge`, id is the label string verbatim
- File node → type derived by CLI from relative file path

### Edge Rendering Modes

Two modes, same graph-model citizen:

- **Labeled.Edge** — compact: label is the full TID (id = label verbatim). Direction via `fromEnd`/`toEnd`.
- **Card.Edge** — expanded: full inline note card with `> edge: <id>`. Richer content capacity. Direction via `fromEnd`/`toEnd`.

At the graph level they are identical. The difference is content capacity only.

### Direction

Expressed via `fromEnd` / `toEnd` on any edge. No separate direction vocabulary — the canvas JSON fields are the model.

### Topology Constraint

No naked direct edges. Every direct edge between two node cards must be a Labeled.Edge (label required). If no label fits, promote to a Card.Edge.

### Connector Label Rule

Card.Edge connectors (between a node card and an edge card) must carry no label or `*`. Any other label is a linting error.

### Linter Rules (v1)

1. Every entity has a valid, unique TID.
2. Every direct edge between two node cards must have a non-empty, non-`*` label.
3. Every edge connected to an edge card must have no label or `*`.
4. Card.Edge connectors must form a consistent directed path — the edge card is a relay, not a sink or source:
   - `node -> edge.card <- node` — error (sink)
   - `node <- edge.card -> node` — error (source)
   - `node -> edge.card -- node` — error (mixed)
   - `node -- edge.card -> node` — error (mixed)

## Canvas.Inline.Note.Style

`Canvas.Inline.Note.Style` defines the required format for inline text nodes in Agentos Canvas files.

Inline text nodes follow `Md.Block` structure with a mandatory TID.Pair declaration:

```md
## Block title
> type: <id>
- rest of the block
```

- The `## heading` is the label; the `> type: <id>` blockquote is the TID.Pair.
- Applies only to inline text nodes. File nodes declare no TID inside the file — the CLI derives it from the path.
- Inline notes are valid plain markdown, readable outside Obsidian.
- Analogous to `Index.Block` for index notes.

## Agentos.Canvas.CLI

Entry point: `agentos canvas`.

## CLI.Normalization

The CLI surfaces a uniform object for each node and edge regardless of rendering mode (card vs label, file vs inline). Design TBD.

## Visual Conventions

- **Node cards** — default color.
- **Edge cards** — color `"6"` (purple) to visually distinguish them as connective tissue.

## Provenance

Promoted from the closed design session at `../live/501-agentos-canvas-design-session.md`.
