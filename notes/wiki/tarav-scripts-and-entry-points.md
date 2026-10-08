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
