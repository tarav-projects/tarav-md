# Chatlas Anchory Statistics - impl-req

## Impl.Abstract

- **scope:** add `agentos chatlas anchory stats` for support-set cardinality statistics without resolving transcript members
- **status:** ready for implementation
- **source:** direct autonomous development request ^c20260731-0u
- **out of scope:** generic Anchory analytics, transcript validation, date/type filtering, and changes to support-set records

## Impl.Agendix

- **touched (chat):** the command belongs under `agentos chatlas anchory`; its workflow produces a JSON-compatible object, rendered prettily by default or emitted as JSON ^c20260731-0u
- **structural:** `chatlas.support-set.v2` records and the Chatlas Anchory depot are the statistic's source surfaces

## Impl.Index

### Chatlas.Anchory.Statistics

- Chatlas owns support-set member semantics while Anchory owns generic record persistence
- the domain operation returns one canonical JSON-compatible statistics payload
- the CLI renders that payload as a concise human report by default and as JSON when requested
- member counts are read from validated records; session models and transcript neighborhoods are not loaded
- the payload reports anchor count, support-turn count, minimum, maximum, mean, population standard deviation, and cardinality distribution

## Execution.Plan

### Slice 1 - Statistics payload

- add a Chatlas Anchory domain function that queries the Chatlas namespace, validates each support-set record, and computes cardinality statistics
- define the empty-depot result without undefined numeric values
- observable: fixture records with different member counts produce deterministic aggregate values and distribution
- check: focused unit tests fail before implementation and pass afterward
- status: not started

### Slice 2 - CLI rendering

- register `agentos chatlas anchory stats` with `--format pretty|json`, defaulting to `pretty`
- render the pretty report only from the canonical payload
- observable: default output is readable and `--format json` returns the complete machine payload
- check: focused command tests and neighboring Chatlas Anchory tests pass
- status: not started

## Impl.Log

- execution gate: autonomous development invocation ^c20260731-0u
- no deviations or blockers
