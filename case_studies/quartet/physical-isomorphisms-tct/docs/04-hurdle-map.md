# 04 — Hurdle map: what physical isomorphisms overcome, and how

The second half of the study question: **which computational hurdles can be
overcome or worked around by physical isomorphisms?** Each row: the hurdle,
the isomorphism, the measured gain (exactly computed in this study), and the
caveat that keeps the claim honest.

## H1 — The von Neumann bottleneck (data movement dominates compute)

- **Hurdle.** A 32b DRAM read costs ~640 pJ while a 32b FP multiply costs
  3.7 pJ (Horowitz 2014): arithmetic is nearly free, *moving operands* is not.
- **Isomorphism.** Compute where the data already is: in-memory / in-situ
  analog computation (crossbar cells hold weights as conductances; Kirchhoff
  sums products at the sense line).
- **Measured (01).** Per MAC-equivalent: 6419× energy vs. von-Neumann digital,
  69× vs. in-memory digital. The gain is exactly the ratio of movement cost to
  physical compute cost.
- **Caveat.** The 6419× assumes both operands come from DRAM; with SRAM-resident
  data the honest ratio is 69×; converters shrink it further at small N.

## H2 — Quadratic/cubic linear algebra (GEMM, convolutions)

- **Hurdle.** Matrix-vector products cost N² sequential MACs; convolutions
  cost N² (direct) or 5N log₂N (FFT).
- **Isomorphism.** Crossbar dot-products (one physical step per output);
  4f optical systems (diffraction performs the Fourier transform in one
  propagation).
- **Measured (01, 02).** Break-even N = 55 vs. in-memory digital (8-bit
  converters); N = 228 at 32-bit effective precision. Convolution ratio
  512/25 (direct vs. FFT); optical wins for reuse T ≥ 21; latency 51200 ops
  → 1 propagation step.
- **Caveat.** Small N loses to converter overhead; low reuse loses to setup.

## H3 — Combinatorial optimization (NP-hard search landscapes)

- **Hurdle.** SAT, TSP, Ising ground states: exponential worst-case search.
- **Isomorphism.** Map the objective to physical energy
  (`E = −ΣJᵢⱼsᵢsⱼ − Σhᵢsᵢ`); let physical relaxation search (annealers,
  photonic Ising machines, simulated annealing).
- **Measured (06).** The SAT→energy mapping is exact (satisfy ⟺ E = 0 on all
  8 assignments of the instance); expansion cost: 16 mapping slots, 6
  surviving monomials, **cubic terms present** — a quadratic-only Ising form
  needs auxiliary spins.
- **Caveat (the honest core).** **No proven asymptotic speedup.** These are
  heuristics; reported speedups over optimized classical baselines are
  contested and instance-dependent. NP-hardness travels through the
  isomorphism intact — what physics buys is a *search heuristic with massive
  parallelism*, not a complexity-class escape.

## H4 — Randomness and sampling (Monte Carlo cost)

- **Hurdle.** Pseudo-random generation and sampling consume digital work;
  sampling error scales as 1/√N.
- **Isomorphism.** A noisy physical source *is* a Bernoulli sampler; stream
  computing turns multiplication into an AND gate.
- **Measured (03).** Exact binomial tail for N = 100 (two independent sums
  agree) sits under the Chebyshev bound 1/4; 1% error needs N ≥ 2500 bits
  (minimality sorry'd in Lean); stochastic multiply beats digital only for
  gate widths w ≥ 11 (w² > N).
- **Caveat.** Streams trade precision for gates: N bit-steps per op; for wide
  arithmetic digital multipliers win.

## H5 — Differential equations (sequential integration steps)

- **Hurdle.** Digital solvers pay one sequential step per increment; error
  falls only as steps grow.
- **Isomorphism.** Analog computers (RC integrators, spring-mass networks)
  integrate in continuous physical time (primitives `accum`, `state_space`).
- **Measured (04).** For y′ = 3t² with exact solution y(1) = 1: Euler error
  is exactly (3M−1)/(2M²); matching a 1/1000 analog error floor needs
  M = 1500 steps vs. 1 physical evolution — a 1500:1 step ratio at the
  declared accuracy.
- **Caveat.** The floor is fixed: digital precision keeps improving past 1/1000
  with more steps; analog wins only when the required accuracy is at or above
  its floor.

## H6 — Interconnect and transport latency

- **Hurdle.** Moving signals across a chip/board costs cycles.
- **Isomorphism.** Optical/RF transport: propagation latency is set by
  physics, and diffraction mixes spatial data for free (`spatial`).
- **Measured (02).** Constant-latency step in the convolution model
  (`LATENCY_RATIO = 51200` at N = 1024).
- **Caveat.** Conversion and readout latency is real (2N terms in our model).

## H7 — Precision walls

- **Hurdle.** Analog deliverables are ~6–10 bits; some tasks need 32+.
- **Workaround.** Mixed-signal passes: use analog for the bulk, digital for
  refinement; quantized/stochastic number representations.
- **Measured (01).** At 32-bit effective precision (4 × 8-bit passes), the
  crossbar break-even moves from N = 55 to N = 228 — the honest cost of
  precision, exactly quantified.
- **Caveat.** Some workloads never amortize high precision; digital wins.

## H8 — Flexibility and build cost (special-purpose physics)

- **Hurdle.** A physical solver is fixed-function; the workload must justify
  the build.
- **Workaround.** Amortization: one-time setup (kernel programming, N²
  writes) spread over many uses; reconfigurable substrates (SLMs, memristor
  crossbars).
- **Measured (02).** Break-even reuse T = 21 in the optical model.
- **Caveat.** Below break-even, general-purpose digital wins outright.

## Summary matrix

| Hurdle | Isomorphism | Gain (this study) | Status |
|---|---|---|---|
| H1 data movement | in-situ / in-memory compute | 6419× / 69× energy | verified (model-dependent) |
| H2 linear algebra | crossbar / optical FFT | break-even N=55/228; 512/25; T=21 | verified (model-dependent) |
| H3 NP-hard search | Ising/annealing | exact mapping; no proven speedup | **open / heuristic** |
| H4 randomness | physical noise streams | tail bounds exact; N≥2500 @1% | verified (tradeoffs honest) |
| H5 ODE/PDE | analog integration | 1500:1 steps at 1/1000 floor | verified (floor-limited) |
| H6 transport | optics | constant-latency step | verified (model) |
| H7 precision | mixed-signal passes | break-even shift 55→228 | verified |
| H8 flexibility | amortization | T ≥ 21 | verified (model) |
