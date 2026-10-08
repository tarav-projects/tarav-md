# Tarav scripts and entry points

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## The pandas analogy

Asked for a plot from a set of data files, an agent writes a script that imports pandas and matplotlib. It does not read and transform the files with its own reading tools; it manipulates the data through the library, and when it uses the library wrongly an error points it toward the right use. In that sense pandas works as a harness. The User wants Tarav to work the same way: when a Project is under Tarav, a large share of operations should be resolved by agents writing and running scripts against the Tarav library.
<!-- tarav.breadcrumb 57619c680942303fe39bd2216f28d604bdfc6e1b2e20b377222365a0700e6548 -->

## Code and recent usage as primary documentation

A package skill that explains how to write Tarav code has a place, but a secondary one, because a skill can go stale and must be maintained. The primary documentation is the Tarav code base itself, which agents should reach easily and which should be curated over time so that it is efficient to traverse. The second source is recent usage: an agent should be able to find examples of how Tarav has been used lately, so neither the code nor its uses depend on separately written documentation.
<!-- tarav.breadcrumb f7287ceb3724cfd08b6ed92073ed7b22904b107dd6d6df4a854e2a477ac84093 -->

Live help already implements this principle for the command line, where a call has a clear interface. Tarav is workflow-based, so several workflows may provide the same principle, and shared primitives are extracted once they are identified. The open matter is how to provide it for scripts.
<!-- tarav.breadcrumb b19baeb1e2541649f411afcae0c2213e4f9601ea61d302b6ab386000d5a50480 -->

## Guarded import and the bypass entry

Most scripts should be run with `tarav run`. Tarav should therefore complain when it is imported by a process that `tarav run` did not start, recognised through a flag in the environment that `tarav run` sets, with an override for the testing infrastructure. The purpose is only to push agents toward `tarav run`.
<!-- tarav.breadcrumb 8408e00cfa49d5511b416a0520f6576f509603fb95a7aacd5a341ef256c255b9 -->

The complaint is a hard error and not a warning, but a controllable one: whatever needs to import Tarav another way must be able to. Tarav's preference for informing over forbidding exists so that Tarav itself stays simple; it is a general principle and not an invariant, and a strong rule is acceptable here. If the hard version proves too complicated it can become a warning.
<!-- tarav.breadcrumb 3ff009ce6720b53c45016c7335037eb8803a3fc0ceefc9af4a74ea490e773d58 -->

The mechanics use an environment variable, and the error message does not mention it. The message says only that the process was started the wrong way.
<!-- tarav.breadcrumb 9c2945439d0de45706efd4be989aeff5390ada7acc5f166204f434fca27829b9 -->

The guard is a speed bump for agents that use Tarav casually. Developers who use Tarav directly need ways through that are as easy and ergonomic as possible.
<!-- tarav.breadcrumb d05524dedf0b3be542c22a1351c382539ba7c1b1da850faf9d4e3040fdc5d407 -->

The way through decided for now is a second entry point to the same library: plain `tarav` is the guarded entry that regular agents meet, and a separate import layer sits over the same system. Its name should read like a warning, and the User settled on `tarav_bypass` for the time being.
<!-- tarav.breadcrumb c7f418e390ec97d1c409f17416621999e063231e4c0001539ad8464931dcd9c7 -->
<!-- tarav.breadcrumb 2cceffa77ac6e28a26262fcff1d3d5038e722243aa319dd1f4d64f328471bbbd -->
<!-- tarav.breadcrumb bc6b6447724781a10909b19dd539759d48806daacc5aaa4ba73f2ce10af76fc9 -->
<!-- tarav.breadcrumb cb35d1a7bb624ceb668341ad8b56428932b7427b8e9b289c5f12d4fb62dbab01 -->

[Impl.Req 874](../../../tarav-py/notes/live/874-tarav-import-guard-and-bypass-entry-impl-req.md) designs the split and its adoption by the command line, the tests and the other importers. Its package layout, landing order and adoption list are agent proposals awaiting confirmation; nothing is implemented yet.
<!-- tarav.breadcrumb 957b05de5ea696a429426587787864242d3a030f15c3116a561650962f0fdf4b -->

## Undecided brainstorm

The ideas below were explored in the same discussion. The User said explicitly that they were brainstorming and that nothing here is decided.
<!-- tarav.breadcrumb 710d229901a296dae473f2af70b31651ef8c8b2fb600bf8cf19aa3f9cf5e0b80 -->

**A run registry.** `tarav run` itself could keep a registry of the code it has run, separate from live help, which records how the command was used. It can be very simple: copies of the scripts, kept for a bounded period such as a week to control size, with metadata such as the Project and the commit so that contextualization can find what it needs.
<!-- tarav.breadcrumb b0d6ba36b6111bee95589c7d302d9017db95b56014df3918665005f3b29205fb -->

**Central storage.** The registry would be stored centrally, so that agents can see how other Projects use the same parts of Tarav. Scripts from other Projects may hold better patterns, agents can be prompted to study them, and the system then evolves by itself.
<!-- tarav.breadcrumb a4143f91cfacc29f9b2a157bf6e6377fc62f98220c614b303dba55556437cbe6 -->

**Lookup from the code.** The help or context of a method could connect to that registry, for example by searching the registered scripts for the method's path. Whether Python can run code when help is requested at run time was left open; a banner in the source telling the reader how to find recent examples was another option.
<!-- tarav.breadcrumb bd7af182362c5386f67aaa6c3f38ee41e81ec856d3bae700a20ca2219ef0b240 -->

**Operations.** An agent is usually asked to perform an operation that belongs to a skill or to a module of a skill, and that module can say whether to use the command line or a script, and where to look the first time. This suggests a concept of an operation that ties defined workflows to source code and recent usage. The User called this a digression for now.
<!-- tarav.breadcrumb fe3cf7b873d3d75e913bbba5777dfdd9027b7e8653642b153a355c99685e056d -->

**Other ways through the guard.** A file checked at import time, a flag found in the argument vector, and other mechanisms were mentioned as possible additional ways to pass. Only the second entry point is being done now.
<!-- tarav.breadcrumb b8d1e29da065aeb38881621f512f3b79c13fe6d01c832389514e380e7594e37c -->
<!-- tarav.breadcrumb 856744ffebf775cc0bf0bd09767f7fdd0833a6a09cde2ef6bf80f7d739bfd394 -->

## Other repositories and the import guard

The repositories outside Tarav that import it directly are not Tarav's concern. When the guard is on they will see the error, and their maintainers resolve it there. [Impl.Req 874](../../../tarav-py/notes/live/874-tarav-import-guard-and-bypass-entry-impl-req.md) was narrowed to `tarav-py` accordingly.
<!-- tarav.breadcrumb fe5ed5ae64b8b55acd08662397c35962ad29973916d085d18050b0856281bb6a -->

## Run script registry

This section continues the registry idea from the brainstorm above; the points here are now decided.

With the import guard funnelling scripts toward `tarav run`, the registry is the other half. It is another registry like the help one, in its own folder. `tarav run` keeps the path of a script and copies the file, and also keeps source given as text or on standard input. It is deliberately simple, with at most some deduplication. It is partitioned at least by Project: a run with the `--project` flag goes under that Project's partition and a plain run under a global one. Metadata is chosen by common sense, such as the calling folder and the date, and will be refined by use.
<!-- tarav.breadcrumb 63fb1aa418365b90767a71f8088bd6e61c80ea2402a44b9baf88b497f677e57b -->

Retention exists only to bound size, so it is expressed in size rather than time: an allocation per partition, for example 50 MB, and a limit per entry of around 1 or 2 MB beyond which the copy is cut. The registry is best effort and not critical; its purpose is to increase contextualization power.
<!-- tarav.breadcrumb fc58a479ac5aba8b499f3a0f494b3330de6ff216fc0c7c79809a02b77c890702 -->

[Impl.Req 875](../../../tarav-py/notes/live/875-run-script-registry-impl-req.md) designs the first implementation. Its layout, metadata fields, write order, and the choice of the Project id as partition key are agent proposals made under the User's request to use common sense; a query command and lookup by name remain undecided.
<!-- tarav.breadcrumb c9e8649e9ebd4358f156067404641e67cef2e8cadb64703719c6c18ae8726a8b -->

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

## Import guard implementation

The User invoked Execute for [Impl.Req 874](../../../tarav-py/notes/live/874-tarav-import-guard-and-bypass-entry-impl-req.md) after requiring a fresh read of this Wiki and the related User turns. In `tarav-py`, the root `tarav` import now requires an entry mark. The separate `tarav_bypass` package supplies that mark before importing Tarav; the installed `tarav` and `tarav-daemon` commands use its doors. `tarav run` passes the mark to child scripts. The error points users to `tarav run` and does not expose the mark or bypass mechanics. Tests and direct-import maintenance scripts use the explicit bypass; repositories outside `tarav-py` remain their maintainers' concern.
<!-- tarav.breadcrumb 208613f4f0d7ffcfdc447a3d16c3aeb1298ea138a9d549bbbc6058848e362b1f -->

The implementation is in product commit `4629dd90ad45e1ac35e9b2b915dae6a9304c9a05`. The committed tree passed 178 Python tests and Ruff; the shared worktree passed 188 tests and Ruff. The built wheel contains both packages, both `tarav run` forms imported Tarav, and the installed daemon restarted through the CLI and launchd. The root Project check ran 362 checks and reported 65 POIs from existing Project state. The package skill's import guidance is a separate `tarav-md` follow-up; it was not part of this `tarav-py` implementation.
<!-- tarav.breadcrumb 60751154b6150079b6df7c41e5530cbdc86e6406945044a42648f25d41205e79 -->

### Run script registry implemented — 2026-10-08

The User asked for implementation to start. `tarav run` now retains what it executes under `~/.tarav/run-registry/`, in one folder per Project id plus `global`, with a 1 MB cut per entry and a 50 MB allocation per partition. The location and reading standard input fully before the child starts were the agent's recommendations, applied because the two open questions had not been answered. Code is in `tarav-py/src/tarav/l1/python_env/registry.py` and `src/tarav/l3/run.py`, with tests in `tests/cli/test_run_registry.py`; [Impl.Req 875](../../../tarav-py/notes/live/875-run-script-registry-impl-req.md) records verification and two small deviations.
<!-- tarav.breadcrumb 1aa842827255e331ecbff11718a21643ed41cabd854fa7455c7aa653740bed8b -->
