#!/usr/bin/env python3
"""T11 - A light is off; the switch is flipped 17 times (F2 at declared XOR site)"""

FLIPS = 17
# declared reading: each flip toggles the state (switch convention)
# state = 0 XOR (FLIPS mod 2)  -- parity arithmetic in F2:
parity = FLIPS % 2
assert parity == 1
final_state = (0 + FLIPS) % 2
assert final_state == 1                        # ON (odd number of toggles)
even_check = (0 + 16) % 2
assert even_check == 0                         # 16 flips would return OFF
# the general parity law (Lean: omega): (n+2) % 2 = n % 2
for n in range(-6, 24):
    assert (n + 2) % 2 == n % 2

print(f"FLIPS={FLIPS}")
print(f"PARITY={parity}")
print(f"FINAL_STATE={final_state}")
print(f"EVEN_CHECK={even_check}")
print(f"ANSWER_STATE={final_state}")
