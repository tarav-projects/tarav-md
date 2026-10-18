# Agents workflow

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

An open design direction (2026-10-09). Nothing here is implemented.

## Why

Tarav demands one minimal thing from the internal harness: an agent can reach
its current session ID. Tarav has Chatlas, but no workflow for dealing with
running agents. Chatlas is more an archive, concerned with full transcripts,
than the provider of a model of a running agent. Tarav also holds earlier code
that configures and runs agents. "Give me the current session" should belong
to a workflow, not only to a command.
<!-- tarav.breadcrumb ba90f9a9cad6 -->

## Direction

An explicit Agents workflow gathers what Tarav has for interfacing with the
providers: how the runners are modelled and asked things. Chatlas stays
important and is not handicapped; it focuses on transcripts. Agents has
submodules per provider. `project.agents` is another workflow, a sub-workflow
of the Project. The existing code is old but working: it is organized, made an
explicit workflow, given clear integration points with the rest of Tarav and
brought to the current philosophy. It is not removed.
<!-- tarav.breadcrumb 1baabf251375 -->

Supported providers are reduced to Claude, Codex and Copilot. The others are
noise at the moment and remain in Git history.
<!-- tarav.breadcrumb dc33392987c3 -->

The [Operator Context](operator-context.md) is its own workflow, not a part of
Agents.
<!-- tarav.breadcrumb 2dd774324718 -->

## Current code (observed 2026-10-09)

- `tarav-py/src/tarav/l1/agent/`: about thirty modules for accounts,
  authentication, rotation, monitoring, run preparation and sessions, with
  `providers/` holding `claude_code`, `codex`, `copilot_cli`, `gemini_cli`,
  `opencode`, `openclaw` and `pi`. It declares no Tarav workflow; its header
  still names `Agentos.Agent.Adapter`.
- The current session is read in `tarav-py/src/tarav/l1/chatlas/commands.py`
  from two environment variables, `CODEX_THREAD_ID` and
  `CLAUDE_CODE_SESSION_ID`. No Python object answers the question.
- Chatlas imports provider configuration, specs and session references from
  the agent package.
- The Chatlas archive on this machine holds sessions of `claude-code` and
  `codex` only.

Request 886 (2026-10-09) removed `gemini_cli`, `opencode`, `openclaw` and
`pi` from the code; `claude_code`, `codex` and `copilot_cli` remain. Profiles
of removed providers left in a user's `~/.tarav/profiles/` now make
`tarav agent` commands fail until they are deleted.
<!-- tarav.breadcrumb cf8f0d05dcc9 -->

Agent proposals, not decided: express what a provider can do by subtyping
(a provider that can report its current session inherits that capability);
report account and profile problems as POIs through checks; start with an
inventory of the modules before reorganizing.

## Inventory of `tarav.l1.agent` — 2026-10-09

Made for request 887, after request 886, by reading the code: 78 Python
files, about 18,800 lines. "Used by" counts imports. Nothing here was changed
by the inventory.
<!-- tarav.breadcrumb 72b03a8b9f6e -->

| Area | Modules | Lines | What it does | Used outside the package |
| --- | --- | --- | --- | --- |
| Model | `primitives.py` | 478 | `AgentConfig`, `SessionSource`, the run mixin and the capability Protocols (`RunCapable`, `PingCapable`, `ProfileCheckCapable`, `AccountStatusCapable`, `SessionDiscoveryCapable`) | Chatlas |
| Configuration | `config.py`, `_config_entry.py`, `_config_models.py`, `profile_scope.py` | 1,313 | Loads `~/.tarav/config.json` and `~/.tarav/profiles/*.json` into agent configurations; validates profiles; chat provider specs | Chatlas |
| Providers | `providers/specs.py`, `homes.py`, `registry.py` | 452 | Canonical provider families and their home layouts; builds the adapter for a configuration; resolves an agent for a run | Chatlas, Scoring, runtime |
| Provider adapters | `providers/claude_code` (2,581), `codex` (1,712), `copilot_cli` (1,333) | 5,626 | Per provider: adapter (`agent.py`), native sessions, transcript extraction, account status; Claude Code and Codex also authentication methods and usage hooks | Chatlas (extractors), runtime (usage hooks) |
| Sessions | `sessions.py`, `session_refs.py`, `session_utils.py`, `session_copy.py`, `providers/extraction.py`, `extractor_common.py` | 2,069 | Discovers provider-native sessions, their backing artifacts and transcripts; copies a session between homes | Chatlas |
| Running | `run_runtime.py`, `run_prepare.py`, `ping.py`, `profile_check.py` | 487 | Builds and runs a provider command, the liveness ping, the read-only fitness check before a run | Scoring |
| Accounts and authentication | `auth_registry.py`, `auth_method.py`, `auth_method_registry.py`, `capture.py`, `activation.py`, `materialization.py`, `rotation.py`, `account_paths.py`, `accounts_log.py` | 1,151 | The account store: capture credentials from a home, activate, push into homes, rotate; a secret-free event log | no |
| Account status and usage | `account_status.py`, `account_status_report.py`, `account_usage_fallback.py`, `usage_registry.py` | 799 | Provider-neutral account status and usage limits; the all-homes drift report; the usage record registry | no |
| Monitor | `monitor/` (16 files), `monitor_log.py` | 4,990 | The accounts monitor: loop, rendering, limits tracking, burst ratio, account rotation and auto-prime workflows | no (5 test files) |
| Commands | `commands/` (8 files), `_cli_common.py` | 1,432 | `tarav agent list`, `accounts` (with `monitor`), `sessions`, `profiles`, `run`, `ping`, `profile-check` | runtime |

Observations:

- Every area is live: each module is imported by another or registered as a
  command. No dead module was found by import.
- Integration with the rest of Tarav is narrow. Chatlas imports
  configuration, provider specs, session references and the extractors;
  Scoring imports the registry and the run types; the runtime registers the
  commands and two usage hooks.
- The package predates the current philosophy: no declared workflow before
  request 887, no registered Tarav Types, capabilities expressed as
  Protocols and not by subtyping, errors raised as `CliError` and not
  reported as POIs. Its commands already use keyed options only.
- Maintained tests import the monitor and the ping directly; sessions,
  accounts and running are not imported by any test.
- After request 886 the home-spec mechanics for SQLite anchors
  (`providers/specs.py`) have no provider that uses them.

## Request 887: the workflow exists and answers the current session — 2026-10-09

`tarav.l1.agent` now declares `AgentsWorkflow`, registered in the runtime.
"Which session is the running agent in?" has a Python answer,
`tarav.l1.agent.current_session.current_session()`. A provider adapter that
can answer inherits `ReportsCurrentSession` and names the environment variable
its harness sets; Claude Code and Codex do. Copilot does not, because it could
not be established that its harness exposes a session ID. Chatlas commands ask
this entry point and behave as before. Source:
`tarav-py/src/tarav/l1/agent/{identity,workflow,current_session}.py`,
`tarav-py/tests/test_agents_workflow.py`.
<!-- tarav.breadcrumb fc19bfd0877a -->
<!-- tarav.breadcrumb 78fb91ee589d -->

