# Famous Constants from First Principles — a Three Column Thinking (TCT) study

**Question:** "how can the famous mathematical constants be derived from first
principles?" — basic set, advanced family, the Fine Structure Constant and
more. The answer is not a list of formulas; it is a **coastline**:

| Class | Meaning | Members | Status |
|---|---|---|---|
| **D** definitional | definition + algorithm + exact certificate | π, e, φ, √2, Champernowne | fully derivable ✓ |
| **T** theorem-pinned | a theorem fixes the value; series compute it | ln 2, ζ(2)=π²/6, ζ(4)=π⁴/90, ζ(3) (Apéry), e^π (Gelfond–Schneider) | derivable ✓ |
| **O** open | computable to any precision; no closed form | **γ** (Erdős prize!), ζ(5), Catalan's closure, ζ(3)'s closure | boundary |
| **U** uncomputable | definable; digits algorithmically impossible | Chaitin's Ω | derivable ≠ computable |
| **P** physical | measured / unit-defined | **α** (fine structure), G, c/h | **REFUSED** (trilogy link) |

## The verified fun

- **π by three independent derivations** — Machin, Euler's arctan identity,
  BBP — overlapping rigorous rational intervals, widths < 10⁻²⁵, shared
  13-digit block, double-path certified.
- **e** two summation paths + exact factorial tail; **φ** with exact Cassini
  certificates `F_{n+1}² − F_n F_{n+2} = (−1)ⁿ`; **√2** via integer isqrt
  *and* Pell certificates `p² − 2q² = ±1`.
- **Basel and friends**: ζ(2) = π²/6, ζ(4) = π⁴/90 sandwiched by partial sums
  with telescoping/integral tails.
- **ln 2** by two genuinely different series whose intervals must overlap;
  **Catalan** with alternating certificates.
- **γ** bracketed two independent ways — and stamped
  `GAMMA_IRRATIONALITY=UNKNOWN`: the famous open wall.
- **Ω** on the catalog as the constant that separates "derivable" from
  "computable" — the punchline of the whole question.
- **α** refused, unchanged from the speed-of-light study:
  `REFUSED: WOULD_BE_GUESS`, formal record in the Lean ledger.

Every claim is double-path verified over ℚ/ℤ (no floats, no randomness);
the assert layer caught five defects mid-build — including one in the witness
method itself (documented in `verification/VERIFICATION_REPORT.md`).

## Repository layout

```
README.md                          ← this file
docs/
  01-overview.md                   ← the five classes; the two walls
  02-decomposition.md              ← 24 claims (24 = 13+3+7+1)
  03-three-columns.md              ← synchronised three-column contract
  04-constant-catalog.md           ← basic set / advanced family / far shore
  05-first-principles-ladder.md    ← what "derivation" means per class;
                                     open problems; numerology guardrail
  06-cent-compiler.md              ← £ → ¢ → ∆ run (constants in physics)
  07-optimization-loop.md          ← ¢ cost 9→6 + tautology/defect audit
  08-references.md                 ← Machin, Euler, Apéry, Gelfond, Chaitin…
scripts/
  verify_column3.py / scaffold_lean_project.py / lean_ledger.py / cent_cost.py
                                   ← TCT §13 bundled scripts (verbatim)
  column3/
    01_pi_convergents.py           ← π × 3 derivations, exact intervals
    02_e_phi_sqrt2.py              ← e, φ (Cassini), √2 (Pell)
    03_zeta2_basel.py              ← ζ(2), ζ(4) tail sandwiches
    04_ln2_catalan.py              ← ln 2 two series; Catalan
    05_gamma_open.py               ← γ two constructions; OPEN stamp
    06_taxonomy.py                 ← Champernowne; D/T/O/U/P machine; α refusal
lean/
  spec.json                        ← lemma spec (2 deliberate boundary sorries)
  tct_constants/                   ← Lean 4 Lake project (6 proved, 3 sorry, 7 axioms)
ledgers/
  classification-ledger.md         ← four ledgers + cross-check register
  insights.md                      ← what the stratification buys
cent/
  decomp_v1.json / decomp_v2.json  ← optimization-loop artifacts
verification/
  VERIFICATION_REPORT.md           ← Tier 1 + Tier 2 status + defect log
  tier1-run.txt                    ← full KEY=*** output of all six scripts
```

## Re-verify (Python 3 stdlib only; no installs)

```bash
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_constants --build    # builds if `lake` installed
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```

## Status

- **Tier 1 (Python):** 6/6 VERIFIED, isolated subprocesses.
- **Tier 2 (Lean):** 6 proved, **3 sorry** (2 deliberate: `gamma_rational_target`,
  `alpha_physical_target`), 7 named axioms. `lake build` not run here; ready.
- **Refusals:** 1 (`WOULD_BE_GUESS` — physical constants from first
  principles), guardrail armed (docs/05).
- **Open, kept open:** γ's arithmetic type, ζ(5), Catalan/ζ(3) closure, α.

Method: Three Column Thinking (TCT) — Geometric Language Machine (GLM),
E. R. A. Craig (DigitalEuan), https://github.com/DigitalEuan/GLM.
Quartet: `maudlin-measurement-trilemma-tct/`, `physical-isomorphisms-tct/`,
`speed-of-light-derivation-tct/`, `famous-constants-tct/`.
