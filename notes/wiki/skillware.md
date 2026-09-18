# Skillware

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Selective context expansion

Discussion of the large `skw document context` output established that agents
should select which declared context to expand. Filesystem-like listing,
head/tail previews, and full reads let the agent avoid reloading material
already in its working context. Resolved full paths should be exposed so
ordinary agent tools can inspect the targets as well.
<!-- tarav.context 5626cd5f:e780d142e0d5e700 -->
<!-- tarav.context 5626cd5f:04b91894a22b75d0 -->
<!-- tarav.context 5626cd5f:6be996c821a77156 -->

This is an instance of the broader
[agent-directed navigation principle](tarav-harness.md): in contexts where
efficiency matters, Tarav supplies simple navigation primitives and hints
instead of flooding the agent. These are design requirements, not a claim that
the context CLI already implements selective expansion.
<!-- tarav.context 5626cd5f:1e6e002c3e5aea1d -->

## Generation as source code

Skillware (`skw`) is a proposed generation programming language: reusable,
composable generation functions interpreted by an agent. A function has a
name, arguments that may be typed, a body, and context. Arguments and bodies
can contain arbitrary text. The purpose is to treat generation prompts as
source code and give structured skills and surfaces supporting tooling.
<!-- tarav.context 5626cd5f:7d31ec0b467c5769 -->
<!-- tarav.context 5626cd5f:c9883973bbe5abf7 -->

Generation typically produces a surface: a file or file fragment. Any file
can be harnessed in this way; the conceptual relationship is
`src.skw → generation → output`.
<!-- tarav.context 5626cd5f:ab2f0bce8f08eb6c -->

## Context dependencies and output assertions

Two distinct obligations surround generation:

- Generation dependencies declare what must be available in the generator
  agent's context at generation time.
- Output assertions declare what the produced surface must satisfy, evaluated
  through checks or Tarav's scoring system.
<!-- tarav.context 5626cd5f:5168b60329ac174e -->
<!-- tarav.context 5626cd5f:f94c9f480b948078 -->

Context connects Skillware to Tarav's contextualization workflows. Skillware
can declare how to obtain context through those workflows; more generally,
context acquisition can itself be expressed as another prompt.
<!-- tarav.context 5626cd5f:5168b60329ac174e -->

What a function declares it needs is distinct from what a particular
invocation received. Tracking the producing chat can supply evidence for
later audits of whether the required context was present.
<!-- tarav.context 5626cd5f:5a5f65e3e8d7fb29 -->

## Tracked outputs and reasoned POIs

Generated outputs can be tracked and become dependencies of other
generations. Changes can raise POIs for review of the dependency tree.
Adding a context requirement can likewise invalidate an output's previous
standing and prompt review or regeneration.
<!-- tarav.context 5626cd5f:c9883973bbe5abf7 -->
<!-- tarav.context 5626cd5f:5a5f65e3e8d7fb29 -->

Invalidation surfaces evidence rather than adjudicating the output. A POI
may report that generation context dependencies changed; this does not prove
that the generated content is wrong. POIs carry the reasons the harness
raised them.
<!-- tarav.context 5626cd5f:f78ed16c912e6afc -->

## Independent MVP and overlapping workflows

The MVP should be mostly independent of the old Index/Diagram integration and
initially omit Tarav contextualization integration. Its starting capabilities
are dependencies between generation blocks, typed prompt arguments, and basic
linting.
<!-- tarav.context 5626cd5f:f4e56e7c96aabb37 -->

A reference-based annotation workflow can independently connect existing
fragments in a dependency graph, while Skillware owns template and expansion
semantics. Similar capabilities do not require one universal dependency
framework. Duplicated mechanics are acceptable initially; common mechanics
can be extracted and migrated explicitly after practical use demonstrates
what is shared.
<!-- tarav.context 5626cd5f:95b365a38206c463 -->
<!-- tarav.context 5626cd5f:2a8ea7f7f375f1e5 -->
<!-- tarav.context 5626cd5f:63d3a76df5ff9266 -->

## Document source, derived product, and annotations

The later document-source design makes the recipe a typed Tarav Record and
the generation event a separate typed annotation owned by Tarav/Skillware.
The product remains an output artifact. Generation sources and bookkeeping
belong under the project's `.skw/` by default, leaving the product surface
uncluttered; colocating them with products remains possible.
<!-- tarav.context 5626cd5f:7a43c2aba753e9dd -->
<!-- tarav.context 5626cd5f:61eca9f7618260a1 -->
<!-- tarav.context 5626cd5f:b9d601861ae47370 -->

Sources are named for their output by default: `explanation.skw.json` contains
everything that generates `explanation.md`. The MVP manages whole documents,
not partially adopted fragments. Literal blocks contain constant text copied
into the product; generation blocks contain the parts supplied by an agent.
<!-- tarav.context 5626cd5f:7d88260becf826ad -->
<!-- tarav.context 5626cd5f:27e992ecd3a7deda -->

Generated block content lives inside `explanation.skw.json` too. Generation
fills or revises the generation blocks' output fields; the compiler produces
the entire `explanation.md` from that source. The product is fully derived.
Compilation is deterministic assembly of literals and retained generated
content, with checks. A linter evaluates the `.skw.json` source.
<!-- tarav.context 5626cd5f:4382a3a0bdfde82d -->
<!-- tarav.context 5626cd5f:ae2333b650f32879 -->

A lock tracks recipe and output versions to detect stale editions.
Generation annotations and the lock track provenance and staleness around
the source. Exact schemas and lock-update mechanics remain to be specified.
<!-- tarav.context 5626cd5f:7d88260becf826ad -->
<!-- tarav.context 5626cd5f:ae2333b650f32879 -->

CLI operations can replace preparation scripts and expose an expanded prompt
directly to an agent without materializing `prompt.txt`. These transient
interfaces do not require extra files in the product surface.
<!-- tarav.context 5626cd5f:e7307d37b67aad58 -->
<!-- tarav.context 5626cd5f:3b1b1b8c07f271e4 -->

JSON and JSONL were considered for source representation. Text can be stored
as vectors of lines in either format; escaped multiline strings are not
required. A first configuration record was acceptable for the JSONL option,
but append-heavy use was not assumed. The subsequent design discussion uses
`.skw.json`; detailed serialization and newline conventions are not settled.
<!-- tarav.context 5626cd5f:f09dda8ca904914e -->
<!-- tarav.context 5626cd5f:d2dbeeec681a8f56 -->
<!-- tarav.context 5626cd5f:8300752a7c8ab271 -->
<!-- tarav.context 5626cd5f:4382a3a0bdfde82d -->

## Edit, lint, compile

Skillware is the source code of generation. Agents see both the instructions
and the current generated content in the source, so existing output becomes
context for revision. Work reduces to editing generation source and running
lint/compile, following a software-like feedback loop.
<!-- tarav.context 5626cd5f:ae2333b650f32879 -->
<!-- tarav.context 5626cd5f:1284390f92e1be09 -->

Implementation independence does not isolate Skillware from Tarav: the
generation source is a Tarav Record and can participate in semantic assertion
scoring and other Tarav capabilities. This provides a connection without
requiring contextualization integration in the initial MVP.
<!-- tarav.context 5626cd5f:9b805c7aa7d9d2bb -->
<!-- tarav.context 5626cd5f:f4e56e7c96aabb37 -->

## Computing with agents

Skillware gives a concrete purpose to
[minimizing uncontrolled agent-generated data](agent-generated-data.md): when
generation is necessary, make it an identifiable, assessable activity.
Defined rules guide generation, and checks or scoring assess compliance.
The ambition is to make computing with agents scale through reusable
structure and tooling, as software does.
<!-- tarav.context 5626cd5f:5168b60329ac174e -->
<!-- tarav.context 5626cd5f:f94c9f480b948078 -->

An unassessed generated claim is not necessarily false or useless, but its
reliability is unknown. The measurement-without-uncertainty analogy motivates
surrounding generation with a mechanically tracked structure, deterministic
checks, scored assertions, and audits. These extend the
[Tarav harness](tarav-harness.md) progressively: the examples illustrate
capabilities to develop and learn from, rather than a requirement to build
every mechanism at once.
<!-- tarav.context 5626cd5f:f94c9f480b948078 -->
<!-- tarav.context 5626cd5f:f78ed16c912e6afc -->

## Skill packages as a specialization of SKW

The proposed `tarav.skw.skills` workflow specializes SKW for skill surfaces:
maintained sources, explicit dependencies, reproducible products, deployable
primitives, and associated tooling and specialized checks. Skills are one
application of SKW. General SKW should not need to understand skill layouts
or consumer-context rules. This is a design direction, not a claim that this
specialization has already been implemented.
<!-- tarav.context 5626cd5f:0550e60d142ad855 -->
<!-- tarav.context 5626cd5f:3870d143ee3c2367 -->

### Developer and consumer dependencies

Developer context dependencies and consumer context dependencies are distinct.
Development can reference Diagram.Model, code, evidence, and other maintenance
context. A developer-only reference can require the maintaining agent or SKW
tooling to call Diagram; consumers should not need those calls by default.
<!-- tarav.context 5626cd5f:2f40044eac0b8d15 -->
<!-- tarav.context 5626cd5f:09fb7d69184d2961 -->

By default, consumer context is available in skill form: bundled content or,
preferably, references to other skills. Self-sufficiency does not mean loading
all content at once. Routers and indexes support selective discovery and
reading. Explicit code-based dependency tracking makes these development and
consumption networks maintainable.
<!-- tarav.context 5626cd5f:1abb691107cee248 -->
<!-- tarav.context 5626cd5f:09fb7d69184d2961 -->

### Md.Model as compiled model content

The discussion began by revisiting the old Index's named blocks, attached
content, and Kernel writing as a convenient Markdown documentation surface
for skill dependencies. It then established the flow
`Diagram.Model → Md.Model → Other.Surfaces`.
<!-- tarav.context 5626cd5f:2ab6c03a7cfadb74 -->
<!-- tarav.context 5626cd5f:1ddba3d5fa3db1d9 -->

Md.Model is not a modeling or additional generation surface. It deploys the
Diagram.Model data needed by skills. Modeling and changes happen in
Diagram.Model; deployment reproduces the Markdown. This corrects the earlier
suggestion of independently authored Markdown models for this workflow.
<!-- tarav.context 5626cd5f:a1dfe42c3b2625b1 -->
<!-- tarav.context 5626cd5f:d3e5c74dd2deec92 -->

Compiled Markdown also serves findability, including when Diagram is
available. The dependency split lets consumer-facing skills expose model
content without requiring Diagram calls by default, while maintainers retain
their development dependencies on Diagram.
<!-- tarav.context 5626cd5f:d3e5c74dd2deec92 -->
<!-- tarav.context 5626cd5f:2f40044eac0b8d15 -->
<!-- tarav.context 5626cd5f:1abb691107cee248 -->

## Static consumer-context contracts for SKW Skills

The published `[PR]` notation exposed a consumer-context problem: a reader
needs the relevant context to interpret the surface. This motivates modeling
declared and reachable consumer context, analogous to checking whether a
software dependency is in scope.
<!-- tarav.context 5626cd5f:4c80beadc201cad7 -->
<!-- tarav.context 5626cd5f:89af931a07d1ccc8 -->

This is static analysis of declared loading paths, not tracking an actual
agent run. It belongs to `skw.skills`, whose surfaces instruct agents, rather
than to every general SKW-annotated surface. Each consumer block should belong
to at least one loading path.
<!-- tarav.context 5626cd5f:473671f8ebc102e8 -->
<!-- tarav.context 5626cd5f:118b493148120bd3 -->

Build dependencies ask whether something the skill was developed from has
changed. Consumer-context analysis asks whether each declared loading path
supplies what its instructions require. These are complementary checks.
<!-- tarav.context 5626cd5f:388502eb9f04853d -->

### Blocks, delivery requirements, and loading structure

The identities in this mechanism are SKW blocks, not Index or Diagram.Model
blocks. Loading a block adds that block to simulated context. Code does not
model what an agent learns or infer meanings supplied by the block; that is
the agent's job. The earlier proposed semantic `provides` vocabulary is not
part of this design.
<!-- tarav.context 5626cd5f:4d0ec63225c7ff1a -->
<!-- tarav.context 5626cd5f:cd745282a6894c8a -->

A block declares what its loading paths must supply, independently of who
uses the block. A requirement can request a reference, inlined content, or
leave the delivery form unspecified. A reachable reference can therefore
satisfy a requirement when that delivery form is allowed; not every
requirement demands previously inlined content.
<!-- tarav.context 5626cd5f:eb85b0f1aef3b0e6 -->

Blocks explicitly declare outward links and inline inclusions. A skill
reference is an annotated and generated `skw.skills` primitive. Loading paths
are built by attaching blocks to parent blocks; the default parent is the
predecessor in the file. Paths within a skill share an entry root, defaulting
to `SKILL.md`. These declarations live as Tarav-compatible Records in `.skw/`.
External systems can integrate with this structure, but SKW owns its mechanics.
<!-- tarav.context 5626cd5f:cd745282a6894c8a -->

### Declared graph and conformance checks

Dependency and loading mechanics operate on declared annotation data.
Compilation generates references from those declarations. Primitive-specific
checks may parse output to check conformance, but output scraping does not
establish or reconstruct the dependency and loading graph.
<!-- tarav.context 5626cd5f:8ffda9a413e0538c -->

The intended checks surface unreachable blocks, missing required context on a
loading path, and path-dependent coverage where only some incoming paths
satisfy the requirements. These are design requirements, not a claim that the
current package file-link checker implements this static loading model.
<!-- tarav.context 5626cd5f:493a067c7b062ce8 -->
