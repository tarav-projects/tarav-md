# LineMarkdown floor

<!-- tarav.sessions
5a029cbf = claude-code:8c55cc60-f28a-439f-a6a0-0521567e600e @5a029cbf49a299c9709013b8ccb3fc517b2fb56fed373d3da819b6ea842afa2f
-->

## A minimal base meant to be extended

Tarav's Markdown parser is deliberately minimal because it is the base that
other parsers build on; how much Markdown a consumer needs cannot be known in
advance. Consumers extend it for their needs, and Tarav is changed when it does
not support that extension.
<!-- tarav.breadcrumb 6fe06e96a65faef5f2046dcc8dce2534244b7477f8e2d62f7607510681cbe492 -->

Higher-level parsers parse the lower-level model, not the original text: the
base model is the file's representation for every layer above it.
<!-- tarav.breadcrumb d093f66993b21c08cc91bb2ee833f6305032d3ca940e5f5ca5fa372e33108b23 -->

## A strict line dialect

For formats a project owns, the base can be a line parser, named as such:
block delimiters never share a line with content. A single-line `$$ … $$`
equation is not allowed; there is one way to write an equation block. The
restriction is the point, because a restricted dialect is easier to build on.
<!-- tarav.breadcrumb 82fcf6e84ff25fbc46c77d58a9c83fba950d0a208c558896566cae19fa1b3d71 -->

Such a parser is a floor linter: its violations are minimal ground truth and
are not blessable, while heuristic layers above it may favour recall and accept
false positives that agents judge.
<!-- tarav.breadcrumb 55a6bde19df9bd6dbd77e0aebebd83349c1b1cf9eb9cbdb1b9e5e6d22a81cd17 -->

It stops at the first violation, like a compiler. Once a delimiter is wrong,
fencing is no longer trusted, so later structure cannot be checked reliably.
<!-- tarav.breadcrumb 2c6e0d30c13c471faf9c0108e65593381ac604a8c23a5b855c8ee55ecfa24468 -->

It is an additional parser, so the lenient one and its current users are left
undisturbed.
<!-- tarav.breadcrumb 5b00f3fdd26c3cb29dbe33b95c0088fc9c8b36a6e63368941d56fb1f4e8aaae7 -->

## Implementation — 840

`LineMarkdownModel` in `tarav-py/src/tarav/l1/surfaces/markdown/line.py` is a
`MarkdownNormalModel` subtype with `math_blocks`. `from_text` raises
`LineMarkdownViolation` (rule, message, span) for `LineMarkdown.Math.NotAlone`,
`LineMarkdown.Math.Unclosed`, `LineMarkdown.Fence.InlineClose` and
`LineMarkdown.Fence.Unclosed`. Headings inside fences or math blocks are not
headings. The lenient parser and its Wiki, Breadcrumb, `mdblocks` and Chatlas
consumers are unchanged. The first consumer is md-library's transcript Checks
(md-library-py 582). See
[840](../../../tarav-py/notes/live/840-line-markdown-floor-parser-impl-req.md).
