#include <stdio.h>
int main()
{
	float studentAYear1 = 4.2;
	float studentAYear2 = 4.5;
	float studentAYear3 = 4.2;
	
	float studentBYear1 = 4.3;
	float studentBYear2 = 4.4;
	float studentBYear3 = 4.7;
	
	float studentCYear1 = 4.3;
	float studentCYear2 = 4.8;
	float studentCYear3 = 4.9;
	/* your code */
	float studentA_avg = (studentAYear1 + studentAYear2 + studentAYear3) / 3;
	float studentB_avg = (studentBYear1 + studentBYear2 + studentBYear3) / 3;
	float studentC_avg = (studentCYear1 + studentCYear2 + studentCYear3) / 3;
	printf("Student name  1stYGrade  2ndYGrade  3rdYGrade  Avg\n");
	printf("StudentA%10.2f%11.2f%11.2f%11.2f\n", studentAYear1, studentAYear2, studentAYear3, studentA_avg);
	printf("StudentB%10.2f%11.2f%11.2f%11.2f\n", studentBYear1, studentBYear2, studentBYear3, studentB_avg);
	printf("StudentC%10.2f%11.2f%11.2f%11.2f\n", studentCYear1, studentCYear2, studentCYear3, studentC_avg);
	return 0;
}