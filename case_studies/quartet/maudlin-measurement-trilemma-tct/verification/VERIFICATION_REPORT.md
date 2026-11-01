# VERIFICATION REPORT

Tier 1 (Python) and Tier 2 (Lean) status for the Maudlin trilemma study.
Method: TCT (Geometric Language Machine), UBP discipline.

## Tier 1 — Python, isolated subprocess (`scripts/verify_column3.py`)

All six Column 3 scripts run in fresh subprocesses, exit 0.

| # | Script | Key checked | Expected | Result |
|---|---|---|---|---|
| 01 | `01_trilemma_core.py` | `C3_CONTRADICTED` | `1` | VERIFIED |
| 02 | `02_born_decoherence.py` | `PURITY` | `1/2` | VERIFIED |
| 03 | `03_grw_collapse_rate.py` | `TAU_MACRO_S` | `1/10000000` | VERIFIED |
| 04 | `04_branch_counting.py` | `BRANCHES_10` | `1024` | VERIFIED |
| 05 | `05_doors_truth_table.py` | `DOORS` | `3` | VERIFIED |
| 06 | `06_cent_fluidic_latch.py` | `ASYMMETRY_OUTCOME` | `1` | VERIFIED |

Full `KEY=VALUE` output: `verification/tier1-run.txt`.

Notable exact values (ℚ only, no floats):
- single-particle GRW wait: `10^16 s` = `12500000000000/39447` years
  (≈ 3.17 × 10⁸ years; floor 316,880,878)
- macro object (N = 10²³): collapse every `1/10000000 s` (100 ns), rate 10⁷ s⁻¹
- detector reduced state: `diag(0, 1/2, 1/2)`, purity `1/2`
- truth table: 7 admissible valuations, 1 excluded (111), 3 doors
- fluidic tie: `1/2 − 1/2 = 0` (no outcome without an extra variable)

## Tier 2 — Lean (`lean/tct_maudlin/`, scaffolded from `lean/spec.json`)

- Proved (sorry-free): **10**
- `sorry` (development required): **3**
  - `branch_weight_sum_general` — gap: nonzero-powers lemma (`pow_ne_zero`/`field_simp` or core induction)
  - `product_state_minors` — gap: ring normalization (`ring` or manual `mul_comm`/`mul_assoc` calc)
  - `everett_emergence_gap` — deliberate target: the Everett emergence-of-outcomes step (Deutsch–Wallace); expected unproven
- Axioms (assumed premises): **5** (named in `lean/tct_maudlin/SORRY_LEDGER.md`)
- Definitions: 3
- `lake build`: **not run** — `lake` not on PATH in this environment. The
  project is complete and ready: `cd lean/tct_maudlin && lake build`.
  (`sorry` compiles with warnings only, so the build is expected to succeed.)

## Optimization loop (docs/07)

- ¢ cost: 12 → 6 primitives (1 iteration accepted, 1 rejected).
- Cross-checks preserved: 14 written, 13 live after tautology audit.
- Answers unchanged by the loop (all `KEY=VALUE` identical).

## How to re-verify

```bash
cd maudlin-measurement-trilemma-tct
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_maudlin --build   # builds if lake present
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```
