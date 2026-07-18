> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Skw.Address.Schema

- [DF] `Skw.Address.Schema` is the accepted syntax set for naming any addressable entity of the workspace — concept blocks, files, regions, spans, chat moments ^c20260712-0u ^c20260712-10u
- [DF] one grammar underlies every form: a name is a root plus an optional region path ^c20260712-0u
- [DF] a name traverses three spaces: ontology space (concepts), file space (surfaces and their spans), and chat space (registered moments) ^c20260712-0u ^c20260712-10u
- [DC] legal forms: `Dotted.Name` (compact symbolic), `Block.Path` (ontology topology), `Locator.Name` (`@`-anchored file, region, or span address), `Anchory.Anchor` (`^`-registered chat moment) ^c20260712-0u ^c20260712-10u
- [PR] the root concept is the address — `Dotted.Name` exists to make ontology addresses inlinable in natural prose, not the other way around ^c20260712-10u
- [DF] the full string is the name of the entity at hand — sigils compose names, they are not operations on them ^c20260712-0u
- [CT] name syntax does not change the named entity's semantics — a block is a block, a span a span, under any legal form ^c20260712-0u ^c20260712-10u
- [CT] a legal name carries at least one sigil; a single bare word is not a name ^c20260712-0u
- [PR] sigils keep names distinguishable from natural prose — inline-always, grep-able (`Name.As.Index`) ^c20260712-0u
- [PR] choose the form that preserves the entity's natural identity — a native address over an artificial coinage ^c20260712-0u
- [FR] locator roots follow common sense, often a `<...>` variable — no closed root vocabulary exists ^c20260712-2u
- [DC] the `@` is agent-maintained: users may omit it, and a bare mention resolves to the locator-named entity when it matches (`Bla/Blo` → `@Bla/Blo`) ^c20260712-2u
- [DC] friendly alternates live as aliases in `Kernel.Block.Meta`, not as competing names ^c20260712-0u
- [CT] aliases resolve inbound references only — user input, queries, legacy mentions; a citation written on any stable surface canonicalizes to the block's title name — an alias in a cite fragments the `Name.As.Index` reverse lookup ^c20260716-17u
- [DC] routing is form-neutral: `000-INDEX.md` routes any legal name ^c20260712-0u

### meta

- aliases: `Block.Naming.Schema` (the founding, block-scoped name), `Address.Schema`

****

## Addressing.Sigil.Vocabulary

- [DF] `Addressing.Sigil.Vocabulary` is the closed set of primitives a `Skw.Address.Schema` name composes from ^c20260712-1u ^c20260712-10u
- [CT] each sigil carries exactly one meaning; expressivity comes from composition, never from overloading ^c20260712-1u
- [DF] `.` joins words into one name atom: `Concept.X`, `AGENTS.md` ^c20260712-1u
- [DF] `/` states descent — the right side lives inside the left side's namespace, in either space ^c20260712-1u
- [DF] `#` switches space — the name leaves file space and enters the file's internal regions ^c20260712-1u
- [DF] `::` states type — the right side is an entity of the left side's type: `Line.Type::DF` ^c20260712-1u
- [DF] `:` states line position inside a file: `@<project>/AGENTS.md:42` ^c20260712-1u
- [DF] `<...>` marks a variable part, resolved by context and legal in any space: `<project>` ^c20260712-1u
- [DF] `@` is the locator prefix — it anchors a name in file space from its first character ^c20260712-1u
- [DF] `^` marks a registered span or moment within a surface — one meaning across spaces, one owning register per space: `Anchory.Anchor` owns chat space (`^c20260712-1u`, a moment), skw labels own file space (`^archive-filter`, a span) ^c20260712-1u ^c20260712-10u
- [CT] `^` never appears in ontology-space names — a registered mark belongs to a surface, never to a concept ^c20260712-10u
- [CT] a sigil's meaning is invariant across positions; where it may appear is grammar, not meaning ^c20260712-1u

### meta

- aliases: `Naming.Sigil.Vocabulary`
