# Capabilities by subtyping

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## Principle

Tarav uses the subtyping system to express capabilities. A type declares that it has a capability by extending a base class that provides it.
<!-- tarav.breadcrumb 43b07da10ec9 -->

The reason is that code is Tarav's main documentation. An agent that reads the declaration of a type sees everything it extends, and can open the context of each parent in turn. The documentation therefore chains naturally through the parents.
<!-- tarav.breadcrumb 79b083bdfded -->

## The type declares, the instance decides

Two design patterns appear to conflict: expressing a property in the type, and deciding it at call time. Tarav uses both, and gives them different jobs. The type declares the capability, and the instance decides whether to use it where the type allows.
<!-- tarav.breadcrumb 9b17a14f7a26 -->
<!-- tarav.breadcrumb 9a94c223c611 -->

Even at the subtype level a capability can be optional or not: what a parent provides may or may not be overruled. A capability provider can expose a way to overrule the capability, or to configure its extent, at construction. A subtype that does not expose that option makes the capability hold for every one of its instances.
<!-- tarav.breadcrumb d7ed606abc98 -->
<!-- tarav.breadcrumb 9f2942caeaac -->

## Worked example: tracking a POI

A POI described by a situation is a natural tracked POI, because the situation defines what is being followed. Tracking still cannot simply be added to every POI: some situations are not fixed points, for example one that depends on a timestamp. So tracking is up to the caller.
<!-- tarav.breadcrumb 46c15508c050 -->

A homogeneous type, whose instances share one meaning across different places, extends the tracking base, and every instance is stored when it is raised. A type whose instances differ each time, such as a notification with a different message each time, cannot express tracking in the type alone and needs a call parameter. Both patterns are used. The tracked-POI design itself is in [POI visibility, navigation, and blessings](poi-system.md).
<!-- tarav.breadcrumb 3b0c1d5c89a8 -->

## Agent proposals, not decided

The following came from the agent during the discussion and were not confirmed by the User.

- Three kinds of trackable type: always tracked, with no way out in the constructor; tracked by default but overrulable; and trackable but off unless the caller opts in.
- `BlessablePOI` already follows this pattern: a type opts into being blessable by extending it.
- A wrong claim of being trackable could be detected from the store, because a type whose situations are not fixed points produces identities that never recur.

See also [Settings capability](settings-capability.md), the convention for configuring capabilities.
