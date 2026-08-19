# SCENARIO

# create a class representing a mobile phone;
# your class should implement the following methods:

# 1. __init__ expects a number to be passed as an argument; 
# this method stores the number in an instance variable self.number
# 2. turn_on() should return the message 'mobile phone {number} is turned on'. 
# Curly brackets are used to mark the place to insert the object's number variable;
# 3. turn_off() should return the message 'mobile phone is turned off';
# 4. call(number) should return the message 'calling {number}'. 
# Curly brackets are used to mark the place to insert the object's 
# number variable;

# create two objects representing two different mobile phones; 
# assign any random phone numbers to them;
# implement a sequence of method calls on the objects to turn 
# them on, call any number. Print the methods' outcomes;
# turn off both mobiles.

class MobilePhone():

    def __init__(self, phonenumber):
        if(len(str(phonenumber)) not in [10, 11]):
            raise Exception("The given phonenumber for the mobile phone is invalid")
        self.number = phonenumber
        self.isTurnedOn = False

    def turn_on(self):
        self.isTurnedOn = True
        print(f"Mobile phone {self.number} is turned on")

    def turn_off(self):
        self.isTurnedOn = False
        print(f"Mobile phone {self.number} is turned off")

    def call(self, number):
        if self.isTurnedOn == False:
            print(f"Cannot call phone number. The phone is turned off")
            return
        print(f"Calling number {number} from phone with number {self.number}")

    def getOwnNumber(self):
        return self.number


mob1 = MobilePhone(3849243901)
mob2 = MobilePhone(2384923042)

mob1.call(mob2.getOwnNumber())

mob1.turn_on()
mob2.turn_on()

mob1.call(mob2.getOwnNumber())
mob2.call(mob1.getOwnNumber())