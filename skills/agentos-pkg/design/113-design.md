> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Hook

- [DF] `Agentos.Hook` is the named event ingress and dispatch mechanism through which producers invoke registered Agentos subsystem callbacks. ^c20260811-3u
- [DC] Hook names are dot-separated, namespaced identifiers whose first segment identifies the owning domain. ^c20260811-4u
- [DC] Subsystems register zero or more callbacks under an exact hook name during Agentos CLI composition. ^c20260811-5u
- [DC] The dispatcher invokes every callback registered under the received hook name sequentially in registration order. ^c20260811-6u
- [DC] A callback failure is logged and dispatch continues with the remaining callbacks. ^c20260811-7u
- [DC] Callback failures do not fail the hook command; invocation validation failures do. ^c20260811-8u
- [CT] Failure logs identify the hook and callback without recording the complete context by default. ^c20260811-9u
- [RJ] Initial registration excludes wildcard subscriptions, priorities, dynamic discovery, and dependency ordering. ^c20260811-10u
- [FR] Callback return values and response aggregation remain undefined until a consumer requires them. ^c20260811-11u

## Agentos.Hook.Invocation

- [DF] `Agentos.Hook.Invocation` is the value delivered to the dispatcher, composed of a hook `name`, an optional `ctx_type`, and a JSON-object `ctx`. ^c20260811-12u
- [DC] `ctx` remains opaque to the dispatcher and is passed unchanged to each selected callback. ^c20260811-13u
- [DF] `ctx_type` is an optional open-string label identifying the context producer or schema; its absence means unknown or untyped context. ^c20260811-14u
- [CT] `ctx_type` accompanies `ctx` without being inserted into it and does not participate in callback selection. ^c20260811-15u
- [DC] The public ingress command is `agentos hook --name <hook-name> [--ctx-type <ctx-type>]`. ^c20260811-16u
- [DC] Each CLI invocation selects exactly one context input: `--ctx-from-stdin` or `--ctx <json>`. ^c20260811-17u
- [DC] `--ctx-from-stdin` is the canonical harness input and reads the JSON context from standard input. ^c20260811-18u
- [DC] `--ctx <json>` is the inline input for small manual invocations. ^c20260811-19u
- [CT] Malformed JSON, a missing hook name, or conflicting context inputs invalidate the invocation before dispatch. ^c20260811-20u

## Agent.Hook

- [DF] `Agent.Hook` is the initial agent-lifecycle vocabulary within the general `Agentos.Hook` namespace. ^c20260811-21u
- [DC] An agent provider integration maps its native lifecycle callbacks onto the nearest matching `Agent.Hook` names. ^c20260811-22u
- [CT] A provider may support only a subset of `Agent.Hook`; emitting a hook means the provider integration observed that semantic boundary. ^c20260811-23u
- [DF] `agent.session.start` means an agent session has become active for a harness run. ^c20260811-24u
- [DF] `agent.prompt.submit` means a prompt has been accepted as input for a new agent turn. ^c20260811-25u
- [DF] `agent.tool.before` means a tool invocation has been selected and is about to execute. ^c20260811-26u
- [DF] `agent.tool.after` means a tool invocation has reached a terminal outcome and its result or error is available. ^c20260811-27u
- [DF] `agent.context.before_compact` means the active agent context is about to be compacted. ^c20260811-28u
- [DF] `agent.context.after_compact` means compaction has completed and the resulting context has become active. ^c20260811-29u
- [DF] `agent.subagent.start` means delegated child-agent execution has begun. ^c20260811-30u
- [DF] `agent.subagent.stop` means delegated child-agent execution has reached a terminal outcome. ^c20260811-31u
- [DF] `agent.turn.stop` means the current agent turn has reached a terminal outcome. ^c20260811-32u
- [DF] `agent.session.end` means the provider integration reports that an agent session is ending or is no longer active. ^c20260811-33u
