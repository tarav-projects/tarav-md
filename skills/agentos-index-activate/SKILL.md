---
name: agentos-index-activate
description: "Bootstrap the Agentos Index runtime for a session. Reads 000-index.md routing table, activates the Index.Eval.Loop, and loads agentos-index-trigger for ongoing detection."
---

# agentos-index-activate

Bootstrap the Agentos Index runtime for this session.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.
Full design reference: `agentos-index/references/eval-loop.md`

## What This Does

- reads `index/000-index.md` routing table to establish minimal index context
- may read additional index notes relevant to the current task context
- activates `Index.Eval.Loop` behavior for the rest of the session
- loads `agentos-index-trigger` for ongoing `Dotted.Name` detection

The index lives at `notes/index/` in the project root.

## Bootstrap Context

Once activated, you operate with these behaviors:

### Dotted.Name Detection

Recognize `Dotted.Names` in conversation — capitalized words joined by dots, always 2+ parts.
Shapes: `Word.Word`, `Word.Word:target`, `<Word>.Word`, `<Word>.Word:<target>`.
NOT triggers: abbreviations (`e.g.`), filenames (`file.txt`), URLs, lowercase dotted, single-part names.

### Index.Eval.Loop (condensed)

When a `Dotted.Name` is detected or you need grounding:

1. **Resolve** — match against routing table (`000-index.md`), load the concept's flat file
2. **Ground** — load relevant `Index.Block` fundamentals into context
3. **Detect gaps** — if unresolved: park as `Unresolved.Index.Name`
4. **Suggest** — if same name recurs 3+ times, suggest registration to user
5. **Park** — unresolved names stay in session working list

### Footer

Report index operations at the end of your response:
```
> Index: loaded `Concept.A`, `Concept.B` | unresolved: `Unknown.Name`
```

### Loading behavior

- default: load block fundamentals only (~600 chars)
- escalate by judgment: load full block or full note if concept is central
- don't auto-load the whole graph — follow links only when needed

## After Bootstrap

- load `agentos-index-trigger` skill for ongoing detection
- for full design context, load `agentos-index`
- for name resolution, load `agentos-index-resolution`
- for writing to the index, the user invokes `agentos-index-writer`
