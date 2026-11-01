# Development-required ledger — tct_T10

- lemmas total: 5
- proved (sorry-free): **4**
- `sorry` (development required): **1**
- axioms: **3**
- definitions: 0

## sorry lemmas

- `area_formula_symbolic` : `∀ (r : Nat), r > 0 → 0 < 3 * r * r`
  - gap: needs Mathlib order reasoning or manual calc

## axioms (assumed)

- `pi_definition` : `Prop` — pi = circle constant (definitional; core Lean cannot name Real.pi)
- `area_formula_premise` : `Prop` — A = pi r^2, r = 1 m
- `classical_bracket_premise` : `Prop` — 223/71 < pi < 22/7 (Archimedes 96-gon)

## To verify

```bash
cd /home/z/my-project/tct_run_d/T10/lean_tct && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
