# Development-required ledger — tct_T08

- lemmas total: 5
- proved (sorry-free): **4**
- `sorry` (development required): **1**
- axioms: **1**
- definitions: 0

## sorry lemmas

- `geometric_growth_symbolic` : `∀ (p : Nat), p * 21 * 21 * 21 = p * 9261 * 1 * 1 * 1 + (p * 21 * 21 * 21 - p * 9261)`
  - gap: general growth identity — needs ring (absent in core)

## axioms (assumed)

- `compound_interest_definition` : `Prop` — A = P(1+r)^n (definition), P=100, r=1/20, n=3

## To verify

```bash
cd /home/z/my-project/tct_run_d/T08/lean_tct && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
