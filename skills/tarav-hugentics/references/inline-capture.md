# Inlined Capture

Load this module for `tarav-hugentics --capture --inline <SURFACE>`.

`Inlined.Capture` is an Agent-operated breadcrumb workflow. It leaves compact,
local references from useful fragments of one `Product.Surface` to relevant
Chatlas `User.Turn`s. A later Agent may peek around those Turns and selectively
digest them into richer context. The references are not themselves a digest,
Diagram capture, grounding Assertion, approval claim, or completeness claim.

The User invocation authorizes one bounded edit of the selected surface. Read
the surface's project instructions before editing. The first implemented
surface specialization is Markdown; for another surface type, report that its
embedding convention is not implemented and leave the file unchanged.

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

## Workflow

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
