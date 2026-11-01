#!/usr/bin/env python3
"""Paper addendum: post-study skill v3 note (§7 closing + reference [3])."""

PAPER = "/home/z/my-project/download/tct_paper.md"

EDITS = []


def edit(old, new):
    EDITS.append((old, new))


# 1 - §7 closing: post-study update paragraph (after the conceptual-questions paragraph)
edit(
"""**On conceptual questions.** Roughly half of each answer landed as axioms in
every run. This is the method behaving as designed: it cleanly separates what
exact arithmetic can check from what physics must assume, and records the
latter by name rather than smuggling it in as proved. Run D extends the
observation across domains: the axiom share is a measurable signature of
question type (25–50% for "why/what is" questions, 0–17% for deterministic
ones, π-inflated 27% for T10).""",
"""**On conceptual questions.** Roughly half of each answer landed as axioms in
every run. This is the method behaving as designed: it cleanly separates what
exact arithmetic can check from what physics must assume, and records the
latter by name rather than smuggling it in as proved. Run D extends the
observation across domains: the axiom share is a measurable signature of
question type (25–50% for "why/what is" questions, 0–17% for deterministic
ones, π-inflated 27% for T10).

**Post-study update (skill v3, same day).** After the study, the skill was
updated to close all four remaining gaps, and every fix was verified live on
the same Lean 4.35.0 / Lake 5.0.0 environment. (i) The output format now
permits exactly what Run D improvised: a multi-line Python witness is
represented in the table cell by its cross-check name or KEY, with the full
witness in the Column-3 script — "never truncate mathematics to fit the
column" (gap 1). (ii) The ledger requires a **coverage map**: Lean lemmas
cover k of N claims, Python-only steps listed by number with a reason — "a
coverage hole is not an error; an unlisted one is" (gap 2). (iii) The output
format names a **Reading** block for licensed interpretations of ambiguous
wording, declared before decomposition and licensed like axioms, with two
conflicting readings routing to `READINGS_DISAGREE` (gap 3). (iv) §8 was
rewritten **probe-first**: a new fifth bundled script `lean_probe.py` checks
tactic/notation availability at run time against the corrected 4.35.0
baseline (13 probes; on this toolchain 13/13 agree), the wrong `norm_num` /
`omega` claims are replaced by the verified landscape table, the failing
`ℚ` worked example became the kernel-checked Nat cross-multiplication
pattern, and a three-rung degradation ladder governs missing capability —
core-available pattern, sorry + named gap, "not run; ready" (gap 4). The
bundled scaffold's lakefile now targets current Lake (single `lean_lib`
with an explicit glob, no `lean_exe`): a fresh project scaffolded and
compiled **as shipped** on Lake 5.0.0 with no workaround — the failure that
all four external case studies inherited is closed at the source. The v3
skill ships with this repository as `skill/SKILL_v3.md`; the version
evaluated in Runs A–D is retained verbatim as `skill/SKILL.md`.""")

# 2 - reference [3]: point to both versions
edit(
"""[3] `three-column-thinking` Skill (this study): single self-contained
`SKILL.md` (586 lines, 14 sections; the updated version evaluated in Run D
adds the §14 four-conditions runbook and the `lean_ledger.py` scanner fix) +
`scripts/{verify_column3,scaffold_lean_project,lean_ledger,cent_cost}.py`.""",
"""[3] `three-column-thinking` Skill (this study): single self-contained
`SKILL.md` (586 lines, 14 sections; the updated version evaluated in Run D
adds the §14 four-conditions runbook and the `lean_ledger.py` scanner fix) +
`scripts/{verify_column3,scaffold_lean_project,lean_ledger,cent_cost}.py`.
Post-study v3 (718 lines, five bundled scripts incl. `lean_probe.py`;
probe-first §8, Lake-5 scaffold, Reading block, coverage map) ships as
`skill/SKILL_v3.md`; the evaluated version is retained as `skill/SKILL.md`.""")


def main():
    text = open(PAPER, encoding="utf-8").read()
    for i, (old, new) in enumerate(EDITS, 1):
        if old not in text:
            print(f"EDIT {i}: OLD STRING NOT FOUND")
            return 1
        if text.count(old) != 1:
            print(f"EDIT {i}: NOT UNIQUE ({text.count(old)})")
            return 1
        text = text.replace(old, new)
    with open(PAPER, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"applied {len(EDITS)} edits; paper now {len(text.splitlines())} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
