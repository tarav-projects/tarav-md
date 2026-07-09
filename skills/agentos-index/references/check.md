# agentos-index --check

Use this module when the caller wants deterministic diagnosis, linter findings, or post-edit validation for an index depot or explicit index/appendix surface.

`--check` and `--lint` both call this module.

## Check Model

- use `agentos index linter` for deterministic index checks
- the linter is parser-backed for index model concerns: concept headings, router rows, kernel lines, line types, source-axis placement, anchor spans, unlinked-line coverage, and block grounding coverage are read from the typed index model
- prefer depot-first checking with `--depot` when a full `Index.Depot` is in scope
- use explicit `--index` and `--appendix` only when the caller has scoped the check to individual surfaces
- resolve finding and check codes through the `agentos-pkg` `Index.Linter` concept and normal `Appendix.Discovery`
- report existing unrelated findings distinctly from findings caused by the current edit

## Check Commands

- depot check: `agentos index linter --depot <depot-root>`
- explicit surface check: `agentos index linter --index <index-path> --appendix <appendix-path>`
- structured output when useful: add `--json`
- line coverage check: add `--coverage line` to warn for unanchored chapter and appendix kernel lines; `--warn-unlinked` is a compatibility alias; agendix kernel lines are checked for anchors without this flag
- block coverage check: add `--coverage block` to warn for chapter concept blocks without a `[GR]`-anchored `Grounding.Head`; `--coverage all` enables both line and block meters
- scoped reporting: add `--scope <path>` to filter findings, per-check counts, summaries, and coverage meters to a file or directory while checks still run over the full configured depot

## Built-In Grounding Checks

- the installed `agentos index linter` runs parser-backed `Line.Type` syntax checks (bracket form, known act codes, `[GR]` trailing anchor; `AS:` outside `agendix/` is an ERROR), `Index.Linter/Line.Unlinked` for agendix lines, and the chatlas grounding-provenance check (anchors resolve; landing turns exist; roles match the source axis)
- `--coverage line` extends `Index.Linter/Line.Unlinked` to chapter and appendix kernel lines as a coverage meter; warnings do not change the exit code
- `--coverage block` enables `Index.Linter/Block.Ungrounded`; inline anchors never satisfy the block meter, and `Grounding.Head` never satisfies the line meter
- a missing chatlas backend renders `Index.Linter/Grounding.Provenance` as a blocked check, never a silent skip
- `agentos anchory scan --depot <chatlas-root>/anchory --src-file <file> --regex '\^(?P<anchor>[0-9]{8}-[0-9]+)'` remains the record-level spot check for a single file

## Beyond The Linter

- semantic lints on typed lines (contradicting `[DC]`s, violated `[CT]`s, reintroduced `[RJ]`s, overridden `[FR]`s) are agent work, not linter checks — see `references/type.md`; report findings, route fixes through `--edit`

## Post-Edit Check

- after an approved index or appendix edit, run the linter over the edited depot or explicit edited surfaces
- if the edit added or touched anchors, run the anchor resolvability scan over the edited files
- if findings existed before the edit, do not treat them as new regressions unless the edit worsened or touched them
- if the edit creates a new error or warning, report it before considering the edit complete
