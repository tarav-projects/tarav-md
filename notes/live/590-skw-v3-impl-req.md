# 590 — skw v3: `$kw` grammar, Closure.Parser::Skw, Poi.Linter output, bless verb — Impl.Req

## Impl.Abstract

- status: draft
- mode: `Alignment.Mode::Autonomous` (--dev --AUTO)
- scope: rework the skw parser to the captured v3 surface grammar (`$kw:` / `$kw.`), recast the engine in the new 107 vocabulary (`Closure.Parser`, `Poi.Linter`, `Poi.Bless`), add the `agentos skillware bless` verb, recast `check` output to legend + bare rows with stable POI identities, migrate all srcs off `[!skw]` with byte-identical compile verification, re-derive the affected skill modules, and land the realization lines on 107.
- source context: the v3 syntax capture on `Skillware.Construct` (107, `^20260712-7`); the parser/linter cluster landed 2026-07-12 (`Closure.Parser`, `Poi.Linter`, `Poi.Bless`, `Structure.Ratchet`, all `^20260712-17`); the md-library linter steal (legend + hash/resolve model) accepted in chat.
- out of scope: dividers / end-free `Annotation.Point` sections (annotated-only backend feature); non-`>` carriers (`#`, `//` for code backends); `pointer` materialization; renaming the verdict vocabulary (`derived-stale` etc. stay; they are presented as POI types); any `agentos skw` CLI rename.

## Impl.Index

### Grammar (normative for this implementation)

- machinery sigil pair on the md carrier: `> $kw: …` opens, `> $kw. …` belongs. Every machinery line carries the sigil; nothing skw is inferred from bare host syntax.
- declaration: `$kw: <command> [^label] [--flag value …]` — CLI-style; command is the first token; one optional `^label` token; flags inline when short.
- explicit label command: `label ^x` declares a labeled literal (compiles as `text`); command-less declarations are invalid.
- belonging lines, contiguous with the declaration: `$kw. --flag value` adds a flag occurrence (`--from` repeats); `$kw. <plain text>` continues the previous flag's value. A non-end `$kw.` line that is not contiguous with an open declaration block is a parse error (stray belonging line).
- closer: `$kw. end-<command>` or `$kw. end-^label`; a multi-close line (`$kw. end-a end-b`) unwinds innermost-first; bare `end` invalid; end lines take no args and consume only their own line.
- flag vocabulary: `--from` (address, repeatable), `--intent` (derivation rule), `--to` (accepted and stored, no engine semantics yet). Unknown flags are parse errors.
- flag value parsing: after command/label, `--flag` starts a value that runs to the next `--flag` token or end of line (from-targets may contain spaces: `references/lang.skw.md#Construct Grammar`).
- commands unchanged: primitives `text`, `copy`, `derived` (+ `label` as labeled-text sugar); structural `router`, `when`, `then`. Fenced code is inert. Headings close nothing. No indentation; bodies at column 0.
- leftover `[!skw]` callout lines after migration are NOT machinery (No.Legacy.Allowed — no dual parsing); the linter raises a soft `legacy-callout` POI when it sees one outside a fence.

### Closure.Parser::Skw recast

- the parser is a `Closure.Parser`: `Parse.Floor` = all skw machinery lines well-formed, constructs closed, labels unique, router rows sane. Below the floor → parse errors (current `SkwFinding` stream). Above the floor everything lands in a node: recognized constructs or opaque text.
- the parser emits no POIs — `SkwSource.findings` are parse errors only (this is already true; make it doctrine in docstrings and naming).
- `check` is the `Poi.Linter`: parse errors gate — a file with parse errors reports them as `parse-error` POIs and its semantic checks (copy-drift, derived-stale, build-state) do not run. Other files still check normally (one broken file never blinds the pass).

### Poi.Linter output (md-library steal)

- every POI gets a stable identity hash: `sha256(target|kind|key|current-relevant-state)` truncated to 10 hex chars — stable across runs while the situation is unchanged; changes when the situation changes.
- human output: a once-per-kind legend (kind, one-sentence meaning, prescribed response) printed only for kinds present in the run, then bare rows: `- [kind] target :: key (hash)`. JSON output carries the same fields.
- per-kind fix protocols stay in `agentos-skillware/references/check.md` (re-derived in slice 6), not in format strings.

### Poi.Bless (bless verb)

- `agentos skillware bless --skill <path> --poi <hash>`: for a `derived-stale` POI, rewrite that recipe's locked dep hashes to the current dependency hashes; body and target untouched; print what was blessed (target, key, per-dep old→new). Loud and auditable — the lock diff is the audit record.
- blessability: only `derived-stale` is blessable. `parse-error` never (below the floor); `copy-drift`/`stale-build`/`never-built` have mechanical fixes (build); `hand-edited` is a judgment call resolved by editing, not blessing. Blessing a non-blessable or unknown hash is a CLI error naming the reason.
- no-silent-blessing survives: build still carries old dep hashes forward; the only two flag-clearing acts are re-derivation and explicit bless.

### Migration

- 10 machinery-bearing srcs: `agentos-index2` (SKILL, edit, ground, back-link, check) and `agentos-skillware` (SKILL, check, doctrine, lang, author). Mapping: `> [!skw]- <decl>` → `> $kw: <decl>`; `> from: X` → `> $kw. --from X`; `> intent: …` (+ bare `>` continuations) → `> $kw. --intent …` (+ `> $kw. …` continuations); `> [!skw]- end-…` → `> $kw. end-…`.
- fenced `[!skw]` examples inside lang/author/doctrine are content, not machinery — they are rewritten to v3 as part of the doc re-derive (slice 6), not the mechanical migration.
- verification: byte-identical compiled targets (git diff clean on runnable files after rebuild) and lock continuity (recipe keys and body/dep hashes unchanged → no new derived-stale).

### Index landing (realization lines, gated by this Impl.Req's user-approved scope)

- `Closure.Parser`: append `- [DC] realized: the skw parser is `Closure.Parser::Skw` — floor: well-formed, closed `$kw` machinery; above it, construct nodes and opaque text ^20260712-17`
- `Poi.Linter`: append `- [DC] realized: `agentos skillware check` — parse errors gate per file; POIs carry stable identity hashes; legend + bare-row output ^20260712-17`
- `Poi.Bless`: append `- [DC] realized: `agentos skillware bless --poi <hash>` — rewrites the recipe's locked dep hashes, body untouched ^20260712-17`

## Execution.Plan

1. **Parser rework (RED→GREEN)** — status: pending
   - RED: rewrite the grammar tests in `agentos-py/tests/test_skillware.py` to v3 syntax (all of them — No.Legacy.Allowed), add new-grammar tests: inline flags, flag-value-with-spaces, `--intent` continuation, stray `$kw.` line, unknown flag, `label ^x`, multi-close, `end-^label`, legacy-callout POI absence from parser (parser ignores `[!skw]`).
   - GREEN: rework `model.py`: `_MACHINERY_RE` for `$kw:`/`$kw.`, declaration/flag tokenizer, contiguous belonging-block reader, closer handling, stray-line finding. Keep dataclasses, `recipe_key`, stack semantics, fence-inertness. Docstring recast to `Closure.Parser::Skw`.
   - check: new grammar tests pass; whole module suite runs.
2. **Build/emit alignment** — status: pending
   - `build.py` consumes spans unchanged; verify src-refresh preserves v3 machinery verbatim and compile strips it. Update `[!skw]` mentions in docstrings/help (`build.py`, `commands.py` parser description).
   - check: expand/emit tests green.
3. **Src migration, byte-identical** — status: pending
   - snapshot compiled targets + lock for both skills; scripted transform of the 10 srcs; `build` both skills; assert compiled targets byte-identical (git diff), lock derived deps unchanged, `check` all-ok.
4. **Poi.Linter recast of check** — status: pending
   - RED: tests for parse-error gating (a file with a parse error reports `parse-error` POIs and no semantic POIs for that file; sibling files unaffected), POI hash stability across runs, hash change when deps move again, legend printed once per present kind, bare-row format, `legacy-callout` POI on a leftover `[!skw]` line.
   - GREEN: `build.py` check_skill returns POI records (kind, target, key, hash, detail); `commands.py` renders legend + rows; JSON payload extended.
5. **Bless verb (RED→GREEN)** — status: pending
   - RED: bless a real derived-stale POI → lock deps rewritten, body/target untouched, subsequent check all-ok, output names old→new; bless `parse-error`/unknown hash → CLI error; blessed situation re-drifts → new hash, new POI.
   - GREEN: `bless_skill(skill_root, poi_hash)` in `build.py`; `bless` subcommand with `--poi` in `commands.py`.
6. **Doc modules re-derive + rebuild** — status: pending
   - `lang.skw.md`: full grammar rewrite to v3 (normative spec + fenced examples). `author.skw.md`: workflow/examples. `check.skw.md`: verdicts→POI kinds table, legend/bare-row reading, bless protocol and blessability rules, re-derive pass updated. `doctrine.skw.md`: derived sections re-derived (`The Construct In Brief` depends on lang `#Construct Grammar`); model narrative mentions `Closure.Parser::Skw`/`Poi.Linter`/`Poi.Bless`. SKILL src if it mentions `[!skw]`.
   - `agentos-index2` srcs: no doc content changes expected beyond the mechanical migration; verify with check.
   - check: build + check all-ok on both skills; derived bodies genuinely re-derived where deps changed (no silent blessing, no lazy body-keeps).
7. **Index realization lines** — status: pending
   - append the three `[DC]` lines (Impl.Index wording) to 107; run `agentos index linter`; run skillware check for doctrine drift (Agentos.Skillware cluster unchanged → expect ok; re-derive if flagged).
8. **Full verification** — status: pending
   - full agentos-py test suite; `agentos skillware build/check/status` on both skills from agentos-md; grep: zero `[!skw]` outside fences in srcs; report.

Deviation triggers: byte-identical check fails → stop, diagnose in src transform, never hand-adjust compiled targets; lock shows new derived-stale after migration → key-shift bug, fix `recipe_key` path, do not bless; any test regression outside skillware → investigate before proceeding.

Acceptance: all slices checked, suite green, both skills all-ok, `[!skw]` gone from src machinery, bless round-trip demonstrated, 107 lines landed and linter-clean.

## Impl.Log

- (empty)
