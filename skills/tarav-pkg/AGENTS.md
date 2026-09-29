# SKW maintenance

This package is a typed `SkwSkill`; `.skw/main.json` declares its sources and
consumer files. Markdown products are compiled from `.skw/src/`.

Edit the corresponding `.skw.json` source and compile it rather than editing
the Markdown product directly. The initial migration preserves all 14 existing
documents byte-for-byte as typed literal `content` blocks with retained
`output`. It claims no generation
history and declares no consumer loading graph; those can be modeled deliberately
later. The Constitution still governs changes to its source and product.

From this directory:

```sh
tarav skw skills ls --limit 5
tarav skw skills ls --source SKILL.skw.json
tarav skw skills read --source SKILL.skw.json --block content
tarav skw skills build
tarav skw skills check
```

`AGENTS.md` is developer guidance, not a deployed consumer file.
