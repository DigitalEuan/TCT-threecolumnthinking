#!/usr/bin/env python3
"""Skill v3 update: close the paper's four remaining gaps.

E1  description: probe-first Lean tier
E2  §3 classification bullet: corrected pure-core tactics
E3  §5 Tier 2: compiled-not-provisional discipline
E4  §6 output format: Reading block, Python-column rule, coverage map
E5  §8 full rewrite: probe-first landscape + cross-multiplication + degradation ladder
E6  §9 example B: Nat cross-multiplication instead of the failing ℚ lemma
E7  §10: five scripts, Lake 5 scaffold, lean_probe.py entry
E8  §13 scaffold source: Lake-5 lakefile (globs, no lean_exe/Main.lean)
E9  §13: add lean_probe.py source block
E10 §14 condition 4: coverage map requirement
"""
import shutil

SRC = "/home/z/my-project/upload/SKILL.md"
DST = "/home/z/my-project/download/SKILL.md"

EDITS = []


def edit(old, new):
    EDITS.append((old, new))


# E1 - frontmatter description
edit(
"Platform-dependent Lean tier: each formalizable step becomes a lemma in a "
"lake-build-ready project, proved where possible, `sorry` with a named gap where not.",
"Platform-dependent Lean tier, probed at run time (`lean_probe.py` checks tactic "
"and notation availability before lemmas are written): each formalizable step "
"becomes a lemma in a lake-build-ready project, proved where possible, `sorry` "
"with a named gap where not.")

# E2 - §3 classification bullet
edit(
"""   - *Formalizable, closed-form* (concrete arithmetic, finite decidable facts)
     → Lean theorem with a pure-core proof: `decide` (closed decidable
     arithmetic) or `rfl`; `norm_num` is available in recent core/Std but if
     your toolchain lacks it, `decide` is the zero-import fallback.""",
"""   - *Formalizable, closed-form* (concrete arithmetic, finite decidable facts)
     → Lean theorem with a pure-core proof: `decide` on closed
     `Nat`/`Int`/`Bool` facts (cross-multiply rationals into `Nat` first, §8)
     or `rfl`; `omega` and `simp` are also pure core. Probe the toolchain
     before writing (§8).""")

# E3 - §5 Tier 2
edit(
"""  `sorry` compiles (warning only), so `lake build` always succeeds; **0 sorry =
  fully described**.""",
"""  `sorry` compiles (warning only), so `lake build` always succeeds; **0 sorry =
  fully described**. Run the build whenever a toolchain is present — an
  uncompiled `decide` proof is provisional (Run D's kernel refuted one
  translation whose Python-side value was correct), and `lean_probe.py`
  (§13) checks the tactic landscape in ~30 s before you write lemmas.""")

# E4 - §6 output format
edit(
"""**Givens.** ... (if the question is "why/how" and supplies no givens, choose and
  explicitly declare *illustrative model values* — label them as such; the
  conceptual/mechanism answer must not depend on them)
**Domain.** ℤ / ℚ / 𝔽₂ / float with declared bound ...
**UBP compliance.** Column 3: Fraction/int only, no floats/random/SHA — or note any declared exception site.
**Decomposition.** N atomic claims: K proved, M sorry, A axioms.

| Step | Plain English | Mathematics | Python (this step) | Lean |
|---|---|---|---|---|
| 1 | ... | ... | ... | theorem ... (proved) / sorry + gap / axiom |

**Full Column 3 script:**""",
"""**Givens.** ... (if the question is "why/how" and supplies no givens, choose and
  explicitly declare *illustrative model values* — label them as such; the
  conceptual/mechanism answer must not depend on them)
**Reading.** the licensed interpretation(s) of ambiguous wording, declared
  *before* decomposition (e.g. "after Wednesday" = the immediate successor
  day, not any later day; "become large" = expand on heating below 4 °C).
  One licensed reading → proceed with it named. Two conflicting licensed
  readings with no tie-break → `READINGS_DISAGREE` (§7). Readings are
  licensed like axioms: named, never silent.
**Domain.** ℤ / ℚ / 𝔽₂ / float with declared bound ...
**UBP compliance.** Column 3: Fraction/int only, no floats/random/SHA — or note any declared exception site.
**Decomposition.** N atomic claims: K proved, M sorry, A axioms.

| Step | Plain English | Mathematics | Python (this step) | Lean |
|---|---|---|---|---|
| 1 | ... | ... | ... | theorem ... (proved) / sorry + gap / axiom |

Python column: a one-line witness (`assert P == V*V/R`) when it fits; when
the witness is multi-line, put the cross-check *name* or the KEY it sets in
the cell and the full witness in the Column-3 script below — never truncate
mathematics to fit the column.

**Coverage map.** Lean lemmas cover k of N decomposed claims; Python covers
all N. Steps without a Lean lemma are listed by number with a reason (e.g.
"5: interval arithmetic — no pure-core irrational lemma"; "7: reporting
only"). A coverage hole is not an error; an unlisted one is.

**Full Column 3 script:**""")

# E5 - §8 full rewrite
edit(
"""## 8. Lean lemma patterns

Pure core Lean 4 (no imports, no network) proves closed computations only:
`decide` (closed decidable integer/rational arithmetic — the zero-import
fallback), `rfl` (definitional equality). `norm_num` is available in recent
core/Std; use it if present, otherwise `decide`. Symbolic tactics (`ring`,
`linarith`, `field_simp`, `omega`) require Std or Mathlib — if needed, either
scaffold with `--with-mathlib` (pin the matching toolchain) or leave the lemma
`sorry` with a gap naming it.

Translation:
- Closed computation: `theorem power_value : (12 : ℚ)^2 / 4 = 36 := by decide`
  (or `by norm_num` if available)
- Symbolic/unproven: `theorem power_symbolic : ∀ V R : ℚ, R ≠ 0 → V^2/R = V*(V/R) := by sorry  -- GAP: requires field_simp/ring (mathlib) or manual calc`
- Empirical premise: `axiom ohms_law_empirical : Prop  -- assumed: V=I·R from physics, not derived`
- Definition: `def power (V R : ℚ) : ℚ := V^2 / R`

Spec JSON for `scaffold_lean_project.py`: `{"module":"TCT","imports":[],
"definitions":[{"name":"...","type":"...","value":"..."}],
"axioms":[{"name":"...","type":"...","note":"..."}],
"lemmas":[{"name":"...","type":"...","proof":"decide" or null,"gap":"... or null"}]}`.""",
"""## 8. Lean lemma patterns

**Probe first, then write.** Environment claims rot with the toolchain —
notation, tactics and constants appear and disappear between versions. Before
writing lemmas, run `scripts/lean_probe.py` (§13; ~30 s, needs only `lean`)
and **believe the probe over this table**. The landscape below is the
verified pure-core baseline (Lean 4.35.0 / Lake 5.0.0, no imports, no
network):

| Pattern | Core 4.35 | Notes / use |
|---|---|---|
| `decide` on closed `Nat`/`Int`/`Bool` | ✔ | the workhorse |
| `rfl` | ✔ | definitional equalities |
| `omega` | ✔ | Int linear arithmetic incl. `%` by constants; goal-shape sensitive — proves Int-mod successor laws, fails Nat-mod goals with negated conclusions |
| `simp` | ✔ | simplification |
| `ℚ` / `ℕ` notation | ✘ | not in core — elaborates as fresh type variables; write `Rat` / `Nat` |
| `decide` / `rfl` on `Rat` | ✘ | kernel reduction stuck (`instDecidableEqRat`) — cross-multiply (below) |
| `native_decide` on `Rat` | ✔ | works, but compiler-trusted, not kernel-checked — label it |
| `norm_num`, `ring`, `linarith`, `field_simp` | ✘ | Mathlib only — `--with-mathlib`, or sorry + gap |
| `Nat.factorial` | ✘ | not in core — inline values or define your own |
| `Real.pi` | ✘ | not in core — geometry axiomatises the constant and says so |
| `Nat` bitwise XOR | △ | `decide` succeeds on closed literals; fails on goals with variables |

**The kernel-checked rational route: cross-multiplication.** To prove an
equation between exact rationals `a/b = c/d`, clear denominators and state
the `Nat`/`Int` fact; name the lemma after the reading it witnesses, so the
translation is self-documenting:

```lean
theorem power_cross : 12 * 12 = 36 * 4 := by decide  -- P = V²/R = 36 W, × b·d
```

**Degradation ladder** (when a probe fails or the toolchain is absent):
1. same claim via a core-available pattern (cross-multiply; `omega`; `simp`);
2. `sorry` + gap naming the missing development
   (`-- GAP: requires field_simp (mathlib)`);
3. Tier 2 reported as "not run; project ready for `lake build`".

Never silently drop a lemma, and never report an uncompiled `decide` proof
as settled: a claim is *proved* only after `lake build` succeeds. (Run D's
kernel refuted a cross-multiplied lemma whose Python-side value was correct —
the translation itself was the error; only compilation catches that class.)

Translation:
- Closed computation: `theorem power_cross : 12 * 12 = 36 * 4 := by decide`
  (reading named in or after the lemma)
- Symbolic/unproven: `theorem power_symbolic : ∀ V R : Rat, R ≠ 0 → V^2/R = V*(V/R) := by sorry  -- GAP: requires field_simp/ring (mathlib) or manual calc`
- Empirical premise: `axiom ohms_law_empirical : Prop  -- assumed: V=I·R from physics, not derived`
- Definition: `def power (V R : Rat) : Rat := V^2 / R`

Spec JSON for `scaffold_lean_project.py`: `{"module":"TCT","imports":[],
"definitions":[{"name":"...","type":"...","value":"..."}],
"axioms":[{"name":"...","type":"...","note":"..."}],
"lemmas":[{"name":"...","type":"...","proof":"decide" or null,"gap":"... or null"}]}`.""")

# E6 - §9 worked example B
edit(
"""**B. Lean tier (same example).** `current_value` and `power_value` prove with
`decide` (or `norm_num` if available); `power_symbolic` (∀ V R, R≠0 → V²/R = V·(V/R)) is `sorry` with gap
"requires field_simp/ring (mathlib) or manual calc"; `ohms_law_empirical` is an
axiom. Scaffold → `lake build` succeeds; 1 sorry remains = development required.""",
"""**B. Lean tier (same example).** `current_value` proves with `decide` on the
cleared form (`12 = 3 * 4`); `power_value` likewise via cross-multiplication
(`12 * 12 = 36 * 4`, witnessing P = V²/R = 36 W); `power_symbolic` (∀ V R,
R≠0 → V²/R = V·(V/R)) is `sorry` with gap "requires field_simp/ring
(mathlib) or manual calc"; `ohms_law_empirical` is an axiom. Scaffold →
`lake build` succeeds; 1 sorry remains = development required.""")

# E7 - §10 bundled scripts list
edit(
"""If a `scripts/` directory is not present next to this file, materialize the four
scripts from §13 (write each code block to `scripts/<filename>.py`) before use —
this document is self-contained.

- `scripts/verify_column3.py` — isolated Python re-derivation checker.
  `python3 verify_column3.py SCRIPT.py --key P --expect 36` (or `--code "..."`,
  `--timeout N`). Exit 0/1/2 = VERIFIED/MISMATCH/ERROR.
- `scripts/scaffold_lean_project.py` — JSON spec → Lake 4 project +
  `SORRY_LEDGER.md`. `--spec spec.json --out tct_lean/ [--with-mathlib]
  [--toolchain leanprover/lean4:vX.Y.Z]`. Pure core by default.
- `scripts/lean_ledger.py` — scan a project for `sorry`/`axiom`; `--build` runs
  `lake build` if present.
- `scripts/cent_cost.py` — count ¢ primitives in a decomposition and diff
  before/after an optimization iteration (`--before v1.json --after v2.json`).""",
"""If a `scripts/` directory is not present next to this file, materialize the five
scripts from §13 (write each code block to `scripts/<filename>.py`) before use —
this document is self-contained.

- `scripts/verify_column3.py` — isolated Python re-derivation checker.
  `python3 verify_column3.py SCRIPT.py --key P --expect 36` (or `--code "..."`,
  `--timeout N`). Exit 0/1/2 = VERIFIED/MISMATCH/ERROR.
- `scripts/scaffold_lean_project.py` — JSON spec → Lake project +
  `SORRY_LEDGER.md`. `--spec spec.json --out tct_lean/ [--with-mathlib]
  [--toolchain leanprover/lean4:vX.Y.Z]`. Pure core by default; lakefile
  targets current Lake (verified on Lake 5.0.0 / Lean 4.35.0).
- `scripts/lean_ledger.py` — scan a project for `sorry`/`axiom`; `--build` runs
  `lake build` if present.
- `scripts/cent_cost.py` — count ¢ primitives in a decomposition and diff
  before/after an optimization iteration (`--before v1.json --after v2.json`).
- `scripts/lean_probe.py` — run-time environment probe: checks tactic /
  notation availability on the local toolchain against the §8 baseline and
  prints the live landscape. Run before writing lemmas (probe-first).""")

# E8 - §13 scaffold source: Lake-5 lakefile, drop MAIN
edit(
"""proof=null -> sorry + GAP comment. Writes lean-toolchain=leanprover/lean4:stable (elan resolves it).
Usage: python3 scaffold_lean_project.py --spec spec.json --out proj/ [--with-mathlib] [--toolchain TAG]
\"\"\"
import argparse, json, os, sys

LAKEFILE = \"\"\"import Lake
open Lake DSL
package {name} where
  moreServerArgs := #["-DwarningAsError=false"]
lean_lib {mod} where
@[default_target] lean_exe «check» where
  root := «Main»
\"\"\"
MAIN = \"\"\"import {mod}
def main : IO Unit := pure ()
\"\"\"
TOOLCHAIN_DEFAULT = "leanprover/lean4:stable\"""",
"""proof=null -> sorry + GAP comment. Writes lean-toolchain=leanprover/lean4:stable (elan resolves it).
Lakefile targets current Lake: single lean_lib with an explicit glob, no lean_exe
(verified Lake 5.0.0 / Lean 4.35.0; the pre-5.0 lean_exe template fails package config).
Usage: python3 scaffold_lean_project.py --spec spec.json --out proj/ [--with-mathlib] [--toolchain TAG]
\"\"\"
import argparse, json, os, sys

LAKEFILE = \"\"\"import Lake
open Lake DSL
package {name} where
  moreServerArgs := #["-DwarningAsError=false"]
@[default_target]
lean_lib {mod} where
  globs := #[.one `{mod}.Basic]
\"\"\"
TOOLCHAIN_DEFAULT = "leanprover/lean4:stable\"""")

edit(
"""    open(os.path.join(args.out, "lakefile.lean"), "w").write(lakefile)
    open(os.path.join(args.out, "Main.lean"), "w").write(MAIN.format(mod=f"{mod}.Basic"))""",
"""    open(os.path.join(args.out, "lakefile.lean"), "w").write(lakefile)""")

# E9 - §13: add lean_probe.py block before §14
edit(
"""if __name__ == "__main__":
    sys.exit(main())
```

## 14. Optimal construction — the four conditions (runbook)""",
"""if __name__ == "__main__":
    sys.exit(main())
```

### scripts/lean_probe.py

```python
#!/usr/bin/env python3
\"\"\"Probe the local Lean toolchain for the TCT lemma patterns (probe-first, S8).
Writes tiny probe files to a temp dir, runs `lean` on each, and prints the live
landscape vs. the pure-core 4.35.0 baseline. Believe the probe, not the docs.
Usage: python3 lean_probe.py [--lean /path/to/lean]
Exit: 0 probe ran, 3 no Lean found.
\"\"\"
import argparse, os, shutil, subprocess, sys, tempfile

PROBES = [
    # (name, source, baseline on pure-core Lean 4.35.0: True = compiles)
    ("decide_nat", "example : 12 * 12 / 4 = 36 := by decide", True),
    ("rfl_definitional", "example : 1 + 1 = 2 := by rfl", True),
    ("omega_int_mod", "example : \u2200 n : Int, (n + 1) % 7 = (n % 7 + 1) % 7 := by omega", True),
    ("simp", "example : 2 + 2 = 4 := by simp", True),
    ("Q_notation", "example : (12 : \u211a)^2 / 4 = 36 := by decide", False),
    ("rat_decide", "example : (12 : Rat)^2 / 4 = 36 := by decide", False),
    ("rat_rfl", "example : (12 : Rat)^2 / 4 = 36 := by rfl", False),
    ("rat_native_decide", "example : (12 : Rat)^2 / 4 = 36 := by native_decide", True),
    ("norm_num", "example : 2 + 2 = 4 := by norm_num", False),
    ("ring", "example (a b : Nat) : a + b = b + a := by ring", False),
    ("nat_factorial", "example : Nat.factorial 5 = 120 := by rfl", False),
    ("real_pi", "#check Real.pi", False),
    ("nat_xor_variable", "example (a : Nat) : (a ^^^ 0) = a := by decide", False),
]

def find_lean(explicit):
    if explicit:
        return explicit
    on_path = shutil.which("lean")
    if on_path:
        return on_path
    elan = os.path.join(os.environ.get("ELAN_HOME", ""), "bin", "lean")
    return elan if os.path.exists(elan) else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lean")
    args = ap.parse_args()
    lean = find_lean(args.lean)
    if not lean:
        print("NO LEAN on PATH or ELAN_HOME - Tier 2 unavailable here.")
        print("Degrade per S8: sorry+gap for formal steps; report 'lake build: not run'.")
        return 3
    ver = subprocess.run([lean, "--version"], capture_output=True, text=True)
    print("probing: " + (ver.stdout.strip() or ver.stderr.strip()))
    tmp = tempfile.mkdtemp(prefix="tct_probe_")
    try:
        agree = disagree = 0
        for name, src, baseline in PROBES:
            path = os.path.join(tmp, name + ".lean")
            with open(path, "w", encoding="utf-8") as f:
                f.write(src + "\\n")
            r = subprocess.run([lean, path], capture_output=True, text=True, timeout=120)
            live = (r.returncode == 0)
            mark = "AGREE" if live == baseline else "!= BASELINE"
            if live == baseline:
                agree += 1
            else:
                disagree += 1
            print("  %-20s %-9s (baseline %-3s) %s" % (name, "AVAILABLE" if live else "absent", "yes" if baseline else "no", mark))
        print("%d agree with the 4.35.0 baseline, %d differ - trust the probe." % (agree, disagree))
        print("Kernel-checked rationals: cross-multiply into Nat (S8); native_decide is compiler-trusted.")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    sys.exit(main())
```

## 14. Optimal construction — the four conditions (runbook)""")

# E10 - §14 condition 4: coverage map
edit(
"""4. **Named ledger.** Every sorry names the exact missing tactic or lemma; every
   axiom is named; an unnamed assumed premise is `WOULD_BE_GUESS`. `0 sorry =
   fully described`. When stuck, switch domains via cent mode (≥2 domains;
   license each analogy as axiom or mark it conjectural sorry).""",
"""4. **Named ledger.** Every sorry names the exact missing tactic or lemma; every
   axiom is named; an unnamed assumed premise is `WOULD_BE_GUESS`. `0 sorry =
   fully described`. The ledger includes a **coverage map** (§6): which
   claims carry a Lean lemma (k of N); Python-only steps are listed with the
   reason. When stuck, switch domains via cent mode (≥2 domains; license
   each analogy as axiom or mark it conjectural sorry).""")


def main():
    text = open(SRC, encoding="utf-8").read()
    for i, (old, new) in enumerate(EDITS, 1):
        if old not in text:
            print(f"E{i}: OLD STRING NOT FOUND")
            return 1
        if text.count(old) != 1:
            print(f"E{i}: NOT UNIQUE ({text.count(old)})")
            return 1
        text = text.replace(old, new)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"applied {len(EDITS)} edits -> {DST} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
