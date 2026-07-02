# Writing Craft

The writing-quality floor for `What.Design.Session`. Apply on every line written into `Session.Abstract`, `Design.Index`, `Session.Notes`, or any other session surface. This reference is `Cited.Duplication` of `[Kernel.Writing, Kernel.Block, Design.Block, Natural.Placement, Hard.Evidence, Cited.Duplication, Inline.Relatedness]` from `agentos-pkg/index/`. The origin owns authority; this is the on-hand operational copy.

**Rules here, exemplars in `index-view.md`.** This file states *how to apply* the writing kernel; `index-view.md` holds the verbatim, well-formed blocks that show *what the bar looks like*. A writing standard does not transfer on principles alone — the line-granularity bar lives in the examples. Read `index-view.md` blocks as the calibration before you draft, and the § Line Granularity contrast below for the failure mode the rules do not catch on their own.

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

## Line Granularity — atomic vs welded

The most common off-spec failure is **welded lines**: prose chopped into bullets, where one bullet carries three or four dimensions joined by semicolons, em-dashes, or "which lets / and demotes" clauses. The line *touches* distinct facets, so it passes a careless reading of the rules — but it is not a kernel line. A kernel line is **one fact, one dimension**, reorderable, with nothing smuggled in.

This failure is invisible from the rules alone; it is only obvious against the exemplars in `index-view.md`. Keep these mocks in view:

**Welded (off-spec):**

```md
- its only mandatory dependency is the `iterante` runtime library; every other
  dependency is the author's choice, which is what lets `mission.py` import
  freely and demotes `iterante` tooling to opt-in (`Iterante.Ctx`)
```

One bullet, four dimensions welded: the mandatory dep, the author's freedom, free imports, tooling demotion. Each is a separate fundamental.

**Atomic (at-spec):**

```md
- `iterante` is the only mandatory dependency; all others are the author's choice
- the mission owns its full dependency set
- `mission.py` may import freely — `iterante` tooling becomes opt-in, not the sole channel (`Iterante.Ctx`)
```

The test: can you reorder the lines without breaking meaning, and does each line survive on its own? Welded lines fail both — drop a clause and the sentence collapses. If your draft reads like flowing prose with bullet markers, you welded it; split until each line is one dimension. Compare against any block in `index-view.md` — that is the granularity.

## Kernel.Block

`Kernel.Block` is the writing object that carries `Kernel.Writing`.

- a markdown section whose heading names the block's main topic — the heading is a conceptual commitment
- one block, one main topic — related material belongs in other blocks, grounding, appendix, or meta
- body lines are mostly bullets enriching the topic from different perspectives
- sections are named `Kernel.Block.Section`s: `Kernel.Block.Fundamentals` (the only required one) + `Kernel.Block.Grounding` + `Kernel.Block.Appendix` + `Kernel.Block.Meta`; `###` is just the inblock form
- dividing rule: fundamentals and appendix are about the concept; grounding cites evidence; meta is about the block itself
- meta is non-conceptual block data only — aliases, outlinks, findability; the strip-test: drop the line and the conceptual load is unchanged

Surface-placement variants of `Kernel.Block` differ only in placement and gating, not in writing rules; what a block may hold — e.g. status in meta — is a surface concern, allowed on design surfaces, barred on a `Stable.Surface`.

## Design.Block

`Design.Block` is the variant used in design artifacts and `Design.Index`. This is the block type a designer writes every turn.

- holds the full state of a concept in one place — fundamentals, grounding, and appendix together
- the in-session variant: `Index.Block` is compressed for the public index; `Appendix.Block` is exhaustive; `Design.Block` is both together for the working session
- at promotion time, fundamentals compress into `Index.Block`, appendix material moves to `Appendix.Block`
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

In a design session this is a constant decision: a drafted line is a fundamental, appendix depth, `#### meta` mechanics, or chat-grounding evidence — placement is part of the design, not an afterthought. The block-section split in `Design.Block` is `Natural.Placement` applied inside one block.

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
