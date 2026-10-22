# tarav-change: commit references that survive rewrites

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## The problem

A commit hash names exact bytes. Rewriting history changes it: removing the
leaked Chatlas exports from tarav-md's history on 2026-10-16 changed 488
commit hashes and left notes in tarav-py, tarav-md and tarav-chatlas-md
citing commits that no longer exist. The User decided this must be solved.
<!-- tarav.breadcrumb 3e4b3f116028 -->

## The idea: Tarav-controlled markers in the repository

The User proposed extra hashes kept in the repository as timestamps: a
tracked file under `<repo root>/.tarav` to which new hashes are appended
over time. When history changes, the commit where a given hash first
appears can still be found, so the file is a Tarav-controlled mapping
between commits and hashes; anyone who wants to track a commit adds a hash
there and commits it.
<!-- tarav.breadcrumb 3c24291dd430 -->

Gerrit's `Change-Id` is the proven precedent: a `commit-msg` hook adds a
random ID trailer that survives amend and rebase, and the review server
groups versions of one change by it.
<!-- tarav.breadcrumb cb5785628311 -->

## Decisions

- Tarav is an external harness, so a Project can require Tarav Git hooks;
  the hooks call the `tarav` CLI with the context Git gives and Tarav
  handles the rest internally.
  <!-- tarav.breadcrumb 7d9e072bf99c -->
- Both carriers: the ID is a commit trailer and a line in a tracked file.
  Hooks are not a guarantee, and that is accepted: more systems are added
  over time to make references reliable, and a tarav-change is one more
  kind of data a reference can carry. A missing `tarav` warns and lets the
  commit through. The hooks belong to the Project configuration, with
  checks that maintain them. The trailer key is lowercase `tarav-change`.
  <!-- tarav.breadcrumb 7351fa761d9c -->
- Two levels: a Git hook system for Projects, then tarav-change as its
  first application.
  <!-- tarav.breadcrumb ca1119beb472 -->

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

## Append-only, with a witness outside the repository

The file is why amend is acceptable: the change-id file must be
append-only, so that surgery cutting history has to cut the file itself,
which survives many modes of change. The User first proposed a global
registry under `~/Documents/tarav` recording change-ids and their commits.
<!-- tarav.breadcrumb 23614856bc9e -->

The User then weighed it: a registry knows which change-id matched which
commit, but cannot find the new commit once the repository's ID was cut or
amended; the file's strength is that it sits next to the edits it tracks.
<!-- tarav.breadcrumb 0f0e6d03354b -->

The bar is best effort, not the last 5% of cases: whoever rewrites Git owns
the consequences, and references carry other hints about their subject.
Knowing when a loss happened is still worth having.
<!-- tarav.breadcrumb e681af66c0d2 -->

The registry's role became a witness: it tracks the change-id file outside
the repository and tests that it stays append-only, and the hook stops a
commit that broke it, with an overrule (an environment variable) as a
speedbump.
<!-- tarav.breadcrumb f93b77414505 -->

Every stop or overrule is recorded, sensed by the hook and handed to the
Project as an Action. The hook contract was relaxed from "never blocks" to
"stops, with an overrule flag", to give an agent the opportunity to respond
and rethink what it is doing. Witness entries are Records per Project and
branch under `~/Documents/tarav/git-changes/`, machine-local.
<!-- tarav.breadcrumb 046e6ae8eb33 -->

### As built — tarav-py request 916

A handler may raise `GitHookRefusal`; `tarav git hook` exits 75 and only
that stops Git, while other failures and a missing `tarav` still let it
continue. `TARAV_GIT_HOOKS_OVERRULE=<handler>` overrules a stop.
`tarav.l1.git.witness` keeps a `Tarav.Git.Change.Witness` per Project
(`project_id`) and branch and a `Tarav.Git.Change.Overrule` per overruled
commit. tarav-change's `pre-commit` stops a commit whose `.tarav/changes`
lost IDs the witness holds and registers a `Tarav.Git.Change.Removed`
action; an overruled commit records itself and opens a
`Tarav.Git.Change.Overruled` action, and the witness moves to the new file.
The tarav-change check raises the same POIs between commits, so a
`reset --hard` or a history rewrite shows up before the next commit.
`ProjectActions.register` registers such actions without treating the
results as a whole run of the Project's checks. Detached HEADs and Projects
without a `project_id` are not witnessed.

## Repository identity and owner — 2026-10-22

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

The User requested Change-ID integration in Archive repository references.
Witness identity is now repository DOI plus branch, replacing the earlier
Project-keyed schema. Project ownership separately routes refusal/overrule
actions. Detached HEAD remains unwitnessed.
<!-- tarav.breadcrumb 5f88ce8ab459 -->

`tarav git hooks install --repo PATH --owner-project PATH --handler tarav-change`
registers or binds a repository and installs hooks without making it a Project.
Existing Projects can use `--project`. Configuration retains the repository DOI,
registry and optional owner; missing binding produces a finding. No legacy
identity fallback is retained. `OwnedRepositorySuite` discovers owned external
repositories through Archive and rechecks them so actions can close on recovery.
Inaccessible local repositories prevent falsely complete discovery scans.

The live tarav-py baseline migrated with original bytes conserved in Attic.
Repository references carry exact commit/tree and optional Change-ID; recovery
requires one unambiguous candidate matching the captured tree.
See [Archive references](archive-doi-registry.md#repository-references-and-change-id--2026-10-22)
and [request 943](../../../tarav-py/notes/live/943-repository-doi-change-references-impl-req.md).
