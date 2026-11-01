# 08 — References

## The definition

- **BIPM**, *SI Brochure* (9th ed., 2019 update): the meter defined via
  c = 299,792,458 m/s exactly (fixed 1983); ampere/μ₀ redefinitions 2019.

## Historical determinations and the EM identification

- **Weber, W., Kohlrausch, R.** (1856). "Ueber die Elektricitätsmenge, welche
  bei galvanischen Strömen durch den Querschnitt der Kette fliesst."
  *Annalen der Physik* 175. — the EM/ESU charge-unit ratio ≈ 3.1074×10¹⁰ cm/s.
- **Fizeau, H.** (1849). "Sur une expérience relative à la vitesse de
  propagation de la lumière." *Comptes Rendus* 29, 90. — toothed wheel,
  ≈ 313,300 km/s.
- **Foucault, L.** (1862). "Détermination expérimentale de la vitesse de la
  lumière." *Comptes Rendus* 55. — rotating mirror, ≈ 298,000 km/s.
- **Maxwell, J. C.** (1865). "A Dynamical Theory of the Electromagnetic
  Field." *Phil. Trans. R. Soc.* 155, 459–512. — c = 1/√(μ₀ε₀); light as EM
  waves. See also "On Physical Lines of Force" (1861–62) and the comparison
  with Weber–Kohlrausch and Fizeau.
- **O'Hanian, H. C.** (2006). "The story of c." *American Journal of Physics*
  74, 995. — the ratio-of-units route to c.

## Existence of the invariant speed

- **von Ignatowski, W.** (1910). "Über die mechanischen Grundlagen der
  Relativitätstheorie." *Annalen der Physik* 338, 1061–1088. — Lorentz
  transformations from relativity + causality; κ ≥ 0.

## Light cones from discrete/microscopic dynamics

- **Courant, R., Friedrichs, K., Lewy, H.** (1928). "Über die partiellen
  Differenzengleichungen der mathematischen Physik." *Math. Annalen* 100. —
  the CFL condition: numerical domain of dependence.
- **Yee, K. S.** (1966). "Numerical solution of initial boundary value
  problems involving Maxwell's equations." *IEEE Trans. Antennas Propag.* 14. —
  FDTD; numerical light cones and dispersion.
- **Lieb, E. H., Robinson, D. W.** (1972). "The finite group velocity of
  quantum spin systems." *Comm. Math. Phys.* 28, 251–257. — v = 2Ja bounds.
- **Nachtergaele, B., Sims, R.** (2006). "Lieb-Robinson bounds and the
  exponential clustering theorem." *Comm. Math. Phys.* 265. — modern form.
- **Barceló, C., Liberati, S., Visser, M.** (2005). "Analogue gravity."
  *Living Reviews in Relativity* 8. — emergent cones (sonic horizons) and
  their status as *analogies*, not derivations of nature's c.

## The value boundary

- **CODATA 2018 / 2022** recommended values: α = 7.2973525693(11)×10⁻³,
  α⁻¹ = 137.035999084(21). — measured, not derived.
- **Eddington, A. S.** (1929+). The "algebraic" derivations of 1/137 — the
  canonical cautionary lineage (near-misses, shifting corrections).
- Modern "purely mathematical derivation" claims (e.g. preprints matching
  CODATA within a few σ) — treated as numerology-class by the refusal
  taxonomy (docs/05) until they deliver parameter-free independent
  predictions.

## Methodology

- **Craig, E. R. A. (DigitalEuan).** *Geometric Language Machine (GLM)*,
  §§2.2–2.3, 12, 17, 19.3, 24. https://github.com/DigitalEuan/GLM — Three
  Column Thinking, UBP discipline, cent_compiler, optimization loop.

## Premise note

Empirical values (historical determinations, α) are carried as axiom-class
premises; the SI value is carried as a *definitional* premise. All structural
claims (cones, bounds, comparisons, intervals) are re-derived exactly in this
repository. The claim "α is derivable from theory alone" is carried as a
**refused** claim with the deliberate Lean `sorry` `alpha_from_premises` as
its formal record.
