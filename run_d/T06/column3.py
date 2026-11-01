#!/usr/bin/env python3
"""T06 - What is 1+1? (the domain declaration is load-bearing)"""

# domain-declared answers:
int_value = 1 + 1                             # Z: successor route
assert int_value == 2
f2_value = (1 + 1) % 2                        # F2 at the declared XOR site
assert f2_value == 0
mod7_value = (1 + 1) % 7                      # Z/7Z
assert mod7_value == 2

# three genuinely disjoint routes to the Z answer:
r1 = 2                                        # definitional successor
r2 = len({("L", 0)} | {("R", 1)})             # tagged disjoint-union cardinality
r3 = len([(a, b) for a in (0, 1) for b in (0,)])  # explicit pairing: 1+1 = 2*1
assert r1 == r2 == r3 == 2
assert (True != True) is False                # Bool xor site

print(f"INT_VALUE={int_value}")
print(f"F2_VALUE={f2_value}")
print(f"MOD7_VALUE={mod7_value}")
print("ROUTES=3")
print(f"ANSWER_INT={int_value}")
