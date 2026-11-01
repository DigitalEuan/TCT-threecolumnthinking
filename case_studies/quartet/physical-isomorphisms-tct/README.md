# Physical → Computational Isomorphisms — a Three Column Thinking (TCT) study

**Question:** how can physical functions be mapped as isomorphisms to
computational systems in ways that produce *measurable improvement* — and
which computational hurdles can be overcome or worked around by using physical
isomorphisms?

**Answer:** five measurable gains under five preconditions — and one honest
refusal. Physics buys **energy** (wires sum currents free), **latency**
(propagation replaces sequential steps), **amortization** (setup paid once),
**sampling** (noise is a free Bernoulli source), and **continuous time**
(no discretization steps). Physics does **not** buy complexity classes:
structure-preserving maps preserve hardness (extended Church-Turing carried as
an axiom; the quantum case explicitly open and unclaimed).

Every gain is located at an exact crossover, computed twice (closed form +
enumeration) over ℚ/ℤ — no floats, no randomness.

## The measured crossovers

| Gain | Exact result | Where |
|---|---|---|
| Energy per MAC-equivalent | 6419× (von Neumann) / 69× (in-memory) | `01` |
| Crossbar break-even size | N = 55 (8-bit converters) → N = 228 (32-bit) | `01` |
| Convolution | direct/FFT = 512/25; optical wins at reuse T ≥ 21 | `02` |
| Latency | 51200 ops → 1 propagation step | `02` |
| Sampling | exact binomial tail ≤ 1/4; 1% error needs ≥ 2500 bits | `03` |
| ODE integration | 1500 Euler steps : 1 analog evolution @ 1/1000 floor | `04` |
| Combinatorial | SAT→Ising exact (8/8 assignments); **no proven speedup** | `06` |

## The hurdle map (docs/04)

H1 data movement → in-situ compute · H2 linear algebra → crossbar/optical ·
H3 NP-hard search → Ising/annealing (heuristic!) · H4 randomness → physical
noise streams · H5 ODE/PDE → analog integration · H6 transport → optics ·
H7 precision → mixed-signal passes · H8 flexibility → amortization.
Each with its caveat; guardrails in docs/05 (`WOULD_BE_GUESS` armed against
model-free speedup claims).

## Repository layout

```
README.md                          ← this file
docs/
  01-overview.md                   ← the question, the five gains, five preconditions
  02-decomposition.md              ← 22 atomic claims (22 = 13+3+6+0)
  03-three-columns.md              ← synchronised three-column contract
  04-hurdle-map.md                 ← hurdles H1–H8: isomorphism, gain, caveat
  05-guardrails.md                 ← what isomorphisms cannot do (ECT, noise, I/O)
  06-cent-compiler.md              ← £ → ¢ → ∆ run + license ledger
  07-optimization-loop.md          ← ¢ cost 11→7, witnesses preserved
  08-references.md                 ← Horowitz, Feynman, Blum-Shub-Smale, Ising…
scripts/
  verify_column3.py / scaffold_lean_project.py / lean_ledger.py / cent_cost.py
                                   ← TCT §13 bundled scripts (verbatim)
  column3/
    01_crossbar_break_even.py      ← energy ratios + break-even N (2 paths)
    02_convolution_amortization.py ← FFT vs direct vs optical; break-even T
    03_stochastic_streams.py       ← exact binomial tails; stream-length bounds
    04_analog_ode.py               ← exact Euler error; analog-floor crossover
    05_primitives_catalog.py       ← 22-primitive × 8-domain license catalog
    06_sat_ising.py                ← exact SAT→energy mapping; gadget cost
lean/
  spec.json                        ← lemma spec
  tct_physiso/                     ← Lean 4 Lake project (9 proved, 3 sorry, 6 axioms)
ledgers/
  classification-ledger.md         ← four ledgers + cross-check register
  insights.md                      ← what the structure buys
cent/
  decomp_v1.json / decomp_v2.json  ← optimization-loop artifacts
verification/
  VERIFICATION_REPORT.md           ← Tier 1 + Tier 2 status
  tier1-run.txt                    ← full KEY=*** output of all six scripts
```

## Re-verify (Python 3 stdlib only; no installs)

```bash
for f in scripts/column3/0*.py; do python3 scripts/verify_column3.py "$f"; done
python3 scripts/lean_ledger.py lean/tct_physiso --build    # builds if `lake` installed
python3 scripts/cent_cost.py --before cent/decomp_v1.json --after cent/decomp_v2.json
```

## Status

- **Tier 1 (Python):** 6/6 VERIFIED, isolated subprocesses.
- **Tier 2 (Lean):** 9 proved, **3 sorry** (named gaps = development required),
  6 named axioms. `lake build` not run here (no toolchain); ready.
- **Refusals:** none among stated results; taxonomy armed (docs/05).
- **Open, unclaimed:** NP-hard speedups (contested); quantum complexity (BQP
  vs BPP).

Method: Three Column Thinking (TCT) — Geometric Language Machine (GLM),
E. R. A. Craig (DigitalEuan), https://github.com/DigitalEuan/GLM. This study
is a full cent_compiler run (§12): docs/06. Companion study:
`maudlin-measurement-trilemma-tct/` (Maudlin's three measurement problems).
