"""Replace @M01 … @M10 in .github/CODEOWNERS with the GitHub usernames from scripts/members.json.

    python3 scripts/apply_members.py          # then commit the updated CODEOWNERS
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
members = json.loads((ROOT / "scripts/members.json").read_text(encoding="utf-8"))["members"]
path = ROOT / ".github/CODEOWNERS"
text = path.read_text(encoding="utf-8")
missing = [k for k, v in members.items() if not v.get("github")]
text = re.sub(r"@(M\d\d)\b", lambda m: "@" + members[m[1]]["github"] if members[m[1]].get("github") else m[0], text)
path.write_text(text, encoding="utf-8")
print("CODEOWNERS updated." + (f" Still missing usernames for: {', '.join(missing)}" if missing else ""))
