# Agentos.Agent

`Agentos.Agent` is the Agentos concept for an agent actor as modeled by the system: a provider-backed or locally defined actor with configured identity, capabilities, homes, runtime behavior, and provider-native surfaces.

## Agent.Instance

`Agent.Instance` is one instantiated `Agentos.Agent` object. It denotes the realized agent object Agentos can list, select, run, inspect, or ask for provider-native capabilities.

`Agent.Instance` is not the same as an `agent.instances[]` config record. Config records are input material; the runtime object should be a proper `Agentos.Agent` or concrete `<Provider>.Agent`.

## Provider Agents

Concrete provider agents, such as `Codex.Agent` or `Claude.Agent`, model provider reality from the Agentos point of view.

A provider agent may extend the general `Agentos.Agent` shape when a field is genuinely provider-specific and cannot be normalized without losing meaning. If a concept can be normalized across providers, it should use the shared `Agentos.Agent` vocabulary instead of provider-specific synonyms.

## Field Boundary

Agent fields must be limited to minimal agent metadata and facts needed to configure or run the agent runtime.

General `Agentos.Agent` fields should cover cross-provider concepts such as provider identity, instance identity, label, homes, command/runtime configuration, environment, timeout, default model behavior, and stable fingerprint.

Provider-specific `<Provider>.Agent` fields are acceptable when they are necessary to configure that provider's native agent runtime or provider-home access and cannot be cleanly represented by the general model.

Fields that are not minimal metadata and are not necessary for configuring or running the agent are not `Agentos.Agent` or `<Provider>.Agent` concerns.

## Session Boundary

Provider sessions have their own model. Facts needed to load, identify, or model session data belong on `<Provider>.SessionRef` or `<Provider>.Session`, not on `Agentos.Agent`, unless they are required to configure the agent's provider-home access.

If a field describes one session's artifacts, storage rows, rollout files, transcript paths, index references, timestamps, native ids, or provider-native session metadata, it belongs to the provider session model.

If a field describes how to discover or access many sessions from a provider home, it may be an agent capability only when it is part of configuring the provider agent's native access. Otherwise it belongs to the subsystem that performs the discovery or indexing.

## Subsystem Boundary

Subsystem concerns should not be folded into the base agent model merely because they are configured near an agent.

Chatlas raw mirroring policy, destination mapping, include/exclude rules, account usage progression, and live usage refresh behavior are subsystem projections or capability-specific configuration. They may be derived from an agent plus subsystem config, but they are not base `Agentos.Agent` fields.
