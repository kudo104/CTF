from PIL import Image


def func(pixels,v13,v12,idx):
	if(int(idx//8) == 0):
		pi = pixels[v13,v12][2]
	if(int(idx//8) == 1):
		pi = pixels[v13,v12][1]
	if(int(idx//8) == 2):
		pi = pixels[v13,v12][0]
	re = pi >> (idx % 8) & 1
	r,g,b = pixels[v13,v12]
	print("v13:{} v12:{} idx:{} r:{} g:{} b:{} {} {}".format(v13,v12,idx,hex(r),hex(g),hex(b),hex(pi),re))
	return re 

im = Image.open("yougotrickrolledChallenge.bmp")

pixels = im.load()

size = im.height * im.width
d = []
v12 = im.height - 1
v13 = 0
idx = 0
s = ""

for i in range(400):

	t = func(pixels,v13,v12,idx)
	s += str(t)
	v3 = idx + 1 
	idx = (idx + 1) // 24
	idx = v3 - 24 * idx
	if(t):
		v12 = v12 - 1 
	else:
		v13 = v13 + 1

