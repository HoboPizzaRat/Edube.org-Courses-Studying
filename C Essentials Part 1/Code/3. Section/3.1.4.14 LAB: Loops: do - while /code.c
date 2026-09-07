#include <stdio.h>

int main()
{
	/* your code */
	int num = 0;
	scanf("%d", &num);
	
    if(num <= 1){
        num = 1;
    }
	else if(num > 20){
	    num = 20;
	}
	
	for(int i = 1; i <= num; i++){
	    char line[] = "*#";
	    for(int j = 1; j <= i; j++){
	        printf("%s", line);
	    }
	    printf("\n");
	}
	
	return 0;
}