# CLI command routing

<!-- tarav.sessions
0d8af26c = codex:01a168fe-92d6-7410-a7f7-7c15cf921b95 @0d8af26c5b8dff7be764aac420b13df80bb530919d551881ae7d1afcc2400744
-->

## Global routing first — 2026-10-23

The User wants a simple global JSON configuration mapping a selected Tarav
command to another invocation, passing through its arguments. Project-specific
configuration can come later. The immediate use case is running a future
Chatlas vector-database command on the Studio while invoking it locally.
<!-- tarav.breadcrumb 092c47eb3301 -->

The CLI router and SSH workflow have separate responsibilities. For this first
implementation, the router can launch `ssh studio-pereiro` followed by the same
Tarav command and arguments directly. Run profiles and SSH workflow integration
are deferred; this task implements the router alone.
<!-- tarav.breadcrumb b7dbf635bd66 -->
<!-- tarav.breadcrumb 9e75162958e9 -->

Routing must always be visible. Before execution, show one simple announcement
with the actual command being run, including SSH and its arguments. The
implementation sends this banner to stderr so stdout remains command data.
<!-- tarav.breadcrumb 56475f85fe18 -->

The User requested a Hugentics implementation request and execution together.
Product design and verification are retained in [Python request 956](../../../tarav-py/notes/live/956-global-cli-command-router-impl-req.md),
with [Wiki request 878](../live/878-global-cli-routing-wiki-impl-req.md).
<!-- tarav.breadcrumb 6fcfed046a90 -->

## Implemented mechanics

The implementation reads optional `cli-routes.json` from the existing Tarav
home. A route declares command tokens and target argv; the longest leading
token match wins, with remaining arguments passed unchanged. Dispatch precedes
local parsing so commands available only remotely can route. An optional
`shell_command` token array is quoted into one final argument for consumers
such as SSH, while ordinary routes receive an argv directly. The router starts
no local shell. The mandatory flushed banner precedes the child's inherited
streams, and the process adapter preserves exit status.

`TARAV_CLI_NO_ROUTE=1` bypasses routing and is inherited by local targets.
An SSH mapping explicitly sets it remotely to prevent routing back. These
configuration, matching and bypass details are implementation choices, rather
than additional User requirements. No production route was enabled: the vector
command and remote Tarav installation are separate work.

Evidence: [configuration and operating guide](../../../tarav-py/src/tarav/l1/cli/README.md),
[router library](../../../tarav-py/src/tarav/l1/cli/routing.py),
[CLI process adapter](../../../tarav-py/src/tarav/l3/cli/cli.py), and
[real CLI tests](../../../tarav-py/tests/cli/test_routing.py). The initial
routing tests measured 15 failures and two passes; after implementation,
88 focused routing, existing CLI and architecture checks passed. A read-only
installed-CLI call through real SSH to the Studio preserved spaces, empty
strings, literal dollar signs and semicolons. Full Project check results remain
in request 956's execution log.
