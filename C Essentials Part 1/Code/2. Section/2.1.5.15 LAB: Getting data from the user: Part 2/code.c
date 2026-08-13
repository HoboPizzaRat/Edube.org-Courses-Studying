#include <stdio.h>

int main()
{
	/* your code */
	float a;
	float b;
	
	scanf("%f", &a);
	scanf("%f", &b);
	
	printf("Value A: %f", a);
	printf("\nValue B: %f", b);
	
	printf("\n%.6f + %.6f = %.6f", a, b, a+b);
	printf("\n%.6f - %.6f = %.6f", a, b, a-b);
	printf("\n%.6f * %.6f = %.6f", a, b, a*b);
	
	return 0;
}