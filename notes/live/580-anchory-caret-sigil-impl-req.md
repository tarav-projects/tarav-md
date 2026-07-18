# Anchory Caret Sigil Migration - impl-req

## Impl.Abstract

- **scope:** move the `Anchory.Anchor` surface sigil from `@YYYYMMDD-N` to `^YYYYMMDD-N` — hard cutover across parser, checks, skill docs, and existing markdown surfaces
- **status:** implemented
- **source:** `Block.Name.Schema` design discussion (this session, 2026-07-09): `@` becomes the locator prefix in the block naming schema; `^` (Obsidian-style) takes the evidence-anchor role so every sigil keeps one meaning
- **out of scope:** the `Block.Name.Schema` index blocks themselves (separate design/edit pass); anchory depot storage format (keys are stored bare, no data migration); any dual-syntax compatibility mode

## Impl.Index

### Anchor.Sigil.Boundary

- the sigil exists only at the markdown surface and at parse/display boundaries — storage and CLI inputs use bare keys
- single parse point: `ANCHOR_RE = re.compile(r"@(?P<anchor>\d{8}-\d+)\b")` at `agentos-py/src/agentos/index/model/parser.py:41`
- input-tolerance point: `blocks_by_anchor` strips a leading `@` at `agentos-py/src/agentos/index/model/nodes.py:108`
- display strings interpolate `@{anchor}` in `agentos-chatlas-py/src/agentos_chatlas/index_checks.py:76,98,112,126`
- anchory depot keys are stored bare by convention; `_validate_anchor` (`agentos-py/src/agentos/anchory/core.py:247`) only checks non-empty string — storage and CLI remain permissive and are unchanged by this req; the sigil boundary is enforced at the markdown surface (linter), not in storage
- CLI `--anchor` args (`agentos-py/src/agentos/anchory/commands.py`, `agentos-chatlas-py/src/agentos_chatlas/commands.py:1500`) take bare keys — no flag changes

### Cutover.Decision

- hard cutover, no dual parsing — aligned with the `No.Legacy.Allowed` index principle
- `@\d{8}-\d+` becomes a linter finding (legacy sigil), not a silently accepted alternate form
- programmatic lookup inputs stay tolerant: `blocks_by_anchor` strips a leading `^` or `@` from its input argument (caller convenience, not a surface form)
- collision check done: no `^\d{8}-\d+` occurrences exist anywhere in `agentos-md` today; markdown footnote syntax `[^1]` cannot match the 8-digit pattern

### Migration.Scope.Rule

- the rewrite scope is defined by rule, not by list: every `*.md` file under `agentos-md/` and `agentos-chatlas-md/` whose content matches a rewrite pattern is in scope — the rule is the authority; the inventory below is informative
- the single exception is this artifact itself (`notes/live/580-anchory-caret-sigil-impl-req.md`), which must describe the old form to specify the migration; the acceptance greps exclude it
- live notes are in scope (563, 569, 571, 573, 574, 575, 577, ...) — they are grep-consistency surfaces (`Name.As.Index` reverse-findability), not protected history
- known literal-anchor surfaces: `agentos-md/skills/agentos-pkg/` (design 102, 105, 106, 107; appendix and agendix files; SKILL.md), `agentos-chatlas-md/skills/agentos-chatlas-pkg/design/100-design.md`, `agentos-md/skills/agentos-index/references/link.md`, live notes above
- known syntax-teaching surfaces (mint path is agent-mediated, so docs are the formatter): `agentos-md/skills/agentos-index/` SKILL.md and references (link.md, search.md, agendix.md, and any of back-link.md / gr-survey.md / gr-review.md / type.md showing the `@` form), `agentos-md/skills/agentos-pkg/SKILL.md`, `agentos-chatlas-md/skills/agentos-chatlas-pkg/references/chatlas-commands.md:96`, and the prose/regex mentions in `agentos-md/notes/live/571-line-type-linter-checks-parking.md`
- `.claude/skills/` entries are symlinks into `agentos-md/skills/` — editing the source tree updates the runnable surface; no second copy exists in this project
- index blocks are normally `Content.Verbatim.Gated`; the user's approval of this Impl.Req is the gate for this mechanical sigil rewrite — no wording may change beyond the rewrite patterns

### Gated.Rewrite.Rule

- pattern 1 (literal anchors): `@(\d{8}-\d+)\b` → `^\1`
- pattern 2 (prose/placeholder form): `@YYYYMMDD-N` → `^YYYYMMDD-N`, and quoted anchor regexes such as `@[0-9]{8}-[0-9]+` → the `^`-escaped equivalent
- no other textual change is permitted on migrated surfaces

## Execution.Plan

### Slice 1 - Parser and model cutover (RED then GREEN)

- update anchor-parsing tests first: `agentos-py/tests/test_index_model_parser.py`, `agentos-py/tests/test_index_linter.py`, `agentos-chatlas-py/tests/test_index_checks.py` expect `^YYYYMMDD-N` spans and `^`-form messages — suite goes RED
- flip `ANCHOR_RE` in `agentos-py/src/agentos/index/model/parser.py:41` to `r"\^(?P<anchor>\d{8}-\d+)\b"`
- update `blocks_by_anchor` input stripping in `agentos-py/src/agentos/index/model/nodes.py:108` to strip a leading `^` or `@`
- update the four `@{anchor}` display strings in `agentos-chatlas-py/src/agentos_chatlas/index_checks.py` to `^{anchor}`
- observable: parser emits anchor spans for `^c20260708-7u` and no longer for `@20260708-7`
- check: both packages' test suites pass GREEN
- status: done

### Slice 2 - Legacy-sigil linter check

- current state (post-579, present in the dirty workspace): the linter registers 18 checks in the `CHECKS` tuple at `agentos-py/src/agentos/index/linter.py:1473`, including `Index.Linter/Block.Ungrounded`
- add a legacy-sigil check to that `CHECKS` registry that flags `@\d{8}-\d+` on index surfaces as a legacy anchor sigil with a fix hint; update any test asserting the registry/check count
- RED-then-GREEN: a fixture line carrying `@20260101-0` produces the finding; the `^` form produces none
- observable: `agentos index linter` reports legacy sigils
- check: new linter test passes; existing linter tests still pass
- status: done

### Slice 3 - Markdown surface migration

- apply the `Gated.Rewrite.Rule` patterns across every file selected by `Migration.Scope.Rule` (script the rewrite; do not hand-edit)
- verify with the migration greps, excluding this artifact: `grep -rn '@[0-9]\{8\}-[0-9]\|@YYYYMMDD' agentos-md agentos-chatlas-md --include='*.md' | grep -v 580-anchory-caret-sigil` returns nothing; the `\^[0-9]\{8\}-` grep returns the pre-migration literal-anchor count (record the baseline count before rewriting)
- observable: `agentos chatlas views inline --anchor <key>` and `agentos index linter` grounding checks resolve anchors from the migrated surfaces
- check: `agentos index linter` run over the agentos-pkg depot reports zero legacy-sigil findings and no new grounding regressions relative to a pre-migration baseline run
- status: done

### Slice 4 - Syntax-teaching doc updates

- rewrite the `@YYYYMMDD-N` syntax descriptions to `^YYYYMMDD-N` across the known syntax-teaching surfaces in `Migration.Scope.Rule` — including `agentos-chatlas-md/skills/agentos-chatlas-pkg/references/chatlas-commands.md` and the 571 parking note — plus anything else the scope-rule grep finds
- observable: `grep -rn '@YYYYMMDD' agentos-md agentos-chatlas-md --include='*.md' | grep -v 580-anchory-caret-sigil` returns nothing
- check: grep clean; spot-read link.md mint instructions to confirm they now teach `^`
- status: done

## Impl.Log

- 2026-07-09 review pass: migration authority moved from a hand-listed inventory to `Migration.Scope.Rule` (rule over list); chatlas-commands.md and the 571 parking note added to syntax-teaching surfaces; storage claim corrected (`_validate_anchor` is permissive, sigil boundary enforced by linter only); Slice 2 pinned to the post-579 18-check `CHECKS` registry
- 2026-07-09 execution checkpoint commits created before mutation: `agentos-py` `2aa73cd`, `agentos-md` `5044b53`, `agentos-chatlas-py` `24c276b`, `agentos-chatlas-md` `bf486d3`
- Slice 1 implemented: parser anchor regex now accepts `^YYYYMMDD-N`, parser tests expect caret spans and no legacy-span parse, `blocks_by_anchor` accepts caller input with or without a sigil, and Chatlas provenance messages render caret anchors
- Slice 1 RED/GREEN: focused tests failed before parser/message changes, then `uv run pytest tests/test_index_model_parser.py tests/test_index_linter.py` passed `34 passed`; `uv run pytest tests/test_index_checks.py` passed `6 passed`
- Slice 2 implemented: `Index.Linter/Anchor.LegacySigil` was added to the linter registry and warns on `@YYYYMMDD-N` in index surfaces with a caret replacement hint
- Slice 2 RED/GREEN: the legacy-sigil fixture failed before the check existed, then `uv run pytest tests/test_index_linter.py` passed `31 passed`
- Slice 3/4 implemented: markdown rewrite baseline found `110` literal legacy anchors outside this artifact; the scripted rewrite converted all selected literal, placeholder, and syntax-teaching forms; post-rewrite caret literal count is `110`
- Migration acceptance grep is clean outside this artifact: `grep -RIn '@[0-9]\{8\}-[0-9]\|@YYYYMMDD\|@(?P<anchor\|@\[0-9\]' agentos-md agentos-chatlas-md --include='*.md' | grep -v 580-anchory-caret-sigil` returns no rows
- Verification: `uv run ruff check src tests` passes in `agentos-py` and `agentos-chatlas-py`; full `uv run pytest` passes in `agentos-py` (`286 passed`) and `agentos-chatlas-py` (`143 passed`)
- Live verification after `uv tool install --reinstall --editable .`: `agentos index linter --depot skills/agentos-pkg --json` and `agentos index linter --depot skills/agentos-chatlas-pkg --json` both pass `19` checks with zero findings
- Coverage-mode smoke: `agentos index linter --depot skills/agentos-pkg --coverage all --scope skills/agentos-pkg/design --json` reports the existing coverage backlog (`1203` unlinked-line warnings, `219` ungrounded-block warnings) and zero legacy-sigil/provenance findings
- Chatlas smoke: `agentos chatlas views inline --anchor 20260707-0 --radius 1 --filter turns --format json` resolves the migrated anchor and returns the landing-turn window
- deviation: an initial broad test rewrite command corrupted three test files; they were restored from the checkpoint immediately, then the intended narrow rewrite was reapplied and verified by RED/GREEN tests
- design follow-up (not this artifact): land the `Block.Name.Schema` sigil table in the index via `agentos-index --edit`
- follow-up for other projects: re-sync imported skills where `agentos-index`/`agentos-pkg` are copied rather than symlinked (`references/skills-routing.md`)
