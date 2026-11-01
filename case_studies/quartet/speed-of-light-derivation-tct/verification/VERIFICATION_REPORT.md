# VERIFICATION REPORT

Tier 1 (Python) and Tier 2 (Lean) status for the speed-of-light derivation
study. Method: TCT (Geometric Language Machine), UBP discipline, cent mode.

## Tier 1 — Python, isolated subprocess (`scripts/verify_column3.py`)

All six Column 3 scripts run in fresh subprocesses, exit 0.

| # | Script | Key checked | Expected | Result |
|---|---|---|---|---|
| 01 | `01_si_definition.py` | `DEFINITIONAL` | `1` | VERIFIED |
| 02 | `02_em_determinations.py` | `ERAS_AGREE` | `1` | VERIFIED |
| 03 | `03_wave_cone.py` | `CONE_BOUND` | `1` | VERIFIED |
| 04 | `04_clifford_cone.py` | `CONE_BOUND` | `1` | VERIFIED |
| 05 | `05_lr_bound.py` | `FRAMEWORKS_MATCH` | `1` | VERIFIED |
| 06 | `06_alpha_boundary.py` | `INV_ALPHA_FLOOR` | `137` | VERIFIED |

Full `KEY=*** output: `verification/tier1-run.txt`.

Notable exact values (ℤ/ℚ only, no floats):
- light-year = 9,460,730,472,580,800 m (definitional chain)
- historical deltas: WK 5473771/149896229 (36,517 ppm);
  Fizeau 6753771/149896229 (45,056 ppm); Foucault 896229/149896229 (5,978 ppm)
- wave cone: edge speed exactly 1 cell/step; SUPPORT_T20 = 19 (= t−1)
- Clifford cone: label-rules ≡ GF(2) symplectic; growth ≤ 1 site/layer
- LR bound: v = 2Ja = 1 (J = 1/2) — tight over both cones; 3/2 at J = 3/4
- α⁻¹ = 10¹³/72973525693 (floor 137), exact uncertainty width
- boundary stamps: `ALPHA_FROM_THEORY=0`, `REFUSAL_REGISTERED=1`

Assert-layer notes: two draft hand-constants were corrected by failing asserts
(ppm floors 45056/5978; see scripts) — the witness discipline did its job.

## Tier 2 — Lean (`lean/tct_lightcone/`, scaffolded from `lean/spec.json`)

- Proved (sorry-free): **5**
- `sorry` (development required): **3**
  - `lr_bound_nonneg` — gap: positivity (`mul_nonneg`, Mathlib)
  - `inv_alpha_interval_general` — gap: `field_simp` + order reasoning
  - `alpha_from_premises` — **deliberate target, expected unproven**: the
    parameter-free derivation of α; the study's formal boundary
- Axioms (named premises): **7**
- Definitions: 3
- `lake build`: **not run** — `lake` not on PATH here; project complete and
  ready: `cd lean/tct_lightcone && lake build`.

## Optimization loop (docs/07)

- ¢ cost: 10 → 7 primitives (iteration 1 accepted; iteration 2 rejected).
- Cross-checks: 14 written, 13 live after dead-artifact removal.

## How to re-verify

```bash
cd speed-of-light-derivation-tct
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_lightcone --build   # builds if lake present
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```
