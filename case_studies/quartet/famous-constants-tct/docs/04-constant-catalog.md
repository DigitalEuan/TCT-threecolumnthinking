# 04 — The constant catalog: basic set, advanced family, and the far shore

The full map the question asks for — each constant with its class, its
derivation route, and its exact status in this study.

## The basic set (class D — definitional; fully derivable)

| Constant | Definition | Route used here | Exact status |
|---|---|---|---|
| π | circle ratio / 2× smallest positive cosine zero | Machin + Euler arctan + BBP, three overlapping rational intervals | 13-digit block shared; widths < 10⁻²⁵ (`01`) |
| e | lim(1+1/n)ⁿ = Σ1/k! | factorial series + exact tail bound, two paths | 12-digit block (`02`) |
| φ | [1;1,1,1,…] = (1+√5)/2 | Fibonacci convergents + exact certificates | Cassini + residual exact (`02`) |
| √2 | x² = 2, x > 0 | isqrt brackets + Pell convergents | p²−2q² = ±1 exact (`02`) |
| Champernowne | 0.123456789101112… | concatenation vs. position arithmetic | two paths agree (`06`) |

## The advanced family (class T — theorem-determined)

| Constant | Theorem pinning it | Route used here | Status |
|---|---|---|---|
| ln 2 | Mercator series | alternating + binary series, overlapping intervals | 12-digit block (`04`) |
| ζ(2) = π²/6 | Euler's Basel problem (1735) | partial sums + tail < 1/N vs. π²/6 interval | sandwiched at N and 2N (`03`) |
| ζ(4) = π⁴/90 | Euler | partial + tail < 1/(3N³) | sandwiched (`03`) |
| ζ(3) (Apéry) | **irrational** (Apéry 1979) | partial sums + tails (computable) | irrationality theorem assumed (`apery_theorem`); **no closed form** → leans into class O |
| e^π (Gelfond) | **transcendental** (Gelfond–Schneider) | value is computable; type is pinned by theorem | status as theorem (`gelfond_schneider`) |
| Catalan G | none pinning the value | alternating series with certificates | computable (`04`); **closed form open** → class O lean |

## The open problems (class O — the famous edge)

| Constant | What is known | What is open | Formal record |
|---|---|---|---|
| γ (Euler–Mascheroni) | definable; computable to any precision with rigorous intervals (`05`) | **irrationality itself** (Erdős prize); no closed form | `gamma_rational_target` (deliberate sorry) |
| ζ(5) | computable; Apéry-like irrationality unknown | closed form; irrationality | docs/05 |
| ζ(3) closed form | irrational (theorem) | any closed form in familiar constants | docs/05 |
| Catalan G closed form | computable to any precision | closed form; irrationality | docs/05 |

## The uncomputable shore (class U)

| Constant | Definition | Status |
|---|---|---|
| Chaitin's Ω | halting probability of a universal prefix machine | **definable from first principles; digits algorithmically uncomputable.** "Derivable" and "computable" come apart here — the diagonal of the constant world |

## The physical family (class P — the trilogy's boundary)

| Constant | Status | Derivation claim |
|---|---|---|
| α (fine structure) | measured (CODATA 2018) | **REFUSED: WOULD_BE_GUESS** — `alpha_physical_target` (deliberate sorry); carries study 3's boundary verbatim |
| c, h | SI-defined exact (2019) | definitional (bookkeeping, as in study 3's B1) |
| G (Newton) | measured | no accepted theoretical derivation; same refusal class |

## Reading the table

The question's "basic set, advanced family, fine structure and more" maps
onto a genuine mathematical coastline: **D** (fully derivable, exact
certificates) → **T** (theorem-pinned, series-computable) → **O** (computable
but open) → **U** (definable but uncomputable) → **P** (measured, refused).
Every row of this table is backed by either a verified script key, a named
axiom, or a named refusal — nothing is hand-waved.
