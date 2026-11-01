# Classification ledger (TCT §14)

Identity: `n = p + s + a + r` → **24 = 13 + 3 + 7 + 1**

## Proved (13) — Python VERIFIED (6/6, isolated subprocesses)

1. π: three independent intervals (Machin / Euler / BBP) mutually overlap (01)
2. π: shared 13-digit block; widths < 10⁻²⁵ (01)
3. π: midpoint consistency across derivations (01)
4. e: two-path factorial sums agree; exact tail bound; 12-digit block (02)
5. φ: Cassini identity exact for n < 30 (02)
6. φ: quadratic residual exact; 12-digit block from convergent bracket (02)
7. √2: isqrt bracket contains the anchor exactly (02)
8. √2: Pell certificates p²−2q² = ±1 on 13 convergents (02)
9. ζ(2): tail < 1/N sandwiches π²/6 at N and 2N (03)
10. ζ(2)/ζ(4): 12-digit blocks match known values (03)
11. ζ(4): tail < 1/(3N³) sandwiches π⁴/90 (03)
12. ln 2: Mercator ∩ binary-series intervals; anchor + digits (04)
13. Catalan + γ + taxonomy: Catalan anchor; γ in two constructions with
    overlap; Champernowne two paths; class counts D/T/O/U/P = 5/5/4/1/4 (04, 05, 06)

Lean proved (6): `cassini_sample`, `pell_sample`, `phi_quadratic_sample`,
`e_partial_value`, `zeta2_partial_value`, `ln2_partial_value`.

## Sorry (3) — named gaps, development required

- `zeta2_tail_symbolic` — needs `linarith`/order reasoning (Mathlib) or
  manual cross-multiplication.
- `gamma_rational_target` — **deliberate, expected unproven**: γ's closed
  form/arithmetic type (irrationality itself = Erdős prize). Class-O boundary.
- `alpha_physical_target` — **deliberate, expected unproven** (trilogy link):
  parameter-free derivation of α; registered `WOULD_BE_GUESS`.

## Axioms (7) — named premises

- `pi_definition` — π = circle ratio (definitional).
- `e_definition` — e = lim(1+1/n)ⁿ (definitional).
- `analysis_convergence_premises` — alternating/telescoping/integral bounds.
- `euler_basel_identity` — ζ(2)=π²/6, ζ(4)=π⁴/90 (Euler 1735).
- `apery_theorem` — ζ(3) irrational (Apéry 1979).
- `gelfond_schneider` — e^π transcendental.
- `physical_constants_empirical` — α measured; c/h defined; G measured.

## Refused (1)

- "the physical constants (α and friends) are derivable from first
  principles" — **`WOULD_BE_GUESS`** (study 3's refusal carried over;
  `ALPHA_REFUSED=1` in script 06). Acceptance bar written in docs/05:
  definition+certificate or theorem — digit-matching is neither.

## Cross-check register (18 written; 4 defects fixed pre-verification; 18 live)

| Script | Cross-check pairs (disjoint derivation paths) |
|---|---|
| 01 | Machin vs. Euler vs. BBP intervals (3 pairwise overlaps); digit blocks ×3; midpoint consistency |
| 02 | e: direct sum vs. recurrence; φ: Cassini vs. quadratic residual; √2: isqrt vs. Pell |
| 03 | ζ(2): containment at N vs. 2N (shrinking); digit blocks; tail sandwich direction |
| 04 | ln 2: Mercator vs. binary series; anchor vs. digit-block methods |
| 05 | γ: t-series vs. H_n − ln n construction; interval overlap; width formula |
| 06 | Champernowne: string vs. position arithmetic; catalog counts; refusal stamp |

Audit findings (all resolved, see docs/07): 1 dead artifact removed;
truncation-anchor method replaced by digit-block witnesses; 1 alternating-
parity direction fixed; 1 Pell seed sign fixed. `c − t = 17 ≥ 2`. ✓
