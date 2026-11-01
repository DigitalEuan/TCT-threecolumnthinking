# 05 — The first-principles ladder: what "derivation" means per class

## The ladder

1. **Definition → value (class D).** A definition plus an algorithm plus a
   certificate. π is "the circle ratio"; the *derivation* is the convergent
   machinery (Machin/BBP) and the proof that the error shrinks (alternating
   bounds). The certificate is what separates derivation from numerology: every
   interval here is *provably* tight, not just converging-looking.
2. **Theorem → value (class T).** Something pins the constant: ζ(2) = π²/6
   because of Euler's product; e^π is transcendental by Gelfond–Schneider.
   Derivation = theorem + series. The theorem is an axiom-class premise here
   (its proof lives in analysis/Mathlib — recorded as
   `analysis_convergence_premises` and `euler_basel_identity`).
3. **Definition without closure (class O).** γ is fully *defined* — and yet
   nobody can say whether it is rational. Computability ≠ closed form ≠
   arithmetic type. This is where "derive from first principles" starts to
   mean "wait for a theorem nobody has".
4. **Definition without computation (class U).** Ω is defined from first
   principles and its digits cannot be computed — at all, ever, by any
   algorithm. The phrase "derived from first principles" survives; the phrase
   "computed" does not.
5. **Measurement (class P).** Physical constants are neither D nor T: α is
   *found*, not unfolded. The trilogy's refusal lives here.

## The open problems, named

- **γ's arithmetic type** — rational or not is unknown (Erdős prize). The
  study computes rigorous intervals and stamps `GAMMA_IRRATIONALITY=UNKNOWN`.
- **ζ(5), ζ(7), …** — no closed forms; even irrationality of ζ(5) is open
  (Apéry's method has not cracked the higher odd zeta values).
- **Catalan's constant** — no closed form; arithmetic type open in the
  standard references cited here.
- **ζ(3)'s closed form** — irrational (Apéry 1979), still closed-form-free.
- **α, G** — physical; derivation claims refused (below).

## The numerology guardrail

The famous-constants attractor has a gravitational field: "derivations" of
1/137 (Eddington lineage), of π from the Great Pyramid, of e from scripture
calendar arithmetic. The taxonomy's refusal trigger (same as study 3):
`WOULD_BE_GUESS` whenever a claim has no licensed derivation path — no
definition→algorithm→certificate chain and no theorem. The acceptance bar is
structural: **a derivation must come with either (a) a definition plus a
computable certificate (D), or (b) a theorem (T).** Matching digits is
neither. This study applies the bar in both directions: it refuses to derive
α, and it refuses to pretend γ is closed — while happily *computing* both
with honest bounds.

## Why the classes are a fun answer and a rigorous one at once

Each class boundary is itself a famous result: Apéry (1979) split ζ(3) from
"mere constant" into "provably irrational"; Gelfond–Schneider settled e^π's
type; Turing/Chaitin showed definability without computability; and the
SI/physics boundary was the subject of study 3. The question "how can the
famous constants be derived from first principles?" has as its answer not a
list of formulas but **this stratification** — and every stratum has a
verified witness in this repository.
