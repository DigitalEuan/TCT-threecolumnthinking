# 07 — Optimization loop and tautology audit

Per TCT §11: iterate on cost after VERIFIED, never at the price of a witness.

## Baseline

- Cost metric: ¢ primitive count (`scripts/cent_cost.py`) for the crossbar
  pipeline decomposition.
- Verification strength: 17 cross-checks across the six Column 3 scripts
  (closed-form vs. enumeration; two-path tail sums; formula vs. loop;
  Boolean-clause vs. polynomial-energy evaluation).
- Tautology audit: 1 dead artifact removed before verification (an inert
  conditional block in script 06 that computed nothing); no asserted check was
  dropped. `c − t = 16 ≥ 2`. ✓

## Iteration 1 — v1 → v2 (accepted)

- **Proposal.** Merge duplicated `sum`/`mult` entries in the crossbar
  pipeline decomposition; drop `scale` and `accum` (stitched steps carrying no
  witness of their own).
- **Measurement.** `cent_cost.py --before cent/decomp_v1.json --after
  cent/decomp_v2.json`:
  `BEFORE: total=11 (atomic=9, composite=2)` →
  `AFTER: total=7 (atomic=5, composite=2)` — **REDUCED by 4**.
- **Re-verification.** Re-ran script 01 (`BREAKEVEN_N=55`) and script 05
  (`MIN_DOMAINS=2`) in isolated subprocesses: VERIFIED; witness keys
  preserved 7 → 7.
- **Verdict. ACCEPTED.**

## Iteration 2 — drop `delay` (rejected)

- **Proposal.** Argue `delay` is implied by `state_space` (an ODE network
  contains transport).
- **Measurement.** Would reduce 7 → 6.
- **Re-verification.** The latency witnesses (01 `LATENCY_RATIO_N256`,
  02 `LATENCY_RATIO`) are exactly the transport content; removing `delay`
  from the decomposition would leave the measured latency claims unmotivated
  — a dropped witness, despite the final values still matching.
- **Verdict. REJECTED.** Loop stops.

## Final report

- ¢ cost: 11 → 7 primitives; cross-checks preserved: 17 written / 16 live.
- Iterations: 1 accepted, 1 rejected, stop. The loop changed proof length
  only — every `KEY=*** is identical before and after
  (`verification/tier1-run.txt`).
