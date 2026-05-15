# Block Syntax

## Kernel.Block:Index

- `Kernel.Block:Index` is `Kernel.Block` placed in `notes/index/` — the loadable unit of meaning in the index
- the smallest node in the index knowledge graph
- the unit loaded into agent context during `Index.Eval.Loop`
- anchored by a heading (H2-H6) that names the concept using `Dotted.Notation`
- aliases: `Index.Block`, `Global.Block`

A block must be:

- **loadable**: small enough to fit in agent context without waste (25-line ceiling)
- **grounding**: gives the agent enough to reason correctly about the concept
- **precise**: reduces ambiguity between what the human means and what the agent understands
- **coupled-but-addressable**: lives in its proper note but can be pulled into context independently

### Block layers

1. **Heading** — identity (the `Dotted.Name`)
2. **Fundamentals** (= the body) — bullet-point sentences, the concept's essential content
3. **Appendix** (optional `### appendix`) — extended conceptual material
4. **Meta** (optional `### meta`) — aliases, findability, outlinks, status — anything non-conceptual

- fundamentals aren't a special section — they're just what the block IS
- the block is fundamentals by default — the whole body is bullet-point sentences
- the dividing rule: fundamentals and appendix are about the concept; meta is about the block itself
- blank lines separate bullet paragraphs — each group is a logical unit
- the 25-line ceiling forces compression — if you can't fit it, split the block

****

## Index.Block.Syntax

- `Index.Block.Syntax` is the structural convention for writing `Index.Blocks` — the "type system" of the index
- separates how a block is written (syntax) from what it means (semantics)
- the concrete target for linting rules and block shape validation

### Universal block shape

```markdown
## Dotted.Name

- [fundamental statement]
- [fundamental statement]
    - [qualification or sub-point]
- [fundamental statement]

- [another bullet paragraph — different facet]
- [statement]
    - [sub-point]

[optional: examples, code, etc.]

### meta

- aliases: [shorter names for this concept]
- findability: [keywords, approximate names]
- related: `Related.Concept.One`, `Related.Concept.Two`
```

### Fields

| Field | Required? | Purpose |
|---|---|---|
| **Heading** (H2-H6) | required | identity — names the concept |
| **Fundamentals** | required | grounding — bullet-point sentences, essential content (~600 chars) |
| **Extra** | optional | examples, code, clarifying material |
| **Appendix** | optional | depth — extended conceptual material |
| **Meta** | optional | non-conceptual — aliases, findability, outlinks, status |

### Size constraint

- **line limit**: 25 lines per block (hard ceiling)
- **character limit per line**: enforced to keep lines focused
- both are context-budget constraints, not aesthetics
- if too big: carrying more than one idea → split into sibling blocks

### Separator requirement

- `****` separators between H2-level blocks are mandatory in index notes
- makes all index content machine-parseable by the `mdblocks` toolchain
- enforced by `agentos index doctor` (CLI) and `agentos-index-doctor` (skill)

### Write first, polish later

- the linter does NOT run at write time — writing is frictionless
- `agentos-index-writer` focuses on meaning alignment, not format enforcement
- linting happens later: during maintenance passes, doctor reviews, compilation
- getting concepts into the index matters more than perfect format

### Linting

- currently: `agentos stdlib mdblocks lint` (block-level)
- future: `agentos index lint` (index-level, including semantic checks)
- the linter is the "compiler" — catches structural violations before they become reasoning errors

****

## Bullet.Point.Sentence

- `Bullet.Point.Sentence` is the writing style for the entire index
- bullet-pointed sentences, one idea per line
- indentation for qualification or sub-points
- blank lines to separate bullet paragraphs (logical groups)

Writing guidelines (paper-abstract style):

- each bullet is one self-contained statement
- together they give the minimal mental model needed to reason correctly
- locating (what kind of thing is this) — use common sense, no rigid categories
- differentiating — only when genuinely valuable, don't force it
- not explanations, not filler — just fundamentals
- concise, direct, high-signal per line

****

## Index.Note

- `Index.Note` is the module-level container — a cluster of related `Index.Blocks`
- centered on one named concept or a tight concept cluster
- both an organizational unit AND a semantic unit

### Notes carry meaning

- the first header + opening paragraph define what the note IS (semantic identity)
- note-level semantics affects how its blocks are interpreted
- blocks are the main semantic units, but they are coupled to their note context

### Properties

- one concept or tight cluster per note
- numbered with a stable 3-digit prefix
- the filename is the stable handle; the title may evolve
- the note header establishes context for all blocks within

****

## Index.Note.Style

- `Index.Note.Style` is the desired mature shape for stable index notes
- concept-centered: organized around a `Named.Concept`, not a task or timeline
- block-structured: meaning is carried in discrete `Index.Blocks`
- high-signal: every block and every line earns its place
- low-prose: bullets and short declarative statements over essay-style paragraphs
- self-locating: the title and opening line ground the reader immediately

This is a convergence target, not a gate. The `Stub.Convention` is the minimum entry bar.
