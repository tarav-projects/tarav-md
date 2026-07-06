# agentos-index --check

Use this module when the caller wants deterministic diagnosis, linter findings, or post-edit validation for an index depot or explicit index/appendix surface.

`--check` and `--lint` both call this module.

## Check Model

- use `agentos index linter` for deterministic index checks
- prefer depot-first checking with `--depot` when a full `Index.Depot` is in scope
- use explicit `--index` and `--appendix` only when the caller has scoped the check to individual surfaces
- resolve finding and check codes through the `agentos-pkg` `Index.Linter` concept and normal `Appendix.Discovery`
- report existing unrelated findings distinctly from findings caused by the current edit

## Check Commands

- depot check: `agentos index linter --depot <depot-root>`
- explicit surface check: `agentos index linter --index <index-path> --appendix <appendix-path>`
- structured output when useful: add `--json`

## Post-Edit Check

- after an approved index or appendix edit, run the linter over the edited depot or explicit edited surfaces
- if findings existed before the edit, do not treat them as new regressions unless the edit worsened or touched them
- if the edit creates a new error or warning, report it before considering the edit complete
