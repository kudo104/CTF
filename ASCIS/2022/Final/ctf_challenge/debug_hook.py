# import idaapi
# import time
# f = open("log.txt","w")

# while(True):
#     idaapi.run_to(0xB81F93)
#     time.sleep(3)
#     if(here() == 0xB81F93):
#         print("oke")
#         break
#     data = []
#     for i in range(0xFE0000,0xFE0005,1):
#         data.append(idc.get_wide_byte(i))
        
#     s = ' '.join([str(elem) for elem in data])
#     s += "\n"
#     f.write(s)
 
# f.close()


import idaapi
import time

f = open("log.txt","a")

idaapi.run_to(0xB81F93)

data = []

for i in range(0x950000,0x950006,1):
    data.append(idc.get_wide_byte(i))
    
s = ' '.join([str(elem) for elem in data])
s += "\n"
f.write(s)
f.close()