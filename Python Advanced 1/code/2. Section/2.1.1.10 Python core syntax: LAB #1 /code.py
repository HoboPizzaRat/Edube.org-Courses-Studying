
# Create a class representing a time interval;

# 0. the class should implement its own method for addition, subtraction on time interval class objects;
# 1. the class should implement its own method for multiplication of time 
#    interval class objects by an integer-type value;
# 2. the __init__ method should be based on keywords to allow accurate and 
#    convenient object initialization, but limit it to hours, minutes, and seconds parameters;
# 3. the __str__ method should return an HH:MM:SS string, where HH represents hours, 
#    MM represents minutes and SS represents the seconds attributes of the time interval object;
# 4. check the argument type, and in case of a mismatch, raise a TypeError exception.
class TimeException(Exception):
    def __init__(self, errormsg, errorcode):
        self.message = errormsg
        self.errorcode = errorcode
        super().__init__(errormsg)

class TimeInterval():
    def __init__(self, hours=0, minutes=0, seconds=0):

        if (type(hours) is not int) or (type(minutes) is not int) or (type(seconds) is not int):
            raise TypeError
        
        self.hoursException = TimeException("Hours over range(0-99)", 200)
        self.minutesException= TimeException("Minutes over range(0-59)", 300)
        self.secondsException = TimeException("Seconds over range(0-59)", 400)

        if hours < 0 or hours > 99:
            raise self.hoursException
        if minutes < 0 or minutes > 59:
            raise self.minutesException
        if seconds < 0 or seconds > 59:
            raise self.secondsException
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, timeinterval):
        newSeconds = 0
        newMinutes = 0
        newHours = 0
        addedHours = 0
        addedMinutes = 0

        addedSeconds = self.seconds + timeinterval.seconds
        newSeconds = addedSeconds % 60

        if addedSeconds > 59:
            newMinutes += 1

        addedMinutes = self.minutes + timeinterval.minutes + newMinutes 
        newMinutes = addedMinutes % 60

        if addedMinutes > 59:
            addedHours += 1

        newHours = self.hours + timeinterval.hours  + addedHours

        #print(self.hours)
        #print(timeinterval.hours)
        #print(newHours)
        newTime = None
        try:
            newTime = TimeInterval(hours=newHours, minutes=newMinutes, seconds=newSeconds)
        except TimeException:
            print("The time overflows over the limits!")
            newTime = TimeInterval(0, 0, 0)
        return newTime

    def __sub__(self, timeinterval):
        newSeconds = 0
        newMinutes = 0
        newHours = 0

        def checkIsTimeUnder0():
            if newHours < 0 or newMinutes < 0 or newSeconds < 0:
                raise TimeException("The hour difference is less than 00:00:00")

        newHours = self.hours - timeinterval.hours
        checkIsTimeUnder0()

        minuteDifference = self.minutes - timeinterval.minutes
        if minuteDifference < 0:
            newHours -= 1
            newMinutes += (60 + minuteDifference)%60
        else:
            newMinutes = minuteDifference
        checkIsTimeUnder0()

        secondDifference = self.seconds - timeinterval.seconds
        if secondDifference < 0:
            newMinutes -= 1
            newSeconds = (60 + secondDifference)%60
        else:
            newSeconds = secondDifference
        checkIsTimeUnder0()

        print(self.hours)
        print(timeinterval.hours)
        print(newHours)
        newTime = None
        try:
            newTime = TimeInterval(hours=newHours, minutes=newMinutes, seconds=newSeconds)
        except TimeException:
            print("The time overflows over the limits!")
            newTime = TimeInterval(0, 0, 0)
        return newTime
    
    def __str__(self):
        hoursStr = str(self.hours).rjust(2, "0")
        minutesStr = str(self.minutes).rjust(2, "0")
        secondsStr = str(self.seconds).rjust(2, "0")
        return f"{hoursStr}:{minutesStr}:{secondsStr}"


timeinterval1 = TimeInterval(hours=20, minutes=3, seconds=40)
timeinterval2 = TimeInterval(hours=19, minutes=5, seconds=40)
timeintervalsum = timeinterval1 + timeinterval2
print(timeintervalsum)
timeminus = timeinterval1 - timeinterval2
print(timeminus)