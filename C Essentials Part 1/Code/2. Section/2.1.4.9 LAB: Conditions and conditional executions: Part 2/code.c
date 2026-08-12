#include <stdio.h>

int main(void) 
{
	int n = -3;
	/* your code */
	int n_abs = 0;
	if(n < 0){
	    n_abs = -n;
	}else{
	    n_abs = n;
	}
	printf("The absolute value of %d is %d\n", n, n_abs);
	printf("The value of n is %d\n", n);
	return 0;
}