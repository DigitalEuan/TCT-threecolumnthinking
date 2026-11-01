# Classification ledger (TCT §14)

Identity: `n = p + s + a + r` → **22 = 13 + 3 + 6 + 0**

## Proved (13) — Python VERIFIED (6/6 scripts, isolated subprocesses)

1. energy ratios 6419× (vN) / 69× (in-memory) per MAC-equivalent (01)
2. break-even N = 55 vs. in-memory digital, 8-bit converters (01)
3. break-even N = 228 at 32-bit effective precision, 4 passes (01)
4. latency ratio 65536/513 at N = 256 (declared model) (01)
5. direct/FFT convolution ratio 512/25 exactly (02)
6. optical break-even reuse T = 21 (02)
7. amortization boundary consistent at T = 21/20 (02)
8. exact binomial tail ≤ Chebyshev bound 1/4, two-path sum (03)
9. stream length ≥ 2500 bits for 1% error (03)
10. stochastic crossover width w = 11 (03)
11. Euler error identity; e(10) = 29/200 (04)
12. M = 1500 digital steps to match the 1/1000 analog floor (04)
13. SAT ⟺ Ising energy-zero equivalence; cubic terms present (06)

Lean counterparts proved: `ratio_vn_exact`, `ratio_inmem_exact`,
`breakeven_55`, `breakeven32_228`, `fft_ratio`, `breakeven_t_21`,
`euler_error_10`, `m_min_1500`, `chebyshev_2500` (9 theorems).

## Sorry (3) — named gaps, development required

- `break_even_symbolic` — needs `ring`/`linarith` (Mathlib) or manual calc.
- `euler_error_general` — needs `field_simp`/`ring` with ℕ→ℚ cast bookkeeping.
- `stochastic_n_required` — minimality claim; needs positivity/`linarith`.

## Axioms (6) — named premises

- `horowitz_energies_empirical` — digital energy figures (Horowitz 2014).
- `crossbar_model_empirical` — cell/conversion energy model (illustrative).
- `analog_offset_model_empirical` — analog error floor 1/1000 (illustrative).
- `noise_bernoulli_empirical` — physical noise = Bernoulli sampling.
- `ising_relaxation_empirical` — physical relaxation toward low energy.
- `physical_church_turing` — ECT premise; **quantum case open, not claimed**.

## Refusals (0) — taxonomy armed

`WOULD_BE_GUESS = 0` among stated results. Refusal triggers documented in
docs/05: speedup claims without a cost model; cross-precision comparisons
without conversion modeling (`DIFFERENT_SCALES`); any claim that quantum
substrates change complexity classes (excluded by construction).

## Cross-check register (17 written; 1 dead artifact removed; 16 live)

| Script | Cross-check pairs (disjoint derivation paths) |
|---|---|
| 01 | ratio via Fraction vs. gcd-reduction; break-even N via inequality vs. enumeration (×2 precision cases) |
| 02 | ratio reduction; break-even T via inequality vs. enumeration; amortization boundary check |
| 03 | tail via two-tail sum vs. complement; Chebyshev bound check; N via formula vs. enumeration; crossover enumeration |
| 04 | error formula vs. direct Fraction loop (M=1..20); M boundary via enumeration vs. direct substitution |
| 05 | vocabulary validity; ≥2-domains coverage; license counts sum |
| 06 | Boolean satisfaction vs. polynomial-energy evaluation (8 assignments); expansion count vs. slot count |

Removed: one inert conditional block in script 06 (computed nothing; tautology
class). `c − t = 16 ≥ 2`. ✓
