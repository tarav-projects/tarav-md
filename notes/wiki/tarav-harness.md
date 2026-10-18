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
<!-- tarav.breadcrumb 45aa14855439 -->

The intended operating loop is:

```text
inspect state -> choose an allowed action -> process -> validate -> emit POIs
    -> fix or bless -> reevaluate
```
<!-- tarav.breadcrumb bd9691f94b38 -->

Prompts, tools, schemas, and transition constraints form the *a priori* quality
front. Deterministic checks, linters, Agent audits, and human review form the
*posterior* front. The promise is not that errors become impossible, but that
the probability of a bad result remaining unnoticed decreases as work and
tooling accumulate. No POIs means only that nothing was detected.
<!-- tarav.breadcrumb eb223eca3f8b -->

## Pregeneration and postgeneration feedback

Pregeneration harnessing supplies context to improve the chance that generation
does what the user intends. Postgeneration harnessing audits or lints the work
so detectable deviations do not pass unnoticed. The postgeneration feedback
from one step becomes part of the pregeneration context of the next, guiding
the collaboration toward convergence.
<!-- tarav.breadcrumb 198fe08b34e6 -->

The design assumes a good-faith agent that has loaded skills explaining Tarav
and its purpose. A short generate → check → revise loop can eliminate a class
of detectable defects without proving complete semantic correctness. The
compiler loop is the motivating analogy. The convergence target is no
deviations detected by the available checks; adding useful checks makes the
system more robust.
<!-- tarav.breadcrumb 559ef4ddb758 -->
<!-- tarav.breadcrumb ce59ffb0a437 -->

Tests are a surface for expressing intention and an interface for guiding the
agent. Pre/postgeneration is a design concept whose loop can be as small as
one method call. Checks can be injected into library methods, avoiding reliance
on the agent remembering to run them at the end. The design can control how
feedback is surfaced to avoid flooding the agent.
<!-- tarav.breadcrumb f530bbdef0ed -->

The library participates in both sides of the loop: its methods express
supported actions and its code supplies context, while operation boundaries
provide places to run checks and return feedback. This control is one reason
running Tarav scripts is a main interface to the system.
<!-- tarav.breadcrumb 6d89b124ca35 -->
<!-- tarav.breadcrumb be5bbd610fd0 -->

## Records and semantic authority

A registered class is the authoritative interpreter of its serialized Record.
The JSON representation remains publicly inspectable, but its semantics belong
to the registered class hierarchy. Generic machinery may read or search the
representation; code that assigns meaning to it must use that class or an
appropriate supertype.
<!-- tarav.breadcrumb faa2825a9291 -->
<!-- tarav.breadcrumb 5579b99b4852 -->

`Type.Resolution.PATH` is the universal, deliberately simple mechanism for
selecting a class from an opaque retained Record. Every independently loadable
JSON object, including each JSONL line, declares its Type at its serialized
root. Once dispatch has selected the registered class, ordinary code owns the
representation and may construct nested objects directly; disk layout should
otherwise be irrelevant to most behavior.
<!-- tarav.breadcrumb 637afeda5384 -->
<!-- tarav.breadcrumb 5f48ce1e454a -->

Opaque JSON does not need a Tarav wrapper. General callers use the JSON library;
typed callers use a Registry or a compatible registered class. A Registry load
returns the authoritative registered class, while a class load is valid only
when the caller is that registered class or one of its descendants.
<!-- tarav.breadcrumb 83f18b785dc0 -->
<!-- tarav.breadcrumb 3caf2c395bfb -->

## Ship identity

A Ship UUID is a semantic landmark with almost no intrinsic meaning. The same
identity primitive can identify a class Type, a retained Record, or domain
cargo. Its containing class and relationship supply the semantics.
<!-- tarav.breadcrumb 89816125156c -->
<!-- tarav.breadcrumb c5fd26439cec -->

Therefore a class can both *have a Ship* as a semantic Type and *model Ships*
inside its Records. Harness should not infer Ship roles from UUID shapes or
serialized paths. A `TaravRecord` exposes its semantic projection through
`ships()`, returning Ship instances selected by the authoritative class.
<!-- tarav.breadcrumb d6dab5491413 -->
<!-- tarav.breadcrumb 8be1a42ce066 -->

## Human-paced evolution

Tarav is a Hugentic system: the human is constitutive of its operation, and
its core workflows assist that human. The intended pace of system evolution
is coupled to human capabilities. Human review before continuation may be
introduced deliberately to slow agents, even when they perform correctly, so
the human knows what is happening and can absorb the system's evolution.
These review points serve human awareness and pacing as well as correctness.
<!-- tarav.breadcrumb 979eec8655b8 -->
<!-- tarav.breadcrumb f884588f77cd -->

## Transparent checking infrastructure

The check-revise loop is one supporting system. As with a shallow test suite,
a clean run supplies only the signal supported by its checks. The design
values checks that are cheap to run, scalable, and especially transparent:
their code can be inspected and revised. Suboptimal use of that infrastructure
is possible; it does not claim complete assessment of the result.
<!-- tarav.breadcrumb 46a1d9db6d70 -->

## Evaluation growth

The next shared capabilities to consolidate are `assertions()` and
`findings()` on an evaluation-bearing `TaravRecord` subtype such as
`TaravObject`. `actions()` and explicit `state()` remain later discoveries,
introduced only when real workflows establish their useful common shape.
<!-- tarav.breadcrumb 15e9dd3cddbf -->

## External harness and selective workflow formalization

Tarav is an external harness around agent work. The native agent harness,
user, tools, permissions, and internal reasoning remain outside Tarav's
control. Tarav becomes active when an agent executes a Tarav workflow such as
capture, navigation, archive registration, or Model construction.
<!-- tarav.breadcrumb 119e81ecba21 -->
<!-- tarav.breadcrumb 29d0644c9b82 -->

The workflow graph describes typed state and possible actions. Before
generation, it gives the agent context and available affordances. After
generation, it evaluates the resulting action and state, producing Records,
Assertions, findings, and POIs. Tarav formalizes the selected slice of work;
it does not overconstrain the agent outside that workflow.
<!-- tarav.breadcrumb fc0dbfa31adf -->
<!-- tarav.breadcrumb b32eb0f4e35f -->

Workflows are selectively composable. A session may use Tarav partially and
return to ordinary native-agent work between workflow executions. The user
and native harness remain in control; entering a workflow activates its
bounded formalization.
<!-- tarav.breadcrumb 6552112683b1 -->

The Tarav Python library is the agent-facing operating environment: it exposes
context discovery, actions, durable state, and evaluation. Scripts, CLI
commands, and skills are consumers of the library and should invoke the same
workflow operations.
<!-- tarav.breadcrumb 59fca4e0a689 -->

### Project packages as operational libraries

A project package can serve as an operational interface for agent-written
Python. The project owns bounded operations whose code precisely declares its
formats, placement rules, mutations, and checks. The agent remains free to
compose those operations into a new script for the task and to supply the
semantic judgment the operation cannot encode.
<!-- tarav.breadcrumb c93ec20584d6 -->

The useful boundary is local and composable: an operation exposes typed inputs
and ordinary Python values, performs one coherent project mutation, and returns
structured results. When the operation can assess its result, it returns bound
POIs directly to the caller so revision does not depend on parsing CLI output or
remembering a separate audit command.
<!-- tarav.breadcrumb 29780168987a -->

The learning path is part of this interface. Project instructions should point
to one runnable example and the relevant source contracts, allowing progressive
inspection without requiring an agent to reconstruct the whole package. This
pattern does not require a generic operation engine or a Program lifecycle;
those abstractions remain discoveries for workflows that demonstrate a need.
<!-- tarav.breadcrumb 2e1a04bddd0c -->

### Unified Python runner

`tarav run [--project [PATH]] -- <python arguments>` is the sole Python
execution command. The words after `--` pass to Python unchanged, including
scripts, `-c`, `-m`, and stdin `-`. Without `--project`, it runs in the installed
Tarav environment. Bare `--project` discovers the nearest Project from the
current directory upward and errors outside a Project; a path starts that
search elsewhere. A selected Project supplies its interpreter and working
directory. Scripts import library operations explicitly; the typed Project
bootstrap remains a library API. See `tarav-py/notes/live/850-unified-run-cli-impl-req.md`.
<!-- tarav.breadcrumb 14a6faa72462 -->
<!-- tarav.breadcrumb aff25ca08815 -->

## Agent-directed context navigation

Where context efficiency matters, Tarav should remain mechanically simple and
avoid flooding an agent with available material. It supplies navigation tools
and hints; the agent decides what to expand, taking account of what it already
has in context and need not reload.
<!-- tarav.breadcrumb bd393792c7cb -->
<!-- tarav.breadcrumb eccc4e6a7f41 -->

The filesystem is the working analogy: listing, head/tail previews, and full
reads are basic primitives, with expansion selected by the agent. Expose
resolved full paths so the agent can also inspect material with its own tools.
Tarav enables navigation rather than choosing the agent's loading sequence.
<!-- tarav.breadcrumb 5f13bdce23ec -->
<!-- tarav.breadcrumb 6fbe16781b02 -->
