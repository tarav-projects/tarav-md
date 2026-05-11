# Index Migration Protocol

Live skill for migrating the Agentos Index to `Index.Block.Syntax` compliance.

Status: **active**

---

## Purpose

Rebuild `notes/index/` from scratch using the new `Index.Block.Syntax` format designed in `513-The.Agentos.Index.md` and operationalized in the `agentos-index` `Skill.Package`.

## Setup (one-time)

1. Move `notes/index/` → `notes/index-migration/` (source material + progress surface)
2. Create fresh `notes/index/` with empty `000-index.md` and `001-ontology.md`
3. Load skills: `agentos-index-activate`, `agentos-index-writer`, `agentos-index`

## Migration Loop

### Skills to load

Before starting a migration session, load:

- `agentos-index` — full design reference (block syntax, naming, ontology rules)
- `agentos-index-activate` — detection rules, eval loop, footer
- `agentos-index-writer` — governs the write loop (two gates, per-block approval)

### Per-block process

The migration uses the `agentos-index-writer` protocol:

```
1. Agent picks next un-migrated block from notes/index-migration/
2. Agent proposes rewritten block in Index.Block.Syntax:
   - Bullet.Point.Sentence style
   - **** separators
   - 25-line ceiling
   - ### index section (findability, related)
   - H2 heading as Dotted.Name where appropriate
3. User approves, requests changes, or skips
4. Agent writes approved block into notes/index/
5. Agent marks source block as <!-- MIGRATED --> in index-migration/
```

This is `Content.Verbatim.Gated` — the user sees and approves every block before it's written.

### Decisions during migration

- **Merge**: multiple old blocks can become one new block if they cover the same concept
- **Split**: one old block can become multiple new blocks if it exceeds 25 lines or mixes concepts
- **Rename**: block headings can change — use proper `Dotted.Names`
- **Drop**: blocks that are pure prose filler, provenance notes, or "related concepts" lists without substance can be dropped or absorbed into `### index` sections
- **New notes**: the new index can have different notes than the old one — different groupings, different numbering

### Numbering

- Fresh `NNN-` allocation for all new notes (`agentos stdlib prefix next --project --target notes/index`)
- Old prefixes are NOT preserved — this is a new index
- `000-index.md` and `001-ontology.md` remain reserved

### Progress tracking

The `notes/index-migration/` folder is the progress surface:

- Blocks marked `<!-- MIGRATED -->` are done
- Blocks without the tag are pending
- Whole files with all blocks migrated can be marked `<!-- FILE MIGRATED -->` at the top

### Session continuity

This note IS the protocol. Load it at the start of any migration session to resume work. The state lives in the `<!-- MIGRATED -->` tags — no separate tracking needed.

## Key References

- `notes/live/513-The.Agentos.Index.md` — the unified design note for the index; source of truth for the current conceptual model (`Soft.Programming.Language`, `Alignment.Surface`, runtime semantics, block syntax, etc.)
- `skills/agentos-index/` — the `Skill.Package` promoted from 513; contains reference files for block syntax, gating, eval loop, naming, etc.
- `notes/live/518-index-migration-2026-05-11.md` — migration session notes; decisions, new blocks, and learnings captured during migration

## Migration Order

Prioritize by importance and dependency:

1. **Tier 1** — Reserved system notes: routing, ontology
2. **Tier 2** — Core concepts: index self-description, naming, skill packaging
3. **Tier 3** — Project model: project identity, skills, numbering, md surfaces
4. **Tier 4** — Subsystems and workflows: hugentic flow, maintenance, doctor, missions, design sessions, agents, canvas

Within each tier, the agent proposes the next block and the user controls advancement.

## Completion

Migration is complete when:

- All meaningful content from `index-migration/` has been migrated or explicitly dropped
- `agentos index doctor` reports 0 errors and 0 warnings on the new index
- `001-ontology.md` is rebuilt with all current concepts
- `000-index.md` routes to all new notes
- `notes/index-migration/` can be archived or deleted
