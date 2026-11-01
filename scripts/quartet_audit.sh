#!/usr/bin/env bash
# Full quartet audit (regenerated): tier1, spot checks, ledger scans,
# and the three-phase Lean build audit (as-shipped / notation-repaired /
# native_decide). Logs to /home/z/my-project/tct_quartet_audit/.
set -e
export ELAN_HOME=/home/z/my-project/tct_work/lean_dist/elan
export PATH="$ELAN_HOME/bin:$PATH"
BASE=/home/z/my-project/case_studies
W=/home/z/my-project/tct_work
OUT=/home/z/my-project/tct_quartet_audit
V="python3 $W/scripts/verify_column3.py"
mkdir -p "$OUT"

# 1. scripts byte-identity
LOG=$OUT/scripts_diff.log; : > $LOG
for s in $BASE/*/*/; do n=$(basename $s); printf "%-34s" "$n:" >> $LOG
  ok=1; for f in verify_column3.py scaffold_lean_project.py lean_ledger.py cent_cost.py; do
    diff -q "$s/scripts/$f" "$W/scripts/$f" >/dev/null 2>&1 || { ok=0; printf " %s:DIFF" "$f" >> $LOG; }
  done
  [ $ok -eq 1 ] && echo " all 4 IDENTICAL to skill S13" >> $LOG || echo "" >> $LOG
done

# 2. tier1 rerun
LOG=$OUT/tier1_rerun.log; : > $LOG
for s in $BASE/*/*/; do n=$(basename $s); echo "=== $n ===" >> $LOG
  (cd "$s" && for f in scripts/column3/0*.py; do
    out=$($V "$f" 2>&1); code=$?
    printf "  %-30s exit=%d %s\n" "$(basename $f)" "$code" "$(echo "$out" | tail -1 | cut -c1-55)" >> $LOG
  done)
done

# 3. spot checks (14)
LOG=$OUT/spot_checks.log; : > $LOG
chk() { study="$1"; out=$($V "$2" --key "$3" --expect "$4" 2>&1); \
  if [ $? -eq 0 ]; then echo "PASS $study: $3=$4" >> $LOG; else echo "FAIL $study: $3=$4" >> $LOG; fi; }
cd $BASE/famous-constants-tct/famous-constants-tct
chk famous-constants scripts/column3/01_pi_convergents.py INTERVALS_OVERLAP 1
chk famous-constants scripts/column3/03_zeta2_basel.py Z2_CONTAINED 1
chk famous-constants scripts/column3/06_taxonomy.py TAXONOMY_VALID 1
cd $BASE/maudlin-measurement-trilemma-tct/maudlin-measurement-trilemma-tct
chk maudlin-trilemma scripts/column3/02_born_decoherence.py PURITY 1/2
chk maudlin-trilemma scripts/column3/03_grw_collapse_rate.py TAU_MACRO_S 1/10000000
chk maudlin-trilemma scripts/column3/04_branch_counting.py BRANCHES_10 1024
chk maudlin-trilemma scripts/column3/05_doors_truth_table.py DOORS 3
cd $BASE/physical-isomorphisms-tct/physical-isomorphisms-tct
chk physical-isomorphisms scripts/column3/01_crossbar_break_even.py BREAKEVEN_N 55
chk physical-isomorphisms scripts/column3/02_convolution_amortization.py BREAKEVEN_T 21
chk physical-isomorphisms scripts/column3/03_stochastic_streams.py N_FOR_1PCT 2500
chk physical-isomorphisms scripts/column3/04_analog_ode.py M_MIN 1500
cd $BASE/speed-of-light-derivation-tct/speed-of-light-derivation-tct
chk speed-of-light scripts/column3/01_si_definition.py DEFINITIONAL 1
chk speed-of-light scripts/column3/06_alpha_boundary.py INV_ALPHA_FLOOR 137
chk speed-of-light scripts/column3/06_alpha_boundary.py REFUSAL_REGISTERED 1
cd $BASE

# 4. ledger scans + cent_cost
LOG=$OUT/ledger_and_loop.log; : > $LOG
for s in $BASE/*/*/; do n=$(basename $s); p=$(ls -d $s/lean/tct_* | head -1)
  echo "── $n" >> $LOG
  python3 $W/scripts/lean_ledger.py "$p" >> $LOG 2>&1
  python3 $W/scripts/cent_cost.py --before "$s/cent/decomp_v1.json" --after "$s/cent/decomp_v2.json" >> $LOG 2>&1
done

# 5. three-phase Lean builds
LOG=$OUT/lean_build_audit.log; : > $LOG
for s in $BASE/*/*/; do n=$(basename $s); p=$(ls -d $s/lean/tct_* | head -1)
  echo "=== $n (as shipped) ===" >> $LOG
  (cd "$p" && rm -rf .lake && lake build > /tmp/qa.txt 2>&1) || true
  grep -m1 error /tmp/qa.txt | sed 's/^/  /' >> $LOG || echo "  BUILD OK (unexpected)" >> $LOG
done
echo "=== notation repair + native_decide phase ===" >> $LOG
python3 - <<'PYEOF'
import os, re, shutil
BASE = "/home/z/my-project/case_studies"
OUT = "/home/z/my-project/tct_work/repaired"
DIRS = {
 "famous-constants": "famous-constants-tct/famous-constants-tct/lean/tct_constants",
 "maudlin-trilemma": "maudlin-measurement-trilemma-tct/maudlin-measurement-trilemma-tct/lean/tct_maudlin",
 "physical-isomorphisms": "physical-isomorphisms-tct/physical-isomorphisms-tct/lean/tct_physiso",
 "speed-of-light": "speed-of-light-derivation-tct/speed-of-light-derivation-tct/lean/tct_lightcone",
}
os.makedirs(OUT, exist_ok=True)
for name, rel in DIRS.items():
    src, dst = os.path.join(BASE, rel), os.path.join(OUT, name)
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(src, dst)
    lb = os.path.join(dst, ".lake")
    if os.path.exists(lb): shutil.rmtree(lb)
    basic = os.path.join(dst, "TCT", "Basic.lean")
    text = open(basic, encoding="utf-8").read()
    nN, nQ = text.count("ℕ"), text.count("ℚ")
    text = text.replace("ℕ", "Nat").replace("ℚ", "Rat")
    text = re.sub(r"^  decide$", "  native_decide", text, flags=re.M)
    open(basic, "w", encoding="utf-8").write(text)
    pkg = re.search(r"^package (\S+)", open(os.path.join(src, "lakefile.lean")).read(), re.M).group(1)
    open(os.path.join(dst, "lakefile.lean"), "w").write(
        'import Lake\nopen Lake DSL\npackage %s where\n'
        '  moreServerArgs := #["-DwarningAsError=false"]\n'
        '@[default_target]\nlean_lib TCT where\n  globs := #[.one `TCT.Basic]\n' % pkg)
    print(f"{name}: repaired {nN} N-occurrences, {nQ} Q-occurrences, decide->native_decide")
PYEOF
for d in $W/repaired/*/; do n=$(basename $d)
  echo "=== $n (repaired: Nat/Rat + native_decide) ===" >> $LOG
  (cd "$d" && rm -rf .lake && lake build > /tmp/qr.txt 2>&1)
  if [ $? -eq 0 ]; then
    echo "  BUILD OK — sorry warnings: $(grep -c 'declaration uses .sorry' /tmp/qr.txt)" >> $LOG
  else
    echo "  BUILD FAILED" >> $LOG; grep error /tmp/qr.txt | head -4 | sed 's/^/    /' >> $LOG
  fi
done
echo "QUARTET_AUDIT_DONE"
