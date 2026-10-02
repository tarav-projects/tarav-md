# Skillware
<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

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
<!-- tarav.context 1f561f5d:19bbdfd778ba3641 -->
<!-- tarav.context 1f561f5d:b797b3be7d0a82e5 -->

Every semantic value retained inside the block is typed. `objects_index`
provides optional block-local names for reusable TaravObjects; those names are
not Ships. An annotation may instead inline a typed object directly. A typed
`ObjectIndexReference` resolves a local name against the containing block.
The index owns local storage and addressing, while each annotation owns the
meaning it assigns to an object.
<!-- tarav.context 1f561f5d:b974c6c7f7064562 -->
<!-- tarav.context 1f561f5d:0b1b0473a31afaa7 -->

The SKW generation path gives an agent the complete block. It has no prompt
placeholder language or argument-binding layer. `GenerationAnnotation` declares
ordered instructions and context objects. Instruction freshness and declared
context freshness are independent acceptance scopes.
<!-- tarav.context 1f561f5d:60d4d034d5e0e584 -->

## Typed SKW depots and skill objects

A skill should have an actionable Python object. The proposed common entry
point is `.skw/main.json`: its registered type identifies the concrete object,
rather than a `skill.json` filename making every SKW depot implicitly a skill.
This updates the earlier skill-specific entry-point proposal; it records the
design direction, not a claim that the migration is implemented.
<!-- tarav.breadcrumb 3b73686a7af704c332e56b58f97dc1060900b5548d4383a7b322fb79a701733d -->
<!-- tarav.breadcrumb 7cf6862414a413df329a781fb376b3d2fd37dedf1b420d0c0a6567be61166e3f -->

Loading should unify with ordinary Tarav directory-record loading instead of
maintaining a separate SKW type-dispatch mechanism. The proposed relationship
is `DirectoryRecord → SkwDepot → SkwSkill`; `SkwDepot` is a working name.
The depot represents `.skw/`, while the skill can expose the enclosing
directory as its product root. Ordinary Python subclassing carries the
specialization, and the registered class should own the object's behavior.
<!-- tarav.breadcrumb 7349114e75330fc1639cba720275f63549ea4d1ff732818116911cf64c0209b0 -->
<!-- tarav.breadcrumb 20436c1ee834709603a177a21698febee05bf22e4b96863e98d6a07bc1271bc2 -->

The declared type maps to a Python class. Changing that declaration to an
incompatible class may fail because the data does not fit its expectations;
each class owns its due diligence. Loading need not enforce universal semantic
correctness. See [record dispatch and class responsibility](record-framework.md#type-dispatch-and-class-responsibility).
<!-- tarav.breadcrumb d59af45128624f17fc53ad2cbfb7860fd351994a1b1bdf3209a2b7315d0c0143 -->

## Selective context expansion

Discussion of the large `skw document context` output established that agents
should select which declared context to expand. Filesystem-like listing,
head/tail previews, and full reads let the agent avoid reloading material
already in its working context. Resolved full paths should be exposed so
ordinary agent tools can inspect the targets as well.
<!-- tarav.breadcrumb 084ddc43696b6de9ddd7351f1f523bee91a4dc82fb91f9c13936bc9870f90af5 -->
<!-- tarav.breadcrumb 0bed3f59c3cfd79112a49ecf7ff5a58061e4ca0fea1608700e8041a5f0fa5568 -->
<!-- tarav.breadcrumb a9cd2cfdca142815abc370d6dc3990a191673381c3a2c92802381fdbcf0b3370 -->

This is an instance of the broader
[agent-directed navigation principle](tarav-harness.md): in contexts where
efficiency matters, Tarav supplies simple navigation primitives and hints
instead of flooding the agent. These are design requirements, not a claim that
the context CLI already implements selective expansion.
<!-- tarav.breadcrumb 9c1482bb38a18daafaed951ba766409d6768013daa80f83a5bd40a44726a6a18 -->

## Generation as source code

Skillware (`skw`) is a proposed generation programming language: reusable,
composable generation functions interpreted by an agent. A function has a
name, arguments that may be typed, a body, and context. Arguments and bodies
can contain arbitrary text. The purpose is to treat generation prompts as
source code and give structured skills and surfaces supporting tooling.
<!-- tarav.breadcrumb a200222d60f72ab7748b119d84dbbac2bc4baac37f3a5ebd722a2350b4c12f83 -->
<!-- tarav.breadcrumb 6d8e72bf7c9d2bf42e01c8fe53fb00cd75f5a3a644feeb52fe4fa483bd03bce8 -->

Generation typically produces a surface: a file or file fragment. Any file
can be harnessed in this way; the conceptual relationship is
`src.skw → generation → output`.
<!-- tarav.breadcrumb b71d6af007208c62b39ab6f2468e4b3489d400dfb600be7eb749563c1ac37b1e -->

## Context dependencies and output assertions

Two distinct obligations surround generation:

- Generation dependencies declare what must be available in the generator
  agent's context at generation time.
- Output assertions declare what the produced surface must satisfy, evaluated
  through checks or Tarav's scoring system.
<!-- tarav.breadcrumb afe13f955077425cb1d95c9af7aa9245d32cc5bc199b0df6babb7da2074095cc -->
<!-- tarav.breadcrumb 8bf3d0a4d38b8b6c096accd102f65dac5927efaa728b73a84b2119ff9e991efc -->

Context connects Skillware to Tarav's contextualization workflows. Skillware
can declare how to obtain context through those workflows; more generally,
context acquisition can itself be expressed as another prompt.
<!-- tarav.breadcrumb 3f987c80483b551d2668fd81322a5293cc748d2290ae50c15cd9da5ec449ecb0 -->

What a function declares it needs is distinct from what a particular
invocation received. Tracking the producing chat can supply evidence for
later audits of whether the required context was present.
<!-- tarav.breadcrumb 43520086ee3765c7e5050720e526e0f6fa5253d4f741ed53c8a5a63725dc621f -->

## Tracked outputs and reasoned POIs

Generated outputs can be tracked and become dependencies of other
generations. Changes can raise POIs for review of the dependency tree.
Adding a context requirement can likewise invalidate an output's previous
standing and prompt review or regeneration.
<!-- tarav.breadcrumb 93ff65c5febade907785e0e60a0c0da21214e32d94bcf788d305c3e08a9dac1a -->
<!-- tarav.breadcrumb 331c34f1b4d8821dff56f47d9f12830aaf7c81bb77d4fd8be47359749cc2cbb6 -->

Invalidation surfaces evidence rather than adjudicating the output. A POI
may report that generation context dependencies changed; this does not prove
that the generated content is wrong. POIs carry the reasons the harness
raised them.
<!-- tarav.breadcrumb 2bf03879797bf48b8748095352f2718bea21a2821b654169584f6cb5c2e40644 -->

## Independent MVP and overlapping workflows

The MVP should be mostly independent of the old Index/Diagram integration and
initially omit Tarav contextualization integration. Its starting capabilities
are dependencies between generation blocks, typed prompt arguments, and basic
linting.
<!-- tarav.breadcrumb 12df00fd81ff7c07c745e39e8dca8493c0c319dc2c191e88e6ccbb8eff04c7bf -->

A reference-based annotation workflow can independently connect existing
fragments in a dependency graph, while Skillware owns template and expansion
semantics. Similar capabilities do not require one universal dependency
framework. Duplicated mechanics are acceptable initially; common mechanics
can be extracted and migrated explicitly after practical use demonstrates
what is shared.
<!-- tarav.breadcrumb 6d99d49160d68de9b8da232cf3fe9733f13d3ef5e5630be84990fb6c92e89ee4 -->
<!-- tarav.breadcrumb 71e1c4e9b9858e1832b51e47d949f8a4949ee2501a25536dacf0dc6c6116052e -->
<!-- tarav.breadcrumb 3c55894ce4833637673a1d271c9f0d6e4559bf4d4f8376366644b28a036bf25f -->

## Document source, derived product, and annotations

The later document-source design makes the recipe a typed Tarav Record and
the generation event a separate typed annotation owned by Tarav/Skillware.
The product remains an output artifact. Generation sources and bookkeeping
belong under the project's `.skw/` by default, leaving the product surface
uncluttered; colocating them with products remains possible.
<!-- tarav.breadcrumb 42dc5aa68c03e29e99d41fdea9c3cf0f64f74618e51da9de607bfb868c67133e -->
<!-- tarav.breadcrumb e7573bb8c49afa03d91b6e4583367d8c198d1bd9c25e96bce58b0c492b56f1f0 -->
<!-- tarav.breadcrumb b2a62735017e0fc001e2809cd1db6ecb9bb1d5f2ba5292f18dd49d637a5b9f78 -->

Sources are named for their output by default: `explanation.skw.json` contains
everything that generates `explanation.md`. The MVP manages whole documents,
not partially adopted fragments. Literal blocks contain constant text copied
into the product; generation blocks contain the parts supplied by an agent.
<!-- tarav.breadcrumb 4c2ba12c15ee0c09eb59777d40e26bcc9a3f81c36edf8095e953f01b7d839f2f -->
<!-- tarav.breadcrumb 43f4b1e8038953ee364f879facf3b7698873ef943054f778179fec55c4a50038 -->

Generated block content lives inside `explanation.skw.json` too. Generation
fills or revises the generation blocks' output fields; the compiler produces
the entire `explanation.md` from that source. The product is fully derived.
Compilation is deterministic assembly of literals and retained generated
content, with checks. A linter evaluates the `.skw.json` source.
<!-- tarav.breadcrumb 67a801d6495fc89ea7a846341c9591c6f97e92f47c48dcb3e807696801e13814 -->
<!-- tarav.breadcrumb 47bab5d97e656f217b8b9b3d9a93f762544ab4e0656a47b14a5afdd417031f64 -->

A lock tracks recipe and output versions to detect stale editions.
Generation annotations and the lock track provenance and staleness around
the source. Exact schemas and lock-update mechanics remain to be specified.
<!-- tarav.breadcrumb 61b8fdb8a1f2db82f53e4d1eae113b4bd13b2f2fdc27a8b49f41ee548feeec3b -->
<!-- tarav.breadcrumb 46bda22671cf877c063d7acdbfffbf6e6df9b4b73ca279b66963e5d8954d9666 -->

CLI operations can replace preparation scripts and expose an expanded prompt
directly to an agent without materializing `prompt.txt`. These transient
interfaces do not require extra files in the product surface.
<!-- tarav.breadcrumb 3f626c97b4cbc3437166232eb0770bb66404503fe863d05c13590168973bcd00 -->
<!-- tarav.breadcrumb edcf67f9bd6dc15566b32c21202e0f3cdc60e9cd29d8ae7530c0cf4baff293d0 -->

JSON and JSONL were considered for source representation. Text can be stored
as vectors of lines in either format; escaped multiline strings are not
required. A first configuration record was acceptable for the JSONL option,
but append-heavy use was not assumed. The subsequent design discussion uses
`.skw.json`; detailed serialization and newline conventions are not settled.
<!-- tarav.breadcrumb 023055ac8bdff3c9cc05e66756ff3df9631a7695b156a87fd135fc40aebf7134 -->
<!-- tarav.breadcrumb d49d9bad1a8b3dc70630ba30bbf00121a175d7264c96da8b39107f55c422c3cf -->
<!-- tarav.breadcrumb 634acc825133bd99bea332bbc43752d51f7d79b431e3e578708b7b415d7e533a -->
<!-- tarav.breadcrumb 7fa6d0235f1a9f732287cbde6fb7003cd006be2f0f3961faf9a7d39be1d99328 -->

## Edit, lint, compile

Skillware is the source code of generation. Agents see both the instructions
and the current generated content in the source, so existing output becomes
context for revision. Work reduces to editing generation source and running
lint/compile, following a software-like feedback loop.
<!-- tarav.breadcrumb d2f5e459d447387290a7b000acaa91b398fae5fd271b37ff69c017489efccdca -->
<!-- tarav.breadcrumb 56c60600e0ada76cf0cb4deafd573973463ddcb1b4536c710519276f83d98bb8 -->

Implementation independence does not isolate Skillware from Tarav: the
generation source is a Tarav Record and can participate in semantic assertion
scoring and other Tarav capabilities. This provides a connection without
requiring contextualization integration in the initial MVP.
<!-- tarav.breadcrumb f4f68522fc2b0f03d0484b8da09429987000bbe65481b50f20b300a8400280ec -->
<!-- tarav.breadcrumb 3b9fd77ee7417adf655a3e494159b94a5b28a2db9b71c43779ab16b5b8297ebf -->

## Computing with agents

Skillware gives a concrete purpose to
[minimizing uncontrolled agent-generated data](agent-generated-data.md): when
generation is necessary, make it an identifiable, assessable activity.
Defined rules guide generation, and checks or scoring assess compliance.
The ambition is to make computing with agents scale through reusable
structure and tooling, as software does.
<!-- tarav.breadcrumb 80a168489eaffdfb7c1a85e054232b967da76bdbc08fd807a960ed53093bfe14 -->
<!-- tarav.breadcrumb 161b319167bc06ccab800f65a40397f2ca33c9bafaff72aaa4d5105e87bb38c1 -->

An unassessed generated claim is not necessarily false or useless, but its
reliability is unknown. The measurement-without-uncertainty analogy motivates
surrounding generation with a mechanically tracked structure, deterministic
checks, scored assertions, and audits. These extend the
[Tarav harness](tarav-harness.md) progressively: the examples illustrate
capabilities to develop and learn from, rather than a requirement to build
every mechanism at once.
<!-- tarav.breadcrumb 4b246721ed3078dcce422950ec1d2a413f4034ef2fcc9018a3bb7f5e0837b34c -->
<!-- tarav.breadcrumb 5d9f1459aceecf052f1cca2478728e0cb9a7e6b4a63a9b7707f150b75587840b -->

## Skill packages as a specialization of SKW

The proposed `tarav.skw.skills` workflow specializes SKW for skill surfaces:
maintained sources, explicit dependencies, reproducible products, deployable
primitives, and associated tooling and specialized checks. Skills are one
application of SKW. General SKW should not need to understand skill layouts
or consumer-context rules. This is a design direction, not a claim that this
specialization has already been implemented.
<!-- tarav.breadcrumb 0c0116e5906a10d755e95a63d059ee7c511a5af36e55ad2c06cd7d31ec6db127 -->
<!-- tarav.breadcrumb 038c173b221be390831638f85da3240d20d9c7c7ae345e2bdec0d186a4d24614 -->

### Developer and consumer dependencies

Developer context dependencies and consumer context dependencies are distinct.
Development can reference Diagram.Model, code, evidence, and other maintenance
context. A developer-only reference can require the maintaining agent or SKW
tooling to call Diagram; consumers should not need those calls by default.
<!-- tarav.breadcrumb a51de2ab89d902c1e3cbf0c91beaf175117e26f4a43755ad83e112268769447e -->
<!-- tarav.breadcrumb e8c7d0a52d42b607d218ce7c9638b1b50cbc47b72067f04ec4531d58e377d6c7 -->

By default, consumer context is available in skill form: bundled content or,
preferably, references to other skills. Self-sufficiency does not mean loading
all content at once. Routers and indexes support selective discovery and
reading. Explicit code-based dependency tracking makes these development and
consumption networks maintainable.
<!-- tarav.breadcrumb 644dc1f25d6c44e856d975874603cde716fca24f296837a7ec46e381ff386fef -->
<!-- tarav.breadcrumb 51204ce80a1a5f4b73fa5b9e90d5aebf9088b019d874f1eea6e7dbb7d527b012 -->

### Md.Model as compiled model content

The discussion began by revisiting the old Index's named blocks, attached
content, and Kernel writing as a convenient Markdown documentation surface
for skill dependencies. It then established the flow
`Diagram.Model → Md.Model → Other.Surfaces`.
<!-- tarav.breadcrumb 905a1d4bc1d6ebd752709adc79238a2386ce51c620929e7b9fbeaca97a588ee3 -->
<!-- tarav.breadcrumb 147a690363af92a4c9120b1768603c906f9557ff77111819b15c91ea0fa278bb -->

Md.Model is not a modeling or additional generation surface. It deploys the
Diagram.Model data needed by skills. Modeling and changes happen in
Diagram.Model; deployment reproduces the Markdown. This corrects the earlier
suggestion of independently authored Markdown models for this workflow.
<!-- tarav.breadcrumb a340f04efd2e12fdcb1e91abb38f9da1193b8dbd87fcaced8f1e8b3ba68d32e2 -->
<!-- tarav.breadcrumb d1a08a46b8210c278226222bece1ca87046a16733fdf4751facac06311dcd7a4 -->

Compiled Markdown also serves findability, including when Diagram is
available. The dependency split lets consumer-facing skills expose model
content without requiring Diagram calls by default, while maintainers retain
their development dependencies on Diagram.
<!-- tarav.breadcrumb 6d760b0c99f9019df91f4fdc012d9fe757aa77cbcf45485532ff99c0d6723233 -->
<!-- tarav.breadcrumb 9b88156a868a056ebbc8359cc16e17f980fe48fee3a349806bac258afc141e4f -->
<!-- tarav.breadcrumb d87361af1a659f6fe35e6115bb9f4b99ef1bdf98c413f40953ac3c86627b8726 -->

## Static consumer-context contracts for SKW Skills

The published `[PR]` notation exposed a consumer-context problem: a reader
needs the relevant context to interpret the surface. This motivates modeling
declared and reachable consumer context, analogous to checking whether a
software dependency is in scope.
<!-- tarav.breadcrumb aad1d7019b0fa03e99c6981ad07561ad782f260723ba5885c1d0e4d85b2ffc39 -->
<!-- tarav.breadcrumb d442151b55302ed448de689dcf04cfb00c608f1dd0bb36fb470d503ab706112e -->

This is static analysis of declared loading paths, not tracking an actual
agent run. It belongs to `skw.skills`, whose surfaces instruct agents, rather
than to every general SKW-annotated surface. Each consumer block should belong
to at least one loading path.
<!-- tarav.breadcrumb b862414026c5843f908372748bf4958b19e611a095506efab45102e12de291fa -->
<!-- tarav.breadcrumb 266f28ccf5f7de4a79ad8142492a95539ea8931ef3ffb1c0ec3bca5dad14e144 -->

Build dependencies ask whether something the skill was developed from has
changed. Consumer-context analysis asks whether each declared loading path
supplies what its instructions require. These are complementary checks.
<!-- tarav.breadcrumb 2ac4800a23ebb8464a194c7aca0c53919a3c0693d386012432f728b9275650d8 -->

### Blocks, delivery requirements, and loading structure

The identities in this mechanism are SKW blocks, not Index or Diagram.Model
blocks. Loading a block adds that block to simulated context. Code does not
model what an agent learns or infer meanings supplied by the block; that is
the agent's job. The earlier proposed semantic `provides` vocabulary is not
part of this design.
<!-- tarav.breadcrumb da649a84f8f95bd2e0aab27735c4ab0a87a3aea241ed2028544e880bab422ef8 -->
<!-- tarav.breadcrumb 47f39cac2f38bf19b984a1e51a345e232ace0402c9545b33a1b94451b9e18dd6 -->

A block declares what its loading paths must supply, independently of who
uses the block. A requirement can request a reference, inlined content, or
leave the delivery form unspecified. A reachable reference can therefore
satisfy a requirement when that delivery form is allowed; not every
requirement demands previously inlined content.
<!-- tarav.breadcrumb 5fe5e46520043a608fefefcbb1f139bcc9e567faccdda22d8f9469a4c1f190e3 -->

Blocks explicitly declare outward links and inline inclusions. A skill
reference is an annotated and generated `skw.skills` primitive. Loading paths
are built by attaching blocks to parent blocks; the default parent is the
predecessor in the file. Paths within a skill share an entry root, defaulting
to `SKILL.md`. These declarations live as Tarav-compatible Records in `.skw/`.
External systems can integrate with this structure, but SKW owns its mechanics.
<!-- tarav.breadcrumb 693aa268c1c061e4630fbeff5189514bbe3e4884a68fb9d533acadc677d8c676 -->

### Declared graph and conformance checks

Dependency and loading mechanics operate on declared annotation data.
Compilation generates references from those declarations. Primitive-specific
checks may parse output to check conformance, but output scraping does not
establish or reconstruct the dependency and loading graph.
<!-- tarav.breadcrumb 39fc3e89fe1a36014896592bd25bbd8fac4ea884caa8c53c8f247317a86af508 -->

The intended checks surface unreachable blocks, missing required context on a
loading path, and path-dependent coverage where only some incoming paths
satisfy the requirements. These are design requirements, not a claim that the
current package file-link checker implements this static loading model.
<!-- tarav.breadcrumb e60c2ed8681dd988cc77812d4ee7078cc1630b067b655c4a1e4bea33430f2746 -->

### Context.Path as the predictable loading contract

The Skill `Context.Path` is the ordered physical loading contract presented to
an agent: Skill description → `SKILL.md` → other selected skill surfaces. SKW
can construct these paths because skill loading is deliberately predictable.
The current scope is static analysis that a skill developer runs; it does not
attempt to record or validate the path selected during a particular agent
invocation.
<!-- tarav.breadcrumb 3667d9754eebd4a01a89ec0891239820d57a6ee93f8dd0b08da204868d4f4c1f -->
<!-- tarav.breadcrumb 08f73507b74c26ec36a03e461f6804e7d9f9149ac686a4cb2c04305320a97075 -->

Each block declares the context required for correct interpretation. The
checker asks whether every declared path reaching that block already contains
the required material. A block may consequently use compact wording that
assumes an earlier contract, allowing skills to optimize their consumer
context without duplicating the contract in every child surface.
<!-- tarav.breadcrumb 9ce7dcf988fedf85bcf650484466bf65f0366953f8e65afcc7806afa33de47d5 -->

## Typed surface components and retained output

The next design direction makes `.skw.json` documents collections of explicitly
typed blocks. `SkwBlock` should be a minimal base, with every concrete block a
subtype loaded through registered types rather than one hardcoded block class.
The suggested common data is `id` and `output`; specialized fields and behavior
belong to subtypes. This is intended architecture, not a claim that the current
literal/generation representation already supports arbitrary block types.
<!-- tarav.breadcrumb 38ac9500381331e503817a884aba3b143ac73f171a9fa4f89444c9be6c54eac5 -->

`output` is the default field retaining the block's current output in the
`.skw.json` source. It is not merely an output-producing method: the source
contains the produced content. The discussion considered `return` and retained
the name `output`. Production may be agentic or code-based, but that distinction
does not remove the retained output from the source.
<!-- tarav.breadcrumb c6b2f50e44be6ed0343b1af16da57dd7635039a7f98a8311913d044d8310775c -->
<!-- tarav.breadcrumb 0b8760962e9a72394e8498dbdd62ecc5f233ba171783b2d88ae4c5ea12b67d9f -->

### Built-in skill surfaces and external styles

General SKW models production of arbitrary surfaces, not only executable or
agent-consumed instructions. Skill development is a built-in specialization at
`tarav.l<X>.skw.skills`. Batchy is a style/application of that specialization,
proposed at `tarav.l<X>.batchy_skills`, not nested under `skw.skills`.
The conceptual specialization SKW → skills → Batchy does not require matching
Python package nesting. Exact layers and workflow-parent declarations remain
implementation decisions. See [Batchy skills](batchy-skills.md).
<!-- tarav.breadcrumb 5db3458984f8975a09d75c5ddb330c33f57af5d39e4c114a768f0e2942a6713d -->

`SkillLink` is a proposed typed skill block whose purpose is to direct the
consuming agent toward a target. It belongs in the skill specialization for now,
not the general SKW engine. Such consumer-facing components are distinct from
internal generation-context or dependency references. They package useful
authoring patterns rather than redefine SKW's underlying mechanics.
<!-- tarav.breadcrumb 7892669286bfa709444c75dcb4d7010f926b536ac1f7fca5b283e8958df3f696 -->

A SkillLink can use code and a shared template to produce homogeneous output;
it need not be agent-generated prose. Typed components give these production
mechanics a concrete home while retaining their output in the source. The
discussion establishes the direction, not a finalized field schema or template.
<!-- tarav.breadcrumb 81b1d37647d2bec6110294ddcba21e5ed179493a3f5ab75b4b0e2f3003485e2b -->
<!-- tarav.breadcrumb c793380bcad7edca6231be7220a403e10cbd68ab02a54f397314d315ce6ffeaa -->

### Typed block implementation (825)

The user invoked Execute for [825](../../../tarav-py/notes/live/825-typed-skw-components-impl-req.md).
[SKW Document](../../../tarav-py/src/tarav/l1/skw/document.py) now loads each
nested block through the trusted Type registry and requires a `SkwBlock` subtype.
Literal and agent-generation blocks have concrete Types; each retains `id` and
current `output` in its source Record. Explicit `produce` updates retained
output, while compile assembles it without running a producer. The skill-owned
[SkillLink](../../../tarav-py/src/tarav/l1/skw/skills.py) declares one target,
produces its escaped relative Markdown link, and reports stale output when that
declaration changes. [Loading](../../../tarav-py/src/tarav/l1/skw/loading.py)
places the retained link inline and counts its declared target as referenced
context. One Hugentics link uses this path. The 36 maintained skill documents
were migrated; builds reproduced all their Markdown without text drift.
Existing generation and context history was not rebased. The full product suite
passed 1,381 tests, including trusted external subtype dispatch and the typed
link behavior.
<!-- tarav.breadcrumb 97dcd940ff0d11c69605334367cb3df25172c3196951cbabcdc3c8f6c2eda593 -->
