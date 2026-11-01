# Deriving the Speed of Light Computationally — a Three Column Thinking (TCT) study

**Question:** "how can the speed of light be derived computationally?" — a
question built to cause issues. It caused four, one per hidden sub-question,
and this repository faces each as it comes.

## The answer

**Structure is derivable — exactly, three independent ways. The value is
measured (α) or defined (SI). The naive claim is refused, on the record.**

| Boundary | Sub-question | Result |
|---|---|---|
| B1 | compute the number 299,792,458? | trivially — it is **defined** (SI); bookkeeping stamped `DEFINITIONAL=1` |
| B2 | derive that light's speed is the *EM* speed? | yes — historically done (Weber–Kohlrausch 1856 vs. Fizeau/Foucault); exact comparisons, ≤ 5% era agreement |
| B3 | derive that an **invariant speed exists**? | yes — wave-scheme cone (edge speed exactly 1/step), Clifford-circuit cone (≤ 1 site/layer, exact GF(2)), Lieb–Robinson bound v = 2Ja (tight, matching both), Ignatowski (causality ⇒ κ ≥ 0) |
| B4 | derive the **dimensionless value** (α) from theory? | **no — open problem.** `REFUSED: WOULD_BE_GUESS` for any claim; the Lean tier carries `alpha_from_premises` as a deliberate `sorry` — the boundary made formal |

Three unrelated formalisms (PDE numerics, Clifford group dynamics, operator
algebra bounds) compute *the same cone* and agree exactly — that coincidence
is the study's deepest verified result. The one thing everyone wants ("the
number, from pure computation") is the one thing the ledger formally denies.

## Repository layout

```
README.md                          ← this file
docs/
  01-overview.md                   ← the four boundaries, the two-part answer
  02-decomposition.md              ← 22 claims (22 = 11+3+7+1)
  03-three-columns.md              ← synchronised three-column contract
  04-derivation-map.md             ← four routes: what each derives, what not
  05-boundaries-and-refusals.md    ← every issue hit + disposition; refusal register
  06-cent-compiler.md              ← £ → ¢ → ∆ run (transmission line / water hammer / string)
  07-optimization-loop.md          ← ¢ cost 10→7, witnesses preserved
  08-references.md                 ← Maxwell, Weber-Kohlrausch, Ignatowski, Lieb-Robinson…
scripts/
  verify_column3.py / scaffold_lean_project.py / lean_ledger.py / cent_cost.py
                                   ← TCT §13 bundled scripts (verbatim)
  column3/
    01_si_definition.py            ← definitional chain, exact (stamped bookkeeping)
    02_em_determinations.py        ← historical determinations, exact comparisons
    03_wave_cone.py                ← integer wave scheme: light cone by enumeration
    04_clifford_cone.py            ← exact GF(2) Clifford dynamics: cone, 2 paths
    05_lr_bound.py                 ← Lieb-Robinson v = 2Ja; cross-framework tightness
    06_alpha_boundary.py           ← 1/α exactly; THE refusal registered here
lean/
  spec.json                        ← lemma spec (incl. deliberate alpha_from_premises)
  tct_lightcone/                   ← Lean 4 Lake project (5 proved, 3 sorry, 7 axioms)
ledgers/
  classification-ledger.md         ← four ledgers + cross-check register
  insights.md                      ← what the decomposition buys
cent/
  decomp_v1.json / decomp_v2.json  ← optimization-loop artifacts
verification/
  VERIFICATION_REPORT.md           ← Tier 1 + Tier 2 status
  tier1-run.txt                    ← full KEY=*** output of all six scripts
```

## Re-verify (Python 3 stdlib only; no installs)

```bash
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_lightcone --build    # builds if `lake` installed
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```

## Status

- **Tier 1 (Python):** 6/6 VERIFIED, isolated subprocesses (asserts corrected
  two draft constants — documented).
- **Tier 2 (Lean):** 5 proved, **3 sorry** (one deliberate: `alpha_from_premises`),
  7 named axioms. `lake build` not run here (no toolchain); ready.
- **Refusals:** 1 (`WOULD_BE_GUESS`, the naive value claim) + 3 qualified/
  refused dispositions in docs/05's register.
- **Open:** parameter-free derivation of α; digital-physics value claims
  (contested); quantum-relativistic unification beyond scope.

Method: Three Column Thinking (TCT) — Geometric Language Machine (GLM),
E. R. A. Craig (DigitalEuan), https://github.com/DigitalEuan/GLM.
Companion studies: `maudlin-measurement-trilemma-tct/` (QM foundations),
`physical-isomorphisms-tct/` (physical→computational gains).
