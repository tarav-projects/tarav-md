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

Design request: `tarav-py/notes/live/851-cli-model-live-help-and-invocation-registry-impl-req.md`.
Open there: whether Live Help is a workflow beside Context or a contribution
to a command's existing reactive `context()`, and whether a rolling window is
acceptable inside the Archive.
<!-- tarav.breadcrumb fea332b561da109685c9fc4bcd7da73f279d41deb6511fa8966f5af1a1436e21 -->
