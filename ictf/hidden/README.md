# Hidden


## Phân tích

Load file vào ida

```
.text:0000560B7E690289                 endbr64
.text:0000560B7E69028D                 push    rbp
.text:0000560B7E69028E                 mov     rbp, rsp
.text:0000560B7E690291                 push    rbx
.text:0000560B7E690292                 sub     rsp, 238h
.text:0000560B7E690299                 mov     rax, fs:28h
.text:0000560B7E6902A2                 mov     [rbp+var_18], rax
.text:0000560B7E6902A6                 xor     eax, eax
.text:0000560B7E6902A8                 lea     rdi, aCanYouGetTheFl ; "Can you get the flag?"
.text:0000560B7E6902AF                 call    checkFlag
.text:0000560B7E6902B4 ; ---------------------------------------------------------------------------
.text:0000560B7E6902B4                 mov     rdx, cs:__bss_start
.text:0000560B7E6902BB                 lea     rax, [rbp+var_220]
.text:0000560B7E6902C2                 mov     esi, 32h ; '2'
.text:0000560B7E6902C7                 mov     rdi, rax
.text:0000560B7E6902CA                 call    near ptr loc_560B7E69012C+4
.text:0000560B7E6902CF ; ---------------------------------------------------------------------------
.text:0000560B7E6902CF                 lea     rax, [rbp+var_220]
.text:0000560B7E6902D6                 mov     edx, 7
.text:0000560B7E6902DB                 mov     esi, 64h ; 'd'
.text:0000560B7E6902E0                 mov     rdi, rax
.text:0000560B7E6902E3                 mov     eax, 0
.text:0000560B7E6902E8                 call    near ptr loc_560B7E69015F+1
.text:0000560B7E6902ED ; ---------------------------------------------------------------------------
.text:0000560B7E6902ED                 lea     rdi, aAreYouSureThou ; "are you sure though "
.text:0000560B7E6902F4                 mov     eax, 0
.text:0000560B7E6902F9                 call    near ptr loc_560B7E69011D+3
.text:0000560B7E6902FE ; ---------------------------------------------------------------------------
.text:0000560B7E6902FE                 lea     rax, [rbp+var_221]
.text:0000560B7E690305                 mov     rsi, rax
.text:0000560B7E690308                 lea     rdi, aCC        ; "%c%*c"
.text:0000560B7E69030F                 mov     eax, 0
.text:0000560B7E690314                 call    loc_560B7E690180
.text:0000560B7E690314 main            endp
```

> Hàm checkFlag()
```
  v0 = sys_read(0, v6, 30uLL);
  v1 = v6;
  v5[2] = 0x910A96FDF83DEB08LL;
  v5[1] = 0x435E9C9331495B55LL;
  v5[0] = 0x7870148BF499D6F9LL;
  v2 = v5;
  v3 = 0LL;
  v4[0] = 0x39E324B32F573C94LL;
  while ( 1 )
  {
    v4[0] = *v1 ^ (v4[0] * v4[0]);
    if ( v4[0] != *v2 )
      break;
    if ( ++v3 == 3 )
      break;
    v1 += 8;
    ++v2;
  }
  __asm
  {
    syscall; LINUX - sys_write
    syscall; LINUX - sys_exit
  }
  exit(1);
```
Hàm này thực hiện kiểm tra flag dựa trên các constant nên sẽ dùng z3 để tìm ẩn

## Script
```
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
```
# Flag
`ictf{h1ddenc0de_1a29d3}`
