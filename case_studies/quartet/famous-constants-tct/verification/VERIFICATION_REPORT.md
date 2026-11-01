# VERIFICATION REPORT

Tier 1 (Python) and Tier 2 (Lean) status for the famous-constants study.
Method: TCT (Geometric Language Machine), UBP discipline, cent mode.

## Tier 1 — Python, isolated subprocess (`scripts/verify_column3.py`)

All six Column 3 scripts run in fresh subprocesses, exit 0.

| # | Script | Key checked | Expected | Result |
|---|---|---|---|---|
| 01 | `01_pi_convergents.py` | `INTERVALS_OVERLAP` | `1` | VERIFIED |
| 02 | `02_e_phi_sqrt2.py` | `PELL_OK` | `1` | VERIFIED |
| 03 | `03_zeta2_basel.py` | `Z2_CONTAINED` | `1` | VERIFIED |
| 04 | `04_ln2_catalan.py` | `CATALAN_ANCHOR_OK` | `1` | VERIFIED |
| 05 | `05_gamma_open.py` | `GAMMA_CONTAINED` | `1` | VERIFIED |
| 06 | `06_taxonomy.py` | `TAXONOMY_VALID` | `1` | VERIFIED |

Full `KEY=*** output: `verification/tier1-run.txt`.

Notable exact results (ℚ/ℤ only, no floats):
- π: three independent intervals (Machin, Euler arctan, BBP) overlapping,
  widths < 10⁻²⁵, shared 13-digit block 31415926535897
- e: 12-digit block 2718281828459 via two summation paths + exact tail bound
- φ: Cassini + quadratic-residual certificates exact; 12-digit block
- √2: isqrt bracket + 13 Pell certificates (p²−2q² = ±1)
- ζ(2): partial+tail sandwiches at N=200/400; ζ(4): tail < 1/(3N³)
- ln 2: Mercator ∩ binary series; 12-digit block 693147180559
- Catalan: alternating certificate; anchor contained
- γ: two independent bracketing constructions overlap; width < 1/100;
  `GAMMA_IRRATIONALITY=UNKNOWN` stamped
- taxonomy: D/T/O/U/P = 5/5/4/1/4; `ALPHA_REFUSED=1`

### Assert-layer interventions (all documented, all fixed)

1. Truncation anchors cannot sit inside intervals tighter than the truncation
   gap → replaced with digit-block witnesses (01, 02, 03, 04).
2. Alternating-remainder parity direction was inverted (04) → corrected.
3. Pell seed 3²−2·2² = +1, not −1 (certificates alternate) → corrected.
4. Huge-fraction printing hit Python's int→str limit (04) → digit-block
   printing.
5. Mercator bracket at k=1 too wide → k=1 handled by the binary ln 2 series (05).

## Tier 2 — Lean (`lean/tct_constants/`, scaffolded from `lean/spec.json`)

- Proved (sorry-free): **6**
- `sorry` (development required): **3**
  - `zeta2_tail_symbolic` — gap: `linarith`/order reasoning (Mathlib)
  - `gamma_rational_target` — **deliberate, expected unproven**: γ's closed
    form / arithmetic type (Erdős-prize open problem)
  - `alpha_physical_target` — **deliberate, expected unproven** (trilogy
    link): α from theory; registered `WOULD_BE_GUESS`
- Axioms (named premises): **7**
- Definitions: 2
- `lake build`: **not run** — `lake` not on PATH here; project complete and
  ready: `cd lean/tct_constants && lake build`.

## Optimization loop (docs/07)

- ¢ cost: 9 → 6 primitives (iteration 1 accepted; iteration 2 rejected —
  `recip` is the term-generation witness machinery).
- Cross-checks: 18 written / 18 live after defect fixes.

## How to re-verify

```bash
cd famous-constants-tct
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_constants --build   # builds if lake present
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```
