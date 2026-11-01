# Maudlin's Three Measurement Problems — a Three Column Thinking (TCT) study

A full TCT study of the quantum measurement trilemma: three claims about
quantum mechanics — the wavefunction is **complete** (C1), it evolves
**linearly** at all times (C2), and measurements have **single outcomes** (C3)
— are individually plausible and jointly incompatible. Tim Maudlin sharpened
the measurement problem into this form in "Three Measurement Problems"
(*Topoi* 14, 1995); John Bell's "Against 'Measurement'" (*Physics World*,
1990) diagnosed the vagueness it replaces. Once the structure is exact, the
interpretation landscape becomes a truth table with **three doors** out of
one room.

Every structural claim in this repository is re-derived exactly — no floats,
no randomness — in isolated subprocesses, and formalized in Lean where
possible (with named gaps where not).

## The result in one table

| Door | Keep | Sacrifice | Family | Pays with |
|---|---|---|---|---|
| `110` | C1 + C2 | C3 | Many-worlds (Everett) | outcomes & probability (open: `everett_emergence_gap`) |
| `101` | C1 + C3 | C2 | Objective collapse (GRW, Diósi–Penrose) | modified dynamics + new parameters |
| `011` | C2 + C3 | C1 | Bohmian mechanics | added ingredient (positions) + nonlocality |

Sidesteppers: **QBism** rejects C1's physicalist reading (ψ = an agent's
expectations); **relational QM** keeps outcomes but makes them
observer-relative. Both relocate a claim rather than opening a fourth door.

## Verified highlights (all exact, ℚ/ℤ)

- Completeness + linearity ⇒ detector in **two** orthogonal reading states
  (`NONZERO_BRANCHES=2`), contradicting C3 (`C3_CONTRADICTED=1`).
- Truth table: 7 admissible valuations of (C1,C2,C3), 1 excluded (111),
  exactly 3 doors.
- GRW: one particle waits `10^16 s ≈ 3.17×10^8 yr` between collapses; a
  `10^23`-particle object collapses every `10^−7 s`.
- Many-worlds: 10 binary measurements → `2^10 = 1024` branches, total weight
  exactly 1.
- Cross-domain (cent): a symmetric fluidic fork feeding a latch **cannot**
  select (`1/2 − 1/2 = 0`); one extra variable ε breaks the tie — the Bohmian
  structure in pipes (conjectural analogy, honestly ledgered).

## Repository layout

```
README.md                        ← this file
docs/
  01-overview.md                 ← the trilemma and the three doors
  02-decomposition.md            ← 20 atomic claims, classified (20 = 12+3+5+0)
  03-three-columns.md            ← the synchronised three-column contract
  04-interpretation-map.md       ← what each interpretation pays
  05-bell-and-measurement.md     ← Bell 1990 and why the trilemma is the precise form
  06-cent-cross-domain.md        ← £ → ¢ → ∆: the trilemma in a fluidic fork
  07-optimization-loop.md        ← cost 12→6, witnesses preserved, tautology audit
  08-references.md               ← primary sources + premise note
scripts/
  verify_column3.py              ← Tier-1 isolated verifier (TCT §13)
  scaffold_lean_project.py       ← JSON spec → Lean 4 Lake project (TCT §13)
  lean_ledger.py                 ← sorry/axiom scanner + optional lake build
  cent_cost.py                   ← ¢ primitive cost metric (TCT §13)
  column3/
    01_trilemma_core.py          ← THE core model: C1∧C2 ⊢ ¬C3
    02_born_decoherence.py       ← exact Born/decoherence bookkeeping
    03_grw_collapse_rate.py      ← GRW collapse-time arithmetic
    04_branch_counting.py        ← many-worlds branch accounting
    05_doors_truth_table.py      ← 8 valuations → 3 doors
    06_cent_fluidic_latch.py     ← cross-domain witness (fluidic fork + latch)
lean/
  spec.json                      ← lemma spec (proved/sorry/axiom)
  tct_maudlin/                   ← Lean 4 Lake project (10 proved, 3 sorry, 5 axioms)
ledgers/
  classification-ledger.md       ← the four ledgers + cross-check register
  insights.md                    ← what the structure buys
cent/
  decomp_v1.json / decomp_v2.json  ← optimization-loop artifacts
verification/
  VERIFICATION_REPORT.md         ← Tier 1 + Tier 2 status
  tier1-run.txt                  ← full KEY=VALUE output of all six scripts
```

## Re-verify (Python 3 stdlib only; no installs)

```bash
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_maudlin --build   # builds if `lake` is installed
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```

## Status

- **Tier 1 (Python):** 6/6 VERIFIED, isolated subprocesses.
- **Tier 2 (Lean):** 10 proved, **3 sorry** (each with a named gap — these are
  exactly the development required), 5 named axioms. `lake build` not run here
  (no toolchain); the project is complete and ready.
- **Refusals:** none. **WOULD_BE_GUESS:** zero.

Method: Three Column Thinking (TCT) — Geometric Language Machine (GLM),
E. R. A. Craig (DigitalEuan), https://github.com/DigitalEuan/GLM. Bundled
scripts are the TCT §13 sources, used verbatim.
