# agentos-skillware --dev (edition-history developer)

Use this module when the caller wants to recover, record, inspect, or lint the chat sessions associated with a managed file's Git editions.

`Skw.Edition.History.Service` is deterministic; this module performs the agentic discovery and evidence judgment around it. Git supplies editions, Chatlas supplies candidate sessions and edit evidence, and `agentos skw edition-history` is the only persistence boundary.

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

3. Refresh and query Chatlas for sessions carrying actual file-touch evidence:

   ```bash
   agentos chatlas query --project <project-root> \
     --file-touched <project-relative-path> --update
   ```

4. Inspect each candidate at the touching events:

   ```bash
   agentos chatlas views inline --session-id <session-id> \
     --file-touched <project-relative-path> --format json
   ```

5. Associate a session only when the touching events and surrounding work plausibly contributed to the edition. Temporal proximity helps rank candidates but is never sufficient evidence by itself.
6. Record every accepted association through the service:

   ```bash
   agentos skw edition-history record \
     --file <file> --commit <commit> --session <session-id> \
     --session-started-at <ISO-time> \
     --evidence-json '{"method":"chatlas-file-touch"}' \
     --depot <depot>
   ```

7. Repeat safely as more Chatlas material becomes available; equivalent record calls are idempotent.
8. Close by reading the grouped history and running the explicit-target linter:

   ```bash
   agentos skw edition-history list --file <file> --depot <depot>
   agentos skw edition-history check --target <file> --depot <depot>
   ```

## Judgment Rules

- seek all editing sessions discoverable for every Git edition, not merely the last editor
- a session association records historical contribution; it does not claim sole authorship or `Touched.Authority`
- prefer file-write evidence over file-read evidence; use surrounding turns to distinguish an edit from inspection
- preserve Chatlas session start time when available so stored timing can later be reconciled
- if evidence remains ambiguous, leave the association unrecorded and report the candidate rather than guessing
- never write `skw.edition-session` records directly with `agentos bloberia`; callers consume the Skillware schema through its service

## Completion

Return the target files, editions inspected, associations created versus already present, unresolved candidates, and the final check findings. A clean minimal check means every target has at least one valid association; it does not prove historical completeness.
