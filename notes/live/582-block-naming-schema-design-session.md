# Block Naming Schema - design-session

## Session.Abstract

- **scope:** redesign block naming into one unified `Block.Naming.Schema` — legal name forms, sigil semantics, the two naming spaces, and the locator form
- **convergence target:** approved edits to the `agentos-pkg` index — one new schema block cluster, revisions to `Dotted.Notation`, `Block.Path`, `Index.Block`, retirement of `Dotted.Parameterized.Notation`
- **prior work landed:** `@` freed for locators — Anchory anchors migrated to `^` (impl-req 580, executed and reviewed)
- **source:** this session plus the codex session `019f475c-0b78-7580-b13f-cc474d0e8786` where the two-form idea originated

## Design.Index

### Block.Naming.Schema

- `Block.Naming.Schema` is the accepted syntax set for naming a `Kernel.Block`
- one grammar underlies every form: a name is a root plus an optional region path
- a name traverses up to two spaces: ontology space (concepts) and file space (surfaces)
- legal forms: `Dotted.Name` (compact symbolic), `Block.Path` (ontology topology), `Locator.Name` (`@`-anchored file or region address)
- the full string is the name of the entity at hand — sigils compose names, they are not operations on them
- name syntax does not change `Kernel.Block` semantics — a block is a block under any legal form
- a legal name carries at least one sigil; a single bare word is not a name
- sigils keep names distinguishable from natural prose — inline-always, grep-able (`Name.As.Index`)
- choose the form that preserves the entity's natural identity — a native address over an artificial coinage
- friendly alternates live as aliases in `Kernel.Block.Meta`, not as competing names
- routing is form-neutral: `000-INDEX.md` routes any legal name

#### appendix

- rationale: a block about `<project>/AGENTS.md#Agentos` previously had no honest name — dotted coinage for files causes concept-name explosion for no reason
- the four motivating usage cases: bare concept, ontological nesting, a file as ontology entity, a region inside a file
- rejected: form-dependent semantics ("concept blocks vs address blocks") — rejected twice in the origin session; blocks are blocks
- rejected: a closed vocabulary of file-space root tokens — common sense governs roots; `<...>` variables are self-describing

#### meta

- status: converging
- related: `Kernel.Block`, `Name.As.Index`, `Dotted.Notation`, `Block.Path`, `Fuzzy.Dotted.Name`
- open: router sorting/placement of `@`-named blocks in `000-INDEX.md`
- open: exact child-block split (`Naming.Sigil.Vocabulary`, `Locator.Name`) vs one bigger block

## Session.Notes

- sigil table settled in chat, pending its own block draft: `.` word-joiner, `/` descent, `#` file→region space switch, `:` type statement (Julia `::`), `<...>` variable part (space-agnostic), `@` locator prefix, `^` evidence anchor (Anchory)
- `:` vs `/` semantics settled: `Concept.X:Blo` — Blo is of the type Concept.X; `Concept.X/Blo` — Blo lives inside Concept.X's namespace; both full strings name the entity
- the type reading of `:` subsumes the old "applied to a target" phrasing of `Dotted.Parameterized.Notation`
- `@` maintenance rule settled: agents maintain the `@`, users need not type it — a user's `Bla/Blo` resolves to block `@Bla/Blo` when that is the match; usability must not suffer
- surfaces that restate naming and will need alignment at landing: `agentos-pkg/SKILL.md` (Dotted Notation section), `agentos-index` references, `Index.Block` heading line
- pre-existing loose end (out of scope): `^20260630-0` example in `agentos-pkg/SKILL.md` does not resolve in the anchory depot

## Session.Log

- 2026-07-09 session opened, artifact backend; scope: block naming schema redesign
- 2026-07-09 prior landed work recorded: Anchory `@`→`^` migration (580)
- 2026-07-09 first draft of `Block.Naming.Schema` block written
- 2026-07-09 redraft after `Kernel.Writing` research pass: de-welded lines, removed deixis, anti-explosion rationale consolidated to appendix; pending commitments noted: `Locator.Name` and the two-space model cited before drafted
