r"""Rule 03 — Phone number.                                        Owner: M04

Spec (assignment)
    Format XXX-XXX-XXXX, keep only the last 4 digits.
    093-245-7894  ->  XXX-XXX-7894

Requirements
    [ ] Thai format 0xx-xxx-xxxx; also "0xx xxx xxxx" and "0xxxxxxxxx" (consistent separator).
    [ ] International format "+66 93-245-7894" -> "+66 XX-XXX-7894" (hint: alternation).
    [ ] Must NOT match "123-456-7890" (no leading 0) or "093-245-78945" (too many digits).
    [ ] Named group `last4`.
    [ ] Mask with re.sub(r"\d", "X", ...) on everything except the last 4 digits.
    [ ] re.VERBOSE with a comment on every line; fill in explain_th / explain_en.

Note: the engine runs the card rule BEFORE this one, so you do not need to worry about
digits that are part of a credit card number.

Acceptance tests: tests/rules/test_phone.py
"""
from __future__ import annotations

import re

from pdpa_shield.engine.types import Rule

# TODO(M04)
PATTERN: re.Pattern | None = None


def mask(m: re.Match) -> str:
    """Return e.g. 'XXX-XXX-7894' or '+66 XX-XXX-7894'."""
    raise NotImplementedError("M04: implement rules.phone.mask")


RULE = Rule(
    key="phone", label_th="เบอร์โทรศัพท์", label_en="Phone number",
    color="#f59e0b", weight=2, pattern=PATTERN, replace=mask,
    example="093-245-7894",
    explain_th=[],  # TODO(M04)
    explain_en=[],  # TODO(M04)
)
