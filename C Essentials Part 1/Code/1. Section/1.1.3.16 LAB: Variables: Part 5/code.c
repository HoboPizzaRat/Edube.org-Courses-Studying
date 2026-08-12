#include <stdio.h>

int main()
{
	int January  		= 31;
	int February        = 29;
	int March 			= 31;
	int April 			= 30;
	int May 			= 31;
	int June 			= 30;
	int July 			= 31;
	int August 			= 31;
	int September 		= 30;
	int October 		= 31;
	int November 		= 30;
	int December 		= 31;
	
	int Q1 = January + February + March;
	int Q2 = April + May + June;
	int Q3 = July + August + September;
	int Q4 = October + November + December;
	
	printf("Days in Q1 of the current year: %d\n", Q1);
    printf("Days in Q2 of the current year: %d\n", Q2);
    printf("Days in Q3 of the current year: %d\n", Q3);
    printf("Days in Q4 of the current year: %d\n", Q4);
	
	return 0;
}