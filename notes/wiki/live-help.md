# Live Help

<!-- tarav.sessions
f5845518 = claude-code:4ee3b84e-14fa-4aa9-9c6f-8d139954fe18 @f5845518e808c6cf0496f867fc656fdad9063980a184f7c3f15c54adf8fcb31f
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Learning from live material

Tarav is developed without a minimal contextualization path for understanding
how Tarav itself works. Contextualization paths are workflows, and several can
exist. The preferred one sends the Agent to live material: the source code,
and active examples, meaning data recently used by that code. Samples dumped
into a skill go stale. Documentation is a last resource, because nothing yet
raises a POI when the code it describes changes.
<!-- tarav.breadcrumb 82886fb280b2 -->

The diagnosis followed an Agent report that adding one small skill module cost
far more in learning mechanics and capture bureaucracy than in content.
<!-- tarav.breadcrumb 197993ff14d5 -->

## Dumb code, smart Agents

The code should be dumb. Agents are smart and navigate quickly from a
sufficient lead. Tarav's job is to remove unprofitable work, such as searching
a large code base for a definition, and to point at declarations, recent uses,
and tools. Git history is therefore only hinted as a ready-to-run command; a
Git query workflow that objects hook into was considered and deferred.
<!-- tarav.breadcrumb cfb5835b1aea -->

## CLI as Tarav objects

The command line should be modeled in Tarav: the CLI as a workflow and
commands as objects that can be referred to, tested, and checked, for example
to detect missing help. Typing things and hooking workflows to each other is
how Tarav grows and how development is kept coordinated. The model need not
be pedantic.
<!-- tarav.breadcrumb 73c19e3697c8 -->

## Invocation registry

Every `tarav` command call is stored with its command and arguments in a
queryable registry that may keep only a recent, configurable window. It lives
in Tarav's central storage, in the partition the owning workflow has there.
<!-- tarav.breadcrumb e4fca3391f69 -->
<!-- tarav.breadcrumb f84a6b8b3db1 -->

## Reactive help

Help in Tarav is reactive, not static. A standard part of every help says
where to find things: the command's source, its recent uses, and a history
hint. The workflow that provides it is called Live Help, after the working
name "live context". The CLI workflow subtypes its types to take part.
<!-- tarav.breadcrumb 8cd458e77e8a -->
<!-- tarav.breadcrumb 34397ad86bd5 -->

Design request: `tarav-py/notes/live/851-usage-registry-cli-model-and-live-help-impl-req.md`.
<!-- tarav.breadcrumb fea332b561da -->

The first implementation makes Live Help a separate workflow and retains recent
usage in the Usage Registry's Archive partition. The day files inside its typed
workflow folders are maintained with a seven-day default window. The CLI trace
records option names and outcome but does not retain arbitrary argument values.
This is the bounded starting behavior; later clients choose their own payloads.
<!-- tarav.breadcrumb d5342ebc7c1c -->

## Usage Registry

User correction to the invocation registry above: it is not a CLI log but its
own workflow that other workflows attach to. Its semantic is a place where you
put your usage trace so Agents can discover fresh examples of how Tarav is
being used. It is like a logging system with a specific meaning, which is why
it is a workflow.
<!-- tarav.breadcrumb d699c1851e82 -->

The registry does not care what is registered. Each workflow is responsible
for knowing what to store so an Agent can see how it was used. The registry
provides only the minimal shape, handles storage, and provides the query.
<!-- tarav.breadcrumb f0c0aa22797d -->

A trace can be left from inside any method, because Tarav's main interface is
the library and the CLI is only a consumer. A CLI command is a good point for
one, since a public command marks a typical or important path, but it is not
the only one.
<!-- tarav.breadcrumb 3a0d4d8d86a5 -->

Each registering workflow may have a partition inside the registry. General
metadata, such as the project and workflow of a call, lets Agents query back
by those native Tarav objects; those queries are built in. Beyond them Agents
send a general query: Tarav databases are by default sets of JSON records, so
the model is to iterate the records and query their JSON.
<!-- tarav.breadcrumb 4089a46c547c -->

The implementation exposes `record_usage()` to library callers, `tarav usage
query` to shell callers, and recent traces in each command's `--help` section.
The command tree is derived from argparse, with deterministic Ships for command
paths. The implementation checks command metadata and surfaces missing help as
POIs. Source: `tarav-py/src/tarav/l1/{usage,cli,live_help}/` and
`tarav-py/src/tarav/l3/cli/cli.py`; verification: 52 focused tests passed.
<!-- tarav.breadcrumb ee1bc214c342 -->
<!-- tarav.breadcrumb 7645d4c33f73 -->

## Usage descriptors

A usage trace is not the whole command. The caller knows which parts of a
call are informative yet economical: a path, not a long file. The trace need
not be the exact arguments; it is an informative descriptor.
<!-- tarav.breadcrumb bfcbbb1eef3f -->

The registry does not know what a command is or how it wants to be expressed.
It lets the caller say what to record about its command or method call, so
Agents get it when they ask for help. Representing the call is the caller's
responsibility, and no mechanics are imposed. A command that receives a whole
file's content understands itself fully and can stand for it with its first
and last characters and a hash, respecting everyone's space. The caller must
not put random things there: the purpose is to inform an Agent how the
command was used.
<!-- tarav.breadcrumb dda8b782ae87 -->

This is the same pattern as
[caller-declared identity inputs](caller-declared-identity-inputs.md).
Implemented in `tarav-py` note 853: a command declares a descriptor function
at registration, there is no default, and a command without one raises a
reminder POI.
<!-- tarav.breadcrumb b2159796c9fa -->

## Typed traces, rendered by their owner

The emitter of a trace should not need to know its consumers, only the
semantic that the trace will contextualize Agents. So a usage record is
typed, and its type has a render method: the type's owner does the rendering.
Help filters by type. A command's help shows recent traces recorded by the
command line; a trace recorded inside a method describes how that method was
called and belongs to that method's help, a later topic.
<!-- tarav.breadcrumb 7e686dfe180a -->

Help must not print whatever blob is there. Without traces of the right type
it shows none.
<!-- tarav.breadcrumb ee5ade92b67c -->

A base type describes the base record of the usage registry and everybody can
subtype it. The minimum viable product is the command line, deployed on at
least a few Tarav commands before any other user exists. Design request:
`tarav-py` note 855.
<!-- tarav.breadcrumb 61783d267a79 -->

For a given help provider, the query selects only that provider's expected
trace Type. Untyped legacy rows and traces of other Types do not appear in
its count or output; Live Help does not need to count what it skips. The
provider owns the heading and Type selection, and the trace Type owns
rendering. This keeps Live Help independent of CLI payload fields.
<!-- tarav.breadcrumb 1e7c8595a0cb -->

Request 855 implemented this in `tarav-py`: `UsageTrace` is the common Type,
`CommandUse` is the CLI specialization, new registry writes are typed, and
`tarav usage query --type` selects exact Types. Existing untyped rows remain
available to an unfiltered registry query. Command descriptors now cover
selected Breadcrumb and Chatlas commands; short text can remain verbatim.
The configured Python suite passed 164 tests. The product code and request
note are the operational source for the current API.
<!-- tarav.breadcrumb dae8175da2f8 -->
