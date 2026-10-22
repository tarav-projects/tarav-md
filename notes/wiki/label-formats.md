# LabelFormats

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

The User chose `Label` as the shared value for dotted Block labels and paths,
replacing the provisional BlockTitle abstraction. A Label accepts any supported
format; later specializations can restrict formats. They requested a
LabelFormats Workflow and adoption throughout the maintained consumers.
<!-- tarav.breadcrumb ca0e5969f3b5 -->
<!-- tarav.breadcrumb 6734d333838a -->
<!-- tarav.breadcrumb 2bb570af426f -->

## Implemented contract — 951

[Request 951](../../../tarav-py/notes/live/951-label-formats-impl-req.md) introduces
`l0.label_formats.Label`, an immutable string value with strict construction and
Pydantic validation. `DottedFormat` preserves the rule of two or more capitalized
alphanumeric segments; `JSONPointerFormat` accepts RFC 6901 string paths, including
the empty root and ~0/~1 escapes. Neither format rewrites text. The identified
`l1.label_formats.LabelFormatsWorkflow` owns this vocabulary; the value module
has no Kernel dependency.

`LabelLine` carries a Label in its authoring Block; `ReviewedLabel` adds Notebook
support/review obligations. TaravClass names use Label too. PathRegistry uses
the JSON Pointer rule specifically, keeping dotted labels distinct from actual
schema positions. Project scaffolding now derives capitalized label words from
Python identifiers, rather than using raw lowercase package slugs. This machine's
System Project adopted the valid label while keeping its Type and Project UUIDs.

The old BlockTitle and ReviewedBlockTitle Python APIs are removed. Their wire
Record Type names and Ships remain unchanged to preserve exact Git-backed review
history. A live read of both existing reviewed titles found no support or review
problems. This is an implementation preservation choice, not a new naming rule.

The extension reader uses LabelLine for title selection, including searching and
displaying JSON Pointer titles. Extension adoption is
[request 016](../../../vscode-tarav-center/notes/live/016-label-formats-adoption-impl-req.md).
There is no PathSchema viewer or Path Notebook in this implementation.

See the [API guide](../../../tarav-py/src/tarav/l0/label_formats/README.md),
[format tests](../../../tarav-py/tests/test_label_formats.py),
[Notebook tests](../../../tarav-py/tests/test_notebook.py) and
[extension reader tests](../../../vscode-tarav-center/tests/test_notebook.py).

Ordinary UI captions, filesystem names, local SKW slugs and schema-producer keys
remain their own text contracts. Label does not supply identity: Ships do.
