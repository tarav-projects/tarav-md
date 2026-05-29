# Launch Runtime

Bootstrap the Index Runtime. Execute these steps in order.

## 1. Load Index Data

- Read `agentos-pkg/index/000-index.md` — the public routing table
- Read all flat files listed in the routing table
- Read `notes/index/001-index.md` if it exists — local entry point
- Read all local flat files listed there
- The full index is now in context.

## 2. Ground on Key Concepts

The index is loaded. Ground on these concepts to understand how the system works:
- `Index.Architecture` — how the index is structured
- `Kernel.Block:Index` — what a block is
- `Kernel.Writing` — how blocks are written
- `Distributed.Index` — public/local split
- `Index.Router` — what the routing table is
- `Index.Runtime` — what the runtime is
- `Index.Surface.Layout` — expected directory structure

## 3. Load Appendix for Key Concepts

Load these appendix files — they give depth on how the index is structured and why:
- `agentos-pkg/appendix/Index.Architecture-appendix.md`
- `agentos-pkg/appendix/Agentos.Index.System-appendix.md`
- `agentos-pkg/appendix/Surface.Link.Directionality-appendix.md`

## 4. Always-on Behavior

- The full index is in context — known `Dotted.Names` ground naturally, no lookup needed
- Use `Appendix.Discovery` when you need depth on any concept
- When an unknown name appears, park it as `Unresolved.Index.Name`
- Report unresolved names in footer: `> Index: unresolved: `Unknown.Name``
- Only report when something is unresolved — no footer for normal operation
- Gap detection is passive — don't interrupt flow
- If the same unresolved name recurs 3+ times, suggest capture to the user
