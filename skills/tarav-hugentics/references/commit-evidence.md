# Git Commit Evidence

Use this module for Git commits owned by modifying Hugentics workflows.
Read-only routes never commit. The workflow brackets each repository it
mutates with a scoped start checkpoint and a scoped completion commit.
Multi-repository work brackets each repository independently.

## Scope

The agent declares the exact repository-relative paths it is committing.
Do not sweep the worktree or absorb unrelated edits. At the start, include
only pre-existing changes inside the declared work scope; use an empty
checkpoint when that scope is clean. At completion, include only files the
workflow actually changed. Broader commits require a separate User request.

## Manifest and message

Write a temporary JSON manifest with this shape:

```json
{
  "type": "Tarav.Git.CommitEvidence.Manifest",
  "repository": "/absolute/repository",
  "files": ["relative/path.py"],
  "message": "Subject\n\n- relative/path.py: bounded change\n<!-- tarav.context <alias>:<turn-prefix> -->",
  "allow_empty": false
}
```

Declare sessions in the message with the ordinary `tarav.sessions` block.
Each human-readable `- ` change group ends with one or more provisional
`tarav.context` markers, or with exactly one honest gap marker:

```text
<!-- tarav.evidence agent-initiated -->
<!-- tarav.evidence unknown-session -->
```

Use `agent-initiated` when the committing agent decided the change without a
supporting User Turn. Use `unknown-session` for pre-existing work whose
discussion cannot be identified. Evidence is best effort; do not fabricate
coverage. Tarav creates Breadcrumb IDs and the recoverable evidence envelope.
Do not author either one manually in a new manifest.

## Commit and recovery

Run:

```bash
tarav git commit --manifest <manifest.json> --json
```

Tarav validates and registers Breadcrumb evidence, commits only the declared
paths, then records the exact commit-message locations. It preserves staged
changes outside the selection. If Git fails, registered Breadcrumbs may remain
without that location. If the commit exists but observation fails, retain its
hash and recover without another commit:

```bash
tarav breadcrumbs register-commit --repo <repository> --commit <hash> --json
tarav breadcrumbs audit chatlas-context --repo <repository> --commit <hash> --json
```

Inspect the scoped diff and run the workflow's checks before the completion
commit. Report the start and completion hashes, Breadcrumb audit result, and
any honest evidence gaps.
