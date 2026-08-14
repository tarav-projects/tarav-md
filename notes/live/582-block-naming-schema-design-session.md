# Block Naming Schema - design-session

## Session.Abstract

- **scope:** redesign block naming into one unified `Block.Naming.Schema` — legal name forms, sigil semantics, the two naming spaces, and the locator form
- **convergence target:** approved edits to the `tarav-pkg` index — one new schema block cluster, revisions to `Dotted.Notation`, `Block.Path`, `Index.Block`, retirement of `Dotted.Parameterized.Notation`
- **status:** landed — all seven blocks approved and written to the index (2026-07-12); remaining follow-up is the `:`→`::` surface migration impl-req
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

### Naming.Sigil.Vocabulary

- `Naming.Sigil.Vocabulary` is the closed set of primitives a `Block.Naming.Schema` name composes from
- each sigil carries exactly one meaning; expressivity comes from composition, never from overloading
- `.` joins words into one name atom: `Concept.X`, `AGENTS.md`
- `/` states descent — the right side lives inside the left side's namespace, in either space
- `#` switches space — the name leaves file space and enters the file's internal regions
- `::` states type — the right side is an entity of the left side's type: `Line.Type::DF`
- `:` states line position inside a file: `@<project>/AGENTS.md:42`
- `<...>` marks a variable part, resolved by context and legal in any space: `<project>`
- `@` is the locator prefix — it anchors a name in file space from its first character
- `^` is reserved by `Anchory.Anchor` for evidence links and never appears inside a block name
- a sigil's meaning is invariant across positions; where it may appear is grammar, not meaning
- the vocabulary is closed by discipline, not by parser — extending it is a gated index decision

#### appendix

- members enumerate inline (one line per sigil), diverging from the `Line.Type.Vocabulary` per-member-block precedent: a sigil's whole semantics fits one line, a `Line.Type` carries validation behavior that earns a block
- the `^` reservation line documents the full sigil budget on index surfaces — collision-proofing, though `^` is not a naming primitive; `Anchory.System` owns its semantics
- `::` mirrors Julia's type-ascription syntax; its type reading subsumes the retired "applied to a target" phrasing: `Maintenance.System::Agentos` reads as the `Maintenance.System` instance identified by `Agentos`
- `:` for lines mirrors the universal `path:line` convention (grep output, editor jump targets); `::` longest-matches over `:`, so parsing is unambiguous
- `#` and `:` are the two file-internal addressers — `#` by heading region (stable), `:` by line number (volatile); prefer regions for durable names

#### meta

- status: converging
- related: `Block.Naming.Schema`, `Line.Type.Vocabulary`, `Anchory.System`, `Dotted.Notation`
- open: none

### Locator.Name

- `Locator.Name` is the `Block.Naming.Schema` form that names an entity by its workspace address
- it begins with `@` — the locator prefix declares file space from the first character
- the body is a path in filesystem language: `@<project>/AGENTS.md`, `@notes/live/582-block-naming-schema-design-session.md`
- roots follow common sense, often a `<...>` variable — no closed root vocabulary exists
- `#` extends the name into the file's heading regions, with `/` descent: `@<project>/AGENTS.md#Agentos/Index`
- `:` extends the name to a line: `@dev/tool.py:42` — heading regions are the durable choice (`Naming.Sigil.Vocabulary`)
- it serves entities that already have a native address — a file, a section, a region — sparing an artificial `Dotted.Name`
- the `@` is agent-maintained: users may omit it, and a bare mention resolves to the locator-named block when it matches (`Bla/Blo` → `@Bla/Blo`)
- a locator-named block is a normal `Kernel.Block` — the address form adds no semantics

#### appendix

- bare-mention resolution: a bare `Bla/Blo` is ontology-space by default; a `Locator.Name` match wins when it exists
- if both an ontology block `Bla/Blo` and a locator block `@Bla/Blo` exist, the mention is ambiguous — resolve the `Fuzzy.Dotted.Name` way: surface both candidates and confirm; no fixed precedence
- rejected: scheme prefixes (`project:`, `skill:`, `index:`) from the origin sketch — replaced by `@` + common-sense roots; `:` now states line position, making schemes unparseable anyway

#### meta

- status: converging
- related: `Block.Naming.Schema`, `Naming.Sigil.Vocabulary`, `Fuzzy.Dotted.Name`, `Kernel.Block.Meta`
- open: none — bare-mention ambiguity resolved by candidate surfacing, not precedence

## Session.Notes

- sigil table and `:`/`/` semantics consolidated into `Naming.Sigil.Vocabulary` (Design.Index)
- `@` maintenance rule consolidated into `Locator.Name` (Design.Index)
- surfaces that restate naming and will need alignment at landing: `tarav-pkg/SKILL.md` (Dotted Notation section), `agentos-index` references, `Index.Block` heading line
- landing-phase impl-req of its own: the `:`→`::` migration — single-`:` parameterized names are pervasive (`Line.Type:DF`, `Alignment.Backend:Artifact:What`, `Natural.Placement:Skills`, the Batchy `Skill.Arg:X` convention in every skill); same shape as the `@`→`^` migration (regex rewrite, linter legacy check, doc updates) but wider, reaching skill files beyond the index
- pre-existing loose end (out of scope): `^20260630-0` example in `tarav-pkg/SKILL.md` does not resolve in the anchory depot

## Session.Log

- 2026-07-09 session opened, artifact backend; scope: block naming schema redesign
- 2026-07-09 prior landed work recorded: Anchory `@`→`^` migration (580)
- 2026-07-09 first draft of `Block.Naming.Schema` block written
- 2026-07-09 redraft after `Kernel.Writing` research pass: de-welded lines, removed deixis, anti-explosion rationale consolidated to appendix; pending commitments noted: `Locator.Name` and the two-space model cited before drafted
- 2026-07-09 `Naming.Sigil.Vocabulary` drafted and accepted: inline member enumeration (divergence from `Line.Type.Vocabulary` precedent recorded in appendix), `^` reservation kept, closed-by-discipline extension rule; sigil table moved out of `Session.Notes` into the block
- 2026-07-09 sigil revision: type statements move from `:` to `::` (Julia mirror); `:` freed for line position inside a file (`path:line` convention); `:`→`::` migration recorded as a landing-phase impl-req in `Session.Notes`
- 2026-07-12 landing batch executed after a seven-block approval walk: new `design/108-design.md` (`Block.Naming.Schema`, `Naming.Sigil.Vocabulary`, `Locator.Name`) with three appendix files; revisions landed in 100 (`Dotted.Notation`, `Index.Block`) and 103 (`Block.Path`, root relaxed to anchored/unanchored); `Dotted.Parameterized.Notation` deleted with five citations re-pointed (106, 101×2, batchy-skill-run.md, ontology-registry.md); router updated (108 entry added, retirement removed); landing anchors `^c20260712-0u`…`-6` minted on the approval turns; linter clean (19 checks, 0 findings)
- 2026-07-09 `Locator.Name` drafted and accepted: `@`-anchored file-space form, `#`/`:` region grammar, common-sense roots, agent-maintained `@`; bare-mention ambiguity resolved by `Fuzzy.Dotted.Name`-style candidate surfacing; scheme prefixes recorded as rejected; one pending commitment discharged (two-space model line in `Block.Naming.Schema` remains cited-only)
