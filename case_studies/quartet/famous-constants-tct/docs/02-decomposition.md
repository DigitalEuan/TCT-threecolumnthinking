# 02 — Decomposition: 24 atomic claims, classified

Classification identity (TCT §14 condition 1): `n = p + s + a + r` →
**24 = 13 + 3 + 7 + 1**.

## Givens (declared; empirical where marked)

- Known leading digits used as independent anchors (exact integer floors):
  π 13 digits, e/φ/√2/ln2/ζ2/ζ4/Catalan 12 digits, γ 10 digits.
- Series parameters: Machin/Euler/BBP term counts (40/90/35...); factorial
  N = 60; Fibonacci to F₃⁶; Pell to 12 convergents; Mercator N = 4000;
  binary M = 60; γ: N = 200 terms.
- Physical givens (**empirical/definitional**): α = 72973525693/10^13
  (CODATA 2018); c, h SI-defined (2019); G measured.

## Proved (13) — Python VERIFIED (6/6, isolated subprocesses)

| # | Claim | Witness |
|---|---|---|
| 1 | π: three independent intervals (Machin / Euler / BBP) mutually overlap | 01 `INTERVALS_OVERLAP=1` |
| 2 | π: all intervals share the known 13-digit block; widths < 10⁻²⁵ | 01 `PI_ANCHOR=1`, `WIDTH_OK=1` |
| 3 | π: midpoints mutually consistent within widths | 01 `MIDPOINTS_CONSISTENT=1` |
| 4 | e: two summation paths agree; tail bound (n+2)/((n+1)(n+1)!); 12-digit block | 02 `E_OK=1` |
| 5 | φ: Cassini identity exact for n < 30 | 02 `CASSINI_OK=1` |
| 6 | φ: quadratic residual (φ² = φ+1) exact; 12-digit block from convergent bracket | 02 `PHI_RESIDUAL_OK=1`, `PHI_OK=1` |
| 7 | √2: isqrt bracket contains the anchor exactly | 02 `SQRT2_OK=1` |
| 8 | √2: Pell certificates p²−2q² = ±1 exact on 13 convergents | 02 `PELL_OK=1` |
| 9 | ζ(2): partial sums + tail < 1/N sandwich the π²/6 interval at N and 2N | 03 `Z2_CONTAINED=1`, `WIDTH_SHRINKS=1` |
| 10 | ζ(2)/ζ(4): 12-digit blocks match known values | 03 `Z2_ANCHOR_OK=1`, `Z4_ANCHOR_OK=1` |
| 11 | ζ(4): partial + tail < 1/(3N³) sandwiches π⁴/90 | 03 `Z4_CONTAINED=1` |
| 12 | ln 2: Mercator and binary-series intervals overlap; anchor + digits | 04 `LN2_OVERLAP=1`, `LN2_ANCHOR_OK=1` |
| 13 | Catalan: alternating interval contains the 12-decimal anchor; γ-classified taxonomy + Champernowne two paths + class counts (06) | 04 `CATALAN_ANCHOR_OK=1`; 05 `GAMMA_CONTAINED=1`, `PATHS_OVERLAP=1`; 06 `TAXONOMY_VALID=1`, `CHAMPERNOWNE_OK=1` |

## Sorry (3) — named gaps, development required

| # | Claim | Gap |
|---|---|---|
| 14 | `zeta2_tail_symbolic` — general tail-sandwich inequality | `linarith`/order reasoning (Mathlib) |
| 15 | `gamma_rational_target` — **deliberate, expected unproven**: γ's closed form/rationality | the open problem itself (Erdős prize); class-O boundary |
| 16 | `alpha_physical_target` — **deliberate, expected unproven** (trilogy link): α from theory | registered `WOULD_BE_GUESS`; no accepted derivation |

## Axioms (7) — named premises

| # | Name | Premise |
|---|---|---|
| 17 | `pi_definition` | π = circle ratio (definitional) |
| 18 | `e_definition` | e = lim(1+1/n)ⁿ (definitional) |
| 19 | `analysis_convergence_premises` | alternating/telescoping/integral bounds (analysis) |
| 20 | `euler_basel_identity` | sin-product coefficient match ⇒ ζ(2)=π²/6, ζ(4)=π⁴/90 |
| 21 | `apery_theorem` | ζ(3) irrational (Apéry 1979) |
| 22 | `gelfond_schneider` | e^π transcendental (Gelfond–Schneider) |
| 23 | `physical_constants_empirical` | α measured; c/h defined; G measured |

## Refused (1)

| # | Claim | Refusal |
|---|---|---|
| 24 | "the physical constants (α and friends) are derivable from first principles" | **`WOULD_BE_GUESS`** — study 3's refusal carries over unchanged; formal record `alpha_physical_target` (06 stamps `ALPHA_REFUSED=1`) |

## The four conditions (§14) — report

1. **Classification identity.** 24 = 13 + 3 + 7 + 1. ✓
2. **Independent cross-checks.** 18 cross-checks across the six scripts
   (three-way π interval overlap; two-path sums; isqrt vs. Pell; Cassini vs.
   quadratic residual; telescoping vs. integral tails; two-series ln 2;
   string vs. position arithmetic). 1 dead artifact removed pre-verification
   (inert draft line in script 04) + 1 anchor-method defect repaired
   (truncation anchors → digit-block witnesses); `c − t = 17 ≥ 2`. ✓
3. **Optimization-loop acceptance.** ¢ pipeline 9 → 6 primitives, witnesses
   preserved (2 re-verified), accepted; iteration 2 (drop `recip`) rejected —
   reciprocal term generation is the witness machinery itself. ✓
4. **Named ledger.** 3 sorry with exact gaps (2 deliberate boundaries);
   7 named axioms; 1 refusal with named reason. `WOULD_BE_GUESS` appears
   exactly once — as the study's verdict on the physical constants. ✓
