# include <stdio.h> 
# include <windows.h>

int main(){
	char f[33] = "GDUCTF{3asy_r3v3rs3_r0t_&_9as3.}";
	char r[33] = "G3qaMUIuMT1cot==DGRlZ0NwAPSOp3R=";
	
	for(int i = 0; i < 32;i++)
	{
		printf("0x, ",r[i] ^ f[i]);
	}
	return 0;
}
