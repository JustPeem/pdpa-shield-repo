# Contributing

## Branches

| Branch | Purpose | Who merges |
|---|---|---|
| `main` | Stable, demo-ready. Tagged releases (`v0.1`, `v1.0`). | M01 only, from `develop` |
| `develop` | Integration branch. All feature PRs target this. | M01 after 1 approval + green CI |
| `feature/<member>-<short-name>` | Your work, e.g. `feature/m04-phone-rule` | you |
| `reference` | Complete working implementation, read-only | nobody |

## Workflow

1. Pick your issue on the project board, move it to **In progress**.
2. `git switch develop && git pull && git switch -c feature/m04-phone-rule`
3. Work in **your own files** (see `CODEOWNERS`). If you must touch someone else's file, tag them in the PR.
4. `pytest -q && ruff check .` must pass locally.
5. Open a PR into `develop` using the template. Link the issue (`Closes #12`).
6. One approval from the file owner or M01, CI green, then squash-merge.

## Commit messages

`<area>: <what>` in the imperative, e.g.

```
rules/phone: support +66 international format
engine: resolve overlapping matches by priority
web/mask: auto-grow the source-log textarea
```

## Rules of the assignment

- Detection and masking use **only** Python's `re` module (no third-party regex, no JS regex).
- Every pattern is written with `re.VERBOSE` and a comment on each line.
- Every rule has test cases for what it **must** match and what it **must not** match.
- No emoji in the UI; icons are SVG.

## Changing a shared contract

`engine/types.py`, `cases.py`, `docs/API.md` and `web/static/css/tokens.css` are shared.
Open an issue labelled `contract` first, get a thumbs-up from every affected owner, then PR.
