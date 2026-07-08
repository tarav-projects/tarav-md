# Linter Grounding Provenance — Impl.Req

## Impl.Abstract

- **Goal**: the index linter checks grounding provenance — anchors resolve, landing turns exist, turn role matches the source axis (`user` unless `AS:`; `AS:` legal only in `agendix/`) — via a check socket in the core linter and a chatlas-powered check registered at the composition root.
- **Scope**: linter external-check socket + CPU-local `Line.Type`/`AS:` checks (`agentos-py`); grounding-provenance bridge check (`agentos-chatlas-py`, full chatlas power); CLI wiring (`agentos-cli`); closes most of `notes/live/571`.
- **Out of scope**: the physical packaging split into `packages/` workspaces (`Dependency.Profile.Split` says no new profile is needed here — the bridge's profile is a subset of chatlas-py's; the split is its own future effort and this code moves into it unchanged); semantic lints (contradicting `[DC]`s etc. — agent work per `references/type.md`); typing legacy untyped lines.
- **Repos**: `agentos-py` (`src/agentos/index/linter.py`, `commands.py`, tests), `agentos-chatlas-py` (new `src/agentos_chatlas/index_checks.py`, tests), `agentos-cli` (wiring + e2e). Reinstall after CLI changes (`uv tool install --reinstall --editable .` from `agentos-cli/`).
- **Source**: this design session — `Dependency.Profile.Split` (102, anchored `@20260708-7`), `Line.Type` source-axis lines (106), `Grounding.Hugentic.Authority` user-turn-only `[CT]` (105), `Chatlas.Anchory` user-turn `[CT]` (chatlas 100), `notes/live/571-line-type-linter-checks-parking.md`.
- **Status**: implemented (2026-07-08); all four slices; suites green (agentos-py 277, chatlas-py +6 bridge tests, cli 56); both live depots clean at 16 checks with provenance verified

## Impl.Index

### Design.Authority
- `Dependency.Profile.Split`: core defines sockets (registration points, not data contracts); bridges wield full libraries; the CLI composes; cores never import bridges
- placement decision (user-aligned): the bridge's dependency profile (`agentos.index` + `agentos.anchory` + chatlas) is a subset of chatlas-py's existing profile → it lives as a module inside `agentos-chatlas-py`, no new distribution
- the contract is NOT narrowed to a probe tuple — the check connects all the way to chatlas (user decision)

### Current.State *(inspected, cited)*
- linter: `CHECKS` tuple iterated by `run_linter` (`linter.py:340-357`); `LinterCheck` (`:149`) pairs metadata with a `run(state)` callable; findings/gates typed (`LinterFinding:117`, `GateResult:142`); `LinterState` holds parsed surfaces and concept blocks
- linter has no notion of `Line.Type` syntax or anchors today; `agendix/` folders are outside its configured surfaces (depot resolver knows chapters/appendix/router only)
- chatlas: anchor resolution (`chatlas_anchory_depot`), session model load, event/turn access, role reading all library-importable; `agentos-cli` already composes via `register_chatlas_commands` (`cli.py:23`)
- the register currently holds ~17 anchors; live index files carrying anchors: `102/105/107-design.md`, several `appendix/*.md`, `agendix/*.md` in two depots

### Socket.Contract
- `run_linter(..., extra_checks: Sequence[LinterCheck] = ())` — external checks run after built-ins, same `LinterState`, same findings/summary/JSON rendering
- external checks may gate themselves (e.g. "chatlas unavailable" → blocked with reason, reusing `GateResult`) — a missing backend degrades to a visible blocked check, never a crash or silent skip
- the socket is registration-only: no chatlas-shaped types in `agentos-py`

### Core.Checks *(CPU-local, no chatlas — from 571)*
- typed-line syntax: a line starting `- [` must match `- \[(AS:)?[A-Z]{2}\] ` (warning)
- known act code: bracket code in the registered set `DF DC CT RJ PR FR EX GR` (warning; keep the set a module constant with a comment pointing at `Line.Type.Vocabulary` — cheap now, index-sourced later)
- `[GR]` lines must carry a trailing anchor token `@\d{8}-\d+` (warning)
- `AS:` outside `agendix/` files = ERROR (`Index.Linter/Source.Axis.Placement`) — the index proper is user-turn-grounded
- untyped lines: NOT checked (pre-fence legacy by design)
- agendix surfaces: depot resolver learns `agendix/` as a lintable surface for these checks only (same filename convention as appendix)

### Bridge.Check *(agentos_chatlas/index_checks.py)*
- `grounding_provenance_check(...) -> LinterCheck` (or a factory taking the chatlas root): for every anchor token in configured surfaces —
  - resolves through the chatlas anchory depot; unresolvable → ERROR (`Anchor.Unresolvable`)
  - record `app == "chatlas"` → loads the session model, locates the landing turn near `at`; no turn in bounds → ERROR (`Anchor.Turn.Missing`)
  - reads the landing turn's role: `assistant` role on a line without `AS:` → ERROR (`Anchor.Provenance`); `AS:`-marked line whose landing is a `user` turn → warning (stale marker)
  - non-chatlas records: skipped, not errors (anchory is application-agnostic)
- uses full chatlas machinery freely (model load, event scan); no narrowed contract

### Composition
- `agentos-cli` builds the linter invocation with `extra_checks=[grounding_provenance_check(...)]` — the `register_chatlas_commands` pattern applied to checks
- `agentos index linter` therefore runs provenance checks in the installed tool by default; library users of `agentos-py` alone get core checks + no bridge (clean degradation)

## Execution.Plan

### S1 — Socket + core Line.Type checks (agentos-py, test-first)
- what changes: `run_linter` gains `extra_checks`; new core checks per Core.Checks; depot resolver includes `agendix/`
- RED (`tests/test_index_linter.py` fixtures): malformed bracket, unknown code, `[GR]` without anchor, `AS:` in a chapter file (error) vs in `agendix/` (legal), untyped lines untouched; an injected dummy `extra_check` runs and reports; a self-gating extra check renders blocked
- check: suite green; live `--depot skills/agentos-pkg` stays clean (current surfaces are well-formed)
- observable: the linter enforces the fence syntax

### S2 — Provenance bridge (agentos-chatlas-py, test-first)
- what changes: `index_checks.py` with the provenance `LinterCheck`
- RED (`tests/`): fixture depot + fixture index file with anchors — resolvable user-turn anchor passes; unresolvable errors; assistant-landing without `AS:` errors; `AS:` line landing on user turn warns; non-chatlas record skipped
- check: suite green
- observable: provenance violations are findings, mechanically

### S3 — Composition + live acceptance (agentos-cli)
- what changes: linter command wiring passes the bridge check; e2e test
- check: reinstall; live `agentos index linter --depot skills/agentos-pkg` (agentos-md) and `--depot skills/agentos-chatlas-pkg` (chatlas-md) — all ~17 live anchors verified; expect clean or genuinely-found issues (report, do not silently fix)
- observable: `agentos index linter` validates the full grounding chain end to end

### S4 — Docs + closure
- what changes: `agentos-py/AGENTS.md` (socket + check codes); `agentos-index` `references/check.md` (provenance checks now IN the linter — move them out of "Beyond The Linter"); `notes/live/571` marked closed except semantic lints; propose (gated, do not self-write) a `[DC]` on `Index.Linter` (104): external checks via the socket, provenance via the chatlas bridge
- check: references match the real CLI behavior

### Acceptance signals
- `agentos index linter --depot <depot>` reports anchor resolvability and turn provenance with zero extra flags
- `AS:` outside agendix is an ERROR; all live depots lint honestly
- all three repos' suites green; `No.Regression.Tests.Allowed` respected

### Risks / deviation triggers
- live acceptance may surface real provenance findings in existing anchors (e.g. hints vs landings) — report them as findings to the user; fixing lines is gated index work, never done inside this execution
- landing-turn location semantics ("near `at`") must match `Chatlas.Anchory` minting validation — reuse the same nearest-event logic chatlas uses in `chatlas_anchory_register`, do not reimplement
- if `LinterState` surface parsing needs >small changes for agendix inclusion, stop and surface — resolver scope creep is a design decision

## Impl.Log

- 2026-07-08: executed in `Alignment.Mode:Autonomous`. S1: socket (`extra_checks`) + `Index.Linter/Line.Types` core check (syntax, unknown code, `[GR]` anchor, `Source.Axis.Placement` error); agendix files discovered as `appendix`-sibling and `depot/agendix` — no `SurfaceKind` ripple (the deviation trigger did not fire; checks walk config paths directly).
- S2: `agentos_chatlas/index_checks.py` — provenance check with per-session model cache; landing-turn role = nearest timestamped message event to `at` (mirrors mint validation semantics); non-chatlas records skipped; missing depot gates to blocked.
- S3: `register_index_commands(..., extra_linter_checks=…)` + composition in `agentos-cli`; live acceptance: both depots 16 checks, 0 findings — all live anchors verified end to end.
- open-space decision: act-code list is a module constant in the core linter with a comment pointing at `Line.Type.Vocabulary` (index-sourced later if cheap).
- open-space decision: the bridge imports the core's `_line_type_surface_files` helper (private-by-underscore but the bridge wields full libraries per design); promote to public name during the packaging split.
- gated follow-up proposed to the user (not self-written): `[DC]` on `Index.Linter` (104) for the socket + provenance checks.
