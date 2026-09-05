# Inlined Capture

Load this module for `tarav-hugentics --capture --inline <SURFACE>`.

`Inlined.Capture` is an Agent-operated breadcrumb workflow. Its ordinary route
leaves compact, local references from useful fragments of one
`Product.Surface` to relevant Chatlas `User.Turn`s. Its `--audit` route checks
the references already present without mutation. A later Agent may peek around
resolved Turns and selectively digest them into richer context. The references
are not themselves a digest, Diagram capture, grounding Assertion, approval
claim, or completeness claim.

Read the selected surface's project instructions first. The ordinary invocation
authorizes one bounded edit of that surface. The audit invocation authorizes no
mutation: do not edit the surface, update Chatlas, create Diagram records, or
write a retained report. The first normative embedding specialization is
Markdown. An Agent may audit another readable surface through its explicit
native convention; when no convention is established, report that limitation
instead of guessing.

## Routes

### Capture

```text
tarav-hugentics --capture --inline <SURFACE>
```

Discover relevant User Turns and insert references according to the selected
surface convention.

### Audit

```text
tarav-hugentics --capture --inline --audit <SURFACE>
```

Inventory and assess existing references in exactly one surface. Audit is
read-only and stops after reporting its findings. It does not assess whether
the surface has complete conversational coverage.

## Markdown contract

Declare relevant sessions once near the top of the document:

```md
<!-- tarav.sessions
phd = codex:01a06bed-b554-7770-86e3-cce2e5729994
-->
```

The left side is a document-local alias. The right side is
`<provider>:<native-session-id>`. Reuse an existing declaration when it names
the intended session. Do not silently rebind an alias in the current surface;
choose another clear alias when a conflict is visible. Do not consult Git or a
separate registry by default.

Attach references immediately after the Markdown block they contextualize:

```md
The theoretical front is established for the scope of the PhD.
<!-- tarav.context phd:dd358589d092f9dd -->
```

Consecutive references attach to that same preceding block. Preserve ordinary
Markdown as the authoritative surface.

## Capture workflow

1. Read the selected Markdown surface and its current session declarations.
2. When the current chat is in scope, resolve and refresh it once through
   `tarav-chatlas-my-session-id`. Reuse its returned provider and native
   session ID; do not perform another update.
3. Discover candidate User Turns from each exact session with the compact
   timestamped ledger when their hashes are not already known:

   ```bash
   tarav chatlas render \
     --provider <provider> \
     --session-id <native-session-id> \
     --side user \
     --order newest \
     --limit 50 \
     --renderer Chatlas.Turn.Ledger.Renderer
   ```

   The ledger aids navigation; the Agent still decides semantic relevance.
4. Group selected Turns by declared session. Resolve each ordered group through
   the shared Chatlas Query engine; Renderers never perform selection.
5. Render each group with the named Markdown reference Renderer:

   ```bash
   tarav chatlas render \
     --provider <provider> \
     --session-id <native-session-id> \
     --turn-hash-prefix <prefix> \
     [--turn-hash-prefix <prefix> ...] \
     --renderer Inlined.Capture.Markdown.Reference.Renderer \
     --renderer-option session-alias=<alias>
   ```

6. Insert the rendered comments after their selected Markdown blocks. Several
   comments may be distributed across the document; a Renderer batch need not
   be inserted as one contiguous group.
7. Re-read the edited surface and report the added references plus unresolved
   POIs.

Use 16 hexadecimal characters as the ordinary prefix length. Resolution is
bounded by the declared session, so collisions are uncommon. If a prefix is
ambiguous, inspect only its matched candidates and lengthen that reference. If
it is missing, report a nonblocking POI rather than guessing.

This workflow uses Chatlas Query for exact resolution and a Renderer for
surface syntax. It adds no alias registry, automatic Git-history audit,
Diagram record, Assertion score, or generalized impact map. Those may be
separate later workflows when the breadcrumbs are worth digesting.

## Audit contract

The generic audit protocol asks the same bounded questions for any supported
surface while leaving syntax recognition to that surface's convention:

1. Which context sources or sessions are declared?
2. Which embedded references occur, and where?
3. Does every reference name one declared source and resolve to exactly one
   intended target?
4. Is the reference's local attachment structurally plausible?
5. Which conditions need Agent or User attention?

Mechanical resolution does not establish semantic relevance, correctness,
authorship, approval, completeness, or exclusive support. Attachment judgment
remains Agent work.

## Audit workflow

1. Read the selected surface, its project instructions, and its native
   embedding convention. Do not enter the ordinary capture workflow.
2. Use surface-native inspection. `tarav surfaces normalize --file <surface>
   --json` may provide syntax facts and source spans for supported languages;
   it does not know Inlined.Capture policy. Use ordinary Agent tools when that
   model is unnecessary or insufficient.
3. Inventory declarations and embedded references with their local source
   locations. Ignore literal examples that the native convention does not make
   active, such as Markdown comments shown inside fenced code.
4. Check declaration and reference syntax, alias binding, and the surface's
   ordinary prefix convention. Continue past recoverable problems so one audit
   exposes the whole bounded surface.
5. Group resolvable references by their declared exact session. Query each
   group in reference order through `tarav chatlas query` or `render`, without
   `--update` or `--refresh`. Confirm each prefix resolves once and the result
   is a User Turn.
6. Inspect local attachment according to the native convention. For Markdown,
   a reference attaches to the immediately preceding Markdown block and
   consecutive references attach to that same block. Report orphaned or
   suspicious attachments; do not repair them.
7. Return one compact in-chat report and stop. Include the surface,
   specialization used, declaration count, reference count, exact-resolution
   count, and POIs with useful source locations.

For Markdown, recognize the declaration and reference forms specified above.
The ordinary prefix is 16 lowercase hexadecimal characters. A nonstandard
prefix is a convention POI but may still be resolved when Chatlas accepts it.
Report at least these conditions when present:

- malformed or conflicting session declarations;
- malformed references or references to undeclared aliases;
- unavailable declared sessions;
- zero or multiple Turn-prefix matches;
- references resolving to an Agent rather than a User Turn;
- references placed inside inactive syntax, without a preceding block, or
  attached to a block whose relevance is doubtful.

An unavailable target is a POI, not permission to update provider data or
guess a replacement. A semantically questionable attachment is likewise a POI,
not a verdict that the surface is wrong.
