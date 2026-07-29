---
name: hugentics-designer
description: "Compatibility entry for the product-design workflow owned by agentos-index --design."
---

# Hugentics Designer Compatibility Entry

`agentos-index --design` is the canonical public entry and sole workflow owner for product design.

Resolve every invocation of this compatibility skill as `agentos-index --design`. Forward the bare topic as `--scope`, preserve `--artifact` and `--AUTO`, and do not create separate workflow state.

Load `agentos-index` and its selected `references/design/` modules. The reference files in this package are compatibility forwarders only and carry no independent behavior.

This compatibility entry remains available until migration consumers no longer depend on the old skill name.
