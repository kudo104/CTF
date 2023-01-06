d = [1,2,3,5,8 ,0xd ,0x15 ,0x22 ,0x37 ,0x59 ,0x90] 
d1 =[48, 52, 115, 105, 125, 126, 38, 16, 10, 109,0xa8]

# Password
for i in range(11):
	print(chr(d[i] ^ d1[i]),end = "")