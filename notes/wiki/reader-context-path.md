# Reader.Context.Path

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Reading paths and expected context

Reader.Context.Path belongs in `skw.skills`, the skill specialization of
[Skillware](skillware.md). It models the context a reader is expected to have
because of the declared route used to reach a block. For example:
Skill.Description → SKILL.md → link to file A → preceding blocks → block X.
It models this portion of reader context, not the reader's entire context.
Developers can rely on earlier material without repeating it, while blocks
declare Reading.Dependencies on the context they assume.
<!-- tarav.breadcrumb f4507db39735 -->

Multiple routes can reach the same block. Their available contexts can be
examined per path, intersected to identify common availability, or united to
identify possible availability. Checks should identify an unmet dependency
and the path that misses it. Developers can then revise routing, introduce a
prerequisite link, or make the consuming block more self-contained.
<!-- tarav.breadcrumb 615c8a733f67 -->

## Typed delivery and semantic targets

Links have reading semantics: some are expected to be followed to reach a
block; others offer further explanation if needed. Dependencies also express
delivery requirements, such as content being inlined or at least referenced.
The model needs to distinguish these forms of availability. Exact link and
dependency Types remain to be designed; the discussion establishes the need
for control and expressivity rather than a fixed schema.
<!-- tarav.breadcrumb ffd8b5134f4b -->

Blocks explicitly declare the semantic entities they contain or provide.
Those declarations are claims, not guarantees about their text, and supply
the targets used to communicate dependencies in the SKW graph. Semantic
content is not inferred merely from a heading or from opaque block output.
<!-- tarav.breadcrumb 91136a6421a1 -->
<!-- tarav.breadcrumb dc20ec72bd12 -->

## Declarations are properties of blocks

All these declarations belong to blocks. An ordinary block can declare that
it contains a link of a particular type to entity A, inlines entity Z, and
requires entity B to have been inlined for its reading. Specialized blocks
such as links or literal inlines are useful implementations, but embedded
links do not each need to become separate blocks. The reading-path mechanics
consume the declarations uniformly without interpreting the prose.
<!-- tarav.breadcrumb 102c4fef933e -->
<!-- tarav.breadcrumb 15bb276efe4b -->

## Structural checking boundary

The immediate work is reading-path mechanics and their structural checks:
does a declared path supply the required semantic entity in the required
form? They take content declarations as given. Assessing whether actual text
substantiates those claims belongs to separate semantic checks and scoring,
to be developed later. A successful structural check certifies connectivity
of the declarations, not the truth of their semantic claims.
<!-- tarav.breadcrumb 34dbcff63198 -->

## Entity identity and subtype semantics

Reading targets require only `TaravEntity`; no reading-specific
`SemanticEntity` type is needed. Content and entities can belong to other
workflows. The reading-path system concerns itself with their declared
presence and availability; it neither collects nor renders that content.
This refines the earlier illustrative code, which introduced a separate
semantic-entity type.
<!-- tarav.breadcrumb b5cbb95595d1 -->

Blocks themselves are TaravEntities. Their `id` values must be UUIDs, with
separate free-text `label` values for readable presentation. The earlier
example `id="scope"` conflated those roles and is not the intended identity
contract. These are design requirements, not a claim that existing SKW
blocks have already been migrated.
<!-- tarav.breadcrumb 43206f78d3ec -->

Prefer a base type plus semantic subtypes over a general type with mode
strings for reading relationships. The Type Graph participates in the
Diagram, so explicit subtypes make the meaning and available kinds of
relationships more discoverable. This is a general modeling preference;
the precise subtype set and names remain to be designed. It refines the
earlier illustrative `ReadingLink(..., mode="consult")` shape without
changing the uniform block-declaration model.
<!-- tarav.breadcrumb 5e002c69d5d2 -->

## Implemented structural slice — 2026-09-30

Impl.Req 828 made SKW blocks `TaravEntity` instances with separate UUID Ships
and local labels. Typed declarations now live on source blocks; the loading
Record retains block bindings, route parents, and the entry root. The analyzer
reports per-route state, intersection/union availability, requirement
observations, diagnostics, and completeness. It does not assess whether a
block's prose proves its declarations. See the
[implementation request](../../../../tarav-py/notes/live/828-reading-path-checks-poi-impl-req.md)
and [reading model](../../../../tarav-py/src/tarav/l1/skw/reading.py).
<!-- tarav.breadcrumb 49e016172044 -->

The maintained `tarav-hugentics` and `tarav-pkg` SKW depots were migrated with
explicit per-document old-label-to-Ship maps. Historical generation
annotations remain untouched; the mapping preserves their recipe fingerprints.
The active source/product lock baselines were rebuilt after the identity-only
source change. Generated anchors may change while authored block content is
preserved.
<!-- tarav.breadcrumb c5ce66086d77 -->

## Containment supplies content; links supply references — 2026-09-30

The discussion simplified the content model: `contains` is sufficient;
inlining need not be a separate declaration. A block declares which entities
its content contains, with further qualification available when useful.
When the contained entity is another SKW block, containment claims that
loading the containing block also loads that block's content. Its annotations
therefore participate recursively in the supplied reader context. This is
declared content equivalence, not a rendering instruction or prose inference.
<!-- tarav.breadcrumb bd60efd23489 -->

Links are weaker: they expose a reference that the agent may choose to
follow. Containment propagates the contained block's annotations, including
its links, but reading-path analysis does not expand the linked target's
annotations merely because that reference is available.
<!-- tarav.breadcrumb 7ef2f2e6329c -->

```text
A contains B contains C → A supplies B and C.
A contains B links C    → A supplies B and a reference to C.
A links B contains C   → A supplies only a reference to B.
```

This stopping rule belongs to reading-path analysis, not to the graph as a
whole. Other analyses may follow links further for their own purposes.
Structural checks consume the declarations; checking whether the actual
content substantiates them remains a separate responsibility.
<!-- tarav.breadcrumb 846885b3831d -->

This refines the earlier inline/expected-link discussion. In particular,
the review of 828 must distinguish exposing B's link within A from assuming
that the reader followed it and loaded C. The former follows from containment;
the latter does not follow from link availability alone. This capture records
the clarified design, not an implementation change or a new code verification.

Evidence pending: the supporting User Turns are in the current Codex session
`01a0d86c-9538-7be1-af96-014cd4203d61`, from “maybe we do not need inlines”
through the confirmation that other analyses can follow links further.
Chatlas refresh was denied write access to its derivation cache during this
capture. Exact Turn attachments and Git closure remain pending; no Breadcrumb
IDs or Turn hashes have been invented.

## Containment and path accumulation

Containment and reading order are separate relationships. If A contains C,
and A precedes B on the reading path, C is available when B requires it.
A does not need to contain B. The same requirement may be unmet when B is
reached through another path that has not supplied C.
<!-- tarav.breadcrumb 67f14f492dd6 -->

The implementation in
[830](../../../../tarav-py/notes/live/830-reading-containment-impl-req.md)
adds `Contains`, recursively expands contained block annotations, and keeps
links as references without automatically advancing to their targets.
Explicit reading routes remain separate. `IncludesBlock` specializes
containment with rendering composition; plain containment does not render.
Shared Checks and POI integration remains in place. Focused verification:
62 tests passed; Ruff passed. See `tarav-py/src/tarav/l1/skw/reading.py`,
`loading.py`, and `tests/test_skw_loading.py` for executable behavior.

Evidence pending: the same session's later clarification beginning “If A
contains C” and its confirmations support this distinction. Chatlas ledger
access was denied writing the Normal Model lock; exact Turn Breadcrumbs and
completion commits remain pending.

Evidence recovery: permissions were restored and the supporting User Turns
were resolved through Chatlas. The pending notices above retain the history
of the original capture; Breadcrumb submission is now available.

## Content claims, reading dependencies and computed paths

Use separate concepts rather than one ambiguous `reading` field:

- `contains`: entities the block claims its output contains. This is a
  content declaration, not a relationship owned exclusively by reading analysis.
- `reading_deps`: what the reader needs to know to understand this block;
  reading-path checks determine whether that context is available.

The reading-path analyzer consumes content claims; it does not define their
entire meaning. A combined `reader_context` or `reading_context` field was
considered and rejected in favor of this separation.
<!-- tarav.breadcrumb 14d04eb3d35e -->

Reading paths describe how context becomes available when a reader reaches a
block. They can be computed from the block's position, including its file,
preceding blocks and entry point. Explicit declarations can supplement that
structure, but the concept does not require a registry, a `reading_paths`
field, or a dedicated file merely to exist. This refines the earlier
suggestion to rename `loading.json`: naming the concept is not a decision to
retain that storage arrangement.
<!-- tarav.breadcrumb 4c54afb27f6e -->
<!-- tarav.breadcrumb eaeb73e6a6d3 -->

These are design decisions for the next revision, not a claim that the current
`reading` record field and loading file have already been migrated.

## Split fields implemented

[831](../../../../tarav-py/notes/live/831-skw-content-and-reading-fields-impl-req.md)
implements `contains`, `reading_deps` and separate `links` lists. A package
without a loading file can compute bindings and reading paths from source
block positions; optional explicit route files remain supported. Contains
is no longer a ReadingDeclaration subtype. The maintained tarav-hugentics
source records were migrated without changing their block IDs or output text.
The old `reading` field requires explicit migration rather than silent fallback.
<!-- tarav.breadcrumb 5b43341ad433 -->
<!-- tarav.breadcrumb 9ebdbf3e39dd -->
