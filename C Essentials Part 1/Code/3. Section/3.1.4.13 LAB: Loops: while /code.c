#include <stdio.h>

int main()
{
	/* your code */
	for(;;){
	    int input1 = 0;
	    int input2 = 0;
	    
	    scanf("%d", &input1);
	    scanf("%d", &input2);
	    
	    int sum = input1 + input2;
	    printf("Sum: %d\n", sum);
	    
	    if(input1 == 99 && input2 == 0){
	        printf("Finish");
	    }
	    if(input1 == 0 || input2 == 0){
	        break;
	    }
	}
}