# Development.Principles — appendix

## Vertical.Slice

- "vertical" means go deep through the layers, not wide across one layer
- a horizontal plan builds all data models, then all services, then all UI — this delays feedback and surfaces integration problems late
- a vertical slice picks one behavior and builds everything needed for that behavior to work — from input to output, through all the layers it touches
- the discipline is relative to the scope of the implementation
    - if the goal is building a module, a slice that exercises that module's interface is vertical enough
    - if the goal is a feature that spans CLI, service, and storage, a slice should cut through all three
- given the implementation scope, cut vertically across the systems involved — not horizontally through one layer at a time
- vertical slices should span as many systems as the implementation goal touches
- once the first vertical path is running and tested, expand: more behaviors, more cases, more edges — the integration path is already proven
- implementation progress is measured in observable behaviors, not in completed layers

### examples

#### CLI feature: `agentos index linter`

- scope: add a CLI command that lints configured index and appendix surfaces
- horizontal approach (avoid):
    - add CLI argument parser for linter
    - add all diagnostic checks
    - add output formatting
    - add tests
- vertical slice:
    - wire CLI entry point → run one deterministic check (e.g., configured surface existence) → print result
    - testable: `agentos index linter --index <path>` runs and outputs a summary
    - then: add gated checks, JSON output, and blocked-check summary
    - then: add remaining linter checks

#### module: prefix allocator for file numbering

- scope: build a prefix allocator that returns the next available file number
- vertical slice:
    - implement `next_prefix(target_dir)` → returns correct next number → unit test passes
    - testable: calling the function with a real directory returns the right prefix
    - then: add edge cases — gaps, reserved ranges, floor constraints

#### full-stack feature: canvas card for mission status

- scope: add a canvas card that shows mission status from real data
- vertical slice:
    - mission data → canvas renderer → one card visible in `.canvas` output
    - testable: generate canvas, card appears with real mission data
    - then: add status coloring, relationships, layout
