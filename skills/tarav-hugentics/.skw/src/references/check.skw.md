> $kw: ^real-time-validation-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Real.Time.Validation.Knowledge.Module

> $kw: --from Reviewed.Content
> --dev-from references/index-context-assembly.skw.md

This is an internal `Real.Time.Capture` primitive, not a public workflow. It validates only the exact editions just landed by the foreground capture batch; broader Index diagnosis and Project/Chat reconciliation are parked in the workflow-retirement issue at `issues/100-issues.md`.

## Validation Slice

1. Run `tarav index linter --depot <depot> --anchor <new-anchor> ...` with one repeated `--anchor` selector per newly landed line.
2. For reviewed lines, add `--check line-approval --check line-verbatim-gate`; a passing line is `Reviewed.Content` for this deterministic gate only.
3. Resolve every new support dossier with `tarav chatlas2 anchory resolve <anchor>` and require its selected message assertions to remain `MATCHED`.
4. Validate and apply the real-time Chatlas2 Capture.Plan, then require its returned audit to contain every exact HEAD line and every planned Delta receipt.
5. Report a new failure before declaring the landing complete. Existing unrelated depot findings and legacy anchors are outside this bounded slice.

## Boundary

- no public `--check` or `--lint` route exists
- no bulk Project/Chat coverage audit or reconciliation cursor runs here
- no Chatlas1 anchor, Normal Model, query, or view is resolved
- the checks establish mechanical correspondence, never semantic truth
