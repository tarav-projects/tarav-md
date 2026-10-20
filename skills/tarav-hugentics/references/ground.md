# Notebook grounding

```text
tarav-hugentics --ground --notebook [HINT]
tarav-hugentics --ground [HINT]
```

Ground the agent in Blocks relevant to the current conversation. HINT focuses
that work; it need not be an exact name, and it does not replace the visible
conversation. Bare --ground selects the Notebook backend. These are skill
selectors, not flags to forward to the CLI.

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

The default source is the inferred Project's complete ModelBlock subtree,
which aims to express its current model of the system. The Context graph
collects every Block and Line in that subtree plus ancestor context; collection
does not mean that the agent has read or endorsed every Line.
<!-- tarav.breadcrumb fd9154f58117 -->
<!-- tarav.breadcrumb 208c1dc24ee4 -->

## Resolve and inspect

1. Identify the conversation's current concepts, claims, tensions and questions.
   Use the hint to focus that frame. If no conversation is available, say that
   the pass is grounded only in the supplied hint.
2. Infer the active Project from the foreground task, explicit Project mentions,
   and working directory. The skill's own repository is not automatically the
   target. Resolve materially ambiguous Projects with the User.
3. Discover the installed command with `tarav notebook --help` and its relevant
   subcommand help. Start with:

   ```sh
   tarav notebook ls --project /absolute/project/path --json
   ```

   Without --project the command infers the nearest Project from cwd. It runs
   through that Project's declared harness, preserving its actual Type. `ls`
   returns scope identity, graph size, the Lines IRI prefix, and a compact map
   of all Blocks in the selected subtree. Previews come from direct Lines;
   there is no mandatory Block name or topic field.
4. Inspect this map before deciding whether a query is useful. Types, Line
   wording and ancestry provide relevance clues. For a small model, reading
   the relevant Blocks directly may be cheaper than preparing a query.

## Query and read

Lines contribute facts through Context hooks. Query execution is the existing
Context Explorer's SPARQL SELECT/ASK engine; Notebook supplies persisted
objects. There is no separate Notebook search language or text-search index.
<!-- tarav.breadcrumb c486d0fdefcb -->

The prefix is `lines: <urn:tarav:lines:>`:

- `lines:text`: Line to literal text;
- `lines:scope`: Line to its one authoring Block;
- `lines:parent`: Block to its parent;
- `lines:contains`: Block to a direct Line or child Block;
- RDF `_1`, `_2`, ... membership predicates retain mixed content order;
- inherited `rdf:type` identifies the concrete Type.

Derive concrete search terms and relationships from the conversation. For
example, replace MODEL_SHIP with the `scope.id` returned by `ls`, and replace
"cache" with a useful term before running:

```sh
tarav notebook query --project /absolute/project/path --sparql '
PREFIX lines: <urn:tarav:lines:>
SELECT ?block ?line ?text WHERE {
  ?line lines:scope ?block; lines:text ?text .
  ?block lines:parent* <urn:uuid:MODEL_SHIP> .
  FILTER(CONTAINS(LCASE(STR(?text)), "cache"))
} LIMIT 20' --json
```

The parent path confines this example to the selected subtree: ancestor Lines
are available as context, but their presence does not make them model content.
Search terms produce leads. The agent judges relevance by reading the Blocks.
Every invocation collects a fresh graph; there is no retained session View.

```sh
tarav notebook read --project /absolute/project/path --id BLOCK_OR_LINE_SHIP --json
```

A read returns the owning Block, ordered direct contents and ancestor direct
Lines. Read relevant child Blocks explicitly and preserve each Line's scope.
Do not interpret a Line through arbitrary additional graph relationships.
Object values in query rows carry Ships and Types; use those identities for
further reads and citations. Known stored identities also open through
`tarav context --id SHIP` in an environment that knows their Types.

## Scope and conclusion

Start at Model by default. When the User requests Discussion or Archive, or
when the task justifies deliberate additional context, select it explicitly:
`--branch discussion`, `--branch archive`, or `--branch project` on the same
commands. State the expansion. `--block SHIP` selects a particular subtree
under this Project; it is mutually exclusive with --branch. Retain discussion
and historical context when using those branches; inclusion does not make
material current or an implementation commitment.

Return a compact continuation-oriented explanation: the relevant Blocks and
Ships, what their Lines contribute to this conversation, material tensions or
missing coverage, and whether further reading is needed. Separate retrieved
material from agent inference. A match is not proof of truth or approval.

Grounding is read-only. It creates no Notebook, Project state, captured Lines,
Breadcrumbs, actions or session repository. Report missing storage, missing
Model, empty or sparse coverage, unresolved identities and query errors
honestly; do not populate the model or silently search every Project. It does
not compose with mutating Hugentics routes. The retired Diagram Model-backed
capture/implementation routes remain parked; Notebook ModelBlock is distinct.
<!-- tarav.breadcrumb ccfc10f461df -->

