# agentos-skillware --edition-history

Use this module when the caller wants to recover, record, amend, inspect, or lint the chat sessions associated with a managed file's Git editions.

`Skw.Edition.History.Service` is deterministic; this module performs the agentic discovery and support judgment around it. Git supplies editions, Chatlas supplies candidate sessions and transcript fragments, and `agentos skw edition-history` is the only persistence boundary.

## Inputs

- use the target file's Agentos-project depot by default; pass `--depot` only for an intentional lifecycle or test override
- require exactly one selection mode:
  - `--target <file>` — repeatable; every target must be an eligible file selected by the project-level `.skw/skw.json` `edition_history.targets` minus `edition_history.exclude`
  - `--random` — select one eligible file from the current Agentos project
- reject `--target` with `--random`, either selector without `--edition-history`, or `--edition-history` without a selector
- work with project-relative file paths when querying Git and Chatlas
- treat the target list as the linter scope; no package-wide completeness claim follows from checking it

## Target Selection

For `--target`, resolve every path inside the current Agentos project and verify that it belongs to the configured eligible set before recovery.

For `--random`, expand the configured eligible set and choose one file from the first nonempty tier:

1. files reported by the default project check as `missing-edition-history`
2. files reported by `agentos skw check --check unsupported-git-edition --json` as `unsupported-git-edition`
3. any configured eligible file

Deduplicate paths within each tier. Selection is random only inside the highest-priority nonempty tier. Print the selected project-relative path and its tier before starting recovery. Fail clearly when the current directory is not inside an Agentos project, edition-history policy is absent, or the configured eligible set is empty.

After selection, `--random` and `--target` run the same recovery workflow.

## Recovery Workflow

1. Resolve the target's Agentos project root and project-relative path.
2. Enumerate every discoverable edition with rename following:

   ```bash
   git log --follow --format='%H%x09%cI' -- <project-relative-path>
   ```

3. Refresh Chatlas and build a candidate session list from several independent signals. Start with normalized file touches and tool events, but always include raw transcript matching for both the project-relative path and basename; normalization can miss generic editing mechanisms or whole-session candidates. Also search visible transcript text, repository attribution, working directory, and the Git edition's time neighborhood. Use newest-first ordering and a scan limit large enough to reach the edition window. Do not require every signal to agree, and do not exclude umbrella-workspace sessions merely because the file belongs to a nested project.

   ```bash
   agentos chatlas query --file-touched <project-relative-path> --update
   agentos chatlas query --tool-contains <path-or-basename> \
     --sort newest --scan-limit 5000 --field identity_hash
   agentos chatlas query --raw-contains <project-relative-path> \
     --sort newest --scan-limit 5000 --field identity_hash
   agentos chatlas query --raw-contains <basename> \
     --sort newest --scan-limit 5000 --field identity_hash
   agentos chatlas query --message-contains <path-or-basename> \
     --sort newest --scan-limit 5000 --field identity_hash
   ```

4. Inspect a focused event fragment for every candidate. `file-edition-pois` ranks normalized file-mutation evidence but remains a heuristic; broad matching and POIs only discover candidates and never establish an association. Resolve the candidate's native session id for the POI pass and retain its neutral Chatlas identity for persistence.

   ```bash
   agentos chatlas file-edition-pois \
     --session <native-session-id> --file <project-relative-path> --json
   agentos chatlas views get --identity-hash <chatlas-identity> \
     --tool-contains <path-or-basename> --view events --json
   agentos chatlas views get --identity-hash <chatlas-identity> \
     --around <ISO-time> --radius 6 --view events --json
   ```

5. Establish a content bridge from the transcript mutation to the Git edition. Inspect the target file's commit diff and verify that the supported mutation produced content represented in that edition:

   ```bash
   git show --format=fuller --find-renames <commit> -- <project-relative-path>
   ```

   A direct write inside the edition's time window proves that the session edited the file, but does not by itself prove contribution to that edition: the write may have been reverted, superseded, or committed later. Associate the session only when the inspected mutation fragment and the commit diff describe the same resulting change. Temporal proximity helps rank candidates but is never sufficient support by itself.
6. Build one embedded `chatlas.support-set.v1` object from the exact supporting events used by that content bridge. Use the neutral Chatlas `identity_hash` as both `--session` and each relevant member's `session`; copy each `event_id` and timestamp exactly. The set must be nonempty and must include the associated session.

   ```json
   {
     "app": "chatlas",
     "schema": "chatlas.support-set.v1",
     "hint": "This session edited the target file.",
     "members": [
       {
         "session": "<chatlas-identity>",
         "event_id": "<event-id>",
         "at": "<exact-event-timestamp>"
       }
     ]
   }
   ```

7. Record every accepted association through the service:

   ```bash
   agentos skw edition-history record \
     --file <file> --commit <commit> --session <chatlas-identity> \
     --session-started-at <ISO-time> \
     --support-file <support-set.json>
   ```

8. Repeat safely as more Chatlas material becomes available; equivalent record calls are idempotent.
9. If better or corrected proof becomes available, replace the association's complete support set through the service rather than editing Bloberia directly:

   ```bash
   agentos skw edition-history amend \
     --file <file> --record <record-id> \
     --support-file <replacement-support-set.json>
   ```

10. Close by reading the Git-complete grouped history and running both linter levels. Through the umbrella `agentos` executable, these operations resolve every support member against Chatlas and reject unavailable sessions, missing events, or timestamp mismatches.

   ```bash
   agentos skw edition-history list --file <file>
   agentos skw edition-history check --target <file>
   agentos skw edition-history check --target <file> --complete
   ```

## Judgment Rules

- seek all editing sessions discoverable for every Git edition, not merely the last editor
- a session association records historical contribution; it does not claim sole authorship or `Touched.Authority`
- use a battery of discovery heuristics because agents may edit through patch tools, shell commands, scripts, or batch operations
- inspect surrounding transcript detail for every candidate and record only exact events that prove contribution
- require correspondence between the supported mutation and the target commit's file diff; an edit event plus temporal proximity is not edition attribution
- persist the support consumers need; never persist discovery signals or search mechanics
- preserve Chatlas session start time when available so stored timing can later be reconciled
- if support remains ambiguous, leave the association unrecorded and report the candidate rather than guessing
- treat the default check as the minimum presence gate; run `--complete` on demand to measure every unsupported Git edition without making that backlog the normal inner loop
- amendment replaces the complete support set and may update the stored session start time; preserve still-valid members when enriching proof
- never write `skw.edition-session` records directly with `agentos bloberia`; callers consume the Skillware schema through its service

## Completion

Return the target files, total/supported/unsupported Git editions, associations created versus already present or amended, unresolved candidates, and both minimal and requested completeness findings. A clean minimal check means every target has at least one structurally valid association whose support resolves through Chatlas; only the opt-in completeness check measures the remaining Git-edition backlog, and neither check judges semantic correctness.
