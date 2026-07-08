# Registry Consistency

Use this when account state looks contradictory: newest artifact is not active, active is not materialized, homes are drifted unexpectedly, or a home is aligned but live calls fail.

## Layer Model

- `registry/captures.jsonl` records observed `Auth.Data` artifacts.
- `registry/artifacts/<artifact-id>` stores the content-addressed secret payload. Do not print it.
- `registry/active.json` maps `<account>/<method>` to the desired active artifact.
- `agentos agent accounts status` compares each configured home's current `Auth.Data` to `active.json`; it performs no provider call.
- `Valid.Credentials` is separate. Only a live provider operation proves current validity.

Current state paths:

```text
~/.agentos/accounts/<provider>/accounts.json
~/.agentos/accounts/<provider>/registry/active.json
~/.agentos/accounts/<provider>/registry/captures.jsonl
~/.agentos/accounts/<provider>/registry/artifacts/<artifact-id>
```

## Read-Only Checks

```bash
agentos agent accounts status --provider <provider> --json
agentos agent accounts capture --provider <provider> --global --dry-run --json
jq . ~/.agentos/accounts/<provider>/registry/active.json
tail -n 40 ~/.agentos/accounts/<provider>/registry/captures.jsonl
agentos agent accounts materialize --provider <provider> --account <account>/<method> --home "$HOME_PATH" --check --json
```

Interpret `materialize --check`:

- `active_artifact_id`: what would be written.
- `captured_artifact_id`: what the home currently contains after a read-only capture.
- equal ids: the home is already aligned to active.
- different ids: materialization has not happened for this active artifact, or the provider updated the home after the last materialization.

## Mutating Flow

Use this only when the user asks to change state.

```bash
agentos agent accounts capture --provider <provider> --home "$HOME_PATH" --json
agentos agent accounts activate --provider <provider> --account <account>/<method> --artifact <artifact-id> --json
agentos agent accounts materialize --provider <provider> --account <account>/<method> --home "$HOME_PATH" --json
agentos agent accounts status --provider <provider> --json
```

If several homes should use the same active artifact, run `materialize` once per home.

## Failure Patterns

- `active` does not imply the home uses that artifact. It only changes `registry/active.json`.
- `aligned` does not imply live validity. It only proves home state matches active state.
- capture timestamp is not always freshness. Inspect provider-specific metadata such as Claude `expiresAt` and refresh-token presence.
- for Claude, token presence is still not enough. Compare `expiresAt` to current time and prefer a real provider check when validity is in doubt.
- materialization is capture-first. If a target home contains a new credential, that credential is archived before overwrite.
- `Unknown.Account` captures are preserved but cannot be activated until adopted into a declared account.
- very fast post-materialize drift can come from the provider mutating the home after a failed live use. Do not assume the write failed until raw home state is checked before and after a real provider operation.

## Concept Grounding

This follows `agentos-pkg` `Account.Management`:

- `Auth.Data.Capture` writes the archival layer.
- `Auth.Data.Activation` writes the registry synchronization layer.
- `Auth.Data.Materialization` writes the home/system layer.
- `Auth.Data.Aligned` and `Auth.Data.Drift` are read-only designations, not validity proofs.
