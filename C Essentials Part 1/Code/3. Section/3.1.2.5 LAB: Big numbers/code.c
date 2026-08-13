#include <stdio.h>

int main()
{
    unsigned int ip_part1;
    unsigned int ip_part2;
    unsigned int ip_part3;
    unsigned int ip_part4;
    
    scanf("%u", &ip_part1);
    scanf("%u", &ip_part2);
    scanf("%u", &ip_part3);
    scanf("%u", &ip_part4);
    
    if(ip_part1 > 255 || ip_part2 > 255 || ip_part3 > 255 || ip_part4 > 255){
        printf("\nIncorrect IP Address.\n");
        return 0;
    }
    
    printf("\nHuman-readable IP address is: %u.%u.%u.%u\n", ip_part1, ip_part2, ip_part3, ip_part4);
    
    unsigned int ip_32bit = ip_part1 * 256 * 256 * 256;
    ip_32bit += ip_part2 * 256 * 256;
    ip_32bit += ip_part3 * 256;
    ip_32bit += ip_part4;
    
    printf("IP address as a 32-bit number: %u\n", ip_32bit);
    /* your code */
	return 0;
}