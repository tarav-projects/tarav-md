****

## POI.Linter/Agendix

- [DC] dependency-sync POIs come in two kinds: undeclared dependency (mention without declaration) and unhonored dependency (declaration without mention), each suppressible by blessing until the situation changes ^c20260716-12u ^c20260716-13u
- [CT] only backticked `Dotted.Notation` mentions are visible to the check — prose paraphrases stay outside the fence, same deal as the `Line.Type` fence ^c20260716-12u
- [DC] first activation on an existing surface floods undeclared-dependency POIs; the baseline is a ratchet-style bulk bless, and new mentions after the baseline still flag ^c20260716-12u

****

## POI.Linter/Agendix/Candidate.POI.Catalog

- [DF] a `POI.Catalog` is a `Skw.Kernel.Index` application that registers `POI.Class` blocks ^c20260724-18u
- [DC] `POI.Class` blocks live in a dedicated `poi` chapter ^c20260724-18u
- [CT] every registered `POI.Class` is routed and machine-addressable ^c20260724-18u
- [CT] each class points to its required documentation through `Skw.Address.Schema` ^c20260724-18u
- [PR] linters, blessing machinery, and gates consume the same catalog ^c20260724-18u
- [RJ] a `POI.Catalog` contains class declarations, not `POI.Instance` occurrences ^c20260724-18u
- [RJ] the catalog routes documentation but does not replace it ^c20260724-18u

****

## POI.Linter/Agendix/Candidate.POI.Documentation

- [DF] `POI.Documentation` is the set of Skw-addressable surfaces that define a `POI.Class` and how its instances should be evaluated ^c20260724-20u
- [CT] each `POI.Class` points from the `POI.Catalog` to one or more documentation entrypoints through `Skw.Address.Schema` ^c20260724-20u
- [CT] documentation may span several surfaces connected through `Skw.Annotation` relationships ^c20260724-20u
- [CT] Skw tooling checks that declared documentation relationships resolve and remain aligned ^c20260724-20u
- [DC] authoritative meaning and evaluation protocol live on the documentation surfaces, not in linter output ^c20260724-20u
- [PR] a `Point.Of.Interest` carries the evidence needed to reach the relevant documentation ^c20260724-20u
- [RJ] `POI.Documentation` is not the `POI.Catalog` and is not duplicated into each `POI.Instance` ^c20260724-20u

****

## POI.Linter/Agendix/Candidate.POI.Blessing

- [DF] a `POI.Blessing` is the explicit act of accepting the current state represented by one `POI.Instance` ^c20260724-23u
- [CT] every blessing targets exactly one `POI.Instance` ^c20260724-23u
- [RJ] blessing an instance does not bless its `POI.Class`, another instance, or a future occurrence ^c20260724-23u
- [CT] only `POI.Class`es that declare blessing as an allowed act may be blessed ^c20260724-23u
- [CT] the applicable `Skw.Gate.Policy` determines which gates defend and audit the blessing ^c20260724-23u
- [DC] missing or unsatisfied gates prevent acceptance and are reported individually ^c20260724-23u
- [PR] blessing is loud and never occurs as a side effect of rebuilding or unrelated changes ^c20260724-23u
- [FR] the owning `POI.System` defines how an accepted instance is recorded or materialized ^c20260724-23u
