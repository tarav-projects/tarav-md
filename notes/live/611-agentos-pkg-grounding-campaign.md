# 611 — agentos-pkg Grounding Campaign

## Grounding.Abstract

- depot: `skills/agentos-pkg` (project `agentos-md`)
- caller boundary: none supplied — scope computed by supervisor
- state: `pass 2 complete (C3 migrated) — awaiting command for pass 3`
- coverage after pass 1: `line 1419/3235 linked` (+12), `block 130/328 grounded` (+2), `gr-density 0.5109` (+0.0058)
- coverage after pass 2: `line 1449/3240 linked` (+30), `block 137/328 grounded` (+7), `gr-density 0.5242` (+0.0133)
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
