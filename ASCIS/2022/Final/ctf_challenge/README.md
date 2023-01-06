# ctf_challenge
Tác giả cho 2 file ctf_challenge và flag.txt.Đây là một dạng bài phục hồi lại nội dung trong file.

![alt](https://github.com/kudo104/CTF/blob/main/ASCIS/2022/Final/ctf_challenge/picture/2.png)

Bỏ vào ida thì biết được chương trình đọc nội dung flag.txt để encrypt

![alt](https://github.com/kudo104/CTF/blob/main/ASCIS/2022/Final/ctf_challenge/picture/1.png)

Tạo file flag.txt và thử thêm nôi dụng là `ASCIS{aaaaaaaaa}` để chạy file. Hmm nhìn khá là ảo thử lấy đống hex này sang string thử ,chương trình lại cho ra đúng nội dung của flag.

![alt](https://github.com/kudo104/CTF/blob/main/ASCIS/2022/Final/ctf_challenge/picture/3.png)

Tiếp tục re tiếp thì bài này là một dạng vm mình sẽ không nói chi tiết mấy cái này tại thấy dài dòng quá.Bài này cấp phát một vùng nhớ 50 byte có quyền thực thi và set cái tất cả các byte trong vùng nhớ thành 0x90 đây chính là lệnh nop và thêm 2 byte ``\xEB\xFE`` này vào vùng nhớ gần cuối đây chính là lệnh jump nhảy tới chính nó đó.Sau đó nó sẽ tạo Thread vô tận đợi đến khi mà chương trình gọi ``SuspendThread`` để tạm dừng Thread lại.Sau đó chương trình sẽ tính toán và sẽ thực thi từng câu lệnh một trong vùng nhớ này.

```
char *__thiscall sub_321040(char *this, _OWORD *a2)
{
  LPVOID v3; // eax
  _OWORD *v4; // ecx
  char *v5; // ecx
  int v6; // eax
  int v7; // ecx
  int v8; // eax
  void *v10; // [esp-10h] [ebp-1Ch]
  void *v11; // [esp-Ch] [ebp-18h]
  LPTHREAD_START_ROUTINE lpStartAddress; // [esp+8h] [ebp-4h]

  *this = &VM::`vftable';
  *(this + 2) = this;
  *(this + 12) = 0i64;
  *(this + 28) = 0i64;
  *(this + 11) = 0;
  lpStartAddress = VirtualAlloc(0, 0x50u, 0x3000u, 0x40u);
  *(this + 16) = VirtualAlloc(0, 0x40u, 0x1000u, 0x40u);
  *(this + 14) = VirtualAlloc(0, 0x40u, 0x3000u, 4u);
  v3 = VirtualAlloc(0, 0xC8u, 0x3000u, 4u);
  v10 = *(this + 14);
  *(this + 17) = v3;
  memset(v10, 0, 0x40u);
  memset(*(this + 17), 0, 0x40u);
  memset(*(this + 16), 0, 0x200u);
  memset(lpStartAddress, 144, 0x50u);
  v4 = *(this + 14);
  if ( v4 )
  {
    if ( a2 )
    {
      *v4 = *a2;
      v4[1] = a2[1];
      v4[2] = a2[2];
      v4[3] = a2[3];
      goto LABEL_6;
    }
    memset(v4, 0, 0x40u);
  }
  *errno() = 22;
  invalid_parameter_noinfo();
LABEL_6:
  v5 = *(this + 17);
  if ( v5 )
  {
    strcpy(v5, "1234567890123456");
  }
  else
  {
    *errno() = 22;
    invalid_parameter_noinfo();
  }
  *(this + 15) = lpStartAddress;
  *(lpStartAddress + 72) = '\xEB';
  *(*(this + 15) + 73) = '\xFE';
  *(this + 376) = CreateThread(0, 0, lpStartAddress, 0, 0, 0);
  Sleep(0x3E8u);
  SuspendThread(*(this + 376));
  *(this + 197) = 65599;
  GetThreadContext(*(this + 376), (this + 788));
  *(this + 237) = *(this + 17);
  *(this + 236) = *(this + 14);
  v6 = *(this + 16);
  v11 = *(this + 376);
  *(this + 241) = 0;
  v7 = v6 + 384;
  *(this + 238) = 0;
  v6 += 32;
  *(this + 240) = 0;
  *(this + 13) = v6;
  *(this + 246) = v6;
  v8 = *(this + 15);
  *(this + 239) = 0;
  *(this + 12) = v7;
  *(this + 242) = v7;
  *(this + 243) = v8;
  SetThreadContext(v11, (this + 788));
  return this;
}
```

Đang chú ý trong quá trình debug thì mình bị lỗi segment liên tục thì phát hiện có 1 anti hardware breapoint

```
BOOL __thiscall sub_E1930(int *this)
{
  void *v3; // [esp-Ch] [ebp-14h]
  void *v4; // [esp-8h] [ebp-10h]

  SuspendThread(this[376]);
  GetThreadContext(this[376], (this + 197));
  v3 = this[15];
  this[243] = v3;
  memset(v3, 0x90, 0x50u);
  *(this[15] + 72) = -21;
  *(this[15] + 73) = -2;
  if ( this[198] || this[199] || this[200] || this[201] )
  {
    *(this[15] + 72) = 0x90;
    *(this[15] + 73) = 0x90;
  }
  v4 = this[376];
  this[198] = 0;
  this[199] = 0;
  this[200] = 0;
  this[201] = 0;
  this[202] = 0;
  this[203] = 0;
  return SetThreadContext(v4, (this + 197));
}
```

Đến đây mình patch lại chương trình tưởng có thể chạy ngon lành cành đào rồi nhưng không nó lại in ra đúng nối dung của file flag.txt.Mình thử debug tới câu lệnh cuối cùng trong vùng nhớ rồi in ra thì biết được nó tính độ dài của chuỗi và so sánh với 0x24.Hmm chạy ngon rồi haha.

Mình patch lại như sau:

```
BOOL __thiscall sub_321930(int *this)
{
  void *v3; // [esp-Ch] [ebp-14h]
  void *v4; // [esp-8h] [ebp-10h]

  SuspendThread(this[376]);
  GetThreadContext(this[376], (this + 197));
  v3 = this[15];
  this[243] = v3;
  memset(v3, 144, 0x50u);
  *(this[15] + 72) = '\xEB';
  *(this[15] + 73) = '\xFE';
  v4 = this[376];
  this[198] = 0;
  this[199] = 0;
  this[200] = 0;
  this[201] = 0;
  this[202] = 0;
  this[203] = 0;
  return SetThreadContext(v4, (this + 197));
}
```

Mình sử dụng mấy câu lẹnh debug_hook của ida không chạy được nên đành chạy tay lấy từng câu lệnh một click đến khi nào chương trình dừng thì thôi do mình lười emulate lại cái code vm :vv

```
import idaapi
import time

f = open("log.txt","a")

idaapi.run_to(0xB81F93)

data = []
# ea là địa chỉ vùng nhớ được cấp phát 50 byte để thực thi câu lệnh
for ea in range(0x950000,0x950006,1):
    data.append(idc.get_wide_byte(ea))
    
s = ' '.join([str(elem) for elem in data])
s += "\n"
f.write(s)
f.close()
```

Sau khi đọc mấy cái code vm này thì biết được đây là mã hóa ``XTEA``.Đoạn Vm sử dụng Xtea 4 lần mỗi lần là 8 byte ban đầu key là ```1234567890123456``` sau đó nó sẽ thực hiện thay đổi key lần lược như sau xor 4 byte với 0xefbeadde và đặt tại 4 byte tiếp theo.

```
   0:   89 78 04                mov    DWORD PTR [eax+0x4], edi
   0:   8b 1c 24                mov    ebx, DWORD PTR [esp]
   0:   8b 74 24 04             mov    esi, DWORD PTR [esp+0x4]
   0:   8b 7c 24 08             mov    edi, DWORD PTR [esp+0x8]
   0:   8b 56 04                mov    edx, DWORD PTR [esi+0x4]
   0:   bb de ad be ef          mov    ebx, 0xefbeadde
   0:   31 da                   xor    edx, ebx
   0:   89 56 08                mov    DWORD PTR [esi+0x8], edx
   0:   81 c7 08 00 00 00       add    edi, 0x8
   0:   89 7d 08                mov    DWORD PTR [ebp+0x8], edi
```
Đọc các đoạn tiếp theo mình được key và script giải mã flag:

```
#include <stdint.h>
#include <stdio.h>


void decrypt (uint32_t v[2], const uint32_t k[4]) {
    uint32_t v0 = v[0], v1 = v[1], sum = 0xf1bbcdc8, i;  /* set up; sum is (delta << 5) & 0xFFFFFFFF */
    uint32_t delta = 0x9E3779B9;                     /* a key schedule constant */
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];   /* cache key */
    
    for (i=0; i < 8; i++) {                         /* basic cycle start */
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
        sum -= delta;
    }               
    
    v[0] = v0; v[1] = v1;
	
	for(int i = 0;i < 4 ; i ++){
		printf("%c",(v0 >> (8*i)) & 0xff);
	}
	for(int i = 0;i < 4 ; i ++){
		printf("%c",(v1 >> (8*i)) & 0xff);
	}
}

int main(){
	uint32_t key1[4] = {0x34333231,0x38373635, 0x32313039, 0x36353433};
//	uint32_t hash[8] = {0x32a86394,0xaea320ce, 0x8d1cbc04, 0xb1228e7a, 0x11b1318a,0xb70ad3aa,0xa2708b62,0x820c8b81};
	uint32_t hash1[2] = {0x32a86394, 0xaea320ce};
	decrypt(hash1,key1);
//	for(int i =0; i < 4; i++){
//		uint32_t h[2];
//		h[0] = hash[i * 2];
//		h[1] = hash[i * 2 + 1];
//		printf("%x %x\n",h[0],h[1]);
//		decrypt(h,key);
//	}
	uint32_t key2[4] = {0x34333231,0xDBFE99B8, 0x32313039, 0x36353433};
	uint32_t hash2[2] = {0x8d1cbc04, 0xb1228e7a};
	decrypt(hash2,key2);
	
	uint32_t key3[4] = {0x34333231,0xDBFE99B8, 0x34403466, 0x36353433};
	uint32_t hash3[2] = {0x11b1318a,0xb70ad3aa};
	decrypt(hash3,key3);
	
	uint32_t key4[4] = {0xDADB5450,0xDBFE99B8, 0x34403466, 0x36353433};
	uint32_t hash4[2] = {0xa2708b62,0x820c8b81};
	decrypt(hash4,key4);
	
	return 0;
}

```

Flag: ``ASCIS{M@sT3r_0f_V1rtu4l_m4Ch1n3}``