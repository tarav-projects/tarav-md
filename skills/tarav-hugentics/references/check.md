# Real.Time.Validation.Knowledge.Module

This is an internal `Real.Time.Capture` primitive, not a public workflow. It validates only the exact editions just landed by the foreground capture batch; broader Index diagnosis and Project/Chat reconciliation are parked in the workflow-retirement issue at `issues/100-issues.md`.

## Validation Slice

1. Run `tarav indexlab lint --library <root> --workspace <name> --record-id <id> ...` with one repeated selector per newly captured record; the run examines only those records.
2. A check reports `passed`, `failed`, `blocked`, or `error`. Only `failed` is a finding against the subject; `blocked` means an earlier check could not be evaluated, so a blocked run never earns a clean verdict.
3. Escalate an individual dossier with `tarav chatlas anchory resolve <anchor>` only when the bounded report exposes a grounding POI.
4. Report a new failure before declaring the capture complete. Unrelated existing findings are outside this bounded slice.

The gate and landing-audit steps are absent because the kernel carries no gate evidence yet; do not substitute a manual check for them.

## Boundary

- no public `--check` or `--lint` route exists
- no bulk Project/Chat coverage audit or reconciliation cursor runs here
- no Chatlas1 anchor, Normal Model, query, or view is resolved
- the checks establish mechanical correspondence, never semantic truth
- for how a `POI.Linter` run behaves in general — tiers, the three-valued verdict, selection and narrowing, gates, the dev lane, and what licenses a blessing — read `tarav-pkg/references/poi-linter.md`
