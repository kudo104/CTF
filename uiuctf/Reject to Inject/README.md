# Reject to Inject
## Miêu tả
`"a sad little foal, cute, watery eyes, ultra detailed, octane render"`

`Seems like the patient is afraid of needles. Can you go help him?`

`Author: yuiop`
## Phân tích

Bài này cho 1 file IV.dll 
Phân tích IV.dll tại DllMain thì có tạo một thread 

```
BOOL __stdcall DllMain_0(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
  HANDLE Thread; // rax

  j___CheckForDebuggerJustMyCode(&unk_7FF9FFFCC0A0);
  if ( fdwReason == 1 )
  {
    Thread = CreateThread(0i64, 0i64, StartAddress, hinstDLL, 0, 0i64);
    CloseHandle(Thread);
  }
  return 1;
}
```
Phân tích `StartAddress` 
```
  memset(ProfileDir, 0, 0x800ui64);
  cchSize[0] = 2048;
  TokenHandle = 0i64;
  SizeInBytes = 0i64;
  v14 = "\\Room2004";
  v15 = "\\sigpwnie.exe";
  memset(Filename, 0, 0x400ui64);
  nSize = 1024;
  v19 = 0;
  strcpy(v20, "IS7WXGC726Z9JZMFPOKWQVMEPJCSU2FIMAC5N2VYIPGFJPCZPROPMYNL");
  memset(Src, 0, 0x38ui64);
  MaxCount = 56i64;
  memset(Dst, 0, 0x1C0ui64);
  CurrentProcess = GetCurrentProcess();
  OpenProcessToken(CurrentProcess, 8u, &TokenHandle);
  GetUserProfileDirectoryW(TokenHandle, ProfileDir, cchSize);
  CloseHandle(TokenHandle);
  memset_0(v24, 8, v4);
  sub_7FF9FFFB144C(v24, ProfileDir);
  SizeInBytes = sub_7FF9FFFB1343(v24);
  strcpy(Str1, SizeInBytes, v5);
  strcat_s_0(Str1, v14, v6);
  strcat_s_0(Str1, v15, v7);
  GetModuleFileNameA(0i64, Filename, nSize);
  v19 = strncmp(Str1, Filename, nSize);
  if ( v19 )
  {
    j_printf("Failed!\n");
    system("pause");
    FreeLibraryAndExitThread(a1, 0);
  }
  sub_7FF9FFFB11B8(v20, Src);
  memccpy(Dst, Src, 125, MaxCount);
  v25 = MessageBoxA(0i64, Dst, "Success", 0);
  sub_7FF9FFFB141A(v24);
  return v25;
```
* Tại hàm này nó sẽ nối path `C:\Users\name\Room2004\sigpwnie.exe`siggpwnie.exe lưu tại Str1 
so sánh với Filename,Filename lấy path sử dụng api `GetModuleFileNameA` 

Sau khi so sánh nếu bằng nhau thì sẽ tới hàm sub_7FF9FFFB11B8() để giải mã flag 
Để lấy flag mình dùng api LoadLibraryA load IV.dll đặt bp tại memccpy để lấy flag  
