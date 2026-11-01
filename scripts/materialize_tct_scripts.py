#!/usr/bin/env python3
"""Materialize the four TCT bundled scripts from SKILL.md S13 code blocks."""
import os
import re
import sys

SKILL = "/home/z/my-project/tct_work/SKILL.md"
OUT = "/home/z/my-project/tct_work/scripts"

NAMES = ["verify_column3", "scaffold_lean_project", "lean_ledger", "cent_cost"]


def main():
    text = open(SKILL, encoding="utf-8").read()
    os.makedirs(OUT, exist_ok=True)
    for name in NAMES:
        header = f"### scripts/{name}.py"
        i = text.find(header)
        if i < 0:
            print(f"ERROR: header not found: {header}")
            return 1
        m = re.search(r"```python\n(.*?)```", text[i:], re.S)
        if not m:
            print(f"ERROR: code block not found after {header}")
            return 1
        src = m.group(1)
        path = os.path.join(OUT, f"{name}.py")
        with open(path, "w", encoding="utf-8") as f:
            f.write(src)
        print(f"wrote {path} ({len(src)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
