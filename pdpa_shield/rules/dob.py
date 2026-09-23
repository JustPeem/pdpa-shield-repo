r"""Rule 04 — Date of birth (starts with "DOB:").                  Owner: M05

Spec (assignment)
    Mask everything except the first 2 digits of the Buddhist-era year.
    DOB:25/12/2549  ->  DOB:XX/XX/25XX

Requirements
    [ ] Validate day 01–31 and month 01–12 with alternation (0[1-9]|[12]\d|3[01] ...).
    [ ] Year must be Buddhist era 25xx; a Gregorian year (2006) must NOT match.
    [ ] Allow "dob : 01-01-2530" (case-insensitive, optional spaces, separator / . or -,
        same separator on both sides — backreference).
    [ ] Keep the "DOB:" prefix exactly as written (named group `prefix`).
    [ ] "DOB:32/13/2549" must NOT match.
    [ ] re.VERBOSE with a comment on every line; fill in explain_th / explain_en.

Acceptance tests: tests/rules/test_dob.py
"""
from __future__ import annotations

import re

from pdpa_shield.engine.types import Rule

# TODO(M05)
PATTERN: re.Pattern | None = None


def mask(m: re.Match) -> str:
    """Return e.g. 'DOB:XX/XX/25XX'."""
    raise NotImplementedError("M05: implement rules.dob.mask")


RULE = Rule(
    key="dob", label_th="วันเดือนปีเกิด", label_en="Date of birth",
    color="#8b5cf6", weight=3, pattern=PATTERN, replace=mask,
    example="DOB:25/12/2549",
    explain_th=[],  # TODO(M05)
    explain_en=[],  # TODO(M05)
)
