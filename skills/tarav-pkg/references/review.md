# Tarav Diagram Review

Use this module to review existing `User.Touched.Chatlas.Index` Block Lines
without modifying their original Annotation records.

Read `../CONSTITUTION.md` and `../tarav-diagram.md` before operating this
workflow.

## Review Phase

1. Render the target Block and inspect its exact Line wording:

   ```bash
   tarav tarav2 diagram render \
     --block-ship <uuid> \
     --renderer Kernel.Writing.Block.WithSupport
   ```

2. Mint one opaque token. Present the exact Lines being reviewed and the
   copyable command `::approve <token>` in the same Agent turn.
3. The User may discuss or request changes. Changed wording requires a fresh
   token and a new final proposal.
4. The Gate exchange exists only when a later User turn contains the exact
   approval command. The proposal and approval turns are Gate evidence, not
   automatic members of the Lines' substantive `Support.Set`s.
5. Settle the review batch and obtain `::land` before writing Diagram records.

## Landing Phase

Refresh Chatlas and resolve the exact proposal and approval Turn references.
Then compile one ordinary post-land `Capture.Manifest` for the complete Block.
The Manifest contains one typed record per reviewed Line wording:

```json
{
  "id": "<new-annotation-uuid>",
  "type": "Diagram.Line.Gate.Annotation",
  "target_annotation": "<existing-line-annotation-uuid>",
  "gates": [{
    "type": "Verbatim.Gate",
    "token": "<opaque-token>",
    "proposal_turn": {
      "session_identity": "<sha256>",
      "turn_address": "<sha256>",
      "turn_hash": "<sha256>"
    },
    "approval_turn": {
      "session_identity": "<sha256>",
      "turn_address": "<sha256>",
      "turn_hash": "<sha256>"
    }
  }]
}
```

This is not a special Review Manifest. It is an ordinary Capture Manifest
whose Annotation `type` selects Gate behavior inside the Tarav library. The
Capture engine does not know what a Gate is and does not modify the reviewed
Lines.

Check and apply through the ordinary writable Capture pipeline:

```bash
tarav tarav2 diagram capture check --manifest <path> --json
tarav tarav2 diagram capture apply --manifest <path> --json
```

Finally, render the Block again. The Renderer recomputes Line review standing
from retained Chatlas evidence:

```bash
tarav tarav2 diagram render \
  --block-ship <uuid> \
  --renderer Kernel.Writing.Block.WithSupport
```

A passing Gate makes its Line ship reviewed. Missing wording, token, role,
ordering, or evidence produces POIs without deleting the record or blocking
future work.
