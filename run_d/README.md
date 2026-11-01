# Run D artifact bundle (regenerated)

Twelve-question battery (T01–T12) of the updated TCT skill, spanning eight
domains, evaluated with Lean 4.35.0 / Lake 5.0.0 in-environment. This copy
was **regenerated and re-verified live** on 2026-11-01 after the original
run payload was lost to an environment recycle; see REGENERATION_NOTES.md
for provenance. Everything here is executable and was executed to produce
the logs in this directory.

```
tct_run_d/
  README.md                  <- this file
  REGENERATION_NOTES.md      <- provenance: what was lost, what is regenerated, from what
  RUN_D_SUMMARY.md           <- battery table + tier status + four-conditions accounting
  optimization_loop.md       <- loop record: 7 accepted / 5 floors / 6 tautologies
  results.log                <- Tier-1 live log (12/12 VERIFIED, 31/31 spot checks)
  spot_checks.log            <- the 31 pre-declared spot checks
  lean_tier.log              <- scaffold + build log (12/12 OK, 56/9/25)
  specs/                     <- the 12 spec.json sources (+ copies in each T-dir)
  T01..T12/
    column3.py               <- Column-3 re-derivation (exact rationals only)
    spec.json                <- classified lemma spec
    lean_tct/                <- scaffolded Lean 4 Lake project (BUILT; lakefile
                                carries the named Lake 5.0 workaround)
    decomp_before.json       <- v1 primitives (pre-loop or floor)
    decomp_after.json        <- v2 primitives (post-loop)
  lean_probe/                <- 15 live environment probes + probe_run.log +
                                probe_results.md
```

## Re-verify (Python 3 stdlib only; no installs)

```bash
for t in T??; do python3 <path-to-skill>/verify_column3.py $t/column3.py; done
python3 <path-to-skill>/lean_ledger.py T01/lean_tct     # etc.
python3 <path-to-skill>/cent_cost.py --before T02/decomp_before.json --after T02/decomp_after.json
# Lean (with lean/lake on PATH): cd T01/lean_tct && lake build
```
