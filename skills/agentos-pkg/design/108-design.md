> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Skw.Address.Schema

- [DF] `Skw.Address.Schema` is the accepted syntax set for naming any addressable entity of the workspace — concept blocks, files, regions, spans, chat moments ^20260712-0 ^20260712-10
- [DF] one grammar underlies every form: a name is a root plus an optional region path ^20260712-0
- [DF] a name traverses three spaces: ontology space (concepts), file space (surfaces and their spans), and chat space (registered moments) ^20260712-0 ^20260712-10
- [DC] legal forms: `Dotted.Name` (compact symbolic), `Block.Path` (ontology topology), `Locator.Name` (`@`-anchored file, region, or span address), `Anchory.Anchor` (`^`-registered chat moment) ^20260712-0 ^20260712-10
- [PR] the root concept is the address — `Dotted.Name` exists to make ontology addresses inlinable in natural prose, not the other way around ^20260712-10
- [DF] the full string is the name of the entity at hand — sigils compose names, they are not operations on them ^20260712-0
- [CT] name syntax does not change the named entity's semantics — a block is a block, a span a span, under any legal form ^20260712-0 ^20260712-10
- [CT] a legal name carries at least one sigil; a single bare word is not a name ^20260712-0
- [PR] sigils keep names distinguishable from natural prose — inline-always, grep-able (`Name.As.Index`) ^20260712-0
- [PR] choose the form that preserves the entity's natural identity — a native address over an artificial coinage ^20260712-0
- [FR] locator roots follow common sense, often a `<...>` variable — no closed root vocabulary exists ^20260712-2
- [DC] the `@` is agent-maintained: users may omit it, and a bare mention resolves to the locator-named entity when it matches (`Bla/Blo` → `@Bla/Blo`) ^20260712-2
- [DC] friendly alternates live as aliases in `Kernel.Block.Meta`, not as competing names ^20260712-0
- [CT] aliases resolve inbound references only — user input, queries, legacy mentions; a citation written on any stable surface canonicalizes to the block's title name — an alias in a cite fragments the `Name.As.Index` reverse lookup ^20260716-17
- [DC] routing is form-neutral: `000-INDEX.md` routes any legal name ^20260712-0

### meta

- aliases: `Block.Naming.Schema` (the founding, block-scoped name), `Address.Schema`

****

## Addressing.Sigil.Vocabulary

- [DF] `Addressing.Sigil.Vocabulary` is the closed set of primitives a `Skw.Address.Schema` name composes from ^20260712-1 ^20260712-10
- [CT] each sigil carries exactly one meaning; expressivity comes from composition, never from overloading ^20260712-1
- [DF] `.` joins words into one name atom: `Concept.X`, `AGENTS.md` ^20260712-1
- [DF] `/` states descent — the right side lives inside the left side's namespace, in either space ^20260712-1
- [DF] `#` switches space — the name leaves file space and enters the file's internal regions ^20260712-1
- [DF] `::` states type — the right side is an entity of the left side's type: `Line.Type::DF` ^20260712-1
- [DF] `:` states line position inside a file: `@<project>/AGENTS.md:42` ^20260712-1
- [DF] `<...>` marks a variable part, resolved by context and legal in any space: `<project>` ^20260712-1
- [DF] `@` is the locator prefix — it anchors a name in file space from its first character ^20260712-1
- [DF] `^` marks a registered span or moment within a surface — one meaning across spaces, one owning register per space: `Anchory.Anchor` owns chat space (`^20260712-1`, a moment), skw labels own file space (`^archive-filter`, a span) ^20260712-1 ^20260712-10
- [CT] `^` never appears in ontology-space names — a registered mark belongs to a surface, never to a concept ^20260712-10
- [CT] a sigil's meaning is invariant across positions; where it may appear is grammar, not meaning ^20260712-1

### meta

- aliases: `Naming.Sigil.Vocabulary`
