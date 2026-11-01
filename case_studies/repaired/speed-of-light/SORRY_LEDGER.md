# Development-required ledger — tct_lightcone

- lemmas total: 8
- proved (sorry-free): **5**
- `sorry` (development required): **3**
- axioms: **7**
- definitions: 3

## sorry lemmas

- `lr_bound_nonneg` : `∀ (J a : ℚ), 0 ≤ J → 0 ≤ a → 0 ≤ 2*J*a`
  - gap: requires positivity reasoning (Mathlib mul_nonneg/positivity) or manual case analysis; symbolic content of the Lieb-Robinson velocity computed concretely in scripts/column3/05_lr_bound.py
- `inv_alpha_interval_general` : `∀ (α lo hi : ℚ), 0 < lo → lo ≤ α → α ≤ hi → 1/hi ≤ 1/α ∧ 1/α ≤ 1/lo`
  - gap: requires field_simp + order reasoning (Mathlib) or manual cross-multiplication with positivity; general shape of the uncertainty inversion verified concretely in scripts/column3/06_alpha_boundary.py
- `alpha_from_premises` : `∀ (α : ℚ), α = 72973525693 / 10^13`
  - gap: DELIBERATE TARGET, EXPECTED UNPROVEN: a parameter-free derivation of the fine-structure constant (equivalently, of c's dimensionless value) from theory alone. No accepted derivation exists; numerology-class claims (Eddington lineage and modern preprints) are registered WOULD_BE_GUESS in the ledgers. Keeping this sorry is the formal boundary of the study: everything else about c is derivable, this is not

## axioms (assumed)

- `si_definition_c` : `Prop` — definitional (BIPM SI): c = 299,792,458 m/s exactly; the meter is defined from c (1983/2019). Computing this number is unit bookkeeping, not derivation
- `maxwell_em_wave_speed` : `Prop` — empirical law (Maxwell 1865): electromagnetic waves propagate at 1/sqrt(mu0*eps0); identifying this with optical speed is the historical derivation of c as an EM quantity
- `historical_determinations_empirical` : `Prop` — empirical: Weber-Kohlrausch 1856 (310,740,000 m/s), Fizeau 1849 (313,300,000), Foucault 1862 (298,000,000) are measured/computed determinations
- `ignatowski_premises` : `Prop` — premises (von Ignatowski 1910): relativity principle + homogeneity + isotropy + causality imply a linear coordinate law containing an invariant speed
- `lieb_robinson_theorem` : `Prop` — rigorous theorem (Lieb-Robinson 1972): commutator propagation in lattice systems is bounded by v = 2Ja; modeling premise: such Hamiltonians describe physical signal propagation
- `alpha_empirical` : `Prop` — empirical (CODATA 2018): alpha = 7.2973525693(11) x 10^-3; the fine-structure constant is MEASURED, not derived
- `wave_scheme_represents_wave` : `Prop` — modeling premise: the integer scheme u_{t+1}(x) = u_t(x+1) + u_t(x-1) - u_{t-1}(x) faithfully discretizes u_tt = c^2 u_xx at c = 1, dx = dt = 1

## To verify

```bash
cd lean/tct_lightcone && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
