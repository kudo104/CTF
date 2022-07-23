from z3 import *

s = [BitVec("s_%d"%i,64) for i in range(3)]
key = [0x7870148BF499D6F9, 0x435E9C9331495B55, 0x910A96FDF83DEB08]
c = 0x39E324B32F573C94
sol = Solver()
for i in range(3):
	c = s[i] ^ ((c * c) & 0xffffffffffffffff)
	sol.add(c == key[i])

print(sol.check())
m = sol.model()
for i in range(3):
	print(hex(m[s[i]].as_long()))

# s = "}3d92a1_ed0cnedd1h{ftci"

# print(s[::-1])


