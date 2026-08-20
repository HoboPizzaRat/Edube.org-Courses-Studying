# Create a function decorator that prints a timestamp 
# (in a form like year-month-day hour:minute:seconds, 
# eg. 2019-11-05 08:33:22)

# Create a few ordinary functions that do some simple tasks, 
# like adding or multiplying two numbers.

# Apply your decorator to those functions to ensure that the 
# time of the function executions can be monitored.
import datetime 
import time
def logger(message):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            now = datetime.datetime.now()
            print(f"{message} : {now}")
        return internal_wrapper
    return wrapper
    

@logger("MATH FUNCTION EXECUTED")
def addyshYddysh(num1, num2):
    print(num1 + num2)




addyshYddysh(1, 2)
time.sleep(1)
addyshYddysh(2, 2)
time.sleep(1)
addyshYddysh(4, 2)
time.sleep(1)
addyshYddysh(5, 2)
