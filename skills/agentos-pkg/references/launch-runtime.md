# Launch Runtime

Bootstrap index work through the canonical `agentos-index` entry surface.

## 1. Enter Through `agentos-index`

- Load `agentos-index` as the public entry place for the index system
- Choose the explicit module that matches the current task when one applies, such as `--search` or `--write`
- Stay at the root skill when the task is only orientation, subsystem understanding, or route selection

## 2. Use Routing-First Selective Loading

- Start from the relevant routing surface: public `index/000-index.md`, local `notes/index/001-index.md`, or both
- Find the target concept or nearby related names before loading flat files
- Read only the flat index files that own the relevant routed concepts
- Load appendix depth only when the selected concept blocks do not carry enough signal
- Load references only when the task needs operational detail or worked examples

## 3. Search Behavior

- Return context with source block citations so the caller can verify and maintain the summary
- Distinguish discovered context from inference
- Surface unresolved names instead of inventing concepts
- Treat repeated unresolved names as capture signals, not reasons to guess

## 4. Depth And Quality References

- use `Appendix.Discovery` when the selected index block suggests or requires depth
- use `agentos-pkg/references/index-block-catalog.md` when the task needs concrete block-writing calibration
- use the `agentos-index --write` module for approved index or appendix edits
