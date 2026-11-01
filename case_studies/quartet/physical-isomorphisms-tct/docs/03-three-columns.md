# 03 — The three-column contract

The three columns describe the **identical logical steps**. Domain: ℚ / ℤ
throughout. UBP: Column 3 uses `fractions.Fraction`/`int`/`math.comb` only —
no floats, no rounding, no random, no SHA-256, stdlib only.

**Givens.** Horowitz energies in 0.1 pJ units (mult 37, add 1, SRAM 50, DRAM
6400); crossbar cell 2, conversion 3700; N = 1024; stream N = 100, p = 1/2;
analog floor 1/1000; 3-SAT instance C1 = (x1 ∨ ¬x2 ∨ x3), C2 = (¬x1 ∨ x2 ∨ x3).

| Step | Plain English | Mathematics | Python (this step) | Lean |
|---|---|---|---|---|
| 1 | the per-operation cost of a von-Neumann digital MAC | 37 + 1 + 2·6400 = 12838 | 01: `per_mac_vn` | `per_mac_vn := 12838` (def) |
| 2 | the per-operation cost of an in-memory digital MAC | 37 + 1 + 2·50 = 138 | 01: `per_mac_inmem` | — |
| 3 | the energy ratio of digital to physical per MAC-equivalent | 12838/2 = 6419; 138/2 = 69 | 01: `RATIO_VN`, `RATIO_INMEM` | `ratio_vn_exact`, `ratio_inmem_exact` (proved) |
| 4 | the analog cost of one matrix-vector product | 2N² + 7400N | 01: `analog_cost` | — |
| 5 | the break-even size against in-memory digital | 2N² + 7400N < 138N² ⟺ N > 925/17 | 01: closed + enumeration, `BREAKEVEN_N=55` | `breakeven_55` (proved); `break_even_symbolic` (sorry) |
| 6 | the same at 32-bit effective precision | 4 passes: N > 2960/13 | 01: `BREAKEVEN_N_32BIT=228` | `breakeven32_228` (proved) |
| 7 | the latency of one matrix-vector product, physical vs. digital | N²/(2N+1) = 65536/513 at N = 256 | 01: `LATENCY_RATIO_N256` | — |
| 8 | the operation counts for convolution | N² = 1048576 vs. 5N log₂N = 51200 | 02: `OPS_DIRECT`, `OPS_FFT` | — |
| 9 | the exact ratio of the two counts | 1048576/51200 = 512/25 | 02: `RATIO_DIRECT_FFT` | `fft_ratio` (proved) |
| 10 | the amortized optical cost over T frames | N² + T(N+1) vs. T·51200 | 02: `optical_total`, `fft_total` | — |
| 11 | the smallest reuse count at which optics wins | T ≥ 1048576/50175 ⟹ T = 21 | 02: closed + enumeration, `BREAKEVEN_T=21` | `breakeven_t_21` (proved) |
| 12 | the exact probability that 100 coin-flip bits miss 1/2 by 0.1 | Σ C(100,k)/2¹⁰⁰ = tail (two paths agree) | 03: `TAIL_EXACT` | — |
| 13 | the Chebyshev upper bound on that tail | p(1−p)/(Nε²) = 1/4 | 03: `CHEBYSHEV`, `CHEBYSHEV_OK` | — |
| 14 | the stream length needed for 1% error | N ≥ p(1−p)/ε² = 2500 (minimal) | 03: `N_FOR_1PCT` | `chebyshev_2500` (proved); `stochastic_n_required` (sorry: minimality) |
| 15 | where stochastic multiplication stops paying | w² > N ⟹ w = 11 | 03: `CROSSOVER_WIDTH` | — |
| 16 | the exact Euler error for the ODE y′ = 3t² | e_M = (3M−1)/(2M²); e₁₀ = 29/200 | 04: `FORMULA_MATCH`, `ERROR_M10` | `euler_error_10` (proved); `euler_error_general` (sorry) |
| 17 | the digital steps to match the analog error floor | (3M−1)/(2M²) ≤ 1/1000 ⟹ M ≥ 1500 | 04: `M_MIN=1500` | `m_min_1500` (proved) |
| 18 | the physical-isomorphism gain in integration steps | 1500 digital : 1 analog (at declared floor) | 04: `STEP_RATIO` | — |
| 19 | the license condition of the analogy catalog | 12 primitives, each in ≥ 2 domains | 05: `MIN_DOMAINS=2`, `LICENSED=37` | — |
| 20 | the exactness of the SAT → energy mapping | satisfy ⟺ E = 0 on all 8 assignments | 06: `EQUIVALENCE=1` | — |
| 21 | the cost of that mapping | 2 clauses × 8 slots = 16 ≤ 6 surviving monomials, cubic present | 06: `TERMS_EXPANDED=6`, `CUBIC_TERMS_PRESENT=1` | — |
| 22 | the guardrail: structure-preserving maps change constants, not classes | ECT premise; quantum case open | — | `physical_church_turing` (axiom, not claimed) |

**UBP compliance.** `Fraction`/`int` only; no floats, no random, no SHA-256;
no XOR sites; stdlib only. All break-even claims are closed inequalities over
ℤ/ℚ, verified by both closed form and enumeration.

**Decomposition.** 22 atomic claims: 13 proved, 3 sorry, 6 axioms, 0 refused
(docs/02).

**Full Column 3 scripts:** `scripts/column3/01…06_*.py`; full outputs
`verification/tier1-run.txt`.

**Verification.** Python: **VERIFIED** — 6/6 scripts, isolated subprocess.
**Lean:** 9 proved, 3 sorry (`break_even_symbolic`, `euler_error_general`,
`stochastic_n_required`), 6 axioms. `lake build`: not run (no toolchain here);
project ready at `lean/tct_physiso/`.
