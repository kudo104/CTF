from pwn import *


f = open("log2.txt","r")

def Convert(string):
    li = list(string.split(" "))
    return li

for line in f:
	line = line[0:len(line)-1]
	l = Convert(line)
	op = []
	for c in l:
		op.append(int(c))
	# print(op)
	print(disasm(bytes(op)))
import idaapi
import time
f = open("log.txt","w")

