# Insights

## The answer to "measurable improvement" is a five-way, with one refusal

Physical isomorphisms improve computation in exactly the ways the physics is
better than arithmetic: **energy** (wires sum currents for free: 6419×),
**latency** (propagation replaces sequential steps: 51200 ops → 1; 1500 Euler
steps → 1 evolution), **amortization** (setup paid once: T ≥ 21), **sampling**
(noise is a free Bernoulli source), and **continuous time** (no discretization
until you need digits). And they refuse the sixth: complexity classes do not
move (ECT axiom; the quantum case honestly quarantined as open).

## Break-even thinking is the discipline that makes claims measurable

Every headline gain in this study survives only inside a model that includes
what physics hates: converters (7400N term → break-even N = 55), precision
(4 passes → N = 228), setup (N² writes → T = 21), noise floors (ε = 1/1000 →
M = 1500). The numbers are not decorations — they are the *locations of the
crossovers*, and each is witnessed twice (closed form + enumeration). A
speedup claim without its crossover is not a measurement; it is marketing —
`WOULD_BE_GUESS` under this study's rules.

## Isomorphisms preserve structure — including hardness

The SAT→Ising mapping (script 06) is exact: satisfaction and zero energy agree
on all 8 assignments. But exactness is not speedup — the 2ⁿ search space maps
onto 2ⁿ energy evaluations, and the cubic monomials in the mapping (computed:
16 slots, 6 surviving terms) are exactly the gadget overhead that quadratic
Ising hardware must pay. The isomorphism transfers the *problem*, faithfully,
including its difficulty. What it changes is the cost per unit of search —
massive physical parallelism — which is a constant-factor story, and the
literature's superlinear claims remain contested (docs/05).

## The ¢ vocabulary as a reusable lens

Twelve primitives cover all eight hurdles: `sum`, `mult`, `rate`, `sat`,
`hysteresis`, `spatial`, `exp`, `log`, `delay`, `accum`, `eq`, `state_space`.
The license catalog (37 licensed / 3 conjectural realizations, each primitive
in ≥ 2 domains) is the discipline that keeps analogy from becoming fantasy.
And the same vocabulary already paid for itself across studies: the Maudlin
study's fluidic latch (`sat` + `hysteresis`) and this study's Ising argmax
(`sat` + `hysteresis`) are the same two primitives in different substrates.

## The honest frontier

Two things this study does **not** settle: whether any physical substrate
beats optimized classical algorithms asymptotically on NP-hard problems
(no proven case), and whether quantum substrates change complexity classes
(unknown). Everything between those frontiers is measurable, and this study
measures it exactly.
