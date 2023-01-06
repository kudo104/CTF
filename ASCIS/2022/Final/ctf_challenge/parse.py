f = open("code.txt","r")


s = ""
for line in f:
    if(line.find("nop") > 0):
        continue
    else:
        s += line
print(s)
f = open("code2.txt","w")
f.write(s)
f.close()
