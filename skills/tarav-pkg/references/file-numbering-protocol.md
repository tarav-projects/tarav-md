# File Numbering Protocol

Operational procedure for allocating Agentos numeric filename prefixes.

## Command

Use `agentos stdlib prefix next`.

Preferred form from inside the intended project tree:

```sh
agentos stdlib prefix next --project-base <project-root-basename> --target <project-relative-target>
```

Explicit form from outside the project tree:

```sh
agentos stdlib prefix next --project /path/to/project --project-base <project-root-basename> --target <project-relative-target>
```

Examples:

```sh
agentos stdlib prefix next --project-base agentos-md --target notes/live
agentos stdlib prefix next --project-base agentos-md --target dev/live
```

## Rules

- Do not assign ordinary numeric prefixes by manual inspection.
- Use `--project-base` so allocation fails if discovery resolves the wrong project.
- Do not use `--project .` unless `.` is the initialized project root.
- If allocation fails, stop and resolve the project target instead of guessing.
- Prefixes are append-only stable handles. Do not renumber existing files to close gaps.

## Current Targets

| Target | Surface | Ordinary Range |
|---|---|---|
| `notes/live` | `Agentos.Live.Note` | `500-999` |
| `dev/live` | `Agentos.Live.Script` | `500-999` |

The allocator currently scans configured project numbered surfaces, including `notes` and `dev/live`, then allocates for the selected target route.
