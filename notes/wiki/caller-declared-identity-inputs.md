# Caller-declared identity inputs

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
f5845518 = claude-code:4ee3b84e-14fa-4aa9-9c6f-8d139954fe18 @f5845518e808c6cf0496f867fc656fdad9063980a184f7c3f15c54adf8fcb31f
-->

## Principle

When a mechanism hashes a situation or state to identify it, the caller should
describe that situation explicitly as a `LiteRecord`. The shared mechanism
should not bury heuristics about which facts matter inside its implementation.
The caller is responsible for the description; shared code handles its
serialization and hashing. This is a general design pattern, not only a POI
identity rule.
<!-- tarav.breadcrumb 5b788275a943 -->

## Responsibility stays visible

Choosing identity inputs is a semantic decision: it determines which
differences distinguish situations and which do not. An explicit LiteRecord
places that decision at the call site, where the producer knows the use case.
The heuristic is not eliminated; it is exposed as the construction of the
situation description instead of being hidden in generic machinery.
<!-- tarav.breadcrumb 84a9fda3121a -->

Simple defaults remain useful. They do not transfer responsibility for
describing the situation away from the caller or require the common mechanism
to infer its meaning. The goal is simple mechanics with visible identity
inputs, not a smarter system for guessing equivalence.
<!-- tarav.breadcrumb 168bd44bcf4e -->

## LiteRecord boundary

LiteRecord gates accepted values through supported serialization. A caller may
provide supported native types, such as dates or Tarav Types, without manually
converting them. This separates how a value is represented from the caller's
decision that the value belongs in the situation description.
<!-- tarav.breadcrumb 56d8b6704573 -->
<!-- tarav.breadcrumb c34e3bb0914f -->

The [POI situation-identity design](poi-system.md#2026-10-01--situation-is-the-identity-input)
is one application: its concrete class Ship and caller-declared situation
determine identity. Blessing is a consumer of that identity, not the reason
for hiding additional equivalence heuristics inside the shared mechanism.
<!-- tarav.breadcrumb bfe5490bf387 -->
<!-- tarav.breadcrumb 323a92d553b6 -->

## Explicit mechanism, flexible construction

“Caller-declared” does not require manually supplying a situation on every
call. Types may provide well-defined state builders and simple defaults.
Direct construction should remain available, especially when cases differ
or the design is changing quickly. This clarifies the earlier call-site
wording: the mechanism is explicit, not necessarily every invocation.
<!-- tarav.breadcrumb 30136e5c5e63 -->

Regardless of how it is supplied, the hash is computed from a `StateRecord`,
which is a `LiteRecord`. The application may constrain those records through
interfaces and checks. Explicit input therefore does not mean unconstrained
input; construction choices converge on the same inspectable hashing input.
<!-- tarav.breadcrumb 2c8642133f7e -->

The general LiteRecord can serve flexible cases; a specialized state type can
provide homogeneous descriptions across multiple call sites. A POI type
exposing its `StateType` was proposed as one example. This records a design
option, not a claim that such an interface is already implemented.
<!-- tarav.breadcrumb 93b71386e198 -->

SKW generation inputs and context freshness were accepted as a good candidate
for this pattern. The acceptance identifies an application to explore; it
does not itself establish a completed SKW change.
<!-- tarav.breadcrumb bee32953e345 -->

## The same pattern for usage traces

The User described this as a common Tarav design pattern beyond POI identity.
When a shared mechanism cannot know what describes a situation, the caller
provides the description, in the least constrained interface as a JSON record
of key-value pairs, and is expected to be clever and brief: for a file, a
path and a content hash, not the content. The Usage Registry applies it to
how a command or method was called. See [Live Help](live-help.md).
<!-- tarav.breadcrumb 7dd018d66065 -->
