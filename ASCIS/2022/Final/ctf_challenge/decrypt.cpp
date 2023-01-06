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

