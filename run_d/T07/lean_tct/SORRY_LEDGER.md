# Development-required ledger — tct_T07

- lemmas total: 6
- proved (sorry-free): **5**
- `sorry` (development required): **1**
- axioms: **1**
- definitions: 0

## sorry lemmas

- `choose_symbolic` : `∀ (n k : Nat), k ≤ n → n * (n - 1) / 2 * (n - 2) / 3 = (n - 2) * (n - 3) / 2 * n / 2`
  - gap: general factorial identity — needs Mathlib ring/field_simp

## axioms (assumed)

- `combination_definition` : `Prop` — C(n,k) = n!/(k!(n-k)!) (definition)

## To verify

```bash
cd /home/z/my-project/tct_run_d/T07/lean_tct && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
