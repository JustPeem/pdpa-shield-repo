# Architecture

## Data flow

```
 browser (web/static/js)                     server (pdpa_shield)
 ───────────────────────                     ─────────────────────────────────────────────
 mask.js ── api.mask(text, enabled) ──POST /api/mask──> app.py
                                                          └─ engine.scanner.scan(text, RULES, enabled)
                                                               for rule in RULES (priority order):
                                                                  rule.pattern.finditer(text)   <- rules/*.py
                                                               resolve overlaps, build Parts
                                                          └─ engine.risk.stats(parts, RULES)
        <──────────── {parts, masked, stats} ─────────────
 renders Before / After panes, stats, risk ring
```

## Modules

| Module | Responsibility | Depends on |
|---|---|---|
| `engine/types.py` | `Rule`, `Part`, `Stats`, `apply_single()` | — |
| `rules/*.py` | One `RULE` each: pattern, mask function, labels, explanations | `types` |
| `engine/registry.py` | `RULES` in priority order: card, email, phone, dob, address | `rules` |
| `engine/scanner.py` | `scan()`, `mask_text()` | `types` |
| `engine/risk.py` | `stats()` — PDPA risk score | `types` |
| `engine/highlight.py` | `highlight_pattern()` — regex tokenizer for the Rules page | — |
| `loggen.py` | Fake log generator with decoys | — |
| `app.py` | Flask routes (docs/API.md) | all of the above |
| `cases.py` | Canonical acceptance cases used by pytest and `/api/tests` | — |

## Why priority order matters

`1234-5678-9012-3456` contains no phone number, but a careless phone pattern could match `5678901234`
inside `1234567890123456`. The scanner runs **card before phone**, and a span that is already accepted
can never be matched again. Lookarounds in each pattern are a second line of defence.

## DFA

*Owner: M04 (theory) · M10 (implementation)*

TODO(M04): expand this section for the report. Key points:

1. Backreferences make languages non-regular in general (`(a*)b\1`), but `(?P<sep>[-\x20]?)…(?P=sep)`
   ranges over only **three** values, so the language equals
   `\d{4}(?:-\d{4}-\d{4}-|\x20\d{4}\x20\d{4}\x20|\d{8})\d{4}` — a plain regular expression.
2. The DFA therefore splits into 3 branches after the first 4 digits (on `-`, space, or a digit).
3. The branches **merge** before the last 4 digits: in every branch the remaining language is exactly
   "4 digits", so those states are equivalent (Myhill–Nerode) and the minimal DFA shares them.
4. Lookarounds are not part of the DFA; they constrain where a match may start/end inside the log line.
5. Python's `re` is a backtracking engine — it does not build this DFA. The DFA page is a model of the
   *language*, not of how `re` executes.
