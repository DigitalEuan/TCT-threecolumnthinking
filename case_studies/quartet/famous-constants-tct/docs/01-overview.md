# 01 — Overview: famous constants from first principles

## The question, and its hidden plural

"How can the famous mathematical constants be derived from first principles?"
is secretly several questions wearing one coat — and the fun of the study is
sorting the coat rack. The constants divide into **five classes**, and which
class a constant lands in completely determines what "derivation" can mean:

| Class | Meaning of "first principles" | Members | Status |
|---|---|---|---|
| **D** — definitional | unfold a definition to any precision, with exact rational certificates | π, e, φ, √2, Champernowne | fully derivable ✓ |
| **T** — theorem-determined | a theorem pins the value; series give rigorous rational intervals | ln 2, ζ(2) = π²/6, ζ(4) = π⁴/90, ζ(3) (irrational, Apéry 1979), e^π (transcendental, Gelfond–Schneider) | derivable ✓ (closed form varies) |
| **O** — open | definable, computable to any precision — but no closed form; some properties unknown | γ (irrationality = Erdős prize!), ζ(5), Catalan's closed form, ζ(3)'s closed form | **boundary** |
| **U** — uncomputable | definable from first principles, yet no algorithm computes its digits | Chaitin's Ω | derivable *as a definition*; digits forever out of reach |
| **P** — physical | measured or unit-defined | α (fine structure), G, c/h (SI) | **refused** — study 3's boundary carries over |

## What this study computes (all exact, no floats)

- **π by three independent derivations** — Machin (1706), Euler's arctan
  identity, and BBP (1995) — each producing rigorous rational intervals that
  mutually overlap and share π's known 13 leading digits (`01`).
- **e** by two summation paths with exact tail bounds; **φ** via Fibonacci
  convergents with exact Cassini certificates `F_{n+1}² − F_n F_{n+2} = (−1)^n`
  and the quadratic residual (φ² = φ + 1!); **√2** via integer `isqrt`
  brackets *and* Pell certificates `p² − 2q² = ±1` (`02`).
- **ζ(2) = π²/6 and ζ(4) = π⁴/90** — Euler's Basel problem — with rigorous
  tail sandwiches (`1/N`, `1/(3N³)`) and shrinking-width containment (`03`).
- **ln 2** by two genuinely different series (Mercator alternating vs. the
  binary series Σ1/(k2^k)) whose intervals must overlap; **Catalan's
  constant** with alternating-series certificates (`04`).
- **γ** — the celebrity of the open class — bracketed two independent ways
  (t-series with Mercator/ln2 brackets vs. the H_n − ln n definition with
  integral sandwiches), with the honest stamp
  `GAMMA_IRRATIONALITY=UNKNOWN` (`05`).
- **The classification machine** itself: Champernowne digits by two disjoint
  paths, the five-class catalog validated, and the physical-constant refusal
  carried over from the trilogy (`06`).

## The two boundaries, and why they're different

**γ is derivable-as-a-definition but not closed-form.** Nobody knows whether
γ is rational (Erdős offered a prize). This study computes it to any
precision with *rigorous* rational intervals — but the moment you ask for a
closed form or an irrationality proof, you hit class O. Formal record: Lean
`sorry` `gamma_rational_target` — deliberate, expected unproven.

**α is not even definable-as-a-value.** Unlike γ, α isn't waiting for a
clever identity — no accepted parameter-free derivation exists at all. The
trilogy's refusal stands: `REFUSED: WOULD_BE_GUESS`, formal record
`alpha_from_premises`/`alpha_physical_target`. The famous-constants question
and the speed-of-light question meet *exactly here*.

## And the genuinely weird one

**Chaitin's Ω**: defined from first principles (halting probability of a
universal prefix machine), yet its digits are algorithmically uncomputable —
each digit is mathematically determined and forever unreachable. "Derivable
from first principles" and "computable" come apart. Class U exists, and
no amount of convergent-series cleverness (the D/T toolkit of scripts 01–05)
touches it.

## The one-paragraph answer

Famous constants are derivable from first principles in exactly the senses
their class allows: D/T constants get rigorous rational intervals from
definitions and theorems (computed here, double-path, certificate-bounded);
O constants like γ are computable but resist closed form (the famous open
problems, kept open on the ledger); Ω is definable yet uncomputable; and the
physical constants — the question's "Fine Structure Constant and more" —
stay measured, with the trilogy's refusal in place. The fun and the rigor are
the same fact: *the map of which "first principles" work for which constant
is itself exactly derivable.*
