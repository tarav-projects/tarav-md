# Tarav on GitHub

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

Tarav's public repositories live in the GitHub organization
[`tarav-projects`](https://github.com/tarav-projects). Most of their consumers
are the User's own projects. This module holds the central design of that
maintenance; details are added as they are decided.
<!-- tarav.breadcrumb a963d11822d527601cec2cb3cde356dc0fa9c80dc206a0ac440bafa9ed302f89 -->

## Source repositories

- Each source repository is developed on `main`. `main` is a development
  branch: it is organized as work progresses, not curated before publishing.
- Consumers, mostly other Tarav projects, track `main` directly, for example
  `uv tool install git+https://github.com/tarav-projects/tarav-py` or the
  dependency `tarav @ git+https://github.com/tarav-projects/tarav-py@main`.
- Every repository carries an MIT `LICENSE` at its root.
- Versions will come from Git tags (`hatch-vcs`) when releases start: a
  release reports `X.Y.Z`, a later commit something like
  `X.Y.(Z+1).devN+g<hash>`, so a consumer of `main` can tell its exact commit.
<!-- tarav.breadcrumb 65b8fdd5c2f3389c2759f46688f47ff1ed4dc28f9f33c587b462981460d6d58f -->

Published source repositories: `tarav-py` (the Python distribution) and
`tarav-md` (skills, Wiki and notes; development only).
<!-- tarav.breadcrumb c2782d5a72ba432ac094159110816cb427f8c75f64995048841f48ece88f3d17 -->

## tarav-releases

`tarav-releases` is a repository only for releases, a release system fully
decoupled from the source repositories. Manifests name bundles, such as
tarav-py with the skills, or tarav-py with the extension and the skills, each
source pinned at a commit or tag. A build assembles a bundle's artifacts and
publishes them as a GitHub Release of `tarav-releases`, with tags prefixed by
bundle. The source repositories stay installable by hand.
<!-- tarav.breadcrumb 407a4472d10a4c37902c878fb94a3a8e1a2d4acaef210dae8904e7174b7a1b4c -->
<!-- tarav.breadcrumb 8bf86c5f0387b6679c871923ebb73645821f8a21f922f80b55be1c865730295d -->

The skills are not a bundle of their own: each product needs the tarav skills,
and each bundle places them where its product expects them. The release
process is developed inside `tarav-releases`.
<!-- tarav.breadcrumb 548e38d816d041b430b725d1f119e74826d23b9dfc390ea01f2d88288fe0d2be -->

## Before publishing

Before a repository's first push or a change of its visibility, scan its whole
history:

```bash
gitleaks git <repository> --redact
```

Review every finding. Record reviewed false positives by fingerprint in the
repository's `.gitleaksignore`, so later scans show only new findings. Stop on
a real secret: rotate it and remove it from history before publishing.
Rewriting history changes commit hashes; tarav-change IDs keep references
findable.
<!-- tarav.breadcrumb 6eed2af890fa033901101705dd6fa142e83f82641bb5b014497ed4803dd562a0 -->

## Creating a repository

```bash
gh repo create tarav-projects/<name> --public --source <path> --remote origin --push
```

The default branch is `main`.

