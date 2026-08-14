def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    if(month == 2):
        return 29 if is_year_leap(year) else 28
    elif(month <= 7):
        return 30 if month % 2 == 0 else 31
    else:
        return 31 if month % 2 == 0 else 30

def day_of_year(year, month, day):
    if(year < 0 or year > 9999):
        return None
    if(month < 1 or month > 12):
        return None
    if(day < 1 or day > 31):
        return None
    
    dayCounter = 0
    for currentMonth in range(1, month):
        dayCounter += days_in_month(year, currentMonth)
    dayCounter += day
    return dayCounter
    

print(day_of_year(2000, 12, 31))
