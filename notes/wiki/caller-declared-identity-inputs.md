# Caller-declared identity inputs

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Principle

When a mechanism hashes a situation or state to identify it, the caller should
describe that situation explicitly as a `LiteRecord`. The shared mechanism
should not bury heuristics about which facts matter inside its implementation.
The caller is responsible for the description; shared code handles its
serialization and hashing. This is a general design pattern, not only a POI
identity rule.
<!-- tarav.breadcrumb 5b788275a9436aca5210d282fedb406cd3972532884ede77c85de2fa86f8b231 -->

## Responsibility stays visible

Choosing identity inputs is a semantic decision: it determines which
differences distinguish situations and which do not. An explicit LiteRecord
places that decision at the call site, where the producer knows the use case.
The heuristic is not eliminated; it is exposed as the construction of the
situation description instead of being hidden in generic machinery.
<!-- tarav.breadcrumb 84a9fda3121af498571bc6c9b146001812f84f1fc325daded05eb8b300afd058 -->

Simple defaults remain useful. They do not transfer responsibility for
describing the situation away from the caller or require the common mechanism
to infer its meaning. The goal is simple mechanics with visible identity
inputs, not a smarter system for guessing equivalence.
<!-- tarav.breadcrumb 168bd44bcf4e290143aee6d90e5c7c4213c7b99c2a1c0107cd9a2e34262c8b1b -->

## LiteRecord boundary

LiteRecord gates accepted values through supported serialization. A caller may
provide supported native types, such as dates or Tarav Types, without manually
converting them. This separates how a value is represented from the caller's
decision that the value belongs in the situation description.
<!-- tarav.breadcrumb 56d8b67045739b297594dc64080f23f018d77902dd9109fa094939f257607ba6 -->
<!-- tarav.breadcrumb c34e3bb0914f9c634d0a2552b5dfe74e2fd88f07be7817a37613b3cac8382648 -->

The [POI situation-identity design](poi-system.md#2026-10-01--situation-is-the-identity-input)
is one application: its concrete class Ship and caller-declared situation
determine identity. Blessing is a consumer of that identity, not the reason
for hiding additional equivalence heuristics inside the shared mechanism.
<!-- tarav.breadcrumb bfe5490bf387811876101ca7343cf0c825db3cfc5b47d550ef12b59336ac5b66 -->
<!-- tarav.breadcrumb 323a92d553b63b3ad4dba167f7093813119e4343c10c7faa006065426778f4e4 -->
