# Index Reindex Session — 2026-05-11

Free-form design notes from the index reindex session.

---

## Index.Block body: no "extra" layer

If an example or code must be in a block, it's there because it's fundamental to understanding the concept — not because it's "extra." The old 513 design had four layers (heading → fundamentals → extra → index section). The new model has three: heading → body → sections. Everything in the body is fundamental by definition. If it's not fundamental, it doesn't belong in the block.

## Context.Minimal.Surface

`Context.Minimal.Surface` is the set of files from a project that agents must ALWAYS load at session start to be oriented.

Why this matters:
- Agents have finite context windows — what you preload matters
- Too much = waste, agent is slow and unfocused
- Too little = agent is lost, keeps asking questions or making wrong assumptions
- The sweet spot is a minimal set that gives full orientation

What it enables:
- It's measurable — CLI can compute total tokens/characters of the whole surface
- Creates a budget constraint — if the surface grows too large, it degrades agent performance
- Optimization feedback: "your Context.Minimal.Surface is X tokens — here's the breakdown per file"
- Pressure to keep orientation files compressed and high-signal

For Agentos, the minimal surface would likely include:
- `AGENTS.md` files (project instructions)
- `000-index.md` (structural orientation)
- `001-ontology.md` (concept map)
- `002-surfaces.md` (surface registry)

This connects to real agent ergonomics. The minimal surface is the "boot sequence" — what the agent loads before it can do anything useful. Keeping it small and high-signal is a maintenance concern.

Possible CLI support:
- `agentos context minimal` — list the files in the minimal surface
- `agentos context minimal --size` — report total size
- `agentos context minimal --budget <tokens>` — warn if over budget
