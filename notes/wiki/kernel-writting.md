# Kernel.Writing

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Purpose

Kernel.Writing is a discipline for expressing a topic through distinct,
focused statements. A block concerns one topic; each line contributes one
dimension of that topic. Lines aim for minimal overlap and independent
revision. The purpose is useful conceptual structure, not merely turning
paragraphs into bullets.
<!-- tarav.breadcrumb a6f93a4fd9781f9107d683b7fecc192f51d30a46ade677d6b0befcc08a5abf34 -->

For now, this discipline belongs in documentation and, potentially, skill
instructions guiding capture and generation. It is not an enforced contract
of the Lines classes. Code may later expose this documentation through object
context; implementing that connection is deferred.
<!-- tarav.breadcrumb fb3aaa90e144b565b427a6ed6c8d1a45b67fcb217b7f0a0ebd7e21ad3bc7f406 -->

## The writing units

The accepted primitive design separates two objects: a `Line(TaravEntity)`
is an identifiable statement; a `Block(TaravEntity)` is an identifiable,
named topic with an ordered collection of Lines. A line expresses one
contribution but need not be understandable without context. Block membership
supplies context without requiring a Model. These are design intentions,
not a claim that the stale implementation has already been rebuilt.
<!-- tarav.breadcrumb c4a56196af97a3b636fcf5ef71cbceee0165064628db375b305ad9eb7d6c84fb -->

Grounding, approval, editions, scoring, and a particular storage backend are
not prerequisites of those base types. Specialized types and integrations
can add them. Models are applications of Lines, not the foundation on which
Lines must depend; revisiting Models is separate work.
<!-- tarav.breadcrumb c06a0d5f93659322a5f02d86390d6324689a58f382ae6dfa3d617c9609fe753e -->
<!-- tarav.breadcrumb 65ed7ae121a9439607f35888af69b6537f60e9cd0f723462e0452db230f944de -->

## Atomicity and orthogonality

“Atomic” is a writing aim: one line carries one useful contribution at the
chosen level of discussion. “Orthogonal” means sibling lines contribute
distinct dimensions with little redundancy. Together they make it easier
to reconsider one statement without unnecessarily rewriting the others.
Independence is an aim, not a guarantee that changing one line cannot affect
the meaning or consistency of its neighbors.
<!-- tarav.breadcrumb 0465b30916bdad56c30add6d6e61d1130ca2054b78cfc9e7010822534a424b11 -->

Context dependence is compatible with this discipline. A line may rely on
the topic named by its block or on previously introduced concepts. Repeating
all that context on every line is not required. The accepted base design
explicitly allows statements that are not self-contained.
<!-- tarav.breadcrumb 09fd4b5cd63633dff17343bdedd7d882ec261acd2dd0589e56b6c704b8cc8e98 -->

### Practical guidance

The following is an editorial elaboration of the discipline, informed by the
historical Kernel.Writing definition and examples listed below, rather than
an additional schema or approved interface:

- Name the topic before organizing its statements. A heading should help the
  reader understand the subject, not merely decorate the page.
- Separate independently useful claims. Do not put unrelated decisions in
  one bullet just because they arose in one sentence.
- Keep conditions with the claims they qualify. Splitting “only when X” away
  can change the meaning rather than improve atomicity.
- Prefer direct language, but retain distinctions needed for sound judgment.
  Shortness is not a substitute for coverage.
- Remove redundant reformulations, not useful boundaries or exceptions.
- Treat definitions, constraints, choices, examples and uncertainties as
  different contributions; do not force them into a fixed mandatory template.
- Use additional explanation where needed. A compact core need not carry
  every example, argument or rejected alternative inline.

### Example: separating contributions

Illustrative authoring example, not a specification of an existing API:

```md
## CheckResult

- A CheckResult describes one execution of a Check.
- A CheckResult can provide POI instances for investigation.
- Inspecting a CheckResult does not itself raise its POIs.
```

Each statement answers a different question: what the object represents,
what it provides, and what inspection does not do. They share a topic without
requiring one compound sentence. Compare a welded version:

```md
- A CheckResult describes a check execution and provides POIs, which agents
  can inspect without raising them, making targeted investigations easier.
```

The second version joins representation, capability, behavior and rationale.
It is not intrinsically wrong prose, but is less convenient when those
dimensions need separate discussion or revision. Conversely, breaking a
single conditional rule into disconnected fragments would make it worse.

## Capture and generation practice

Kernel.Writing primarily guides the process producing the statements:
choosing the topic, separating contributions and reducing unnecessary
coupling before or during generation. Its present realization is guidance,
not a parser deciding whether text is sufficiently atomic or a constructor
rejecting imperfect statements.
<!-- tarav.breadcrumb a541d5ea264daf252819254326b3c6c207ff1d53c675b5ea44f4250cdfd29c10 -->

An author can use this lightweight sequence as a practical aid:

1. Read the material in its context and identify the topic being captured.
2. Draft the distinct contributions, preserving qualifications and uncertainty.
3. Split welded claims and remove repetition without losing useful dimensions.
4. Read the block together: check whether its lines still express the intended
   account and whether shared context is clear.
5. Preserve relevant evidence through the chosen capture workflow; the writing
   style itself does not establish support or truth.

This sequence is suggested practice, not a new compulsory Tarav workflow.
The older discipline also emphasized capture before polish and coverage over
compression; those historical ideas explain why neat formatting should not
become a prerequisite for retaining useful material.

## Relationship to SKW skills

The discussion returned to Kernel.Writing while considering the semantic
entities that `skw.skills` can use, and identified Lines as the existing
workflow to revisit. The desired foundation is reusable Lines primitives,
not a writing format imposed on every SKW block.
<!-- tarav.breadcrumb 6e4001b56839f21dca7270f545b8e1c8a5f1be9dfa52565c54d415fcc23ca060 -->
<!-- tarav.breadcrumb d023449cc87998bd2f7aad462eeb21f44ba80bfc2df25545baefb2c04e6b433f -->

The conceptual separation is useful: a Lines Block organizes statements about
a topic; an SKW block retains/presents output and can declare what entities
that output provides or requires. A future integration could reference a
whole Lines Block or a particular Line. That is a candidate application,
not an implemented binding or a promise that mentioning a topic supplies
every statement about it. See [Reader.Context.Path](reader-context-path.md)
for the declaration-based availability design.

The structural reading checks consume declarations. Whether prose faithfully
expresses a Line, whether Lines overlap, or whether an extraction preserves
the source meaning are different questions. Kernel.Writing currently guides
the author; it does not add those semantic checks to the present reading-path
implementation. The shared [Checks workflow](checks-workflow.md) can support
such work later without making it a prerequisite of the base objects.

## Historical lineage and present scope

The Attic investigation found the earlier discipline in Deposit
`e1636df6-0910-40eb-bd64-0aee93b06db2`,
`20260826T213706Z-tarav-skills-reboot`. Relevant historical locations within
`material/skills/tarav-pkg/` are:

- `design/102-design.md`: Kernel.Writing, Kernel.Block and its sections.
- `appendix/Kernel.Writing-appendix.md`: writing versus organization.
- `references/index-block-catalog.md`: atomic-line examples and failure modes.
- `design/107-design.md`, Index.Line: block-supplied context and semantic
  orthogonality without requiring standalone completeness.

These are recovery pointers, not runtime dependencies or inherited policy.
The old design included Fundamentals, Appendix and Meta sections, along with
index-specific support and review machinery. This note does not reinstate
those structures. The present decision is narrower: document the writing
discipline and rebuild a minimal Lines base independently of Models.
<!-- tarav.breadcrumb a9edde538da0b3a0674ec66a08e1ac82117f600a4a63dc7e1d6a859577474ba5 -->
<!-- tarav.breadcrumb b990cd01efd39a91fc653e8b35397cc19e5d20a862d0a4dbe1dab26c0af8fa94 -->
