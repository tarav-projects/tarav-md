****

## Issue.I0001.Tournament.Definition.Import.Closure

- [PR] decide whether a `Tournament.Definition` snapshot must cover its import closure or only the definition file itself ^c20260806-38u
- [CT] the per-tournament snapshot freezes the definition file; nothing freezes the modules that file imports ^c20260806-39u
- [CT] pairing strategies living in an importable library make the gap load-bearing rather than theoretical ^c20260806-40u
- [PR] a library upgrade mid-tournament can change how a running tournament samples, which is the incomparability snapshotting exists to prevent ^c20260806-41u
- [CT] v1 ships without covering the import closure, which defers the question rather than answering it ^c20260806-45u

****

## Issue.I0002.Review.Evidence.Block.Binding

- [CT] `LineRecord` review evidence currently verifies isolated line wording without binding approval to the enclosing block address or current `Line.Scope`. ^c20260821-11u
- [PR] decide whether reviewed-edition identity should cover block address, `Line.Type`, body, label, and scope, or one block-edition manifest over its ordered current records. ^c20260821-12u
- [CT] defer this correction while typed block selection and `Index.Review.Policy` are designed; block-level review must not be treated as mechanically complete until it closes. ^c20260821-13u
