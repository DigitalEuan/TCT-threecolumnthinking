# VERIFICATION REPORT

Tier 1 (Python) and Tier 2 (Lean) status for the physical-isomorphism study.
Method: TCT (Geometric Language Machine), UBP discipline, cent cross-domain mode.

## Tier 1 — Python, isolated subprocess (`scripts/verify_column3.py`)

All six Column 3 scripts run in fresh subprocesses, exit 0.

| # | Script | Key checked | Expected | Result |
|---|---|---|---|---|
| 01 | `01_crossbar_break_even.py` | `BREAKEVEN_N` | `55` | VERIFIED |
| 02 | `02_convolution_amortization.py` | `BREAKEVEN_T` | `21` | VERIFIED |
| 03 | `03_stochastic_streams.py` | `N_FOR_1PCT` | `2500` | VERIFIED |
| 04 | `04_analog_ode.py` | `M_MIN` | `1500` | VERIFIED |
| 05 | `05_primitives_catalog.py` | `MIN_DOMAINS` | `2` | VERIFIED |
| 06 | `06_sat_ising.py` | `EQUIVALENCE` | `1` | VERIFIED |

Full `KEY=*** output: `verification/tier1-run.txt`.

Notable exact values (ℚ/ℤ only, no floats):
- energy per MAC-equivalent: 6419× (von Neumann), 69× (in-memory)
- crossbar break-even: N = 55 (8-bit converters), N = 228 (32-bit, 4 passes)
- convolution: direct/FFT = 512/25; optical break-even reuse T = 21
- stochastic: exact tail (two-path) ≤ 1/4; 1% error needs N ≥ 2500 bits
- analog ODE: error (3M−1)/(2M²); e(10) = 29/200; M = 1500 steps to floor
- catalog: 12 primitives × 8 domains, 40 realizations (37 licensed / 3 conjectural)
- SAT→Ising: satisfy ⟺ E = 0 on all 8 assignments; 6 satisfying; cubic terms present

Note: an assertion layer in script 01 caught a hand-arithmetic error in a
commented constant during development (12838/2 = 6419, not 6409) —
documentation corrected to match the verified value.

## Tier 2 — Lean (`lean/tct_physiso/`, scaffolded from `lean/spec.json`)

- Proved (sorry-free): **9**
- `sorry` (development required): **3**
  - `break_even_symbolic` — gap: `ring`/`linarith` (Mathlib) or manual calc
  - `euler_error_general` — gap: `field_simp`/`ring` with cast bookkeeping
  - `stochastic_n_required` — gap: positivity/`linarith` (minimality claim)
- Axioms (named premises): **6** — incl. `physical_church_turing` (ECT;
  quantum case explicitly open and unclaimed)
- Definitions: 4
- `lake build`: **not run** — `lake` not on PATH here; project complete and
  ready: `cd lean/tct_physiso && lake build`.

## Optimization loop (docs/07)

- ¢ cost: 11 → 7 primitives (iteration 1 accepted; iteration 2 rejected as a
  lost witness).
- Cross-checks: 17 written, 16 live after dead-artifact removal.

## How to re-verify

```bash
cd physical-isomorphisms-tct
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_physiso --build      # builds if lake present
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```
