# Index View

A curated `Cited.Duplication` of the `agentos-pkg` index blocks this skill treats as fundamental. Two jobs at once:

- **form exemplars** — these are real, well-formed `Kernel.Block`s. They are the calibration for *how a block should be written* — atomic, orthogonal lines. When you draft a `Kernel.Block:Design`, imitate the line granularity you see here, not your prose instinct. `writing-craft.md` states the rules; this file shows the bar.
- **concept context** — they are also the hugentic concepts the designer uses every turn, loaded so the skill is self-sufficient and never needs to open the live index just to recall form.

Each block below is copied **verbatim** from its origin. The origin owns authority; this is a drift-checkable copy. If a block here disagrees with origin, origin wins and this copy is stale — fix it.

This is a *selection*, not the whole index. Start small; add a block here only when a real gap shows in session.

---

## Writing kernel

Origin: `agentos-pkg/index/102-index.md` (`Kernel.Writing`, `Kernel.Block`) and `agentos-pkg/index/100-index.md` (`Kernel.Block:Design`).

### Kernel.Writing

- `Kernel.Writing` is a portable conceptual writing system for capturing and communicating fundamental signal
- it can be applied retrospectively to an existing corpus or actively during an ongoing conversation
- source material can be chat, argument, codebase, documentation, design artifact, implementation behavior, or observation
- in live use, it helps participants converge by naming topics, separating dimensions, and reducing redundant prose
- in retrospective use, it distills existing material into named conceptual blocks
- its purpose is to turn source material into named conceptual blocks that support future judgment
- each line aims to describe a fundamental dimension of the topic — the view is multi-faceted
- lines aim to be orthogonal — avoid redundancy, prefer independent facts
- language is direct — prefer concise expression, avoid superfluous words
- completeness means covering the fundamental angles of a topic, not explaining every detail
- coverage over compression — losing a fundamental dimension is more costly than an extra line
- space constraints are external — the surface determines the budget, not the philosophy
- the filter: capture material that changes future judgment
- useful material can enter before it has mature structure — capture first, polish later
- `Kernel.Block` is the writing object that embodies `Kernel.Writing`

### Kernel.Block

- `Kernel.Block` is the base writing object of `Kernel.Writing`
- a block is a markdown section whose heading names the block's main topic
- the heading is a conceptual commitment — it states what the block is about
- a block should center one main topic; related material belongs in separate blocks, grounding, appendix, or meta
- body lines are mostly bullets that enrich the topic from different perspectives
- a block applies `Kernel.Writing` at section scale
- structure: fundamentals (conceptual) + `### grounding` (chat evidence) + `### appendix` (extended conceptual) + `### meta` (non-conceptual)
- the dividing rule: fundamentals and appendix are about the concept; grounding cites chat evidence; meta is about the block itself
- meta covers: aliases, outlinks, findability, status, open questions, session mechanics — anything non-conceptual
- all block types in the system are parameterizations of `Kernel.Block` placed in specific surfaces with specific constraints
- parameterized using `Dotted.Parameterized.Notation`: `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design`

### Kernel.Block:Design

- `Kernel.Block:Design` is `Kernel.Block` used in design artifacts — fundamentals, grounding, and appendix in a single block
- holds the full state of a concept in one place — used in conversations and design sessions
- at promotion time: fundamentals compress into `Kernel.Block:Index`, appendix material goes to `Kernel.Block:Appendix`
- the distinction: `Kernel.Block:Index` is compressed, `Kernel.Block:Appendix` is exhaustive, `Kernel.Block:Design` is both together
- preserve user's wording when it carries design judgment

#### meta

- aliases: `Design.Block`, `Design.Session.Block`, `Design.Index.Block`

---

## Alignment spine

Origin: `agentos-pkg/index/102-index.md` (`Alignment.Loop`, `Alignment.Backend`, `Hard.Evidence`).

### Alignment.Loop

- `Alignment.Loop` is the general workflow machinery for human-agent convergence
- sequence: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`
- parameterized by phase: `Alignment.Loop:What` (design), `Alignment.Loop:How` (impl design), `Alignment.Loop:Exec` (impl execution, light)

### Alignment.Backend

- `Alignment.Backend` is where session state lives
- `Alignment.Backend:InChat` — state lives in chat, no file overhead
- `Alignment.Backend:Artifact` — state lives in a file-backed artifact, durable and handoff-ready
- parameterized by phase: `Alignment.Backend:InChat:What`, `Alignment.Backend:Artifact:What`, etc.
- `Alignment.Backend:InChat` and `Chat.Surface` are distinct concerns: `Alignment.Backend:InChat` is the active session state — the live chat as it unfolds, "what's in RAM"; `Chat.Surface` is the durable record of past chats — the archived interaction trail

### Hard.Evidence

- `Hard.Evidence` is the principle that evidence-based arguments have priority over agent assumptions during alignment work
- concrete evidence: user instructions, inspected codebase state, active session artifacts, stable project surfaces, `Chat.Surface` content (especially user turns)
- alignment sessions aim to be `Hard.Evidence`-based — more is welcome, but the core alignment axes are the priority

---

## How to read these as exemplars

Look at the **line granularity**, not just the content:

- every line is one fact, one dimension — never a semicolon-chain welding three facets together
- the first line is the definition in `Concept is a …` form
- lines are independent — you could reorder them and lose nothing
- no subordinate clauses smuggling a second dimension into a line ("X, which is what lets Y and demotes Z")

When your draft block does not look like these, it is off-spec regardless of whether the content is right. See `writing-craft.md` § Line Granularity for the welded-vs-atomic contrast.
