# Dotted.Notation — Appendix

****

## Dotted.Notation/NOT.Triggers

- abbreviations: `e.g.`, `i.e.`, `etc.`
- filenames: `file.txt`, `config.json`, `SKILL.md`
- URLs: `github.com`, `anthropic.com`
- lowercase dotted: `user.name`, `object.method`
- single-part names: just `Index` alone is not a trigger

****

## Dotted.Notation/Regex.Patterns

Formal patterns for detection and linting:

```
Basic:          [A-Z][a-z]+(\.[A-Z][a-z]+)+
Parameterized:  [A-Z][a-z]+(\.[A-Z][a-z]+)+:[A-Za-z][\w\-\.]*
Variable:       <[A-Z][a-z]+>(\.[A-Z][a-z]+)+
Variable+Param: <[A-Z][a-z]+>(\.[A-Z][a-z]+)+(:<[A-Z][a-z]+>|:[A-Za-z][\w\-\.]*)
```
