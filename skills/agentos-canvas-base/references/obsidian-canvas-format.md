# Obsidian Canvas Format

Reference for the Obsidian `.canvas` file format — structure, conventions, and how to work with it programmatically.

## What a Canvas File Is

A `.canvas` file is a JSON document that Obsidian renders as an infinite visual board. It contains nodes (cards) and edges (connections between cards). Humans edit it visually in Obsidian; agents edit the JSON directly.

## File Structure

```json
{
  "nodes": [ ... ],
  "edges": [ ... ]
}
```

Obsidian preserves unknown top-level keys and unknown fields on nodes/edges. This means you can add custom data (like `_model`) without breaking Obsidian.

## Nodes

A node is a card on the canvas. Obsidian supports several node types.

### Text Node

The most common type. Contains Markdown text rendered inline.

```json
{
  "id": "abc123",
  "type": "text",
  "text": "## Heading\nBody text here",
  "x": -480,
  "y": -200,
  "width": 380,
  "height": 210
}
```

### File Node

Embeds a vault file (note, image, PDF).

```json
{
  "id": "def456",
  "type": "file",
  "file": "path/to/note.md",
  "x": 100,
  "y": 100,
  "width": 400,
  "height": 400
}
```

### Link Node

Embeds a URL.

```json
{
  "id": "ghi789",
  "type": "link",
  "url": "https://example.com",
  "x": 0,
  "y": 0,
  "width": 400,
  "height": 300
}
```

### Group Node

A container that visually groups other nodes. Does not enforce containment — it is purely visual.

```json
{
  "id": "jkl012",
  "type": "group",
  "label": "My Group",
  "x": -100,
  "y": -100,
  "width": 600,
  "height": 400
}
```

### Common Node Fields

| Field | Required | Description |
|---|---|---|
| `id` | yes | Unique string identifier |
| `type` | yes | `text`, `file`, `link`, or `group` |
| `x` | yes | Horizontal position (pixels, can be negative) |
| `y` | yes | Vertical position (pixels, can be negative) |
| `width` | yes | Width in pixels |
| `height` | yes | Height in pixels |
| `color` | no | Color preset: `"1"` red, `"2"` orange, `"3"` yellow, `"4"` green, `"5"` cyan, `"6"` purple. Or a hex string `"#rrggbb"` |
| `text` | text only | Markdown content |
| `file` | file only | Vault-relative path |
| `url` | link only | URL string |
| `label` | group only | Group label |

## Edges

An edge is a visual connection between two nodes.

```json
{
  "id": "e01",
  "fromNode": "abc123",
  "toNode": "def456",
  "fromSide": "bottom",
  "toSide": "top",
  "label": "my label"
}
```

### Edge Fields

| Field | Required | Description |
|---|---|---|
| `id` | yes | Unique string identifier |
| `fromNode` | yes | ID of the source node |
| `toNode` | yes | ID of the target node |
| `fromSide` | no | `top`, `bottom`, `left`, `right`. Omit for automatic |
| `toSide` | no | `top`, `bottom`, `left`, `right`. Omit for automatic |
| `fromEnd` | no | `none` or `arrow`. Default: `none` |
| `toEnd` | no | `none` or `arrow`. Default: `arrow` |
| `color` | no | Same color system as nodes |
| `label` | no | Text label displayed on the edge |

### Direction

By default, edges have an arrow at the `toEnd` and none at the `fromEnd` (directed from → to). Set `fromEnd` / `toEnd` explicitly to create undirected edges, bidirectional arrows, or reverse the arrow.

## Coordinate System

- Origin `(0, 0)` is the center of the canvas
- `x` increases rightward, `y` increases downward
- Positions refer to the top-left corner of the node
- Obsidian auto-pans; there are no canvas boundaries

## Working With Canvas Files Programmatically

### Reading

Parse the file as JSON. Nodes and edges are flat arrays — no nesting.

### Writing

Write valid JSON. Obsidian re-reads the file when it changes on disk (if the canvas is open, it live-reloads).

### Editing Safely

- **Preserve unknown fields.** Obsidian keeps custom keys. If you read and rewrite, carry all fields through — do not strip unknown keys.
- **Preserve positions.** Node positions are user-arranged layout. Do not overwrite `x`, `y`, `width`, `height` on existing nodes unless explicitly intended.
- **Generate unique IDs.** Node and edge IDs must be unique within the file. Use UUIDs or sequential IDs.
- **Validate edges.** Every `fromNode` and `toNode` must reference an existing node ID. Orphan edges are silently ignored by Obsidian but represent broken state.

### Obsidian Behavior

- Obsidian may reorder nodes/edges and compact the JSON on save
- Obsidian may adjust node sizes if the text content overflows
- Obsidian preserves custom top-level keys and custom fields on nodes/edges
- File and group nodes embed content visually but do not create structural relationships
