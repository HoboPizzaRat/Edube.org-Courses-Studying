class WeekDayError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"ERROR OCCURED: {self.message}"

class Weeker:
    

    def __init__(self, day):
        self.__days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.__dayIndex = self.__days.index(day)
        if self.__dayIndex == -1:
            self.__dayIndex = 0
            raise WeekDayError

    def __str__(self):
        return self.__days[self.__dayIndex]

    def add_days(self, n):
        self.__dayIndex = (self.__dayIndex + n) % len(self.__days)

    def subtract_days(self, n):
        self.__dayIndex = (self.__dayIndex - n) % len(self.__days)
    


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker("Wed")
    weekday.subtract_days(2)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
