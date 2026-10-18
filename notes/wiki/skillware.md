# Skillware

## Specialized document Types — idea for later design

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

Explore specialized SKW document Types that express the structure of the
document being authored. A skill document is the motivating example: its
description could be a dedicated, separately editable block, with metadata
distinguished from instruction sections. The Type could check the structural
requirements appropriate to that kind of document.
<!-- tarav.breadcrumb e03c125a4aec -->

This is a captured design idea, not an implemented contract. The exact Type
name, required metadata, block Types, and enforcement rules remain open. A
minimal metadata contract with flexible instruction sections was suggested;
it has not been settled as a schema. This concerns SKW modeling, not additional
constitutional requirements.
<!-- tarav.breadcrumb d49d5f0e5c3f -->

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## SKW Code and reader-facing products

`skw.code` is the common workflow for developing instruction surfaces as
typed, inspectable source. It owns neutral documents and blocks, workflow-owned
annotations, reading declarations, and compilation. Specialized workflows such
as `skw.skills` can add conventions and operations without making those
conventions universal.
<!-- tarav.breadcrumb 523d48e8728e -->
<!-- tarav.breadcrumb 23c2754e6eb5 -->

The “code” is developer-side structure, not necessarily what the consuming
agent reads. Compilation or rendering produces an ordinary surface—often plain
instructions or text—and the reader interprets that product. The compiler
concept remains inside `skw.code`; it is not a separate workflow.
<!-- tarav.breadcrumb 4b5e244fe943 -->
<!-- tarav.breadcrumb 23aa1e251759 -->

## Reading graph type family

`ReadingGraph` is the common `skw.code` Type for static analysis of declared
reader routes. `SkillReadingGraph` is its concrete Skill-owned specialization
and retains package binding, rendering, inspection, and path analysis. The
Project-owned `ProjectReadingGraph` is an abstract specialization point; it
does not yet prescribe how AGENTS.md, Tarav context, or project skills declare
an onboarding route.
<!-- tarav.breadcrumb 8de9cbab08cb -->

This is deliberately a graph of probable routes designed by surface authors,
not a runtime trace or constraint on an agent. Agents may navigate elsewhere;
the graph answers whether a declared route supplies the context that its blocks
say a reader needs. See
[Impl.Req 841](../../../../tarav-py/notes/live/841-reading-graph-specializations-impl-req.md)
and the implemented
[`ReadingGraph`](../../../../tarav-py/src/tarav/l1/skw/code/graph.py) family.
<!-- tarav.breadcrumb fba8045d4f03 -->

## Neutral typed block substrate

The implemented SKW document model uses one neutral concrete `SkwBlock`:

```text
SkwBlock
├── id
├── label
├── objects_index     optional locally named typed objects
├── annotations       typed workflow-owned meanings
└── content           retained block content
```

A block's content can be literal, agent-produced, code-produced, or assessed
by another workflow. Generation is therefore a `GenerationAnnotation`, rather
than a separate kind of block. Reading declarations are annotation subtypes as
well. Consumers select only the annotation Types they understand, so several
workflows can act on the same block without sharing one relationship
vocabulary.
<!-- tarav.breadcrumb e195fddade73 -->
<!-- tarav.breadcrumb 312ae6452b9c -->

Every semantic value retained inside the block is typed. `objects_index`
provides optional block-local names for reusable TaravObjects; those names are
not Ships. An annotation may instead inline a typed object directly. A typed
`ObjectIndexReference` resolves a local name against the containing block.
The index owns local storage and addressing, while each annotation owns the
meaning it assigns to an object.
<!-- tarav.breadcrumb 590131fc1138 -->
<!-- tarav.breadcrumb 076fb6c47b9e -->

The SKW generation path gives an agent the complete block. It has no prompt
placeholder language or argument-binding layer. `GenerationAnnotation` declares
ordered instructions and context objects. Instruction freshness and declared
context freshness are independent acceptance scopes.
<!-- tarav.breadcrumb 65a2f59a39ba -->

## Typed SKW depots and skill objects

A skill should have an actionable Python object. The proposed common entry
point is `.skw/main.json`: its registered type identifies the concrete object,
rather than a `skill.json` filename making every SKW depot implicitly a skill.
This updates the earlier skill-specific entry-point proposal; it records the
design direction, not a claim that the migration is implemented.
<!-- tarav.breadcrumb 3b73686a7af7 -->
<!-- tarav.breadcrumb 7cf6862414a4 -->

Loading should unify with ordinary Tarav directory-record loading instead of
maintaining a separate SKW type-dispatch mechanism. The proposed relationship
is `DirectoryRecord → SkwDepot → SkwSkill`; `SkwDepot` is a working name.
The depot represents `.skw/`, while the skill can expose the enclosing
directory as its product root. Ordinary Python subclassing carries the
specialization, and the registered class should own the object's behavior.
<!-- tarav.breadcrumb 7349114e7533 -->
<!-- tarav.breadcrumb 20436c1ee834 -->

The declared type maps to a Python class. Changing that declaration to an
incompatible class may fail because the data does not fit its expectations;
each class owns its due diligence. Loading need not enforce universal semantic
correctness. See [record dispatch and class responsibility](record-framework.md#type-dispatch-and-class-responsibility).
<!-- tarav.breadcrumb d59af4512862 -->

## Selective context expansion

Discussion of the large `skw document context` output established that agents
should select which declared context to expand. Filesystem-like listing,
head/tail previews, and full reads let the agent avoid reloading material
already in its working context. Resolved full paths should be exposed so
ordinary agent tools can inspect the targets as well.
<!-- tarav.breadcrumb 084ddc43696b -->
<!-- tarav.breadcrumb 0bed3f59c3cf -->
<!-- tarav.breadcrumb a9cd2cfdca14 -->

This is an instance of the broader
[agent-directed navigation principle](tarav-harness.md): in contexts where
efficiency matters, Tarav supplies simple navigation primitives and hints
instead of flooding the agent. These are design requirements, not a claim that
the context CLI already implements selective expansion.
<!-- tarav.breadcrumb 9c1482bb38a1 -->

## Generation as source code

Skillware (`skw`) began as a proposed generation programming language:
reusable, composable generation functions interpreted by an agent. The early
model gave a function a name, typed arguments, a body, and context. The current
document model keeps the source-code principle while replacing prompt arguments
with a complete typed block and workflow annotations.
<!-- tarav.breadcrumb a200222d60f7 -->
<!-- tarav.breadcrumb 6d8e72bf7c9d -->

Generation typically produces a surface: a file or file fragment. Any file
can be harnessed in this way; the conceptual relationship is
`src.skw → generation → output`.
<!-- tarav.breadcrumb b71d6af00720 -->

## Context dependencies and output assertions

Two distinct obligations surround generation:

- Generation dependencies declare what must be available in the generator
  agent's context at generation time.
- Output assertions declare what the produced surface must satisfy, evaluated
  through checks or Tarav's scoring system.
<!-- tarav.breadcrumb afe13f955077 -->
<!-- tarav.breadcrumb 8bf3d0a4d38b -->

Context connects Skillware to Tarav's contextualization workflows. Skillware
can declare how to obtain context through those workflows; more generally,
context acquisition can itself be expressed as another prompt.
<!-- tarav.breadcrumb 3f987c80483b -->

What a function declares it needs is distinct from what a particular
invocation received. Tracking the producing chat can supply evidence for
later audits of whether the required context was present.
<!-- tarav.breadcrumb 43520086ee37 -->

## Tracked outputs and reasoned POIs

Generated outputs can be tracked and become dependencies of other
generations. Changes can raise POIs for review of the dependency tree.
Adding a context requirement can likewise invalidate an output's previous
standing and prompt review or regeneration.
<!-- tarav.breadcrumb 93ff65c5feba -->
<!-- tarav.breadcrumb 331c34f1b4d8 -->

Invalidation surfaces evidence rather than adjudicating the output. A POI
may report that generation context dependencies changed; this does not prove
that the generated content is wrong. POIs carry the reasons the harness
raised them.
<!-- tarav.breadcrumb 2bf03879797b -->

## Independent MVP and overlapping workflows

The early MVP was designed to remain mostly independent of the old
Index/Diagram integration and initially omit Tarav contextualization
integration. It proposed generation-block dependencies, typed prompt arguments,
and basic linting. The neutral block substrate above supersedes its block and
argument model while preserving that workflow independence.
<!-- tarav.breadcrumb 12df00fd81ff -->

A reference-based annotation workflow can independently connect existing
fragments in a dependency graph, while Skillware owns template and expansion
semantics. Similar capabilities do not require one universal dependency
framework. Duplicated mechanics are acceptable initially; common mechanics
can be extracted and migrated explicitly after practical use demonstrates
what is shared.
<!-- tarav.breadcrumb 6d99d49160d6 -->
<!-- tarav.breadcrumb 71e1c4e9b985 -->
<!-- tarav.breadcrumb 3c55894ce483 -->

## Document source, derived product, and annotations

The later document-source design makes the recipe a typed Tarav Record and
the generation event a separate typed annotation owned by Tarav/Skillware.
The product remains an output artifact. Generation sources and bookkeeping
belong under the project's `.skw/` by default, leaving the product surface
uncluttered; colocating them with products remains possible.
<!-- tarav.breadcrumb 42dc5aa68c03 -->
<!-- tarav.breadcrumb e7573bb8c49a -->
<!-- tarav.breadcrumb b2a62735017e -->

Sources are named for their output by default: `explanation.skw.json` contains
everything that generates `explanation.md`. The implementation manages whole
documents, not partially adopted fragments. All ordinary content uses neutral
`SkwBlock` Records; a `GenerationAnnotation` declares when an agent-generation
workflow participates.
<!-- tarav.breadcrumb 4c2ba12c15ee -->
<!-- tarav.breadcrumb 43f4b1e80389 -->

Generated block content lives inside `explanation.skw.json` too. Generation
fills or revises a block's `content`; the compiler produces the entire
`explanation.md` from that source. The product is fully derived.
Compilation is deterministic assembly of literals and retained generated
content, with checks. A linter evaluates the `.skw.json` source.
<!-- tarav.breadcrumb 67a801d6495f -->
<!-- tarav.breadcrumb 47bab5d97e65 -->

A lock tracks recipe and output versions to detect stale editions.
Generation annotations and the lock track provenance and staleness around
the source. Exact schemas and lock-update mechanics remain to be specified.
<!-- tarav.breadcrumb 61b8fdb8a1f2 -->
<!-- tarav.breadcrumb 46bda22671cf -->

CLI operations replace preparation scripts and expose the typed block's
instructions and selected context directly to an agent. These transient
interfaces do not require extra files in the product surface.
<!-- tarav.breadcrumb 3f626c97b4cb -->
<!-- tarav.breadcrumb edcf67f9bd6d -->

JSON and JSONL were considered for source representation. Text can be stored
as vectors of lines in either format; escaped multiline strings are not
required. A first configuration record was acceptable for the JSONL option,
but append-heavy use was not assumed. The subsequent design discussion uses
`.skw.json`; detailed serialization and newline conventions are not settled.
<!-- tarav.breadcrumb 023055ac8bdf -->
<!-- tarav.breadcrumb d49d9bad1a8b -->
<!-- tarav.breadcrumb 634acc825133 -->
<!-- tarav.breadcrumb 7fa6d0235f1a -->

## Edit, lint, compile

Skillware is the source code of generation. Agents see both the instructions
and the current generated content in the source, so existing output becomes
context for revision. Work reduces to editing generation source and running
lint/compile, following a software-like feedback loop.
<!-- tarav.breadcrumb d2f5e459d447 -->
<!-- tarav.breadcrumb 56c60600e0ad -->

Implementation independence does not isolate Skillware from Tarav: the
generation source is a Tarav Record and can participate in semantic assertion
scoring and other Tarav capabilities. This provides a connection without
requiring contextualization integration in the initial MVP.
<!-- tarav.breadcrumb f4f68522fc2b -->
<!-- tarav.breadcrumb 3b9fd77ee741 -->

## Computing with agents

Skillware gives a concrete purpose to
[minimizing uncontrolled agent-generated data](agent-generated-data.md): when
generation is necessary, make it an identifiable, assessable activity.
Defined rules guide generation, and checks or scoring assess compliance.
The ambition is to make computing with agents scale through reusable
structure and tooling, as software does.
<!-- tarav.breadcrumb 80a168489eaf -->
<!-- tarav.breadcrumb 161b319167bc -->

An unassessed generated claim is not necessarily false or useless, but its
reliability is unknown. The measurement-without-uncertainty analogy motivates
surrounding generation with a mechanically tracked structure, deterministic
checks, scored assertions, and audits. These extend the
[Tarav harness](tarav-harness.md) progressively: the examples illustrate
capabilities to develop and learn from, rather than a requirement to build
every mechanism at once.
<!-- tarav.breadcrumb 4b246721ed30 -->
<!-- tarav.breadcrumb 5d9f1459acee -->

## Skill packages as a specialization of SKW

The proposed `tarav.skw.skills` workflow specializes SKW for skill surfaces:
maintained sources, explicit dependencies, reproducible products, deployable
primitives, and associated tooling and specialized checks. Skills are one
application of SKW. General SKW should not need to understand skill layouts
or consumer-context rules. This is a design direction, not a claim that this
specialization has already been implemented.
<!-- tarav.breadcrumb 0c0116e5906a -->
<!-- tarav.breadcrumb 038c173b221b -->

### Developer and consumer dependencies

Developer context dependencies and consumer context dependencies are distinct.
Development can reference Diagram.Model, code, evidence, and other maintenance
context. A developer-only reference can require the maintaining agent or SKW
tooling to call Diagram; consumers should not need those calls by default.
<!-- tarav.breadcrumb a51de2ab89d9 -->
<!-- tarav.breadcrumb e8c7d0a52d42 -->

By default, consumer context is available in skill form: bundled content or,
preferably, references to other skills. Self-sufficiency does not mean loading
all content at once. Routers and indexes support selective discovery and
reading. Explicit code-based dependency tracking makes these development and
consumption networks maintainable.
<!-- tarav.breadcrumb 644dc1f25d6c -->
<!-- tarav.breadcrumb 51204ce80a1a -->

### Md.Model as compiled model content

The discussion began by revisiting the old Index's named blocks, attached
content, and Kernel writing as a convenient Markdown documentation surface
for skill dependencies. It then established the flow
`Diagram.Model → Md.Model → Other.Surfaces`.
<!-- tarav.breadcrumb 905a1d4bc1d6 -->
<!-- tarav.breadcrumb 147a690363af -->

Md.Model is not a modeling or additional generation surface. It deploys the
Diagram.Model data needed by skills. Modeling and changes happen in
Diagram.Model; deployment reproduces the Markdown. This corrects the earlier
suggestion of independently authored Markdown models for this workflow.
<!-- tarav.breadcrumb a340f04efd2e -->
<!-- tarav.breadcrumb d1a08a46b821 -->

Compiled Markdown also serves findability, including when Diagram is
available. The dependency split lets consumer-facing skills expose model
content without requiring Diagram calls by default, while maintainers retain
their development dependencies on Diagram.
<!-- tarav.breadcrumb 6d760b0c99f9 -->
<!-- tarav.breadcrumb 9b88156a868a -->
<!-- tarav.breadcrumb d87361af1a65 -->

## Static consumer-context contracts for SKW Skills

The published `[PR]` notation exposed a consumer-context problem: a reader
needs the relevant context to interpret the surface. This motivates modeling
declared and reachable consumer context, analogous to checking whether a
software dependency is in scope.
<!-- tarav.breadcrumb aad1d7019b0f -->
<!-- tarav.breadcrumb d442151b5530 -->

This is static analysis of declared loading paths, not tracking an actual
agent run. It belongs to `skw.skills`, whose surfaces instruct agents, rather
than to every general SKW-annotated surface. Each consumer block should belong
to at least one loading path.
<!-- tarav.breadcrumb b862414026c5 -->
<!-- tarav.breadcrumb 266f28ccf5f7 -->

Build dependencies ask whether something the skill was developed from has
changed. Consumer-context analysis asks whether each declared loading path
supplies what its instructions require. These are complementary checks.
<!-- tarav.breadcrumb 2ac4800a23eb -->

### Blocks, delivery requirements, and loading structure

The identities in this mechanism are SKW blocks, not Index or Diagram.Model
blocks. Loading a block adds that block to simulated context. Code does not
model what an agent learns or infer meanings supplied by the block; that is
the agent's job. The earlier proposed semantic `provides` vocabulary is not
part of this design.
<!-- tarav.breadcrumb da649a84f8f9 -->
<!-- tarav.breadcrumb 47f39cac2f38 -->

A block declares what its loading paths must supply, independently of who
uses the block. A requirement can request a reference, inlined content, or
leave the delivery form unspecified. A reachable reference can therefore
satisfy a requirement when that delivery form is allowed; not every
requirement demands previously inlined content.
<!-- tarav.breadcrumb 5fe5e4652004 -->

Blocks explicitly declare outward links and inline inclusions. A skill
reference is an annotated and generated `skw.skills` primitive. Loading paths
are built by attaching blocks to parent blocks; the default parent is the
predecessor in the file. Paths within a skill share an entry root, defaulting
to `SKILL.md`. These declarations live as Tarav-compatible Records in `.skw/`.
External systems can integrate with this structure, but SKW owns its mechanics.
<!-- tarav.breadcrumb 693aa268c1c0 -->

### Declared graph and conformance checks

Dependency and loading mechanics operate on declared annotation data.
Compilation generates references from those declarations. Primitive-specific
checks may parse output to check conformance, but output scraping does not
establish or reconstruct the dependency and loading graph.
<!-- tarav.breadcrumb 39fc3e89fe1a -->

The intended checks surface unreachable blocks, missing required context on a
loading path, and path-dependent coverage where only some incoming paths
satisfy the requirements. These are design requirements, not a claim that the
current package file-link checker implements this static loading model.
<!-- tarav.breadcrumb e60c2ed8681d -->

### Links are declared; a prose part checks the text (904)

On 2026-10-14 the User settled how a link relates to the text of its block.
A block declares that it holds a link; the SKW system trusts the declaration
and does not read the prose. The maintainers care that the text really holds
the link, and that is the concern of the link's own Type: a link Type can
carry checks that read the prose and raise POIs, while the base checks
nothing.
<!-- tarav.breadcrumb ea58dff47f2e -->

This is one case of a wider rule: relations between blocks are declared, the
system checks that the declarations fit together, and other mechanisms may
later check or score the declarations against the text.
<!-- tarav.breadcrumb 38e991854d46 -->
<!-- tarav.breadcrumb c327258f0f09 -->

So a declaration no longer generates its link: the earlier `{{skw:link-N}}`
slot and the parsing of every block for undeclared links were removed. The
prose part is composed into the link rather than being a subtype of it, so
how a link is read and how it is written stay separate. `SkillLink`, a
block whose purpose is to be a link, stays as it is: blocks inside blocks
are another way to build output and remain undecided.
<!-- tarav.breadcrumb b3546af0a791 -->
<!-- tarav.breadcrumb bd1423ab1274 -->

Implemented by [request 904](../../../tarav-py/notes/live/904-a-link-is-declared-its-type-checks-the-prose-impl-req.md):
[`MarkdownProse`](../../../tarav-py/src/tarav/l1/skw/code/reading.py) checks
that the text holds a Markdown link to the declared target, and the check
`Tarav.SKW.Check.LinkProse` raises `Tarav.SKW.POI.MissingMarkdownLink`. The
65 slots of `tarav-hugentics` and `tarav-pkg` became literal links; every
compiled file stayed the same.

### Context.Path as the predictable loading contract

The Skill `Context.Path` is the ordered physical loading contract presented to
an agent: Skill description → `SKILL.md` → other selected skill surfaces. SKW
can construct these paths because skill loading is deliberately predictable.
The current scope is static analysis that a skill developer runs; it does not
attempt to record or validate the path selected during a particular agent
invocation.
<!-- tarav.breadcrumb 3667d9754eeb -->
<!-- tarav.breadcrumb 08f73507b74c -->

Each block declares the context required for correct interpretation. The
checker asks whether every declared path reaching that block already contains
the required material. A block may consequently use compact wording that
assumes an earlier contract, allowing skills to optimize their consumer
context without duplicating the contract in every child surface.
<!-- tarav.breadcrumb 9ce7dcf988fe -->

## Typed surface components and retained output

The next design direction makes `.skw.json` documents collections of explicitly
typed blocks. `SkwBlock` should be a minimal base, with every concrete block a
subtype loaded through registered types rather than one hardcoded block class.
The suggested common data is `id` and `output`; specialized fields and behavior
belong to subtypes. This is intended architecture, not a claim that the current
literal/generation representation already supports arbitrary block types.
<!-- tarav.breadcrumb 38ac95003813 -->

`output` is the default field retaining the block's current output in the
`.skw.json` source. It is not merely an output-producing method: the source
contains the produced content. The discussion considered `return` and retained
the name `output`. Production may be agentic or code-based, but that distinction
does not remove the retained output from the source.
<!-- tarav.breadcrumb c6b2f50e44be -->
<!-- tarav.breadcrumb 0b8760962e9a -->

### Built-in skill surfaces and external styles

General SKW models production of arbitrary surfaces, not only executable or
agent-consumed instructions. Skill development is a built-in specialization at
`tarav.l<X>.skw.skills`. Batchy is a style/application of that specialization,
proposed at `tarav.l<X>.batchy_skills`, not nested under `skw.skills`.
The conceptual specialization SKW → skills → Batchy does not require matching
Python package nesting. Exact layers and workflow-parent declarations remain
implementation decisions. See [Batchy skills](batchy-skills.md).
<!-- tarav.breadcrumb 5db3458984f8 -->

`SkillLink` is a proposed typed skill block whose purpose is to direct the
consuming agent toward a target. It belongs in the skill specialization for now,
not the general SKW engine. Such consumer-facing components are distinct from
internal generation-context or dependency references. They package useful
authoring patterns rather than redefine SKW's underlying mechanics.
<!-- tarav.breadcrumb 7892669286bf -->

A SkillLink can use code and a shared template to produce homogeneous output;
it need not be agent-generated prose. Typed components give these production
mechanics a concrete home while retaining their output in the source. The
discussion establishes the direction, not a finalized field schema or template.
<!-- tarav.breadcrumb 81b1d37647d2 -->
<!-- tarav.breadcrumb c793380bcad7 -->

### Typed block implementation (825)

The user invoked Execute for [825](../../../tarav-py/notes/live/825-typed-skw-components-impl-req.md).
[SKW Document](../../../tarav-py/src/tarav/l1/skw/document.py) now loads each
nested block through the trusted Type registry and requires a `SkwBlock` subtype.
At that checkpoint, literal and agent-generation blocks had concrete Types;
each retained `id` and current `output` in its source Record. Explicit
`produce` updated retained output, while compile assembled it without running a producer. The skill-owned
[SkillLink](../../../tarav-py/src/tarav/l1/skw/skills.py) declares one target,
produces its escaped relative Markdown link, and reports stale output when that
declaration changes. [Loading](../../../tarav-py/src/tarav/l1/skw/loading.py)
places the retained link inline and counts its declared target as referenced
context. One Hugentics link uses this path. The 36 maintained skill documents
were migrated; builds reproduced all their Markdown without text drift.
Existing generation and context history was not rebased. The full product suite
passed 1,381 tests, including trusted external subtype dispatch and the typed
link behavior. Implementation 836 later replaced that block taxonomy and
`output` field with the neutral typed block substrate documented above;
`SkillLink` remains a genuine specialized block subtype.
<!-- tarav.breadcrumb 97dcd940ff0d -->
