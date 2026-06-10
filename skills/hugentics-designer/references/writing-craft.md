# Writing Craft

The writing-quality floor for `What.Design.Session`. Apply on every line written into `Session.Abstract`, `Design.Index`, `Session.Notes`, or any other session surface. This reference is `Cited.Duplication` of `[Kernel.Writing, Kernel.Block, Kernel.Block:Design, Natural.Placement, Hard.Evidence, Cited.Duplication, Inline.Relatedness]` from `agentos-pkg/index/`. The origin owns authority; this is the on-hand operational copy.

## Kernel.Writing

`Kernel.Writing` is the conceptual writing system every session output should pass through.

- the purpose: turn source material into named conceptual blocks that support future judgment
- each line aims at a fundamental dimension of the topic — the view is multi-faceted
- lines aim to be orthogonal — avoid redundancy, prefer independent facts
- language is direct — concise expression, no superfluous words
- completeness means covering the fundamental angles, not explaining every detail
- coverage over compression — losing a fundamental dimension is more costly than an extra line
- the filter on whether to capture a line: does it change future judgment?
- useful material can enter before it has mature structure — capture first, polish later

Applied in-session: when you draft a `Design.Index.Block`, walk every bullet against these tests. If two bullets compress to one without losing a dimension, fuse them. If a bullet only restates the heading, drop it.

## Kernel.Block

`Kernel.Block` is the writing object that carries `Kernel.Writing`.

- a markdown section whose heading names the block's main topic — the heading is a conceptual commitment
- one block, one main topic — related material belongs in other blocks, grounding, appendix, or meta
- body lines are mostly bullets enriching the topic from different perspectives
- structure: fundamentals (conceptual) + `### grounding` (chat evidence) + `### appendix` (extended conceptual) + `### meta` (non-conceptual)
- dividing rule: fundamentals and appendix are about the concept; grounding cites chat evidence; meta is about the block itself
- meta carries: aliases, outlinks, findability, status, open questions, session mechanics — anything non-conceptual

Session-loaded variants of `Kernel.Block` differ only in placement and gating, not in writing rules.

## Kernel.Block:Design

`Kernel.Block:Design` is the variant used in design artifacts and `Design.Index`. This is the block type a designer writes every turn.

- holds the full state of a concept in one place — fundamentals, grounding, and appendix together
- the in-session variant: `Kernel.Block:Index` is compressed for the public index; `Kernel.Block:Appendix` is exhaustive; `Kernel.Block:Design` is both together for the working session
- at promotion time, fundamentals compress into `Kernel.Block:Index`, appendix material moves to `Kernel.Block:Appendix`
- preserve user's wording when it carries design judgment — never paraphrase quoted-tone phrasing into agent-tone summary
- in a `Design.Index`, the block uses H3 (under the `## Design.Index` H2 parent); appendix and meta are `#### appendix` and `#### meta`

What a fundamentals line should carry, in order of weight:

- the **definition** — what the concept is
- **boundaries** — what it is NOT, where it stops
- **judgments** — design opinions explicit, not buried in tone
- **relations** — coupling to other concepts (use `Inline.Relatedness`)
- **unresolved conceptual pressure** — what's open, marked as open

If a block has no boundary line and no unresolved-pressure line, it is probably under-specified.

### appendix — extended conceptual

Use the block's `#### appendix` for:

- rationale for the decisions in the fundamentals
- pressure tests, edge cases, usage scenarios
- rejected alternatives and why
- worked examples
- depth that didn't fit the compressed fundamentals

### meta — non-conceptual

Use the block's `#### meta` for:

- aliases
- outlinks and relations
- status (fresh, active, converging, parked, settled)
- open questions
- session-mechanics annotations
- promotion notes if the concept may move to a public surface

## Natural.Placement

`Natural.Placement` is the principle that each surface holds the facet of a concept that is natural to its function.

- the full description of a concept is distributed across surfaces, each complementing the others: index → conceptual grounding and discovery; appendix → extended depth and scoped views; skills → operational behavior; code → the implementation itself; chat → the user/agent interaction record
- it primarily governs where origin material naturally belongs
- describing in markdown what code already holds is redundant placement, not useful duplication — the question is always placement
- content that feels unnatural in a surface is probably misplaced
- a cited duplicate may also be naturally placed when local use strongly benefits from the repeated content; uncited or stale duplication is the anti-pattern, not duplication itself

In a design session this is a constant decision: a drafted line is a fundamental, appendix depth, `#### meta` mechanics, or chat-grounding evidence — placement is part of the design, not an afterthought. The block-section split in `Kernel.Block:Design` is `Natural.Placement` applied inside one block.

## Hard.Evidence

`Hard.Evidence` is the principle that evidence-based arguments beat agent assumption during alignment work.

- concrete evidence sources: explicit user instructions, inspected codebase state, active session artifacts, stable project surfaces (`Md.Surface`, `Index.Block`, `Skill.Md`), `Chat.Surface` content with priority to user turns
- alignment sessions aim to be `Hard.Evidence`-based as much as possible — more is welcome, but the core alignment axes are the priority
- agent assumption is allowed as a provisional input, but should be marked as such — never presented as established fact
- when evidence and assumption conflict, evidence wins; the assumption gets dropped or surfaced as a question

In a `Design.Index.Block`, mark assumption-based lines as such — typically with phrasing like "assumed:" or by moving the line to `#### meta` under "open" until evidence arrives.

## Cited.Duplication

`Cited.Duplication` is the discipline this very reference applies.

- intentional duplication of concept material into another surface with an explicit `Concept.Cite` to the origin
- used when local access improves agent performance, bootstrapping, workflow execution, or readability
- the duplicate may be rewritten or summarized, but must remain aligned with the cited origin
- the cite anchors maintenance — if the origin shifts, drift becomes visible
- inside a design session: use `Cited.Duplication` when the discussion needs context from another surface (a prior session, a skill, an index block) — pull the relevant lines in, cite, do not force the reader to chase

Format the citation as `[Concept.Name]` inline, or as an opening note like this file's top line.

## Inline.Relatedness

`Inline.Relatedness` is the writing discipline of naturally blending related `Dotted.Names` into concept text.

- when a related concept is already part of a sentence's meaning, use its `Dotted.Name`
- the goal is not to create explicit related-edge metadata — relationships emerge from natural prose
- use `[Concept.Cite]` bracket form only when a materially important relation should be visible but does not fit the sentence
- enriches the session by making concept relationships discoverable inside ordinary writing

In a `Design.Index`, `Inline.Relatedness` means: write `the workflow registers via [Mia.View.Workflow]`, not `the workflow uses the registration mechanism (see Mia.View.Workflow)`.

## Operational Discipline

Per turn, before writing into a session surface:

- name the block — heading is the conceptual commitment
- draft fundamentals — each line a distinct facet (definition, boundary, judgment, relation, open)
- pressure-check for orthogonality — two lines saying the same thing fuse to one
- pressure-check for boundaries — does the block name what it is NOT?
- pressure-check for evidence — which lines are `Hard.Evidence`, which are assumption?
- preserve user wording where it carries judgment
- move rationale / examples / tradeoffs to `#### appendix`
- move status / open questions / aliases to `#### meta`

If the user pushes back on a line, the line probably failed one of those checks.
