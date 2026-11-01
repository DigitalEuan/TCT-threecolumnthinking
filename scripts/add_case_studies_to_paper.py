#!/usr/bin/env python3
"""Stage 2: add the external case studies (aistudio.xiaomimimo.com quartet)
to the Run D edition of tct_paper.md. (maudlin 10/3/5 + totals 30/12/25 baked in.)"""

PAPER = "/home/z/my-project/download/tct_paper.md"

EDITS = []


def edit(old, new):
    EDITS.append((old, new))


# 1 - abstract
edit(
"""do not exist in core, and the bundled scaffold's lakefile template is
incompatible with Lake 5.0. Beyond verification, the
runs reveal the "why" of TCT:""",
"""do not exist in core, and the bundled scaffold's lakefile template is
incompatible with Lake 5.0. Finally, four independent case studies produced
on a third platform (aistudio.xiaomimimo.com) with the same updated skill —
the famous constants, the speed of light, physical isomorphisms, and Maudlin's
quantum measurement trilemma — are recorded and audited: their Python tiers
reproduce exactly (24/24 scripts, byte-identical bundled tooling, ledger and
loop claims all re-verified), while their Lean tiers fail to compile as
shipped for the same three stacked reasons Run D documented — "proved, not
compiled" is endemic, and the skill's environment guidance is the root cause.
Beyond verification, the
runs reveal the "why" of TCT:""")

# 2 - experimental design
edit(
"""- T12 "Given V=12 V, I=5 A, R=4 Ω, what is the power?" — the designed
  INCONSISTENT_GIVENS refusal.

**Comparison dimensions.**""",
"""- T12 "Given V=12 V, I=5 A, R=4 Ω, what is the power?" — the designed
  INCONSISTENT_GIVENS refusal.

**External case studies (the quartet).** Beyond the experiment-structured
runs, four self-authored TCT studies produced on a third platform,
aistudio.xiaomimimo.com, with the same updated skill are recorded and
audited as *use studies*: `famous-constants-tct` (deriving the famous
mathematical constants from first principles), `speed-of-light-derivation-tct`
(four boundaries of deriving c computationally), `physical-isomorphisms-tct`
(five measurable gains of physical→computational isomorphisms, and one
refusal), and `maudlin-measurement-trilemma-tct` (Maudlin's quantum
measurement trilemma as a truth table). Unlike Runs A–D, these chose their
own open-domain questions and shipped their own repositories; the audit
(§5.6) re-verified them end-to-end on the Run D environment.

**Comparison dimensions.**""")

# 3 - section 5.6
edit(
"""# 6. Why TCT: what the runs revealed""",
"""## 5.6 External case studies: the quartet, recorded and audited

Four independent studies (aistudio.xiaomimimo.com, updated skill) are
recorded as case studies; each ships a full TCT repository — eight
documentation files, six Column-3 scripts, a Lean project scaffolded from a
classified spec, cent decompositions, ledgers, and a verification report —
and all four bundle the skill's §13 scripts byte-identically (16/16 files).

| Study | Question shape | n = p+s+a+r | Refusal | ¢ v1→v2 | Lean (as claimed) |
|---|---|---|---|---|---|
| famous-constants | constants from first principles | 24 = 13+3+7+1 | α (`WOULD_BE_GUESS`) | 9→6 | 6/3/7 |
| speed-of-light | four boundaries of deriving c | 22 = 11+3+7+1 | α from theory (`WOULD_BE_GUESS`) | 10→7 | 5/3/7 |
| physical-isomorphisms | five gains, five preconditions | 22 = 13+3+6+0 | complexity-class speedups | 11→7 | 9/3/6 |
| maudlin-trilemma | measurement trilemma → 3 doors | 20 = 12+3+5+0 | — | 12→6 | 10/3/5 |
| | **Totals** | **88 = 49+12+25+2** | **2** | | **30/12/25** |

Highlights that extend the paper's findings: π derived three independent ways
with overlapping exact intervals below 10⁻²⁵; the invariant speed derived by
three unrelated formalisms (integer wave scheme, GF(2) symplectic Clifford
dynamics, Lieb–Robinson v = 2Ja, tight against both) while the dimensionless
value is formally refused; measurable isomorphism crossovers (energy 6419×/69×,
break-even N = 55/228, reuse T = 21) with complexity-class speedups refused
under an explicit extended-Church–Turing axiom; and the measurement trilemma
as an exact truth table (7 valuations, 1 excluded, 3 doors) with GRW timings
in exact rationals. The quartet also normalises a pattern Run D only
glimpsed — the *deliberate sorry as a boundary marker*: γ's arithmetic type,
α from premises, and the Everett emergence gap are open problems written
into the formal ledger instead of being hand-waved past.

**Audit results** (this paper's environment, Lean 4.35.0). The Python tier
transfers perfectly: all 24 Column-3 scripts re-verify in isolated
subprocesses, and 14/14 expected-value spot checks taken from the studies'
own reports (`PURITY=1/2`, `BREAKEVEN_N=55`, `INV_ALPHA_FLOOR=137`,
`REFUSAL_REGISTERED=1`, …) match exactly; ledger scans, cent-cost reductions
and classification identities all reproduce. The Lean tiers, however, do not
compile as shipped — on the toolchain their own `lean-toolchain` pins — for
the same three stacked reasons Run D documented independently: the Lake-4-era
scaffold lakefile (Lake 5.0 rejects it), the Mathlib-only ℕ/ℚ notations (47
occurrences, which pure core resolves as fresh type variables), and `decide`
on rationals (kernel-stuck). Each study reports "`lake build`: not run here;
project complete and ready"; the audit shows "ready" was untested and is
false on pure core. With the Run-D repairs (lakefile workaround, ℕ→`Nat`/
ℚ→`Rat`, `native_decide` fallback) all four projects build, each carrying
exactly its three named sorries as warnings — so their "proved" Lean counts
are compiler-checkable but not kernel-checked on pure core. The full audit
ships with the case-study record.

# 6. Why TCT: what the runs revealed""")

# 4 - section 6.12
edit(
"""rational. The Stern–Brocot search for the simplest rational inside the
bracket (267/85) is itself exact. The UBP does not forbid irrational answers;
it disciplines how they are reported.""",
"""rational. The Stern–Brocot search for the simplest rational inside the
bracket (267/85) is itself exact. The UBP does not forbid irrational answers;
it disciplines how they are reported.

**6.12 The Python tier transfers; the Lean tier does not — yet (the
quartet).** The four external case studies are the transfer test Runs A–D
could not be: authored independently of the experiment loop, on a third
platform, choosing their own questions. Their Python tiers reproduced
byte-for-byte and claim-for-claim on the audit machine — the §13 tooling,
the KEY=VALUE contract, the ledger discipline and the loop accounting all
travel. Their Lean tiers failed to compile as shipped, for exactly the three
reasons Run D had documented a day earlier on a different platform. The
protocol's split personality at distance: the executable half is robust
because it is self-verifying; the formal half is fragile because it makes
environment claims the skill asserts rather than probes. The deliberate
sorry as boundary marker (γ, α, the Everett gap) is the quartet's own
contribution to the method — the honest "we cannot, and here is the named
reason" carried into the formal record.""")

# 5 - section 7, gap 4
edit(
"""4. **Scaffold tooling drift.** The bundled `scaffold_lean_project.py` lakefile
   template is Lake-4-era; until §13 is updated, every user on a current
   toolchain needs Run D's named workaround. More generally, Run D shows the
   skill's environment claims (tactic availability, notation, constants)
   rot with the toolchain and should be phrased as *probe-first*: state the
   pattern, verify availability at run time, fall back with a named gap —
   exactly what Run D did.""",
"""4. **Scaffold tooling drift — confirmed at scale by the external case
   studies.** The bundled `scaffold_lean_project.py` lakefile template is
   Lake-4-era; until §13 is updated, every user on a current toolchain needs
   Run D's named workaround. All four external case studies inherited the
   failure verbatim — plus the ℕ/ℚ notation and decide-on-rationals issues —
   so their Lean tiers reported "ready" while not compiling on their own
   pinned toolchain. More generally, Run D and the quartet together show the
   skill's environment claims (tactic availability, notation, constants) rot
   with the toolchain and should be phrased as *probe-first*: state the
   pattern, verify availability at run time, fall back with a named gap —
   exactly what Run D did.""")

# 6 - conclusion sentence
edit(
"""lakefile template for current Lake.

# Artifacts""",
"""lakefile template for current Lake.

The four external case studies extend the assessment from experiment to
transfer: authored independently on a third platform, their Python tiers
reproduced exactly under audit while their Lean tiers failed to compile as
shipped for the same three reasons — the skill's executable half is robust
because it is self-verifying, and its formal half becomes robust the same
way, by probing instead of asserting.

# Artifacts""")

# 7 - artifacts paragraph
edit(
"""`results.log`), together with the environment probes (`lean_probe/`).""",
"""`results.log`), together with the environment probes (`lean_probe/`).

The external case-study record accompanies the paper:
`tct_case_studies.md` (the recorded studies and the full audit) and the four
quartet repositories as shipped, bundled with the audit logs
(`tier1_rerun.log`, `lean_build_audit.log`, `lean_build_repaired.log`,
`lean_build_native.log`) and the minimal-repair Lean copies under
`repaired/`.""")

# 8 - reference [5]
edit(
"""[4] Run D artifact bundle (this study): dola.com AI system, 1 Nov 2026 —
12 question directories (T01–T12) with Column-3 scripts, Lean specs and
built Lake projects (Lean 4.35.0 / Lake 5.0.0), optimization-loop
decompositions, and per-question TCT payloads; plus environment probes and
run logs.""",
"""[4] Run D artifact bundle (this study): dola.com AI system, 1 Nov 2026 —
12 question directories (T01–T12) with Column-3 scripts, Lean specs and
built Lake projects (Lean 4.35.0 / Lake 5.0.0), optimization-loop
decompositions, and per-question TCT payloads; plus environment probes and
run logs.

[5] External case-study quartet (aistudio.xiaomimimo.com, 2026), recorded
and audited in `tct_case_studies.md`: `famous-constants-tct`,
`speed-of-light-derivation-tct`, `physical-isomorphisms-tct`,
`maudlin-measurement-trilemma-tct` — four self-authored TCT repositories
(88 claims = 49+12+25+2) with byte-identical §13 tooling, re-verified
Python tiers, and Lean tiers compiled here for the first time (as shipped:
failing; with named repairs: 4/4 building, 3 named sorries each).""")


def main():
    text = open(PAPER, encoding="utf-8").read()
    for i, (old, new) in enumerate(EDITS, 1):
        if old not in text:
            print(f"EDIT {i}: OLD STRING NOT FOUND")
            return 1
        if text.count(old) != 1:
            print(f"EDIT {i}: OLD STRING NOT UNIQUE ({text.count(old)})")
            return 1
        text = text.replace(old, new)
    with open(PAPER, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"applied {len(EDITS)} edits; paper now {len(text.splitlines())} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
