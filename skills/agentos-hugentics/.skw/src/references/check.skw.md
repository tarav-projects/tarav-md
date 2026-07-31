# Index.Check.Operation.Module

> $kw: --from Appendix.Discovery --from Index.Depot --from Index.Edition.Turn --from Index.Linter --from Index.Presumption --from Line.Type --from Line.Verbatim.Gate --from Reviewed.Content --from Support.Set --from Touched.Authority --from User.Attention
> --dev-from references/index-context-assembly.skw.md

Use this module when the caller wants deterministic diagnosis, linter findings, or post-edit validation for an index depot or explicit index/appendix surface.

`--check` and `--lint` both call this module.

`Line.Verbatim.Gate` is a protocol check that economizes `User.Attention`; it is independent of touched-data authority.

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
- missing-reference POI: `Index.Linter/Line.Unlinked` warns by default for every live chapter, appendix, or agendix kernel line without a support reference; `--coverage line` adds the reference-presence meter and `--warn-unlinked` remains a compatibility alias
- block grounding check: add `--coverage block` to report chapter concept blocks containing lines without a resolvable nonempty `Support.Set`; `--coverage all` enables the reference-presence and resolved-grounding meters
- scoped reporting: add `--scope <path>` to filter findings, per-check counts, summaries, and coverage meters to a file or directory while checks still run over the full configured depot
- approval evidence: add `--check line-approval` to require an approval-typed user member on each anchored line in scope
- reviewed-content gate: add `--check line-verbatim-gate` to verify tokenized approval cargo and deterministic material equivalence between presented and landed line content; a passing line is `Reviewed.Content`

## Material Equivalence

The checker verifies sufficient deterministic evidence of content correspondence without parsing an `Index.Edition.Turn` layout:

- the proposal and approval turns must resolve and both carry the token
- the proposal must contain the landed line after removing trailing anchors
- Unicode-equivalent characters are normalized
- case and whitespace differences are ignored, including indentation and wrapping
- every other character remains significant

This policy certifies presentation followed by explicit token approval. It does not certify that the user read or evaluated the content, and it does not establish `Touched.Authority`; authority derives independently from the line's `Support.Set`.

## Built-In Grounding Checks

- the installed `agentos index linter` runs parser-backed `Line.Type` syntax checks (bracket form, known act codes, `[GR]` trailing anchor; `AS:` outside `agendix/` is an ERROR), default `Index.Linter/Line.Unlinked` POIs for every live line missing a reference, and the chatlas grounding-provenance check
- `--coverage line` measures syntactic support-reference presence; it never claims that a present reference resolves
- `--coverage block` enables `Index.Linter/Block.Ungrounded`: a block is grounded iff every kernel line has a support reference resolving to a nonempty `Support.Set` (empty blocks count grounded)
- a missing chatlas backend renders `Index.Linter/Grounding.Provenance` as a blocked check, never a silent skip
- `agentos anchory scan --depot <chatlas-root>/anchory --src-file <file> --regex '\^(?P<anchor>[a-z][0-9]{8}-[0-9]+[a-z]?)'` remains the record-level spot check for a single file
- `Index.Linter/Line.Approval` and `Index.Linter/Line.Verbatim.Gate` are currently opt-in because legacy lines have not completed the approval-evidence campaign; their warnings are review debt, while malformed token cargo or materially different proposed content is an error

## Beyond The Linter

> $kw: --derived
> --from references/type.skw.md#Semantic Lints
> --intent compress the semantic-lint catalogue into one routing line: agent work,
> --cont not linter checks; findings reported, fixes through --edit

- semantic lints on typed lines (contradicting `[DC]`s, violated `[CT]`s, reintroduced `[RJ]`s, overridden `[FR]`s) are agent work, not linter checks — see `references/type.md`; report findings, route fixes through `--edit`
- an ungrounded live line is grounding debt carrying `Index.Presumption`, not disposable text; a finding does not prescribe deletion or demotion

> $kw. end

## Post-Edit Check

- after an approved index or appendix edit, run the linter over the edited depot or explicit edited surfaces
- for newly approved lines, also run `--check line-approval --check line-verbatim-gate --scope <edited-path>`; new tokenized lines should add no findings even while legacy warnings remain elsewhere
- if the edit added or touched anchors, run the anchor resolvability scan over the edited files
- if findings existed before the edit, do not treat them as new regressions unless the edit worsened or touched them
- if the edit creates a new error or warning, report it before considering the edit complete
