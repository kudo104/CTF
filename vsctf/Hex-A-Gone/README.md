# HEX-A-GONE
## Miêu tả 
* Fall Guys is now free for all, but it comes with some risks. An evil fall guy made a ransomware to corrupt the game and prevent you from getting the crown. Can you beat him and win the game?
* File: `flag.enc.bmp` , ``hex-a-gone``
## Tổng quan
* Tác giả cho một file binary và file ảnh bmp đã bị mã hóa
* Nhiệm vụ là giải mã file bmp lấy flag
## Phân tích 
* Load file vào ida
```
  *&v11[22] = __readfsqword(0x28u);
  printf(
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿Hex-A-Gone⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠉⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⢀⣠⣶⣶⣶⣶⣤⡀⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⣾⡿⢿⣿⣿⡿⢿⣿⡆⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⠄⢿⣇⣸⣿⣿⣇⣸⡿⠃⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠉⠛⠛⠛⠛⠉⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿⣿\n"
    "⣿⣿⣿⡟⠄⠄⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿\n"
    "⣿⣿⡟⠄⠄⠄⢠⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣧⠄⠄⠄⠈⢿⣿\n"
    "⣿⣿⡇⠄⠄⠄⣾⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣧⠄⠄⠄⠘⣿\n"
    "⣿⣿⣇⠄⣰⣶⣿⣿⣿⣦⣀⡀⠄⠄⠄⠄⠄⠄⠄⢀⣠⣴⣿⣿⣿⣶⣆⠄⢀⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⢸⣿⠇⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣴⣾⣿⣶⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n",
    15000LL,
    a3);
  strcpy(v11, "flag.bmp");
  strcpy(&v11[9], "flag.enc.bmp");
  usleep(0xB71B0u);
  printf("Encrypting flag...\n", 75000LL, 15000LL);
  encrypt_file(v9, v11);
  write_file(&v11[9], v11, v3, v4, v5, v6, v9[0], v9[1], v9[2], v10[0]);
  usleep(0x16E360u);
  printf("Saving encrypted image to flag.enc...\n", 150000LL, 15000LL);
  usleep(0xB71B0u);
  printf("Successful!\n", 15000LL, v7);
  return 0LL;
```
* Đoạn code trong hàm _main_ thực hiện việc đọc file, mã hóa và viết lại file bmp thành _enc.bmp_
> Hàm encrypt_file()
```
  v22 = __readfsqword(0x28u);
  parse_bmp(&im, a2);
  num = 123LL;
  v15 = calloc(2 * im.height_ * im.witdh, 8uLL);
  for ( i = 0; i < 2 * im.height_ * im.witdh; ++i )
  {
    num = devran(num);
    v15[i] = num;
  }
  ptr = calloc(im.height_ * im.witdh, 4uLL);
  for ( j = 0; j < im.height_ * im.witdh; ++j )
    ptr[j] = j;
  for ( size = im.height_ * im.witdh - 1; size > 0; --size )
  {
    v12 = v15[size] % (size + 1);
    v13 = ptr[v12];
    ptr[v12] = ptr[size];
    ptr[size] = v13;
  }
  alloc = calloc(3 * im.witdh * im.height_, 1uLL);
  for ( k = 0; k < im.height_ * im.witdh; ++k )
  {
    v2 = &pixels[3 * ptr[ptr[k]]];
    v3 = &alloc[3 * k];
    *v3 = *v2;
    v3[2] = v2[2];
  }
  *pixels = *alloc ^ WORD1(v15[im.height_ * im.witdh]);
  pixels[1] = alloc[1] ^ 1 ^ BYTE1(v15[im.height_ * im.witdh]);
  pixels[2] = alloc[2] ^ 0x41 ^ v15[im.height_ * im.witdh];
  for ( m = 1; m < im.height_ * im.witdh; ++m )
  {
    pixels[3 * m] = WORD1(v15[im.witdh * im.height_ + m]) ^ alloc[3 * m] ^ pixels[3 * m - 3];
    pixels[3 * m + 1] = BYTE1(v15[im.witdh * im.height_ + m]) ^ alloc[3 * m + 1] ^ pixels[3 * m - 2];
    pixels[3 * m + 2] = v15[im.witdh * im.height_ + m] ^ alloc[3 * m + 2] ^ pixels[3 * m - 1];
  }
  free(alloc);
  free(v15);
  free(ptr);
  v4 = pixels;
  *a1 = im;
  a1[1] = v4;
  v5 = v21;
  a1[2] = v20;
  a1[3] = v5;
  return a1;
```
* Hàm này thực hiện đọc từng pixels tại hàm _parse_bmp_ và mã hóa hóa từng pixels
* Hàm devran là một hàm sinh số mặc định
    ```
    _int64 __fastcall sub_558E6E79F31A(unsigned __int64 a1)
    {
        unsigned __int64 v2; // [rsp+0h] [rbp-8h]

        v2 = (((a1 << 13) ^ a1) >> 7) ^ (a1 << 13) ^ a1;
        return (v2 << 17) ^ v2;
    }
    ```
* Mình có thấy thuật toán mã hóa chỉ có một ẩn số là _alloc_ còn tất cả các biến khác đều có \
>> Vậy chỉ cần viết ngược lại thuật toán ban đầu là mình có thể giải mã được file bmp
## Script
```
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

```
## Flag
out.bmp


