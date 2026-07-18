# Skillware Span Labels — Impl.Req

## Impl.Abstract

- **Goal**: implement span labels per the landed `Skillware.Construct` lines (`^c20260711-1u`): a `^label` token on any declaration (bare `^label` = labeled `text`), `end-^label` closers, `path^label` / file-local `^label` locators, fine-grained span hashing, src-only stripping — plus the skill teaching it.
- **Design source**: this session (2026-07-11 morning); index capture `^c20260711-1u` on 107 `Skillware.Construct`.
- **Out of scope**: labels on hand-owned plain files (labels are src machinery); `to:` label targets beyond what `from:` resolution gives for free; label renaming tooling.
- **Repos**: `agentos-py` (parser, locators, lock keys, tests), `agentos-md` (agentos-skillware content).
- **Status**: executed 2026-07-11 — all slices done; verification green; changes uncommitted for review

## Impl.Index

### Design.Decisions

- **declaration grammar**: the declaration line may carry one `^label` token — `> [!skw]- ^x` (labeled `text`), `> [!skw]- derived ^x`, `> [!skw]- router ^x`. Label form: `^` + `[A-Za-z0-9_-]+`. A label duplicated within one file → finding. A declaration with a label token but no command = the `text` primitive with that label.
- **closers**: `end-^x` closes the innermost construct iff its label is `x` (else mismatch finding naming both accepted owners); `end-<command>` keeps working; multi-close lines may mix forms (`end-^x end-router`).
- **locators** (`from:` values): `path^label` — the labeled span in that src file; bare `^label` — file-local (the current src). Resolution: parse the target src, find the labeled construct, take its body, strip any nested machinery (parse+emit on the slice), trim. Missing label → unresolvable finding. `path#Region` unchanged. A locator may not combine `#` and `^`.
- **fine-grained hashing falls out**: the dep hash is over the extracted span body — edits elsewhere in the target file do not touch it, so a `from: file^label` consumer goes `derived-stale` only when the labeled span itself changes.
- **lock keys**: a labeled recipe keys by its label (`^x`) instead of `heading[@ordinal]` — position- and heading-independent lock identity. `recipe_key` returns `^label` when present; unlabeled recipes keep the v2 heading/ordinal scheme. Existing locks are unaffected (no labels exist yet).
- **emit**: nothing new — the label lives on the declaration line, which is already stripped machinery; compiled surfaces never carry labels.
- **model surface**: `SkwRecipe` and `SkwConstruct` gain `label: str | None`.
- **skill content** (agentos-md): `lang.skw.md` — label token in Construct Grammar, `end-^label` in the closure rules, `^label` forms in Locators, a labeled example in the fenced grammar block; expected `derived-stale` on `doctrine#The Construct In Brief` (dep = `lang#Construct Grammar`) → proper re-derive. Light mention in `author.md` (labels as the stable-address choice for imported spans; renaming a label breaks importers).

### Current.State *(inspected this session)*

- v2 parser (`model.py`): stack parser, owned ends, multi-close token loop (`end-` prefix parse), `recipe_key` heading/ordinal; 23 skillware tests / 313 suite green (587).
- `build.py`: `_resolve_locator` splits on `#` only; `expand_file` hashes resolved locator lines; lock keyed via `recipe_key`.
- `agentos-skillware`: 7 all-ok surfaces; `lang.md#Construct Grammar` is the doctrine digest's dep.
- 107 `Skillware.Construct` carries the three label lines (`^c20260711-1u`); linter clean.

## Execution.Plan

### S1 — parser: label tokens + label closers (agentos-py)
- what: RED — labeled text (bare `^x`), labeled derived, `end-^x` correct close, label mismatch finding, duplicate label finding, label never in compiled emit; GREEN — declaration token parse, frame label, closer matching, per-file label registry
- check: new tests + full skillware file green
- status: done

### S2 — locators + hashing + lock keys (agentos-py)
- what: RED — copy from `path^label`, derived from local `^label`, missing-label finding, fine-grained staleness (edit outside the span → no flag; edit inside → `derived-stale`), labeled recipe lock key `^x`; GREEN — `_resolve_locator` `^` form with current-file context, span extraction with machinery strip, `recipe_key` label branch
- check: skillware tests green; full pytest + ruff clean
- status: done

### S3 — the skill teaches labels (agentos-md)
- what: `lang.skw.md` updates (grammar, closure, locators, fenced example with a label); re-derive `doctrine#The Construct In Brief`; `author.md` stable-address note; rebuild; final pass — pytest, both skill checks, index linter
- check: all green; lang.md documents the label forms
- status: done

### Acceptance signals
- a labeled span authored in one src is importable as `path^label` from another and locally as `^label`
- its consumer drifts only with the span, not the file
- compiled surfaces carry zero labels; both skills all-ok; suite green

### Risks / deviation triggers
- if the multi-close token loop and `^` parsing collide (a command legitimately starting with `end-`? none exist), record and disambiguate by reserved-prefix rule
- if slice-level machinery stripping for label extraction fights the parser API, extract via a nested `parse_skw_source` on the body lines and strip its machinery spans — additive, no API break

## Impl.Log

- **checkpoints**: both repos checkpointed as found (agentos-md carried the trait/label index captures; agentos-py carried the uncommitted 587 v2 engine work — captured per the as-found rule).
- **S1**: RED (3 tests), GREEN — `^label` token parse on declarations (bare `^label` = labeled `text`), `label` on `SkwRecipe`/`SkwConstruct`, `end-^label` matching with dual-owner mismatch messages, per-file duplicate-label finding, `recipe_key` label branch. 26 tests green.
- **S2**: RED (2 tests), GREEN — `_resolve_locator` `^` form (`path^label` + file-local via the expansion stack), `_labeled_span` extraction with nested-machinery strip, fine-grained staleness verified (edit outside span → clean; inside → `derived-stale` keyed `^consumer`). 28 tests, 318 suite, ruff clean.
- **deviation (fence-unaware region extraction, latent since v1)**: found via a missing expected `derived-stale` — `_region_body` treated a heading *inside a fenced example* as a section boundary, so `lang#Construct Grammar`'s dep hash covered only the intro paragraph and edits below the example never registered (a silent-staleness hole, the exact failure class the system exists to prevent). Fixed RED-GREEN: `_region_body` now fence-aware. The doctrine digest then correctly flagged `derived-stale` and was properly re-derived (label-aware wording).
- **S3**: lang grammar/closure/locator updates with a labeled fenced example; author stable-address guidance; doctrine re-derive. Final: 29 skillware tests / 319 suite, ruff clean, both skills all-ok, index linter 0/0.
