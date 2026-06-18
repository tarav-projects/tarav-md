# Harness.Injected.ENV — Appendix

****

## Harness.Injected.ENV/Examples

- home env binding is harness injection when the provider uses env to select its runtime home
- credential env binding is harness injection when the provider uses env to receive a managed credential
- credential env values must be redacted in display paths
- examples: `CODEX_HOME`, `CLAUDE_CONFIG_DIR`, `COPILOT_HOME`
- credential example: `CLAUDE_CODE_OAUTH_TOKEN`
- non-example: permission flags, telemetry flags, model policy, sandbox policy
- related: `Provider.Instance`, `Agentos.Agent.Adapter`
