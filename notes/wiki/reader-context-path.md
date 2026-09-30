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
<!-- tarav.breadcrumb f4507db397357d7fbec0a471d988d9f4f4f49b5ce7b8ab8e86d5526ba80685b9 -->

Multiple routes can reach the same block. Their available contexts can be
examined per path, intersected to identify common availability, or united to
identify possible availability. Checks should identify an unmet dependency
and the path that misses it. Developers can then revise routing, introduce a
prerequisite link, or make the consuming block more self-contained.
<!-- tarav.breadcrumb 615c8a733f678183d2706134c836609a4bdd316ac67d609cff8ca2ab37639b8a -->

## Typed delivery and semantic targets

Links have reading semantics: some are expected to be followed to reach a
block; others offer further explanation if needed. Dependencies also express
delivery requirements, such as content being inlined or at least referenced.
The model needs to distinguish these forms of availability. Exact link and
dependency Types remain to be designed; the discussion establishes the need
for control and expressivity rather than a fixed schema.
<!-- tarav.breadcrumb ffd8b5134f4b84dfd1ab777ec75c384dd1c4ac1976af38652da0aec5ecfa031e -->

Blocks explicitly declare the semantic entities they contain or provide.
Those declarations are claims, not guarantees about their text, and supply
the targets used to communicate dependencies in the SKW graph. Semantic
content is not inferred merely from a heading or from opaque block output.
<!-- tarav.breadcrumb 91136a6421a14129b47dc8f8b2f90c06a07ee03dd9bfa6fd0ee4c8a5dfef04a7 -->
<!-- tarav.breadcrumb dc20ec72bd12907a8c3c5e639e5b6a9c14a8b5a1db18ca6ff5a09709fdfdb0b1 -->

## Declarations are properties of blocks

All these declarations belong to blocks. An ordinary block can declare that
it contains a link of a particular type to entity A, inlines entity Z, and
requires entity B to have been inlined for its reading. Specialized blocks
such as links or literal inlines are useful implementations, but embedded
links do not each need to become separate blocks. The reading-path mechanics
consume the declarations uniformly without interpreting the prose.
<!-- tarav.breadcrumb 102c4fef933e33bde1813fe777152edf81a5fc067bc9996a0c97c7e96372b475 -->
<!-- tarav.breadcrumb 15bb276efe4b5d3517684017d9756b3c7911852403e79e9fc375fe5b8295fda1 -->

## Structural checking boundary

The immediate work is reading-path mechanics and their structural checks:
does a declared path supply the required semantic entity in the required
form? They take content declarations as given. Assessing whether actual text
substantiates those claims belongs to separate semantic checks and scoring,
to be developed later. A successful structural check certifies connectivity
of the declarations, not the truth of their semantic claims.
<!-- tarav.breadcrumb 34dbcff63198cfd9675c93e0977587350c9047daa38406741a55742ff62792c9 -->

## Entity identity and subtype semantics

Reading targets require only `TaravEntity`; no reading-specific
`SemanticEntity` type is needed. Content and entities can belong to other
workflows. The reading-path system concerns itself with their declared
presence and availability; it neither collects nor renders that content.
This refines the earlier illustrative code, which introduced a separate
semantic-entity type.
<!-- tarav.breadcrumb b5cbb95595d14571bca64824ac67d78253f53f161ae9767fb8d0ee7a8068b77c -->

Blocks themselves are TaravEntities. Their `id` values must be UUIDs, with
separate free-text `label` values for readable presentation. The earlier
example `id="scope"` conflated those roles and is not the intended identity
contract. These are design requirements, not a claim that existing SKW
blocks have already been migrated.
<!-- tarav.breadcrumb 43206f78d3ec6e0246bb1495ed0e60fa3ae1e574cbcf237fca5030581fb07715 -->

Prefer a base type plus semantic subtypes over a general type with mode
strings for reading relationships. The Type Graph participates in the
Diagram, so explicit subtypes make the meaning and available kinds of
relationships more discoverable. This is a general modeling preference;
the precise subtype set and names remain to be designed. It refines the
earlier illustrative `ReadingLink(..., mode="consult")` shape without
changing the uniform block-declaration model.
<!-- tarav.breadcrumb 5e002c69d5d2ea0299c90fe0ee0ff565bfd53328bc43515e6550f8fb30f20dc9 -->
