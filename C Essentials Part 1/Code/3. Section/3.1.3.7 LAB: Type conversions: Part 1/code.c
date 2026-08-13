#include <stdio.h>

int main()
{
    float input;
    scanf("%f", &input);
    
    int converted = input;
    
    if(converted >= 1 && converted < 2){
        printf("Very bad");
    }
    else if(converted >= 2 && converted < 3){
        printf("Bad");
    }
    else if(converted >= 3 && converted < 4){
        printf("Neutral");
    }
    else if(converted >= 4 && converted < 5){
        printf("Good");
    }
    else if(converted >= 5 && converted < 6){
        printf("Very good");
    }
}