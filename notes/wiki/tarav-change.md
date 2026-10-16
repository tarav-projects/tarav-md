# tarav-change: commit references that survive rewrites

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## The problem

A commit hash names exact bytes. Rewriting history changes it: removing the
leaked Chatlas exports from tarav-md's history on 2026-10-16 changed 488
commit hashes and left notes in tarav-py, tarav-md and tarav-chatlas-md
citing commits that no longer exist. The User decided this must be solved.
<!-- tarav.breadcrumb 3e4b3f116028774aba744b1cb36ea495a9871d61b314f088db12207b28fd35bf -->

## The idea: Tarav-controlled markers in the repository

The User proposed extra hashes kept in the repository as timestamps: a
tracked file under `<repo root>/.tarav` to which new hashes are appended
over time. When history changes, the commit where a given hash first
appears can still be found, so the file is a Tarav-controlled mapping
between commits and hashes; anyone who wants to track a commit adds a hash
there and commits it.
<!-- tarav.breadcrumb 3c24291dd4309b7cb94982af6c32590b673418052e810e1bcb0c2531ce77d682 -->

Gerrit's `Change-Id` is the proven precedent: a `commit-msg` hook adds a
random ID trailer that survives amend and rebase, and the review server
groups versions of one change by it.
<!-- tarav.breadcrumb cb578562831150e75a9d9128cad14f631f453a1eecdda993bdf9d6758dcd1429 -->

## Decisions

- Tarav is an external harness, so a Project can require Tarav Git hooks;
  the hooks call the `tarav` CLI with the context Git gives and Tarav
  handles the rest internally.
  <!-- tarav.breadcrumb 7d9e072bf99ca395fdd560575303d1994f28a800e19ea5d8e3285e21e402896d -->
- Both carriers: the ID is a commit trailer and a line in a tracked file.
  Hooks are not a guarantee, and that is accepted: more systems are added
  over time to make references reliable, and a tarav-change is one more
  kind of data a reference can carry. A missing `tarav` warns and lets the
  commit through. The hooks belong to the Project configuration, with
  checks that maintain them. The trailer key is lowercase `tarav-change`.
  <!-- tarav.breadcrumb 7351fa761d9c563d1491c27cfdf275bf9dfbe50e870f27c7a453310b282362f5 -->
- Two levels: a Git hook system for Projects, then tarav-change as its
  first application.
  <!-- tarav.breadcrumb ca1119beb47289e89f5a23375a121a4b004028d59bf8e9afc7b08cad379dad62 -->

## As built — tarav-py request 915

Project Git hooks (`tarav.l1.git.hooks`): the `git` section of a Project's
`.tarav/config.json` names handlers (`{"hooks": {"handlers": [...],
"chain": <folder>}}`). `tarav git hooks install --project [PATH]
[--handler NAME]` writes one script per needed Git hook into
`.tarav/git-hooks/`, sets `core.hooksPath` and adds the `.gitattributes`
lines handlers need. Each script runs the chained hook, then
`tarav git hook --name <hook> --arg ...` in process; a missing or failing
Tarav never blocks Git. Every Project suite includes a hooks check
(`Tarav.Git.Hooks.NotInstalled`, `Stale`, `UnknownHandler`,
`AttributesMissing`) plus each handler's own check.

tarav-change (`tarav.l1.git.change`): `pre-commit` appends a UUID4 to
`.tarav/changes` and stages it, `commit-msg` adds `tarav-change: <id>`,
`post-commit` realigns the repository's own index, `post-rewrite` logs
old→new hashes in the clone's `.git/tarav/rewrites.jsonl`; the file merges
with `merge=union`. `tarav git change find --id <id>` lists the commits on
any branch that gained the ID. `Tarav.Git.Change.Missing` reports commits
made without the hooks. tarav-py uses it since commit `ff21d4d`.

Mechanics found by experiment: only `pre-commit` can still stage into the
commit, through the `GIT_INDEX_FILE` Git passes (it differs for plain, `-a`,
`<paths>` and temporary-index commits); an amend cannot be detected in
`pre-commit`. So an amended commit gains a new ID and keeps the old line,
and both IDs find it. Cherry-pick and rebase copy the ID with the content.

Open: carrying tarav-change IDs in Tarav References; enabling the hooks in
the other repositories; rewriting the citations the tarav-md purge left.
