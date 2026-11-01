#!/usr/bin/env bash
# Run D environment probes: re-verify every pure-core Lean claim live.
export ELAN_HOME=/home/z/my-project/tct_work/lean_dist/elan
export PATH="$ELAN_HOME/bin:$PATH"
P=/home/z/my-project/tct_run_d/lean_probe
rm -rf "$P"; mkdir -p "$P"

cat > $P/p01_Q_notation.lean <<'EOF'
example : (12 : ℚ)^2 / 4 = 36 := by decide
EOF
cat > $P/p02_rat_decide.lean <<'EOF'
example : (12 : Rat)^2 / 4 = 36 := by decide
EOF
cat > $P/p03_rat_rfl.lean <<'EOF'
example : (12 : Rat)^2 / 4 = 36 := by rfl
EOF
cat > $P/p04_rat_native_decide.lean <<'EOF'
example : (12 : Rat)^2 / 4 = 36 := by native_decide
EOF
cat > $P/p05_omega_int_mod.lean <<'EOF'
example : ∀ n : Int, (n + 1) % 7 = (n % 7 + 1) % 7 := by omega
EOF
cat > $P/p06_omega_nat_mod_negated.lean <<'EOF'
example (n : Nat) (h : ¬(n % 2 = 1)) : ¬((n + 1) % 2 = 1) := by omega
EOF
cat > $P/p07_simp.lean <<'EOF'
example : 2 + 2 = 4 := by simp
EOF
cat > $P/p08_norm_num.lean <<'EOF'
example : 2 + 2 = 4 := by norm_num
EOF
cat > $P/p09_ring.lean <<'EOF'
example (a b : Nat) : a + b = b + a := by ring
EOF
cat > $P/p10_nat_factorial.lean <<'EOF'
example : Nat.factorial 5 = 120 := by rfl
EOF
cat > $P/p11_real_pi.lean <<'EOF'
#check Real.pi
EOF
cat > $P/p12_nat_xor_decide.lean <<'EOF'
example : (5 ^^^ 3) = 6 := by decide
EOF
cat > $P/p13_nat_decide.lean <<'EOF'
example : 12 * 12 / 4 = 36 := by decide
EOF
cat > $P/p14_bool_xor_decide.lean <<'EOF'
example : Bool.xor true true = false := by decide
EOF

LOG=$P/probe_run.log
: > "$LOG"
declare -A EXPECT=(
  [p01_Q_notation]=FAIL [p02_rat_decide]=FAIL [p03_rat_rfl]=FAIL
  [p04_rat_native_decide]=PASS [p05_omega_int_mod]=PASS
  [p06_omega_nat_mod_negated]=FAIL [p07_simp]=PASS [p08_norm_num]=FAIL
  [p09_ring]=FAIL [p10_nat_factorial]=FAIL [p11_real_pi]=FAIL
  [p12_nat_xor_decide]=FAIL [p13_nat_decide]=PASS [p14_bool_xor_decide]=PASS
)
for f in $P/p*.lean; do
  n=$(basename "$f" .lean)
  err=$(lean "$f" 2>&1); code=$?
  [ $code -eq 0 ] && res=PASS || res=FAIL
  firsterr=$(echo "$err" | grep -m1 "error" | head -c 90)
  agree=$([ "$res" = "${EXPECT[$n]}" ] && echo AGREE || echo DISAGREE)
  printf "%-28s live=%-4s expected=%-4s %s | %s\n" "$n" "$res" "${EXPECT[$n]}" "$agree" "$firsterr" | tee -a "$LOG"
done

# p15: scaffolded project as shipped (no workaround) vs Lake 5.0
SC=/home/z/my-project/tct_work/scripts/scaffold_lean_project.py
D=$P/p15_scaffold_as_shipped
echo '{"module":"TCT","imports":[],"definitions":[],"axioms":[],"lemmas":[{"name":"trivial_one","type":"1 + 1 = 2","proof":"decide"}]}' > $P/p15_spec.json
python3 "$SC" --spec $P/p15_spec.json --out "$D" --name tct_p15 >/dev/null 2>&1
(cd "$D" && lake build > /tmp/p15.txt 2>&1); code=$?
[ $code -eq 0 ] && res=PASS || res=FAIL
printf "%-28s live=%-4s expected=FAIL %s | %s\n" "p15_scaffold_lake5" "$res" \
  "$([ $res = FAIL ] && echo AGREE || echo DISAGREE)" "$(grep -m1 error /tmp/p15.txt | head -c 90)" | tee -a "$LOG"
echo "PROBES_DONE"
