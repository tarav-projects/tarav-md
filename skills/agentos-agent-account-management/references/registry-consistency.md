# Registry Consistency

Use this when account state looks contradictory: newest artifact is not active, active artifact is invalid, passive reconcile reverts homes, or homes are `matching-active` while live provider calls fail.

## Invariants To Check

For each account:

- `accounts.json.active_artifact_id` should point to the artifact intended for home materialization.
- `accounts.json.artifact_file` should match the active artifact id.
- The active artifact should exist in `artifacts.jsonl`.
- The active artifact payload file should exist under `artifacts/`.
- Known homes should hash to the active artifact.
- The active artifact should have fresh verification evidence when passive reconcile is expected to preserve it.

Commands:

```bash
jq '.accounts.<account>' ~/.agentos/accounts/<provider>/accounts.json
rg '"account":"<account>"' ~/.agentos/accounts/<provider>/artifacts.jsonl
rg '"account":"<account>"' ~/.agentos/accounts/<provider>/verifications.jsonl
agentos agent accounts status --provider <provider> --home <home> --json
```

## Failure Pattern

Registered does not mean valid.

Active does not necessarily mean freshest.

Freshest does not necessarily mean verified.

Verified matters because passive reconcile chooses from verification evidence. A newly registered Codex artifact that has not been verified can be overwritten by an older verified artifact during passive reconcile or account status.

## Repair Pattern

1. Find candidate artifacts for the account.
2. Test candidates with a real provider operation.
3. Promote the working artifact as active.
4. Write verification evidence for the working artifact.
5. Link configured and managed homes from the verified active artifact.
6. Re-run status and live validation.

For Codex, successful `account/rateLimits/read` is a strong live validation for usage-monitor problems.

## Better System Direction

The registry should separate these fields instead of overloading `active_artifact_id`:

- `latest_observed_artifact_id`
- `latest_verified_artifact_id`
- `desired_artifact_id`
- `materialized_artifact_id` per home

Passive reconcile should never silently downgrade a home from a newer observed artifact to an older verified artifact. If it sees a newer unverified artifact, it should classify the account as `needs_verification` and report the candidate. Sync should require an explicit policy decision:

- `verified-only`: preserve current behavior.
- `newest-live-verified`: verify candidate before activating.
- `manual`: report candidates only.

This would make account repair predictable and prevent the "new metadata, old active id" state.
