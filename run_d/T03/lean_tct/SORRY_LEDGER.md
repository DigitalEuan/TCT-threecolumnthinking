# Development-required ledger — tct_T03

- lemmas total: 5
- proved (sorry-free): **4**
- `sorry` (development required): **1**
- axioms: **5**
- definitions: 0

## sorry lemmas

- `general_free_fall_symbolic` : `∀ (g t : Nat), g > 0 → 0 < g * t * t`
  - gap: needs Mathlib order reasoning (linarith) or manual calc

## axioms (assumed)

- `newton_gravity_law` : `Prop` — F = GmM/r^2 (named premise)
- `gravity_earth_value` : `Prop` — g = 49/5 m/s^2 (illustrative)
- `kinematic_relations_premise` : `Prop` — v = gt, h = gt^2/2, v^2 = 2gh
- `free_fall_premise` : `Prop` — drop from rest, no drag
- `mass_independence_premise` : `Prop` — free-fall acceleration independent of mass

## To verify

```bash
cd /home/z/my-project/tct_run_d/T03/lean_tct && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
