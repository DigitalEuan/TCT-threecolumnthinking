#!/bin/bash
# Run D Lean tier: scaffold all 12 projects from specs, apply the named
# Lake 5.0 workaround, build, and log. Regenerated after environment recycle.
export ELAN_HOME=/home/z/my-project/tct_work/lean_dist/elan
export PATH="$ELAN_HOME/bin:$PATH"
BASE=/home/z/my-project/tct_run_d
SC=/home/z/my-project/tct_work/scripts/scaffold_lean_project.py
LOG=$BASE/lean_tier.log
: > "$LOG"
pass=0; fail=0
for t in T01 T02 T03 T04 T05 T06 T07 T08 T09 T10 T11 T12; do
  d="$BASE/$t/lean_tct"
  rm -rf "$d"
  python3 "$SC" --spec "$BASE/$t/spec.json" --out "$d" --name "tct_$t" >> "$LOG" 2>&1
  # Named Lake 5.0 workaround (the skill's template is Lake-4-era):
  printf 'import Lake\nopen Lake DSL\npackage tct_%s where\n  moreServerArgs := #["-DwarningAsError=false"]\n@[default_target]\nlean_lib TCT where\n  globs := #[.one `TCT.Basic]\n' "$t" > "$d/lakefile.lean"
  (cd "$d" && lake build > /tmp/rd_build.txt 2>&1)
  if [ $? -eq 0 ]; then
    pass=$((pass+1))
    echo "$t: BUILD OK  (sorry warnings: $(grep -c 'declaration uses .sorry' /tmp/rd_build.txt))" | tee -a "$LOG"
  else
    fail=$((fail+1))
    echo "$t: BUILD FAILED" | tee -a "$LOG"
    grep "error" /tmp/rd_build.txt | head -5 | sed 's/^/    /' | tee -a "$LOG"
  fi
done
echo "lean tier: $pass/12 built, $fail failed" | tee -a "$LOG"
[ $pass -eq 12 ] && echo "LEAN_TIER_DONE_OK"
