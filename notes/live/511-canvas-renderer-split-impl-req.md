# Canvas Renderer Split - impl-req

## Impl-Req State

Ready for implementation.

## User Intent

Extract all canvas layer mutation logic (positions, sizes, colors) from `agentos canvas` commands into a dedicated `Canvas.Renderer` module, establishing the architectural boundary between model operations and layout operations.

## Why This Exists

The canvas CLI currently mixes model layer operations (add-card, add-edge, sync) with canvas layer mutations (placing new nodes, sizing them). This coupling creates risk: model commands accidentally overwrite user-arranged layouts. The design decision is that layout is user-owned by default, and only the renderer can intentionally mutate it.

The split was captured in `110-Agentos.Canvas.md` under `Canvas.Renderer`.

## Current Situation

- `core.py` contains layout functions (`place_one`, `layout_grid`, `_avoid_overlap`), sizing functions (`estimate_node_size`, `resize_node`, `make_canvas_node`), and a `make_node_text` function — all mixed with model layer code.
- `commands.py` calls these directly from model commands (`init`, `add-card`, `sync`).
- Position/size mutations happen at card creation only (already corrected), but the code isn't organized to reflect the architectural boundary.
- No renderer module exists yet.

## Requested Change

1. **Create `agentos/canvas/renderer.py`** — move all canvas layer mutation logic here:
   - `estimate_node_size`, `resize_node` — sizing
   - `make_canvas_node` — node factory (computes initial position + size)
   - `make_node_text` — TID.Pair text generation
   - `layout_grid` — grid layout for init
   - `place_one`, `_avoid_overlap` — incremental placement
   - Constants: `MIN_NODE_WIDTH`, `MAX_NODE_WIDTH`, `MIN_NODE_HEIGHT`, `PX_PER_CHAR`, `PX_PER_LINE`

2. **Keep in `core.py`** — model layer only:
   - Model dataclasses (`ModelCard`, `ModelRelationship`, `CanvasModel`)
   - Model I/O (`parse_model`, `model_to_dict`, `read_model`, `write_model`)
   - Topology parsing (`parse_topology`, `parse_init_input`, `topology_to_dict`)
   - Canvas file I/O (`read_canvas`, `write_canvas`)
   - Lint (`lint_canvas`, `LintError`, spatial helpers `_nodes_adjacent`, `_node_contains`, `_is_tid_pair`)
   - Sync (`sync_canvas`, `SyncAction`)

3. **`model_to_canvas` moves to `renderer.py`** — it's the bridge function that creates positioned canvas output from a model. It belongs with the renderer since it makes layout decisions.

4. **Update imports** in `commands.py` to pull layout/sizing from `renderer` instead of `core`.

5. **`sync_canvas` in `core.py`** calls renderer functions for placing new nodes. This is a clean dependency: model operations delegate to the renderer for creation-time layout only.

## Constraints And Invariants

- This is a pure refactor. No new features, no behavior changes.
- All existing `agentos canvas` commands must work identically after the split.
- The renderer module does not expose CLI commands yet. Command surface design is deferred.
- Lint stays in `core.py` — it reads canvas state but never writes it.

## Out Of Scope

- Renderer CLI commands (`agentos canvas render ...`).
- Rich renderer configuration or model-aware cascading.
- Color management.
- Any change to the canvas file format or model schema.

## Acceptance Signals

- `renderer.py` exists with all layout/sizing functions.
- `core.py` has no layout/sizing functions — only model, I/O, lint, sync.
- All `agentos canvas` subcommands produce identical output.
- `agentos canvas lint` passes on existing canvas files.

## Relevant Files Or Surfaces

- `agentos-py/src/agentos/canvas/core.py` — current mixed module
- `agentos-py/src/agentos/canvas/commands.py` — CLI commands
- `agentos-md/notes/index/110-Agentos.Canvas.md` — Canvas.Renderer design section
- `agentos-md/notes/index/001-ontology.md` — Canvas.Renderer ontology entry

## Open Questions

None.

## Related Impl-Reqs

- `509-agentos-canvas-cli-impl-req.md` — original CLI implementation request (predecessor).

## End Log
