# agentos-skillware --dev (edition-history developer)

Use this module when the caller wants to recover, record, inspect, or lint the chat sessions associated with a managed file's Git editions.

`Skw.Edition.History.Service` is deterministic; this module performs the agentic discovery and support judgment around it. Git supplies editions, Chatlas supplies candidate sessions and transcript fragments, and `agentos skw edition-history` is the only persistence boundary.

## Inputs

- require one explicit Bloberia `--depot`; never infer or substitute a global depot
- require one or more target files inside initialized Agentos projects
- work with project-relative file paths when querying Git and Chatlas
- treat the target list as the linter scope; no package-wide completeness claim follows from checking it

## Recovery Workflow

1. Resolve the target's Agentos project root and project-relative path.
2. Enumerate every discoverable edition with rename following:

   ```bash
   git log --follow --format='%H%x09%cI' -- <project-relative-path>
   ```

3. Refresh Chatlas and build a candidate session list from several independent signals. Start with normalized file touches, then broaden through tool input/output containing the path or basename, transcript text, repository attribution, working directory, and the Git edition's time neighborhood. Do not require every signal to agree, and do not exclude umbrella-workspace sessions merely because the file belongs to a nested project.

   ```bash
   agentos chatlas query --file-touched <project-relative-path> --update
   agentos chatlas views inline --tool-contains <path-or-basename> --format json
   agentos chatlas views inline --contains <path-or-basename> --format json
   ```

4. Inspect a focused transcript fragment for every candidate. Broad matching only discovers candidates; it never establishes an association.

   ```bash
   agentos chatlas views inline --identity-hash <chatlas-identity> \
     --tool-contains <path-or-basename> --format json
   agentos chatlas views inline --identity-hash <chatlas-identity> \
     --around <ISO-time> --radius 6 --format json
   ```

5. Associate a session only when the inspected fragment proves that its work contributed to the edition. Temporal proximity helps rank candidates but is never sufficient support by itself.
6. Build one embedded `chatlas.support-set.v1` object from the exact supporting events. Use the neutral Chatlas `identity_hash` as both `--session` and each relevant member's `session`; copy each `event_id` and timestamp exactly. The set must be nonempty and must include the associated session.

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
     --support-file <support-set.json> \
     --depot <depot>
   ```

8. Repeat safely as more Chatlas material becomes available; equivalent record calls are idempotent.
9. Close by reading the grouped history and running the explicit-target linter:

   ```bash
   agentos skw edition-history list --file <file> --depot <depot>
   agentos skw edition-history check --target <file> --depot <depot>
   ```

## Judgment Rules

- seek all editing sessions discoverable for every Git edition, not merely the last editor
- a session association records historical contribution; it does not claim sole authorship or `Touched.Authority`
- use a battery of discovery heuristics because agents may edit through patch tools, shell commands, scripts, or batch operations
- inspect surrounding transcript detail for every candidate and record only exact events that prove contribution
- persist the support consumers need; never persist discovery signals or search mechanics
- preserve Chatlas session start time when available so stored timing can later be reconciled
- if support remains ambiguous, leave the association unrecorded and report the candidate rather than guessing
- never write `skw.edition-session` records directly with `agentos bloberia`; callers consume the Skillware schema through its service

## Completion

Return the target files, editions inspected, associations created versus already present, unresolved candidates, and the final check findings. A clean minimal check means every target has at least one valid association; it does not prove historical completeness.
