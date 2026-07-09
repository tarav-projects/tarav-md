# Anchor System — Design Handoff

- handoff live-note: enough context for a fresh agent to start developing the anchor system
- grounding session: `99144906-781e-43cc-9d27-b40f166e2acf` (index-migration session; anchors emerged inside the grounding-system redesign)
- status: design converged on fundamentals below; not yet in the index (blocks drafted, unwritten); no code exists

## Why

- the grounding system was redesigned from first principles: `Context.Grounding` (read-side: enrich agent context with `Hard.Evidence`-linked data) and `Index.Linking` (write-side: build/maintain the index's pointers back to the surfaces it indexes — the `Chat.Surface` foremost)
- the old pointer form, `Chat.Ref` (`@<hash>-<time>..<time>`), is fat, provider-coupled, and brittle — a broken ref means editing gated index content
- the anchor system replaces it: a tiny stable token on the citing surface, all finding-data behind a register — the symbol-table move applied to evidence

## Design (converged with the user)

- **`Link.Anchor`** — a small stable token, e.g. `^20260630-0`, standing for a context on some surface; the register resolves it
  - immutable in meaning: no reuse of anchors; an entry changes only to amend an error or improve its resolution
  - the token carries hints of what it anchors; if the token's own hint is wrong (e.g. wrong date), mint a new anchor — do not repurpose
  - date-based keys for chat/index linking: humans are sequential sources of information; time is the natural parameter (`-0` suffix = register position that day, keeps the token small)
  - keeps the citing surface clean: token tiny, resolution data in the register
- **`Anchor.Register`** — the lookup: anchor → `context_ref`, a plain queryable dictionary
  - registration checks the key is free; any string can key any data — chat anchoring is one application, the date-key format one convention
  - **an agentos subsystem, NOT per-project** — the `context_ref` can carry the project as a field; it connects with chatlas for chat-anchor resolution
  - git-tracked — every amendment audited
  - deliberately simple: no uniqueness machinery beyond the free-key check
  - collisions tolerated, not fought — the caller is an agent: it queries, disambiguates, re-anchors
  - the register is plumbing, not truth: **the information lives on the surfaces, never in the register**; desync is detected by agents reading the surfaces (cross-surface sense breaks), not by the register

## Fit with the index system

- `Index.Linking` entries (a block's `Concept.X/Grounding` section, `Grounding.Entry` rows) carry anchors instead of raw chat refs
- `Chat.Grounding.Ref.Resolution` semantics survive: an anchor is a landing point into a neighborhood, not a claim of one exact turn; resolve via register, then read around
- `Context.Grounding` full level: follow anchors out to the original surfaces (chats via chatlas + git history, code directly)
- the `Agendix` (agent-driven, ungated shadow of the index) will use anchors for its hard provenance rule — every agendix line carries a pointer to its chat evidence

## Open (decide during implementation or bounce back)

- `Chat.Ref` replacement is directionally confirmed ("we are redoing the Chat.Ref system") but the migration of existing `Chat.Ref` usages/blocks is not planned; `Chat.Ref` block in the index still stands
- `File.Mention` (`@<path-hint>`) shares the `@` sigil — unify as another anchor application, or keep separate? (unresolved)
- concept names `Link.Anchor` / `Anchor.Register` are working names, not user-locked
- register storage location + format (JSONL? one file? sharded by date?) — open; must be git-tracked and cheap to query
- CLI shape — suggestion from the discussion: `agentos anchors register / resolve / query` in agentos stdlib style; chatlas provides the chat-application (register at interaction, resolve to session+turn via `chatlas query`)
- registration ergonomics for agents mid-conversation (who mints, when, how the daily `-N` counter is allocated)

## Where things live

- agentos CLI/runtime code: `agentos-py` (subsystems under `src/agentos/`), CLI wiring pattern: `src/agentos/index/commands.py` is a good reference; executable owned by `agentos-cli` (see `agentos-py/AGENTS.md` for reinstall notes)
- chatlas: `agentos-chatlas-py` (code), `agentos-chatlas-md/skills/agentos-chatlas-pkg/` (index/skill surfaces)
- index concepts to read for context: `Context.Grounding`, `Index.Linking`, `Index.Grounding`, `Chat.Grounding`, `Chat.Surface`, `Kernel.Block.Grounding`, `Grounding.Entry`, `Agendix` (all in `agentos-md/skills/agentos-pkg/`, routed via `000-INDEX.md`)
- deprecated prior art (do not build on, reference only): `agentos-chatlas-md/skills/_DEPRECATED/chatlas-grounding-agent/` and `skills/agentos-chatlas-pkg/_DEPRECATED/grounding-workflow.md` (the L1/L2 miner + `Chat.Grounding.Request` queue)
