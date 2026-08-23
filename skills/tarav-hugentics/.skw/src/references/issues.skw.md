> $kw: ^index-issues-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-authority-contract

> $kw: --dev-from references/index-context-assembly.skw.md

# Index.Issue.Operation.Module

Use this module for current temporary Project topics. An issue may be an opportunity, question, migration, contradiction, defect, or administrative checkpoint; its subject is not presumed negative.

## Minimal Form

- files live at `issues/NNN-issues.md`
- each block identity is `Issue.I####` with an optional descriptive dotted suffix
- every line is typed and carries a resolvable support reference
- all existing two-character line types remain available; richer tag policy is deliberately deferred
- open and resolved are computed projections, never folders or cached status fields

## Lifecycle

1. Create or update the grounded `Issue.Block` for the current temporary topic.
2. Keep ordinary model edits on their natural chapter, appendix, or agendix surface; issue context belongs in each changed line's dossier.
3. A reviewed `[DC]` line with exact tokenized approval is a Resolution.Line. Several model edits and Resolution.Lines may share one approval token.
4. A block is open until it has a reviewed Resolution.Line. Openness is healthy and never itself a linter error.
5. Retain a resolved issue while its rationale conditions the present model. Remove it from Project HEAD when it no longer does; its Chat.Index Delta and Git history remain.

Read computed standing from the records through `tarav indexlab project` and `tarav indexlab lint`; the dedicated issues command went with the Markdown realization. Never infer review from the `issues/` folder or synthesize a user gate.
