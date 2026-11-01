# Development-required ledger — tct_T01

- lemmas total: 8
- proved (sorry-free): **6**
- `sorry` (development required): **2**
- axioms: **3**
- definitions: 0

## sorry lemmas

- `energy_exchange_symbolic` : `∀ (k m x : Nat), x > 0 → k * x * x / (2 * m) * m = k * x * x / 2`
  - gap: needs Mathlib order reasoning (linarith) or manual calc
- `damped_loop_bound` : `∀ n : Nat, n > 0 → 1 ≤ 3 ^ n / 4 ^ n + 1`
  - gap: geometric decay bound — development required

## axioms (assumed)

- `hooke_law` : `Prop` — F = kx (Hooke, empirical)
- `si_units_premise` : `Prop` — k = 100 N/m, x0 = 1/5 m, m = 1 kg (illustrative givens)
- `energy_exchange_premise` : `Prop` — elastic PE <-> KE, no dissipation

## To verify

```bash
cd /home/z/my-project/tct_run_d/T01/lean_tct && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
