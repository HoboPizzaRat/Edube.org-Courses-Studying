#include <stdio.h>
#include <stdlib.h> 

int main()
{
    int secondsInMinute = 60;
    int minutesInHour = 60;
    int secondsInHour = secondsInMinute * minutesInHour;
    
    int three_hours = secondsInHour * 3;
    int three_minutes = secondsInMinute * 3;
    int five_minutes = secondsInMinute * 5;
    
    printf("There are %d seconds in 3 hours.\n", three_hours);
    printf("There are %d seconds in 3 minutes.\n", three_minutes);
    printf("There are %d seconds in 5 minutes.\n", five_minutes);
}