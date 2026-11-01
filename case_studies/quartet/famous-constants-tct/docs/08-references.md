# 08 — References

## Derivations and series

- **Machin, J.** (1706). "The quadrature of the circle." —
  π/4 = 4·arctan(1/5) − arctan(1/239).
- **Euler, L.** (1735). "De summis serierum reciprocarum" (the Basel
  problem): Σ1/n² = π²/6; and the sine-product argument
  (Introductio, 1748) for ζ(2k) = rational·π^{2k}, incl. ζ(4) = π⁴/90.
- **Bailey, D. H., Borwein, P., Plouffe, S.** (1997). "On the rapid
  computation of various polylogarithmic constants." *Math. Comp.* 66. — the
  BBP formula for π (hex digits without predecessors).
- **Euler–Mascheroni constant**: Euler (1735) introductio/Commentarii;
  standard definition γ = lim(H_n − ln n).

## Arithmetic type and open problems

- **Apéry, R.** (1979). "Irrationalité de ζ(2) et ζ(3)." *Astérisque* 61. —
  ζ(3) irrational; the rapid-convergence approximants.
- **Gelfond–Schneider theorem** (1934): α^β transcendental for algebraic
  α≠0,1 and irrational algebraic β ⇒ e^π = (−1)^{−i} is transcendental.
- **Chaitin, G. J.** (1975). "A theory of program size formally identical to
  information theory." *JACM* 22. — Ω: definable, uncomputable.
- **Erdős prize**: open problem status of γ's irrationality; see e.g.
  "List of unsolved problems in mathematics" (rationality of γ and of
  Catalan's constant listed as open in the standard references).
- **Finch, S. R.** (2003). *Mathematical Constants.* Cambridge University
  Press. — the catalog sourcebook (incl. Glaisher–Kinkelin, Khinchin,
  Conway's constant).
- **Borwein, J., Bailey, D., Girgensohn, R.** (2004). *Experimentation in
  Mathematics.* — experimental mathematics and certificate discipline.

## Cautionary lineage (the numerology guardrail)

- **Eddington, A. S.** (1929+): algebraic "derivations" of 1/137 — the
  canonical shifting-target lineage (docs/05's guardrail class).
- Modern preprint claims of closed-form α or 137 derivations — graded
  `WOULD_BE_GUESS` until they meet the acceptance bar (definition+certificate
  or theorem).

## Physical occurrences (cent ∆ ledger)

- Planck's black-body sums (ζ(4) = π⁴/90 in the Stefan–Boltzmann constant);
  RC decay (e); phyllotaxis (φ); random-walk returns (ζ(2)-class sums);
  Feynman periods (ζ(3) and beyond — research-level, marked conjectural).

## Methodology

- **Craig, E. R. A. (DigitalEuan).** *Geometric Language Machine (GLM)*,
  §§2.2–2.3, 12, 17, 19.3, 24. https://github.com/DigitalEuan/GLM — Three
  Column Thinking, UBP discipline, cent_compiler, optimization loop.

## Premise note

Known digit blocks are used strictly as *independent witnesses* (digit-block
checks), never as derivation inputs. Analytic facts (alternating-series
bounds, Euler's product identity, Apéry, Gelfond–Schneider) are axiom-class
premises; all arithmetic in the six scripts is re-derived exactly. The
deliberate `sorry`s (`gamma_rational_target`, `alpha_physical_target`)
record the study's boundaries: γ's arithmetic type and α's value are the
famous-constants question's two hard walls.
