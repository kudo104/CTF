# Flag Checker
## Miêu tả 
* Someone posted an interesting idea on Discord about encrypting a message. I implemented it and here is the program to check the flag.
* File : _chall.exe_
## Phân tích 
* Load file vào ida
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // esi
  int v4; // esi
  int v6; // [esp-8h] [ebp-14h]
  int v7; // [esp+0h] [ebp-Ch]

  sub_131A880();
  if ( unknown_libname_8() )
  {
    sub_131A7B0(L"--- Invoked %s [version: %s, commit hash: %s] main = {", L"apphost");
    for ( i = 0; i < argc; ++i )
      sub_131A7B0(L"%s", argv[i]);
    sub_131A7B0(L"}", v7);
  }
  sub_1319730();
  v4 = sub_131F390(argc, argv);
  sub_131A710();
  sub_131A170(v4, v6);
  return v4;
}
```
* Phân tích thì không có gì đặc biệt
* Mình quan sát String thì mình thấy một file dll rất lạ _VSCTF.dll_

```
.rdata:0132FAF4	0000000B	C	__p___argc
.rdata:0132FB02	0000000C	C	__p___wargv
.rdata:0132FB10	00000008	C	_c_exit
.rdata:0132FB1A	0000002B	C	_register_thread_local_exe_atexit_callback
.rdata:0132FB48	00000014	C	_configthreadlocale
.rdata:0132FB5E	0000000E	C	_set_new_mode
.rdata:0132FB6E	0000000D	C	__p__commode
.rdata:0132FB7E	0000000D	C	_controlfp_s
.rdata:0132FB8E	00000009	C	strcpy_s
.data:0133000C	00000006	C	ja 8r{
.data:01330041	00000024	C	38cc827-e34f-4453-9df4-1e796e9f1d07
.data:013300C8	0000000A	C	VSCTF.dll
.data:013304D8	00000051	C	Copyright (c) by P.J. Plauger, licensed by Dinkumware, Ltd. ALL RIGHTS RESERVED.
.data:013305A0	00000018	C	.?AVruntime_error@std@@
.data:013305C0	00000014	C	.?AVexception@std@@
.data:013305DC	0000001B	C	.?AVfailure@ios_base@std@@
.data:01330600	00000017	C	.?AVsystem_error@std@@
.data:01330620	00000018	C	.?AV_System_error@std@@
.data:01330640	00000013	C	.?AVios_base@std@@
.data:0133065C	00000014	C	.?AV?$_Iosb@H@std@@
.data:01330678	00000030	C	.?AV?$basic_ios@_WU?$char_traits@_W@std@@@std@@
.data:013306B0	00000036	C	.?AV?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@
.data:013306F0	00000034	C	.?AV?$basic_istream@_WU?$char_traits@_W@std@@@std@@
.data:0133072C	00000034	C	.?AV?$basic_ostream@_WU?$char_traits@_W@std@@@std@@
.data:01330768	00000035	C	.?AV?$basic_iostream@_WU?$char_traits@_W@std@@@std@@
.data:013307A8	00000048	C	.?AV?$basic_stringbuf@_WU?$char_traits@_W@std@@V?$allocator@_W@2@@std@@
.data:013307F8	0000004B	C	.?AV?$basic_stringstream@_WU?$char_traits@_W@std@@V?$allocator@_W@2@@std@@
.data:0133084C	00000016	C	.?AV_Facet_base@std@@
.data:0133086C	00000017	C	.?AVfacet@locale@std@@
.data:0133088C	0000001A	C	.?AU_Crt_new_delete@std@@
.data:013308B0	00000015	C	.?AUctype_base@std@@
```

> Dump _VSCTF.dll_
* Mình sẽ chạy thử file vào tìm đường dẫn sinh ra _VSCTF.dll_ tại bảng _Modules_ của ida 

![alt text](https://github.com/kudo104/CTF/blob/main/vsctf/Flag%20Checker/Picture/Screenshot%202022-07-13%20204352.png)

## Phân tích _VSCTF.dll_
* File được code bằng C#
* Load file vào dnspy
```
private static void Main(string[] args)
{
	Console.Write("Enter the flag: ");
	string text = Console.ReadLine();
	if (text.Length != 32)
	{
		Console.WriteLine("Wrong flag.");
		return;
	}
	string input = text.Substring(0, text.Length / 2);
	string input2 = text.Substring(text.Length / 2);
	byte[] array = Utils.OwO(input).Concat(Utils.OaO(input2)).ToArray<byte>();
	if (array.Length != 48)
	{
		Console.WriteLine("Wrong flag.");
		return;
	}
	for (int i = 0; i < array.Length; i++)
	{
		if ((Secrets.SuperConfidential[i] ^ i) != (int)array[i])
		{
			Console.WriteLine("Wrong flag.");
			return;
		}
	}
	Console.WriteLine("Correct! You got the flag.");
}
```
* Độ dài kí tự fake_flag là 32, fake_flag chia làm 2 vào hai hàm OwO và OaO và Concat lại thành 1 biến array so sánh với ``(Secrets.SuperConfidential[i] ^ i)``
* Để khôi phục lại flag mình cần phân tích hai hàm OwO và OaO làm gì
> Hàm OwO
```
public static byte[] OaO(string input)
{
	if (input == null || input.Length <= 0)
	{
		return Array.Empty<byte>();
	}
	byte[] bytes = Encoding.ASCII.GetBytes(Secrets.fish);
	for (int i = 0; i < bytes.Length; i++)
	{
		bytes[i] = (byte)(i ^ (int)bytes[i]);
	}
	return new BlowFish(bytes)
	{
		IV = Encoding.ASCII.GetBytes(Secrets.bite)
	}.EncryptCBC(Encoding.ASCII.GetBytes(input));
}
```
- Hàm này dùng mã hóa BlowFish 
> Hàm OaO
```
public static byte[] OwO(string input)
{
	if (input == null || input.Length <= 0)
	{
		return Array.Empty<byte>();
	}
	byte[] result;
	using (Aes aes = Aes.Create())
	{
		aes.Key = Encoding.ASCII.GetBytes(Secrets.rickroll);
		aes.IV = Encoding.ASCII.GetBytes(Secrets.dance);
		ICryptoTransform transform = aes.CreateEncryptor(aes.Key, aes.IV);
		using (MemoryStream memoryStream = new MemoryStream())
		{
			using (CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write))
			{
				using (StreamWriter streamWriter = new StreamWriter(cryptoStream))
				{
					streamWriter.Write(input);
				}
				result = memoryStream.ToArray();
			}
		}
	}
	return result;
}
```
Hàm này dùng mã hóa AES mode CBC 

> Key và iv của BlowFish và AES_CBC đều lưu trong class Secrets 

```
namespace VSCTF
{
	// Token: 0x02000003 RID: 3
	internal class Secrets
	{
		// Token: 0x04000001 RID: 1
		public static readonly string F14gH3r3 = "vsctf{dQw4w9WgXcQ}";

		// Token: 0x04000002 RID: 2
		public static readonly string rickroll = "Never_gonna_give_View_Source_up!";

		// Token: 0x04000003 RID: 3
		public static readonly string dance = "y0ur_f1r5t_3v3nt";

		// Token: 0x04000004 RID: 4
		public static readonly string Copyright = "@sahuang#6271";

		// Token: 0x04000005 RID: 5
		public static readonly string AnotherOne = "vsctf{REDACTED}";

		// Token: 0x04000006 RID: 6
		public static readonly string fish = "i_am_a_tiny_fish";

		// Token: 0x04000007 RID: 7
		public static readonly string bite = "QAQ?QAQ!";

		// Token: 0x04000008 RID: 8
		public static readonly int[] SuperConfidential = new int[]
		{
			84,201,30,221,189,40,193,255,191,235,23,199,136,17,83,32,45,66,52,24,203,140,251,39,121,252,139,63,142,108,109,219,122,210,72,35,146,64,226,84,24,33,178,48,156,245,115,234
		};
	}
}
```

##  Scirpt
```
from Cryptodome.Cipher import AES
import blowfish 
enc = [	84,201,30,221,189,40,193,255,191,235,23,199,136,17,83,32,45,66,52,24,203,140,251,39,121,252,139,63,142,108,109,219,122,210,72,35,146,64,226,84,24,33,178,48,156,245,115,234]

for i in range(48):
	enc[i] = enc[i] ^ i

enc1 = enc[0:16]
enc2 = enc[32:]
key1 = "i_am_a_tiny_fish"
key_1 = [0]*len(key1)
for i in range(len(key1)):
	key_1[i] = ord(key1[i]) ^ i
key_1 = bytearray(key_1)
iv1 = bytearray("QAQ?QAQ!","ascii")
key2 = bytearray("Never_gonna_give_View_Source_up!","ascii")
iv2 = bytearray("y0ur_f1r5t_3v3nt","ascii")
cipher = AES.new(key2,AES.MODE_CBC,iv2)
enc2 = bytearray(enc2)
enc1 = bytearray(enc1)
print(cipher.decrypt(enc1))

cipher = blowfish.Cipher(key_1)
data_decrypted = b"".join(cipher.decrypt_cbc(enc2, iv1))
print(data_decrypted)
```
# Flag
``vsctf{y0u_n33d_AES&BLOWFISH_727}``
