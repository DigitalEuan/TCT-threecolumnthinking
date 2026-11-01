# RUN D SUMMARY — broad-domain battery (regenerated)

Platform: dola.com's AI system (agent sandbox), updated 14-section skill,
Lean 4.35.0 / Lake 5.0.0 installed in-environment. Regenerated and
re-verified live on 1 Nov 2026 after an environment recycle (see
REGENERATION_NOTES.md).

## Battery results

| Test | Question (domain) | n | p | s | a | r | Lean p/s/a | build |
|---|---|---|---|---|---|---|---|---|
| T01 | spring (conceptual physics) | 12 | 6 | 2 | 4 | 0 | 6/2/3 | OK |
| T02 | bounce (conceptual physics) | 12 | 7 | 2 | 3 | 0 | 5/2/3 | OK |
| T03 | "what is gravity?" (definition) | 12 | 5 | 1 | 6 | 0 | 4/1/5 | OK |
| T04 | water expansion (empirical) | 13 | 6 | 1 | 6 | 0 | 4/1/5 | OK |
| T05 | after Wednesday (Z/7Z, calendar) | 7 | 6 | 0 | 1 | 0 | 4/0/1 | OK |
| T06 | 1+1 (arithmetic, domain decl.) | 5 | 5 | 0 | 0 | 0 | 5/0/0 | OK |
| T07 | 2-of-5 toppings (combinatorics) | 6 | 4 | 1 | 1 | 0 | 5/1/1 | OK |
| T08 | compound interest (finance, Q) | 7 | 5 | 1 | 1 | 0 | 4/1/1 | OK |
| T09 | next term 2,4,8,16 (refusal) | 7 | 5 | 0 | 1 | 1 | 4/0/1 | OK |
| T10 | circle area (irrational, bounds) | 11 | 7 | 1 | 3 | 0 | 4/1/3 | OK |
| T11 | 17 switch flips (F2, XOR site) | 7 | 6 | 0 | 1 | 0 | 7/0/1 | OK |
| T12 | V=12, I=5, R=4 (refusal) | 6 | 4 | 0 | 1 | 1 | 4/0/1 | OK |
| | **Totals** | **105** | **66** | **9** | **28** | **2** | **56/9/25** | **12/12** |

Classification identity: **105 = 66 + 9 + 28 + 2** (closes exactly).

## Tier status (this regeneration)

- Tier 1 (Python, isolated subprocesses): **12/12 VERIFIED**;
  **31/31** pre-declared spot checks (`--key/--expect`) PASS
  (`results.log`, `spot_checks.log`), including both refusal verdicts
  (`REFUSED:UNDERDETERMINED`, `REFUSED:INCONSISTENT_GIVENS`), the π-bracket
  containment, and the exact bounce ledger (h₃ = 3645/8192 m, total distance
  125/14 m, total time exactly 5 s).
- Tier 2 (Lean): **12/12 `lake build` OK** (`lean_tier.log`), 56 proved /
  9 sorry / 25 axioms, five projects sorry-free (T05, T06, T09, T11, T12).
  The kernel refuted the regenerated T10 lower-bound lemma on first attempt
  (314103·71 = 223·100000 + **813** is false; the correct constant is
  **1313**) — the same class of catch the original run made on the bounce
  lemma. Proof patterns: Nat/Int `decide`, Nat cross-multiplication,
  `omega` for Int-mod/parity laws, one `rfl`, one Bool `decide`.
- Optimisation loop: 7 accepted / 5 floor stops (`optimization_loop.md`).
- Environment probes: 14/15 AGREE with the paper's documented findings;
  1 boundary refinement (p12, see `lean_probe/probe_results.md`).
