#include <stdio.h>
#include <stdbool.h>

int main()
{
	int months[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	int day;
	int month;
	int year;
	
	
	printf("\nEnter day:\n");
	scanf("%d", &day);
	printf("\nEnter month:\n");
	scanf("%d", &month);
	printf("\nEnter year:\n");
	scanf("%d", &year);
	
	
	bool isLeapYear = false;
	if (year % 400 == 0){
		isLeapYear = true;
	}
	else if (year % 100 == 0){
		isLeapYear = false;
	}
	else if (year % 4 == 0){
		isLeapYear = true;
	}
	/* your code */
	
	int dayOfTheYear = 0;
	for(int i = 0; i < month-1; i++){
	    dayOfTheYear += months[i];
	}
	dayOfTheYear += day;
	
	if(month >= 2 && isLeapYear){
        dayOfTheYear--;
    }
	
	printf("\nDay of the year: %d", dayOfTheYear);
    if(isLeapYear){
        printf("\n%d is a leap year.", year);
    }else{
        printf("\n%d is not a leap year.", year);
    }
	return 0;
}