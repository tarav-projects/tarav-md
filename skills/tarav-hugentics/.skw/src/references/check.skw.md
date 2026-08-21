> $kw: ^real-time-validation-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Real.Time.Validation.Knowledge.Module

> $kw: --from Reviewed.Content
> --dev-from references/index-context-assembly.skw.md

This is an internal `Real.Time.Capture` primitive, not a public workflow. It validates only the exact editions just landed by the foreground capture batch; broader Index diagnosis and Project/Chat reconciliation are parked in the workflow-retirement issue at `issues/100-issues.md`.

## Validation Slice

1. Run `tarav index linter --label <new-label> ...` with one repeated `--label` selector per newly landed line; the run examines only those records.
2. For reviewed lines, add `--check gate-verifies`; it walks the approval token through both turns, and a passing line is `Reviewed.Content` for that deterministic gate only.
3. Require the `tarav index capture land` report's final audit to contain every exact source attachment, `LineRecord`, HEAD line, and planned Delta receipt. On successful placement, tokenized gates must appear on both `LineRecord.review` and `LineRecord.landing`: approval licenses the edition, while the separate land command decides when to exercise that license.
4. Escalate an individual dossier with `tarav chatlas anchory resolve <anchor>` only when the bounded report exposes a grounding POI.
5. Report a new failure before declaring the landing complete. Existing unrelated depot findings and legacy anchors are outside this bounded slice.

## Boundary

- no public `--check` or `--lint` route exists
- no bulk Project/Chat coverage audit or reconciliation cursor runs here
- no Chatlas1 anchor, Normal Model, query, or view is resolved
- the checks establish mechanical correspondence, never semantic truth
