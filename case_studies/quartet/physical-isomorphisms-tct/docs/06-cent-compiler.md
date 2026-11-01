# 06 — cent_compiler run: £ → ¢ → ∆ (TCT §12)

This study *is* a cent run, so the §12 output format is given in full.

## £ — Abstract Intent

Compile the goal *"evaluate a computational function with measurable
improvement"* into physical realization: find a substrate where the dominant
operation of the workload is a native physical interaction, solve there, map
the result back through the isomorphism.

## ¢ — Intermediate representation (22-primitive vocabulary)

The workload's dominant operations, compiled to `¢` (validated in
`scripts/column3/05_primitives_catalog.py`; 12 primitives used, each realized
in ≥ 2 domains):

| Primitive | Class | Computational role | Physical role (example) |
|---|---|---|---|
| `sum` | atomic | accumulation / dot products | Kirchhoff node sums currents |
| `mult` | atomic | products, scaling | translinear loop; gear differential |
| `rate` | atomic | clocks, sampling, frequencies | VCO; spin-torque oscillator |
| `sat` | atomic | clamping, argmax, decisions | amplifier limiter; clutch |
| `hysteresis` | atomic | latching, memory of outcome | Schmitt trigger; magnetic state |
| `spatial` | atomic | fields, mixing, FFT | beam propagation; channel flow |
| `exp` | atomic | nonlinearities, rates | diode I-V; Arrhenius |
| `log` | atomic | compressive scaling | log amplifier; pH |
| `delay` | atomic | pipelining, transport | transmission line; pipe delay |
| `accum` | atomic | integration | integrating capacitor; odometer |
| `eq` | composite | comparison, null detection | comparator; Wheatstone bridge |
| `state_space` | composite | ODE/PDE evolution | analog computer; spring-mass; RC |

Decomposition cost (optimization loop, docs/07): v1 = 11 primitives →
v2 = 7 for the crossbar pipeline: `state_space, sum, mult, rate, sat, eq,
delay`.

## ∆ — Physical substrates: two isomorphisms worked in full

### ∆1 — Electrical: memristor crossbar (solution in this domain)

Problem: N×N matrix-vector product. In the crossbar domain the solution is
"one clock": row voltages × conductances = column currents (that *is* the dot
product). Cost in this domain (script 01): `2N² + 7400N` energy units vs.
`12838N²` digital — break-even N = 55, ratio 6419× asymptotically.

### ∆2 — Optical: 4f Fourier system (solution in this domain)

Problem: convolution. In the optical domain the solution is "one propagation":
F(g∗h) = F(g)·F(h), and the lenses perform F physically. Cost (script 02):
setup `N²`, per frame `N+1`; wins over digital FFT for T ≥ 21 reuses;
latency 1 step vs. 51200 ops.

### Inverse mapping (∆ → £)

Both solutions map back through the same accounting: the *answer stream*
(digital-equivalent results at declared accuracy) is produced at the physical
cost, and the comparison is exact once I/O, conversion, precision, and reuse
are in the model. Remove any of those from the model and the result is
refused (`WOULD_BE_GUESS`), not reported.

## License ledger (§12 requirement)

- **Licensed analogies (axiom-class): 37 of 40** realizations — established
  engineering practice (Kirchhoff sums, translinear multipliers, 4f Fourier
  optics, VCO rates, latches, diode exponentials, Arrhenius, RC integration…).
- **Conjectural (sorry-class): 3** — `mult`/spintronic (torque-product),
  `log`/digital (LUT approximation), `state_space`/optical (cavity-mode
  general state space). Recorded as conjecture, not asserted.
- The coverage condition (each used primitive ≥ 2 domains) is executable:
  `MIN_DOMAINS=2`.

## Cross-study note

The Maudlin trilemma study's fluidic tie-break (a latch that needs an extra
variable to break a flow tie) is the same `sat` + `hysteresis` realization
used here for combinatorial decisions. The `¢` vocabulary is doing its job:
one notation for both studies.
