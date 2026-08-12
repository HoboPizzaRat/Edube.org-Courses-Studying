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
	int daysInFirstHalf = January + February + March + April + May + June;
	int daysInSecondHalf = July + August + September + October + November + December;
	printf("Days in the first half of the current year: %d\n", daysInFirstHalf);
	printf("Days in the second half of the current year: %d\n", daysInSecondHalf);
	printf("Days in the current year: %d\n", daysInFirstHalf + daysInSecondHalf);
	return 0;
}