#include <stdio.h>

int main()
{
    int months[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    int day_of_month;
    int month;
    
    printf("\n");
    scanf("%d", &day_of_month);
    scanf("%d", &month);
    
    int counted_days = 0;
    for(int i = 0; i < month - 1; i++){
        counted_days += months[i];
    }
    counted_days += day_of_month;
    
    printf("\nThe day of the year: %d\n", counted_days);
    
	return 0;
}