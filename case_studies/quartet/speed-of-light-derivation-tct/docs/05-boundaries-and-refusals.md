# 05 — Boundaries and refusals: what we hit, and how we handled it

This question was expected to "cause all sorts of issues". It did. Here is
every boundary encountered and the disposition applied.

## B1 — The definitional trap

**Issue.** "Derive 299,792,458" is unsatisfiable as stated: since the 1983
meter definition (and 2019 SI), the number is exact by decree. A script that
prints it derives nothing.
**Disposition.** Computed the full definitional chain exactly (script 01) and
stamped `DEFINITIONAL=1` — the triviality is witnessed, not just asserted.
The claim "computation produced c" is thereby distinguished from "computation
derived c".

## B2 — Circularity in the constants

**Issue.** The tempting modern computation c = 1/√(μ₀ε₀) is circular today:
post-2019, μ₀ is measured *from* α and c is defined; ε₀ is derived from μ₀
and c. Feeding modern constants back into Maxwell's formula produces the
definition, not a derivation.
**Disposition.** Used the historically *non-circular* route instead: the
Weber–Kohlrausch unit ratio (1856) and the optical determinations as separate
empirical legs, compared exactly (script 02). The circularity is documented,
not hidden — this is why the modern-formula route is B2-*era-verified* only
in its 19th-century instantiation.

## B3 — "Emergent c" claims across frameworks

**Issue.** Many frameworks "derive" a speed of light: lattice field theory,
cellular automata / hypergraph rewriting, analog gravity (sonic horizons),
condensed-matter cones (Lieb–Robinson). Which claims are derivations and
which are fits?
**Disposition.** Split by what is computed:
- *derived exactly*: the cone speed of a given scheme (scripts 03–04: edge
  speed, support growth — enumerable, two implementations each);
- *derived rigorously*: LR bound 2Ja from a Hamiltonian (script 05);
- *fitted, not derived*: why nature's cone speed is 299,792,458 m/s — in
  every one of these frameworks the grid ratio / coupling / metric is an
  input. Digital-physics programs (e.g. hypergraph-update proposals) are
  recorded at exactly this status: cone derivable; value parameter-fitted;
  strong claims remain contested.

## B4 — The value claims (numerology lineage)

**Issue.** A long lineage claims closed derivations of 1/137: Eddington's
"proof" of α⁻¹ = 136 + 1 (with escalating corrections), and modern
"purely mathematical derivations" landing within a few σ of CODATA. These are
the specific artifacts the question promises to stir up.
**Disposition.** `REFUSED: WOULD_BE_GUESS`. The taxonomy's trigger: no
licensed derivation path from stated premises; and the signature pattern —
free parameters tuned post-hoc to the measured value, no independent
parameter-free predictions. Acceptance bar (stated, not vague): a derivation
must fix α *and* predict other constants with no fitted input. None has. The
Lean tier carries `alpha_from_premises` as the deliberate unproven target so
the boundary is visible in the formal ledger, not just in prose.

## B5 — Units vs. dimensionless values

**Issue.** Statements like "c is exactly 299,792,458" vs. "c ≈ 137 in atomic
units" seem contradictory to newcomers.
**Disposition.** Kept the layers separate throughout: SI value (definition,
script 01), historical determinations (measurements, script 02), dimensionless
value 1/α (one measured constant, script 06). The study's core distinction —
**structure derivable, value measured** — is exactly this layering.

## Refusal register

| Claim | Disposition | Reason |
|---|---|---|
| "c's number derived from pure computation" | REFUSED | `WOULD_BE_GUESS` — definitional or fitted, never derived |
| "α has a closed-form derivation" (Eddington-class, modern preprints) | REFUSED | `WOULD_BE_GUESS` — no independent parameter-free predictions |
| "digital physics predicts c" | QUALIFIED | cone derived; value parameter-fitted (B3) |
| "modern c = 1/√(μ₀ε₀) is an independent derivation" | REFUSED-as-circular | `INCONSISTENT_GIVENS`-class: post-2019 constants contain c already |

Everything not in this register is either proved (11 claims), honestly
axiomatic (7), or a named open problem (3 sorry, one deliberate).
