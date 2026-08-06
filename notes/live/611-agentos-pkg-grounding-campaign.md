# 611 — agentos-pkg Grounding Campaign

## Grounding.Abstract

- depot: `skills/agentos-pkg` (project `agentos-md`)
- caller boundary: none supplied — scope computed by supervisor
- state: `campaign active — pass 1, cluster C1 (Cold.Loading)`
- coverage before — two different denominators, both correct:
  - linter meter (all index lines, incl. non-kernel): `line 1407/3235 linked`, `block 128/328 grounded` (328 = coverage-eligible blocks)
  - blocks meter (kernel lines only): `gr-density 0.5051` over 2063 kernel lines / 1042 unique anchors across 329 inventoried blocks
  - the block counts differ by one because the linter excludes one block from coverage eligibility that the inventory still lists
- ungrounded surface: 170 blocks / 887 kernel lines, all inside `design/100..107-design.md` (`design/108..111`, `poi/`, `issues/` carry no zero-grounded blocks)
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
- candidate sessions: `3d91f5b30cc3` (codex, 2026-06-15), `fd6eaa31f7a2` (codex, 2026-06-15)
- git hint: `## Supervisor.Agent` introduced in `76cc466` (2026-06-15, "checkpoint before hugentics-impl-executer")
- evidence hint: `Soft.Program` appears in 9 sessions; the only two on the introduction date are both codex sessions of 2026-06-15
- note: dispatch `3d91f5b30cc3` first; `fd6eaa31f7a2` is the same-day sibling and becomes a second packet only if lines come back ambiguous

### `C3` — Line.Type vocabulary family — rank 3

- target: `design/106-design.md`
  - `Line.Type.Vocabulary` (:302, 7 lines)
  - `Line.Type::DF` (:314, 3) · `::DC` (:322, 3) · `::CT` (:330, 3) · `::RJ` (:338, 3) · `::PR` (:346, 3) · `::FR` (:354, 3) · `::EX` (:362, 3)
- candidate session: `27821fc60104` (claude-code, 2026-07-13)
- git hint: `## Line.Type::DF` introduced in `bb3229d` (2026-07-12, "skw v3 execution checkpoint")
- evidence hint: 12 sessions mention `Line.Type` in user text; `27821fc60104` is the only one inside the 07-12/07-13 introduction window
- fallback candidates: `4f7b47fffe9e` (2026-07-08), `9d194db7f404` (2026-07-10)
- caution: `Line.Type::GR` is already grounded and out of scope; the 7 targeted type blocks are a tight family and may share support turns — each still needs its own line-bound relationship

### `C4` — Index.Edit action family — rank 4

- target: `design/107-design.md`
  - `Index.Edit.Action` (:653, 5) · `Index.Edit.Create.Block` (:663, 5) · `Index.Edit.Append.Line` (:673, 5) · `Index.Edit.Modify.Line` (:683, 5) · `Index.Edit.Revise.Block` (:693, 5) · `Partial.Cite` (:703, 5)
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
| L01 | Context.Loading.Path | 74 | — | no | `` - `Context.Loading.Path` is the tiered path by which context enters an agent, ordered from guaranteed-at-cold to pulled-on-demand `` |
| L02 | Context.Loading.Path | 75 | — | no | `- each tier is a distinct loading mechanism with its own guarantee level; a later tier becomes reachable only once earlier tiers have loaded what it needs` |
| L03 | Context.Loading.Path | 76 | — | no | ``- tier 1 `Cold.Loading` — context guaranteed present from a cold start`` |
| L04 | Context.Loading.Path | 77 | — | no | ``- tier 2 `SKILL.Loading` — context that arrives whole when a skill is loaded`` |
| L05 | Context.Loading.Path | 78 | — | no | ``- tier 3 `Dynamic.Loading` — context pulled selectively, on demand`` |
| L06 | Context.Loading.Path | 79 | — | no | `- the path bootstraps itself: each tier loads the keys and surfaces the next tier needs to act` |
| L07 | Cold.Loading | 97 | — | no | ``- `Cold.Loading` is the `Context.Loading.Path` tier guaranteed present from a cold start, before the agent takes any action`` |
| L08 | Cold.Loading | 98 | — | no | ``- it loads through the `Cold.Loading.Hook`s an agent always sees on entry — skill descriptions and `AGENTS.md` `` |
| L09 | Cold.Loading | 99 | — | no | ``- the guarantee comes from redundant placement: the same context is wired into many `Context.Hook`s so the system cannot miss it`` |
| L10 | Cold.Loading | 100 | — | no | `- it is the bootstrap tier — it carries the minimal vocabulary and routing keys the later tiers need to act at all` |
| L11 | Cold.Loading | 101 | — | no | ``- only `Workflow.Neutral.Skill` orientation belongs here — non-steering, safe to always load; its cost is paid every session, so it stays minimal`` |
| L12 | Cold.Loading | 102 | — | CT | ``- [CT] `Cold.Loading` surfaces are linter-controlled because they shape every agent run before task-specific routing begins`` |
| L13 | Cold.Loading.Hook | 108 | — | DF | ``- [DF] `Cold.Loading.Hook` is a `Context.Hook` that the harness loads automatically before the agent acts`` |
| L14 | Cold.Loading.Hook | 109 | — | CT | ``- [CT] it injects a `Cold.Loading.Surface` `` |
| L15 | Cold.Loading.Hook | 110 | — | EX | ``- [EX] project-root `AGENTS.md` is a `Cold.Loading.Hook` when the harness reads it before the agent acts`` |
| L16 | Cold.Loading.Hook | 111 | — | EX | ``- [EX] skill descriptions are `Cold.Loading.Hook`s when the harness advertises them before skill selection`` |
| L17 | Cold.Loading.Hook | 112 | — | CT | `- [CT] its loaded content is linter-controlled because every session receives it` |
| L18 | Cold.Loading.Surface | 118 | — | DF | ``- [DF] `Cold.Loading.Surface` is a surface whose content is guaranteed present at `Cold.Loading` `` |
| L19 | Cold.Loading.Surface | 119 | — | CT | `- [CT] it is identified by harness loading behavior, not only by file name or path` |
| L20 | Cold.Loading.Surface | 120 | — | EX | ``- [EX] a project-root `AGENTS.md` loaded before the agent acts is a `Cold.Loading.Surface` `` |
| L21 | Cold.Loading.Surface | 121 | — | CT | ``- [CT] a `Context.Hook` is the injection mechanism; `Cold.Loading.Surface` is the loaded content surface`` |
| L22 | Cold.Loading.Surface | 122 | — | CT | ``- [CT] `Package.Driver` content may be projected into a `Cold.Loading.Surface` when the package must be reachable from cold`` |
| L23 | Cold.Loading.Surface | 123 | — | CT | ``- [CT] `Cold.Loading.Surface`s are linter-controlled because every session pays their context cost`` |
| L24 | SKILL.Loading | 129 | — | no | ``- `SKILL.Loading` is the `Context.Loading.Path` tier that arrives whole when a skill is loaded`` |
| L25 | SKILL.Loading | 130 | — | no | ``- the `SKILL.md` file is its unit — the single discrete loading step between `Cold.Loading` and `Dynamic.Loading` `` |
| L26 | SKILL.Loading | 131 | — | no | ``- it is atomic: loading a skill brings its entire `SKILL.md` at once, all-or-nothing, with no finer selection`` |
| L27 | SKILL.Loading | 132 | — | no | ``- whatever an author wants present the moment a skill is in context belongs in its `SKILL.md` `` |
| L28 | SKILL.Loading | 133 | — | no | ``- it sets up the next tier: the keys and routes loaded here are what `Dynamic.Loading` selects against`` |

Anchorable subset: L12–L23 (12 typed lines). L01–L11 and L24–L28 are untyped legacy lines; `agentos chatlas anchory` rejects `--line-content` that is not a typed Index line, so they cannot receive a line-bound `Support.Set` until they are typed through the normal verbatim gate. This is a scope discovery from pass 1, not a research failure.

| packet | cluster | session | lines | worker model class | state |
|---|---|---|---|---|---|
| `P1` | C1 | `918b793b73f8` | 28 | medium / medium reasoning | `researching` |
| `P2` | C2 | `3d91f5b30cc3` | 35 | medium / medium reasoning | `surveyed` |
| `P3` | C3 | `27821fc60104` | 28 | medium / medium reasoning | `surveyed` |
| `P4` | C4 | `ade6275355cc` | 30 | medium / medium reasoning | `surveyed` |

Contingent packets (dispatch only on ambiguity in the parent packet): `P2b` → `fd6eaa31f7a2` (C2), `P4b` → `549979e6f80a` (C4), `P3b` → `4f7b47fffe9e` (C3), `P1b` → `549979e6f80a` (C1).

## Grounding.Log

- 2026-08-06 — survey pass complete; no agents spawned, no transcripts loaded, no anchors minted, no Index lines edited.
- note: `agentos chatlas query` content filters cost ~40s per call against this corpus; survey used 6 such calls.
