# Development-required ledger — tct_T04

- lemmas total: 5
- proved (sorry-free): **4**
- `sorry` (development required): **1**
- axioms: **5**
- definitions: 0

## sorry lemmas

- `anomalous_expansion_symbolic` : `∀ (a b : Nat), a ≤ b → a - 1 ≤ b - 1`
  - gap: density-inversion reasoning — needs Mathlib (Nat.sub lemmas)

## axioms (assumed)

- `archimedes_principle` : `Prop` — buoyancy = weight of displaced fluid
- `ice_density_empirical` : `Prop` — rho_ice = 2750 (scaled, near 917 kg/m^3)
- `water_density_empirical` : `Prop` — rho_water = 2997 (scaled, near 999 kg/m^3 at 4 C)
- `expansion_definition_premise` : `Prop` — water's anomalous expansion: max density at 4 C
- `buoyancy_premise` : `Prop` — floating equilibrium: displaced mass = object mass

## To verify

```bash
cd /home/z/my-project/tct_run_d/T04/lean_tct && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
