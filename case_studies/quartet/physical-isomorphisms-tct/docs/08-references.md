# 08 — References

## Empirical basis

- **Horowitz, M.** (2014). "Computing's Energy Problem (and what we can do
  about it)." *IEEE ISSCC 2014*. — the energy figures used as givens: 32b FP
  multiply ≈ 3.7 pJ, 32b add ≈ 0.1 pJ, 32b SRAM read ≈ 5 pJ, 32b DRAM read
  ≈ 640 pJ (45nm-class; all our ratios scale with these).
- **Strukov, D., Snider, G. S., Stewart, D. R., Williams, R. S.** (2008).
  "The missing memristor found." *Nature* 453, 80–83. — crossbar substrate.
- Analog/crossbar converter-overhead analyses: e.g. "Gravitating Towards the
  Physical Limits of Crossbar Acceleration" (arXiv:1803.06913); ADC overhead
  as the dominant crossbar cost is the standard finding this study models as
  the 7400N term.

## Physical computation theory

- **Feynman, R. P.** (1982). "Simulating Physics with Computers."
  *International Journal of Theoretical Physics* 21, 467–488. — the origin of
  computing-by-physical-isomorphism as a program.
- **Bennett, C. H., Landauer, R.** (1985). "The fundamental physical limits of
  computation." *Scientific American* 253(1), 48–56.
- **Vergis, A., Steiglitz, K., Dickinson, B.** (1986). "The complexity of
  analog computation." *Mathematics and Computers in Simulation* 28, 91–113.
- **Blum, L., Shub, M., Smale, S.** (1989). "On a theory of computation and
  complexity over the real numbers." *Bulletin of the AMS* 21, 1–46. — analog
  models and precision/noise caveats.
- **Bournez, O., Pouly, A.** (2020). "Analog Models of Computation." In:
  *Handbook of Computability and Complexity in Analysis*. — survey of when
  physical/analog systems compute what.

## Stochastic & stream computing

- **von Neumann, J.** (1956). "Probabilistic logics and the synthesis of
  reliable organisms from unreliable components." In: *Automata Studies*
  (Shannon & McCarthy, eds.). — noisy components, probabilistic logic.
- **Alaghi, A., Hayes, J. P.** (2013). "Survey of stochastic computing."
  *ACM Transactions on Embedded Computing Systems* 12(2s), 92. — stream
  representations, AND-multiplication, correlation caveats.

## Optimization substrates

- **Kirkpatrick, S., Gelatt, C. D., Vecchi, M. P.** (1983). "Optimization by
  simulated annealing." *Science* 220, 671–680.
- **Boixo, S. et al.** (2014). "Evidence for quantum annealing with more than
  one hundred qubits." *Nature Physics* 10, 218–224.
- **Rønnow, T. F. et al.** (2014). "Defining and detecting quantum speedup."
  *Science* 345, 420–424. — how contested speedups are measured.
- **Albash, T., Lidar, D. A.** (2018). "Adiabatic quantum computation."
  *Reviews of Modern Physics* 90, 015002. — status of annealing speedup
  claims: no general proven speedup.

## Optical & analog function mapping

- **VanderLugt, A.** (1964). "Optical signal processing." *IEEE Transactions
  on Information Theory* — 4f correlator: Fourier transforms by lenses.
- **Jaeger, H.** (2001). "The 'echo state' approach to analysing and training
  recurrent neural networks." GMD Report 148. — reservoir computing: physics
  as a fixed computational substrate, trained readout only.

## Methodology

- **Craig, E. R. A. (DigitalEuan).** *Geometric Language Machine (GLM)*,
  §§2.2–2.3, 12, 17, 19.3, 24. https://github.com/DigitalEuan/GLM — Three
  Column Thinking, UBP, cent_compiler cross-domain mode, optimization loop.

## Premise note

The extended Church-Turing thesis (efficient digital simulability of physical
systems) is carried as an **axiom**, not a result; its quantum caveat (BQP vs
BPP) is open and is explicitly excluded from all claims. All measured gains in
this study are relative to the declared cost models in scripts 01–06 and
re-verify exactly against them.
