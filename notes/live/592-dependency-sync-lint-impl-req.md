# Dependency-Sync Lint — Impl.Req

## Impl.Abstract

- implement the **declaration/mention dependency-sync lint** for skw-managed skill surfaces: a bidirectional CPU check between *declared* dependencies and *addressable-name mentions*, surfaced as POIs, resolved by agents
- design source: design session `agentos-md/notes/live/591-touched-surface-index-design-session.md` + the landing-pass drift finding (skill references cited `Index.Main` after its rename with `agentos skillware check` reporting 0 POIs)
- the user's model (accepted in chat, 2026-07-16): declarations are **normative intent** — part of the generation contract ("this surface MUST depend on these"); mentions are the artifact's actual references; the CPU checks set-sync in **both directions**, modulo blessings; auto-derived implicit edges were explicitly rejected — two surfaces must exist to be synced
- scope: `agentos-py` skillware subsystem (`agentos-py/src/agentos/skillware/`) — parser vocabulary, check pass, bless ergonomics, tests
- out of scope: index-linter changes, `Skw.Network` notification/fan-out machinery, prose-paraphrase detection (only backticked `Dotted.Notation` mentions are visible — the fence is what the syntax can see), any index/markdown content edits
- status: executed

## Impl.Index

### Current.State (inspected 2026-07-16)

- checker: `agentos-py/src/agentos/skillware/build.py` — `check_skill()` (line ~521) is the `Poi.Linter` pass; existing POI kinds: `parse-error`, `unresolvable`, `never-built`, `stale-build`, `hand-edited`, `copy-drift`, `derived-stale`; POIs carry stable identity hashes via `_poi()` (~379)
- declarations today: only recipe `--from` targets on `copy`/`derived` constructs (`SkwRecipe.froms`, `model.py` ~44); there is **no declaration-only vehicle** for a plain dependency
- address resolution: `_resolve_locator()` (build.py ~137) already resolves bare `Dotted.Name`s against configured depots (`skillware.json` `depots` → `parse_depot()` → `_depot_block_body()`); labeled spans (`^label`) and file/region locators also supported
- command registry: `model.py` — `PRIMITIVE_COMMANDS = ("text", "copy", "derived")`, `STRUCTURAL_COMMANDS = ("router", "when", "then")`; unknown commands are parse findings (~345)
- bless: `bless_skill(skill_root, poi_hash)` (~650) records a `BlessRecord` in the lock; a blessed POI hash is suppressed until the situation (hence hash) changes
- CLI: `agentos-py/src/agentos/skillware/commands.py` — `_cmd_skillware_check` prints entries + POI rows; `_cmd_skillware_bless` takes one `poi_hash`
- tests: `agentos-py/tests/test_skillware.py`
- read `agentos-py/AGENTS.md` (and root `AGENTS.md`) before editing

### Design.Decisions (resolved in AUTO mode — recorded, not hidden)

- **`depends` command** — new declaration-only skw construct: `$kw: depends --from <addr> [--from <addr> …]`. It is **void** (bodyless): the registry marks it self-closing — no owned `end-depends` required, consistent with the doctrine that mandatory ends exist because "nothing can infer where an arbitrary body stops"; a void command has no body to bound. If void commands prove invasive to the parser's frame model, fallback: accept an empty body with mandatory `end-depends` and record the deviation in `Impl.Log`.
- **declared set** per src file = union of (a) all `depends` `--from` targets, (b) all `copy`/`derived` recipe `--from` targets
- **mention set** per file = backticked dotted names extracted from the **expanded target text** (`expansion.fresh_lines`), regex on the pattern `` `X.Y[.Z…]` `` (segments capitalized, `::` params allowed), keeping only names that **resolve** in the configured depots — non-resolving mentions are ignored here (dangling cites are the index linter's concern, not this check's)
- **forward check** — `undeclared-dependency` POI: a resolving mention not covered by any declared target and not blessed
- **reverse check** — `unhonored-dependency` POI: a `depends` target (dotted-name form) never mentioned in the expanded text. `copy`/`derived` froms are **exempt** from the reverse check — their body materializes the target; the name need not appear
- **POI identity** binds to `(file, name, resolution)` so a bless survives until that pair's situation changes — same discipline as `derived-stale` ("a further dep change mints a new POI")
- **baseline flood** — first activation on an existing skill floods `undeclared-dependency`; mitigation is a bulk bless: `agentos skillware bless --skill S --kind undeclared-dependency --all` (ratchet-style baseline; new mentions after the baseline still flag)
- naming note: files/spans in `depends` froms participate in both checks by their locator string presence? **No** — v1 scopes the sync to dotted-name targets only; file/span `depends` targets are declared-only (no mention check either way). Recorded as a conscious v1 boundary.

## Execution.Plan

Each slice is independently observable; run `python -m pytest agentos-py/tests/test_skillware.py` per slice. RED→GREEN: write the failing test first where marked.

### Slice 1 — `depends` construct in the parser
- add `depends` to the registry as a **void command** (`model.py`): parsed into a construct/recipe-like record carrying `froms`; no body; no end required; opening it closes nothing and nothing needs closing
- RED: test that `$kw: depends --from Concept.A --from Concept.B` parses with zero findings and exposes both targets; test that a `depends` with a body line under it is a finding
- GREEN: implement; existing tests stay green
- check: parse fixture with `depends` among `text`/`copy` constructs round-trips through `parse_skw_source`

### Slice 2 — mention extraction + resolution helper
- new pure function in `build.py` (or a small `mentions.py`): `extract_mentions(text) -> set[str]` (regex over backticked dotted names) and `resolve_mentions(skillware, names) -> set[str]` reusing the depot cache path of `_resolve_locator`
- RED: unit tests — extracts `` `Index.Ontology` ``, `` `Turn.Type::Project.Index.Gate` ``; ignores lowercase/`file.md` paths/single-segment names; resolution keeps only depot-resolving names
- check: function-level tests only; no checker change yet

### Slice 3 — dependency-sync pass in `check_skill`
- after the existing per-file checks (only when parse and expansion succeeded): compute declared set (slice 1 records + recipe froms), mention set (slice 2 over `expansion.fresh_lines`), emit `undeclared-dependency` and `unhonored-dependency` POIs per the decisions above
- RED: fixture skill with a depot: (a) a src mentioning a resolving block with no declaration → `undeclared-dependency`; (b) a `depends` on a block never mentioned → `unhonored-dependency`; (c) declared + mentioned → clean; (d) copy-recipe target unmentioned → clean (exempt)
- check: `agentos skillware check --skill <fixture>` shows the new POI kinds with stable hashes; blessing one suppresses it on re-run; changing the mention re-mints

### Slice 4 — bulk bless
- extend `_cmd_skillware_bless` (`commands.py`): `--kind <poi-kind> --all` blesses every current POI of that kind for the skill (loops `check_skill` output through `bless_skill`); keep single-hash form unchanged
- RED: test bulk bless clears all `undeclared-dependency` POIs; a subsequently added mention still flags
- check: CLI help shows the new flags; exit codes unchanged

### Slice 5 — acceptance on a real surface
- run `agentos skillware check --skill agentos-md/skills/agentos-index` (its `skillware.json` must configure the `agentos-pkg` depot — add if missing, that is config, not content)
- expected observable: `undeclared-dependency` POIs for the index-block names its references mention (e.g. `Verbatim.User.Gated`, `Index.Ontology`) — the exact class of drift that motivated this feature
- do NOT bless or edit those surfaces; report the POI list as the acceptance evidence

### Risks / deviation triggers
- void-command support may not fit the parser's stack frames → use the empty-body fallback (Design.Decisions) and log it
- mention regex over-matching in code fences/examples → acceptable v1 noise (bless path exists); log examples encountered
- `skillware.json` schema for depots may differ from assumed → inspect `load_skillware()` first; adapt, log
- performance: depot parse per file → reuse the existing `_depot_cache`; resolve the mention set against one prebuilt name index per depot if slow

### Acceptance signals
- all new tests green, existing suite green
- slice 5 produces the expected POI class on `agentos-index`
- `bless --kind --all` then re-check → 0 POIs of that kind; introducing a new undeclared mention → exactly one new POI

## Impl.Log

- 2026-07-16 — pre-edit checkpoints created per execution workflow: `agentos-md` commit `50e07e0`, `agentos-py` empty commit `507a46f`.
- 2026-07-16 — implemented parser support for void `$kw: depends --from ...` declarations, preserving explicit close requirements for body-bearing commands.
- 2026-07-16 — implemented backticked dotted-name mention extraction/resolution, dependency-sync POIs (`undeclared-dependency`, `unhonored-dependency`), and hash-based suppression for blessed dependency-sync situations.
- 2026-07-16 — extended `agentos skillware bless` with `--kind <poi-kind> --all`; single `--poi` form remains supported.
- 2026-07-16 — verification: `uv run python -m pytest tests/test_skillware.py -q` passed (`60 passed`); `agentos skillware bless --help` shows `--kind` and `--all`.
- 2026-07-16 — real-surface acceptance: `agentos skillware check --skill /Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-index` reported 77 `undeclared-dependency` POIs across 13 checked files; no blessings or content edits were applied to `agentos-index`.
