# 07 — Optimization loop and tautology audit

Per TCT §11: iterate on cost after VERIFIED; never at the price of a witness.

## Baseline

- Cost metric: ¢ primitive count (`scripts/cent_cost.py`) for the light-cone
  derivation pipeline (docs/06).
- Verification strength: 14 cross-checks across the six Column 3 scripts
  (Fraction vs. gcd; dict vs. list-matrix evolution; Pauli-label rules vs.
  GF(2) symplectic matrices; closed formula vs. interaction-range sum;
  integer division vs. cross-multiplied inequalities; interval reciprocals
  vs. direction checks).
- Tautology audit: 1 dead artifact removed in pre-verification cleanup (an
  inert draft block in script 03 that computed nothing); no asserted check
  dropped. `c − t = 13 ≥ 2`. ✓

## Iteration 1 — v1 → v2 (accepted)

- **Proposal.** Merge duplicated `sum`/`rate` entries; drop `accum`
  (stitched step carrying no witness of its own — the cone derivation
  propagates, it does not integrate).
- **Measurement.** `cent_cost.py --before cent/decomp_v1.json --after
  cent/decomp_v2.json`: `BEFORE: total=10 (atomic=8, composite=2)` →
  `AFTER: total=7 (atomic=5, composite=2)` — **REDUCED by 3**.
- **Re-verification.** Re-ran script 03 (`EDGE_SPEED=1`) and script 04
  (`CONE_BOUND=1`) in isolated subprocesses: VERIFIED; cone witnesses
  preserved.
- **Verdict. ACCEPTED.**

## Iteration 2 — drop `spatial` (rejected)

- **Proposal.** Argue `state_space` already carries geometry.
- **Measurement.** Would reduce 7 → 6.
- **Re-verification.** The cone claims *are* spatial-support claims
  (`SUPPORT_T20=19`, Clifford support growth): removing `spatial` would leave
  the support witnesses unmotivated — a dropped witness despite matching
  final values.
- **Verdict. REJECTED.** Loop stops.

## Final report

- ¢ cost: 10 → 7 primitives; cross-checks preserved: 14 written / 13 live.
- Iterations: 1 accepted, 1 rejected, stop. All `KEY=*** values identical
  before and after the loop (`verification/tier1-run.txt`).
- The loop changed proof length only — as designed, the answers — including
  the refusal at the value boundary — are untouched.
