# Usage.Pattern.Routing — Appendix

****

## Usage.Pattern.Routing/Deployments

- a row's value can be deployed several ways: an inline router entry; an `Aux.Workflow.Skill` when a hot path deserves its own skill surface; a dynamic master-agent preset-prompt; or a vendored static doc
- the vendored static doc (the former `Usage.Workflow`) is a derived module — an operational projection of index knowledge, citing the blocks it projects, drift-checked via its skw declarations (`Skw.Ann.Dependency`) ^c20260710-2u
- the dynamic preset-prompt is regenerated from the index per call — no drift, a cost per call
- choose on the vendored↔dynamic dial: read-cheap static where traffic is high and stable, dynamic where freshness matters
