# Agentos.Canvas.CLI First Draft - impl-req

## Impl-Req State

Ready for implementation. Design converged through discussion; no blockers.

## User Intent

Implement a minimal `agentos canvas` CLI that lets agents declare graph topology and have it rendered as a positioned Obsidian Canvas file. The agent focuses on topology and content; the CLI handles layout.

## Why This Exists

Agents currently have no programmatic way to create or modify `.canvas` files without manually computing `x, y` coordinates. The CLI removes layout burden from the agent and provides a simple, flag-based interface for graph construction.

## Current Situation

- `agentos canvas` subcommand does not exist yet.
- The `Agentos.Canvas.Graph.Model` is defined in `notes/index/110-Agentos.Canvas.md`.
- A reference canvas exists at `notes/canvas/agentos-canvas-design-session.canvas`.

## Requested Change

Implement the following commands under `agentos canvas`:

### `agentos canvas init`

Create a new canvas file from a topology JSON.

```bash
agentos canvas init --topology topology.json --file graph.canvas
```

**Topology JSON format:**

```json
{
  "nodes": ["cli", "missions", "chatlas"],
  "edges": [
    {"from": "cli", "to": "missions", "edge-id": "uses"},
    {"from": "cli", "to": "chatlas", "edge-id": "stores in"}
  ]
}
```

- Each node id in `nodes` becomes an inline text node with `Canvas.Inline.Note.Style` format (`## <id>\n> node: <id>`).
- Each edge becomes a Labeled.Edge in the canvas.
- All nodes are auto-laid-out (full layout pass).

### `agentos canvas add-node`

Add a single node to an existing canvas, auto-placed near its neighbors.

```bash
agentos canvas add-node --file graph.canvas --node-id new-thing --connect-to cli --edge-id "uses"
```

- Creates the node with `Canvas.Inline.Note.Style`.
- Creates the edge (Labeled.Edge).
- Places the node using the "place one" heuristic (centroid of neighbors + offset to avoid overlap).

### `agentos canvas add-edge`

Add an edge between existing nodes.

```bash
agentos canvas add-edge --file graph.canvas --from cli --to new-thing --edge-id "uses"
```

### `agentos canvas place`

Reposition a single node to a better location given its current neighbors.

```bash
agentos canvas place --file graph.canvas --node-id new-thing
```

- Computes centroid of connected neighbors.
- Offsets to avoid overlap.
- Does NOT reposition other nodes.

### `agentos canvas show`

Print the canvas topology as JSON to stdout (same format `init` consumes).

```bash
agentos canvas show --file graph.canvas
```

Output:

```json
{
  "nodes": ["cli", "missions", "chatlas"],
  "edges": [
    {"from": "cli", "to": "missions", "edge-id": "uses"},
    {"from": "cli", "to": "chatlas", "edge-id": "stores in"}
  ]
}
```

Round-trip: `show` output is valid `init` input.

### `agentos canvas lint`

Validate the canvas against `Agentos.Canvas.Graph.Model` linter rules.

```bash
agentos canvas lint --file graph.canvas
```

Checks (v1):
1. Every inline node has a valid, unique TID.Pair.
2. Every direct edge between two node cards has a non-empty, non-`*` label.
3. Every edge connected to an edge card has no label or `*`.
4. Card.Edge connectors form consistent directed paths (no sink/source/mixed errors).

## Constraints And Invariants

- All arguments use explicit option flags (no positional arguments).
- `--node-id` for node identity, `--edge-id` for edge identity.
- The CLI never performs a full re-layout on an existing canvas — only `init` does full layout.
- Human-moved positions in Obsidian are always respected by incremental commands.
- Inline notes follow `Canvas.Inline.Note.Style` (Md.Block + TID.Pair blockquote).
- Edge ids are stored verbatim (no reformatting, no slugification).

## Out Of Scope

- Card.Edge creation via CLI (agents can create these by editing the canvas directly for now).
- CLI.Normalization (uniform object output) — design TBD, separate impl-req later.
- `--connect-from` (reverse edge direction on add-node) — can be added later.
- Content editing commands — agents read/write `.canvas` JSON directly for content changes.
- Advanced layout algorithms — simple heuristic is sufficient for v1.

## Acceptance Signals

- `agentos canvas init` produces a valid `.canvas` file that renders correctly in Obsidian.
- `agentos canvas show` output is valid input for `agentos canvas init` (round-trip).
- `agentos canvas lint` catches all four linter rule violations.
- `agentos canvas add-node` places a new node without overlapping existing nodes.
- All inline nodes in generated canvases follow `Canvas.Inline.Note.Style`.

## Relevant Files Or Surfaces

- `agentos-md/notes/index/110-Agentos.Canvas.md` — subsystem definition and Graph.Model
- `agentos-md/notes/canvas/agentos-canvas-design-session.canvas` — reference canvas showing both edge types
- `agentos-md/notes/live/501-agentos-canvas-design-session.md` — full design session with accepted decisions

## Open Questions

- Which layout algorithm for `init`? Hierarchical (Sugiyama) for DAGs or spring (force-directed) for general graphs. Suggest: start with spring, it handles both.
- Should `add-node` without `--connect-to` just place the node at a default offset from the graph center?

## Related Impl-Reqs

- None. This is the first `Agentos.Canvas` implementation request.

## End Log

- 2026-05-06: Created from design discussion. CLI surface converged with explicit flags, topology JSON format, and surgical layout strategy.
