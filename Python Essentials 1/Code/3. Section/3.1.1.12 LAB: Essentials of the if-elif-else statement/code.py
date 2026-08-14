year = int(input("Enter a year: "))

isLeapYear = False

if year % 400 == 0: 
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
    

if isLeapYear:
    print("Leap year")
else:
    print("Common Year")
#
# Write your code here.
#	
