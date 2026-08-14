# Index.Narrative and line identity - design-req

status: Open

## Session.Abstract

- **target** — decompose the overloaded `Index.Line` concept into the wording it materializes and the semantic object it indexes, and define the identity, support, and gating model for the latter.
- **origin concern** — `The.Renaming.Problem`: a mechanical `Agentos.*` → `Tarav.*` rename breaks every gated line's `Line.Verbatim.Gate`, with no repair path, because gate verification is live containment against an immutable chat transcript.
- **settled frame** — the friction is not in the gate. `Index.Line` has been doing two jobs at once; every symptom is that fusion showing through. Naming the second job (`Index.Narrative`) dissolves the renaming problem as a special case.
- **next useful move** — settle the naming layer questions (`Touched.` vs `Index.` prefix; the general token primitive's namespace), then reconcile the contradicting live `[CT]`s before landing any block.

## Design.Index

### The.Decomposition

- [DF] `Index.Line` currently carries two jobs: the **semantic object** indexing a region of chat history, and the **concrete wording** materialized on a surface
- [DC] the decomposition assigns the wording job to `Index.Line` and the semantic job to `Index.Narrative`
- [DC] `Index.Line` keeps its existing definition — `[DC] Index.Line is its atomic presentation unit` ^c20260729-169u is unambiguously the wording job, so the existing name stays where the existing definition already points
- [PR] every friction in this design traces to the fusion: renaming cannot change wording without breaking identity; the gate protects wording when the object is what matters; citations cite the object and receive the wording; support has no vocabulary to say which job it grounds
- [DC] this is a decomposition of an existing concept, not a new subsystem — the second job was always being done, only implicitly
- [DC] the audit rule for existing text is mechanical: for every live line mentioning `Index.Line`, ask which job it is about

### Index.Narrative

- [DF] `Index.Narrative` is a set of `Index.Line`s that share support — the semantic object an index entry indexes
- [DF] its support is the history in the chat being indexed by the narrative, not an evidence bundle for a claim
- [DC] a line is a **view** of its narrative: one wording, one placement, one `Line.Type`
- [CT] a line may not drift from its narrative; it must be semantically coherent with **all** of the narrative's support
- [DC] a line's support is its narrative's support; there is no separate per-line support
- [PR] indexing the object in parts is what buys the freedom to rename, reword, and relocate while the semantics hold
- [DC] the narrative is the semantic subject of the index; an `Index.Line` is always read in the context of one
- [CT] support is undifferentiated: operational turns (a rename request) and semantic turns (an assertion) are both support, distinguished by reading rather than by structure

### Line.Identity

- [DC] identity is held by the `Anchor.Record`, not by the anchor id, the attachment hash, the content, or the label
- [DC] two identifiers: one UUID for the `Index.Narrative`, one for each `Line.Version`
- [DC] `Anchor.Label` remains the public, mutable surface reference, decoupled from identity
- [PR] an identifier that is also a name eventually blocks renaming — the failure this project already paid for with `agentos.project` and `agentos.agent.usage-record` during the tarav migration
- [DC] UUID collision is negligible, so reusing one is always an intentional act rather than an accident
- [DC] the attachment assertion (today's content hash) remains the surface's honesty check, detecting drift between a surface occurrence and the record
- [CT] once identity detaches from content, the mutation gate is the **replacement** for the constraint content rigidity was providing — anchor-as-identity is only safe to the extent that gate is real
- [DC] the `Anchor.Record` is the manifest of everything indexed by the narrative, including its edition history
- [FR] index anchory is git-tracked, so manual recovery is always available and the model need not defend against data loss

### Semantic.Equivalent.Edition

- [DF] `Semantic.Equivalent.Edition` is the gated mechanism by which a new `Line.Version` joins a narrative under a persisting identity
- [DC] its purpose is to keep the narrative's support attached across a wording change, not primarily to avoid re-approval
- [CT] a new version may only be added with a user turn to link to; agents cannot add a version because they prefer it
- [DC] the user turn may be operational or semantic; both qualify as `Touch.Authority.Surface`
- [PR] the support anchors are therefore the operation log — "whatever support we had before → a rename was requested" — so no separate operation record is needed
- [DC] the narrative reads as a **narrative**: an auditable sequence of touch events, each a real user turn
- [DC] grounding is flat; no version's standing depends on another's, so approximate equivalence never composes into accumulated drift
- [DC] every version remains answerable to the original support, so drift is detectable against the origin rather than merely non-accumulating

### Assertion.Layering

- [CT] the semantic claim ("this mutation preserves meaning") is not CPU-checkable and never becomes so
- [DC] what a linter can check is that mutations under one token share an `Equivalent.Diff` — a statement about the edit, not about meaning
- [DC] robustness beyond that comes from requiring the agent to leave a trace in chat that a later pass can audit
- [CT] `Equivalent.Diff` must never be allowed to stand in for the semantic claim; each mechanism states what it actually covers
- [DC] this is the case `[PR] weaker evidence mechanisms may provide partial robustness when the gold standard cannot be established practically` ^c20260724-121u describes, with `[CT] each mechanism must make its evidence strength explicit` ^c20260724-47u as the obligation
- [PR] structure belongs only where content cannot make the distinction legible; prefer a semantic assertion audited later over a structural distinction enforced now

### Token.Primitive

- [DF] the general primitive (working name `Skw.Token`) is a token used to make an assertion, or part of one, programmatically auditable
- [DC] semantics are assigned to a token by the mechanics imposed on it, most often a linter audit
- [CT] token mechanics are gate-local; a rule stated for one token species does not constrain another
- [DC] the index today has four species with no generalizing concept — `Edition.Approval.Token`, `Poi.Unlock.Token`, `Skw.Surface.Token`, and the agendix `User.Gate.Token`; that absence is the coverage gap
- [DF] `Reading.Proxy.Token` (rename of `Skw.Surface.Token`) is a token whose possession stands in for a reading act the gate cannot observe, with `Reading.Proxy.Gate` as its gate
- [DC] `Edition.Approval.Token` is a **composition**: a reading proxy plus an approval assertion, borne by the user rather than the agent
- [PR] separating those assertions is what lets a rename relax the reading scope (the rule, not the N lines) while keeping the approval intact
- [DC] evidence strength has one stable question: how hard is the token to obtain without doing the reading it stands for
- [DC] the homogeneity constraint — every line citing one token exhibits the same induced rewrite rule, with no unexplained residue — generalizes the existing minting discipline `[DC] the agent mints a fresh token when the edition's wording changes and reuses it while the wording holds` ^c20260726-26u from *one wording* to *one rule*

### Consequences

- [DC] **citations become stable across edition** — citing a narrative resolves to the idea and picks up the current version, fixing cite staleness that exists today independent of renaming; this is the strongest argument for the model
- [CT] **adding support is a re-validation event** — under shared support, a new turn joining a narrative obliges every existing line to remain coherent with it; accretion is not free
- [DC] **the split test** — if no single wording can be coherent with all the support, the narrative has become two; a derivable signal rather than taste, though still a semantic evaluation
- [CT] **the narrative is not the default read unit** — it is an escalation rung on the `Context.Grounding` gradient, below the agendix; making it the default read costs N× context against `[PR] Kernel.Writing supplies the density filter` ^c20260729-326u
- [DC] `Index.Line.Manifest` generalizes to narrative scope rather than colliding — it is `[CT] derived inspection material, never authority` ^c20260809-185u, which is the correct shape at the wrong level
- [DC] the rollout is itself an instance of `The.Renaming.Problem` at depot scale, and the second time this design's first customer is itself (the `Skw.Surface.Token` → `Reading.Proxy.Token` rename is the first)

### Rejected

- [RJ] a closed operation vocabulary to keep transformations legible — superseded by constraining the token's extension instead, which lets the vocabulary stay open because safety comes from the token being self-evidencing
- [RJ] a `derived.approval.turn` carrying `{base, operation}` cargo — unnecessary once the support anchors are recognized as the operation log
- [RJ] grounding inherited along an ancestor chain, verified by recursive fold — support is flat; there is no chain to fold
- [RJ] a structural split between per-line provenance and per-narrative support — the distinction is semantically obvious from reading the turn, and encoding it adds a classification that can go stale or be wrong
- [RJ] a linter that recomputes the equivalence assertion — the linter reaches `Equivalent.Diff` and no further
- [RJ] naming the derived edge by its claim (`Semantically.Equivalent:<op>`) rather than its operation — withdrawn: the hollowing vector it invited is blocked by the homogeneity constraint, so the claim-shaped name is sound

## Session.Notes

**Contradicting live `[CT]`s — gated reconciliation required before any landing.**

- `^c20260811-45u` — `[CT] using an anchor as a line reference is an operational selector, not a claim that the anchor is the Index.Line identity or a Stable.Reference`. The single line that must flip; nothing else does that work.
- `^c20260811-44u`, `^c20260811-46u` — occurrence agreement and best-effort selection both presume identity lives in content. Under the new model, occurrence disagreement is a reconciliation state, not a selection failure.
- `^c20260810-22u` — `[CT] an anchor attached to a prior Support.Reference is not reused for its successor edge` forces new anchors on support change, fighting identity persistence.
- `^c20260810-20u`, `^c20260810-21u` — flagged by the user as overspecification: they prescribe when successor references get minted rather than saying what the relationship is, and were written when line→chat was the only axis.
- `^c20260729-266u` — `Support.Set` as "evidence bundle linking a grounded statement" is line-level and claim-level; the narrative model needs indexed-history, which accommodates an operational turn without labelling it.
- `^c20260809-110u` and `^c20260809-109u` are **supporting**, not contradicting: content is already denied identity and the attachment-assertion machinery already exists. The move completes a half-stated model.

**Open questions.**

- `SIS.System` — referenced by the user as where semantic assertions get evaluated later. Zero hits anywhere in the tree; not a near-miss on any existing concept. Needs definition or a pointer.
- Naming layer — `Touched.Narrative` (general model, alongside `Touched.Data` / `Touched.Support.Network`) vs `Index.Narrative` (Markdown realization). Precedent is mixed: `Index.Line` already sits in the general `Touched.Index` block.
- The general token primitive's namespace — `Skw.Token` inverts the taxonomy, since two of its three species (`Edition.Approval.Token`, `Poi.Unlock.Token`) are not Skillware. A namespace-neutral name (`Assertion.Token`, `Auditable.Token`) keeps the parent wider than its children.
- Is `Reading.Proxy.Gate` a distinct gate with its own checker, or the name for what any gate does when its token is agent-borne?
- Narrative ordering direction — versions are ordered by edition but that order carries no grounding semantics. Unsettled whether index `[0]` is oldest or newest; append-only argues oldest-first.
- Does `Semantic.Equivalent.Edition` want the `.Edition` or `.Mutation` suffix — settled on `Edition` for neighborhood consistency with `Index.Edition.Turn` and `Edition.Approval.Token`.

**Deferred.**

- Whether a line's own edit after a mutation breaks its membership or is absorbed by canonicalization. Leaning break; it is the case that will actually annoy people, so it deserves a deliberate decision.
- Whether a token is sealed or standing. Homogeneity constrains *what* may be added under a token, never *that* things may be added later, making it a standing capability with a fixed shape. Probably fine, possibly fenced by depot scope.
- Transcript durability: gate verification depends on chats surviving Chatlas retention. Already captured as `[DC] a gate is a property of an object ... with the chats retained, its state is checkable after the fact` ^c20260718-38u.

**Agendix promotion candidates** — this session leaned on all four:

- `^c20260724-47u`, `^c20260724-121u`, `^c20260724-106u` (`User.Gate/Agendix/Candidate.Skw.Context.Gate`) — explicit evidence strength, partial robustness, gate composition. This is the "algebra of gates" already harvested as a lead.
- `^c20260718-38u` (`Verbatim.User.Gated/Agendix`) — gate as a property of an object, checkable after the fact.

## Session.Log

- **2026-08-14** — opened. Design session grew out of `The.Renaming.Problem` surfaced while planning the `Agentos.*` → `Tarav.*` index rename during the tarav migration.
- Grounded against `tarav-pkg` `design/107-design.md` via `--ground`; scale measured at 39 errors / 10,682 warnings for `line-verbatim-gate` + `line-approval` on `skills/tarav-pkg`.
- Frame moved three times: gate algebra → token extension homogeneity → identity decomposition. The third reframe subsumed the first two.
- No index landing proposed. A prior `Index.Line.Identity` block draft was withdrawn at user instruction pending `::capture`; it is superseded by the `Line.Identity` and `Index.Narrative` blocks above.
