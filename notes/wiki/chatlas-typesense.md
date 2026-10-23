# Chatlas Typesense search

<!-- tarav.sessions
0d8af26c = codex:01a168fe-92d6-7410-a7f7-7c15cf921b95 @0d8af26c5b8dff7be764aac420b13df80bb530919d551881ae7d1afcc2400744
-->

## Consume a search product

The User wants a full-featured search product that owns embedding generation,
indexing and retrieval. Tarav supplies a small Chatlas adapter, exposing text,
available speaker/date/provider information and exact references to original
Chatlas material. Training a model was exploratory and is outside this first
deployment. Typesense is the selected initial product, installed only on the
Studio. Tarav code is developed here, pushed to GitHub, then pulled there.
<!-- tarav.breadcrumb 5e15d08c46cd -->

The interface is `tarav chatlas typesense ...`, intended for agents to call
directly. The global CLI router routes that command family to the Studio. The
Typesense command itself knows nothing about the Studio or SSH: it uses the
endpoint and data paths on whichever machine executes it.
<!-- tarav.breadcrumb ca8b335b3f65 -->
<!-- tarav.breadcrumb fd95bbdfc3ca -->

Search begins only with existing Normal Model files. Raw transcripts, provider
capture and regeneration from raw are outside this adapter's input contract.
<!-- tarav.breadcrumb c947c52484a4 -->

## Implemented consumer

The Python integration lives in `tarav.l2.chatlas_typesense`, composed into the
CLI through an injected Chatlas command registrar. `status` inspects service/data
availability; `sync` projects stored Messages into text chunks and imports them;
`search` delegates hybrid matching to Typesense and returns exact source selectors.
Typesense's documented built-in embedding preset handles inference. There is no
embedding service or training loop implemented by Tarav.

The consumer reads main.json, messages.jsonl, turns.jsonl and events.jsonl through
the public Normal Model DirectoryRecord. Each chunk retains exact text offsets,
Message/Event/Turn references, provider/session identity and stored time. The
current header has no project information, so the first interface has no project
filter. Chunking and a replaceable sync checkpoint are implementation choices;
neither changes the source Model nor makes the search index authoritative.

Sources: [adapter guide](../../../tarav-py/src/tarav/l2/chatlas_typesense/README.md),
[Python implementation request 957](../../../tarav-py/notes/live/957-chatlas-typesense-normal-model-search-impl-req.md),
and [HTTP contract tests](../../../tarav-py/tests/chatlas_typesense/test_typesense.py).
The initial 15 integration tests passed, followed by 103 broader routing,
Chatlas and architecture tests. Those are protocol/adapter checks; a live
Typesense engine and real retrieval relevance have not yet been tested.

## Deployment standing

The existing Git-only Chatlas transfer will not supply these inputs:
normal-model/ is ignored and has zero tracked files. Deployment therefore needs
an explicit copy of stored Normal Model files, preserving the User's original
Git-depot transfer test. The adapter never fills that gap by reading raw chats.

Tankefac's maintained Ansible guidance requires the operator to run machine
check/apply. The prepared deployment declares a pinned ARM64 Typesense daemon as
services, a personal Tarav client from GitHub, private API credentials, loopback
HTTP, Normal Model-only transfer and a first-session import check. Source and
commands are retained in the Ansible repository's
[deployment guide](/Users/pereiro/projects/tankefactory-projects/tankefac-ansible/notes/typesense-deployment.md).
Actual installation, live ingestion/relevance checks and enabling the local
router remain pending the operator run. Nothing installs Typesense on the Mac Pro.

## Required proof of concept

The User requires following deployment through a live test that finds the first
chats discussing Kernel.Writing. The request stays open until the actual service
indexes the stored Normal Models, returns dated early conversations and those
Message/Turn references are checked against the source files. Local fixtures or
a reference scan are supporting checks, not substitutes for this result.
<!-- tarav.breadcrumb 577bd2bfa715 -->

The interface now supports `search --order oldest|newest|relevance`. The live POC
must review topic relevance and spelling variants, group repeated chunks by
conversation, and make approximate-search and coverage limits explicit.
