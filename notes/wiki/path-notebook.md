# Path Notebook

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

The User proposed a simple typed Notebook whose Blocks reference registered
paths. They clarified that schemas also have Ships and can have notes: a Line
at a subpath is interpreted with all parent notes, through the schema, using
the ordinary Notebook ancestry rule.
<!-- tarav.breadcrumb 4036cdd6b4c6 -->
<!-- tarav.breadcrumb 9fc36f1d200e -->

## Implementation — 953

[Request 953](../../../tarav-py/notes/live/953-path-notebook-impl-req.md) implements
PathNotebook inside the existing Project Notebook. `project.notebook().paths`
and `project.paths.notebook()` select the same child without writing. Explicit
Project Notebook creation adds that child to an existing edited layout while
retaining its previous Lines, Blocks and identity.

The data is ordinary Notebook data:

- PathNotebook references its registry Ship.
- SchemaBlock references a registered View's Ship and holds general schema notes.
- PathBlock references a Path Ship. Its Lines inherit context from the schema,
  empty root position and intervening path Blocks.

Adding a path note materializes only its required registered ancestor chain in
memory. Save persists it. Pointer tokens remain escaped: `/a~1b` is one segment,
not two. Missing/ambiguous/retired registry links report a problem. An unchanged
Path Ship keeps its note after a same-parent rename; a changed parent reports
ancestry drift for explicit maintenance instead of silently moving text. Ordinary
stored notes remain readable as historical context.

The [API guide](../../../tarav-py/src/tarav/l1/notebook/PATHS.md),
[link Types](../../../tarav-py/src/tarav/l1/notebook/paths.py),
[Notebook integration](../../../tarav-py/src/tarav/l2/notebook.py) and
[behavior tests](../../../tarav-py/tests/test_path_notebook.py) show the exact
contract. PathRegistry still holds no documentation or attachment list. Existing
capture/support/review operations retain their policies; no new evidence policy
is imposed on plain note Lines.

The stored Tarav Project Notebook now contains an empty Path Notebook child.
Adoption changed only its membership Record and added that child; the other
2,165 existing Records were unchanged. The parent Project Notebook Ship is
`f6c673d6-88e7-5071-8533-ab0a6450c6e6`; its Path Notebook is
`aab88039-65ca-5411-8f8f-372111a384f8`.

See [PathRegistry](path-registry.md), [LabelFormats](label-formats.md) and
[Line Notebook](line-notebook.md). The PathSchema extension viewer is separate.
