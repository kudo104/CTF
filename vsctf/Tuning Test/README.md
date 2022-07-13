# Tuning Test
## Miêu tả
* I failed again in winning a Tuning Test qualification at miHoYo's new game, Zenless Zone Zero. Fortunately, there's a second chance for CTF players - I could get an invitation code by entering the correct serial key. Please help!
* File : _zzz_
## Phân tích
* Load file vào ida
```
  v14 = __readfsqword(0x28u);
  puts(off_5010);
  s = malloc(0x23uLL);
  printf("Enter the serial key to unlock ZZZ Tuning Test qualification: ");
  __isoc99_scanf("%35s", s);
  if ( strlen(s) != 35 || sub_1BFA(s) != 1 || !sub_1C82(s) )
  {
    puts("Invalid serial key.");
    return 0LL;
  }
  else
  {
    memset(buff, 0, sizeof(buff));
    strcpy(
      key,
      "vsCTF is a capture the flag competition organized by Team View Source. vsCTF is meant for players of all skill lev"
      "els and everyone is welcomed to participate and learn.");
    memset(&key[169], 0, 87);
    v6 = 0;
    for ( i = 0; i < strlen(s); ++i )
    {
      if ( i % 12 > 5 && i % 12 <= 10 )
      {
        idx = v6++;
        s_1[idx] = s[i];
      }
    }
    s_1[v6] = 0;
    size = strlen(s_1);
    size_key = strlen(key);
    sub_1774(buff, key, size_key);
    sub_1A51(buff, s_1, size);
    s1 = sub_12E9(s_1, size);
    if ( !strcmp(s1, "nRYEZjDuqxtlL8L6EatC") )
    {
      puts("Congratulations! You have won ZZZ Tuning Test qualification.");
      printf("Your flag: ");
      sub_1B88();
    }
    else
    {
      puts("Invalid serial key.");
    }
    return 0LL;
```
> Hàm main thực hiện kiểm tra flag chia làm 2 phần:
1. Hàm _sub_1BFA()_ và _sub_1C82()_
    * Hàm sub_1BFA() dùng để kiểm tra vị trí nhất định phải có kí tự "-"
    ```
    __int64 __fastcall sub_1BFA(const char *a1)
    {
        int i; // [rsp+1Ch] [rbp-14h]

        for ( i = 0; i < strlen(a1); ++i )
        {
            if ( i % 6 == 5 && a1[i] != '-' )
            return 0LL;
        }
        return 1LL;
    }
    ```
    * Hàm sub_1C82() 
    ```
    v6 = a1[26] + a1[24] + a1[15] + a1[13] + a1[4] + a1[2] + *a1 + a1[28] == 486;
    v7 = a1[1] * *a1 - a1[4] + a1[12] * a1[13] - a1[16] + a1[24] * a1[25] - a1[28] == 0x3591;
    v8 = a1[27] * a1[14] * a1[3] - a1[15] * a1[2] * a1[25] == -6256;
    v9 = (a1[1] - a1[3]) * a1[4] == 48;
    v10 = (8 * a1[13] - 4 * a1[15]) * a1[14] == 0x507C;
    v11 = (4 * a1[28] - 4 * *a1) * a1[27] == 0xFFFFEA10;
    v5 = 1;
    for ( i = 0; i < strlen(a1); ++i )
    {
        if ( i % 12 <= 4 && (a1[i] > 90 || a1[i] <= 47 || a1[i] > 57 && a1[i] <= 64) )
        v5 = 0;
    }
    v1 = a1[4] - a1[3] - a1[2] - a1[1] + *a1 * *a1 == 6744
        && a1[16] - a1[15] - a1[14] - a1[13] + a1[12] * a1[12] == 0x965
        && a1[28] - a1[27] - a1[26] - a1[25] + a1[24] * a1[24] == 0x100B;
    v12 = v1;
    v2 = a1[14] <= 57 && (a1[14] + a1[24]) * (a1[28] - a1[1]) == -1508;
    return v6 && v7 && v8 && v9 && v10 && v11 && v5 && v12 && v2;
    ```
    - Hàm này kiểm tra tại các kí tự 0-4,12-16,24-28
2. Các kí tự còn lại sử dụng mã hóa rc4 sau đó dùng base64 để kiểm tra các kí tự còn lại tại hàm _sub_1774()_,_sub_1A51()_ và _sub_12E9()_
## Script
```
from z3 import*
import base64
import os


# 1.z3 
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

# 2.rc4 
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
            print(s1[i],end="")
```
## Serial
>> SE8D0-vsctf-2K31P-4begi-AD648-nnerz