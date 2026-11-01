# 07 — Optimization loop and tautology audit

Per TCT §11: once an answer is VERIFIED, iterate on cost — but never at the
price of a verification path. A simplification is accepted iff the primitive
count drops **and** the witness count is preserved or increased.

## Baseline

- Cost metric: ¢ primitive count (`scripts/cent_cost.py`) for the cent
  decomposition; script line/step count as secondary.
- Verification strength: 14 cross-checks across the six Column 3 scripts
  (disjoint derivation paths each): script 01 ×3, 02 ×3, 03 ×2, 04 ×2,
  05 ×2, 06 ×2.

## Tautology audit (§14 condition 2)

One artifact was found in script 02: an intermediate line computing a
"disjointness" boolean that no `assert` consumed — dead weight of the
tautology class (computed but unverified, hence unverifiable). Removed during
the first run (it also raised a NameError). The two real witnesses of that
script — explicit off-diagonal sum, and the zero-product support test — are
disjoint derivation paths and were kept. Net: `t = 1` removal, `c − t = 13 ≥ 2`.

## Iteration 1 — ¢ decomposition v1 → v2

- **Proposal.** Merge duplicated `sum`/`mult`/`eq` primitives (each used once
  per role) and drop `scale`, `rate`, `accum` — stitched steps with no witness
  attached.
- **Measurement.** `python3 scripts/cent_cost.py --before cent/decomp_v1.json
  --after cent/decomp_v2.json`:
  `BEFORE: total=12 (atomic=9, composite=3)` →
  `AFTER: total=6 (atomic=4, composite=2)` — **REDUCED by 6**.
- **Re-verification.** All seven `assert` witnesses of script 06 re-run in an
  isolated subprocess: `VERIFIED`, `EXTRA_VARIABLE_REQUIRED=1`; Lean project
  untouched (no proof depends on the ¢ list). Witness count: 7 → 7 (preserved).
- **Verdict. ACCEPTED.**

## Iteration 2 — none

- **Proposal.** Drop `hysteresis` (argue it is implied by `sat`).
- **Measurement.** Would reduce 6 → 5.
- **Re-verification.** The latch witness (`TIE_NO_OUTCOME` / `ASYMMETRY_OUTCOME`)
  distinguishes *selection* (`sat`) from *irreversibility* (`hysteresis`);
  dropping `hysteresis` would leave the "outcome does not un-happen" content of
  C3 unrepresented — a dropped witness.
- **Verdict. REJECTED** (would sacrifice a witness). Loop stops here.

## Final report

- Original cost: 12 ¢ primitives → final: 6.
- Cross-checks preserved: 14 → 14 (minus 1 dead artifact: 13 live).
- Iterations run: 1 accepted, 1 rejected, stop.
- The loop changed only proof length, never the answer: every `KEY=VALUE` of
  scripts 01–06 is identical before and after (final run:
  `verification/tier1-run.txt`, `verification/VERIFICATION_REPORT.md`).
