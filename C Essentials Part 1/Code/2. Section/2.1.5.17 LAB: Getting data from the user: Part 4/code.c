#include <stdio.h>

int main()
{
	/* your code */
	char days[7][20] = {
	    "Monday",
	    "Tuesday",
	    "Wednesday",
	    "Thursday",
	    "Friday",
	    "Saturday",
	    "Sunday"
	};
	int day = 0;
	
	printf("Enter the day of the week (1-7): ");
	scanf("%d", &day);
	
	if(day < 1 || day > 7){
	    printf("Invalid input. Please enter a number between 1 and 7.");
	    return 0;
	}
	printf("The day of the week is: %s", days[day-1]);
	return 0;
}