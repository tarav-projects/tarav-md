# Notebook capture

```text
tarav-hugentics --capture --notebook [FOCUS]
    [--project PATH] [--branch model|discussion|archive|project | --block SHIP]
tarav-hugentics --capture --notebook --audit [FOCUS]
tarav-hugentics --capture --notebook --unreviewed [FOCUS]
tarav-hugentics --capture --notebook --auto [FOCUS]
```

Capture the current conversation into recursive Notebook Blocks and Lines.
Default to interactive reviewed capture in the inferred Project's ModelBlock.
Project and subtree selectors are skill arguments; pass their resolved values
to the corresponding Notebook navigation commands. They are not filesystem
folders to create. --branch and --block are mutually exclusive. Select one
capture backend: Notebook, Wiki or inline; do not combine them implicitly.
<!-- tarav.breadcrumb c49d456f1041 -->

Read [Kernel Writing](kernel-writing.md) before proposing wording. Use
[Notebook grounding](ground.md) for navigation guidance and read-only Context
commands during preparation; this does not select a second --ground workflow.
For writes, follow [commit evidence](commit-evidence.md) for each mutated Git
repository, with exact declared file scopes. Keep proposal plans outside the
live Notebook store. This is an Agent-operated skill over Python APIs, not a
command that invokes an agent or an independent capture database.


## Prepare the target

Infer the Project from the foreground work, explicit mentions and cwd. The
skill repository is not automatically the target. Resolve material ambiguity
with the User. Resolve the Project through its own harness when running Python.
Use `tarav notebook --help` and relevant subcommand help, then map the complete
selected subtree:

```sh
tarav notebook ls --project /absolute/project/path --json
tarav notebook read --project /absolute/project/path --id BLOCK_OR_LINE_SHIP --json
```

The default branch is Model; explicitly pass --branch or --block for another
scope. Read useful Blocks and ancestor direct Lines before proposing edits.
For a small Model, read its content directly. Use Context's existing SPARQL
queries for further discovery; do not build another Notebook search system.
Compare the conversation with existing content: additions, amendments, overlap,
contradictions and questions. Keep the evidence inventory internal unless a
gap changes the User's decision. Support links do not establish agreement.
<!-- tarav.breadcrumb e7e779097631 -->

An explicit mutating capture invocation can initialize a missing Notebook
through `project.notebook().create()`. Report the seeded root and read its
layout. This creates its standard explanatory context, not proposed design.
Missing branches or unresolved Block identities require a concrete destination;
do not guess one. Audit leaves missing storage absent.

Resolve the current provider/native session with `tarav chatlas current-session`
and obtain its neutral identity through the Normal Model. Refresh that exact
session once at each evidence checkpoint, using `tarav chatlas update`; reuse
the result within that checkpoint. A later User approval or landing command is
a new checkpoint containing new messages, so ingest it before resolving its
references. Do not poll or reconstruct the transcript instead of using the
visible discussion. Discover exact CLI options through subcommand help.


## Discuss, review and change focus

Present a compact roadmap of coherent capture candidates and recommend one
first focus. A roadmap is orientation, not an approval-ready proposal. Work on
one Block or small related change at a time. Reuse existing Ships when a Line
continues the same semantic identity; new meaning may need a new Line.

Keep focus independent of mode:

- **Discuss:** open conversation about the design or current proposal.
  `::discuss` holds this mode until `::review`; status requests and interruptions
  do not resume proposals. Preserve existing drafts and approved items.
- **Review:** present the exact staged wording, destination, operation and
  Types, with Before/After for amendments and a fresh opaque token. Present the
  output of `draft.propose(token)` intact; a useful human heading or explanation
  may surround it. Do not replace it with a summary or a hand-edited rendering.
- **Approve:** the User replies `::approve TOKEN`. Approval covers precisely
  that proposal and creates no live Notebook records. Bare approval, a general
  positive remark or unrelated authorization is not token evidence.
- **Next focus:** keep approved items pending and continue with another Block.
  Return to discussion whenever requested. Only advertise commands available
  for the current mode and foreground proposal.
<!-- tarav.breadcrumb 911dcef79245 -->
<!-- tarav.breadcrumb f00ff39cf69e -->

Changing wording, Type, target, operation or semantic context requires a fresh
token and a newly presented proposal. Presentation-only wrapping outside the
returned payload may keep the token. An amendment retains its Ship and concrete
Type. Plain archive Lines have no evidence attachments; cite them as historical
context for a new supported capture rather than silently migrating their Type.
<!-- tarav.breadcrumb 5f296af589e5 -->


## Stage with the Notebook API

Run Python through `tarav run --project /absolute/project/path -- script.py`.
The script selects the actual Project and initializes runtime registration.
For the default destination:

```python
import json
import secrets
import tempfile
from pathlib import Path
from tarav.l2.project import Project
from tarav.l3.runtime import get_runtime

get_runtime()
project = Project.from_path(Path(project_path))
book = project.notebook().create()
draft = book.draft(block=book.model)
block = draft.add_block()
line = draft.add("The agreed design statement.", block=block)
# For an existing Notebook Line, use draft.amend(existing_ship, exact_wording).
token = "notebook:" + secrets.token_hex(8)
presentation = draft.propose(token)
plan_path = Path(tempfile.mkdtemp(prefix="tarav-capture-")) / "proposal.json"
plan_path.write_text(json.dumps(draft.export(), indent=2), encoding="utf-8")
print(presentation)
```

project_path and the proposed wording are real task inputs, not literal example
values. Resolve an explicit branch/Block to its stored object and pass it as
block instead of book.model. Draft construction, new Blocks, Lines, proposal
rendering and plan export do not persist candidate content. New Lines are
ReviewedLine by default. Keep each plan path and its actual token associated
with the foreground proposal; never regenerate its random Ships on resume.
The temporary plan is transport, not source authority or approval evidence.
<!-- tarav.breadcrumb 60862fbc4489 -->


## Land approved content and inspect

Wait for `::land` for one unambiguous foreground approved proposal or
`::land-all-approved` for the approved cluster. These commands do not supply
missing token approval. Resolve proposal, approval and substantive support
Turns from Chatlas; retain full session identity, Turn address and Turn hash in
ChatlasTurnReference objects. Inspect the actual selected Turns rather than
guessing hashes, roles, order or support. A token-only approval is review
evidence, not substantive design support. The producer is a real Agent turn;
each conversational support root must precede it.

Restore and land one plan:

```python
from tarav.l1.grounding import SupportMember
from tarav.l2.notebook_draft import NotebookDraft

book = project.notebook()
draft = NotebookDraft.restore(book, json.loads(plan_path.read_text()))
review = draft.land(
    proposal=proposal_turn_ref, approval=approval_turn_ref,
    producer=producer_turn_ref,
    support={line_ship: [SupportMember(user_turn_ref, neighborhood=neighbor_refs)]},
)
```

The Reference objects, line_ship, neighbor_refs and plan_path are actual retained
inputs from this capture. Support maps every new/amended Line to its own
substantive evidence. One SupportMember supplies one root plus optional
neighborhood per SupportSet; additional members in the input list create
independent sets. Do not manufacture future approval references. Base capture
and validation remain separate: missing/invalid support can be retained and
reported, but cannot be reported as grounded or scored.

Landing revalidates source/context, Type, placement and exact proposal evidence
before writing. It preserves prior evidence on amendments and uses current
support/review records. Reload affected Blocks and use `book.inspect(line)`;
run the Project's checks/status as appropriate and report remaining findings.
Semantic support judgments and scores are not implemented by this skill.

Independent child-Block additions can land in sequence without overwriting one
another. A changed authoring context requires a fresh draft and token; approval
of the old context is not transferred. For a cluster, apply approved plans in
order and keep unresolved plans pending. The batch is not an atomic transaction.
If an IO failure interrupts writes, inspect records and evidence before retrying;
report partial effects and never invent a successful landing or roll back
User-touched data merely to hide a finding. Report affected Ships and evidence
standing compactly; do not re-dump settled wording.
<!-- tarav.breadcrumb 1124a502eb0b -->


## Audit and unreviewed capture

--audit reads existing content, maps candidates and reports a small roadmap,
then stops. It does not initialize storage, stage proposals, advertise approval
or landing commands, refresh Chatlas, create evidence, write or commit.

--auto and --unreviewed are equivalent one-trigger capture routes. Infer and
read the same target; use Kernel Writing and User-rooted support. Settle one
bounded pass internally and write through the existing `Notebook.capture`
and `Notebook.support` APIs with reviewed=False. For an existing Notebook Line,
save its intended wording before attaching fresh support. Preserve concrete
Types and earlier evidence. Do not ask for token approval or a separate landing
command, and never attach fabricated review evidence or mark the result
reviewed. Existing review requirements still apply and may produce findings;
report them without weakening the Types. Explicit edit protections remain in
force. If the User redirects into discussion or review, stop autonomous landing
and follow that interaction instead.

This module uses current Lines/Notebook, Context, Grounding, Review and Chatlas
APIs. It does not execute retired Diagram commands, restore the old Index,
add LineTrace/lineage, drive the extension, or capture implementation details
without substantive conversational support.

