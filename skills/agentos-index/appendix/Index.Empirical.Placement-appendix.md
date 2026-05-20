# Index.Empirical.Placement — Appendix

## Index.Empirical.Placement/Extraction

- two modes: programmatic (scrape user + visible assistant for `Dotted.Names`) and semantic (agent judges which concepts were reasoned about)
- programmatic is cheap and deterministic — good proxy for frequent runs
- semantic is expensive but catches unnamed usage — good for deep audits

****

## Index.Empirical.Placement/Signals

- promotion: appendix concept used more than index-level neighbors
- demotion: index concept used less than appendix-level neighbors
- load-but-not-used: concept was in context but never referenced — demotion signal
- discovery-frequency: how often agents load an appendix — promotion signal

****

## Index.Empirical.Placement/Configuration

- scope is configurable per run — single project, cross-project, time-windowed
- algorithms are pluggable: frequency, recency-weighted, co-occurrence, discovery-frequency

****

## Index.Empirical.Placement/Delegation

- this is a strong target for agentic work with medium-size models
- the extraction and comparison steps are bounded, repetitive, and well-defined
- a medium model can scrape sessions, count usage, compare layers, and produce a migration plan draft
- the human or a stronger model reviews the plan — the mining itself doesn't need top-tier reasoning
- fits naturally into `Iterante` task loops or periodic maintenance passes
