# Tarav Capture

Use this module to discuss, approve, and land `User.Touched.Chatlas.Index`
Annotations into a Project's configured main Model.

Read `../CONSTITUTION.md` and `../tarav-diagram.md` before operating this
workflow.

## Authority Boundary

The chat is the WIP capture surface. Do not create a `Capture.Manifest` or
write semantic Diagram Annotations before the user sends `::land` for a
settled proposal. Mechanical Diagram bootstrap and Project-to-Model
association may occur earlier when needed to establish the capture target;
report that setup without treating it as semantic landing.

The user and Agent discuss and approve the semantic capture in chat. The
post-land Manifest is only a faithful mechanical compilation of that approved
material.

## Discussion Phase

1. Resolve the current Agent's native session identity. Prefer the
   `tarav-chatlas-my-session-id` skill when available.
2. Run `tarav chatlas update` for that session so prior chat material is
   available to Chatlas.
3. Inspect the Project's configured Model and recent chat context:

   ```bash
   tarav tarav2 diagram capture context \
     --project \
     --session-id <native-session-id> \
     --provider <provider> \
     --json
   ```

4. If the Project has no main Model, the capture context may mechanically
   bootstrap one in the default `User.Touched.Chatlas.Index` Namespace and
   associate the Project with it. Report that setup. When an existing shared
   Model is an evident candidate, inspect Models and discuss or select that
   association instead of creating an unnecessary duplicate.
5. Propose Blocks and atomic Lines in chat. For each one, make clear whether it
   reuses an existing lineage or creates a new lineage, its wording, and the
   User turns providing meaningful support.
6. Revise until the user has approved every Block and Line intended for the
   batch. Do not treat silence as approval.
7. Present one final settled capture proposal in the Agent turn immediately
   preceding the requested `::land`. This final turn must contain no unapproved
   semantic additions.

End the discussion phase without mutation. Invite `::land` only when the
proposal is settled.

## Landing Phase

Enter this phase only when the user sends `::land` for the settled proposal.
`::land` authorizes materialization; it is not a substitute for the earlier
semantic approvals.

1. Refresh Chatlas. Resolve the final pre-land Agent turn and all approved User
   support turns through `diagram capture context`. The final pre-land Agent
   turn is the Annotation producer.
2. Create the `Capture.Manifest` only now:

   ```bash
   tarav tarav2 diagram capture template \
     --project \
     --manifest <temporary-json-path> \
     --json
   ```

3. Compile exactly the approved Lines and their Block grouping into the
   Manifest. UUIDs, hashes, references, and equivalent bureaucracy may be
   filled mechanically. Do not introduce or reinterpret semantic content.
4. Run mechanical validation:

   ```bash
   tarav tarav2 diagram capture check --manifest <path> --json
   ```

5. Correct mechanical errors. If correction requires a semantic change, stop
   landing, return to discussion, and obtain approval again.
6. Apply the mechanically executable Manifest:

   ```bash
   tarav tarav2 diagram capture apply --manifest <path> --json
   ```

   During development, the Agent may deliberately leave the created
   Annotation files uncommitted without changing the Manifest:

   ```bash
   tarav tarav2 diagram capture apply \
     --manifest <path> \
     --no-commit \
     --json
   ```

   `--no-commit` transfers Git responsibility to the developer. Reapplying the
   same Manifest does not later commit those existing files automatically.

7. Report created and existing Annotation identities plus every POI. POIs do
   not block landing and must not be silently hidden.

The temporary Manifest is not Diagram authority. The Namespace Annotation tape
and its Git history are the materialized result.

## MVP Boundaries

- Interactive capture only; no autonomous capture.
- One Project main Model per invocation, although that Model may be shared by
  many Projects.
- New Block and Line Annotations, and later support-only Annotations.
- No Assertion scoring, Model composition, lineage forks, or automatic POI
  repair in this workflow.
