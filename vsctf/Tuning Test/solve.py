from z3 import*

a1 = [BitVec("s_%d"%i,8) for i in range(36)]

sol = Solver()
# for i in a1:
# 	sol.add(i > 0x20)
# 	sol.add(i <= 0x7f)

sol.add(a1[26] + a1[24] + a1[15] + a1[13] + a1[4] + a1[2] + a1[0] + a1[28] == 486)
sol.add(a1[1] * a1[0] - a1[4] + a1[12] * a1[13] - a1[16] + a1[24] * a1[25] - a1[28] == 0x3591)
sol.add(a1[27] * a1[14] * a1[3] - a1[15] * a1[2] * a1[25] == -6256)
sol.add((a1[1] - a1[3]) * a1[4] == 48)
sol.add((8 * a1[13] - 4 * a1[15]) * a1[14] == 0x507C)
sol.add((4 * a1[28] - 4 * a1[0]) * a1[27] == 0xFFFFEA10)
q = a1[16] - a1[15] - a1[14] - a1[13] + a1[12] * a1[12] == 0x965
p = a1[4] - a1[3] - a1[2] - a1[1] + a1[0] * a1[0] == 6744
d = a1[28] - a1[27] - a1[26] - a1[25] + a1[24] * a1[24] == 0x100B
for i in a1:
	sol.add(Or(And(i >= 48, i <= 57),And(i >= 65, i <= 90)))
sol.add(And(q,And(p,d)))
sol.add(And(a1[14] <= 57,(a1[14] + a1[24]) * (a1[28] - a1[1]) == -1508))
sol.check()

s1 = ""
for i in a1:
	m = sol.model()
	s1 += chr(m[i].as_long())

import base64
import os

key = "vsCTF is a capture the flag competition organized by Team View Source. vsCTF is meant for players of all skill levels and everyone is welcomed to participate and learn."
data = base64.b64decode(b"nRYEZjDuqxtlL8L6EatC")
array = []
for i in range(256):
    array.append(i)
num = 0
for i in range(256):
    num = (num + array[i] + ord(key[i%len(key)])) % 256
    num2 = array[i]
    array[i] = array[num]
    array[num] = num2
num = 0
k = 0
out = [None]*len(data)
m = 0
for i in range(len(data)):
    k = (k + 1) % 256
    num = (num + array[k]) % 256
    num3 = array[k]
    array[k] = array[num]
    array[num] = num3
    num4 = array[(array[k] + array[num]) % 256]
    out[i] = chr(data[i] ^ num4)

s2 = ""
for i in out:
    if( ord(i) >= 0x20 and ord(i) < 0x7f):
        s2 += i

k = 0
for i in range(36):
    if(i % 12 > 5 and i %  12 <= 10):
        print(s2[k],end = "")
        k = k + 1
    else:
        if((i % 6) == 5):
            print("-",end="")
        else:
            print(s1[i],end = "")
