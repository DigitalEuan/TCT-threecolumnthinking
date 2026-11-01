#!/usr/bin/env python3
"""Paper updates for the regenerated Run D bundle + two regeneration findings."""

PAPER = "/home/z/my-project/download/tct_paper.md"

EDITS = []


def edit(old, new):
    EDITS.append((old, new))


# 1 - Artifacts paragraph: describe the regenerated bundle accurately
edit(
"""# Artifacts

The Run D artifact bundle accompanies this paper: per-question directories
`T01…T12/` each containing `column3.py` (the Column-3 re-derivation),
`spec.json`, the scaffolded Lean project `lean_tct/` (built, Lean 4.35.0),
`decomp_before/after.json`, `payload.md` (the full three-column answer in the
skill's §6 output format), and the run-level logs
(`RUN_D_SUMMARY.md`, `lean_tier.log`, `optimization_loop.log`,
`results.log`), together with the environment probes (`lean_probe/`).""",
"""# Artifacts

The Run D artifact bundle accompanies this paper. The original payload was
lost to an environment recycle; the shipped bundle is a **regeneration**
(see its `REGENERATION_NOTES.md`): per-question directories `T01…T12/` each
containing `column3.py` (the Column-3 re-derivation, regenerated and
re-executed), `spec.json` (lemma inventory locked to the battery table),
the scaffolded Lean project `lean_tct/` (built, Lean 4.35.0), and
`decomp_before/after.json`; plus the run-level records `RUN_D_SUMMARY.md`,
`lean_tier.log`, `optimization_loop.md`, `results.log`, `spot_checks.log`
(31/31), and the environment probes `lean_probe/` (15 live probes,
`probe_results.md`). Every artifact in it was re-executed in the
regeneration environment; the original per-question payload files (the
§6-format three-column answers) are not recoverable, and their analytical
content lives in §5.4 and §6.8–6.11 above.""")

# 2 - reference [4]: regeneration note
edit(
"""[4] Run D artifact bundle (this study): dola.com AI system, 1 Nov 2026 —
12 question directories (T01–T12) with Column-3 scripts, Lean specs and
built Lake projects (Lean 4.35.0 / Lake 5.0.0), optimization-loop
decompositions, and per-question TCT payloads; plus environment probes and
run logs.""",
"""[4] Run D artifact bundle (this study): dola.com AI system, 1 Nov 2026 —
12 question directories (T01–T12) with Column-3 scripts, Lean specs and
built Lake projects (Lean 4.35.0 / Lake 5.0.0), optimization-loop
decompositions, and environment probes and run logs. Regenerated and
re-verified live (Tier 1 12/12 + 31/31 spot checks; Tier 2 12/12 built,
56/9/25) after the original payload was lost to an environment recycle;
provenance in the bundle's REGENERATION_NOTES.md.""")

# 3 - section 7: xor probe refinement (p12)
edit(
"""`Nat.factorial` is absent (the scaffold must
define its own); `decide` also fails on Nat bitwise XOR; and core Lean cannot
name `Real.pi` at all,""",
"""`Nat.factorial` is absent (the scaffold must
define its own); `decide` fails on Nat bitwise XOR *goals with variables*
(the regeneration refined the boundary: closed-literal XOR such as
`5 ^^^ 3 = 6` does decide, while `∀ a, (a ^^^ 0) = a` does not); and core
Lean cannot name `Real.pi` at all,""")

# 4 - section 5.4: T10 loop-accounting refinement
edit(
"""optimisation loop (one iteration) accepted 7 reductions — every one of which
removed an audited tautology or a reporting step, never a witness path — and
correctly stopped at the floor for the 5 minimal derivations (T03, T06, T09,
T11, T12: dropping any remaining primitive would drop a verification path).
Cross-check paths were preserved in every accepted iteration.""",
"""optimisation loop (one iteration) accepted 7 reductions — every one of which
removed an audited tautology or a reporting step, never a witness path — and
correctly stopped at the floor for the 5 minimal derivations (T03, T06, T09,
T11, T12: dropping any remaining primitive would drop a verification path).
Cross-check paths were preserved in every accepted iteration. (The
regeneration's loop re-costing records one accounting refinement: T09 is
double-counted in that sentence — it accepted the Lagrange-evaluation
removal and then stopped at its floor — and T10, unassigned there, also
stops at the floor; 7 accepted + 6 floors − 1 overlap covers all twelve
tests exactly.)""")


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
