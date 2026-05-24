# File.Numbering.Protocol Appendix

****

## File.Numbering.Protocol/Design.Rationale

`File.Numbering.Protocol` gives agents and humans stable handles for markdown and live working surfaces.

The number is the durable handle. The filename title can improve as understanding improves, but the prefix should remain stable so citations, references, and handoffs keep working.

Gaps are expected. Allocation is append-only because preserving address stability matters more than making a directory visually contiguous.

****

## File.Numbering.Protocol/Range.Model

Current Agentos package guidance uses these ranges:

- `000-099`: reserved fixed-role files
- `100-299`: public package index flat files
- `300-499`: local project index flat files
- `500-999`: rolling working files, including `Agentos.Live.Note` and `Agentos.Live.Script`

Reserved examples:

- `000-index.md`: public `Index.Router`
- `001-index.md`: local `Index.Router`
- `010.TODOS.md`: reserved live TODO parking
- `011.ISSUES.md`: reserved live issue parking

****

## File.Numbering.Protocol/Placement

The index block should hold compact semantics. This appendix holds rationale and range shape. The operational command recipe belongs in `references/file-numbering-protocol.md`.

Domain-specific surfaces can specialize the protocol by naming their target path, filename pattern, allocation range, and uniqueness scope.

****

## File.Numbering.Protocol/Future.Checks

The desired diagnostics are project-wide duplicate detection, range validation, reserved-prefix drift detection, and append-only enforcement.
