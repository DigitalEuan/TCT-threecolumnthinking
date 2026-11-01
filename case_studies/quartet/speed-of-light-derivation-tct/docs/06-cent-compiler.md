# 06 — cent_compiler run: £ → ¢ → ∆ (TCT §12)

## £ — Abstract Intent

Compile *"derive the speed of light"* into the 22-primitive vocabulary and
look for domains where the derivation is native. The insight from the run:
what physics/computation natively derives is **causal propagation** (a cone),
not a number — so the compilation targets propagation, and the number is
tracked as an input parameter wherever it appears.

## ¢ — Intermediate representation

The light-cone derivation pipeline (v2 after optimization, docs/07):

| Primitive | Role in the derivation |
|---|---|
| `state_space` | the field/circuit/Hamiltonian state being propagated |
| `sum` | superposition of modes / Huygens wavelets |
| `mult` | coupling strengths (J, LC products), scaling |
| `rate` | frequency/time-step mapping |
| `delay` | propagation: one cell/layer per step — the cone itself |
| `spatial` | the lattice/field geometry carrying the cone |
| `eq` | characteristic/equality checks (stability, matching) |

Cost: v1 (10 primitives) → v2 (7), witnesses preserved.

## ∆ — Physical substrates: three isomorphisms

**∆1 — Electrical: the transmission line (telegrapher's equation).**
A lossless line with inductance L and capacitance C per unit length
propagates voltage waves at v = 1/√(LC) — squared form exact: v² = 1/(LC).
With L = C = 1 (declared units): v = 1 exactly — the same cone as the integer
wave scheme. This is Maxwell's 1850s problem in a wire: the speed of light is
the wave speed of the EM field, and the transmission line is the EM field
modeled as circuits. **Licensed** (standard transmission-line theory).

**∆2 — Fluidic: the water-hammer wave.**
A pressure wave in an incompressible pipe travels at v = √(K/ρ) (K bulk
modulus, ρ density); squared form v² = K/ρ exact for rational K, ρ. The same
`state_space`+`delay`+`spatial` cone structure. **Licensed** (Joukowsky 1898).

**∆3 — Mechanical: the taut string.**
Wave speed v = √(T/μ) (tension T, linear density μ); v² = T/μ exact.
The discrete version is literally script 03's scheme (masses + springs),
whose cone speed is Δx/Δt. **Licensed** (elementary wave mechanics).

### Inverse mapping (∆ → £)

Each domain realizes the same derivation: **a wave equation on a medium has a
characteristic speed set by the medium's constants — and that characteristic
speed is what "the speed of light" means for the EM medium.** The value in SI
units re-enters only through measured constants (L, C; K, ρ; T, μ) or the
unit definition. The structural part of "derive c computationally" is fully
compiled; the value part appears in every domain as exactly one parameter —
consistent with the B4 boundary.

## License ledger (§12)

| Analogy | License | Status |
|---|---|---|
| transmission line v² = 1/(LC) ↔ wave cone | physical law (telegrapher's equation) | licensed |
| water hammer v² = K/ρ ↔ wave cone | physical law (Joukowsky) | licensed |
| taut string v² = T/μ ↔ wave cone | physical law (elementary) | licensed |
| Clifford circuit cone ↔ physical cone | structural (discrete dynamics) | licensed for the cone; **conjectural** as a model of nature's light |
| hypergraph/digital-physics cone ↔ physical cone | contested research program | **conjectural** — value is fitted (docs/05) |
| lattice LR bound ↔ relativistic c | rigorous theorem + modeling premise | licensed for the bound; premise axiom-class |

Conjectural entries are recorded as sorry-class in the cent ledger, not
asserted (TCT §12).
