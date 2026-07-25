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
- `Index.Block` (100) · agentos-pkg · two lines added: named grouping of `Index.Line`s (attaches lines to the heading's concept); one grouping among many — grounding/approval/audit per line · **landed 2026-07-18 ^c20260718-14u**
- `Kernel.Line` (107) · agentos-pkg · resolved by layering: stays the general writing atom; `Index.Line` = `Kernel.Line` + grounding invariant; light revision citing the specialization · revisit-light
- `Block.Line.Gradient` (107) · agentos-pkg · one line added: gradient is organization above the `Index.Line` — position never changes grounding/authority · **landed 2026-07-18 ^c20260718-15u — axis 2 closed**

### Axis 3 — gating axis + User.Attention

- `User.Attention` · agentos-pkg · NEW — the scarce resource; verbatim gate spends it deliberately ("pass through User.Attention"); agendix scales because it does not spend it · revisit-pending
- `Edit.Trigger.Gated` → `Edition.Trigger.User.Gated` (104) · agentos-pkg · restate: convenience gate — user controls conversation/workflow; auditable but low value · **landed 2026-07-16**
- `User.Attention` block · agentos-pkg · see axis 3 header row · **landed 2026-07-16**
- `Content.Verbatim.Gated` → `Verbatim.User.Gated` (104) · agentos-pkg · restate: the authority gate — per-line approval anchors; bidirectional alignment; verbatim mismatch = linter POI for agent judgment · **landed 2026-07-16**

### Axis 4 — anchor model + typed support turns

- `Chat.Support.Set` (renamed from `Anchor.Support.Turns`) · chatlas · NEW — ordered relevance-sorted user-turn support set for anchored statements; typed members; old names retire to meta aliases · **landed 2026-07-16**; generality line added: support set is a general primitive, `Support.Set::<Subject>` specialization pattern, alias `Support.Set` · **landed 2026-07-16 ^c20260716-15u**
- `Turn.Type` / `Turn.Type.Vocabulary` · chatlas (next to `Chat.Support.Set`) · NEW — vocabulary of support-turn roles mirroring `Line.Type`; first member `Turn.Type::Index.Approved`; typed turns make gates lintable · **landed 2026-07-16**
- `Chatlas.Anchory` (CH 100) · chatlas · `[CT]` revision to support-set form **landed 2026-07-16**; typed-turn material lives in `Chat.Support.Set`/`Turn.Type` — no further block edit; the concept's appendix is the default landing for relevant lines that find no block · **revisited 2026-07-16, no edit**
- `Anchory.System` (107) · agentos-pkg · no generalization needed — anchory is plumbing usable by systems beyond chatlas; chatlas is currently the only consumer; payload-ownership line already covers it · **revisited 2026-07-16, no edit**
- `Line.Type::GR` (106) · agentos-pkg · boundary line added: grounding is factual evidence, not authority — gate turns live in a line's own support set · **landed 2026-07-16 ^c20260716-18u**
- `Kernel.Block.Grounding` (105) · agentos-pkg · support-set + approval-turn model touches grounding heads · revisit-pending
- `Inline.Grounding` (105) · agentos-pkg · trailing anchors now resolve to support sets · revisit-pending
- `Git.Dating` (107) · agentos-pkg · already general: "git dates the wording, chatlas finds the session and turns" covers gate-turn location; capability block does not name its new consumers (`Touched.Support.Network`, `Demoted.Anchored.Line`) · **revisited 2026-07-17, no edit — axis 4 closed**

- `Touched.Support.Network` (alias `Index.Support.Network`) · agentos-pkg (107, after `Touched.Surface.Index`) · NEW — the dynamic network `Support.Set` ↔ `Anchor.Metadata` ↔ `Anchored.Line`; live cut on the surface, history in git, invariant turns on the chat; new-meaning-new-anchor doctrine · **landed 2026-07-16 ^c20260716-19u..24**
- `Demoted.Anchored.Line` (defines `Index.Demoted.Turn` inline) · agentos-pkg (107, after `Touched.Support.Network`) · NEW — demotion replaced the archive/`[DR]`/`Outdated.Concept` corridor entirely: a demoted edge is evidence-based and computed (git history vs live cut), nature unknown by design, no stored account; `[RJ]` on archive surfaces and maintained drift explanations; appendix holds generated-views, rejoining, and the design arc · **landed 2026-07-16 ^c20260716-25u..31**
- `Kernel.Block.Grounding` (105) · agentos-pkg · RETIRED — grounding is a line property, defined positively on `Index.Line`; block removed, `Grounding.Head`/`Grounding.Drift` demote as machinery; old appendix deleted (git keeps) · **landed 2026-07-17 ^c20260716-33u ^c20260717-0u**
- `Inline.Grounding` (105) · agentos-pkg · RETIRED — block removed; surviving mechanics (≤3 curated anchors, gate-turn fallback stamp, reading rule, `Grounding.Density`) migrated to new `Index.Line` appendix (`Grounding.Mechanics`/`Grounding.Density`/`Grounding.Head` sections); `Grounded.Line`/`Ungrounded.Line` inlined on `Index.Line` (`[+2]` concepts) · **landed 2026-07-17 ^c20260716-33u ^c20260717-0u**
- grounding-retirement follow-ups · pending — (a) tooling Impl.Req: `--coverage block` / evidence-board flag in linter.py + stats.py measure by `Grounding.Head` presence, axis now retired; (b) citation drift: `Grounding.Head`/`Inline.Grounding`/`Kernel.Block.Grounding` still cited in 100/102/103, SKILL.md, index-block-catalog, ~5 appendix files — dependency-sync territory; (c) existing `Grounding.Head`/`Grounding.Drift` appendix sections across depots demote in place, cleaned opportunistically · **594 EXECUTED 2026-07-18: tooling recut to line-property coverage + citations synced; (c) stays opportunistic; open follow-up: appendix-section names invisible to the Dotted.Name resolver (Capture.Offer depends blessed) ^c20260718-1u**

### Axis 5 — attachment-point generalization (CLOSED 2026-07-18 — chat-derivative rows split to axis 11)

- `Chat.Agendix` (defines `Turn.Type::Attachment` inline) · chatlas (100, after `Turn.Type`) · NEW — TSI member attached to the `Chat.Surface`; lines ground through `Chat.Support.Set` (multi-turn claims), one member is the attachment turn (`Turn.Type::Attachment`, tape position + ordering key, gate-pattern presence lint); ungated, tape-ordered, terminal (never drains), consumers cite the chat, converges on closed chats, hard provenance · **landed 2026-07-17 ^c20260713-6u ^c20260713-7u ^c20260717-1u ^c20260717-2u**
- `Skw.Touched.Index` (defines `Skw.Appendix`/`Skw.Agendix` inline; supersedes the standalone `Skw.Agendix` row) · agentos-pkg (107, before `Skw.Network`) · NEW — TSI member on `Skw.Annotation`s; one mixed surface, gated/ungated computed per line from the gate-typed turn (not geographic); promotion = state change, not relocation; two worlds meet at the annotation (skw = whole agentic development stack, not just maintenance — axis-6 wording consequence: "maintenance substrate" → "development substrate") · **landed 2026-07-17 ^c20260717-6u..10**
- `Skw.Address.Schema` (108) · agentos-pkg · schema shape holds against all new systems; chat space stays registration-only (anchory detaches link shape from link content — pollution cap); raw path-like chat address `[RJ]`-parked + prefix-ripple noted in new `Skw.Address.Schema` agendix; code-construct addressing stays free-form under the `[FR]` line; no fourth space — accounts/namespaces are registers, not spaces · **revisited 2026-07-17, agendix capture only ^c20260717-11u**
- `Capture.Offer` (107) · agentos-pkg · destinations line fixed ("index main" → "ontology") + generalization line (offer may target any TSI member within reach); demoted to `Touched.Surface.Index` appendix, then PROMOTED BACK to a 107 block after 594 execution showed appendix sections are invisible to the Dotted.Name resolver — needing to be referenceable is a reason to create a block (new closing line captures this); appendix file removed, router restored · **revisited, demoted, promoted back 2026-07-18 ^c20260718-0u ^c20260718-1u ^c20260718-2u**

### Axis 6 — skw development substrate (CLOSED 2026-07-19)

- `Skw.Network` · agentos-pkg · NEW — graph of annotated surfaces linked by explicit + implicit relationships; CPU notifies, agent judges · **landed 2026-07-16**
- `Agentos.Skillware` (107) · agentos-pkg · restate's two-substrate split REJECTED in discussion: no split — touch is an orthogonal axis over skw objects, TSI = the computed set of touched things; +3 lines (no-split, annotation-touched-itself, integration-at-scale promoted from agendix) · **landed 2026-07-19 ^c20260719-0u ^c20260718-23u**
- `Skw.Quote.Binding` (107) · agentos-pkg · NEW — dependency declared by its own quoted content (`--quote` refining nearest `--from`); designed in-session, agendix-captured, promoted · **landed 2026-07-18 ^c20260718-25u..29u**
- `Skw.Touched.Index` (107) · agentos-pkg · +syntax line: `--supp <line> ^<anchor>` — the annotation is its own block; deps bind content, supps ground the annotation itself · **landed 2026-07-19 ^c20260719-0u**
- `Skw.Language` (107) · agentos-pkg · +boundary line: skw lines need no user grounding, touch opt-in per object · **landed 2026-07-19 ^c20260719-0u**
- `Drift.POI` (107) · agentos-pkg · restate's "POI carries all drift evidence" already stated by the trigger line · **revisited 2026-07-19, no edit**
- `Surface.Annotation` (107) · agentos-pkg · restate's resolution-time semantic context = the local-grounding-recipe line · **revisited 2026-07-19, no edit**
- `Derivation.Rule` / `Derived.Content` / `Import.Management` (107) · agentos-pkg · generation-context + drift story intact, no contradiction · **revisited 2026-07-19, no edit**
- `Semantic.Router` (107) · agentos-pkg · neighboring only, restate does not touch it · **revisited 2026-07-19, no edit**
- PARKED: label sigil collision (`^label` vs anchory `^c…` keys; candidate: labels move to `@`) · parked 2026-07-19

### Axis 7 — copy/reuse mechanic (CLOSED 2026-07-19 — resolved as the skw consolidation)

- `Module.Import` (107) · agentos-pkg · RENAMED `Skw.Dependency`, absorbing `Import.Management` (aliases keep both names); DF recut to any-two-surfaces; derived mode recut off `Derivation.Rule` · **landed 2026-07-19 ^c20260719-1u**
- `Skillware.Recipe` (107) · agentos-pkg · RETIRED — absorbed by the construct form; `[RJ] Import.Manifest` + v1 recipe realization migrated to `Skw.Dependency/Appendix` · **landed 2026-07-19 ^c20260719-1u**
- `Skw.Annotation` (107) · agentos-pkg · NEW — the unit/primitive of skw (was a dangling name in `Skw.Touched.Index`'s DF); absorbs `Skillware.Construct` (syntax) + `Surface.Annotation` (aliases both); construct-grammar depth → `Skw.Annotation/Construct.Grammar` appendix section · **landed 2026-07-19 ^c20260719-1u**
- `Derivation.Rule` / `Derived.Content` / `Derived.Module` (107) · agentos-pkg · RETIRED — derivation mechanics salvaged to `Skw.Dependency/Appendix` · **landed 2026-07-19 ^c20260719-1u**
- consolidation sweep: 107 namespace members 20→14; router row updated; appendix/agendix files renamed (`Surface.Annotation-appendix`→`Skw.Annotation-appendix`, `Module.Import-agendix`→`Skw.Dependency-agendix`); 3 appendix cites recut; agentos-skillware skill re-derived (doctrine/lang/author/check src; 3 derived-stale POIs: 2 re-derived, 1 blessed); depot linter 0/0 · **2026-07-19**

### Axis 8 — authority root (CLOSED 2026-07-19 — verified against the landed model: 5 confirm as-is + 2 cite-up ^c20260719-2u)

- `Chat.Surface` (100) · agentos-pkg · CONFIRMED as-is — "user turns are `User.Touched` surface, assistant turns touched-adjacent" states the root cleanly · **closed 2026-07-19**
- `Chat.Surface.Closure` (100) · agentos-pkg · CONFIRMED as-is — wording holds against the no-split model · **closed 2026-07-19**
- `Chat.Grounding` (100) · agentos-pkg · CONFIRMED as-is — already per-line ("a block or line linked back"); compatible with the support-set model · **closed 2026-07-19**
- `Hard.Evidence` (102) · agentos-pkg · CONFIRMED + cite-up line landed: anchors make the descent mechanical; `Touched.Surface.Index` = the computed set of claims that survive it ^c20260719-2u · **landed 2026-07-19**
- `We.Distrust.Summaries` (102) · agentos-pkg · CONFIRMED as-is — "the link restores confidence — recompute against the evidence" is the consumers-go-down-to-the-source grounding · **closed 2026-07-19**
- `User.Touched` (106) · agentos-pkg · CONFIRMED + cite-up line landed: `Touched.Surface.Index` is the computed enumeration of the predicate ^c20260719-2u · **landed 2026-07-19**
- `Touched.Authority` (106) · agentos-pkg · CONFIRMED as-is — "no authority status is stored — read from provenance" is exactly the computed-TSI stance · **closed 2026-07-19**

### Axis 9 — agentic verification layer (brainstorm — no drafting until matured)

- `Verification.Turn` / `Double.Check.Turn` · tbd · turns (assistant-legal) that double-check a linking state: does this turn support this line? is this really an approval turn? — verification, never authority; confidence and authority orthogonal · brainstorm
- distinct-context CPU check · tbd · N verifications count only across genuinely distinct sessions/contexts — independence is CPU-checkable via Chatlas session identity/lineage; the proof-of-work analogy · brainstorm
- `Internal.Consistency.Checker` · tbd · standing agentic workflow operationalizing the semantic lints (is this `[CT]` really a constraint? does this anchor support this line?) — factual questions, not alignment questions; user turns not specially authoritative here; spends no `User.Attention` · brainstorm
- implicit validation signals · tbd · CPU-countable: line loaded N times without change = survival evidence; weak alone (confounds validated/ignored) but always available — sometimes the only evidence; keep and weight, never drop · brainstorm
- explicit validation campaigns · tbd · launch N agents on an internal consistency test, collect OK/BAD — all chat-based, auditable (`Chat.Surface.Closure`) · brainstorm
- confidence score · tbd · accumulated verification as prioritization signal (what to re-verify first, what to trust on cheap passes) — a cache of verification: worse when stale, never a corrupted source; not a gate input, not authority · brainstorm
- system-failure POI · tbd · an old, many-times-loaded line found wrong is a failure of the verification layer itself — an improvement POI aimed at the checker, not the content · brainstorm

### Axis 10 — accountable assertions, gates, and the Bloberia (brainstorm 2026-07-17, discussion-advanced — drafting order agreed, not landed)

- `User.Gate` · agentos-pkg (104) · **LANDED 2026-07-19 ^c20260719-12u..15u** — redesigned in discussion: a gate IS an `Accountable.Assertion` whose claim is about the `Chat.Surface` (evidence of a declared kind findable in the dossier); one declaration, two systems read it — flow (pre-evidence, behavior-shaping, honored in-session) and audit (post-evidence, recomputable assert, checker territory); predicate family existence/correspondence/order, gate strength = predicate composition (verbatim = all three, edition-trigger = existence only); state computed never stored — invalidation is recomputation returning failed; robustness = design for audit, not for enforcement; gates attach to any assertable object (gates-as-skw-primitive is this applied, not a separate design); instance cross-lines added to both 104 gate blocks · **landed 2026-07-19**
- `Accountable.Assertion` · agentos-pkg · **LANDED 2026-07-19 (106) ^c20260719-8u..10u** — reframed in discussion: the root is the principle `Constraint.Steering` (NEW, 106: steer agent work by designing constraints; anatomy: mint-time test, standing test, graded checkability, direction-forcing, stability; compiler-loop PR; instances line), and `Accountable.Assertion` is its unit/deposit — recorded claim (stamp = judgment cached at mint, never truth) + audit path; trail realizations on-surface (type tag) or external schema (Anchory dossier), axis = audit cost; judgment is someone's (user or agent), authority stays `Touched.Authority`; `Line.Type` gained the static-typing analogy + stability lines · **landed 2026-07-19**
- trust tiers / trust policy · agentos-pkg · workflow parameter, sibling of `Alignment.Mode`: callers choose the trust level tolerated — trust stated value → CPU checks → evidence metadata → replay evaluations → descend to `Hard.Evidence`; `We.Distrust.Summaries` = the warning label on the top tier, not a ban; system's job: make every policy expressible and the descent always convenient · discussion-advanced
- `Judgement.Bank` · namespace · evaluation ledger: accounts for assertions, transactions = evaluation records (assertion id, verdict, evaluator, anchor into evaluating session, version-bound via the POI-identity discipline), balance = computed fold, never stored authority; bless records are the one-sided prototype (judgment cache recording only overrides); campaigns (axis 9) fill it; `Index.Line` = the md-native realization with an empty evaluation ledger today · **RETIRED as a name 2026-07-20 ^c20260720-0u** — nothing left to mint: the system dissolved into Anchory (Bloberia deflation) + the dossier model (anchor = collection point); the surviving substance landed as 2 lines on `Accountable.Assertion` (open-append evaluation records folded on read; evaluation is confidence, never authority — second record family beside the gated dossier); new systems implemented on demand, axis 9 mints the real concept when the verification layer matures
- `Bloberia` · DEFLATED 2026-07-17 — the substrate idea collapsed back into `Anchory`: the `^<text>` surface primitive, JSON payloads with subsystem-owned meaning, and `Anchory.Namespace` already exist; what evidence mechanics need is an Anchory evolution, not a sibling system — (1) append semantics (accumulating records/accounts), (2) query over payloads (folds, filters), (3) central/local depots with row-level sync (chatlas-update-shaped, not git-pull); `Judgement.Bank` becomes an Anchory namespace/application; boundary stands: surfaces = human world, depot = machine world, pointers bridge · resolved-conceptually
- axis 10 net yield (user consolidation 2026-07-17): the genuinely new concept is `Accountable.Assertion` — conceptualizing that the surfaces are full of assertions (type tags, anchors, declarations = frozen judgment + audit path); plus the mechanics mandate: conceptualize and implement evidence accumulation (evaluation records, version-binding, computed balances) on Anchory; trust tiers = workflow policy; existing system integrates unchanged (linter = CPU tier, POI/bless = one-sided judgment-record prototype, `Index.Line` = md-native ad-hoc-but-conformant realization) · discussion-advanced
- drafting order agreed: `Accountable.Assertion` root first, then `User.Gate`, then `Judgement.Bank`/`State.Point` as thin consumers on Anchory · queue — `Accountable.Assertion`+`Constraint.Steering` and `User.Gate` LANDED 2026-07-19; `State.Point` RETIRED 2026-07-19 before drafting: never realized anywhere, and a stored state point contradicts the landed computed-never-stored rule — its evaluation-record reading is `Judgement.Bank`'s transaction
- anchory evolution (designed in chat 2026-07-17, ^c20260717-3u): namespace activation (namespace = logical axis inside depots, `--namespace`; depot = materialization address, `--depot` short-circuits discovery), per-namespace `meta.json` (intention fallback, declared key prefix `c20260716-5`-style, semantics pointer), local+global depot registry with auto-registration on touch, `Pwd.Upward.Search` via registry records (agendix-captured), `resolve` without prior depot knowledge, `--meta` flag (metadata never bundled by default), `agentos-anchory-pkg` skill as the universal literacy surface; grammar settled 2026-07-18: `^c20260718-4u` (ns-prefix + alloc-prefix + counter + optional turn-tag suffix; tag never allocates, passed at register, anchory composes; bare citations banned on surfaces via lint; tag-less keys are a lint POI) — Impl.Req `agentos-py/notes/live/694-anchory-evolution-impl-req.md` · **EXECUTED 2026-07-18**: grammar live (`^c20260718-4u`), chatlas depot migrated 150/150 (0 tag-less), 620 citations swept across 57 files, both depots lint clean, `agentos-anchory-pkg` skill created; post-ship doc-sync scan landed 2026-07-18 ^c20260718-3u: skill grammar/CLI references updated (agentos-index src + chatlas-commands), `Chatlas.Anchory` key-convention line rewritten + turn-tag line added, `Skw.Address.Schema` agendix ripple flipped to landed, `Anchory.System` enriched (composed keys / meta.json intention / registry+Pwd.Upward.Search)
- `Agentos.Forum` (adjacent system, ^c20260717-5u): agendix-captured; Impl.Req at `agentos-py/notes/live/693-agentos-forum-impl-req.md` · **EXECUTED 2026-07-18** (external agent; `agentos forum post|check|read` live, banner on `chatlas update`, `agentos-forum` skill; deviations: root corrected to `~/Documents/agentos/forum/`, retired `agentos future forum` replaced without aliases)
- DO NOT FORGET — first real forum post: "update your anchors — namespace/prefix changes, see more..." · **POSTED 2026-07-18T10:36:53Z** — "update your anchors: anchory namespace grammar shipped", the forum's first real post

### Axis 11 — chat derivative family (split from axis 5 2026-07-18 — less mature design, own maturation track)

- `Chat.Derivative` · chatlas · NEW — the derived-data family over chats: views (closed, model-space) vs agendix (user-touch digest) vs general derivatives (free output); skw-governed generation · revisit-pending
- `Chatlas.View.Model` / `View.Identity` / `View.Class` / `View.Workflow` / `Session.Set` (CH 100) · chatlas · legacy view family merge against `Chat.Derivative` model (moved from Flagged) · merge-pending

### Reconciliation — against parallel-session landed text (2026-07-16 anchors)

- 107 gradient line "friction buys authority" → "friction buys stability" · **landed 2026-07-16**
- `Index.Agendix` `[CT]` "uncaptured" → "ungated"; "no authority of its own" → per-line authority reword · **landed 2026-07-16**
- 106 "until captured through the gate" → "until landed through the gate" · **landed 2026-07-16**
- `references/type.md` still teaches the retired `AS:` source axis · **RESOLVED 2026-07-20 — verified no drift**: both `AS:` mentions (type.md, check.md) already teach the retired form (`[AS:XX]` is retired/legacy; `AS:` outside `agendix/` is a lint ERROR) — this is the current model, not stale teaching
- SKW DRIFT FINDING (landing pass): `agentos-index` skill references still cite `Index.Main` / `Content.Verbatim.Gated` / `Edit.Trigger.Gated` · **RESOLVED 2026-07-20 — swept by a parallel session**: zero occurrences remain in `skills/agentos-index` or `skills/agentos-hugentics-designer`; `agentos skillware check --skill skills/agentos-index` = 0 POIs, compiled surfaces match src. Residual old-name hits across the depot are exclusively `- aliases:` declarations (107/104) and appendix salvage notes (`Skw.Dependency`/`Skw.Annotation`) — all legitimate, kept resolvable by design. The underlying gap (undeclared name-dependencies drifting silently) stays real; `Skw.Network` pointer bindings remain the structural fix, tracked as a toolchain follow-up
- same drift in `agentos-hugentics-designer/references/index-view.md` and the project-root `.claude/skills/agentos-index` copy · **RESOLVED 2026-07-20 — no-op**: `index-view.md` does not exist; `.claude/skills` are symlinks into `skills/`, so already covered

## Session.Notes

- landing 2026-07-16: all approved items landed on both depots; linters clean (0 errors, 0 warnings each); 14 anchors minted (^c20260713-3u, ^c20260715-5u, ^c20260715-6u, ^c20260716-1u … ^c20260716-11u); every landed line anchor-stamped to its approval turn
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
- 2026-07-18 — chat-derivative rows split from axis 5 into new axis 11 (less mature design, own maturation track); axis 5 closed
- 2026-07-18 — axis 2 closed: `Index.Block` gains the line-first pair (^c20260718-14u), `Block.Line.Gradient` gains the organization-above-the-line boundary (^c20260718-15u); `Index.Line` row was already landed 2026-07-16, `Kernel.Line` resolved by layering
- 2026-07-18 — axis 6 opened as alignment discussion: skw = integration substrate (deps between any two surfaces, TSI expansion via backends, gates as skw primitive deferred); `Quote.Binding` designed and named — dependency declared by its own quoted content (`--quote` flag refining nearest `--from`, exact syntax approved on a python example; machinery out of docstrings); agendix capture landed (candidate block `Module.Import/Agendix/Quote.Binding` + lines on `Module.Import`, `Skw.Backend`, `Agentos.Skillware`, `Verbatim.User.Gated`; ^c20260718-23u..28u)
- 2026-07-19 — axis 7 CLOSED as the skw consolidation (^c20260719-1u): `Skw.Annotation` minted as the primitive (absorbs `Skillware.Construct`+`Surface.Annotation`), `Module.Import`→`Skw.Dependency` absorbing `Import.Management`, derivation trio + `Skillware.Recipe` retired with appendix salvage; skw family 26→20 blocks; full citation sweep incl. agentos-skillware skill re-derivation; all repos committed first per user instruction
- 2026-07-19 — axis 6 CLOSED: no-split model approved (touch orthogonal over skw objects; TSI = computed set of touched things); `--supp` designed — the annotation's own `Index.Line`s, "the annotation is its own block"; revision set landed on `Agentos.Skillware` (+3), `Skw.Touched.Index` (+1), `Skw.Language` (+1); Drift.POI/Surface.Annotation/derivation-trio/Semantic.Router revisited no-edit; label-sigil question parked (^c20260719-0u)
- 2026-07-18 — `Quote.Binding` PROMOTED to 107 as `Skw.Quote.Binding` (alias `Quote.Binding`; +content-addressing PR line; `Module.Import` gains the refinement cross-line; candidate block removed from agendix; router + namespace members updated) ^c20260718-29u
- 2026-07-19 — axis 8 CLOSED (^c20260719-2u): all seven authority-root blocks verified against the landed model — 5 confirmed as-is (`Chat.Surface`, `Chat.Surface.Closure`, `Chat.Grounding`, `We.Distrust.Summaries`, `Touched.Authority`), 2 gained a cite-up line to `Touched.Surface.Index` (`Hard.Evidence`: anchors make the descent mechanical; `User.Touched`: the TSI is the computed enumeration of the predicate)
- 2026-07-19 — anchor/support-set discussion agendix-captured (^c20260719-3u ^c20260719-4u): anchor = evidence-dossier collection point with a meaningless key (semantic assertion = the line↔support-set relationship); append point for same-meaning evidence, new anchor on meaning change; support set structured by chats with typed turns (CPU-checkable independence); support-append is a GATED editor operation — candidates `Index.Edit.Support.Append` + `Index.Editor` role (agendix: Touched.Support.Network, Index.Edit.Action)
- 2026-07-19 — axis 10 head LANDED (^c20260719-8u ^c20260719-9u ^c20260719-10u): `Constraint.Steering` minted (106) — steer agent work by designing constraints; five-point anatomy (mint-time test, standing test, graded checkability, direction-forcing, stability) + compiler-loop PR + instances; `Accountable.Assertion` landed beside it as the deposited unit (stamp + audit path; on-surface vs external-schema trail, audit-cost axis); `Line.Type` gained static-typing analogy + stability lines; router row updated
- 2026-07-19 — `User.Gate` LANDED (104, ^c20260719-12u ^c20260719-13u ^c20260719-14u ^c20260719-15u): gate = an `Accountable.Assertion` over the `Chat.Surface`; flow/audit as two systems on one declaration; existence/correspondence/order predicates, strength = composition; state computed never stored (invalidation = recomputation); design-for-audit-not-enforcement robustness PR; gates attach to any assertable object; instance cross-lines on `Verbatim.User.Gated` + `Edition.Trigger.User.Gated`; router row updated — axis 10 queue: 2 of 3 drafted (`Judgement.Bank`/`State.Point` remain)
- 2026-07-20 — `Judgement.Bank` RETIRED as a name (^c20260720-0u): the system already dissolved into Anchory + the dossier model; substance landed as 2 lines on `Accountable.Assertion` (open-append evaluation records, folded on read, second family beside the gated dossier; [CT] evaluation is confidence never authority); `State.Point` retired earlier same pass — axis 10 queue fully resolved (2 landed, 2 retired)
- 2026-07-20 — reconciliation sweeps CLOSED (verification pass, no edits needed): the rename drift (`Index.Main`/`Content.Verbatim.Gated`/`Edit.Trigger.Gated`) was already swept by a parallel session (0 residual in agentos-index/agentos-hugentics-designer; skillware check 0 POIs); the `AS:` mentions already teach the retired form; `index-view.md` absent, `.claude/skills` symlinked; residual old-name hits are all legitimate aliases + appendix salvage. Underlying undeclared-name-dependency gap noted for the `Skw.Network` pointer-binding toolchain follow-up
- 2026-07-20 — skw-interface generalization designed (^c20260720-8u..11u): `agentos skillware`→`agentos skw`, `.skillware/`→`.skw/`, `skillware.json`→`skw.json`; recursive git-tracked `.skw/` build home at project + package scope, `.agentos/` keeps identity+runtime only; one mirrored four-key `skw.json` schema (depots/surfaces/exclude/projects) with project→package cascade; `agentos skw check` project-scope discovery default (`--skill` narrows), cross-package `dangling-dependency` payoff; recursive unit `Skw.Package` with the `Skw.* ⊃ Skill.*` naming ladder. Conceptual part captured to `Agentos.Skillware/Agendix` (+`/Skw.Package`); Impl.Req at `agentos-py/notes/live/697-skw-generalization-project-scope-impl-req.md`
- 2026-07-20 — Slice 6 (697) LANDED: `Skw.Package` minted in 107 (the recursive `.skw/`-owning unit; git-tracked, `skw.json`+optional `src/`+lock; scope-mirror schema; naming ladder stated with `Package.Skill`/`Skill.Build.Surface`/`Skill.Runnable.Surface`/`Skill.Module` as the skills-backend instances — general `Skw.*` roots reserved for a second backend; folder-vs-file grain CT) ^c20260720-13u; `Agentos.Skillware` gained the `agentos skw` toolchain + project-scope-check line and `Skw.Package` member; `Skill.Build.Surface` realization `.skillware/`→`.skw/`; `Agentos.Skillware` agendix candidate promoted (file removed); 2 benign derived-stale on the skillware skill re-blessed; depot linter 0/0
- 2026-07-20 — `Skw.Package` block CORRECTED (^c20260720-13u): removed the false "naming ladder" claiming `Skw.Package ⊃ Package.Skill` / `Skw.Module ⊃ Skill.Module` — those conflated two orthogonal models. `Skw.Package` is just a folder with a `.skw/` build home (a build-system unit); the Batchy skill-design framework (`Package.Skill`, `Skill.Module`) is a separate axis skw does not touch. Replaced with a backend-agnostic `[CT]`: a `Package.Skill` is one thing that can be a `Skw.Package`, but skw sees only sources and compiled surfaces
