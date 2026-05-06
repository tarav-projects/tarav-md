# Agentos.Canvas.Model.Design - design-session

## Motivation

Decouple the modeling language from the rendering language inside Agentos.Canvas. The `.canvas` file stays the single artifact, but it contains two layers: a model layer (domain semantics, topology) and a canvas layer (visual rendering, text content, layout). This enables clean SSOT by concern and supports a human/agent collaboration workflow where each party works on what they're best at.

## Items

- Agentos.Canvas.Model.Design: [closed] two-layer architecture inside a single .canvas file
- Agentos.Canvas.Domain.Model: [closed] card primitives and relationship types

## Agentos.Canvas.Model.Design

**Discovery:** Obsidian Canvas ignores extra JSON fields in `.canvas` files. Extra fields on nodes, edges, and at the top level survive Obsidian edits (moves, resizes, text changes). This means the model layer can live inside the same file — no separate model file needed.

**Two layers, one file:**

- **Model layer** — extra JSON fields Obsidian ignores. Owns topology (what exists, how it connects) and domain metadata.
- **Canvas layer** — what Obsidian reads. Owns text content, positions, sizes, colors.

**SSOT by concern:**

| Concern | Authority |
|---|---|
| Topology (nodes, edges) | Model layer |
| Domain semantics | Model layer |
| Text content | Canvas layer |
| Positions, sizes, colors | Canvas layer |

**Text lifecycle:** model → CLI migrate → canvas. One-way. The model is the staging area for text, the canvas is the final home. Both having text for the same node at the same time is an error (unless forced with a flag).

**CLI role:** detects drift between the two layers, reports mismatches. Does not auto-resolve — the agent or human decides based on context.

**No imposed types:** the model layer defines its own domain vocabulary. Agentos.Canvas doesn't enforce `node:` / `edge:` type prefixes.

**Verified:** extra-data test at `notes/canvas/extra-data-test.canvas` confirms Obsidian preserves unknown fields.

## Agentos.Canvas.Domain.Model

The domain model defines the vocabulary for expressing graph structure on canvas. "Card" is the visual primitive (what's on the canvas); "node" is reserved for graph semantics.

**Card primitives:**

| Item | What it is |
|---|---|
| `Canvas.Card` | The visual primitive — a card on the canvas |
| `Card.ID` | Identity via TID.Pair |
| `Card.Type` | Type via TID.Pair, lives in both model and canvas layers |
| `Card.Text` | Text content, lives on canvas layer (migrated from model via CLI) |
| `Card.Relationship` | Relationships between cards |

**Relationship types:**

| Relationship | Meaning | Linter checks |
|---|---|---|
| `edge` | Flow connection, rendered as a canvas edge | Canvas has an edge between the cards |
| `adjacent` | Cards touch borders | Canvas positions: bounds touch |
| `contains` | One card inside another | Canvas positions: child fits within parent |

**Type lifecycle:** Type lives in both layers permanently. Model declares it, canvas has it in the TID.Pair blockquote. Mismatch → linter error, agent resolves based on context.

**Text lifecycle:** model → CLI migrate → canvas. One-way. Model is the staging area, canvas is the final home.

**Extensibility:** new relationship types (e.g. `same-row`, `left-of`, `grouped-with`) can be added later as new linter rules without changing the architecture.

**Reference:** `notes/canvas/module-example.canvas` demonstrates `contains` (SubModule inside Module) and `adjacent` (Functions touching Module border).

## Notes

- This design supersedes the earlier assumption that the canvas file is self-describing (with TID.Pair blockquotes as the identity system). The model layer takes over the semantic role.
- The existing CLI implementation (init, show, add-node, add-edge, place, lint) predates this design. It will need to be updated to work with the model layer.
- The earlier `Agentos.Canvas.Graph.Model` (from `110-Agentos.Canvas.md`) defined linter rules based on canvas-only inspection. Those rules may need revision once the model layer is the topology authority.

## End Log

- 2026-05-06: Session created and closed. Two-layer architecture settled after discovering Obsidian preserves extra JSON fields.
- 2026-05-06: Added Agentos.Canvas.Domain.Model. Card primitives (Canvas.Card, Card.ID, Card.Type, Card.Text, Card.Relationship) and relationship types (edge, adjacent, contains) defined.
