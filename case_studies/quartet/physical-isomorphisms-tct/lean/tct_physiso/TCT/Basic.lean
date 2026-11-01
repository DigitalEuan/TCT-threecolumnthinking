namespace TCT

def per_mac_vn : ℕ := 12838
def cell_energy : ℕ := 2
def conv_energy : ℕ := 3700
def ops_fft : ℕ := 51200

axiom horowitz_energies_empirical : Prop
-- assumed premise: empirical (Horowitz, ISSCC 2014, 45nm-class): 32b FP multiply 3.7 pJ, 32b add 0.1 pJ, 32b SRAM read 5 pJ, 32b DRAM read 640 pJ
axiom crossbar_model_empirical : Prop
-- assumed premise: empirical/illustrative: analog crossbar cell compute ~ 0.2 pJ per MAC-equivalent; DAC/ADC conversion ~ 370 pJ each (converter overhead is the known crossbar limitation)
axiom analog_offset_model_empirical : Prop
-- assumed premise: illustrative: a physical analog integrator holds a fixed offset error floor of 1/1000
axiom noise_bernoulli_empirical : Prop
-- assumed premise: empirical: a noisy physical bit source samples independent Bernoulli trials (stochastic computing premise)
axiom ising_relaxation_empirical : Prop
-- assumed premise: empirical: a physical Ising system relaxes preferentially toward low-energy configurations (annealing premise)
axiom physical_church_turing : Prop
-- assumed premise: premise (extended Church-Turing thesis): physical systems are efficiently simulable by digital computers, so physical isomorphisms change constants and latency, not complexity classes; the quantum case (BQP vs BPP) remains OPEN and is not claimed

theorem ratio_vn_exact : (12838 : ℚ) / 2 = 6419 := by
  decide

theorem ratio_inmem_exact : (138 : ℚ) / 2 = 69 := by
  decide

theorem breakeven_55 : (2*55^2 + 7400*55 < 138*55^2) ∧ (2*54^2 + 7400*54 ≥ 138*54^2) := by
  decide

theorem breakeven32_228 : (8*228^2 + 29600*228 < 138*228^2) ∧ (8*227^2 + 29600*227 ≥ 138*227^2) := by
  decide

theorem fft_ratio : (1024^2 : ℚ) / (5*1024*10) = 512/25 := by
  decide

theorem breakeven_t_21 : (51200*21 ≥ 1048576 + 1025*21) ∧ (51200*20 < 1048576 + 1025*20) := by
  decide

theorem euler_error_10 : (3*10 - 1 : ℚ) / (2*10^2) = 29/200 := by
  decide

theorem m_min_1500 : (1000*(3*1500 - 1) ≤ 2*1500^2) ∧ (1000*(3*1499 - 1) > 2*1499^2) := by
  decide

theorem chebyshev_2500 : ((1:ℚ)/4) / ((1/100)^2) = 2500 := by
  decide

theorem break_even_symbolic : ∀ (N : ℚ), 0 < N → (2*N^2 + 7400*N < 138*N^2 ↔ 7400 < 136*N) := by
  sorry
  -- GAP: requires ring/field_simp/linarith (Mathlib) or a manual calc with positivity side-goals; symbolic form of the break-even computation verified concretely in scripts/column3/01_crossbar_break_even.py

theorem euler_error_general : ∀ (M : ℕ), 0 < M → (1:ℚ) - ((M-1)*(2*M-1) / (2*M^2)) = (3*M-1) / (2*M^2) := by
  sorry
  -- GAP: requires field_simp + ring with ℕ-to-ℚ cast bookkeeping (Mathlib) or a manual calc; general form of the error identity checked for M = 1..20 in scripts/column3/04_analog_ode.py

theorem stochastic_n_required : ∀ (n : ℕ), (1:ℚ)/4/n ≤ (1/100)^2 → 2500 ≤ n := by
  sorry
  -- GAP: requires linarith/field_simp over ℚ with positivity (Mathlib) or manual cross-multiplication; this is the MINIMALITY claim for the stream length (equality instance proved in chebyshev_2500)

end TCT
