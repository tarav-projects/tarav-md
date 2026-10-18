# Gitleaks in Tarav

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## Why

Tarav-md's history held leaked API keys from committed Chatlas exports
(2026-10-16). Gitleaks found them before publishing. The User wanted the
project repositories cleaned and the same detection available to every Tarav
Project, and chose to build the integration first and run the cleanup scan
from Tarav.
<!-- tarav.breadcrumb 19a9086c9bb2 -->

## Integration choices — 2026-10-18

Gitleaks is a Go binary with no official Python library. The User chose
calling the binary over Python alternatives (detect-secrets scans files, not
history; ggshield sends content to GitGuardian's service), transparently
under a gitleaks workflow, without an adapter abstraction or renamed Types.
<!-- tarav.breadcrumb 0604a9ab327b -->

The workflow sits under Git. Gitleaks joins the default hook handlers; a
Project without hooks installed raises a POI as a reminder and opts out by
blessing it. The hook scans only the commit; full history scans run on
request.
<!-- tarav.breadcrumb 6ae712657e65 -->

A stopped commit is overruled with the existing comma-separated
`TARAV_GIT_HOOKS_OVERRULE` from request 916, such as `gitleaks,tarav-change`;
the User had considered a boolean flag and kept naming what is overruled.
<!-- tarav.breadcrumb d60e2d6fb752 -->

## Detection, then verification

Gitleaks detects and Tarav double-checks. Each gitleaks run, on request or in
the hook, leaves a new report in a depot. Tarav's check confirms each reported
finding is still there; that is the situation that raises the POI and opens
the action. The action closes when the data disappears, when the fingerprint
is in `.gitleaksignore`, or when the latest report drops it. For a finding in
a commit, "still there" means the commit is reachable and the file and lines
exist in it: Git addresses content by hash.
<!-- tarav.breadcrumb 7d5be5279310 -->

Blessing a finding's action is appending its fingerprint to
`.gitleaksignore`, the file gitleaks itself honors; the closing lands on the
Action tape like any other.
<!-- tarav.breadcrumb 34607f8f3b8c -->

Working trees are not verified. A report without a commit, the hook's staged
findings, opens an action closed by hand, to keep the system simple.
<!-- tarav.breadcrumb 612ce9f2b577 -->

## As built — tarav-py request 920

`tarav.l1.git.gitleaks`: `run_gitleaks` (history or staged) writes the raw
report and a `Tarav.Git.Gitleaks.Run` Record under
`~/Documents/tarav/gitleaks/<root commit>/`. `GitleaksCheck` raises
`Finding`, `NeverScanned` and `Missing`; the `gitleaks` handler's staged
reports raise `Staged` through a check that runs in no suite. Findings belong
to the nearest Project marker above the repository, else the System Project,
whose suite checks scanned repositories no Project owns.
`tarav git gitleaks scan --repo PATH` scans and registers actions on the
owner. Default handlers apply to Projects whose config names none, and
`HooksNotInstalled` is blessable. tarav-py runs the handler. Chatlas
(`~/Documents/tarav/chatlas`, 4 GB of transcript history) is left out of the
cleanup scan for now, at the User's request. See
[Impl.Req 920](../../../tarav-py/notes/live/920-gitleaks-workflow-impl-req.md).
