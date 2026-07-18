# Grounding-Retirement Tooling + Citation Sync — Impl.Req

## Impl.Abstract

- retire the last tooling and citation remnants of the block-grounding axis (`Grounding.Head` evidence boards, `Inline.Grounding`, `Kernel.Block.Grounding`, `Grounding.Drift`) after the design-side retirement landed: grounding is now a line property defined positively on `Index.Line` (`Grounded.Line`/`Ungrounded.Line`), mechanics in `agentos-md/skills/agentos-pkg/appendix/Index.Line-appendix.md`
- design source: design session `agentos-md/notes/live/591-touched-surface-index-design-session.md` (grounding-retirement follow-ups row); user order anchored `^20260718-1` (chatlas anchory depot); retirement decision turns `^20260716-33` `^20260717-0` neighborhood
- two halves: (1) `agentos-py` index tooling still measures block grounding by `Grounding.Head` presence — an axis that no longer exists; (2) live md surfaces still cite the retired concept names
- out of scope: `_DEPRECATED` skills; deleting existing `## <Block>/Grounding.Head` / `Grounding.Drift` sections inside appendix files (they demote in place, cleaned opportunistically per the session decision — after slice 1 the tooling no longer reads them, so they are inert)
- status: executed 2026-07-18 (all four slices; suites green, both depots lint clean, skillware check clean)

## Impl.Index

### Current.State (inspected 2026-07-18)

- `agentos-py/src/agentos/index/linter.py` — `_check_block_ungrounded` (~line 1475) + `_grounded_block_paths` (~line 1504): block coverage (`--coverage block`) counts a block covered iff its appendix carries a `Grounding.Head` section with an anchored `[GR]` line; finding `BLOCK_UNGROUNDED` message says "no Grounding.Head evidence board"
- `agentos-py/src/agentos/index/model/stats.py` — `BlockGroundingStats.board` flag + `_board_block_paths` implement the same board detection; docstrings cite `Grounding.Head`
- `agentos-py/src/agentos/index/commands.py` — `agentos index blocks` prints a `board` column (~lines 116–136) and its help text cites "evidence-board flag" (~line 162)
- tests: `agentos-py/tests/test_index_linter.py`, `test_index_blocks.py` cover the current board semantics
- md citation drift (live surfaces only; `grep -rln "Grounding.Head\|Inline.Grounding\|Kernel.Block.Grounding\|Grounding.Drift"`):
  - `agentos-md/skills/agentos-pkg/`: `SKILL.md`, `references/index-block-catalog.md`, design chapters `100/102/103` (105 already cleaned), appendix files (mixed: some are prose citations, some are the inert `Grounding.Head` sections themselves — only prose citations are in scope)
  - `agentos-md/skills/agentos-index/`: `SKILL.md` + most `references/*.md`, with skillware sources under `.skillware/src/` (edit the `.skw.md` sources, regenerate the views; several declare `depends --from Inline.Grounding` / `--from Kernel.Block.Grounding`)
  - `agentos-md/skills/hugentics-designer/references/index-view.md`, `writing-craft.md`; `agentos-md/skills/agentos-session-supervisor/references/role-chat-grounding.md`
  - `agentos-chatlas-md/skills/agentos-chatlas-pkg/appendix/Chatlas.Anchory-appendix.md`
- the 593-landed dependency-sync lint checks skw `depends` declarations against addressable names — retired names must clear from `depends` lists or that lint regresses
- read root `AGENTS.md` and `agentos-py/AGENTS.md` before editing

### Design.Decisions (resolved in AUTO mode — recorded, not hidden)

- **new block-coverage semantics** — a chapter concept block is covered iff every kernel line in it carries at least one trailing anchor (all lines are `Grounded.Line`s); derived purely from line grounding, no appendix machinery; empty blocks (0 kernel lines) count covered
- **`BLOCK_UNGROUNDED` finding** — keep the code, reword: "Index concept block has ungrounded kernel lines (lines missing trailing anchors)."; details gain `ungrounded_lines` count
- **`stats.py`** — drop the `board` field and `_board_block_paths` entirely; add `grounded_lines: int` so consumers can read line-level coverage per block; `gr_density` unchanged
- **`agentos index blocks`** — replace the `board` column with `grounded` (`<grounded_lines>/<kernel_lines>`); update help text to cite `Grounding.Density` and line grounding only
- **citation rewrite rules** (apply the surviving vocabulary, preserve existing anchors verbatim):
  - `Grounding.Head` / "evidence board" → grounding lives on the lines; point at `Index.Line` (`Index.Line/Grounding.Mechanics` for mechanics)
  - `Inline.Grounding` → `Grounded.Line` / line-property grounding on `Index.Line`
  - `Kernel.Block.Grounding` → cite `Index.Line` grounding; where a sentence only existed to invoke the block-grounding scheme, drop the sentence
  - `Grounding.Drift` → `Demoted.Anchored.Line` / demotion (evidence-based, computed)
- **design chapters 100/102/103** — rewrite the citing lines minimally to the surviving names; do not restructure blocks; anchors stay untouched
- **skillware `depends`** — remove `--from Inline.Grounding` / `--from Kernel.Block.Grounding` (add `--from Index.Line` or `--from Grounded.Line` only where the rewritten text actually mentions them); regenerate views with the skillware build so `.skillware/src` and rendered files stay in sync

## Execution.Plan

Run `python -m pytest agentos-py/tests/test_index_linter.py agentos-py/tests/test_index_blocks.py` per slice; RED→GREEN where marked. Checkpoint commits per execution workflow before starting.

### Slice 1 — linter block coverage
- rewrite `_check_block_ungrounded` to the all-lines-grounded semantics; delete `_grounded_block_paths`
- RED: block with all lines anchored → covered, no finding; block with one unanchored line → `BLOCK_UNGROUNDED` with `ungrounded_lines`; a `Grounding.Head` appendix section no longer affects coverage
- GREEN: implement; full linter suite stays green

### Slice 2 — stats + blocks CLI
- `stats.py`: drop `board`/`_board_block_paths`, add `grounded_lines`; `commands.py`: `grounded` column + help text; fix docstrings citing `Grounding.Head`
- RED: `agentos index blocks --json` shape carries `grounded_lines`, no `board` key; table renders `<g>/<n>`
- check: no `Grounding.Head` reference remains under `agentos-py/src/`

### Slice 3 — agentos-index skill citation sync
- apply the rewrite rules across `agentos-index` skillware sources (`.skillware/src/**/*.skw.md`), including `depends` lists; regenerate views; verify rendered `SKILL.md`/`references/*.md` match
- check: dependency-sync lint green; `grep` for the four retired names under `skills/agentos-index/` returns nothing

### Slice 4 — remaining md surfaces
- rewrite prose citations in: agentos-pkg `SKILL.md`, `references/index-block-catalog.md`, design `100/102/103`, appendix prose citations (NOT the inert `Grounding.Head`/`Grounding.Drift` sections themselves); hugentics-designer + session-supervisor references; chatlas `Chatlas.Anchory-appendix.md`
- check: `agentos index linter --depot skills/agentos-pkg` clean from `agentos-md/`; same for the chatlas depot; remaining hits for the four names are only inert appendix section headings/bodies or `_DEPRECATED`

### Risks / deviation triggers
- distinguishing prose citation vs inert section inside appendix files requires judgment — when unsure, leave the line and log it in `Impl.Log`
- skillware regeneration may rewrite more than the touched files → diff before committing; if the build drifts unrelated content, edit rendered files by hand and log the deviation
- design-chapter rewrites must not change block meaning — if a line cannot be rewritten without semantic change, leave it and log for a design-session revisit

### Acceptance signals
- both test files green + full suite green
- `agentos index blocks` shows the `grounded` column; block coverage responds to line anchors only
- retired-name grep across live skills returns only inert sections and `_DEPRECATED`
- linter clean on both depots

## Impl.Log

- 2026-07-18 · executed by the designing agent in the same session (`--exec --AUTO`); pre-execution checkpoint commits in agentos-py (3ec04ba), agentos-md (6f1f24a), agentos-chatlas-md (c8c89be) captured pre-existing uncommitted work as found
- slice 1 · RED→GREEN as planned; `KernelLine` already imported in linter.py; scope-filter test updated (its old assertions encoded board semantics: block coverage in scope is now 0/1 and finding_count 2)
- slice 2 · RED→GREEN as planned; also updated `agentos-py/AGENTS.md` lines documenting the old `--coverage block` and `blocks` board semantics (doc-update-required policy)
- slice 3 · one intentional retired-name mention kept: `search.skw.md` line orienting readers that `Grounding.Head`/`Grounding.Drift` appendix sections are inert legacy; skillware check surfaced 9 POIs — 3 undeclared-dependency fixed by adding `--from Index.Line`/`--from Demoted.Anchored.Line`, 1 derived-stale blessed (digest content unaffected by dep edits), 5 unhonored-dependency `Capture.Offer` blessed — DEVIATION NOTE: `Capture.Offer` was demoted this session from a 107 block to an appendix section of `Touched.Surface.Index`, and appendix-section names are not resolvable by the Dotted.Name depot resolver; blessing records the situation, but appendix-section addressability is an open follow-up for the resolver
- slice 4 · one extra live citation found and fixed beyond the plan inventory: `105-design.md` `Chat.Grounding.Target.Block` line citing `Kernel.Block.Grounding` (rewritten to line-property wording); `Chatlas.Anchory-appendix.md` hit left as-is (a frozen anchor-hint quote — historical data, not a citation); `100-design.md` `Grounding.Audit` block: the "demoted inline grounding also lands in Grounding.Drift" line was folded into the rewritten demotion line rather than rewritten standalone (pure-demotion doctrine has no drift destination)
- verification · agentos-py suite 372 passed; `agentos index linter --depot` clean on agentos-pkg and agentos-chatlas-pkg; `agentos skillware check --skill skills/agentos-index` 0 POIs; `agentos index blocks` smoke shows the `grounded g/n` column (installed CLI is editable, no reinstall needed)
- post-execution 2026-07-18 · the `Capture.Offer` deviation resolved by design change: the user promoted `Capture.Offer` back to a 107 block ("needing to be referenceable is a reason to create a block", `^20260718-2`); the five blessed unhonored-dependency POIs were then removed from `lock.json` (no unbless CLI exists; surgical edit + rebuild, check clean) — left in place they would have masked any future recurrence of the same situation-stable POI hashes; the general resolver follow-up (appendix-section addressability) stays open but is no longer blocking anything
- remaining retired-name hits are by design: inert `*/Grounding.Head` section headings + historical hint/[GR] quotes in appendix files (opportunistic cleanup), `_DEPRECATED` skills, and the intentional search.md orientation line
