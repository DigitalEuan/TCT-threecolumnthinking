# 02 — Decomposition: 22 atomic claims, classified

Classification identity (TCT §14 condition 1): `n = p + s + a + r` →
**22 = 13 + 3 + 6 + 0**.

## Givens (declared, illustrative unless marked empirical)

- Energy units of 0.1 pJ; Horowitz (ISSCC 2014) figures: 32b FP mult = 37,
  32b add = 1, SRAM read = 50, DRAM read = 6400 units (**empirical**).
- Crossbar model: cell compute = 2 units, DAC/ADC conversion = 3700 units each
  (**illustrative**, consistent with "converters dominate" findings).
- Workloads: N×N matrix-vector (N = 1024 for latency), 1-D convolution
  N = 1024, stream N = 100 at p = 1/2, ODE `y' = 3t²`, 3-SAT instance with 3
  variables / 2 clauses.

## Proved (13) — Python VERIFIED; Lean proved where a lemma exists

| # | Claim | Witness |
|---|---|---|
| 1 | energy ratio per MAC-equivalent: 6419× (vN), 69× (in-memory) | 01 `RATIO_VN`, `RATIO_INMEM`; Lean `ratio_vn_exact`, `ratio_inmem_exact` |
| 2 | break-even N = 55 vs. in-memory digital (8-bit converters) | 01 `BREAKEVEN_N`; Lean `breakeven_55` |
| 3 | break-even N = 228 at 32-bit effective precision (4 passes) | 01 `BREAKEVEN_N_32BIT`; Lean `breakeven32_228` |
| 4 | latency ratio N²/(2N+1) = 65536/513 at N = 256 (declared model) | 01 `LATENCY_RATIO_N256` |
| 5 | direct/FFT convolution ratio = 512/25 exactly | 02 `RATIO_DIRECT_FFT`; Lean `fft_ratio` |
| 6 | optical break-even reuse T = 21 | 02 `BREAKEVEN_T`; Lean `breakeven_t_21` |
| 7 | amortization boundary consistent (T=21 in, T=20 out) | 02 `AMORTIZATION_CONSISTENT` |
| 8 | exact binomial tail (two paths) ≤ Chebyshev bound 1/4 | 03 `TAIL_EXACT`, `CHEBYSHEV_OK` |
| 9 | stream length ≥ 2500 bits for 1% error (minimality) | 03 `N_FOR_1PCT`; Lean `chebyshev_2500` (equality) |
| 10 | stochastic crossover gate-width 11 (11² > 100) | 03 `CROSSOVER_WIDTH` |
| 11 | Euler error identity `(3M−1)/(2M²)`; e(10) = 29/200 | 04 `FORMULA_MATCH`, `ERROR_M10`; Lean `euler_error_10` |
| 12 | digital steps to match analog floor: M = 1500 (boundary exact) | 04 `M_MIN`; Lean `m_min_1500` |
| 13 | SAT ⟺ Ising energy zero on all 8 assignments; cubic terms present | 06 `EQUIVALENCE`, `CUBIC_TERMS_PRESENT` |

Plus catalog license condition: 12 primitives used, each realized in ≥ 2 of 8
domains, 37 licensed / 3 conjectural (05 `MIN_DOMAINS`, `LICENSED`) — counted
within claims 1–13's machinery, reported in ledgers.

## Sorry (3) — named gaps, development required

| # | Claim | Gap |
|---|---|---|
| 14 | `break_even_symbolic` — the algebraic equivalence of the break-even inequality for all N | needs `ring`/`linarith` (Mathlib) or manual calc |
| 15 | `euler_error_general` — the error identity for all M > 0 | needs `field_simp`/`ring` with cast bookkeeping |
| 16 | `stochastic_n_required` — minimality of 2500 for 1% error | needs `linarith`/positivity reasoning |

## Axioms (6) — empirical/premise, never sorry theorems

| # | Name | Premise |
|---|---|---|
| 17 | `horowitz_energies_empirical` | digital energy figures (Horowitz 2014) |
| 18 | `crossbar_model_empirical` | cell/conversion energy model |
| 19 | `analog_offset_model_empirical` | fixed analog error floor 1/1000 |
| 20 | `noise_bernoulli_empirical` | physical noise = Bernoulli sampling |
| 21 | `ising_relaxation_empirical` | physical relaxation toward low energy |
| 22 | `physical_church_turing` | efficient digital simulability of physical systems (ECT); **quantum case open, not claimed** |

## Refusals

None (`r = 0`), but the refusal taxonomy is armed: any "physical computing is
N× faster" claim **without a declared cost model** is `WOULD_BE_GUESS`; any
precision comparison across **DIFFERENT_SCALES** (e.g. 8-bit analog vs 64-bit
digital without declared conversion) is refused, not estimated.

## The four conditions (§14) — report

1. **Classification identity.** 22 = 13 + 3 + 6 + 0. ✓
2. **Independent cross-checks.** 17 cross-checks across the six scripts
   (closed-form vs. enumeration; two-path tail sums; formula vs. loop;
   Boolean vs. polynomial energy). 1 dead artifact removed pre-verification
   (an inert conditional block in script 06); `c − t = 16 ≥ 2`. ✓
3. **Optimization-loop acceptance.** ¢ decomposition 11 → 7 primitives,
   witnesses preserved (7 → 7 keys), re-verified, accepted; second proposal
   (drop `delay`) rejected as a lost witness. ✓
4. **Named ledger.** 3 sorry with exact missing tactics; 6 named axioms;
   `WOULD_BE_GUESS = 0` among stated results; the quantum claim is explicitly
   **not** stated. ✓
