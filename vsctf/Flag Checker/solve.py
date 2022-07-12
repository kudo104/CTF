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

