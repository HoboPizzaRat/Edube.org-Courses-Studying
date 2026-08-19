# The task:

# Write a program that creates a datetime object 
# for November 4, 2020 , 14:53:00. The object created 
# should call the strftime method with the appropriate 
# format to display the following result:

# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44
from datetime import timedelta
from datetime import date 
from datetime import datetime

startDate = datetime(year=2020, month=11, day=4, hour=14, minute=53, second=0)

def printAndFormatDate(dateobj):
    print(dateobj.strftime("%Y/%m/%d %H:%M:%S"))
    print(dateobj.strftime("%-y/%B/%d %H:%M:%S %p"))
    print(dateobj.strftime("%a, %Y %b %d"))
    print(dateobj.strftime("%A, %Y %B %d"))
    print(f'Weekday: {dateobj.strftime("%w")}')
    print(f'Day of the year: {dateobj.strftime("%j")}')
    print(f'Week number of the year: {dateobj.strftime("%U")}')
printAndFormatDate(startDate)