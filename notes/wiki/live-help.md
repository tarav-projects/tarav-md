# Live Help

<!-- tarav.sessions
f5845518 = claude-code:4ee3b84e-14fa-4aa9-9c6f-8d139954fe18 @f5845518e808c6cf0496f867fc656fdad9063980a184f7c3f15c54adf8fcb31f
-->

## Learning from live material

Tarav is developed without a minimal contextualization path for understanding
how Tarav itself works. Contextualization paths are workflows, and several can
exist. The preferred one sends the Agent to live material: the source code,
and active examples, meaning data recently used by that code. Samples dumped
into a skill go stale. Documentation is a last resource, because nothing yet
raises a POI when the code it describes changes.
<!-- tarav.breadcrumb 82886fb280b2796489cad9b6ddd27a487ebf049257e0e02e0e61f8e66b099900 -->

The diagnosis followed an Agent report that adding one small skill module cost
far more in learning mechanics and capture bureaucracy than in content.
<!-- tarav.breadcrumb 197993ff14d5568c1a10922e230e9f622813464fdc7c8a73eefc020a5ed5bbe1 -->

## Dumb code, smart Agents

The code should be dumb. Agents are smart and navigate quickly from a
sufficient lead. Tarav's job is to remove unprofitable work, such as searching
a large code base for a definition, and to point at declarations, recent uses,
and tools. Git history is therefore only hinted as a ready-to-run command; a
Git query workflow that objects hook into was considered and deferred.
<!-- tarav.breadcrumb cfb5835b1aead0e527031c7ee3e0d035456782cb78f4ea43c958718b4d2fbfe7 -->

## CLI as Tarav objects

The command line should be modeled in Tarav: the CLI as a workflow and
commands as objects that can be referred to, tested, and checked, for example
to detect missing help. Typing things and hooking workflows to each other is
how Tarav grows and how development is kept coordinated. The model need not
be pedantic.
<!-- tarav.breadcrumb 73c19e3697c8070d2dde2ef9069ebd9b4a8e52cfa5a7e61caffd8943b07f5121 -->

## Invocation registry

Every `tarav` command call is stored with its command and arguments in a
queryable registry that may keep only a recent, configurable window. It lives
in Tarav's central storage, in the partition the owning workflow has there.
<!-- tarav.breadcrumb e4fca3391f69e78fb43bb196150c33d642159cb03a83944cc8792c7e447bb7c4 -->
<!-- tarav.breadcrumb f84a6b8b3db1e31e532c79981016a2c2bcfba8b93534cf8a7cc9330fcd5ace21 -->

## Reactive help

Help in Tarav is reactive, not static. A standard part of every help says
where to find things: the command's source, its recent uses, and a history
hint. The workflow that provides it is called Live Help, after the working
name "live context". The CLI workflow subtypes its types to take part.
<!-- tarav.breadcrumb 8cd458e77e8a0c426f2e427a6c97ca90bb29388a5da81d57b027984651e98130 -->
<!-- tarav.breadcrumb 34397ad86bd561231be38dc5ce8889dd7580122be0ac80af0035c0d8fe715012 -->

Design request: `tarav-py/notes/live/851-usage-registry-cli-model-and-live-help-impl-req.md`.
<!-- tarav.breadcrumb fea332b561da109685c9fc4bcd7da73f279d41deb6511fa8966f5af1a1436e21 -->

The first implementation makes Live Help a separate workflow and retains recent
usage in the Usage Registry's Archive partition. The day files inside its typed
workflow folders are maintained with a seven-day default window. The CLI trace
records option names and outcome but does not retain arbitrary argument values.
This is the bounded starting behavior; later clients choose their own payloads.
<!-- tarav.breadcrumb d5342ebc7c1c1d136c099d83811e196e771c61a21cf3ac976bc7a918ade9ebcc -->

## Usage Registry

User correction to the invocation registry above: it is not a CLI log but its
own workflow that other workflows attach to. Its semantic is a place where you
put your usage trace so Agents can discover fresh examples of how Tarav is
being used. It is like a logging system with a specific meaning, which is why
it is a workflow.
<!-- tarav.breadcrumb d699c1851e82e4c2924e071440a5870192abd2a3fb344116028bfe536208c874 -->

The registry does not care what is registered. Each workflow is responsible
for knowing what to store so an Agent can see how it was used. The registry
provides only the minimal shape, handles storage, and provides the query.
<!-- tarav.breadcrumb f0c0aa22797d781adc7483eb03ee1cb790c9cb99f47aeaa2817a477267fda14e -->

A trace can be left from inside any method, because Tarav's main interface is
the library and the CLI is only a consumer. A CLI command is a good point for
one, since a public command marks a typical or important path, but it is not
the only one.
<!-- tarav.breadcrumb 3a0d4d8d86a519410886ff3ff029a1c6ee457bddc90908475a2d4926969741a0 -->

Each registering workflow may have a partition inside the registry. General
metadata, such as the project and workflow of a call, lets Agents query back
by those native Tarav objects; those queries are built in. Beyond them Agents
send a general query: Tarav databases are by default sets of JSON records, so
the model is to iterate the records and query their JSON.
<!-- tarav.breadcrumb 4089a46c547c8145c6a20403639d58e92e7ccabf4551689c974d7b00e80b60b3 -->

The implementation exposes `record_usage()` to library callers, `tarav usage
query` to shell callers, and recent traces in each command's `--help` section.
The command tree is derived from argparse, with deterministic Ships for command
paths. The implementation checks command metadata and surfaces missing help as
POIs. Source: `tarav-py/src/tarav/l1/{usage,cli,live_help}/` and
`tarav-py/src/tarav/l3/cli/cli.py`; verification: 52 focused tests passed.
<!-- tarav.breadcrumb ee1bc214c3425f509955c22f39bc8435d666e66ccafa3cea32c69f29e6cadd57 -->
<!-- tarav.breadcrumb 7645d4c33f7385a4d60c93e66542f1fad65448c66a2ae8c1a33b1aa4da7262c7 -->
