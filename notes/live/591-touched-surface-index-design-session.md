# Touched.Surface.Index — Design Session

## Session.Abstract

- `What.Design.Session` over the `Touched.Surface.Index` redesign: revisiting the index/anchory/skillware concept space from the perspective of the restate note `## 2026:07:15-17:34:41`
- the restate's spine: everything is statements linked to `Chat.Surface` user turns — the unique source of user authority; the `Agentos.Index` is one instance of a general `Touched.Surface.Index`; skw is the maintenance substrate, integrated but not user-grounded
- every block in `Design.Index` is a **revisit**: the first move on each is establishing its relationship with the restate — confirm, revise, rename, or absorb
- scope spans two depots: `agentos-pkg` (agentos-md) and `agentos-chatlas-pkg` (agentos-chatlas-md)
- session origin chat: the chat-manager/chatlas discussion that produced `Anchor.Support.Turns`, `Skw.Network`, `Index.Ontology`, the gating reframe, and the restate itself

## Design.Index

Each row: block · depot · relationship with `2026:07:15-17:34:41` · status. All statuses start `revisit-pending` unless marked. `approved-unlanded` = accepted in chat this session, not yet written to the index.

### Axis 1 — the Index generalizes to Touched.Surface.Index

- `Touched.Surface.Index` · agentos-pkg · NEW — the restate's central abstraction: surfaces of user-turn-grounded lines; name chosen over `User.Turns.Index` · **landed 2026-07-16**
- `Agentos.Index.System` (103) · agentos-pkg · member of `Touched.Surface.Index` `[DC]` added; `Project.Index` alias; namespace-member rename · **landed 2026-07-16**
- `Index.Skillware` (103) · agentos-pkg · reframe as instance of the general grounded-line surface · revisit-pending
- `Index.Main` → `Index.Ontology` (107) · agentos-pkg · role rename; concept-naming layer of the `Project.Index`; aliases `Index.Main`, `Index.Fundamentals` (kept) · **landed 2026-07-16**
- `Index.Surface` (107) · agentos-pkg · composition = router + ontology + appendix + agendix (agendix is part of the surface — its touched-captured-ungated layer); alias `Project.Index.Surface` · **landed 2026-07-16**
- `Index.Appendix` (103) · agentos-pkg · mechanical: `Index.Main` refs → `Index.Ontology`; attachment framing already landed by parallel session · revisit-light
- `Index.Agendix` (107) · agentos-pkg · parallel session landed candidate-blocks + two-axis `[CT]`; remaining: "worse cache" append (approved-unlanded) + mechanical rename + per-line-authority reword (see reconciliation) · revisit-light
- `Capture.Gradient` · agentos-pkg (107, near `Index.Agendix`) · NEW — the chat → agendix → appendix/ontology ladder; gate buys stability not authority; authority per-line in the `Chat.Support.Set` · **landed 2026-07-16**

### Axis 2 — Index.Line atom + grouping

- `Index.Line` · agentos-pkg · NEW — the restate's atom: a user-turn-grounded line; layered on `Kernel.Line` (general atom + grounding invariant) · **landed 2026-07-16**
- `Index.Block` (100) · agentos-pkg · restate: "a named set of related lines"; grouping is one of many — carries relocated line "blocks are one grouping of lines, not the only one" · revisit-pending
- `Kernel.Line` (107) · agentos-pkg · resolved by layering: stays the general writing atom; `Index.Line` = `Kernel.Line` + grounding invariant; light revision citing the specialization · revisit-light
- `Block.Line.Gradient` (107) · agentos-pkg · reconcile with the line-first model · revisit-pending

### Axis 3 — gating axis + User.Attention

- `User.Attention` · agentos-pkg · NEW — the scarce resource; verbatim gate spends it deliberately ("pass through User.Attention"); agendix scales because it does not spend it · revisit-pending
- `Edit.Trigger.Gated` → `Edition.Trigger.User.Gated` (104) · agentos-pkg · restate: convenience gate — user controls conversation/workflow; auditable but low value · **landed 2026-07-16**
- `User.Attention` block · agentos-pkg · see axis 3 header row · **landed 2026-07-16**
- `Content.Verbatim.Gated` → `Verbatim.User.Gated` (104) · agentos-pkg · restate: the authority gate — per-line approval anchors; bidirectional alignment; verbatim mismatch = linter POI for agent judgment · **landed 2026-07-16**

### Axis 4 — anchor model + typed support turns

- `Chat.Support.Set` (renamed from `Anchor.Support.Turns`) · chatlas · NEW — ordered relevance-sorted user-turn support set for anchored statements; typed members; old names retire to meta aliases · **landed 2026-07-16**; generality line added: support set is a general primitive, `Support.Set::<Subject>` specialization pattern, alias `Support.Set` · **landed 2026-07-16 ^20260716-15**
- `Turn.Type` / `Turn.Type.Vocabulary` · chatlas (next to `Chat.Support.Set`) · NEW — vocabulary of support-turn roles mirroring `Line.Type`; first member `Turn.Type::Index.Approved`; typed turns make gates lintable · **landed 2026-07-16**
- `Chatlas.Anchory` (CH 100) · chatlas · `[CT]` revision to support-set form **landed 2026-07-16**; typed-turn material lives in `Chat.Support.Set`/`Turn.Type` — no further block edit; the concept's appendix is the default landing for relevant lines that find no block · **revisited 2026-07-16, no edit**
- `Anchory.System` (107) · agentos-pkg · no generalization needed — anchory is plumbing usable by systems beyond chatlas; chatlas is currently the only consumer; payload-ownership line already covers it · **revisited 2026-07-16, no edit**
- `Line.Type::GR` (106) · agentos-pkg · boundary line added: grounding is factual evidence, not authority — gate turns live in a line's own support set · **landed 2026-07-16 ^20260716-18**
- `Kernel.Block.Grounding` (105) · agentos-pkg · support-set + approval-turn model touches grounding heads · revisit-pending
- `Inline.Grounding` (105) · agentos-pkg · trailing anchors now resolve to support sets · revisit-pending
- `Git.Dating` (107) · agentos-pkg · restate: CPU/agent path for locating verbatim/approval evidence on chats · revisit-pending

- `Touched.Support.Network` (alias `Index.Support.Network`) · agentos-pkg (107, after `Touched.Surface.Index`) · NEW — the dynamic network `Support.Set` ↔ `Anchor.Metadata` ↔ `Anchored.Line`; live cut on the surface, history in git, invariant turns on the chat; new-meaning-new-anchor doctrine · **landed 2026-07-16 ^20260716-19..24**
- archive surface · agentos-pkg/chatlas · NEW candidate — attachment surface for current relationships with drifted turns; `Line.Type::DR` (why the turn drifted, turn anchor trailing); `Outdated.Concept` fallback bucket for turns no current concept absorbs; live-cut discipline caps it (drop to git when useless) · draft-pending
- `Kernel.Block.Grounding` (105) · agentos-pkg · direction agreed in chat: line support sets absorb the evidence-board role; `Grounding.Head`/`Grounding.Drift` justification weak in the new model — rewrite pending the archive/`[DR]` drafts · discussion-advanced
- `Inline.Grounding` (105) · agentos-pkg · direction agreed: becomes *the* grounding mechanism · discussion-advanced

### Axis 5 — attachment-point generalization

- `Chat.Agendix` · chatlas · NEW — agendix mechanics attached to a chat instead of an ontology block; tape-ordered track; terminal, no drain; consumers cite the chat, never the agendix line · revisit-pending
- `Skw.Agendix` · agentos-pkg · NEW — agendix-like lines attached to an `Skw.Annotation` (file, module, class, function) · revisit-pending
- `Chat.Derivative` · chatlas · NEW — the derived-data family over chats: views (closed, model-space) vs agendix (user-touch digest) vs general derivatives (free output); skw-governed generation · revisit-pending
- `Skw.Address.Schema` (108) · agentos-pkg · attachment scales only as far as addressing — the bottleneck; chat addresses (identity_hash + tape position/range) · revisit-pending
- `Capture.Offer` (107) · agentos-pkg · the single-candidate capture across all attachment surfaces · revisit-pending

### Axis 6 — skw maintenance substrate

- `Skw.Network` · agentos-pkg · NEW — graph of annotated surfaces linked by explicit + implicit relationships; CPU notifies, agent judges · **landed 2026-07-16**
- `Agentos.Skillware` (107) · agentos-pkg · umbrella; restate: two-substrate split — authority substrate (`Touched.Surface.Index`) vs maintenance substrate (skw, not user-grounded, integrated) · revisit-pending
- `Skw.Language` (107) · agentos-pkg · restate: not all lines user-grounded; not part of `Touched.Surface.Index` but fully integrated — annotations may depend on index elements · revisit-pending
- `Drift.POI` (107) · agentos-pkg · restate: the POI is the notification and carries all drift evidence · revisit-pending
- `Surface.Annotation` (107) · agentos-pkg · restate: surfaces annotated with semantic context — how/why created — read by agents at resolution time · revisit-pending
- `Derivation.Rule` / `Derived.Content` / `Import.Management` (107) · agentos-pkg · generation-context + drift story the restate leans on · revisit-pending
- `Semantic.Router` (107) · agentos-pkg · neighboring; verify against the restate · revisit-pending

### Axis 7 — copy/reuse mechanic

- `Module.Import` (107) · agentos-pkg · restate: copy binding as reuse discipline — directional verbatim copies (A is a copy of B) across arbitrary agentic surfaces (skills, prompts) · revisit-pending
- `Skillware.Recipe` (107) · agentos-pkg · inline copy declaration form · revisit-pending

### Axis 8 — authority root (verify against restate, likely confirm + cite)

- `Chat.Surface` (100) · agentos-pkg · restate confirms: user turns as first and unique source of user authority · revisit-pending
- `Chat.Surface.Closure` (100) · agentos-pkg · restate confirms closure; verify wording · revisit-pending
- `Chat.Grounding` (100) · agentos-pkg · verify against support-set model · revisit-pending
- `Hard.Evidence` (102) · agentos-pkg · verify; likely cite up to `Touched.Surface.Index` · revisit-pending
- `We.Distrust.Summaries` (102) · agentos-pkg · verify; grounding of "consumers go down to the source" · revisit-pending
- `User.Touched` (106) · agentos-pkg · verify; the touch vocabulary the general index is named by · revisit-pending
- `Touched.Authority` (106) · agentos-pkg · verify; authority rationale for user-turn anchoring · revisit-pending

### Axis 9 — agentic verification layer (brainstorm — no drafting until matured)

- `Verification.Turn` / `Double.Check.Turn` · tbd · turns (assistant-legal) that double-check a linking state: does this turn support this line? is this really an approval turn? — verification, never authority; confidence and authority orthogonal · brainstorm
- distinct-context CPU check · tbd · N verifications count only across genuinely distinct sessions/contexts — independence is CPU-checkable via Chatlas session identity/lineage; the proof-of-work analogy · brainstorm
- `Internal.Consistency.Checker` · tbd · standing agentic workflow operationalizing the semantic lints (is this `[CT]` really a constraint? does this anchor support this line?) — factual questions, not alignment questions; user turns not specially authoritative here; spends no `User.Attention` · brainstorm
- implicit validation signals · tbd · CPU-countable: line loaded N times without change = survival evidence; weak alone (confounds validated/ignored) but always available — sometimes the only evidence; keep and weight, never drop · brainstorm
- explicit validation campaigns · tbd · launch N agents on an internal consistency test, collect OK/BAD — all chat-based, auditable (`Chat.Surface.Closure`) · brainstorm
- confidence score · tbd · accumulated verification as prioritization signal (what to re-verify first, what to trust on cheap passes) — a cache of verification: worse when stale, never a corrupted source; not a gate input, not authority · brainstorm
- system-failure POI · tbd · an old, many-times-loaded line found wrong is a failure of the verification layer itself — an improvement POI aimed at the checker, not the content · brainstorm

### Reconciliation — against parallel-session landed text (2026-07-16 anchors)

- 107 gradient line "friction buys authority" → "friction buys stability" · **landed 2026-07-16**
- `Index.Agendix` `[CT]` "uncaptured" → "ungated"; "no authority of its own" → per-line authority reword · **landed 2026-07-16**
- 106 "until captured through the gate" → "until landed through the gate" · **landed 2026-07-16**
- `references/type.md` still teaches the retired `AS:` source axis · pending sync
- SKW DRIFT FINDING (landing pass): `agentos-index` skill references (SKILL.md, edit/capture/enrich/gr-review/back-link/agendix/type .md) still cite `Index.Main` / `Content.Verbatim.Gated` / `Edit.Trigger.Gated`; `agentos skillware check` reports 0 POIs — these name-dependencies are undeclared, so the rename drifted silently; the `Skw.Network` design is the fix (pointer bindings on block names) · pending sync
- same drift in `agentos-hugentics-designer/references/index-view.md` and the project-root `.claude/skills/agentos-index` copy · pending sync

### Flagged (not a block revisit)

- `Chatlas.View.Model` / `View.Identity` / `View.Class` / `View.Workflow` / `Session.Set` (CH 100) · chatlas · legacy view family merge against `Chat.Derivative` model · merge-pending

## Session.Notes

- landing 2026-07-16: all approved items landed on both depots; linters clean (0 errors, 0 warnings each); 14 anchors minted (^20260713-3, ^20260715-5, ^20260715-6, ^20260716-1 … ^20260716-11); every landed line anchor-stamped to its approval turn
- previously approved-in-chat: `Touched.Surface.Index` block; `Chat.Support.Set` block (renamed from `Anchor.Support.Turns`); `Chatlas.Anchory` `[CT]` revision ("a chat anchor resolves to its `Chat.Support.Set`; you land on the set and read the neighborhoods"); `Skw.Network` block; `Index.Agendix` "worse cache" line; `Turn.Type` as own vocabulary (direction approved, block undrafted)

### approved block — Touched.Surface.Index

```md
## Touched.Surface.Index

- [DF] `Touched.Surface.Index` is the general category of surfaces composed of `Index.Line`s — statements grounded to a `Chat.Support.Set` of user turns
- [CT] membership is the grounding invariant: every line carries at least one anchor resolving to its `Chat.Support.Set` — nothing else is required of a member
- [DC] the `Chat.Surface` user turn is the first and unique source of user authority; every member surface roots there
- [DC] "index" is earned by construction: every line finally points down to its chat support — a member is a cache over the chats, never authority; consumers verify through the support turns
- [FR] the nature of the annotation varies by application: a line may restate the turn content, or contextualize why the support turns support what is being annotated
- [DC] member surfaces differ by design axes on top of the invariant: attachment point, gating, format, ordering
- [EX] the `Agentos.Index` is the first member — lines attached to concepts; `Chat.Agendix` attaches them to chats; `Skw.Agendix` to any `Skw.Annotation`
```

### approved block — Chat.Support.Set

```md
## Chat.Support.Set

- [DF] `Chat.Support.Set` is the ordered, relevance-sorted set of `Chat.Surface` user turns that support an anchored statement
- [CT] support turns are user turns only — the authority moments; assistant content is recovered by neighborhood reading
- [DC] a support set may hold a single turn when one turn is the actual support, or many when the fact spans them
- [DC] the set is relevance-sorted — a reader consumes top-down, as deep as its budget allows
- [DC] support turns may be typed: a type names the role a turn plays for the annotated statement, orthogonal to the sort order
- [DC] an untyped member is plain evidence — the default role; typed members carry specific duties
- [EX] `index-approved` — the turn where the user approved the line's verbatim text onto the index
- [PR] types make gates checkable: a surface's gate can require a turn of a given type in every line's set — presence is CPU-lintable, correspondence stays an agent check
- [PR] anchor the authority, read the content around it — the user reaction is the touch event; the idea it reacts to is the neighborhood
- [DC] registration echoes the set's neighborhoods for the minting agent to verify

### meta

- aliases: `Anchor.Support.Turns`, `Anchor.Landing.Turns`
```

### approved block — Verbatim.User.Gated

```md
## Verbatim.User.Gated

- [DF] `Verbatim.User.Gated` is the authority gate: the user approves the exact wording before it is committed — content passes through `User.Attention`
- [PR] this is the gate's value: the touched index moves at user speed because the user actually saw every line land
- [DC] approval is per line: each line's `Chat.Support.Set` holds a `Turn.Type::Index.Approved` turn — the evidence the user saw it
- [DC] approving a block is approving all its lines — one user act, every line grounded to that approval turn
- [DC] the gate is auditable state: presence of the approval turn is CPU-lintable; correspondence of text to turn is an agent check
- [DC] the verbatim evidence precedes or is contained in the approval turn: the agent shows the exact line in chat, the user approves — the lint searches at-or-before the approval turn, and a miss is a linter POI for agent judgment, not a failure
- [PR] the gate aligns both directions: user → index carries authority; system → user shows the user every line, refreshing their model of the system bit by bit
- [DC] implies `Edition.Trigger.User.Gated` — gated content necessarily has a gated trigger

### meta

- aliases: `Content.Verbatim.Gated`
```

### approved block — Edition.Trigger.User.Gated

```md
## Edition.Trigger.User.Gated

- [DF] `Edition.Trigger.User.Gated` is the convenience gate: the user explicitly initiates the edit workflow — the agent never starts writing mid-conversation on its own
- [PR] its value is workflow control: the user owns the conversation tempo; capture does not interrupt discussion
- [DC] auditable but low value: the triggering turn is on the chat like any other, but nothing rides on checking it — a skip's worst case is a premature draft
- [DC] distinct from `Verbatim.User.Gated`, which gates what is written rather than when

### meta

- aliases: `Edit.Trigger.Gated`
```

### approved block — User.Attention

```md
## User.Attention

- [DF] `User.Attention` is the scarce resource of the hugentic system: what the user can actually read, judge, and approve
- [PR] the system economizes it deliberately — surfaces are designed by how much of it they spend
- [DC] `Verbatim.User.Gated` spends it on purpose — that spend is what buys authority; the `Index.Agendix` scales precisely because it spends none
- [DC] analogous to attention in LLMs: the limited context the human can condition on — "we must make Y pass through the `User.Attention`"
- [EX] spend it on the `Project.Index`; offload everything else to agent-driven surfaces
```

### approved block — Turn.Type

```md
## Turn.Type

- [DF] `Turn.Type` is the role a member turn plays inside a `Chat.Support.Set` — a per-member tag, orthogonal to the set's relevance sort
- [DC] the untyped member is the default: plain evidence for the annotated statement
- [DC] the vocabulary is soft and extensible (`Concept.Hardness`) — a new type is an index edit, mirroring `Line.Type.Vocabulary`
- [DC] gates consume types by name: a surface gate may require a turn of a given type in every line's set; the linter checks presence, the agent checks correspondence
- [DC] gate types follow the surface: each `Verbatim.User.Gated` surface names its own gate type — `Turn.Type::<Surface>.Gate`
- [EX] `Turn.Type::Project.Index.Gate` — the turn that opened the project index gate for a line's verbatim text; required by the `Project.Index`'s gated surfaces

### meta

- aliases: `Turn.Type::Index.Approved` (retired to alias of `Turn.Type::Project.Index.Gate`)
```

RENAME RIPPLE (mechanical, applied at landing): `Verbatim.User.Gated` `[DC]` and `Index.Line` `[EX]` say `Turn.Type::Index.Approved` → `Turn.Type::Project.Index.Gate`.

### approved block — Index.Ontology

```md
## Index.Ontology

- [DF] `Index.Ontology` is the concept-naming layer of the `Project.Index` — the routed body of `Index.Block`s that names and defines the project's concepts
- [DC] it is the authoritative name-set: `Index.Appendix` and `Index.Agendix` attach their material to concepts the ontology names
- [DC] fully composed of conceptual blocks under tight `Kernel.Writing` compression, every one routed by `Index.Router`
- [DC] it is the index-level echo of `Kernel.Block.Fundamentals`: the compressed front, depth deferred to `Index.Appendix`
- [DC] with `Index.Appendix`, `Index.Agendix`, and `Index.Router` it composes the `Index.Surface`

### meta

- aliases: `Index.Main`, `Index.Fundamentals`
```

### approved revision — Agentos.Index.System (additions)

```md
- [DC] it is a member of the `Touched.Surface.Index` category — `Index.Line`s attached to the project's named concepts
```
plus meta aliases gain `Project.Index`; namespace-members: `Index.Main` → `Index.Ontology`.

### approved revision — Index.Surface

```md
- [DF] `Index.Surface` is the file surface of one `Project.Index` — `Index.Router`, `Index.Ontology`, `Index.Appendix`, and `Index.Agendix` taken as a single addressable surface
- [DC] the agendix is part of the surface — its touched, captured, ungated layer

### meta

- aliases: `Project.Index.Surface`
```
(rest of block intact; `Index.Main` ref updated)

### approved block — Capture.Gradient

```md
## Capture.Gradient

- [DF] `Capture.Gradient` is the ladder a touched statement climbs across surfaces: chat → agendix → appendix/ontology
- [DC] chat — touched, uncaptured, volatile
- [DC] agendix — touched, captured, ungated: agent-authored wording, not a `Stable.Surface` — nothing may link into it
- [DC] appendix/ontology — touched, captured, gated: wording passed `User.Attention`, a `Stable.Surface` — citable from other surfaces
- [PR] the gate buys stability, not authority: authority is per-line, living in its `Chat.Support.Set` — a thinly grounded gated line can carry less weight than an agendix line grounded on an explicit user statement
- [DC] reading order follows the gradient — ontology and appendix first, agendix later: a prior, not a verdict on any line
```

### approved block — Index.Line

```md
## Index.Line

- [DF] `Index.Line` is the atom of the `Touched.Surface.Index`: one statement, grounded to a `Chat.Support.Set` by its trailing anchor
- [CT] one line, one fact — atomic and reorderable, surviving on its own (`Kernel.Writing` granularity)
- [DC] the line is the unit of grounding, approval, and audit: gates, linters, and drift checks run per line
- [DC] lines carry a `Line.Type` classifying their act
- [EX] on a `Verbatim.User.Gated` surface, each line's support set holds a `Turn.Type::Index.Approved` turn
- [PR] everything above the line is organization — blocks, surfaces, attachment points; everything below it is evidence — anchors, support sets, turns
```

- settled vocabulary this session: **Index** = whole surface; **Ontology + Appendix + Agendix** = its content layers; `Touched.Surface.Index` chosen over `User.Turns.Index`; per-line approval (block approval = approving all its lines); `Verbatim.User.Gated` = authority gate (content passes through `User.Attention` at user speed, evidenced by approval turns); `Edition.Trigger.User.Gated` = convenience gate (user controls workflow)
- open threads: typed support turns (approval turn type) vs `[AP]` line — leaning typed turns + linter rule; mechanical edits (renames, typos) vs verbatim gate re-approval noise; `Index.Fundamentals` alias keep/drop; `Skw.Network` still maturing
- anchor-model settled prose: an anchor is an ordered relevance-sorted set of supporting user turns; no privileged element; land on the set, read the neighborhoods; "anchor the authority, read the content around it"

## Session.Log

- 2026-07-16 — session opened; artifact created from the 8-axis grounding worklist; all blocks set to revisit against `## 2026:07:15-17:34:41`
- 2026-07-16 — `Touched.Surface.Index` converged and approved (invariant-only membership; "index" earned by construction; annotation nature application-free)
- 2026-07-16 — `Anchor.Support.Turns` renamed `Chat.Support.Set`; typed support turns added (roles orthogonal to relevance sort; `index-approved` first type; presence CPU-lintable / correspondence agent-checked); `Turn.Type` to be own vocabulary mirroring `Line.Type`
- 2026-07-16 — `Turn.Type` block approved (chatlas, next to `Chat.Support.Set`; `Turn.Type::Index.Approved` first member)
- 2026-07-16 — `Index.Line` block approved (fundamentals only; workflow lines relocated to `Verbatim.User.Gated` and `Index.Block` rows); `Kernel.Line` resolved by layering — general atom stays, `Index.Line` adds the grounding invariant
- 2026-07-16 — axis 3 approved: `Verbatim.User.Gated` (authority gate, bidirectional alignment, verbatim-precedes-or-contained, mismatch = POI), `Edition.Trigger.User.Gated` (convenience gate), `User.Attention`; mechanical-edits thread dissolved into CPU-presence/agent-judgment split
- 2026-07-16 — axis 9 added (brainstorm): agentic verification layer — verification vs authority split (factual vs alignment questions), distinct-context checks, implicit/explicit validation signals, confidence as prioritization, system-failure POIs
- 2026-07-16 — parallel-session discovery: touch/capture two-axis model discussed and refined to touch + capture + gate (capture = harvesting, both agendix and index capture; the splitting axis is the user gate); both axes readable off the `Chat.Support.Set` (gate turn present → gated; set without gate turn → ungated; no set → illegal)
- 2026-07-16 — `Turn.Type::Index.Approved` renamed `Turn.Type::Project.Index.Gate`; pattern `Turn.Type::<Surface>.Gate` fixed; ripple noted
- 2026-07-16 — ontology trio approved: `Index.Ontology` (Project.Index-scoped, both aliases kept), `Agentos.Index.System` additions, `Index.Surface` (agendix included as touched-captured-ungated layer; `Project.Index.Surface` alias)
- 2026-07-16 — `Capture.Gradient` block approved: gate buys stability not authority; authority is per-line in the support set; reading order a prior, not a verdict; reconciliation section opened against parallel-session landed text
- 2026-07-16 — LANDING PASS: all 15 approved items landed (agentos-pkg: Touched.Surface.Index, Index.Line, User.Attention, Capture.Gradient, Skw.Network new; Index.Ontology, Index.Surface, Agentos.Index.System, Edition.Trigger.User.Gated, Verbatim.User.Gated, Index.Agendix, Kernel.Line, Index.Appendix revised; 106/107 reconciliations · chatlas: Chat.Support.Set, Turn.Type new; Chatlas.Anchory revised); routers updated; linters clean; 14 approval anchors minted and stamped
- 2026-07-16 — skw test observations recorded in reconciliation section: silent drift in skill references (undeclared name-dependencies), skillware check blind to it — Skw.Network pointer bindings are the designed fix
