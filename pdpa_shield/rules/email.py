r"""Rule 02 — Email address.                                       Owner: M03

Spec (assignment)
    Hide the username except its first and last character, keep the domain.
    somchai.d@company.com  ->  s*******d@company.com      (one * per hidden character)

Requirements
    [ ] Named groups `first`, `middle`, `last`, `domain`.
    [ ] Username may contain letters, digits and . _ % + -
    [ ] Multi-level domains such as bank.co.th must work (hint: (?:label\.)+tld).
    [ ] Must NOT match "user@localhost" (no TLD).
    [ ] Decide and document what happens to a 1- or 2-character username.
    [ ] re.VERBOSE with a comment on every line; fill in explain_th / explain_en.

Acceptance tests: tests/rules/test_email.py
"""
from __future__ import annotations

import re

from pdpa_shield.engine.types import Rule

# TODO(M03)
PATTERN: re.Pattern | None = None


def mask(m: re.Match) -> str:
    """Return e.g. 's*******d@company.com'."""
    raise NotImplementedError("M03: implement rules.email.mask")


RULE = Rule(
    key="email", label_th="อีเมล", label_en="Email",
    color="#0a6cff", weight=1, pattern=PATTERN, replace=mask,
    example="somchai.d@company.com",
    explain_th=[],  # TODO(M03)
    explain_en=[],  # TODO(M03)
)
