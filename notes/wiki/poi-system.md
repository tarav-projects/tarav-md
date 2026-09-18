# POI visibility, navigation, and blessings

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Detection and presentation

Detection retains all findings, including blessed ones. Presentation defaults
to all POIs in scope, with compact counts/grouping and bounded pages. Agents
can selectively expand evidence, check code, documentation, or blessing
records. This separates full finding visibility from how much material enters
the agent's context.
<!-- tarav.context 5626cd5f:aa9a2fab99ccb3b1 -->

POIs are analogous to automatic issues. Their existence does not mean an agent
must address all of them during every task. Users and agents choose which
findings to address for a particular workflow; navigation should protect the
agent's context from being flooded.
<!-- tarav.context 5626cd5f:cea96d34169da33f -->

## Minimal navigation

An agent facing a POI needs a route to understand what it checks and where its
documentation lives. The initial navigation primitive can simply point to the
path of the POI class. A richer navigation interface is not a prerequisite for
providing that entry point.
<!-- tarav.context 5626cd5f:bbac0c1dcd8f0019 -->
<!-- tarav.context 5626cd5f:aa9a2fab99ccb3b1 -->

## Recorded blessings and permitted resolutions

A blessing is an agent action accepting the state as valid despite a raised
POI. Blessing actions must be recorded so they can be scored. A blessed POI
remains visible, marked as blessed rather than disappearing from the findings.
<!-- tarav.context 5626cd5f:bbac0c1dcd8f0019 -->
<!-- tarav.context 5626cd5f:cea96d34169da33f -->

Not every POI is blessable. Some represent errors whose intended resolution is
fixing the analyzed surface. The blessing system must preserve that distinction.
These are design requirements; this capture does not assert a completed
implementation or settle the blessing Record schema.
<!-- tarav.context 5626cd5f:cea96d34169da33f -->
