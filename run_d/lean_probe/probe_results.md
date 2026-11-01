# Run D environment probes — live results (Lean 4.35.0, pure core)

Every probe was re-run live on 2026-11-01 (see `probe_run.log` for raw
output; `pXX_*.lean` are the probe sources).

| # | Probe | Statement | Live | Paper (§7) | Verdict |
|---|---|---|---|---|---|
| p01 | Q notation | `(12 : ℚ)^2 / 4 = 36 := by decide` | FAIL (instance synth) | fails at elaboration | AGREE |
| p02 | Rat decide | `(12 : Rat)^2 / 4 = 36 := by decide` | FAIL (kernel stuck) | kernel-stuck | AGREE |
| p03 | Rat rfl | `(12 : Rat)^2 / 4 = 36 := by rfl` | FAIL | kernel-stuck | AGREE |
| p04 | Rat native_decide | same, `native_decide` | PASS | works (compiler-trusted) | AGREE |
| p05 | omega, Int mod | `∀ n : Int, (n+1) % 7 = (n % 7 + 1) % 7` | PASS | present in core | AGREE |
| p06 | omega, Nat mod, negated | `(h : ¬(n % 2 = 1)) : ¬((n+1) % 2 = 1)` | FAIL | goal-shape sensitive | AGREE |
| p07 | simp | `2 + 2 = 4 := by simp` | PASS | present in core | AGREE |
| p08 | norm_num | `2 + 2 = 4 := by norm_num` | FAIL (unknown tactic) | absent | AGREE |
| p09 | ring | `a + b = b + a := by ring` | FAIL (unknown tactic) | absent | AGREE |
| p10 | Nat.factorial | `Nat.factorial 5 = 120 := by rfl` | FAIL (unknown ident) | absent | AGREE |
| p11 | Real.pi | `#check Real.pi` | FAIL (unknown ident) | absent | AGREE |
| p12 | Nat xor, closed | `(5 ^^^ 3) = 6 := by decide` | **PASS** | "decide fails on Nat bitwise XOR" | **REFINED** |
| p12b | Nat xor, variable | `(a : Nat) : (a ^^^ 0) = a := by decide` | FAIL | — | boundary confirmed |
| p13 | Nat decide | `12 * 12 / 4 = 36 := by decide` | PASS | the working pattern | AGREE |
| p14 | Bool xor decide | `Bool.xor true true = false := by decide` | PASS | the working pattern | AGREE |
| p15 | scaffold lakefile | scaffolded project as shipped, `lake build` | FAIL (package config) | Lake 5.0 rejects template | AGREE |

**14/15 AGREE; 1 refinement (p12).** The refinement: on this exact 4.35.0
build, `decide` *does* kernel-reduce **closed-literal** Nat bitwise XOR
(`5 ^^^ 3 = 6`); the failure the paper reported reproduces for **non-closed**
xor goals (`∀ a, (a ^^^ 0) = a`, probe p12b). The paper's blanket sentence
"decide also fails on Nat bitwise XOR" should be read as the general
(variable) goal shape; the probe-first discipline records the boundary
exactly.
