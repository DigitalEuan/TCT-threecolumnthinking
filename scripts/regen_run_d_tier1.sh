#!/bin/bash
# Run D Tier-1: isolated verification of all 12 column3 scripts + 31 spot checks.
V="python3 /home/z/my-project/tct_work/scripts/verify_column3.py"
BASE=/home/z/my-project/tct_run_d
cd "$BASE"
: > results.log
pass=0; fail=0
for t in T01 T02 T03 T04 T05 T06 T07 T08 T09 T10 T11 T12; do
  out=$($V "$t/column3.py" 2>&1); code=$?
  final=$(echo "$out" | tail -1)
  echo "$t: exit=$code final=$final" | tee -a results.log
  [ $code -eq 0 ] && pass=$((pass+1)) || fail=$((fail+1))
done
echo "tier1: $pass/12 VERIFIED, $fail failed" | tee -a results.log

: > spot_checks.log
chk() { out=$($V "$BASE/$1/column3.py" --key "$2" --expect "$3" 2>&1); \
  if [ $? -eq 0 ]; then echo "PASS $1: $2=$3" >> spot_checks.log; \
  else echo "FAIL $1: $2=$3 ($out)" >> spot_checks.log; fi; }
# 31 pre-declared spot checks (documented values)
chk T01 STORED_ENERGY_J 2
chk T01 MAX_SPEED 2
chk T02 H3 3645/8192
chk T02 TOTAL_DISTANCE 125/14
chk T02 TOTAL_TIME 5
chk T03 T 5/7
chk T03 V 7
chk T03 H 5/2
chk T04 SUBMERGED 2750/2997
chk T04 ABOVE 247/2997
chk T05 NEXT_DAY_INDEX 4
chk T05 CALENDAR_ANCHOR_OK 1
chk T06 ANSWER_INT 2
chk T06 F2_VALUE 0
chk T06 MOD7_VALUE 2
chk T07 ANSWER 10
chk T07 PASCAL 10
chk T08 AMOUNT 9261/80
chk T08 TERMINATING 1
chk T09 GEOMETRIC 32
chk T09 CUBIC 30
chk T09 REFUSAL UNDERDETERMINED
chk T10 STERN_BROCOT 267/85
chk T10 PI_IN_BRACKET 1
chk T10 WIDTH 168/100000
chk T11 ANSWER_STATE 1
chk T11 PARITY 1
chk T12 P_VI 60
chk T12 P_I2R 100
chk T12 P_V2R 36
chk T12 REFUSAL INCONSISTENT_GIVENS
p=$(grep -c PASS spot_checks.log); f=$(grep -c FAIL spot_checks.log)
echo "spot checks: $p/31 PASS, $f FAIL" | tee -a results.log
[ "$p" = "31" ] && [ "$fail" = "0" ] && echo "TIER1_DONE_OK"
