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
