# 1. introduce the Delicacy class to represent a generic delicacy. 
# The objects of this class will replace the old school dictionaries. 
# Suggested attribute names: name, price, weight;
# 2. your class should implement the __str__() method to represent
# each object state;
# 3 experiment with the copy.copy() and deepcopy.copy() methods 
# to see the difference in how each method copies objects .
import copy

class Delicacy():
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        output = f"DELICACY ({id(self)})\n"
        output += f"name: {self.name}\n"
        output += f"price: {self.price}\n"
        output += f"weight: {self.weight}"
        return output

def comparing_two_objects(obj1, obj2):
    print("-----------------------------------")
    print("Comparing two objects")
    print("")
    print(obj1)
    print("")
    print("vs")
    print("")
    print(obj2)
    print("-----------------------------------")

delicacy1 = Delicacy("cake", 200, 0.750)
delicacy2 = Delicacy("Holy Moly", 69, 0.01)
comparing_two_objects(delicacy1, delicacy2)

print("making shallow copy of delicacy1")
delicacy1_shallow = copy.copy(delicacy1)
print("changing name on delicary1_shallow")
delicacy1_shallow.name = "Kekkonen"
comparing_two_objects(delicacy1, delicacy1_shallow)

print("making shallow copy of delicacy1")
delicacy1_deep = copy.deepcopy(delicacy1)
print("changing name on delicary1_copy")
delicacy1_deep.name = "Kakka"
comparing_two_objects(delicacy1, delicacy1_deep)
