from PIL import Image
import numpy as np

im = Image.open("flag.enc.bmp")

d = im.load()
size = im.height * im.width
h = im.height
pixels = []
dec = []
for i in range(im.height):
	for j in range(im.width):
		r,g,b = d[j,h-1]
		enc = []
		enc2 = []
		enc2.append(0)
		enc2.append(0)
		enc2.append(0)
		enc.append(ord(chr(r)))
		enc.append(ord(chr(g)))
		enc.append(ord(chr(b)))
		dec.append(enc2)
		pixels.append(enc)
	h = h - 1

def devran(a1):
	v2 = (((a1 << 13) & 0xffffffffffffffff ) ^ a1) &  0xffffffffffffffff
	v2 = (((v2 >> 7) & 0xffffffffffffffff) ^ v2) & 0xffffffffffffffff
	v2 = (((v2 << 17) & 0xffffffffffffffff) ^ v2 ) & 0xffffffffffffffff
	v2 = v2 & 0xffffffffffffffff
	return v2

size = im.height * im.width
v15 = []
num = 123
for i in range(2 * size):
	num = devran(num)
	v15.append(num)

ptr = []
for i in range(size):
	ptr.append(i)

k = size - 1
while(k > 0):
	v12 = v15[k] % (k + 1)
	v13 = ptr[v12]
	ptr[v12] = ptr[k]
	ptr[k] = v13
	k = k - 1

dec[0][0] = ((v15[im.height * im.width] >> 16) & 0xff) ^ pixels[0][0] 
dec[0][1] = ((v15[im.height * im.width] >> 8) & 0xff) ^ 1 ^ pixels[0][1]
dec[0][2] = (v15[im.height * im.width] & 0xff) ^ 0x41 ^pixels[0][2]


for n in range(1,size,1):
	dec[n][0] = ((v15[im.width * im.height + n] >> 16) & 0xff) ^ pixels[n - 1][0] ^ pixels[n][0] 
	dec[n][1] = ((v15[im.width * im.height + n] >> 8) & 0xff) ^ pixels[n - 1][1] ^ pixels[n][1]
	dec[n][2] = (v15[im.width * im.height + n] & 0xff) ^ pixels[n - 1][2] ^ pixels[n][2]


for i in range(size):
	pixels[ptr[ptr[i]]][0] = dec[i][0]
	pixels[ptr[ptr[i]]][1] = dec[i][1]
	pixels[ptr[ptr[i]]][2] = dec[i][2] 

h = im.height
m = 0 
for i in range(im.height):
	for j in range(im.width):
		r,g,b = pixels[m]
		d[j,h-1] = r,g,b
		m = m + 1
	h = h - 1
	
im.save("out.bmp")
