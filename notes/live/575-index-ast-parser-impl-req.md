# Index AST Parser + Linter Port — Impl.Req

## Impl.Abstract

- **Goal**: give the Agentos Index a parsed model layer — a typed AST for index surfaces — and rebuild the linter as checks over that AST, with a parity sweep against the current raw-scan engine before retiring it. Ships the `Line.Unlinked` check (agendix always, index under `--warn-unlinked`) as the first native check, and a block↔anchor query API.
- **Scope**: new parser package in `agentos-py`; node/document check runner integrated into the existing linter machinery; port of all current checks; parity harness; raw-engine retirement; chatlas bridge updated to consume the parser; the new unlinked check; docs.
- **Out of scope**: consolidating `agentos.mdblocks` into the parser (the linter keeps mapping mdblocks findings initially — parity first; consolidation is a follow-up cleanup); semantic lints (agent work); index-content edits (gated — this effort proposes, never writes index blocks); the chatlas-aware provenance check's logic (it only re-bases onto the parser).
- **Repos**: `agentos-py` (parser package, linter port, tests), `agentos-chatlas-py` (`index_checks.py` re-base), `agentos-cli` (e2e only; no wiring change expected — the `extra_checks` socket is stable API). Reinstall note: `uv tool install --reinstall --editable .` from `agentos-cli/` after CLI-visible changes.
- **Source**: design discussion in session `9d194db7…` (2026-07-08); reference implementation: `/Users/pereiro/projects/md-library-project/md-library` — `src/md_library/docast/` (nodes 109 lines, parser 493) and `src/md_library/lint2/` (runner 1340, parity 341); its index documents the architecture (`skills/md-library-pkg/design/101-design.md:97-133`).
- **Status**: implemented

## Impl.Index

### Design.Principle::Parser.As.Model.Layer
- the parser is the index's model layer, the analogue of `Chatlas.Session.Model` for chat: surfaces parse into one typed model; the linter is just the first consumer
- other consumers arrive free: block↔anchor queries ("ask a block by its anchors"), `--type` calibration passes, grounding audits, coverage metrics
- a document ALWAYS parses: parse problems are `Diagnostic` nodes in the tree, never exceptions (md-library's key move — `docast/nodes.py`, `Diagnostic(Node)` with `reason`)

### Design.Principle::Checks.Over.AST
- checks never touch raw text; they receive typed nodes or the whole parsed document
- two check shapes, mirroring `lint2/runner.py:112-125`: a node check declares the node types it sees (`node_types` dispatch tuple, runner routes); a document check sees the whole parsed surface
- Tier-0 conformance: every parser `Diagnostic` becomes a linter finding BEFORE semantic checks — "did it parse" gates "is it right" (`101-design.md:110-111` in md-library's index)

### Reference.Implementation *(read before coding)*
- `md_library/docast/nodes.py` — `Node` (src, start_line, end_line, parsed dict, spans list), `InlineSpan` (frozen: kind, src, start, end, line, column, parsed), `Diagnostic`, `Document`
- `md_library/docast/parser.py` — line-classifier → block builder; `_location()` for span line/column; escaped-char handling
- `md_library/lint2/runner.py` — `Lint2PhysicalLine` (raw, stripped, line, block_index, node_type: physical lines back-referencing nodes), `Lint2Context`, check dataclasses, the runner loop (`:1252`)
- the parity-sweep pattern: md-library kept the legacy engine wired to no command until old-vs-new parity held, then demoted it — NOTE (pre-execution review): `lint2/parity.py` no longer exists at that path; the parity examples now live in md-library's tests — take the pattern, not the path
- do NOT copy code wholesale — the index grammar differs; copy the architecture

### Target.Package
- location: `agentos-py`, new subpackage `src/agentos/index/model/` (`nodes.py`, `parser.py`, `__init__.py`) — "model" names the role (naming is small open space; avoid bare `ast`, it shadows stdlib in readers' minds)
- public entry points: `parse_index_file(path | text) -> IndexDocument`; `parse_depot(root) -> IndexDepotModel` (surfaces classified: router, chapter files, appendix, agendix); query helpers: `anchors_by_block()`, `blocks_by_anchor()`, `kernel_lines()` iterators
- the linter's existing public API is FROZEN: `run_linter(config, …, extra_checks=…)`, `build_linter_config`, `LinterCheck/LinterFinding/GateResult/LinterState`, `register_index_commands(…, extra_linter_checks=…)`, JSON/text rendering — external callers (chatlas bridge, cli, tests) must not need changes beyond what S6 does deliberately; new options such as `--warn-unlinked` should flow through optional config/state fields, not required positional API changes

### Index.Grammar *(the node vocabulary — parse targets with current live syntax)*
- `Separator` — a line of four-plus `*` (`****`); anchors block boundaries
- `BlockHeading` — `## <Block.Path>`: root `Dotted.Name`, optional `:Param` segments, optional `/Segment` children (dotted or single-word free label); parsed payload carries root/params/segments (mirror `BLOCK_PATH_RE`, `linter.py`)
- `KernelLine` — `- ` bullet inside a block; parsed payload: act code + `AS:` source marker from a leading `[XX]`/`[AS:XX]` bracket (absent = untyped legacy), plus spans
- `MetaHeading`/`MetaLine` — `### meta` section and its lines (`namespace-members`, `aliases`) — parsed but never treated as `KernelLine`s
- `RouterEntry` — router table rows; TWO live dialects, both must parse: `## Routing`-style flat list (agentos-pkg `000-INDEX.md`) and `## Chapters`/`### <chapter>`-style (chatlas-pkg); an entry parses to (file path, [(concept, plus_n | None), …])
- `BlankLine`, `Text` (prose lines outside blocks — router prologue, `>` callouts), `CodeFence` (fenced blocks inside appendix pages — e.g. the JSON example in `Chatlas.Anchory-appendix.md` — their interior lines must NOT parse as kernel lines), `Diagnostic`
- `InlineSpan` kinds: `anchor` (`@\d{8}-\d+`), `concept_cite` (backticked `Dotted.Name`, including parameterized and partial forms), `type_bracket`, `file_mention` (backticked path-like)
- surface classification (in `parse_depot`): router (`000-INDEX.md` at root), chapter (`<dir>/NNN-<dir>.md`), appendix (`appendix/Concept.Name-appendix.md`, `-appendix-N.md` pages), agendix (`agendix/Concept.Name-agendix.md` + `Unassigned-agendix.md`); `AGENTS.md` files inside surface dirs are excluded (existing linter behavior — see `test_index_linter_ignores_agents_md_in_index_directory`)

### Parity.Contract
- a parity harness (dev-side, in tests) runs the OLD raw engine and the NEW AST engine over: the full fixture corpus in `tests/test_index_linter.py` AND both live depots (`agentos-md/skills/agentos-pkg`, `agentos-chatlas-md/skills/agentos-chatlas-pkg`)
- parity = identical check results (code, status, blocked_by) and findings (code, path, line, severity) modulo a documented allowlist of deliberate improvements; every divergence is either fixed or allowlisted with a reason in the Impl.Log
- the old engine is retired ONLY after parity holds; retirement is deletion (`No.Legacy.Allowed`), not a parked copy — git history is the archive

### Bridge.Rebase
- `agentos_chatlas/index_checks.py` currently imports the private `_line_type_surface_files` and re-scans lines with its own regex — after the port it consumes the parser: iterate `KernelLine` nodes' `anchor` spans (with node line numbers), `AS:` from the parsed payload
- the parser API it needs becomes public in S3 (this also discharges the 574 log note about promoting the private helper)

### New.Check::Line.Unlinked
- code `Index.Linter/Line.Unlinked`, severity warning
- a `KernelLine` with no `anchor` span is unlinked; scope: agendix surfaces ALWAYS (enforces the agendix hard-provenance `[CT]`); chapter+appendix surfaces only under a new `--warn-unlinked` flag (coverage meter, off by default — the index's unlinked lines are pre-linking legacy)
- meta lines, router entries, prose, code-fence interiors are not `KernelLine`s — excluded by construction

## Execution.Plan

*(RED.GREEN.Test.Suite throughout: each slice writes failing behavior tests first. Fixtures should be excerpts of REAL live-depot content — copy blocks from `agentos-pkg` 105/106/107 and the chatlas depot into fixtures, they exercise every grammar feature: typed lines, `AS:`, anchors, meta sections, code fences, both router dialects.)*

### S1 — Nodes + structural parser
- what: `model/nodes.py` (node dataclasses, `InlineSpan`, `Diagnostic`, `IndexDocument`), `model/parser.py` classifying separators, block headings, blank, text, code fences; blocks assembled between separators; heading outside a separator-anchored block → `Diagnostic`
- RED: a real 107 excerpt parses to the expected node sequence; an unclosed code fence and a heading-without-separator produce `Diagnostic` nodes, not exceptions; line numbers exact
- check: new test module green

### S2 — KernelLine + spans + meta
- what: bullet parsing (act code, `AS:`, untyped), span extraction (`anchor`, `concept_cite`, `type_bracket`, `file_mention`) with exact positions; `### meta` handling
- RED: a line `- [AS:CT] text ^20260708-0` yields parsed `{act: "CT", source: "AS"}` + one anchor span; untyped line yields no type payload; backticked `Dotted.Name`s become `concept_cite` spans; meta lines are not kernel lines; anchors inside code fences are NOT spans
- check: green; span positions verified by slicing `src`

### S3 — Router dialects + depot model + query API
- what: `RouterEntry` parsing for BOTH dialects; `parse_depot` surface classification (router/chapter/appendix/agendix, AGENTS.md exclusion) — the router is an EXPLICIT parse step from the depot root: `000-INDEX.md` is not in today's derived index surfaces and must never be reached only via chapter discovery (pre-execution review finding); public query helpers `blocks_by_anchor` / `anchors_by_block` / `kernel_lines`
- RED: both live routers' formats parse (fixture copies); `[+N]` annotations parsed; `blocks_by_anchor("20260705-0")` on a fixture returns the citing block path + line
- check: green; live smoke — `parse_depot` over both real depots reports zero `Diagnostic`s (or only known/justified ones, recorded in the log)

### S4 — Check runner over the AST
- what: node-check/document-check dataclasses + dispatch integrated INTO the existing linter (`LinterState` gains the parsed model; findings/gates/rendering unchanged); Tier-0 conformance check (Diagnostics → findings)
- DESIGN CLARIFICATION (pre-execution review): today's checks are a covert pipeline — early "checks" build inventory (file discovery, mdblocks, concepts) that later checks and gates consume, so ordering is load-bearing. The AST runner makes the split explicit: PARSING is the inventory phase, CHECKS only find. Gate codes, blocked statuses, and their rendering must reproduce exactly — parity compares blocked checks too, not only findings
- RED: a toy node check fires per matching node type; a `Diagnostic` in a fixture becomes a conformance finding; existing raw checks still run unchanged alongside
- check: full existing suite still green (old engine untouched so far)

### S5 — Port all checks + parity
- what: every check in `CHECKS` reimplemented as AST checks (filenames, router presence/targets/legacy-name, block sections, duplicate concepts, unanchored sections, appendix orphans/pages, Line.Types, Source.Axis.Placement, …; the mdblocks-syntax check keeps calling `agentos.mdblocks` and mapping its findings — unchanged); parity harness runs old vs new over fixtures + both live depots
- RED: the parity test itself — asserts finding-set equality modulo the allowlist
- check: parity green; every allowlist entry has a one-line justification in `Impl.Log`
- deviation trigger: a divergence that cannot be cleanly fixed or justified → stop and surface; do not weaken the parity assertion

### S6 — Retire the raw engine + bridge rebase
- what: delete the superseded raw-scan check implementations and private helpers (including `_line_type_surface_files`); `agentos_chatlas/index_checks.py` consumes the parser's public API; parity harness deleted with the old engine (it tested the transition, not durable behavior — `No.Regression.Tests.Allowed`)
- check: all three repos' suites green; `grep` shows no orphaned raw-scan helpers; both live depots lint with identical summaries to pre-port (16 checks, 0 findings)

### S7 — `Line.Unlinked` + `--warn-unlinked`
- what: the new check per New.Check spec; `--warn-unlinked` flag on `agentos index linter`
- RED: unlinked agendix kernel line warns by default; unlinked chapter line silent by default, warns under the flag; separators/headings/meta/fence interiors never warn; linked lines never warn
- check: live — both depots' agendix files pass (baseline measured at review time: 0 unlinked in both agendixes); `--warn-unlinked` baselines ≈ agentos-pkg design 1237 + appendix 642, chatlas design 167 + appendix 62 — expect that order of magnitude, warnings only, exit code unaffected by warnings
- observable: linking coverage is measurable per depot

### S8 — Docs + gated proposals
- what: `agentos-py/AGENTS.md` (parser package, check architecture, flag); `agentos-index` `references/check.md` (+`--warn-unlinked`, parser-backed engine note); update `references/search.md` reading guide if node vocabulary surfaces there; PROPOSE (gated, never self-write) index blocks to the user: an `Index.Model`/parser concept for the agentos-pkg index and an `Index.Linter` appendix update
- check: docs match real CLI; gated proposals delivered as verbatim drafts in the completion report

### Acceptance signals
- both live depots: identical lint results before/after the port, plus the new check's behavior
- `blocks_by_anchor` answers "which block does this anchor ground" as a library call
- all suites green (`agentos-py`, `agentos-chatlas-py`, `agentos-cli`); ruff clean; no regression-test slop

### Risks / deviation triggers
- the two router dialects are the grammar's messiest corner — if a third variant appears in fixtures/live, stop and surface (normalizing router syntax is a design decision, not open space)
- line-number fidelity: old-engine findings cite physical lines; AST checks must reproduce them exactly or parity fails — carry line numbers on every node/span from S1, never recompute
- `mdblocks` overlap temptation: do NOT fold mdblocks into the parser in this effort; parity depends on its findings staying byte-identical
- scale: live depots are the real test corpus; if parsing them surfaces grammar realities this req missed, record in `Impl.Log` and extend the grammar — the grammar section here is the map, the depots are the territory

## Impl.Log

- 2026-07-08 execution: created checkpoint commits in `agentos-md`, `agentos-py`, `agentos-chatlas-py`, and `agentos-cli` before implementation edits per the execution workflow.
- S1-S3 implemented `agentos.index.model` with typed nodes, `parse_index_file`, `parse_depot`, router parsing, code-fence protection, span extraction, and block-anchor query helpers.
- S1 deviation resolved autonomously: live index separators are delimiters, not open/close toggles; the same `****` closes the previous block and prepares the next. Parser separator handling was adjusted after live depot smoke initially produced false `heading_without_separator` diagnostics.
- S4-S6 implemented parser-backed linter state for concept inventory, router entries, unanchored-section detection, line-type checks, source-axis placement, and the Chatlas grounding bridge. The old private `_line_type_surface_files` helper and raw router/section parsing helpers were removed.
- S7 implemented `Index.Linter/Line.Unlinked` and `agentos index linter --warn-unlinked`; default scope checks agendix only, while the flag extends warnings to chapter and appendix kernel lines.
- S7 live baseline changed from the pre-review rough estimate: installed CLI reports 1847 `Line.Unlinked` warnings for `agentos-pkg` under `--warn-unlinked`; the lower count is expected because parser-backed logic excludes meta lines and non-kernel material.
- S8 updated `agentos-py/AGENTS.md`, `agentos-index/references/check.md`, and `agentos-index/references/search.md`.
- Verification: `agentos-py` full suite 281 passed; `agentos-chatlas-py` full suite 139 passed; `agentos-cli` full suite 56 passed; scoped ruff passed for touched `agentos-py` and `agentos-chatlas-py` files.
- Verification caveat: whole-repo ruff is not clean due unrelated pre-existing deprecated/dev files (`agentos-py/_DEPRECATED/...`, `agentos-py/dev/account-usage.py`, `agentos-chatlas-py/dev/user-script-invariant-test/validate.py`); touched-file ruff is clean.
- Installed CLI refreshed with `uv tool install --reinstall --editable .` from `agentos-cli/`; installed smoke checks show both live depots clean by default with 17 checks, 0 findings, and `--warn-unlinked` warning-only exit code 0.
