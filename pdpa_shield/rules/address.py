r"""Rule 05 — Thai address (starts with "Address:").               Owner: M06

Spec (assignment)
    Address: <house no.> [soi] <road> <subdistrict> <district> <province>
    Mask only the house number.
    Address: 689 ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ
      -> Address: XXX ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ

Requirements
    [ ] Named groups: prefix, house, moo, soi, road, subdistrict, district, province.
    [ ] house may be "689" or "99/12".
    [ ] moo (หมู่ / ม.) and soi (ซอย / ซ.) are optional groups.
    [ ] Bangkok (แขวง / เขต) and provinces (ตำบล / อำเภอ / จังหวัด) both work.
    [ ] Road names may contain a number: "ถนนพระราม 4".
    [ ] Use [ \t]+ between parts (never \s+) so a match cannot run onto the next log line.
    [ ] "Address: 689 ไม่ระบุ" must NOT match.
    [ ] RULE.target = "house" (only that group is replaced) — already set below.
    [ ] re.VERBOSE with a comment on every line; fill in explain_th / explain_en.

Acceptance tests: tests/rules/test_address.py
"""
from __future__ import annotations

import re

from pdpa_shield.engine.types import Rule

# TODO(M06)
PATTERN: re.Pattern | None = None


def mask(m: re.Match) -> str:
    """Return the replacement for the `house` group only, i.e. 'XXX'."""
    raise NotImplementedError("M06: implement rules.address.mask")


RULE = Rule(
    key="address", label_th="ที่อยู่ (เลขที่บ้าน)", label_en="Address (house number)",
    color="#12b76a", weight=3, pattern=PATTERN, replace=mask, target="house",
    example="Address: 689 ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ",
    explain_th=[],  # TODO(M06)
    explain_en=[],  # TODO(M06)
)
