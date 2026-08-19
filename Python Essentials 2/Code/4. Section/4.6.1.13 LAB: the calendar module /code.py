# 1. Create a class called MyCalendar that extends 
# the Calendar class;
# 2. create the count_weekday_in_year method with the 
# year and weekday parameters. The weekday parameter 
# should be a value between 0-6, where 0 is Monday
# and 6 is Sunday. The method should return the 
# number of days as an integer;
# 3. in your implementation, use the monthdays2calendar 
# method of the Calendar class.

from calendar import Calendar

class MyCalendar(Calendar):

    def count_weekday_in_year(self, year=2000, weekday=0):
        counter = 0
        for month in range(1, 12+1):
            for week in self.monthdays2calendar(year, month):
                for daynumber, weekdaynumber in week:
                    if weekdaynumber == weekday and daynumber != 0:
                        counter += 1

        return counter

mycalendar = MyCalendar()
countedWeekdays = mycalendar.count_weekday_in_year(year=2019, weekday=0)
print(countedWeekdays)
countedWeekdays = mycalendar.count_weekday_in_year(year=2000, weekday=6)
print(countedWeekdays)