# Development-required ledger — tct_physiso

- lemmas total: 12
- proved (sorry-free): **9**
- `sorry` (development required): **3**
- axioms: **6**
- definitions: 4

## sorry lemmas

- `break_even_symbolic` : `∀ (N : ℚ), 0 < N → (2*N^2 + 7400*N < 138*N^2 ↔ 7400 < 136*N)`
  - gap: requires ring/field_simp/linarith (Mathlib) or a manual calc with positivity side-goals; symbolic form of the break-even computation verified concretely in scripts/column3/01_crossbar_break_even.py
- `euler_error_general` : `∀ (M : ℕ), 0 < M → (1:ℚ) - ((M-1)*(2*M-1) / (2*M^2)) = (3*M-1) / (2*M^2)`
  - gap: requires field_simp + ring with ℕ-to-ℚ cast bookkeeping (Mathlib) or a manual calc; general form of the error identity checked for M = 1..20 in scripts/column3/04_analog_ode.py
- `stochastic_n_required` : `∀ (n : ℕ), (1:ℚ)/4/n ≤ (1/100)^2 → 2500 ≤ n`
  - gap: requires linarith/field_simp over ℚ with positivity (Mathlib) or manual cross-multiplication; this is the MINIMALITY claim for the stream length (equality instance proved in chebyshev_2500)

## axioms (assumed)

- `horowitz_energies_empirical` : `Prop` — empirical (Horowitz, ISSCC 2014, 45nm-class): 32b FP multiply 3.7 pJ, 32b add 0.1 pJ, 32b SRAM read 5 pJ, 32b DRAM read 640 pJ
- `crossbar_model_empirical` : `Prop` — empirical/illustrative: analog crossbar cell compute ~ 0.2 pJ per MAC-equivalent; DAC/ADC conversion ~ 370 pJ each (converter overhead is the known crossbar limitation)
- `analog_offset_model_empirical` : `Prop` — illustrative: a physical analog integrator holds a fixed offset error floor of 1/1000
- `noise_bernoulli_empirical` : `Prop` — empirical: a noisy physical bit source samples independent Bernoulli trials (stochastic computing premise)
- `ising_relaxation_empirical` : `Prop` — empirical: a physical Ising system relaxes preferentially toward low-energy configurations (annealing premise)
- `physical_church_turing` : `Prop` — premise (extended Church-Turing thesis): physical systems are efficiently simulable by digital computers, so physical isomorphisms change constants and latency, not complexity classes; the quantum case (BQP vs BPP) remains OPEN and is not claimed

## To verify

```bash
cd lean/tct_physiso && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
