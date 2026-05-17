# Load Runtime

Bootstrap the Index Runtime. Execute these steps in order.

## 1. Load Index Data

- Read `index/000-index.md` — the public routing table
- Read all flat files listed in the routing table
- Read `notes/index/000-index.md` if it exists — local entry point
- Read all local flat files listed there
- The full index is now in context.

## 2. Load Appendix for Runtime Concepts

- Load appendix files for runtime-related concepts:
  - `appendix/Index.Architecture-appendix.md`
  - `appendix/Agentos.Index.System-appendix.md`
  - `appendix/Agentos.Surfaces-appendix.md`
- These give the agent depth on how the index is structured and why.

## 3. Understand the Index

The index contains the concepts you need. Key blocks to ground on:
- `Index.Architecture` — how the index is structured
- `Kernel.Block:Index` — what a block is
- `Kernel.Writing` — how blocks are written
- `Distributed.Index` — public/local split
- `Index.Router` — what the routing table is
- `Index.Runtime` — what the runtime is

## 4. Operating Behavior

Now that the index is loaded, understand how to operate:
- For writing rules → `references/gating.md`
- For name detection and resolution → `references/naming.md`
- For appendix and research → `references/appendix.md`
- For maintenance → `references/maintenance.md`

## 5. Always-on Behavior

- Detect `Dotted.Names` in conversation — they're already in your context
- Report appendix loads and unresolved names in footer:
  `> Index: loaded appendix `Concept.A` | unresolved: `Unknown.Name``
- Only report when something happened — no footer for normal grounding
- Gap detection is passive — park unknown names, don't interrupt flow
- If the same unresolved name recurs 3+ times, suggest capture to the user
