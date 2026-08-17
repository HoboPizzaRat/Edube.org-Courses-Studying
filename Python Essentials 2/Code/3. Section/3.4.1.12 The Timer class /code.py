class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        if hours > 23 or hours < 0:
            print("Invalid hours! resetting it to 0")
            self.__hours = 0
            pass
        else:
            self.__hours = hours
        if minutes > 59 or minutes < 0:
            print("Invalid minutes! resetting it to 0")
            self.__minutes = 0
            pass
        else:
            self.__minutes = minutes
        if seconds > 59 or seconds < 0:
            print("Invalid seconds! resetting it to 0")
            self.__seconds = 0
            pass
        else:
            self.__seconds = seconds
        

        

    def __str__(self):
        hours_str = str(self.__hours).rjust(2, "0")
        minutes_str = str(self.__minutes).rjust(2, "0")
        seconds_str = str(self.__seconds).rjust(2, "0")
        return f"{hours_str}:{minutes_str}:{seconds_str}"

    def next_second(self):
        self.__seconds = self.__seconds + 1
        if self.__seconds >= 60:
            self.__seconds = 0
            self.__minutes += 1
        if self.__minutes >= 60:
            self.__minutes = 0
            self.__hours += 1
        if self.__hours >= 24:
            self.__hours = self.__hours % 24


    def prev_second(self):
        self.__seconds = self.__seconds - 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
        if self.__minutes < 0:
            self.__minutes = 59
            self.__hours -= 1
        if self.__hours < 0:
            self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
