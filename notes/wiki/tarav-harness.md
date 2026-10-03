# Tarav.Harness

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
1ae20f8c = codex:01a0ff32-0ec2-7b72-8850-fa795135f3c9 @1ae20f8c8159f12d2402ea702cf49c876ec46a72f71ce12423ae1dbdf2a91871
-->

## Purpose

`tarav.harness` is the reusable core for making arbitrary systems legible,
operable, and self-evaluating for Agents. It provides the primitives needed to
build domain-specific harnesses; Diagram is one consumer, and PaperSON can be
another. Tarav may remain one project, but Harness must remain independent of
Diagram, Archive, Chatlas, Skillware, and CLI semantics.
<!-- tarav.breadcrumb 45aa1485543925fe2a24961f6f30312a8f5dff8a4b348fea3f7e960d2e5f4c61 -->

The intended operating loop is:

```text
inspect state -> choose an allowed action -> process -> validate -> emit POIs
    -> fix or bless -> reevaluate
```
<!-- tarav.breadcrumb bd9691f94b3845f0c5a983575f7da2c8d87a1829ce83feb10fb005ab8d0948d4 -->

Prompts, tools, schemas, and transition constraints form the *a priori* quality
front. Deterministic checks, linters, Agent audits, and human review form the
*posterior* front. The promise is not that errors become impossible, but that
the probability of a bad result remaining unnoticed decreases as work and
tooling accumulate. No POIs means only that nothing was detected.
<!-- tarav.breadcrumb eb223eca3f8b813cb1cb4344056a3766baec78ce3c6f72534a28523d2f574028 -->

## Pregeneration and postgeneration feedback

Pregeneration harnessing supplies context to improve the chance that generation
does what the user intends. Postgeneration harnessing audits or lints the work
so detectable deviations do not pass unnoticed. The postgeneration feedback
from one step becomes part of the pregeneration context of the next, guiding
the collaboration toward convergence.
<!-- tarav.breadcrumb 198fe08b34e6fb77fc5579451ea0f64e2698a5750a9258b30aa98768cbb9fa27 -->

The design assumes a good-faith agent that has loaded skills explaining Tarav
and its purpose. A short generate → check → revise loop can eliminate a class
of detectable defects without proving complete semantic correctness. The
compiler loop is the motivating analogy. The convergence target is no
deviations detected by the available checks; adding useful checks makes the
system more robust.
<!-- tarav.breadcrumb 559ef4ddb7582c0ec464e5ad6b4bf658306642dfda7d5ae085f916e61ed082cd -->
<!-- tarav.breadcrumb ce59ffb0a4370d54cc91bc2c00416c6e338b52cfb15166f8b6328f51f880a8b5 -->

Tests are a surface for expressing intention and an interface for guiding the
agent. Pre/postgeneration is a design concept whose loop can be as small as
one method call. Checks can be injected into library methods, avoiding reliance
on the agent remembering to run them at the end. The design can control how
feedback is surfaced to avoid flooding the agent.
<!-- tarav.breadcrumb f530bbdef0edb7ddafcd458abc33e52ccd0100ee41fd093aab3b358c654433aa -->

The library participates in both sides of the loop: its methods express
supported actions and its code supplies context, while operation boundaries
provide places to run checks and return feedback. This control is one reason
running Tarav scripts is a main interface to the system.
<!-- tarav.breadcrumb 6d89b124ca357e017baf8cb02e3785f2b28b3d646f98c8883762ca535bacbe1f -->
<!-- tarav.breadcrumb be5bbd610fd0dca5d99f032d6d27a411235083d1cdfe6238fb0b14bd58ffe06b -->

## Records and semantic authority

A registered class is the authoritative interpreter of its serialized Record.
The JSON representation remains publicly inspectable, but its semantics belong
to the registered class hierarchy. Generic machinery may read or search the
representation; code that assigns meaning to it must use that class or an
appropriate supertype.
<!-- tarav.breadcrumb faa2825a9291a6d80f443b8003e8ee82fd5454a460f4efb824c10d7d75f41272 -->
<!-- tarav.breadcrumb 5579b99b4852388298d2f2ac18087f8370c131de4e410846fa03c137c987e6b3 -->

`Type.Resolution.PATH` is the universal, deliberately simple mechanism for
selecting a class from an opaque retained Record. Every independently loadable
JSON object, including each JSONL line, declares its Type at its serialized
root. Once dispatch has selected the registered class, ordinary code owns the
representation and may construct nested objects directly; disk layout should
otherwise be irrelevant to most behavior.
<!-- tarav.breadcrumb 637afeda5384e682adfcc42d982f4c2a1ab9be76009d75f5720773bfbf0cd2eb -->
<!-- tarav.breadcrumb 5f48ce1e454a5d569a13988a7379a89399bca3b02499283e96f83d676d47676b -->

Opaque JSON does not need a Tarav wrapper. General callers use the JSON library;
typed callers use a Registry or a compatible registered class. A Registry load
returns the authoritative registered class, while a class load is valid only
when the caller is that registered class or one of its descendants.
<!-- tarav.breadcrumb 83f18b785dc0cf390e34f3e64bea06480e9b1b5c6b6efeebfb826595fcdcd5d7 -->
<!-- tarav.breadcrumb 3caf2c395bfb1e362701d5e8428fc4a1cb9b1438b030917b67642638cf5d89dc -->

## Ship identity

A Ship UUID is a semantic landmark with almost no intrinsic meaning. The same
identity primitive can identify a class Type, a retained Record, or domain
cargo. Its containing class and relationship supply the semantics.
<!-- tarav.breadcrumb 89816125156cc53a1dd29f5b2c783a74c62d8d9b727014343d6e0e2b178e6206 -->
<!-- tarav.breadcrumb c5fd26439cec9ac4e398df2e45b1d5f4bd8bd5789abe9f9e2e29d98be302e699 -->

Therefore a class can both *have a Ship* as a semantic Type and *model Ships*
inside its Records. Harness should not infer Ship roles from UUID shapes or
serialized paths. A `TaravRecord` exposes its semantic projection through
`ships()`, returning Ship instances selected by the authoritative class.
<!-- tarav.breadcrumb d6dab5491413ff39825f04a32daab3d8b8ce78b19030f5f77884ad5ff8abca5c -->
<!-- tarav.breadcrumb 8be1a42ce06631f49866741c5e2f4a7f65fdedec18fa40ab359f13c934422136 -->

## Human-paced evolution

Tarav is a Hugentic system: the human is constitutive of its operation, and
its core workflows assist that human. The intended pace of system evolution
is coupled to human capabilities. Human review before continuation may be
introduced deliberately to slow agents, even when they perform correctly, so
the human knows what is happening and can absorb the system's evolution.
These review points serve human awareness and pacing as well as correctness.
<!-- tarav.breadcrumb 979eec8655b8d329adc75c62cc2a5f4a397363a6d2daf6133fb8dd8763d321ff -->
<!-- tarav.breadcrumb f884588f77cd62f1cf719a25a9568d0f02e8e3dd31ec31c53caabfc46a789073 -->

## Transparent checking infrastructure

The check-revise loop is one supporting system. As with a shallow test suite,
a clean run supplies only the signal supported by its checks. The design
values checks that are cheap to run, scalable, and especially transparent:
their code can be inspected and revised. Suboptimal use of that infrastructure
is possible; it does not claim complete assessment of the result.
<!-- tarav.breadcrumb 46a1d9db6d707dd3f95c1867603cfa3e67c7908b73e78d4788442ffb381c0cad -->

## Evaluation growth

The next shared capabilities to consolidate are `assertions()` and
`findings()` on an evaluation-bearing `TaravRecord` subtype such as
`TaravObject`. `actions()` and explicit `state()` remain later discoveries,
introduced only when real workflows establish their useful common shape.
<!-- tarav.breadcrumb 15e9dd3cddbf95311a9a2df9aa3cc3aa52868f4bcf214c1c18f92bc39793d142 -->

## External harness and selective workflow formalization

Tarav is an external harness around agent work. The native agent harness,
user, tools, permissions, and internal reasoning remain outside Tarav's
control. Tarav becomes active when an agent executes a Tarav workflow such as
capture, navigation, archive registration, or Model construction.
<!-- tarav.breadcrumb 119e81ecba21226fe690c7b11a387d49578d105055141362be8567bc2be0e91d -->
<!-- tarav.breadcrumb 29d0644c9b82eb4f5079aa11654fe7a66b69df750c1f552e13d0bcab69f6b344 -->

The workflow graph describes typed state and possible actions. Before
generation, it gives the agent context and available affordances. After
generation, it evaluates the resulting action and state, producing Records,
Assertions, findings, and POIs. Tarav formalizes the selected slice of work;
it does not overconstrain the agent outside that workflow.
<!-- tarav.breadcrumb fc0dbfa31adf2fdce6c343feb178610cd6eb8f3a9227c5e87a092c517a6825c5 -->
<!-- tarav.breadcrumb b32eb0f4e35f67999febd469f6641a97f908a65032be6b432e3fce150a75c68c -->

Workflows are selectively composable. A session may use Tarav partially and
return to ordinary native-agent work between workflow executions. The user
and native harness remain in control; entering a workflow activates its
bounded formalization.
<!-- tarav.breadcrumb 6552112683b1a0f66f8df62ef53b068f3e14a51272d7d43715ed0087a613f1e0 -->

The Tarav Python library is the agent-facing operating environment: it exposes
context discovery, actions, durable state, and evaluation. Scripts, CLI
commands, and skills are consumers of the library and should invoke the same
workflow operations.
<!-- tarav.breadcrumb 59fca4e0a689608465452887b506baa3dcafc6ee73f81bfa3eb7aec258211ed3 -->

### Project packages as operational libraries

A project package can serve as an operational interface for agent-written
Python. The project owns bounded operations whose code precisely declares its
formats, placement rules, mutations, and checks. The agent remains free to
compose those operations into a new script for the task and to supply the
semantic judgment the operation cannot encode.
<!-- tarav.breadcrumb c93ec20584d6cf7a3b79ee853970fae450de898f157a0f0003bccb168258cdf7 -->

The useful boundary is local and composable: an operation exposes typed inputs
and ordinary Python values, performs one coherent project mutation, and returns
structured results. When the operation can assess its result, it returns bound
POIs directly to the caller so revision does not depend on parsing CLI output or
remembering a separate audit command.
<!-- tarav.breadcrumb 29780168987ad4a26e2ea82c378a091b76503fd367a87c015be13e5f5987ccd0 -->

The learning path is part of this interface. Project instructions should point
to one runnable example and the relevant source contracts, allowing progressive
inspection without requiring an agent to reconstruct the whole package. This
pattern does not require a generic operation engine or a Program lifecycle;
those abstractions remain discoveries for workflows that demonstrate a need.
<!-- tarav.breadcrumb 2e1a04bddd0cfdad85779e8768007cf92d869714630a1132b5ecedae419e923b -->

### Unified Python runner

`tarav run [--project [PATH]] -- <python arguments>` is the sole Python
execution command. The words after `--` pass to Python unchanged, including
scripts, `-c`, `-m`, and stdin `-`. Without `--project`, it runs in the installed
Tarav environment. Bare `--project` discovers the nearest Project from the
current directory upward and errors outside a Project; a path starts that
search elsewhere. A selected Project supplies its interpreter and working
directory. Scripts import library operations explicitly; the typed Project
bootstrap remains a library API. See `tarav-py/notes/live/850-unified-run-cli-impl-req.md`.
<!-- tarav.breadcrumb 14a6faa72462829f9895a88e253bc36b9b8dee41f5f8ca0fac7fe68efe02e2d2 -->
<!-- tarav.breadcrumb aff25ca088155aaafb47e52f580d396a6d31167b4240d97938348acbd6752fde -->

## Agent-directed context navigation

Where context efficiency matters, Tarav should remain mechanically simple and
avoid flooding an agent with available material. It supplies navigation tools
and hints; the agent decides what to expand, taking account of what it already
has in context and need not reload.
<!-- tarav.breadcrumb bd393792c7cb869490e81c9a37a21a2b0b83c696b205e34d71ee8f1d2f6c12fc -->
<!-- tarav.breadcrumb eccc4e6a7f418a7ee6103bf742331aae02879bfa958b7b13e161dee91ae32b8a -->

The filesystem is the working analogy: listing, head/tail previews, and full
reads are basic primitives, with expansion selected by the agent. Expose
resolved full paths so the agent can also inspect material with its own tools.
Tarav enables navigation rather than choosing the agent's loading sequence.
<!-- tarav.breadcrumb 5f13bdce23ecc12a238a409a7500c1c8887f0183bfc0dbc222e03b3a96718f66 -->
<!-- tarav.breadcrumb 6fbe16781b02ce61f18923f21754f8bf66056df2a381049289a8271151b8f5c7 -->
