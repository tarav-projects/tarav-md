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
<!-- tarav.breadcrumb ba90f9a9cad6d9b61e4282de2f9a096a000eb4d2f66745a460f5120455ff237f -->

## Direction

An explicit Agents workflow gathers what Tarav has for interfacing with the
providers: how the runners are modelled and asked things. Chatlas stays
important and is not handicapped; it focuses on transcripts. Agents has
submodules per provider. `project.agents` is another workflow, a sub-workflow
of the Project. The existing code is old but working: it is organized, made an
explicit workflow, given clear integration points with the rest of Tarav and
brought to the current philosophy. It is not removed.
<!-- tarav.breadcrumb 1baabf25137502a4f0fb33db6a52c643db2378b98abf7177ae1110486ca37f98 -->

Supported providers are reduced to Claude, Codex and Copilot. The others are
noise at the moment and remain in Git history.
<!-- tarav.breadcrumb dc33392987c3d1c59cb9395c7ba251605f58aa4edcf6d3adccf31cfa5f5e5577 -->

The [Operator Context](operator-context.md) is its own workflow, not a part of
Agents.
<!-- tarav.breadcrumb 2dd774324718bcfd1d632bbc9b0de3ec3b9a20259b6c62f3e852c7594acfffb1 -->

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
<!-- tarav.breadcrumb cf8f0d05dcc94f619dd9cdfe22c49028b44c78b609a08d255a50ea858b9eb054 -->

Agent proposals, not decided: express what a provider can do by subtyping
(a provider that can report its current session inherits that capability);
report account and profile problems as POIs through checks; start with an
inventory of the modules before reorganizing.
