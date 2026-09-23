# Team plan — 10 members

Replace `Member 01 … Member 10` with real names and GitHub usernames in
[`scripts/members.json`](../scripts/members.json) and [`.github/CODEOWNERS`](../.github/CODEOWNERS).

## Overview

| ID | Role | Owns | Main deliverable | Side responsibility |
|---|---|---|---|---|
| **M01** | Tech Lead & Integrator | `engine/types.py`, `cases.py`, CI, `tests/test_integration.py` | Green integration test on `main`, release `v1.0` | Final report editor, demo script |
| **M02** | Regex — Credit card | `rules/card.py` | Card rule + Luhn info | Card DFA review with M10 |
| **M03** | Regex — Email | `rules/email.py` | Email rule | Presentation slides lead |
| **M04** | Regex — Phone | `rules/phone.py` | Phone rule incl. +66 | RE → DFA theory write-up |
| **M05** | Regex — Date of birth | `rules/dob.py` | DOB rule with date validation | QA lead: manual test checklist |
| **M06** | Regex — Address | `rules/address.py` | Thai address rule (hardest regex) | Address test cases from real formats |
| **M07** | Masking engine | `engine/registry.py`, `scanner.py`, `risk.py`, `highlight.py` | Priority/overlap scanner, risk score, highlighter | Performance check on 10k-line logs |
| **M08** | Backend & data | `app.py`, `loggen.py`, `web/static/js/api.js`, `docs/API.md` | All `/api/*` endpoints, log generator | Deployment / run instructions |
| **M09** | Frontend — shell & Mask page | `index.html`, `base.css`, `mask.css`, `app.js`, `i18n.js`, `icons.js`, `mask.js` | Liquid Glass shell, TH/EN, page 01 | Design system owner (`tokens.css`) |
| **M10** | Frontend — Rules, Tests, DFA | `rules.*`, `tests.*`, `dfa.*` (css + js) | Pages 02–04 incl. animated DFA | Screenshots for the report |

Everyone: write the report section for what they own (half a page + one screenshot or diagram).

## How the work fits together

```
 M02 card ─┐
 M03 email ├─> Rule objects ──> M07 engine (scan, risk, highlight) ──> M08 API ──> M09/M10 pages
 M04 phone │   (engine/types.py)                                        (docs/API.md)
 M05 dob   │
 M06 addr ─┘            M01 owns the contracts and the integration test
```

Nobody is blocked on day 1:

- Rule owners test with `apply_single()` — no engine needed.
- M07 tests the engine with fake rules (`tests/engine/test_scanner.py`).
- M08 codes against the engine's function signatures; tests turn green as M07 lands.
- M09/M10 build the UI against the **reference backend** (see below) until `develop` is ready.

## Timeline (4 weeks)

| Week | Milestone | Exit criteria |
|---|---|---|
| 1 | **M1 · Foundations** | Everyone has cloned, run `pytest`, opened a draft PR. Contracts frozen. Tokens + shell layout merged. First draft of every pattern. |
| 2 | **M2 · Core** | All `tests/rules/*` and `tests/engine/*` pass. `/api/mask`, `/api/generate` work. |
| 3 | **M3 · UI & integration** | All four pages work in TH/EN, light/dark. `tests/test_integration.py` passes. `v0.9` on `main`. |
| 4 | **M4 · Polish & delivery** | QA checklist done, report + slides done, demo rehearsed, `v1.0` tagged. |

---

## M01 — Tech Lead & Integrator

**Owns:** repository settings, CI, `pdpa_shield/engine/types.py`, `pdpa_shield/cases.py`, `tests/test_integration.py`, merges to `main`.

- [ ] Run `scripts/github_bootstrap.sh`, invite members, protect `main` and `develop` (1 review + CI).
- [ ] Walk the team through the contracts in week 1; freeze them by end of week 1.
- [ ] Review every PR that touches a shared contract.
- [ ] Keep `develop` green; merge `develop` → `main` at each milestone, tag `v0.9`, `v1.0`.
- [ ] Integration: `tests/test_integration.py` green = project done.
- [ ] Edit the final report (collect sections from everyone) and write the 5-minute demo script.

**Done when:** `main` passes all 77 tests and the demo runs from a fresh clone following the README.

## M02 — Regex: Credit card

**Owns:** `pdpa_shield/rules/card.py`, `tests/rules/test_card.py`

- [ ] Pattern with lookbehind/lookahead boundaries and a backreference for a consistent separator.
- [ ] `mask()` keeps the separator; named group `last4`.
- [ ] `info()` returns `luhn_ok` / `luhn_fail` (Luhn checksum — tooltip only, not used for matching).
- [ ] `explain_th` / `explain_en` bullets; at least 2 extra cases in `cases.py` (1 positive, 1 negative).
- [ ] Review the card DFA on page 04 with M10: it must accept exactly what the regex accepts.

## M03 — Regex: Email (+ slides lead)

**Owns:** `pdpa_shield/rules/email.py`, `tests/rules/test_email.py`

- [ ] Pattern with named groups `first`, `middle`, `last`, `domain`; multi-level domains.
- [ ] One `*` per hidden character; decide and document the 1–2 character username case.
- [ ] Negative cases: no TLD, email glued to other words.
- [ ] Lead the presentation slides (structure, visuals, timing) with input from everyone.

## M04 — Regex: Phone (+ DFA theory)

**Owns:** `pdpa_shield/rules/phone.py`, `tests/rules/test_phone.py`, `docs/ARCHITECTURE.md#dfa`

- [ ] Thai and `+66` formats via alternation; consistent separator via backreference.
- [ ] Negative cases: no leading 0, too many digits.
- [ ] Write the theory section: why a backreference over a finite separator set is still regular,
      how the 3-branch DFA is derived, why the branches merge (equivalent states → minimal DFA).

## M05 — Regex: Date of birth (+ QA lead)

**Owns:** `pdpa_shield/rules/dob.py`, `tests/rules/test_dob.py`, `docs/QA_CHECKLIST.md`

- [ ] Validate day 01–31 and month 01–12 with alternation; Buddhist-era year 25xx only.
- [ ] Case-insensitive `DOB`, optional spaces, `/ . -` separators (same on both sides).
- [ ] Write and run the manual QA checklist (every button, TH/EN, light/dark, mobile, reduced motion) in weeks 3–4; file bugs as issues.

## M06 — Regex: Address

**Owns:** `pdpa_shield/rules/address.py`, `tests/rules/test_address.py`

- [ ] Named groups for every address part; optional `moo` and `soi`; Bangkok and provincial wording.
- [ ] Never cross a line break (`[ \t]+`, not `\s+`).
- [ ] Collect at least 5 more real-world address shapes and add them to `cases.py`.

## M07 — Masking engine

**Owns:** `pdpa_shield/engine/registry.py`, `scanner.py`, `risk.py`, `highlight.py`, `tests/engine/*`

- [ ] `scan()`: priority order, overlap resolution, target-group replacement, lossless parts.
- [ ] `mask_text()`, `stats()` (risk formula in `risk.py` docstring).
- [ ] `highlight_pattern()` — a tokenizer for regex syntax, itself written with `re`.
- [ ] Benchmark: 10 000 generated lines must mask in under 2 s; note the result in the report.

## M08 — Backend & data

**Owns:** `pdpa_shield/app.py`, `pdpa_shield/loggen.py`, `web/static/js/api.js`, `docs/API.md`, `tests/test_api.py`, `tests/test_loggen.py`

- [ ] All endpoints in `docs/API.md`, returning exactly those shapes.
- [ ] Upload: size limit, encodings `utf-8`, `utf-8-sig`, `cp874`, `tis-620`; clear 400 errors.
- [ ] `loggen.generate(n, seed)`: every PII shape plus decoys; deterministic with a seed.
- [ ] Keep `api.js` in sync; tell M09/M10 in the PR when a response changes.

## M09 — Frontend: shell, design system, Mask page

**Owns:** `web/templates/index.html`, `web/static/css/{tokens,base,mask}.css`, `web/static/js/{app,i18n,icons,mask}.js`

- [ ] Liquid Glass shell: ambient background, glass sidebar with sliding nav indicator, segmented controls.
- [ ] TH/EN switching for every string (`i18n.js`), default Thai; light/dark theme; both remembered.
- [ ] Page 01 exactly as in `docs/DESIGN.md` (auto-height source log, A · summary, B · before/after, redaction animation, tooltips, copy/download, drag & drop).
- [ ] Mobile layout (< 900 px) and `prefers-reduced-motion`.

## M10 — Frontend: Rules, Tests, Automaton pages

**Owns:** `web/static/css/{rules,tests,dfa}.css`, `web/static/js/{rules,tests,dfa}.js`

- [ ] Page 02: legend + rule cards with highlighted patterns (from `tokens`), TH/EN explanations.
- [ ] Page 03: summary + progress, auto-height try-it box, results table with drawn check icons.
- [ ] Page 04: 3-branch minimal DFA for card and phone, tape + moving head, play/step/reset/speed,
      δ(q, a) readout, ACCEPT pulse / REJECT shake. **No JavaScript regex.**
- [ ] With M02/M04: prove the DFA accepts the same strings as the Python regex (random test).

---

## Reference branch

`reference` contains a complete working implementation in the same layout. Use it to:

- run a real backend while building the UI:
  ```bash
  git worktree add ../pdpa-ref reference
  cd ../pdpa-ref && pip install -r requirements.txt && flask --app pdpa_shield.app run --port 5001
  ```
- compare behaviour when you are stuck.

Do **not** copy it wholesale — the grade is for work you can explain. Every rule owner must be able to
explain each line of their pattern in the demo.

## Definition of done (every task)

- Tests for your files pass; `ruff check .` is clean.
- Docstring checklist in your file is fully ticked.
- PR reviewed and merged into `develop`; issue closed.
- Report section written (half a page + one figure).
