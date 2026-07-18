# Skillware v2 — Universal Construct — Impl.Req

## Impl.Abstract

- **Goal**: implement Skillware v2 per the landed `Skillware.Construct` index block (107, `^c20260710-4u`): one universal declaration+body+owned-end construct, fully explicit closure, position-free primitives (`text`, `copy`, `derived`), first structural commands (`router`, `when`, `then`), and migration of ALL existing srcs to the strict form — no v1 dialect survives (`No.Legacy.Allowed`).
- **Design source**: this session's design discussion (2026-07-10 evening) + the `Skillware.Construct` and recast `Skillware.Recipe` blocks; anchors `^c20260710-4u`.
- **Out of scope**: structured outlink annotations on `then` and the findability lint family (deferred — "just text at the moment", user); `libs`/stdlib cross-skill resolution; shapes; `pointer` binding.
- **Repos**: `agentos-py` (parser + build/check + tests), `agentos-md` (migration of 19 srcs, agentos-skillware content update).
- **Status**: executed 2026-07-10 — all slices done; verification green; changes uncommitted for review

## Impl.Index

### Design.Decisions

- **the construct** (normative, from `Skillware.Construct`): `> [!skw]- <command>` declaration + `> key: value` arg lines (bare `>` continuation) + flat body at column 0 + mandatory owned closer `> [!skw]- end-<command>`.
  - bare `end` (with or without dash, incl. v1's `[!skw] end`) → finding "bare end is invalid; close with end-<command>"
  - multi-close: `end-a end-b` tokens on one declaration line, processed left→right, must match the open stack innermost-first; mismatch → finding naming expected vs found
  - a heading closes nothing; a construct still open at a heading or EOF → finding (bodies therefore cannot span headings)
  - fenced lines stay inert (shipped in 586)
- **command vocabulary v2**: `text` (literal tag; leaf), `copy`, `derived` (leaf primitives — a construct opening inside a primitive body is a finding), `router` (structural; body holds `when`/`then` pairs plus free literal prose), `when`/`then` (valid only inside an open `router`, else finding; a `when` not followed by its `then` before the next `when`/router close → finding). Unknown command → finding (as v1).
- **position-free primitives**: the v1 "recipe must be first in its section" convention and its finding are dropped; any number of constructs per section, anywhere. Section heading remains the human-facing association only.
- **parser shape** (agentos-py `model.py`): stack-based construct parser replacing the v1 open-recipe scan. Public API preserved: `parse_skw_source` still returns `SkwSource` with `recipes` (copy/derived constructs, now with `command`-agnostic construct data), `findings`; spans now cover declaration/args and owned-end lines. New: constructs tree (or flat list with depth/parent) exposing `router`/`when`/`then`/`text` for structural checks. Machinery lines = every declaration, arg, and end line of every construct — `_emit` strips them all.
- **build/check** (`build.py`): emit strips all construct machinery at any nesting; copy refresh and derived tracking operate on primitive (leaf) bodies exactly as v1; lock recipe key extended from `(heading, verb)` to `(heading, verb, ordinal)` — ordinal = occurrence order within the heading — so multiple primitives per section key stably. Existing locks (one recipe per heading) migrate transparently: match `(heading, verb, 0)` falling back to `(heading, verb)`. Router/when/then are *structural only*: no lock state, no compile output beyond their stripped machinery; their checks are parse findings.
- **migration (ALL srcs, 19 files)**: index2 (12) + agentos-skillware (7); every `> [!skw]- derived` body gains `> [!skw]- end-derived` (replacing bare `> [!skw] end` where present, inserted before the closing heading/EOF where heading-closed); compiled targets must be byte-identical before/after migration (machinery strips either way) — verified by diff.
- **agentos-skillware content update** (the skill must teach its own v2): `lang.skw.md` spec rewritten — construct form, owned ends + multi-close, primitives incl. `text`, no-indentation principle, router/when/then, fenced-inert; the fenced grammar example moves to strict syntax. `doctrine.skw.md`: `Recipe In Brief` re-derive (its `lang#Recipe Grammar` dep changes). `author.md`/`check.md`/`build.md`: light touch — end-form mentions updated. Whatever `check` flags derived-stale after the lang rewrite gets a proper re-derive pass.

### Current.State *(inspected)*

- srcs carry 12 `derived` callouts and 6 bare `> [!skw] end` closers (6 bodies heading-closed); no `copy` recipes exist anywhere; no nested constructs exist (v1 could not express them).
- `model.py`: v1 scanner — `_CALLOUT_RE` verb capture, `_read_callout` fields, open-recipe + close-at-heading logic, `end` verb, first-in-section finding; fence-inertness landed in 586.
- `build.py`: `_emit` strips `callout_span`s + end spans and replaces copy bodies; lock `_recipe_states` keyed by heading; `old_recipes` dict keyed `(heading, verb)`.
- tests: 16 in `tests/test_skillware.py` (306 suite-wide); several fixtures use v1 bare-end / heading-closure and will be updated to strict form as part of the slices (accepted-design update, not legacy retention).
- both skills all-ok at start; index linter clean.

## Execution.Plan

### S1 — parser v2: construct + strict owned ends (agentos-py)
- what: RED — tests for: bare `end` finding; owned end closes; owned-end mismatch finding; multi-close incl. wrong-order finding; dangling-open at heading and at EOF findings; position-free (second construct mid-section parses, no first-in-section finding); `text` command parses as tagged literal. GREEN — stack parser in `model.py`; v1 fixtures in the file updated to strict form.
- check: new tests pass; full skillware test file green
- status: done

### S2 — structural commands + build/check over v2 (agentos-py)
- what: RED — tests for: `router` with two `when`/`then` pairs parses, machinery fully stripped from emit (nested); `when` outside router finding; `when` without `then` finding; two derived under one heading key distinctly in lock and check independently. GREEN — vocabulary + structural findings in `model.py`, `_emit`/lock ordinal in `build.py`.
- check: skillware tests green; full pytest suite green; ruff clean
- status: done

### S3 — migrate all srcs (agentos-md)
- what: rewrite 19 srcs to strict form (script: add `end-derived` closers, replace bare ends); capture each skill's compiled targets before, rebuild after, diff — must be byte-identical; `check` all-ok both skills
- check: empty target diffs; both checks exit 0
- status: done

### S4 — agentos-skillware teaches v2 (agentos-md)
- what: rewrite `lang.skw.md` (construct spec, strict example in fence); re-derive whatever `check` flags (`doctrine#Recipe In Brief` expected); touch author/check/build end-form mentions; rebuild; final pass — pytest, both skill checks, index linter
- check: all green; lang.md teaches only the strict form
- status: done

### Acceptance signals
- v1 dialect is unparseable-as-valid: bare ends and heading-closure produce findings everywhere
- all 19 srcs strict; compiled surfaces unchanged by migration (byte-diff empty), changed only by the S4 content updates
- a router/when/then section round-trips: parses, structurally checks, compiles to pure prose
- suite green (agentos-py), both skills all-ok, linter clean

### Risks / deviation triggers
- if preserving `parse_skw_source`'s return shape fights the tree model, extend `SkwSource` additively (new field) rather than breaking `recipes` consumers
- if a heading-closed derived body turns out to span subsections (body containing headings), strict closure makes it a finding — restructure that src (split or move the end) and record it
- if lock fallback matching misfires on any existing skill, rebuild once (targets identical, lock rewrites) and record the blessing rationale

## Impl.Log

- **checkpoints**: agentos-md checkpoint committed the Skillware.Construct index capture + doctrine re-derive as found; agentos-py empty checkpoint (clean).
- **S1/S2** (executed as one pass — the parser rework and structural commands interlock): stack parser landed in `model.py` (`SkwConstruct`, `machinery_spans`, `recipe_key` with `@ordinal`); `build.py` emit/lock/check keyed via `recipe_key`; v1 fixtures updated to strict form; 7 new tests (owned-end mismatch, multi-close incl. wrong order, open-at-heading/EOF, position-free + text, nesting finding, router structural checks, router compile, dual-derived ordinal keys). 23 skillware tests, 313 suite-wide, ruff clean.
- **parser bug found by the multi-close RED**: `_read_callout` swallowed an immediately adjacent callout line as an arg continuation (latent in v1 — adjacent callouts could not occur); fixed by breaking on a callout match.
- **S3**: fence-aware migration script converted 9 srcs (the other 10 are recipe-free passthroughs); rebuild reported 0 built — every compiled target byte-identical to the pre-migration snapshot; both checks all-ok.
- **S4**: `lang.skw.md` rewritten as the v2 spec (Construct Grammar with strict fenced example, Primitives incl. `text`, Structural Commands with router example); `doctrine#Recipe In Brief` re-derived as `#The Construct In Brief` against the renamed `lang#Construct Grammar` dep; SKILL router/module rows updated. Final: build 3 rebuilt, both skills all-ok, index linter 0/0, pytest 313.
- **deferred (per Impl.Abstract)**: structured outlinks on `then` + findability lints; stdlib/`libs`; shapes.
