# 611 — agentos-pkg Grounding Campaign

## Grounding.Abstract

- depot: `skills/agentos-pkg` (project `agentos-md`)
- caller boundary: none supplied — scope computed by supervisor
- state: `pass 4 complete — P6 attached 6/7; P4 landed nothing (wrong side of a compaction boundary), fallback P4b pending`
- coverage after pass 1: `line 1419/3235 linked` (+12), `block 130/328 grounded` (+2), `gr-density 0.5109` (+0.0058)
- coverage after pass 2: `line 1449/3240 linked` (+30), `block 137/328 grounded` (+7), `gr-density 0.5242` (+0.0133)
- coverage after pass 4: `line 1455/3240 linked` (+6), `block 137/328 grounded` (+0), `gr-density 0.5271` (+0.0029) — pass 3 attached nothing
- coverage before — two different denominators, both correct:
  - linter meter (all index lines, incl. non-kernel): `line 1407/3235 linked`, `block 128/328 grounded` (328 = coverage-eligible blocks)
  - blocks meter (kernel lines only): `gr-density 0.5051` over 2063 kernel lines / 1042 unique anchors across 329 inventoried blocks
  - the block counts differ by one because the linter excludes one block from coverage eligibility that the inventory still lists
- ungrounded surface: 170 blocks / 887 kernel lines, all inside `design/100..107-design.md` (`design/108..111`, `poi/`, `issues/` carry no zero-grounded blocks)
- readiness partition (depot-wide, after pass 1) — 2094 bullet lines:
  - `grounded` — 1054 lines already carry a trailing support reference
  - `groundable` — 69 ungrounded lines already typed; dispatchable under `::start-campaign`
  - `typing-required` — 971 ungrounded legacy untyped bodies; dispatchable only under `::start-campaign-with-typing`
  - `residue` — 0 so far; only an authorized research result may classify a body as residue
  - by file — `groundable`: 106 (41), 102 (11), 107 (8), 101 (7), 104 (1), poi/103 (1); `typing-required` concentrates in 106 (153), 104 (142), 101 (133), 100 (128), 102 (126), 107 (106), 105 (93), 103 (88)
- computed scope: clusters `C1`–`C4` below — 24 blocks / ~121 kernel lines across 4 single-session packets
- survey commands used:
  - `agentos index linter --depot agentos-md/skills/agentos-pkg --coverage all --json`
  - `agentos index blocks --depot agentos-md/skills/agentos-pkg --sort gr-density --json`
  - `git log -S'## <Block.Path>' --format='%h %ad %s' --date=short` (introduction commit per block family)
  - `agentos chatlas query --project-base agentos-project --user-contains '<Concept>' --text`
  - `agentos chatlas query --project-base agentos-project --file-write skills/agentos-pkg/design/106-design.md --text`

### Ungrounded deficit by file

| file | zero-grounded blocks | kernel lines |
|---|---|---|
| 100-design.md | 19 | 103 |
| 101-design.md | 29 | 150 |
| 102-design.md | 25 | 128 |
| 103-design.md | 13 | 73 |
| 104-design.md | 21 | 121 |
| 105-design.md | 15 | 87 |
| 106-design.md | 38 | 172 |
| 107-design.md | 10 | 53 |

Also present: 30 partially grounded blocks (`0 < gr-density < 1`) — deferred; this pass targets whole-block deficits with strong single-session hints.

## Grounding.Clusters

Selection rank prefers: coherent concept family + one dominant candidate session + git introduction date that matches that session's activity window.

### `C1` — Cold.Loading family — rank 1

- target: `design/101-design.md`
  - `Context.Loading.Path` (:72, 6 lines)
  - `Cold.Loading` (:95, 6 lines)
  - `Cold.Loading.Hook` (:106, 5 lines)
  - `Cold.Loading.Surface` (:116, 6 lines)
  - `SKILL.Loading` (:127, 5 lines)
- typing disposition: 12 `groundable` (attached in pass 1) + 16 `typing-required`
- candidate session: `918b793b73f8` (codex, last activity 2026-07-09)
- git hint: `## Cold.Loading.Hook` introduced in `5044b53` (2026-07-09, "checkpoint before 580 caret sigil execution")
- evidence hint: only 3 sessions in the whole corpus contain `Cold.Loading` in user text; one sits exactly on the introduction date
- fallback candidates: `549979e6f80a` (claude-code, 2026-07-02), `fb3b66315917` (codex, 2026-08-03)

### `C2` — Program.Hardness / executor-axis family — rank 2

- target: `design/106-design.md`
  - `Program.Hardness` (:445, 2 lines)
  - `Soft.Program` (:452, 7 lines)
  - `Agentic.Program` (:464, 7 lines)
  - `CPU.Program` (:476, 6 lines)
  - `Supervisor.Agent` (:487, 13 lines)
- typing disposition: 0 `groundable`, 34 `typing-required` — needs `::start-campaign-with-typing`
- candidate sessions: `3d91f5b30cc3` (codex, 2026-06-15), `fd6eaa31f7a2` (codex, 2026-06-15)
- git hint: `## Supervisor.Agent` introduced in `76cc466` (2026-06-15, "checkpoint before hugentics-impl-executer")
- evidence hint: `Soft.Program` appears in 9 sessions; the only two on the introduction date are both codex sessions of 2026-06-15
- note: dispatch `3d91f5b30cc3` first; `fd6eaa31f7a2` is the same-day sibling and becomes a second packet only if lines come back ambiguous

### `C3` — Line.Type vocabulary family — rank 3

- target: `design/106-design.md`
  - `Line.Type.Vocabulary` (:302, 7 lines)
  - `Line.Type::DF` (:314, 3) · `::DC` (:322, 3) · `::CT` (:330, 3) · `::RJ` (:338, 3) · `::PR` (:346, 3) · `::FR` (:354, 3) · `::EX` (:362, 3)
- typing disposition: 0 `groundable`, 28 `typing-required` — needs `::start-campaign-with-typing`
- candidate session: `27821fc60104` (claude-code, 2026-07-13)
- git hint: `## Line.Type::DF` introduced in `bb3229d` (2026-07-12, "skw v3 execution checkpoint")
- evidence hint: 12 sessions mention `Line.Type` in user text; `27821fc60104` is the only one inside the 07-12/07-13 introduction window
- fallback candidates: `4f7b47fffe9e` (2026-07-08), `9d194db7f404` (2026-07-10)
- caution: `Line.Type::GR` is already grounded and out of scope; the 7 targeted type blocks are a tight family and may share support turns — each still needs its own line-bound relationship

### `C4` — Index.Edit action family — rank 4

- target: `design/107-design.md`
  - `Index.Edit.Action` (:653, 5) · `Index.Edit.Create.Block` (:663, 5) · `Index.Edit.Append.Line` (:673, 5) · `Index.Edit.Modify.Line` (:683, 5) · `Index.Edit.Revise.Block` (:693, 5) · `Partial.Cite` (:703, 5)
- typing disposition: 0 `groundable`, 30 `typing-required` — needs `::start-campaign-with-typing`
- candidate sessions: `ade6275355cc` (codex, 2026-07-06), `549979e6f80a` (claude-code, 2026-07-02)
- git hint: `## Index.Edit.Create.Block` first appears in `0663782` (2026-07-02, "in-progress index-architecture redesign"), completed in `6ba0aa1` (2026-07-05, "Index.Edit.* action blocks + Partial.Cite (line cluster complete)")
- evidence hint: 7 sessions mention `Index.Edit`; the two spanning the 07-02..07-06 authoring window are the candidates
- note: the commit subject names the cluster as complete, so the authoring discussion is very likely one of these two sessions

## Grounding.Work

Dispatched packets persist their materialized manifest below, so packet identity survives this session and attachment can revalidate line content without re-deriving it from the worker prompt. Undispatched packets carry coordinates only until dispatch.

### `P1` manifest — dispatched pass 1

- session: `918b793b73f8f94764311d7771b25da5ed60a8e1f7db869bbe28f9a05b6634a8`
- source: `agentos-md/skills/agentos-pkg/design/101-design.md`, materialized at dispatch, all 28 lines verified anchor-free
- `hash` is the packet-local line id used in the worker result contract; `sha` is the first 12 hex of the SHA-256 of the exact line text

| hash | block | file line | sha | typed | exact content |
|---|---|---|---|---|---|
| L01 | Context.Loading.Path | 74 | `7be32873f4ce` | no | `` - `Context.Loading.Path` is the tiered path by which context enters an agent, ordered from guaranteed-at-cold to pulled-on-demand `` |
| L02 | Context.Loading.Path | 75 | `607c7c9439a4` | no | `- each tier is a distinct loading mechanism with its own guarantee level; a later tier becomes reachable only once earlier tiers have loaded what it needs` |
| L03 | Context.Loading.Path | 76 | `6025365d4fe6` | no | ``- tier 1 `Cold.Loading` — context guaranteed present from a cold start`` |
| L04 | Context.Loading.Path | 77 | `c37ccf4e0f0d` | no | ``- tier 2 `SKILL.Loading` — context that arrives whole when a skill is loaded`` |
| L05 | Context.Loading.Path | 78 | `5291ffab2a55` | no | ``- tier 3 `Dynamic.Loading` — context pulled selectively, on demand`` |
| L06 | Context.Loading.Path | 79 | `43d9b3d62773` | no | `- the path bootstraps itself: each tier loads the keys and surfaces the next tier needs to act` |
| L07 | Cold.Loading | 97 | `2fc3d402e551` | no | ``- `Cold.Loading` is the `Context.Loading.Path` tier guaranteed present from a cold start, before the agent takes any action`` |
| L08 | Cold.Loading | 98 | `69a37923769d` | no | ``- it loads through the `Cold.Loading.Hook`s an agent always sees on entry — skill descriptions and `AGENTS.md` `` |
| L09 | Cold.Loading | 99 | `10148ffe7b04` | no | ``- the guarantee comes from redundant placement: the same context is wired into many `Context.Hook`s so the system cannot miss it`` |
| L10 | Cold.Loading | 100 | `536b7886c1ea` | no | `- it is the bootstrap tier — it carries the minimal vocabulary and routing keys the later tiers need to act at all` |
| L11 | Cold.Loading | 101 | `acf3f163e8bf` | no | ``- only `Workflow.Neutral.Skill` orientation belongs here — non-steering, safe to always load; its cost is paid every session, so it stays minimal`` |
| L12 | Cold.Loading | 102 | `415a8faed04c` | CT | ``- [CT] `Cold.Loading` surfaces are linter-controlled because they shape every agent run before task-specific routing begins`` |
| L13 | Cold.Loading.Hook | 108 | `00f982efb02f` | DF | ``- [DF] `Cold.Loading.Hook` is a `Context.Hook` that the harness loads automatically before the agent acts`` |
| L14 | Cold.Loading.Hook | 109 | `77ca27845dbf` | CT | ``- [CT] it injects a `Cold.Loading.Surface` `` |
| L15 | Cold.Loading.Hook | 110 | `42820282978a` | EX | ``- [EX] project-root `AGENTS.md` is a `Cold.Loading.Hook` when the harness reads it before the agent acts`` |
| L16 | Cold.Loading.Hook | 111 | `46a3b7a50a7e` | EX | ``- [EX] skill descriptions are `Cold.Loading.Hook`s when the harness advertises them before skill selection`` |
| L17 | Cold.Loading.Hook | 112 | `23bb71c957b7` | CT | `- [CT] its loaded content is linter-controlled because every session receives it` |
| L18 | Cold.Loading.Surface | 118 | `72a9969fcabe` | DF | ``- [DF] `Cold.Loading.Surface` is a surface whose content is guaranteed present at `Cold.Loading` `` |
| L19 | Cold.Loading.Surface | 119 | `899a6527ddd4` | CT | `- [CT] it is identified by harness loading behavior, not only by file name or path` |
| L20 | Cold.Loading.Surface | 120 | `0767286f3b4c` | EX | ``- [EX] a project-root `AGENTS.md` loaded before the agent acts is a `Cold.Loading.Surface` `` |
| L21 | Cold.Loading.Surface | 121 | `4548fc8695b8` | CT | ``- [CT] a `Context.Hook` is the injection mechanism; `Cold.Loading.Surface` is the loaded content surface`` |
| L22 | Cold.Loading.Surface | 122 | `adf0595c6bc9` | CT | ``- [CT] `Package.Driver` content may be projected into a `Cold.Loading.Surface` when the package must be reachable from cold`` |
| L23 | Cold.Loading.Surface | 123 | `908dcb1738ac` | CT | ``- [CT] `Cold.Loading.Surface`s are linter-controlled because every session pays their context cost`` |
| L24 | SKILL.Loading | 129 | `50f06bd3b665` | no | ``- `SKILL.Loading` is the `Context.Loading.Path` tier that arrives whole when a skill is loaded`` |
| L25 | SKILL.Loading | 130 | `18ab3606be9c` | no | ``- the `SKILL.md` file is its unit — the single discrete loading step between `Cold.Loading` and `Dynamic.Loading` `` |
| L26 | SKILL.Loading | 131 | `b551d1f3cf2e` | no | ``- it is atomic: loading a skill brings its entire `SKILL.md` at once, all-or-nothing, with no finer selection`` |
| L27 | SKILL.Loading | 132 | `43a81116f11c` | no | ``- whatever an author wants present the moment a skill is in context belongs in its `SKILL.md` `` |
| L28 | SKILL.Loading | 133 | `019a2dc4b392` | no | ``- it sets up the next tier: the keys and routes loaded here are what `Dynamic.Loading` selects against`` |

Anchorable subset: L12–L23 (12 typed lines). L01–L11 and L24–L28 are untyped legacy lines; `agentos chatlas anchory` rejects `--line-content` that is not a typed Index line, so they cannot receive a line-bound `Support.Set` until they are typed through the normal verbatim gate. This is a scope discovery from pass 1, not a research failure.

| packet | cluster | session | lines | worker model class | state |
|---|---|---|---|---|---|
| `P1` | C1 | `918b793b73f8` | 28 (12 anchorable) | medium / medium reasoning | `attached` — 12/12 anchorable lines supported and attached; 16 untyped lines out of scope |
| `P2` | C2 | `3d91f5b30cc3` | 35 | medium / medium reasoning | `surveyed` |
| `P3` | C3 | `27821fc60104` | 28 | medium / medium reasoning | `ambiguous` — 28/28, wrong session (bad git hint) |
| `P3b` | C3 | `4f7b47fffe9e` | 28 | medium / medium reasoning | `attached` — 25 migrated, 3 `ambiguous` |
| `P5` | C5 | `02161ec9eb99` | 34 | medium / medium reasoning | `ambiguous` — 32/34; 2 proposals rejected at supervisor gate |
| `P5b` | C5 | `6f7f95adf906` | 7 (QA.Space) | medium / medium reasoning | `ambiguous` — 7/7 |
| `P6` | C6 | `918b793b73f8` | 7 | medium / medium reasoning | `attached` — 6 supported and attached, 1 `ambiguous` |
| `P4` | C4 | `4f7b47fffe9e` | 30 | medium / medium reasoning | `ambiguous` — 30/30; all typed confidently, none supported |
| `P4` | C4 | `ade6275355cc` | 30 | medium / medium reasoning | `surveyed` |

### `P1` attachment record — pass 1 closed

All 12 previews returned no `equivalent_anchors` and no `exact_line_equivalent_anchors`; each anchor is freshly minted and line-bound. Line `Line.Type + body` preserved verbatim; only a trailing `^anchor` was appended.

| hash | file line | anchor | support members (user turns, relevance order) |
|---|---|---|---|
| L12 | 102 | `^c20260709-33u` | r120 |
| L13 | 108 | `^c20260709-34u` | r424, r416, r432 |
| L14 | 109 | `^c20260709-35u` | r424, r378, r432 |
| L15 | 110 | `^c20260709-36u` | r424, r416, r432 |
| L16 | 111 | `^c20260709-37u` | r424, r416, r432 |
| L17 | 112 | `^c20260709-38u` | r120, r424, r432 |
| L18 | 118 | `^c20260709-39u` | r378, r416, r432 |
| L19 | 119 | `^c20260709-40u` | r378, r432 |
| L20 | 120 | `^c20260709-41u` | r378, r432 |
| L21 | 121 | `^c20260709-42u` | r378, r424, r432 |
| L22 | 122 | `^c20260709-43u` | r378, r416, r432 |
| L23 | 123 | `^c20260709-44u` | r120, r378, r432 |

All members are in session `918b793b73f8…6634a8`. Block outcome in `design/101-design.md`: `Cold.Loading.Hook` 5/5 grounded, `Cold.Loading.Surface` 6/6 grounded, `Cold.Loading` 1/6, `Context.Loading.Path` 0/6 and `SKILL.Loading` 0/5 (all their lines untyped).

### `P3` manifest — dispatched pass 2 (type-and-ground migration)

- authority: `Legacy.Type.Migration.Exception`, granted by `::start-campaign-with-typing C3`
- session: `27821fc601044870d33e059c2617cc83a0632c46c7c1f94e7ec3a4bebc418726` (claude-code, last activity 2026-07-13)
- source: `agentos-md/skills/agentos-pkg/design/106-design.md`, materialized at dispatch
- all 28 bodies verified: untyped, anchor-free, `typing-required`
- vocabulary supplied to worker: `DF`, `DC`, `CT`, `RJ`, `PR`, `FR`, `EX`, `GR`
- out of scope: `Line.Type::GR` (:370) is already typed and already grounded

| hash | block | file line | sha | exact legacy body |
|---|---|---|---|---|
| M01 | Line.Type.Vocabulary | 304 | `6d4297adecde` | `- `Line.Type.Vocabulary` is the controlled set of `Line.Type`s an index uses — small, curated, soft (`Concept.Hardness`); extensible, not a hard enum` |
| M02 | Line.Type.Vocabulary | 305 | `4e5f8bc8265c` | `- each type is a verb on the `Design.Space` — types sort by how a line acts on the space: collapsing it, describing it, or declaring it open` |
| M03 | Line.Type.Vocabulary | 306 | `c28442cab37f` | `- a type earns its place when a recurring line-act has no home; a type that attracts filler is a smell` |
| M04 | Line.Type.Vocabulary | 307 | `b65c155b7fe1` | `- each type creates a validation point: a typed line must perform its act — a constraint line must constrain something; a typed line that performs nothing is mistyped filler` |
| M05 | Line.Type.Vocabulary | 308 | `96b6c4540840` | `- the vocabulary is the fence of the index: index content is what the vocabulary can express — a line that can take no type belongs elsewhere; developing the vocabulary is deciding what the index is for` |
| M06 | Line.Type.Vocabulary | 309 | `66daf9d17a42` | `- scope widens only by widening the vocabulary — a visible, gated act, instead of line-by-line scope creep` |
| M07 | Line.Type.Vocabulary | 310 | `1c9c1e912dc4` | `- calibration: type the live index against a candidate vocabulary and inspect what remains untyped — each residue is a discussion: out of the index, or a vocabulary extension` |
| M08 | Line.Type::DF | 316 | `d59f9540c069` | `- `Line.Type::DF` marks a definition — the line fixes what a name means` |
| M09 | Line.Type::DF | 317 | `5f44dd67b7b7` | `- validation point: the line must bind a name to a meaning; a `DF` that introduces no name is mistyped` |
| M10 | Line.Type::DF | 318 | `293a319dddfc` | `- lint: two `DF` lines binding the same name to different meanings, and a block whose first line is not a `DF`` |
| M11 | Line.Type::DC | 324 | `e23d57825b88` | `- `Line.Type::DC` marks a decision — the line pins a `Design.Variable` to a value` |
| M12 | Line.Type::DC | 325 | `63f97afee54d` | `- validation point: the line must name what was decided and the value it took; a `DC` that pins nothing is mistyped` |
| M13 | Line.Type::DC | 326 | `b3aec73fc629` | `- lint: two `DC` lines pinning the same variable to different values is a contradiction to surface` |
| M14 | Line.Type::CT | 332 | `8e1d6c42e6a1` | `- `Line.Type::CT` marks a constraint — the line bounds a `Design.Variable` to a subset without picking a value` |
| M15 | Line.Type::CT | 333 | `3e93a09d2333` | `- validation point: the line must exclude something; a `CT` that rules nothing out is filler` |
| M16 | Line.Type::CT | 334 | `abe74a7d6367` | `- lint: constraints whose intersection is empty, and a `CT` silently violated by a later `DC`` |
| M17 | Line.Type::RJ | 340 | `4077646bc4e4` | `- `Line.Type::RJ` marks a rejection — the line excludes a considered alternative` |
| M18 | Line.Type::RJ | 341 | `a1e0785813b3` | `- validation point: the line must name the rejected alternative, preferably with the reason` |
| M19 | Line.Type::RJ | 342 | `eaf72c188d39` | `- lint: a rejected alternative later reintroduced without a new touch` |
| M20 | Line.Type::PR | 348 | `442ad39f1fbe` | `- `Line.Type::PR` marks a principle — a generative orientation that spawns constraints across many variables` |
| M21 | Line.Type::PR | 349 | `9608c40b646f` | `- validation point: the line must orient decisions beyond one variable; a `PR` scoped to a single variable is a `CT`` |
| M22 | Line.Type::PR | 350 | `00b1e0b3a942` | `- lint: decisions or constraints that run against a standing principle` |
| M23 | Line.Type::FR | 356 | `ccd66534e1d6` | `- `Line.Type::FR` marks a free declaration — the user explicitly leaves a `Design.Variable` agent-owned` |
| M24 | Line.Type::FR | 357 | `e9a48df08736` | `- validation point: the line must name what is left open; freedom is a touched act, not an omission` |
| M25 | Line.Type::FR | 358 | `d950d5e1f9d5` | `- lint: a `FR` variable later constrained without retiring the declaration` |
| M26 | Line.Type::EX | 364 | `99f438417a32` | `- `Line.Type::EX` marks an example — the line illustrates another line's claim with a concrete case` |
| M27 | Line.Type::EX | 365 | `ac78d61f0c61` | `- validation point: the line must exemplify something specific; an example that illustrates no claim is filler` |
| M28 | Line.Type::EX | 366 | `80dee507aa9e` | `- lint: an example inconsistent with the constraints and decisions it illustrates` |

In-depot precedent supplied as calibration (not as an answer): the already-typed `Line.Type::GR` block at :370 has the same three-line shape and reads `[DF]` / `[CT]` / `[DC]`. The worker was required to justify each classification against the vocabulary and against user evidence independently, and to return `residue` rather than pattern-match the precedent.

### `P5` manifest — dispatched pass 3 (ordinary typed grounding)

- authority: ordinary `::start-campaign C5` — no typing authority; all 34 lines already `groundable`
- session: `02161ec9eb991d3811af60919194f86b715059aff583e42979dbf4e627738cf7` (codex, last activity 2026-07-30)
- source: `agentos-md/skills/agentos-pkg/design/106-design.md`, all 34 lines verified typed and anchor-free
- nomination — two independent signals, neither of them a git date (per the pass-2 methodology correction):
  1. **anchor neighbourhood**: the already-grounded blocks interleaved with this family (`User.Model.Space`, `Touch.Authority.Surface`, `Open.Inference`) carry `c20260729-*` anchors that resolve to this exact session
  2. **phrase query**: `--user-contains "Open.Space"` returns 10 sessions corpus-wide, and this session is among them
- sibling candidate: `edb7847bcba1` (codex, 2026-07-29)

| hash | block | file line | sha | exact typed line |
|---|---|---|---|---|
| S01 | QA.Space | 84 | `72462a0a3bae` | `- [DF] `QA.Space` is the implicit space of questions and possible answers that define a topic, artifact, task, source, or user model` |
| S02 | QA.Space | 85 | `2176623dcd90` | `- [PR] alignment is the progressive conditioning of a `QA.Space` through agent/user interaction` |
| S03 | QA.Space | 86 | `5efb07ce7bf9` | `- [DC] a `QA.Space` is a model, not a requirement that agents mechanically enumerate every question and answer` |
| S04 | QA.Space | 87 | `c7cb00673ca9` | `- [DC] any state of a `QA.Space` can be described as answer regions that are open, constrained, fixed, touched, or untouched` |
| S05 | QA.Space | 88 | `c349ce24d972` | `- [PR] the touched/open ratio is the control surface: the user tightens control by constraining more of the space, and delegates automation by leaving space open` |
| S06 | QA.Space | 89 | `8b5802fe4785` | `- [DC] hugentic surfaces nest over `QA.Space`: the `Chat.Surface` records it, the index digests it, and implementation surfaces realize it` |
| S07 | QA.Space | 90 | `402e40f91e59` | `- [PR] `QA.Space` is never required complete to proceed; the agent works `Open.Space` to keep moving, and alignment catches up` |
| S08 | Work.Space | 107 | `e1a9ace80fbd` | `- [DF] `Work.Space` is a `QA.Space` about the work at hand` |
| S09 | Work.Space | 108 | `4e2bdf7eb6a7` | `- [DC] it models what is true, needed, selected, excluded, available, blocked, open, constrained, or fixed in the work` |
| S10 | Work.Space | 109 | `4bdc0697475d` | `- [PR] agents act in the `Open.Space` of `Work.Space` and obey the `Constrained.Space` of `Work.Space`` |
| S11 | Work.Space | 110 | `5a8dcf1b2569` | `- [CT] touch is not an action gate for `Work.Space`; openness governs whether the agent decides` |
| S12 | Source.Space | 116 | `c41b5ec36148` | `- [DF] `Source.Space` is a `QA.Space` about a source surface or source artifact` |
| S13 | Source.Space | 117 | `50a4d90c2ee3` | `- [DC] it can model whatever matters about a source: what it says, contains, implies, connects to, supports, contradicts, enables, or raises as a point of interest` |
| S14 | Source.Space | 118 | `78a872dab7fa` | `- [CT] source-local signals do not by themselves establish current `User.Model.Space` claims unless they are grounded through a user-touched process` |
| S15 | Source.Space | 119 | `28c1ad900e5c` | `- [PR] source surfaces feed alignment by surfacing candidate questions and points of interest for later touch` |
| S16 | Design.Space | 125 | `7fb9389a2c69` | `- [DF] `Design.Space` is a `QA.Space` about artifact design` |
| S17 | Design.Space | 126 | `fbcce78522f3` | `- [DC] it scopes `QA.Space` to design questions whose answers shape an artifact` |
| S18 | Design.Space | 127 | `c82bd30477df` | `- [DC] it is a vector space of `Design.Variable`s; each variable one axis, and `Design.Target.Model` is a point in this space` |
| S19 | Touched.Space | 169 | `dd13d519d43f` | `- [DF] `Touched.Space` is the region of a `QA.Space` carrying `User.Touched` evidence` |
| S20 | Touched.Space | 170 | `482625614102` | `- [DC] it is the part of the modeled space that the hugentic process has reached` |
| S21 | Touched.Space | 171 | `9adb751ef43b` | `- [DC] the index is its primary alignment surface, but not the only one; the `Chat.Surface` is another hugentic surface that holds touch` |
| S22 | Touched.Space | 172 | `bbe65965fc29` | `- [CT] a touched region may be open or constrained; touch means engaged, not decided` |
| S23 | Open.Space | 188 | `3012a5aa5743` | `- [DF] `Open.Space` is the region of a `QA.Space` where meaningful agent choice remains` |
| S24 | Open.Space | 189 | `feab36267551` | `- [DC] in `Open.Space`, the agent makes its own decisions to act: coherent, never random, and provisional` |
| S25 | Open.Space | 190 | `610b4edd7e72` | `- [CT] `Open.Space` is orthogonal to touch: it may be untouched, or it may be touched by an explicit free declaration (`FR`)` |
| S26 | Open.Space | 191 | `5388ffcc8c76` | `- [CT] consequences logically entailed by constraints are not open; the agent may fail to derive them, but is not free to decide against them` |
| S27 | Open.Space | 192 | `ecc823115c30` | `- [DC] open resolutions become directive constraints only once touched` |
| S28 | Constrained.Space | 211 | `53e7de882729` | `- [DF] `Constrained.Space` is the region of a `QA.Space` where possible answers have been narrowed below total freedom` |
| S29 | Constrained.Space | 212 | `bbd3ab4d7c21` | `- [DC] constraint can come from user directives, grounded arguments, formal implications, code reality, physical reality, or consequences of prior constraints` |
| S30 | Constrained.Space | 213 | `610001d43c4f` | `- [CT] in `Constrained.Space`, the agent does not choose outside the remaining valid answer region` |
| S31 | Constrained.Space | 214 | `4f7c8e8ace26` | `- [PR] constraint strength varies; `Fixed.Space` is the maximally constrained endpoint` |
| S32 | Fixed.Space | 220 | `350e8fcb19ff` | `- [DF] `Fixed.Space` is the region of `Constrained.Space` narrowed to one valid answer` |
| S33 | Fixed.Space | 221 | `b8912271cc60` | `- [DC] it is the 0%-free endpoint of the freedom axis` |
| S34 | Fixed.Space | 222 | `620b692dd5c3` | `- [CT] a fixed region is not a decision point for the agent; the agent's job is to recognize and obey the fixed answer` |

Resolving a neighbouring anchor back to its session is the strongest nomination method found so far in this campaign — it uses grounding already verified by an earlier pass rather than commit timing. Preferred for remaining clusters wherever a grounded block sits adjacent to an ungrounded one.

### `P6` manifest — dispatched pass 4 (ordinary typed grounding)

- authority: ordinary grounding; all 7 lines already `groundable`, no typing authority consumed
- session: `918b793b73f8` (codex, 2026-07-09) — the session that landed 12/12 in pass 1
- source: `design/101-design.md`, block `Agentos.AGENTS.Section` (:83), all 7 verified typed and anchor-free
- nomination: `--user-contains "Agentos.AGENTS.Section"` returns exactly 2 sessions corpus-wide (this one and `27821fc60104`), corroborated by verified prior grounding in the same file
- fallback: `27821fc60104`

| hash | file line | sha | exact typed line |
|---|---|---|---|
| G01 | 85 | `2bb76551c1f0` | `- [DF] `Agentos.AGENTS.Section` is the structured Agentos section inside an `AGENTS.md` `Cold.Loading` surface` |
| G02 | 86 | `4e4356cd69c4` | `- [DC] its canonical section heading is `## Agentos`` |
| G03 | 87 | `f6830ecc4275` | `- [CT] it may carry any Agentos-managed context agents should receive from `AGENTS.md`, including configuration, package-driver hints, subsystem routing, and local policy` |
| G04 | 88 | `3d95bcdd560a` | `- [CT] configuration is a primary use, not the boundary of the section` |
| G05 | 89 | `a11f5138f930` | `- [DC] nested `AGENTS.md` surfaces override parent `Agentos.AGENTS.Section` values by nearest-scope precedence` |
| G06 | 90 | `7f7cc02aa22c` | `- [CT] `Agentos.AGENTS.Section` is linter-controlled because it participates in `Cold.Loading`, where accidental or conflicting context is paid by every session` |
| G07 | 91 | `21c6a217dbe5` | `- [PR] subsections should be named by subsystem, so each package can own and lint its own Agentos-facing content` |

### `P4` manifest — dispatched pass 4 (type-and-ground migration)

- authority: `Legacy.Type.Migration.Exception`, granted by `::start-campaign-with-typing`
- session: `4f7b47fffe9e` (claude-code, 2026-07-08) — the session that landed 25/25 in pass 2
- source: `design/107-design.md`, all 30 verified untyped and anchor-free
- nomination: `--user-contains "Index.Edit.Action"` returns exactly 2 sessions corpus-wide (this one and `9d194db7f404`); commit `6ba0aa1` (2026-07-05) treated as weak corroboration only
- known limitation: this session is `/compact`-continued; content predating the compaction boundary is unqueryable, which cost 3 lines in pass 2
- fallback: `9d194db7f404`
- excluded from scope: `Partial.Cite`'s `### meta` line (`- aliases: \`Partial.Name\``, :713) is a `Kernel.Block.Meta` line, not a kernel line

| hash | block | file line | sha | exact legacy body |
|---|---|---|---|---|
| N01 | Index.Edit.Action | 655 | `dc2f24757857` | `- `Index.Edit.Action` is the small set of moves that edit the index — each a named action chosen by the case that calls for it` |
| N02 | Index.Edit.Action | 656 | `00b340beed49` | `- the moves: `Index.Edit.Create.Block`, `Index.Edit.Append.Line`, `Index.Edit.Modify.Line`, `Index.Edit.Revise.Block`` |
| N03 | Index.Edit.Action | 657 | `50eee9176eb4` | `- two tempos: hot capture (append during the `Alignment.Loop`) and cold consolidation (a maintenance pass over accumulated lines, where `Index.Edit.Create.Block` and `Index.Edit.Revise.Block` mostly live)` |
| N04 | Index.Edit.Action | 658 | `879b6ba86eb2` | `- the bias is the lowest-cost action that captures the aligned content (`Writing.Friction.Reduction`)` |
| N05 | Index.Edit.Action | 659 | `24b2c3fa2cad` | `- every action is user-gated and `Verbatim.User.Gated` — it is the index` |
| N06 | Index.Edit.Create.Block | 665 | `64dbfff09c78` | `- `Index.Edit.Create.Block` is the `Index.Edit.Action` of adding a new named concept block to the index` |
| N07 | Index.Edit.Create.Block | 666 | `2ab91a5b92fb` | `- the case: a genuinely new concept appears — coined by the user, or revealed when accreted lines show a pattern during consolidation` |
| N08 | Index.Edit.Create.Block | 667 | `ef9981d52c81` | `- the naming hint: when lines need to be referenced — cited from elsewhere, or pointed at as a group — they need a name; referenceability is what earns a block` |
| N09 | Index.Edit.Create.Block | 668 | `35f1a7685cb4` | `- it is the higher-cost action — a new frame, a router entry, a placement decision; prefer `Index.Edit.Append.Line` unless the concept is genuinely new` |
| N10 | Index.Edit.Create.Block | 669 | `1fed15dfd60c` | `- it mostly lives in the cold tempo, extracted from accumulated lines, not coined hot` |
| N11 | Index.Edit.Append.Line | 675 | `3f6a75621c47` | `- `Index.Edit.Append.Line` is the `Index.Edit.Action` of adding a `Kernel.Line` to the nearest coherent block — the default index edit` |
| N12 | Index.Edit.Append.Line | 676 | `504fc29fbbec` | `- it is the lowest-cost capture path, which is why it is the first beat: drop the line, do not stop to architect a block` |
| N13 | Index.Edit.Append.Line | 677 | `e82319de4020` | `- landing selection picks the nearest coherent frame — a concept block, its appendix, or a namespace for subsystem-level lines` |
| N14 | Index.Edit.Append.Line | 678 | `45b2e6a6ef1f` | `- it is a load-then-word operation: select the block, bring it into context, then word the line against what it already says` |
| N15 | Index.Edit.Append.Line | 679 | `6ab3f67763ef` | `- the block defines the wording — terse, framed, non-redundant — never generated blind and attached` |
| N16 | Index.Edit.Modify.Line | 685 | `12ce75987632` | `- `Index.Edit.Modify.Line` is the `Index.Edit.Action` of refining or correcting an existing `Kernel.Line`, keeping its block` |
| N17 | Index.Edit.Modify.Line | 686 | `869ec5cff4ae` | `- the case: a statement already in the block is wrong, imprecise, or superseded by aligned discussion` |
| N18 | Index.Edit.Modify.Line | 687 | `012aa31c5be3` | `- like `Index.Edit.Append.Line` it is load-then-word — the block and the existing line both frame the new wording` |
| N19 | Index.Edit.Modify.Line | 688 | `d47e9de27fdd` | `- it is `Verbatim.User.Gated` — the replacement wording is approved before commit` |
| N20 | Index.Edit.Modify.Line | 689 | `9ba320c3e952` | `- prefer it over stacking a contradicting append: a corrected line beats two lines that disagree` |
| N21 | Index.Edit.Revise.Block | 695 | `82c8ee240410` | `- `Index.Edit.Revise.Block` is the `Index.Edit.Action` of restructuring a block whose frame no longer holds its accreted lines` |
| N22 | Index.Edit.Revise.Block | 696 | `da464b0c414a` | `- the case: lines have piled up past the block's coherence — it needs reorder, split, or promotion of lines into the appendix` |
| N23 | Index.Edit.Revise.Block | 697 | `9419b8f08680` | `- it is a consolidation move, cold tempo — done with the warm context gathered while chatting, not hot` |
| N24 | Index.Edit.Revise.Block | 698 | `504aa1055445` | `- it may spawn `Index.Edit.Create.Block` when a promoted cluster of lines earns its own name` |
| N25 | Index.Edit.Revise.Block | 699 | `b45291df6395` | `- it preserves the lines — restructuring moves and reframes them, it never discards aligned content` |
| N26 | Partial.Cite | 705 | `1d6e9af0a3d9` | `- `Partial.Cite` is using a shortened form of a `Dotted.Name` when it still resolves unambiguously` |
| N27 | Partial.Cite | 706 | `d723e3b68d4f` | `- legal when the short form has no collision in the engaged indexes, or the full name was already cited in the same document` |
| N28 | Partial.Cite | 707 | `a66c8e4ef9d2` | `- it is pure ergonomics — `Append.Line` for `Index.Edit.Append.Line` once the family is established` |
| N29 | Partial.Cite | 708 | `dfcf79614e5a` | `- the canonical name is always the full path; the router and block headings carry it — shortening is reader-facing convenience only` |
| N30 | Partial.Cite | 709 | `9e55ef946cd3` | `- it is the authoring side of `Fuzzy.Dotted.Name`: resolution tolerates approximation, `Partial.Cite` deliberately relies on it` |
| N31 | Partial.Cite | 713 | `fb003b80935e` | `- aliases: `Partial.Name`` |

Both packets dispatched concurrently against different files and different sessions, so neither can interfere with the other's relocation or attachment.

Contingent packets (dispatch only on ambiguity in the parent packet): `P2b` → `fd6eaa31f7a2` (C2), `P4b` → `549979e6f80a` (C4), `P3b` → `4f7b47fffe9e` (C3), `P1b` → `549979e6f80a` (C1).

## Grounding.Log

- 2026-08-06 — survey pass complete; no agents spawned, no transcripts loaded, no anchors minted, no Index lines edited.
- note: `agentos chatlas query` content filters cost ~40s per call against this corpus; survey used 6 such calls.
- 2026-08-06 — `::start-campaign Cold.Loading`: pass 1 opened on C1. P1 materialized (manifest above) and dispatched to one read-only research agent at the medium model class, medium reasoning. No escalation.
- 2026-08-06 — P1 round-1 result returned 15 `supported` / 13 `ambiguous`. Two structural rejections at the supervisor gate, both rework rather than research failure:
  - `--line-content` requires a typed Index line; L08 is untyped, so it dropped to `ambiguous`. Under the module's current contract this is a `typing-required` classification, not an exclusion: L01–L11 and L24–L28 remain eligible through `::start-campaign-with-typing`.
  - proposed member sets included assistant and apply-patch turns; `agentos chatlas anchory preview` rejected `turn-r122` as unavailable. Anchor members must be resolvable user turns. Requeued to the same worker with the user-turn constraint instead of the supervisor inspecting transcripts to repair the sets.
- 2026-08-06 — report hardened after review: dispatched packets now persist a materialized manifest (exact content + sha12 + typed marker), the recorded linter command carries `--json`, and the two coverage denominators are labeled.
- 2026-08-06 — P1 round-2 result: all 12 anchorable lines `supported` with user-turn-only member sets. All 12 passed `agentos chatlas anchory preview` with zero equivalence collisions; registered and attached. Focused lint of `design/101-design.md`: **0 errors**.
- 2026-08-06 — attachment raised 12 new `Project.Line.Issue.Context.Missing` warnings (no `Issue.I####` edition context on the new line records). This class is depot-wide and pre-existing at ~6971 instances, so the new lines match the depot's current convention rather than regressing it. Flagged, not fixed — attaching Issue identities is a separate edition-context decision.
- 2026-08-06 — pass 1 closed. Coverage `1407→1419` lines linked, `128→130` blocks grounded, gr-density `0.5051→0.5109`.
- 2026-08-06 — module contract updated mid-campaign to add `Legacy.Type.Migration.Exception` and `::start-campaign-with-typing`. Report re-derived against the new model: readiness partition added to `Grounding.Abstract`, typing disposition added per cluster, and the earlier conclusion that `C2`/`C3`/`C4` were "retired" reversed — they are `typing-required`, not unreachable. No attached support was affected; pass 1 was an ordinary typed-line campaign and remains valid under the new contract.

- 2026-08-06 — `::start-campaign-with-typing C3`: `Legacy.Type.Migration.Exception` granted for cluster C3. `P3` dispatched against `27821fc60104` and returned **28/28 `ambiguous`** — that session contains no user turn touching this material. Nothing typed, nothing attached; correct honest outcome, not a worker failure.
- 2026-08-06 — **supervisor error identified**: `P3`'s session was nominated from a git date. Commit `bb3229d` (2026-07-12) is a *checkpoint* commit ("worktree as found"), so it dates the commit, not the authoring. Re-nomination by content instead of date: `--user-contains "Line.Type.Vocabulary"` returns exactly 2 sessions corpus-wide (`4f7b47fffe9e`, `9d194db7f404`) and `--user-contains "validation point"` returns 3; `27821fc60104` appears in neither. **Methodology correction for remaining clusters: nominate on distinctive line phrases in user text; treat checkpoint-commit dates as weak evidence only.**
- 2026-08-06 — `P3b` dispatched to `4f7b47fffe9e`: 25/28 `supported` with type classifications, 3 `ambiguous` (M01–M03, content predates that session's post-`/compact` queryable window; sibling `9d194db7f404` suggested).
- 2026-08-06 — migration gate passed for all 25: vocabulary code valid, no pre-existing type prefix, no pre-existing anchor, prefix-only delta verified by reconstruction, and the 3 ambiguous lines verified untouched. All 25 previews returned zero `equivalent_anchors` and zero `exact_line_equivalent_anchors` — **a typed candidate's identity does not collide with any existing anchor**, resolving the open question raised before this pass.
- 2026-08-06 — type prefix and trailing anchor landed as one write per line. Body preservation proven against git HEAD: 25 removed / 25 added, and every added line reduces to an exact removed body once prefix and anchor are stripped. Focused lint of `design/106-design.md`: **0 errors**.
- 2026-08-06 — pass 2 closed. All 7 `Line.Type::*` blocks now 1.000 grounded; `Line.Type.Vocabulary` 4/7 (its 3 remaining lines are the `ambiguous` M01–M03). Coverage `1419→1449` lines, `130→137` blocks, gr-density `0.5109→0.5242`.
- 2026-08-06 — independent classification converged on the `Line.Type::GR` precedent shape (`DF`/`CT`/`DC`) for all 7 type blocks. Worth noting as a possible precedent-anchoring risk rather than pure convergence, though the worker supplied per-line `why-type` reasoning and the shape is what the blocks' own content implies.

### `P3b` attachment record — pass 2 closed

| hash | line | type | anchor | support (user turns) |
|---|---|---|---|---|
| M04 | 307 | PR | `^c20260707-9u` | d6e9b729, e4557134 |
| M05 | 308 | PR | `^c20260707-10u` | a28776a1, a05fcd6c |
| M06 | 309 | CT | `^c20260707-11u` | a28776a1, a05fcd6c |
| M07 | 310 | DC | `^c20260707-12u` | a28776a1, a05fcd6c |
| M08 | 316 | DF | `^c20260708-21u` | 30fa56dc, 894cdf8a |
| M09 | 317 | CT | `^c20260708-22u` | 30fa56dc, 894cdf8a |
| M10 | 318 | DC | `^c20260708-23u` | 30fa56dc, 894cdf8a |
| M11–M13 | 324–326 | DF/CT/DC | `^c20260707-13u`…`-15u` | d6e9b729, e4557134 |
| M14–M16 | 332–334 | DF/CT/DC | `^c20260707-16u`…`-18u` | d6e9b729, e4557134 |
| M17–M19 | 340–342 | DF/CT/DC | `^c20260707-19u`…`-21u` | d6e9b729, e4557134 |
| M20–M22 | 348–350 | DF/CT/DC | `^c20260707-22u`…`-24u` | d6e9b729, e4557134 |
| M23–M25 | 356–358 | DF/CT/DC | `^c20260707-25u`…`-27u` | d6e9b729, e4557134 |
| M26–M28 | 364–366 | DF/CT/DC | `^c20260707-28u`…`-30u` | a28776a1, a05fcd6c |

Unresolved, left untyped and untouched: `M01` (:304), `M02` (:305), `M03` (:306) — `Line.Type.Vocabulary`'s first three lines. Next candidate session `9d194db7f404`.

Note on shared support: M11–M25 share one member pair. Each line still carries its own line-bound anchor over its own distinct content, per `Grounding.Work.Packet` rules. The RJ/PR/FR definitions rest on the user accepting a converged five-type list rather than discussing each type individually — legitimate acceptance under the worker contract, but the weakest support in this pass and the first place to look if these lines are ever disputed.

- 2026-08-06 — `::start-campaign C5` (ordinary typed grounding, 34 `groundable` lines). `P5` dispatched to `02161ec9eb99`, nominated by **anchor neighbourhood** — the already-grounded blocks interleaved with this family resolve to that session — plus an `Open.Space` phrase hit. Returned 32/34 `ambiguous`.
- 2026-08-06 — **supervisor rejected the 2 `supported` proposals** (S10, S11, `Work.Space`). Both rested on a single user turn that the worker's own justification concedes predates the coining of `Work.Space` and `Constrained.Space`. A semantically adjacent statement from an earlier conceptual stage is not support for this line's content, and both lines leaning on one turn is the shared-support failure mode the packet explicitly warned against. Nothing attached. Coverage unchanged.
- 2026-08-06 — **the anchor-neighbourhood nomination method failed here, and the failure is informative**: adjacency in the file is not evidence of shared authorship. These blocks are ungrounded *precisely because* they came from a different session than their already-grounded neighbours. Method downgraded from "strongest available" to "one signal among several — corroborate with a phrase query before dispatch."
- 2026-08-06 — re-nomination by user-text phrase, corpus-wide: `Work.Space` **0 sessions**, `Source.Space` **0**, `Design.Space` **0**, `Constrained.Space` **0**, `Fixed.Space` **0**, `QA.Space` **exactly 1** (`6f7f95adf906`). `P5b` dispatched there for the 7 `QA.Space` lines: 7/7 `ambiguous` — the session's only `QA.Space` occurrences are an auto-generated compaction summary and an agent-authored re-derivation, neither user-authored.
- 2026-08-06 — pass 3 closed having attached nothing. This is a correct outcome, not a failure: the campaign's job is to attach honest support, and there is none to attach here.

### Finding: some ungrounded lines may be genuinely ungroundable

The Space family's vocabulary — `Work.Space`, `Source.Space`, `Design.Space`, `Constrained.Space`, `Fixed.Space` — **appears in zero user turns across the entire corpus**. `QA.Space` appears in one, and only in machine-generated text. This material looks agent-authored or re-derived from broader discussion the user never phrased in these terms.

Per `Index.Line`, that is not a defect to fix by force: an ungrounded line remains index content and carries `Index.Presumption`; missing grounding is debt, not a deletion trigger. But it does mean **the remaining deficit is not uniformly reachable**, and future scoping should not assume it is. Before committing a cluster to a pass, run the cheap corpus-wide phrase query first — a zero-session result predicts an empty pass at near-zero cost.

`C5` is retired as ungroundable-for-now, distinct from `C2`/`C4` which are merely `typing-required`.

- 2026-08-06 — `::start-campaign-with-typing` for the A+E pair. `P6` (C6, 7 `groundable` lines, session `918b793b73f8`) and `P4` (C4, 30 `typing-required` lines, session `4f7b47fffe9e`) dispatched **concurrently** — different files, different sessions, no interference. C6 consumes no typing authority since its lines are already typed.
- 2026-08-06 — **both packets aborted on first attempt: the module's reference files were renamed mid-session.** `references/grounding-agent.md` → `references/index-retrofit.md` and `references/grounding-worker.md` → `references/index-retrofit-worker.md`; the subsystem is now `Index.Retrofit.*` (`Grounding.Supervisor.Agent` → `Index.Retrofit.Supervisor`, `Grounding.Work.Packet` → `Index.Retrofit.Packet`, `Grounding.Agent.Workflow.Module` → `Index.Retrofit.Workflow.Module`). The worker refused to improvise a substitute contract, which is the correct behavior.
- 2026-08-06 — supervisor verified the renamed contracts before re-dispatch: **content is identical apart from concept renames.** Research procedure, the typing/support two-requirement rule, `Legacy.Type.Migration.Exception` handling, result format, `User.Command` triggers (`::start-campaign`, `::start-campaign-with-typing`, `::resurvey`, `::campaign-status`, `::stop-after-current`) and the Discipline list are unchanged. No re-derivation of completed passes is required; passes 1–3 remain valid.
- 2026-08-06 — both packets re-dispatched against the corrected path with packets otherwise unchanged.

**Naming note:** this report is still filed under its original `grounding-campaign` name and uses `Grounding.*` section headings. The subsystem is now `Index.Retrofit.*`. Renaming the artifact mid-campaign would break the resumability the report exists to provide, so the name is kept and the mapping recorded here. Rename at campaign close if desired.

- 2026-08-06 — **pass 4 interrupted.** Both re-dispatched workers were terminated by an API session limit (resets 18:10 America/Havana) before either returned a packet result. This is an infrastructure stop, not a research outcome.
  - `P6` had confirmed the corrected contract path and begun research; it had flagged two turns in `918b793b73f8` as promising for the `Agentos.AGENTS.Section` block and was widening its per-line searches when it stopped. **No result contract was returned, so nothing from that partial run is usable as support.** Recorded here only as a search hint for the re-dispatch, explicitly NOT as a finding.
  - `P4` had independently verified the renamed contract path — checking the file existed rather than taking the supervisor's redirect on faith — and stopped at the same limit before any research.
- 2026-08-06 — **no mutation occurred in pass 4.** No anchors minted, no type prefixes landed, no Index line touched. Depot state is exactly as pass 3 left it: `line 1449/3240 linked`, `block 137/328 grounded`, `gr-density 0.5242`. Both packet manifests above are materialized and revalidated, so re-dispatch needs no re-derivation — only a re-run of the two worker prompts.

### Resuming pass 4

Both packets are fully specified above and their target lines were verified current at dispatch. To resume after the limit resets, re-dispatch unchanged, using the **renamed** contract path `references/index-retrofit-worker.md`:

- `P6` — C6 `Agentos.AGENTS.Section`, 7 `groundable` lines, session `918b793b73f8`, fallback `27821fc60104`. Ordinary grounding; consumes no typing authority.
- `P4` — C4 `Index.Edit.*` + `Partial.Cite`, 30 `typing-required` lines, session `4f7b47fffe9e`, fallback `9d194db7f404`. Requires a fresh `::start-campaign-with-typing` grant, since command authority does not survive across sessions.

Revalidate both manifests against current file content before dispatch; a line whose `Line.Type + body` or legacy body has changed is `stale` and must be dropped from its packet.

- 2026-08-06 — pass 4 resumed. Both manifests revalidated against current file content before re-dispatch: `P6`'s 7 lines all still typed and anchor-free with matching content hashes; `P4`'s 30 lines all still untyped and anchor-free. **No drift, so no line dropped as `stale`.** Both re-dispatched concurrently against `references/index-retrofit-worker.md`.
- 2026-08-06 — `P4` resumes under the same `::start-campaign-with-typing` grant that opened pass 4. The pass was interrupted by infrastructure, not completed, so the bounded authority for this cluster set is still the one the user issued; no new grant was inferred.
- 2026-08-06 — the interrupted `P6` run's partial search hints (turns near `r101`/`r111`) were passed to the new worker **explicitly labelled as a search hint and not a finding**, with instructions to re-derive all support from scratch and to return `ambiguous` if that is what the evidence gives.

- 2026-08-06 — `P6` returned 6/7 `supported`, 1 `ambiguous`. All 6 passed preview with zero equivalence collisions; registered and attached. Focused lint of `design/101-design.md`: **0 errors**. `Agentos.AGENTS.Section` now 6/7 grounded.
  - `G07` (`subsections should be named by subsystem, so each package can own and lint its own Agentos-facing content`) came back `ambiguous`. The session discusses subsections and per-project linter config but never ties subsection naming to per-subsystem package ownership. The worker declined to stretch nearby turns onto it — correct. Left untouched; next candidate `27821fc60104`.
  - the worker independently resolved the prior interrupted run's `r101`/`r111` hint: `r101` is a near-duplicate turn sitting **off the active conversation path**, so `r111` is the canonical member. The hint was not taken on faith.
  - two attachments are honestly weaker than the rest and are recorded as such: `G03`'s named examples (`subsystem routing`, `local policy`) have no verbatim user support — the support is for the line's breadth claim, which the user did state. `G06`'s "cost paid by every session" rationale is agent wording over a user requirement to normalize sections for linting. Both match the shape already accepted in pass 1 (user states the requirement, agent supplies the rationale clause); flagged here as the first place to look if either is disputed.
- 2026-08-06 — `P4` returned **30/30 `ambiguous`**. Every line received a confident type classification, but the session yielded no user support for any of them. Cause: `4f7b47fffe9e` is `/compact`-continued and its earliest indexed turn is the compaction summary itself (2026-07-07T17:23Z); commit `6ba0aa1` (2026-07-05) predates that window entirely. The only occurrences of these terms are inside the auto-generated summary — recap text, not user turns. **Nothing typed, nothing attached.**
  - this is the second time a `/compact` boundary has blocked a packet in this campaign (it also cost 3 lines in pass 2). **Method note for future scoping: a `/compact`-continued session can only ground material authored after its compaction boundary.** Check the session's earliest indexed turn against the target's git introduction window before dispatching — if the commit predates the boundary, the packet is doomed and the fallback should be dispatched first.
  - proven prior authorship in a session does not transfer across its compaction boundary: this same session landed 25/25 in pass 2 for material authored *after* the boundary.

### Scope discovery carried into future passes

Typing state — not session recall — is the binding constraint on this depot. Of C1's 28 lines only 12 were `groundable`; the other 16 are `typing-required`.

Depot-wide the ratio is stark: **69 `groundable` lines against 971 `typing-required` bodies**. So the ordinary `::start-campaign` route can reach only ~7% of the remaining deficit. The rest is reachable only through `Legacy.Type.Migration.Exception` under `::start-campaign-with-typing`, which types and grounds a legacy body atomically while preserving the body byte-for-byte.

Clusters `C2` (34 lines), `C3` (28) and `C4` (30) are entirely `typing-required`. They are **not retired** — their session hints are strong and they become dispatchable the moment typing authority is granted.

#### Groundable inventory — the whole `::start-campaign` surface

| block | file:line | groundable lines |
|---|---|---|
| `QA.Space` | 106:82 | 7 |
| `Agentos.AGENTS.Section` | 101:83 | 7 |
| `Gr.Req` | 102:89 | 6 |
| `Open.Space` | 106:186 | 5 |
| `Work.Space` | 106:105 | 4 |
| `Touched.Space` | 106:167 | 4 |
| `Source.Space` | 106:114 | 4 |
| `Constrained.Space` | 106:209 | 4 |
| `Fixed.Space` | 106:218 | 3 |
| `Design.Space` | 106:123 | 3 |
| (remainder) | 102, 104, 107, poi/103 | 22 across partially grounded blocks |

### `C5` — Space family — recommended pass 2 (`::start-campaign`)

- target: `design/106-design.md` — `QA.Space`, `Work.Space`, `Source.Space`, `Design.Space`, `Touched.Space`, `Open.Space`, `Constrained.Space`, `Fixed.Space`
- typing disposition: 34 `groundable`, 0 `typing-required` — dispatchable without typing authority
- git hint: `## QA.Space` introduced in `22fa13a` (2026-07-13, "docs: model qa space alignment axes")
- candidate session: not yet queried — resolve at dispatch with `--user-contains 'QA.Space'` and `--user-contains 'Touched.Space'`
- `C6` (`Agentos.AGENTS.Section`, 7) and `C7` (`Gr.Req`, 6) are the other coherent groundable clusters and can share the pass

### Typing-migration candidates — `::start-campaign-with-typing`

`C2`, `C3`, `C4` and C1's 16-line remainder are the ranked candidates, all with an identified candidate session and git introduction window. `C3` is the strongest first migration: the `Line.Type::*` family is small, semantically explicit about its own acts, and its blocks describe the very vocabulary the migration would apply — a good calibration target where a wrong classification is easy to spot.

Applicable `Line.Type.Vocabulary` for any migration packet: `DF`, `DC`, `CT`, `RJ`, `PR`, `FR`, `EX`, `GR` (`design/106-design.md:302`). Workers must return honest `residue` rather than force a body into the vocabulary.
