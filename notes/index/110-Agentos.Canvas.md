# Agentos.Canvas

`Agentos.Canvas` is a surface for human/agent collaboration — visual, built on Obsidian `.canvas` files. It sits alongside `notes/live`, `notes/index`, and other Agentos surfaces as a specialized medium for expressing structure and relationships visually.

---

## What Agentos.Canvas Is

`Agentos.Canvas` is the Agentos surface type for visual graphs. Canvas files are shared artifacts: humans edit them in Obsidian; agents operate on them through the `agentos canvas` CLI.

Canvas is not a replacement for markdown surfaces — it is a complement. It expresses structure and relationships that are easier to read visually than in prose or lists.

## Surface Location

Canvas files live in `notes/canvas/`, a sibling directory to `notes/live/` and `notes/index/`.

## Two-Layer Architecture

A single `.canvas` file contains two layers:

- **Model layer** — extra JSON fields Obsidian ignores. Owns topology (what exists, how it connects) and domain metadata.
- **Canvas layer** — what Obsidian reads. Owns text content, positions, sizes, colors.

Obsidian preserves unknown JSON fields on nodes, edges, and at the top level. This allows the model layer to live inside the same file with no separate model file.

### SSOT By Concern

| Concern | Authority |
|---|---|
| Topology (cards, relationships) | Model layer |
| Domain semantics (types, metadata) | Model layer |
| Text content | Canvas layer |
| Positions, sizes, colors | Canvas layer |

### Text Lifecycle

Model → CLI migrate → canvas. One-way. The model is the staging area for text, the canvas is the final home. Both having text for the same card at the same time is an error (unless forced with a flag).

### Type Lifecycle

Type lives in both layers permanently. Model declares it, canvas has it in the TID.Pair blockquote. Mismatch → linter error, agent resolves based on context.

### CLI Role

- **`lint`** — read-only validation of model↔canvas consistency.
- **`sync`** — forward-pass model→canvas resolution. If the path is clear (model card with no canvas node, model edge-relationship with no canvas edge), it applies automatically. Ambiguous cases are reported, not resolved.

## Canvas.Card

The visual primitive — a card on the canvas. "Card" is the visual term; "node" is reserved for graph-level semantics.

### Card.ID

Identity via TID.Pair.

### Card.Type

Type via TID.Pair. Domain-defined — Agentos.Canvas does not impose type names. In a flow graph a card might be `step: validate-input`; in an architecture graph, `module: auth`.

### Card.Text

Text content lives on the canvas layer. Follows `Md.Block` structure with a TID.Pair declaration:

```md
## Block title
> type: <id>
- rest of the block
```

### Card.Relationship

Relationships between cards. The model declares them; the linter checks that the canvas satisfies them.

| Relationship | Meaning | Linter checks |
|---|---|---|
| `edge` | Flow connection, rendered as a canvas edge | Canvas has an edge between the cards |
| `adjacent` | Cards touch borders | Canvas positions: bounds touch |
| `contains` | One card inside another | Canvas positions: child fits within parent |

New relationship types can be added as new linter rules without changing the architecture.

## Edge Rendering

### Labeled.Edge

Compact: the edge label is the full identity (id = label verbatim). Direction via `fromEnd`/`toEnd`.

### Card.Edge

Expanded: a full card with its own TID.Pair. Richer content capacity. Connected to other cards with `*` or unlabeled connectors. Direction via `fromEnd`/`toEnd`.

At the graph level they are identical. The difference is content capacity only.

### Direction

Expressed via `fromEnd` / `toEnd` on any edge. No separate direction vocabulary — the canvas JSON fields are the model.

## Agentos.Canvas.CLI

Entry point: `agentos canvas`.

Current commands: `init`, `show`, `add-card`, `add-edge`, `place`, `sync`, `lint`.

## Visual Conventions

- **Edge cards** — color `"6"` (purple) to visually distinguish them as connective tissue.

## Provenance

- Promoted from design session at `../live/501-agentos-canvas-design-session.md`.
- Updated with two-layer model and domain primitives from `../live/510-agentos-canvas-model-design-session.md`.
