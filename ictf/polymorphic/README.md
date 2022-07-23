# Polymorphic

## Phân tích
Nhập fake_flag thì bị crash
```
kudo104@DESKTOP-3H61LP8:/mnt/d/ATTT/RE/exercise/ictf/_polymorphic$ ./polymorphic
123456
Segmentation fault (core dumped)
```
Load vào ida để phân tích
```
.text:0000000000401000                 xor     dword ptr cs:loc_40100A, 4E784379h
.text:000000000040100A
.text:000000000040100A loc_40100A:                             ; DATA XREF: .text:_start↑w
.text:000000000040100A                 sub     rax, 0FFFFFFFFFFFFFFDEh
.text:000000000040100E                 xor     dword ptr cs:loc_401022, 0A5D80C00h
.text:0000000000401018                 xor     dword ptr cs:loc_401022+4, 6AE4AAB1h
.text:0000000000401022
.text:0000000000401022 loc_401022:                             ; DATA XREF: .text:000000000040100E↑w
.text:0000000000401022                                         ; .text:0000000000401018↑w
.text:0000000000401022                 lea     rsi, ds:0FFFFFFFFFAE4AAB1h
.text:000000000040102A                 xor     dword ptr cs:loc_401034, 0B1507C79h
.text:0000000000401034
.text:0000000000401034 loc_401034:                             ; DATA XREF: .text:000000000040102A↑w
.text:0000000000401034                 add     rax, 21h ; '!'
.text:0000000000401038                 xor     dword ptr cs:loc_401042, 79D6092Fh
.text:0000000000401042
.text:0000000000401042 loc_401042:                             ; DATA XREF: .text:0000000000401038↑w
.text:0000000000401042                 xor     byte ptr [eax], 0E9h
.text:0000000000401046                 xor     dword ptr cs:loc_40105A, 25340DF2h
.text:0000000000401050                 xor     dword ptr cs:loc_40105A+4, 9C7F82BCh
.text:000000000040105A
.text:000000000040105A loc_40105A:                             ; DATA XREF: .text:0000000000401046↑w
.text:000000000040105A                                         ; .text:0000000000401050↑w
.text:000000000040105A                 lea     rsi, ds:0CEF12BCh
.text:0000000000401062                 xor     dword ptr cs:loc_40106C, 0C0508647h
.text:000000000040106C
.text:000000000040106C loc_40106C:                             ; DATA XREF: .text:0000000000401062↑w
.text:000000000040106C                 add     rax, 50h ; 'P'
.text:0000000000401070                 xor     cs:dword_40107A, 0DF1484EDh
```
Tại Engtrypoint chương trình dùng phép xor để giải mã từng opcode cho nên mình sẽ dùng idapython để giải mã để phân tích
```
import idaapi

import idautils,idaapi

ea = 0x401000
end_ea = 0x401C74
while(ea <= end_ea):
      if idc.print_insn_mnem(ea) == "xor" and idc.get_operand_type(ea,0) == 2:
            v = idc.get_wide_dword(ea + 6)
            ea_xref = 0
            for address in idautils.DataRefsFrom(ea):
                 ea_xref = address
                 break      
            tmp = idc.get_wide_dword(ea_xref) ^ v
            idc.patch_dword(ea_xref,tmp)
      ea = idc.next_head(ea)
```
Sau khi giải mã 
```
.text:0000000000401000                 xor     dword ptr cs:loc_40100A, 4E784379h
.text:000000000040100A
.text:000000000040100A loc_40100A:                             ; DATA XREF: _start↑w
.text:000000000040100A                 xor     eax, eax
.text:000000000040100C                 nop
.text:000000000040100D                 nop
.text:000000000040100E                 xor     dword ptr cs:loc_401022, 0A5D80C00h
.text:0000000000401018                 xor     dword ptr cs:loc_401022+4, 6AE4AAB1h
.text:0000000000401022
.text:0000000000401022 loc_401022:                             ; DATA XREF: _start+E↑w
.text:0000000000401022                                         ; _start+18↑w
.text:0000000000401022                 sub     rsp, 80h
.text:0000000000401029                 nop
.text:000000000040102A                 xor     dword ptr cs:loc_401034, 0B1507C79h
.text:0000000000401034
.text:0000000000401034 loc_401034:                             ; DATA XREF: _start+2A↑w
.text:0000000000401034                 xor     edi, edi
.text:0000000000401036                 nop
.text:0000000000401037                 nop
.text:0000000000401038                 xor     dword ptr cs:loc_401042, 79D6092Fh
.text:0000000000401042
.text:0000000000401042 loc_401042:                             ; DATA XREF: _start+38↑w
.text:0000000000401042                 mov     rsi, rsp
.text:0000000000401045                 nop
.text:0000000000401046                 xor     dword ptr cs:loc_40105A, 25340DF2h
.text:0000000000401050                 xor     dword ptr cs:loc_40105A+4, 9C7F82BCh
.text:0000000000401050 _start          endp ; sp-analysis failed
.text:0000000000401050
.text:000000000040105A
.text:000000000040105A loc_40105A:                             ; DATA XREF: _start+46↑w
.text:000000000040105A                                         ; _start+50↑w
.text:000000000040105A                 mov     edx, 80h
.text:000000000040105F                 nop
.text:0000000000401060                 nop
.text:0000000000401061                 nop
.text:0000000000401062                 xor     dword ptr cs:loc_40106C, 0C0508647h
```
Sau khi đọc qua từng instruction thì nó kiểm tra từng kí tự của flag lưu trong stack
nếu đúng thì sẽ kiểm tra kí tự tiếp theo sai thì chương trình sẽ crash.


Mình sẽ viết script để đọc từng instruction ghi vào file txt cho dễ đọc

```
import idaapi,idautils

ea = 0x401000
end_ea = 0x401C74
off = []
while(ea <= end_ea):
      if idc.print_insn_mnem(ea) == "xor" and idc.get_operand_type(ea,0) == 2:
            for address in idautils.DataRefsFrom(ea):
                 off.append(address)
                 break      
      ea = idc.next_head(ea)
      
f = open("asm.txt","w")  

for p in off:
    if idc.print_insn_mnem(p) == "nop":
        continue
    else:
        s = hex(p) + " " + idc.generate_disasm_line(p,0)
        f.write(str(s) + "\n")
```
# Flag
`ictf{dynam1c_d3bugg1ng_1s_n1ce}`
