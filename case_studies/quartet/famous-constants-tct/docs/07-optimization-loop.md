# 07 — Optimization loop and tautology audit

Per TCT §11: iterate on cost after VERIFIED; never at the price of a witness.

## Baseline

- Cost metric: ¢ primitive count (`scripts/cent_cost.py`) for the
  constant-computation pipeline (docs/06).
- Verification strength: 18 cross-checks across the six Column 3 scripts
  (three-way interval overlap; two-path sums; isqrt vs. Pell; Cassini vs.
  quadratic residual; telescoping vs. integral tails; two-series ln 2;
  string vs. position arithmetic; two-way γ bracketing).
- Tautology audit findings (all fixed pre-verification):
  1. one inert draft line in script 04 (computed nothing) — removed;
  2. **anchor-method defect**: truncated-decimal anchors can never lie inside
     intervals tighter than the truncation gap — replaced by digit-block
     witnesses (both endpoints share the known digits);
  3. one parity-direction error in the alternating-remainder logic (04);
  4. one Pell seed sign (3²−2·2² = +1, certificates alternate).
  The assert layer caught 2–4 as failures; each fix re-derived from the
  computed values, not guessed. Live cross-checks: 18.

## Iteration 1 — v1 → v2 (accepted)

- **Proposal.** Merge the duplicated `sum`; drop `scale` and `accum`
  (stitched steps with no witness of their own).
- **Measurement.** `cent_cost.py --before cent/decomp_v1.json --after
  cent/decomp_v2.json`: `BEFORE: total=9 (atomic=7, composite=2)` →
  `AFTER: total=6 (atomic=4, composite=2)` — **REDUCED by 3**.
- **Re-verification.** Re-ran script 01 (`INTERVALS_OVERLAP=1`) and script 03
  (`Z2_CONTAINED=1`) in isolated subprocesses: VERIFIED; witnesses preserved.
- **Verdict. ACCEPTED.**

## Iteration 2 — drop `recip` (rejected)

- **Proposal.** Argue `sum` plus `mult` subsume term generation.
- **Measurement.** Would reduce 6 → 5.
- **Re-verification.** Every series in the study is *made of* reciprocal
  terms (1/k!, 1/k², 1/(2k+1)², 1/(k2^k)): dropping `recip` would leave the
  term-generation witnesses (`E_OK`, `Z2_CONTAINED`, `CATALAN_ANCHOR_OK`)
  without their primitive — a dropped witness.
- **Verdict. REJECTED.** Loop stops.

## Final report

- ¢ cost: 9 → 6 primitives; cross-checks preserved (18 live).
- Iterations: 1 accepted, 1 rejected, stop. All `KEY=*** values identical
  before/after (`verification/tier1-run.txt`) — including the two deliberate
  refusals, which the loop correctly leaves untouched.
