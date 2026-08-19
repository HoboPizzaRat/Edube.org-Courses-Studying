# SCENARIO

# Write a code that creates objects representing 
# apples as long as both limitations are met. When 
# any limitation is exceeded, than the packaging process is stopped, 
# and your application should print the number of apple class objects 
# created, and the total weight.

# Your application should keep track of two parameters:
# - the number of apples processed, stored as a class variable;
# - the total weight of the apples processed; stored as a class variable.
#   Assume that each apple's weight is random, and can vary 
#   between 0.2 and 0.5 of an imaginary weight unit;
import random

class Apple():
    weight_min = 0.2
    weight_max = 0.5

    def __init__(self):
        self.__weight = random.uniform(Apple.weight_min, Apple.weight_max)

    def get_weight(self):
        return self.__weight
    
class ApplePacker():


    def __init__(self, packerMaximumWeight, packerWantedUnits):
        self.packedApples = []
        self.packedWeight = 0
        self.packedUnits = 0
        self.packerMaximumWeight = packerMaximumWeight
        self.packerWantedUnits = packerWantedUnits

    def estimateWeight(self, n):
        return n * ((Apple.weight_min + Apple.weight_max)/2)
    
    def estimateMinCountForWeight(self, weight):
        return int(weight/(Apple.weight_max))

    def addApple(self):
        apple = Apple()
        self.packedApples.append(apple)
        self.packedWeight += apple.get_weight()
        self.packedUnits += 1

    def remoceApple(self):
        apple = self.packedApples.pop()
        self.packedWeight -= apple.get_weight()
        self.packedUnits -= 1

    def hasTruckGottenOverWeight(self):
        return self.packerMaximumWeight < self.packedWeight

    def hasTruckGottenFull(self):
        if self.packerMaximumWeight - self.packedWeight <= Apple.weight_max:
            return True
        else:
            return False

    def hasEnoughWantedUnits(self):
        return self.packedUnits >= self.packerWantedUnits

    def hasQuotaReached(self):
        isEnoughWantedUnits = self.hasEnoughWantedUnits()
        isTruckGottenFull = self.hasTruckGottenFull()
        if isTruckGottenFull:
            print("TRUCK IS FULL, CANNOT ADD MORE APPLES!")
        return isEnoughWantedUnits or isTruckGottenFull

    def remainingApplesForQuota(self):
        howMuchRemaining = self.packerWantedUnits - self.packedUnits
        return 0 if howMuchRemaining < 0 else howMuchRemaining
        
    def packNApples(self, n):
        availableWeight = self.packerMaximumWeight - self.packedWeight
        addedApples = 0
        if n <= self.estimateMinCountForWeight(availableWeight):
            for a in range(n):
                self.addApple()
                addedApples += 1
            return (self.hasEnoughWantedUnits(), addedApples, self.remainingApplesForQuota())
        else:
            while not self.hasQuotaReached():
                self.addApple()
                addedApples += 1
            return (self.hasEnoughWantedUnits(), addedApples, self.remainingApplesForQuota())
    
    def printPackerState(self):
        print("------------------------------------")
        print("PACKER STATUS")
        print(f"apples: {self.packedUnits}")
        print(f"weight: {self.packedWeight}")
        print(f"MAX WEIGHT: {self.packerMaximumWeight}")
        print(f"WANTED APPLES: {self.packerWantedUnits}")
        print(f"QUOTA REACHED: {self.hasEnoughWantedUnits()}")



applepacker = ApplePacker(packerWantedUnits=100, packerMaximumWeight=200)
while(True):
    appleResults = applepacker.packNApples(99)
    applepacker.printPackerState()
    if appleResults[-1] == 0:
        break
