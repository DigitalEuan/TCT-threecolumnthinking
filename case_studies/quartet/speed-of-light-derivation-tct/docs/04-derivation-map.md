# 04 — Derivation map: what each route actually derives

Four derivation routes are often confused under "deriving c". Each row states
what the route delivers — and, crucially, what it does not.

## Route 1 — Symmetry and causality (analytic): existence

**von Ignatowski (1910).** From the relativity principle, homogeneity,
isotropy, and causality alone, the transformation between inertial frames
must be linear with a one-parameter addition law:

    x' = (x − vt) / (1 − κvx),   κ = 1/c²

Causality (no signal reversal) forces **κ ≥ 0**: either Galilean (κ = 0) or
a finite invariant speed (κ > 0). *Existence of a light cone is derivable;
its value is the free parameter κ.* Formal status here: premises as axiom
(`ignatowski_premises`); the algebraic development is analytic (docs/08).

## Route 2 — Electrodynamics (empirical computation): identification

**Maxwell (1861–65).** EM wave speed = 1/√(μ₀ε₀), computed from electrical
measurements; Weber–Kohlrausch's unit ratio (1856) matched optical c to the
era's accuracy (script 02: 36,517 ppm for WK; all three determinations within
5%). This *derived that light's speed is the EM speed* — the historically
genuine computational derivation. Its output was never "pure": measured
constants in, measured comparison out.

## Route 3 — Discrete dynamics (exact computation): cone speed

**Wave scheme (script 03) & Clifford circuits (script 04).** In any faithful
discrete dynamics, an invariant speed *emerges and is exactly computable*:

- integer wave scheme: characteristics move exactly Δx/Δt cells/step
  (edge speed 1 verified to t = 20, both implementations);
- Clifford brickwork: Pauli support grows ≤ 1 site/layer (exact GF(2),
  two implementations agree at every layer).

**What is derived:** a light cone with speed = grid ratio. **What is not:**
why *nature's* grid ratio corresponds to 299,792,458 m/s — that re-enters as
one empirical constant. (This is also where "digital physics" programs make
their strong claims: a hypergraph update rule with a characteristic speed.
The *cone* is derivable in such models; the *value* is fitted, not derived —
docs/05.)

## Route 4 — Microscopic bounds (rigorous computation): maximum signal speed

**Lieb–Robinson (1972).** For lattice Hamiltonians with coupling J and spacing
a, commutator propagation is bounded by v = 2Ja (exact rational for rational
J). Script 05: v = 1 at J = 1/2 — exactly the cone speed of routes 3a and 3b
(`FRAMEWORKS_MATCH=1`, `BOUND_TIGHT=1`). This is an *effective* speed of
light, rigorously derived from a Hamiltonian — the cleanest modern sense in
which "c is computable from a microscopic model".

## The synthesis

| Route | Derives | Needs empirical input? | Status here |
|---|---|---|---|
| 1 Ignatowski | invariant speed *exists* (κ ≥ 0) | no (causality) | axiom + docs |
| 2 Maxwell/WK | light's speed *is* 1/√(μ₀ε₀) | yes (electrical + optical measurements) | verified exactly (02) |
| 3a/3b lattice | cone speed *is* grid/layer ratio | value fitted, cone derived | verified exactly (03, 04) |
| 4 LR bound | max signal speed ≤ 2Ja | yes (J, a) | verified exactly (05) |
| — value route | α, hence c in natural units | **yes, always** (α measured) | **refused as derivation** (06) |

The map's shape mirrors the earlier studies' trilemma habit: separate the
claims, and the "mystery" decomposes into derivable structure + one measured
number + one definition + one refusal.
