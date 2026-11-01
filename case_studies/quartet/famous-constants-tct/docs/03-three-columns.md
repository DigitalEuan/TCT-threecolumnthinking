# 03 — The three-column contract

The three columns describe the **identical logical steps**. Domain: ℚ / ℤ
(rational intervals; irrational values carried by convergents + certificates,
UBP D1). **UBP.** `Fraction`/`int` only; no floats, no random, no SHA-256.

**Givens.** Known digit blocks (exact integer floors) as independent anchors;
series term counts as declared in docs/02; α = 72973525693/10^13 (empirical).

| Step | Plain English | Mathematics | Python (this step) | Lean |
|---|---|---|---|---|
| 1 | the arctan series with its alternating error certificate | arctan(1/x) = Σ(−1)^k/((2k+1)x^{2k+1}), \|err\| ≤ next term | 01: `arctan_inv` | `analysis_convergence_premises` (axiom) |
| 2 | the Machin derivation of pi | π = 16·arctan(1/5) − 4·arctan(1/239) | 01: interval A | `pi_definition` (axiom) |
| 3 | the Euler arctan derivation of pi | π = 4(arctan(1/2)+arctan(1/3)) | 01: interval B | — |
| 4 | the BBP derivation of pi | π = Σ[4/(8k+1)−2/(8k+4)−1/(8k+5)−1/(8k+6)]/16^k | 01: interval C | — |
| 5 | the agreement of the three derivations | pairwise overlap; shared 13-digit block; widths < 10⁻²⁵ | 01: `INTERVALS_OVERLAP=1`, `PI_ANCHOR=1` | — |
| 6 | the factorial series for e with tail bound | R_n < (n+2)/((n+1)(n+1)!) | 02: `E_OK=1` (two paths) | `e_definition` (axiom) |
| 7 | the Fibonacci convergents of phi | p/q = F_{n+1}/F_n; \|φ − p/q\| < 1/q² | 02: `PHI_OK=1` | — |
| 8 | the exact certificates of phi's quadratic nature | F_{n+1}² − F_n F_{n+2} = (−1)ⁿ; F_{n+1}² − F_{n+1}F_n − F_n² = (−1)ⁿ | 02: `CASSINI_OK=1`, `PHI_RESIDUAL_OK=1` | `cassini_sample`, `phi_quadratic_sample` (proved) |
| 9 | the two derivations of sqrt(2) | isqrt brackets; Pell p²−2q² = ±1 | 02: `SQRT2_OK=1`, `PELL_OK=1` | `pell_sample` (proved) |
| 10 | the partial sums of the Basel series | S_N = Σ1/n²; tail < 1/N | 03: `Z2_CONTAINED=1` | `zeta2_partial_value` (proved); `zeta2_tail_symbolic` (sorry) |
| 11 | the Basel identity itself | Σ1/n² = π²/6 (Euler 1735) | 03: interval from π | `euler_basel_identity` (axiom) |
| 12 | the fourth-order cousin | Σ1/n⁴ = π⁴/90; tail < 1/(3N³) | 03: `Z4_CONTAINED=1` | — |
| 13 | the two series for ln 2 and their agreement | Mercator (±1/(N+1)) vs. Σ1/(k2^k) (tail ≤ 1/((M+1)2^M)) | 04: `LN2_OVERLAP=1` | `ln2_partial_value` (proved) |
| 14 | Catalan's constant by alternating squares | G = Σ(−1)^k/(2k+1)², \|err\| ≤ 1/(2N+3)² | 04: `CATALAN_ANCHOR_OK=1` | — |
| 15 | the t-series for gamma | t_k = 1/k − ln(1+1/k); tail < 1/(2N) | 05: `GAMMA_CONTAINED=1` | — |
| 16 | the definition-side bracketing of gamma | H_n − U_n < γ < H_n − L_n (integral sandwiches) | 05: `GAMMA_CONTAINED_COARSE=1`, `PATHS_OVERLAP=1` | — |
| 17 | the open boundary of gamma | no closed form; irrationality UNKNOWN | 05: `GAMMA_IRRATIONALITY=UNKNOWN` | `gamma_rational_target` (sorry: deliberate) |
| 18 | the Champernowne digits by two paths | concatenation ≡ position arithmetic | 06: `CHAMPERNOWNE_OK=1` | `champernowne_head` (def) |
| 19 | the five-class taxonomy of constants | D/T/O/U/P catalog valid; counts (5,5,4,1,4) | 06: `TAXONOMY_VALID=1`, `CLASS_COUNTS` | — |
| 20 | the uncomputable boundary (Chaitin Ω) | definable; digits uncomputable | 06: class U stamp | — |
| 21 | the physical constants boundary | α measured; c/h defined; G measured | 06: `ALPHA_REFUSED=1` | `physical_constants_empirical` (axiom); `alpha_physical_target` (sorry: deliberate) |
| 22 | the naive claim, refused | "all constants derivable from first principles" | 06: `ALPHA_STATUS=REFUSED_WOULD_BE_GUESS` | — |

**UBP compliance.** `Fraction`/`int` only; irrational values carried by
rational convergents and exact error certificates; no floats, no random.

**Decomposition.** 24 atomic claims: 13 proved, 3 sorry, 7 axioms, 1 refused
(docs/02).

**Full Column 3 scripts:** `scripts/column3/01…06_*.py`; outputs
`verification/tier1-run.txt`.

**Verification.** Python: **VERIFIED** 6/6 (the assert layer corrected four
draft defects along the way: two anchor methods, one parity direction, one
Pell seed sign — all documented in verification/). **Lean:** 6 proved,
3 sorry (`zeta2_tail_symbolic`, `gamma_rational_target` [deliberate],
`alpha_physical_target` [deliberate]), 7 axioms. `lake build`: not run here;
ready at `lean/tct_constants/`.
