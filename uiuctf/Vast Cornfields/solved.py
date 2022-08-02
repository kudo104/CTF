
aAb = 'abcdefghijklmnoprstuvwxyz'
aVas = 'vastbcdefghijklmnopruwxyz'
aCor = 'cornfieldsabghjkmptuvwxyz'
# dec = "the_inside_of_a_field_of_corn_and_dreams"
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


