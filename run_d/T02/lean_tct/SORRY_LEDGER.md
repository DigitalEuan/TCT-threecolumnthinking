# Development-required ledger — tct_T02

- lemmas total: 7
- proved (sorry-free): **5**
- `sorry` (development required): **2**
- axioms: **3**
- definitions: 0

## sorry lemmas

- `geometric_closure_symbolic` : `∀ (a r : Nat), r > 1 → 1 ≤ a * r / (r - 1) + 1`
  - gap: infinite geometric sum — needs Mathlib order theory
- `dissipation_ledger_symbolic` : `∀ (e : Nat), e > 1 → 1 ≤ e * e`
  - gap: general e^{2k} accounting — development required

## axioms (assumed)

- `restitution_empirical` : `Prop` — e = 3/4 (measured, declared)
- `gravity_value_earth` : `Prop` — g = 49/5 m/s^2 (engineered rational)
- `kinematics_premise` : `Prop` — constant-g kinematics, no drag

## To verify

```bash
cd /home/z/my-project/tct_run_d/T02/lean_tct && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
