#!/usr/bin/env python3
"""Rebuild the Run D edition of tct_paper.md from the session-1 edit sequence
(baked-in fixes: conclusion line-wrap; applied to a fresh copy of the upload)."""

PAPER = "/home/z/my-project/download/tct_paper.md"

EDITS = []


def edit(old, new):
    EDITS.append((old, new))


# E1 - abstract
edit(
"""mode. We evaluate the skill on two conceptual physics questions ("how does a
spring store and release energy?" and "why do things bounce?") across three
independent runs: Run A (this environment, with the skill's bundled tooling),
Run B (Claude.ai, first version of the skill, no bundled scripts, stand-in
checker), and Run C (Claude.ai, revised skill with embedded scripts and hardened
optimisation loop). All three runs produced exact, independently re-verified
answers; the revision closed every defect surfaced by Run B (missing scripts,
over-strong Lean tactic claim, silent loss of cross-checks during optimisation,
undeclared illustrative givens, toolchain guessing). Beyond verification, the
runs reveal the "why" of TCT: the protocol forces into the open exact-rational
witness construction, calculus-free exact witnesses, quantified approximation
error, and the distinction between counted and independent checks. Remaining
gaps are identified: cross-check *independence* (tautologies can inflate
counts), unconfirmed `decide` on `ℚ` without Mathlib, output-format column fit
for multi-line checks, and uncompiled Lean tiers in all runs.""",
"""mode. We evaluate the skill first on two conceptual physics questions ("how does a
spring store and release energy?" and "why do things bounce?") across three
independent runs: Run A (dola.com's AI system, with the skill's bundled tooling),
Run B (Claude.ai, first version of the skill, no bundled scripts, stand-in
checker), and Run C (Claude.ai, revised skill with embedded scripts and hardened
optimisation loop). All three runs produced exact, independently re-verified
answers; the revision closed every defect surfaced by Run B (missing scripts,
over-strong Lean tactic claim, silent loss of cross-checks during optimisation,
undeclared illustrative givens, toolchain guessing). We then evaluate the
*updated* skill — now carrying a four-conditions "optimal construction" runbook
(classification identity, tautology-audited cross-checks, loop acceptance rule,
named ledger) — on a broad twelve-question battery spanning eight domains
("what is gravity?", water's anomalous expansion, "what comes after
Wednesday?", "what is 1+1?", combinatorics, compound interest, sequence
continuation, and parity at a declared 𝔽₂ site) in Run D,
again on dola.com's AI system, this time with a Lean 4.35 toolchain installed
in-environment: the study's first run in which every Lean project is actually
compiled. Run D verified all twelve answers (31/31 Tier-1 spot checks; 12/12
`lake build`), exercised the refusal taxonomy twice with machine-checked
justifications, and both corrected and extended the skill's Lean guidance:
`decide` and `rfl` fail on `Rat` in pure core (the Nat cross-multiplication
pattern is the only kernel-checked route), `omega` and `simp` are present in
core where the skill says otherwise, the `ℚ` notation and `Nat.factorial`
do not exist in core, and the bundled scaffold's lakefile template is
incompatible with Lake 5.0. Beyond verification, the
runs reveal the "why" of TCT: the protocol forces into the open exact-rational
witness construction, calculus-free exact witnesses, quantified approximation
error, the distinction between counted and independent checks, the
load-bearing nature of domain declaration, and refusal-as-proved-claim.
Remaining gaps are identified: output-format column fit for multi-line checks,
Python-only steps the ledger does not flag as coverage holes, a missing
convention for declaring the *reading* of an ambiguous question, and the
scaffold's lakefile template.""")

# E2 - introduction
edit(
"""This paper reports the design and comparative evaluation of an agent Skill that
operationalises TCT. The skill is a single self-contained markdown document
(plus four stdlib-only Python helpers, also embedded in the document) and is
intended to load into any LLM agent runtime. We study it on two deliberately
conceptual ("why/how") questions, which force the protocol to separate
checkable arithmetic from assumed physics, and we compare three independent
runs to measure how the skill's design decisions affect the quality of the
result.""",
"""This paper reports the design and comparative evaluation of an agent Skill that
operationalises TCT. The skill is a single self-contained markdown document
(now 586 lines in 14 sections, plus four stdlib-only Python helpers, also
embedded in the document) and is intended to load into any LLM agent runtime.
We study it first on two deliberately conceptual ("why/how") questions, which
force the protocol to separate checkable arithmetic from assumed physics, and
we compare three independent runs to measure how the skill's design decisions
affect the quality of the result. We then evaluate the updated skill (which
adds a four-conditions "optimal construction" runbook, §14 of the skill) on a
broad twelve-question battery spanning eight domains, in an environment that
— unlike all earlier runs — has a Lean toolchain, so the Lean tier is compiled
rather than merely emitted.""")

# E3 - skill design size
edit(
"""The skill is a single self-contained markdown document (551 lines, 13 sections)
with four embedded stdlib-only Python helpers. Its pipeline:""",
"""The skill is a single self-contained markdown document (586 lines, 14 sections)
with four embedded stdlib-only Python helpers. Its pipeline:""")

# E4 - pipeline step 7
edit(
"""6. **cent_compiler mode.** Decompose into ¢ primitives, exhibit at least two ∆
   domain isomorphisms, solve in the easier domain, map back, and ledger
   licensed (axiom) vs. conjectural (sorry) analogies.""",
"""6. **cent_compiler mode.** Decompose into ¢ primitives, exhibit at least two ∆
   domain isomorphisms, solve in the easier domain, map back, and ledger
   licensed (axiom) vs. conjectural (sorry) analogies.
7. **Four-conditions runbook (new in the updated skill, §14).** An optimal run
   satisfies four exact, checkable conditions, derived by applying TCT to
   itself: (i) *classification identity* — every atomic claim lands in exactly
   one class proved/sorry/axiom/refused, so n = p+s+a+r; (ii) *independent
   cross-checks* — if c cross-check paths are written and t tautologies are
   removed, insight requires (c−t) ≥ 2, where a tautology is any check
   comparing expressions algebraically equivalent by construction; (iii)
   *optimisation-loop acceptance* — a simplification is accepted iff cost
   decreases **and** the verification-path count is preserved or increased
   (run one iteration, then stop); (iv) *named ledger* — every sorry names the
   exact missing tactic or lemma, every axiom is named, and an unnamed assumed
   premise is `WOULD_BE_GUESS`. The runbook also records a scanner fix:
   `lean_ledger.py` now counts only standalone `sorry`/`admit` proof-body
   lines, so identifiers containing the substring no longer false-positive.""")

# E5 - Run A platform note
edit(
"""**Runs.**
- **Run A** — this environment, using the skill's bundled tooling (original and
  revised versions). Illustrative givens: Q1 k=100 N/m, x=1/5 m, m=1 kg; Q2
  e=1/2, v_in=4 m/s, h₀=4 m.""",
"""**Runs.**
- **Run A** — dola.com's AI system (the agent sandbox referred to as "this
  environment" in the original runs), using the skill's bundled tooling
  (original and revised versions). Illustrative givens: Q1 k=100 N/m, x=1/5 m,
  m=1 kg; Q2 e=1/2, v_in=4 m/s, h₀=4 m.""")

# E6 - Run D battery in experimental design
edit(
"""- **Run C** — Claude.ai, revised skill (scripts embedded in §13 and materialised;
  optimisation loop hardened to preserve cross-checks; `decide` fallback;
  `:stable` toolchain; declared illustrative givens). Same givens as Run B.

**Comparison dimensions.** Python verification status; number of independent
cross-check paths and executed checks before/after optimisation; Lean
proved/sorry/axiom counts; whether `lake build` was run; defects surfaced.""",
"""- **Run C** — Claude.ai, revised skill (scripts embedded in §13 and materialised;
  optimisation loop hardened to preserve cross-checks; `decide` fallback;
  `:stable` toolchain; declared illustrative givens). Same givens as Run B.

**Run D (broad-domain battery, updated skill).** To evaluate the *updated*
skill — the 14-section document whose §14 runbook formalises the four
conditions — on dola.com's AI system with a Lean 4.35.0 / Lake 5.0.0 toolchain
installed in-environment, a twelve-question battery was run (T01–T12), keeping
the two original physics questions and adding ten questions chosen to stress
domains and protocol features the earlier runs never touched:

- T01 "How does a spring store and release energy?" — conceptual physics
  re-run (k=100, x₀=1/5, m=1, Run A convention);
- T02 "Why do things bounce?" — conceptual physics re-run with
  engineered rational givens (g=49/5, h₀=5/2, m=1/2, e=3/4, so v_in=7
  exactly);
- T03 "What is gravity?" — definition-plus-consequences ("what is" shape);
- T04 "How does water become large when hot and cold?" — anomalous
  expansion, an almost purely definitional/empirical question (rational
  witnesses near measured densities);
- T05 "What comes after Wednesday?" — conventional knowledge, cyclic ℤ/7ℤ
  arithmetic, an external stdlib calendar anchor;
- T06 "What is 1+1?" — minimal arithmetic, where the domain declaration
  itself (ℤ vs 𝔽₂) is load-bearing;
- T07 "How many ways to choose 2 toppings from 5?" — combinatorics,
  the cross-check showcase;
- T08 "£100 at 5% compound interest for 3 years?" — exact rational finance
  with a terminating-decimal claim;
- T09 "What comes next: 2, 4, 8, 16, …?" — a refusal-taxonomy stress test
  (UNDERDETERMINED);
- T10 "What is the area of a circle of radius 1 m?" — an irrational target
  that must be reported *measured, not exact* with a declared rational error
  bound;
- T11 "A light is off; the switch is flipped 17 times — on or off?" — 𝔽₂ at
  a declared XOR site (UBP D9 exercised for the first time in the study);
- T12 "Given V=12 V, I=5 A, R=4 Ω, what is the power?" — the designed
  INCONSISTENT_GIVENS refusal.

**Comparison dimensions.** Python verification status; number of independent
cross-check paths and executed checks before/after optimisation; Lean
proved/sorry/axiom counts; whether `lake build` was run; defects surfaced.""")

# E7+E8 - Run D results section (with corrected axiom-share sentence)
edit(
"""## 5.4 Comparison""",
"""## 5.4 Run D (dola.com's AI system, updated skill, compiled Lean tier)

**Setup.** The four bundled scripts were materialised verbatim from §13 of the
updated skill. Before the battery, the environment's Lean (4.35.0, Lake 5.0.0)
was probed on the exact lemma patterns the skill prescribes; the probes
already corrected the skill's §8 guidance in both directions (details in §7).

**Tier 1.** All twelve Column-3 scripts ran in isolation; 31/31 pre-declared
spot checks (`verify_column3.py --key K --expect V`) returned VERIFIED,
including both refusal verdicts (`REFUSED:UNDERDETERMINED`,
`REFUSED:INCONSISTENT_GIVENS`), the π-bracket containment, and the exact
bounce ledger (h₃ = 3645/8192 m, total distance 125/14 m, total time exactly
5 s).

**Tier 2.** All twelve Lake projects were scaffolded from classified specs and
**compiled** — the study's first compiled Lean tier: 12/12 `lake build`
succeeded, totalling 56 proved / 9 sorry / 25 axioms, with five projects
sorry-free (T05, T06, T09, T11, T12). Compilation was not free: the kernel
*refuted* the runner's first cross-multiplied bounce lemma (729·2·4096 =
3645·512·256 is simply false); after correcting it to 729·5·8192 =
3645·4096·2, the build passed. This is the study's first error caught by the
Lean tier — Run B's suspicion that "proved" without compilation is weak
proof is here made concrete.

**Battery results.**

| Test | Question (domain) | n | p | s | a | r | Lean p/s/a | build |
|---|---|---|---|---|---|---|---|---|
| T01 | spring (conceptual physics) | 12 | 6 | 2 | 4 | 0 | 6/2/3 | OK |
| T02 | bounce (conceptual physics) | 12 | 7 | 2 | 3 | 0 | 5/2/3 | OK |
| T03 | "what is gravity?" (definition) | 12 | 5 | 1 | 6 | 0 | 4/1/5 | OK |
| T04 | water expansion (empirical) | 13 | 6 | 1 | 6 | 0 | 4/1/5 | OK |
| T05 | after Wednesday (ℤ/7ℤ, calendar) | 7 | 6 | 0 | 1 | 0 | 4/0/1 | OK |
| T06 | 1+1 (arithmetic, domain decl.) | 5 | 5 | 0 | 0 | 0 | 5/0/0 | OK |
| T07 | 2-of-5 toppings (combinatorics) | 6 | 4 | 1 | 1 | 0 | 5/1/1 | OK |
| T08 | compound interest (finance, ℚ) | 7 | 5 | 1 | 1 | 0 | 4/1/1 | OK |
| T09 | next term 2,4,8,16 (refusal) | 7 | 5 | 0 | 1 | 1 | 4/0/1 | OK |
| T10 | circle area (irrational, bounds) | 11 | 7 | 1 | 3 | 0 | 4/1/3 | OK |
| T11 | 17 switch flips (𝔽₂, XOR site) | 7 | 6 | 0 | 1 | 0 | 7/0/1 | OK |
| T12 | V=12, I=5, R=4 (refusal) | 6 | 4 | 0 | 1 | 1 | 4/0/1 | OK |
| | **Totals** | **105** | **66** | **9** | **28** | **2** | **56/9/25** | **12/12** |

The classification identity holds exactly: 105 = 66 + 9 + 28 + 2. Overall,
26.7% of all atomic claims are named axioms; the axiom share of the "why/how"
and "what is" questions (25–50%: T01 33%, T02 25%, T03 50%, T04 46%) exceeds
that of the deterministic questions (0–17%), with one exception — T10 at 27%,
inflated because core Lean cannot name π at all and forces its definition,
the area formula, and the classical bracket into axioms. T06 ("what is
1+1?") is the study's first payload with **zero** axioms *and* zero sorries:
fully described.

**Four-conditions runbook.** The tautology audit earned its place six times:
the 1-based index encoding (T05), the ordered-selection count (T07), the
farthings walk (T08), the geometric-decay height variant (T02), the
mass-conservation re-assertion (T04), and the Lagrange evaluation (T09) were
all reclassified from "independent check" to representation variant. The
optimisation loop (one iteration) accepted 7 reductions — every one of which
removed an audited tautology or a reporting step, never a witness path — and
correctly stopped at the floor for the 5 minimal derivations (T03, T06, T09,
T11, T12: dropping any remaining primitive would drop a verification path).
Cross-check paths were preserved in every accepted iteration.

## 5.5 Comparison""")

# E9 - comparison table with Run D column
edit(
"""| Dimension | Run A | Run B (v1) | Run C (revised) |
|---|---|---|---|
| Bundled scripts used | yes | no (stand-in) | yes (materialised from §13) |
| Python VERIFIED | yes | yes | yes (all keys) |
| Cross-check paths before→after loop | 7→4 primitives; paths preserved | 10→4, 12→8 (silent loss) | 10→10, 12→12 (preserved) |
| Lean tactic | `decide`/`norm_num` | `norm_num` questioned | `decide` fallback; Nat cross-multiply |
| Toolchain | `:stable` (no guess) | would have to guess | `:stable` (no guess) |
| Lean proved/sorry/axioms | 7/2/3 (combined) | not scaffolded | Q1 3/1/4; Q2 6/1/3 |
| `lake build` executed | no | no | no |
| Illustrative givens | declared | invented, undeclared | declared & labelled |
| Defects surfaced | — | 4 | 0 of the prior 4; 4 new gaps (§6) |""",
"""| Dimension | Run A | Run B (v1) | Run C (revised) | Run D (updated, broad battery) |
|---|---|---|---|---|
| Platform | dola.com AI system | Claude.ai | Claude.ai | dola.com AI system |
| Bundled scripts used | yes | no (stand-in) | yes (materialised from §13) | yes (materialised verbatim) |
| Python VERIFIED | yes | yes | yes (all keys) | yes (31/31 spot checks, 12 questions) |
| Cross-check paths before→after loop | 7→4 primitives; paths preserved | 10→4, 12→8 (silent loss) | 10→10, 12→12 (preserved) | 7 accepted / 5 floor stops; audit removed 6 tautologies; paths preserved in all |
| Lean tactic | `decide`/`norm_num` | `norm_num` questioned | `decide` fallback; Nat cross-multiply | probes: `decide`/`rfl` fail on `Rat`; Nat cross-multiply; `omega` present in core |
| Toolchain | `:stable` (no guess) | would have to guess | `:stable` (no guess) | `:stable` → 4.35.0, installed in-environment |
| Lean proved/sorry/axioms | 7/2/3 (combined) | not scaffolded | Q1 3/1/4; Q2 6/1/3 | 56/9/25 across 12 projects |
| `lake build` executed | no | no | no | **yes — 12/12 OK** (after a named lakefile workaround) |
| Illustrative givens | declared | invented, undeclared | declared & labelled | declared & labelled (2 physics questions) / not needed (10) |
| Defects surfaced | — | 4 | 0 of the prior 4; 4 new gaps (§7) | 9 new environment/tooling findings; 1 runner error caught by the Lean kernel |""")

# E10 - section 6 intro
edit(
"""The physics content of both answers is textbook. What is non-obvious is what the
protocol forced into the open — these seven observations are the "why" of TCT.""",
"""The physics content of both answers is textbook. What is non-obvious is what the
protocol forced into the open — the first seven observations come from the
physics-question runs (A–C); the last four (6.8–6.11) are what the broad-domain
battery of Run D added. Together they are the "why" of TCT.""")

# E11 - sections 6.8-6.11
edit(
"""**6.7 Analogies are self-correcting under the ledger.** The cent_compiler mode
flagged the thermal-decay analogy as conjectural (exponential in time, not
per-cycle) rather than asserting it, while the electrical isomorphism was
licensed. Isomorphism validity domains become explicit rather than glossed.""",
"""**6.7 Analogies are self-correcting under the ledger.** The cent_compiler mode
flagged the thermal-decay analogy as conjectural (exponential in time, not
per-cycle) rather than asserting it, while the electrical isomorphism was
licensed. Isomorphism validity domains become explicit rather than glossed.

**6.8 The domain declaration is load-bearing (T06).** "What is 1+1?" has no
domain-free answer: 2 in ℤ, 0 in 𝔽₂ (at the declared XOR site), 2 in ℤ/7ℤ.
A prose answer silently assumes ℤ; TCT forces the assumption into the open,
and the minimal question still runs the full pipeline — five claims, three
genuinely disjoint routes (definitional successor, disjoint-union
cardinality, explicit pairing), zero sorries, zero axioms. The optimisation
loop correctly stops immediately at the one-primitive floor.

**6.9 A refusal can itself be a proved claim (T09, T12).** For "what comes
next: 2, 4, 8, 16, …?", the protocol's honest answer is `UNDERDETERMINED` —
and the refusal is *justified* by exact witnesses: the geometric reading
(32), the interpolating cubic (30), and Moser's circle-region sequence (31)
all match the four givens and disagree, which disproves uniqueness of the
continuation. The conventional answer 32 survives only as a conditional on a
*named* simplicity axiom. Likewise T12's INCONSISTENT_GIVENS refusal is
executed, not asserted: Column 3 derives all three licensed readings and
witnesses their disagreement, and Lean proves each pairwise inconsistency by
`decide`. "I cannot answer" becomes a checkable statement about the givens.

**6.10 Definitional questions check axiom coherence, not arithmetic (T04,
T03).** Water's anomalous expansion is almost pure definition-substitution:
every "independent" numeric route to the volume ratios is algebraically
linked, so the (c−t) ≥ 2 condition can only be met by importing a second
axiom base — Archimedes' principle — after which the cross-check verifies the
*coherence of two axioms* (displacement route vs density route agree on the
submerged fraction 2750/2997) rather than any arithmetic. "What is gravity?"
shows the same shape at larger scale: 50% of its claims are named premises,
and the checkable content is the witness triple (t = 5/7 s, v = 7 m/s,
h = 5/2 m) satisfying three kinematic relations simultaneously.

**6.11 "Measured, not exact" is a working discipline, not a disclaimer
(T10).** The circle's area cannot be an exact rational, so the no-float rule
forces a different mode: two genuinely independent exact-rational interval
routes (Archimedes' harmonic/geometric-mean perimeter iteration, and a
side-doubling area recursion), each carried entirely in `Fraction` interval
arithmetic with bisection square roots, overlap at π ∈ [3.14103…, 3.14271…],
sit strictly inside the classical 223/71–22/7 bracket (proved by `decide` on
the cross-multiplied integers), and declare the error bound as an exact
rational. The Stern–Brocot search for the simplest rational inside the
bracket (267/85) is itself exact. The UBP does not forbid irrational answers;
it disciplines how they are reported.""")

# E12 - section 7 rewrite
edit(
"""# 7. Remaining gaps and limitations

**What the revision fixed.** All four Run-B defects were closed in Run C: the
scripts travel embedded in the document (§13) and materialise on first use; the
Lean tactic claim was corrected to `decide`/`rfl` with `norm_num` as optional;
the optimisation loop now measures verification-path count and rejects any
reduction that drops a witness; illustrative givens must be declared and the
mechanism answer must be independent of them.

**Remaining gaps (identified by Run C).**
1. **Cross-check independence is not enforced.** The loop counts checks, not
   whether they compare two *independently computed* expressions. The Run C
   runner caught and removed two tautologies (`U_half+K_half==U`,
   `KE_out+lost==KE_in`) that would have inflated the count. A future rule: a
   cross-check must compare two expressions with disjoint derivation paths.
2. **`decide` on `ℚ` unconfirmed without Mathlib.** Run C avoided rationals in
   Lean by cross-multiplying into `Nat`. The skill should either confirm
   `decide` on `ℚ` in pure core or recommend the cross-multiplication pattern.
3. **Output-format column fit.** The prescribed "Python (this step)" table
   column does not accommodate multi-line check witnesses; Run C substituted
   cross-check names. The skill should permit that substitution.
4. **Coverage asymmetry.** Q2 step 8 (limits and repeated bounces) was checked
   in Python but had no Lean lemma — a coverage gap the ledger did not flag.
5. **Lean tier never compiled.** In all three runs `lake` was absent, so "proved"
   means "a `decide` proof was written", not "compiled". The sorry ledger is
   therefore provisional until `lake build` runs.

**On conceptual questions.** Roughly half of each answer landed as axioms in
every run. This is the method behaving as designed: it cleanly separates what
exact arithmetic can check from what physics must assume, and records the latter
by name rather than smuggling it in as proved.""",
"""# 7. Remaining gaps and limitations

**What the revision fixed.** All four Run-B defects were closed in Run C: the
scripts travel embedded in the document (§13) and materialise on first use; the
Lean tactic claim was corrected to `decide`/`rfl` with `norm_num` as optional;
the optimisation loop now measures verification-path count and rejects any
reduction that drops a witness; illustrative givens must be declared and the
mechanism answer must be independent of them.

**What the updated skill and Run D closed.**
1. **Cross-check independence (Run C gap 1) — closed by design and exercised.**
   The §14 runbook now prescribes the tautology audit — a real check compares
   two expressions with disjoint derivation paths; anything algebraically
   equivalent by construction is removed, not counted. Run D's audit removed
   six such variants across the battery (§5.4), including two the runner had
   initially written as checks.
2. **`decide` on `ℚ` unconfirmed (Run C gap 2) — resolved empirically, against
   the skill.** With Lean 4.35.0 compiled in-environment, the probes show the
   pure-core landscape precisely: the `ℚ` *notation itself* does not exist in
   core (it elaborates as a fresh type variable); on the core type `Rat`, both
   `decide` and `rfl` fail with kernel reduction stuck in `instDecidableEqRat`;
   `native_decide` works but trusts the compiler. The Nat/Int
   cross-multiplication pattern that Run C improvised is confirmed as the only
   kernel-checked route, and Run D used it throughout. The skill's §8/§9
   worked-example lemma `(12 : ℚ)^2 / 4 = 36 := by decide` therefore fails in
   pure core at elaboration, not at the tactic.
3. **The Lean tier was never compiled (Run C gap 5) — closed, with new
   findings.** Run D compiled all twelve projects (`lake build` 12/12). Two
   results matter. First, the bundled scaffold's lakefile template is
   incompatible with Lake 5.0 in two ways — `lean_exe … root := «Main»` fails
   package configuration, and `lean_lib TCT` no longer globs submodules —
   requiring a named post-scaffold workaround (`globs := #[.one `TCT.Basic]`);
   the skill's §13 scaffold needs the same update. Second, compilation has
   teeth: the kernel refuted the runner's first cross-multiplied bounce lemma,
   which no amount of Python-side verification would have flagged because the
   Python value itself was correct — the *translation* into Lean was the
   error. "Proved" before Run D meant "a proof was written"; now it means
   "the kernel checked it".

**New findings that correct the skill's §8 guidance (from the Run D probes).**
`omega` and `simp` are present in pure core Lean 4.35 (the skill lists them as
requiring Std/Mathlib), which let Run D prove the general weekday-successor
and parity laws symbolically rather than leaving them sorry; `norm_num` and
`ring` are confirmed absent; `Nat.factorial` is absent (the scaffold must
define its own); `decide` also fails on Nat bitwise XOR; and core Lean cannot
name `Real.pi` at all, so geometry questions must axiomatise the constant
itself (T10's axiom share rose to 27% for exactly this reason). One
sharp-edged detail: `omega` proves Int-mod successor laws but fails Nat-mod
goals with negated conclusions — goal shape matters when choosing tactics.

**Remaining gaps.**
1. **Output-format column fit (Run C gap 3, still open).** The prescribed
   "Python (this step)" table column does not accommodate multi-line check
   witnesses; Run D again substituted cross-check names and coverage notes.
   The skill should permit that substitution explicitly.
2. **Coverage asymmetry (Run C gap 4, still open).** Run D again contains
   Python-checked steps with no Lean lemma (T01 steps 5 and 7; T03 step 5;
   T10 steps 4–6 and 8). The ledger reports both tiers' totals but does not
   flag the *difference* — a per-step coverage map (which claims have a Lean
   lemma) is the missing instrument.
3. **No named place for declaring the reading of an ambiguous question.**
   Three Run D questions required an interpretation declaration before any
   decomposition: T05 ("after Wednesday" = immediate successor, not any later
   day), T09 (puzzle convention = conditional answer, not THE answer), T04
   ("become large" = expand). The skill's §6 givens block covers givens but
   not readings; each run improvised a "reading declared" line. The output
   format should name that block.
4. **Scaffold tooling drift.** The bundled `scaffold_lean_project.py` lakefile
   template is Lake-4-era; until §13 is updated, every user on a current
   toolchain needs Run D's named workaround. More generally, Run D shows the
   skill's environment claims (tactic availability, notation, constants)
   rot with the toolchain and should be phrased as *probe-first*: state the
   pattern, verify availability at run time, fall back with a named gap —
   exactly what Run D did.

**On conceptual questions.** Roughly half of each answer landed as axioms in
every run. This is the method behaving as designed: it cleanly separates what
exact arithmetic can check from what physics must assume, and records the
latter by name rather than smuggling it in as proved. Run D extends the
observation across domains: the axiom share is a measurable signature of
question type (25–50% for "why/what is" questions, 0–17% for deterministic
ones, π-inflated 27% for T10).""")

# E13 - conclusion + artifacts
edit(
"""# 8. Conclusion

The TCT skill converts "plausible derivation" into "independently re-verified
derivation" across both deterministic and conceptual questions, and its sorry
ledger makes the unproved remainder explicit. The comparative runs show that the
protocol's value is not only verification — it is the "why" it forces into the
open: exact-rational witness construction, calculus-free exact witnesses,
quantified approximation error, and the sharp distinction between a counted
check and an independent one. The skill's design defects are themselves
discoverable and closable through exactly the cross-check accounting the
protocol prescribes. The principal open work is enforcing cross-check
*independence*, confirming pure-core `decide` on `ℚ`, and compiling the Lean
tier end-to-end.

# References""",
"""# 8. Conclusion

The TCT skill converts "plausible derivation" into "independently re-verified
derivation" across both deterministic and conceptual questions, and its sorry
ledger makes the unproved remainder explicit. The comparative runs show that
the protocol's value is not only verification — it is the "why" it forces into
the open: exact-rational witness construction, calculus-free exact witnesses,
quantified approximation error, and the sharp distinction between a counted
check and an independent one. Run D extends this across eight domains and
adds three lessons. First, breadth is not dilution: the same 14-section skill
produced exact verified answers everywhere from 1+1 to π-bracketing, and its
refusal taxonomy answered two questions *correctly by refusing*, with the
refusal itself machine-checked. Second, the Lean tier only tells the truth
when it is compiled: Run D's kernel refuted one of the runner's own lemmas
and falsified the skill's worked-example tactic pattern while confirming an
improvised alternative — evidence that the sorry ledger is provisional until
`lake build` runs, and that environment claims in the skill should be
probe-first rather than asserted. Third, the four-conditions runbook works:
the classification identity closed exactly (105 = 66+9+28+2), the tautology
audit removed six would-be checks, and the hardened loop accepted seven
simplifications without losing a single witness path. The skill's design
defects are themselves discoverable and closable through exactly the
cross-check accounting the protocol prescribes. The principal open work is
the output-format column fit, a per-step Lean coverage map, a named
declaration block for question readings, and updating the bundled scaffold's
lakefile template for current Lake.

# Artifacts

The Run D artifact bundle accompanies this paper: per-question directories
`T01…T12/` each containing `column3.py` (the Column-3 re-derivation),
`spec.json`, the scaffolded Lean project `lean_tct/` (built, Lean 4.35.0),
`decomp_before/after.json`, `payload.md` (the full three-column answer in the
skill's §6 output format), and the run-level logs
(`RUN_D_SUMMARY.md`, `lean_tier.log`, `optimization_loop.log`,
`results.log`), together with the environment probes (`lean_probe/`).

# References""")

# E14 - references
edit(
"""[3] `three-column-thinking` Skill (this study): single self-contained
`SKILL.md` + `scripts/{verify_column3,scaffold_lean_project,lean_ledger,cent_cost}.py`.""",
"""[3] `three-column-thinking` Skill (this study): single self-contained
`SKILL.md` (586 lines, 14 sections; the updated version evaluated in Run D
adds the §14 four-conditions runbook and the `lean_ledger.py` scanner fix) +
`scripts/{verify_column3,scaffold_lean_project,lean_ledger,cent_cost}.py`.

[4] Run D artifact bundle (this study): dola.com AI system, 1 Nov 2026 —
12 question directories (T01–T12) with Column-3 scripts, Lean specs and
built Lake projects (Lean 4.35.0 / Lake 5.0.0), optimization-loop
decompositions, and per-question TCT payloads; plus environment probes and
run logs.""")

# E15 - section 5.1 heading
edit("## 5.1 Run A (this environment)", "## 5.1 Run A (dola.com's AI system)")


def main():
    text = open(PAPER, encoding="utf-8").read()
    for i, (old, new) in enumerate(EDITS, 1):
        if old not in text:
            print(f"EDIT {i}: OLD STRING NOT FOUND")
            return 1
        if text.count(old) != 1:
            print(f"EDIT {i}: OLD STRING NOT UNIQUE ({text.count(old)})")
            return 1
        text = text.replace(old, new)
    with open(PAPER, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"applied {len(EDITS)} edits; paper now {len(text.splitlines())} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
