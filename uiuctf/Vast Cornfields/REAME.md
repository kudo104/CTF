# Vast Cornfields
## Miêu tả
`Iterative functions are sooooooo last year. All the cool kids are keeping secrets with recursion nowadays`

`author: Spamakin`
## Phân tích
Phân tích file vast_cornfield tại hàm main có 1 đoạn so sánh chuỗi đã bị encode
```
    for ( i = 0; ; i = encode(dest, i) )
    {
    v10 = strlen(dest);
    if ( !less(i, v10) )
        break;
    }
    v11 = strcmp(dest, "odt_sjtfnb_jc_c_fiajb_he_ciuh_nkn_atvfjp");
```

> Hàm encode()
```
  while ( eq(*(a1 + i1), 0x5F) )
    i1 = inc(i1);
  for ( i2 = inc(i1); eq(*(a1 + i2), 0x5F); i2 = inc(i2) )
    ;
  s_i = *(a1 + i1);
  v14 = 0;
  for ( i = less(0, 5u); i; i = less(v14, 5u) )
  {
    v15 = 0;
    for ( j = less(0, 5u); j; j = less(v15, 5u) )
    {
      v23 = mul(v14, 5);
      idx = add(v23, v15);
      if ( eq(aAbcdefghijklmn[idx], s_i) )
      {
        v12 = v14;
        v13 = v15;
      }
      v15 = inc(v15);
    }
    v14 = inc(v14);
  }
  v10 = *(a1 + i2);
  v18 = 0;
  for ( k = less(0, 5u); k; k = less(v18, 5u) )
  {
    v19 = 0;
    for ( m = less(0, 5u); m; m = less(v19, 5u) )
    {
      v21 = mul(v18, 5);
      v22 = add(v21, v19);
      if ( eq(aAbcdefghijklmn[v22], v10) )
      {
        v16 = v18;
        v17 = v19;
      }
      v19 = inc(v19);
    }
    v18 = inc(v18);
  }
  v6 = mul(v12, 5);
  *(a1 + i1) = aVastbcdefghijk[add(v6, v17)];
  v20 = mul(v16, 5);
  *(a1 + i2) = aCornfieldsabgh[add(v20, v13)];
  return inc(i2);
```

> Sctipt 
```

aAb = 'abcdefghijklmnoprstuvwxyz'
aVas = 'vastbcdefghijklmnopruwxyz'
aCor = 'cornfieldsabghjkmptuvwxyz'
enc = "odt_sjtfnb_jc_c_fiajb_he_ciuh_nkn_atvfjp"

arr = []
s = ""

def brute(result):
    v1 = 0  
    v2 = 0
    for i in range(5):
        for j in range(5):
            if(result == (i * 5) + j):
                v1 = i
                v2 = j
    return v1,v2

def decode(i1):
    while(enc[i1] == "_"):
        arr.append(i1)
        i1 = i1 + 1
    i2 = i1 + 1
    while(enc[i2] == "_"):
        arr.append(i1)
        i2 = i2 + 1
    re1 = aVas.find(enc[i1])
    re2 = aCor.find(enc[i2])
    v12,v17 = brute(re1)
    v16,v13 = brute(re2)
    v23 = (v12 * 5) + v13
    v21 = (v16 * 5) + v17
    print("{}{}".format(aAb[v23],aAb[v21]),end = "")
    i2 = i2 + 1
    return i2

i = 0
v10 = len(enc)
c = 0
while(i < v10):
    i = decode(i)

```
# Flag

`uitctf{the_inside_of_a_field_of_corn_and_dreams}`