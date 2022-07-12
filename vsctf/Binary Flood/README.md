# Binary Flood
# Miêu tả
* Someone sent me a bunch of binaries and told me that he hid a secret behind the trees. I have no idea what he means, can you help me out?
* File : Binary Flood

## Tổng quan 
* Có tất cả 1337 fille.
## Phân tích file_0
* Load file_0 vào ida
``` 
  std::string::basic_string(v9, a2, a3);
  std::operator<<<std::char_traits<char>>(&std::cout, "Enter the key: ");
  std::operator>><char>(&std::cin, v9);
  sub_401880(v8);
  v14 = v9;
  v6 = std::string::begin(v9);
  v5 = std::string::end(v14);
  while ( __gnu_cxx::operator!=<std::unique_ptr<spdlog::details::flag_formatter> *,std::vector<std::unique_ptr<spdlog::details::flag_formatter>>>(
            &v6,
            &v5) )
  {
    v7 = *sub_401B1C(&v6);
    make(v8, &v7);
    nlohmann::detail::primitive_iterator_t::operator++(&v6);
  }
  v13 = sub_401BAA(v8);
  v3 = v13;
  sub_401BCA(v10, v8);
  v12 = sub_4013E0(v10, v3);
  std::__cxx1998::vector<double,std::allocator<double>>::~vector(v10);
  sub_40147F(v11, v12);
  LOBYTE(v3) = std::operator==<char>(v11, "NzPxDxwEv9TLmgFVNjCRjcEJgKMiCJBBvcY0mKo");
  std::string::~string(v11);
  if ( v3 )
    std::operator<<<std::char_traits<char>>(&std::cout, "You got it.\n");
  else
    std::operator<<<std::char_traits<char>>(&std::cout, "Nope.\n");
  std::__cxx1998::vector<double,std::allocator<double>>::~vector(v8);
  std::string::~string(v9);
  return 0LL;
  ```
* Sau khi phân tích thì biết file thực hiện nhập fake_key sau đó kiểm tra với chuỗi mã hóa _NzPxDxwEv9TLmgFVNjCRjcEJgKMiCJBBvcY0mKo_
* Mình quan sát thấy được sau khi mã hóa thì fake_key chỉ thay đổi vị trí

> Tìm từng vị trí kí tự
```
s1 = ''
s2 = ''
idx = []
for i in range(39):
	for j in range(39):
		if(s1[i] == s2[j]):
			idx.append(j)
```
> Phục hồi lại chuỗi ban đầu

```
for i in range(39):
	print(s1[idx[i]],end = "")
```
* Sau khi phục hồi được chuỗi _JVBERi0xLjcKJcKzx9gNCjEgMCBvYmoNPDwvTmF_ đây là chuỗi mã hóa base64

* Giải mã ra thì đây là một đoạn header của file pdf

Vậy mình cần viết script để đọc tất cả các chuỗi phục hồi,giải mã base64
[solve.py](https://github.com/kudo104/CTF/blob/main/vsctf/Binary%20Flood/solve.py)

Sau khi chạy script thì flag trong file pdf
## Flag:
vsctf{templated_binaries_are_1337}


