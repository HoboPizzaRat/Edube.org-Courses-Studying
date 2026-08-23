# in progress
# 1. Imagine you’ve been given a task to clean up the code of a system 
# developed in Python – the code should be treated as legacy code;
# the system was created by a group of volunteers who worked with 
# no clear “clean coding” rules;
# 2. the system suffers from a problem: we don’t know in which order
# the classes are created, so it causes multiple dependency problems;
# 3. your task is to prepare a metaclass that is responsible for:
#   - equipping all newly instantiated classes with time stamps, persisted 
#     in a class attribute named instantiation_time;
#   - equipping all newly instantiated classes with the get_instantiation_time() 
#     method. The method should return the value of the class attribute 
#     instantiation_time.

# The metaclass should have its own class variable (a list) that 
# contains a list of the names of the classes instantiated by the
# metaclass (tip: append the class name in the __new__ method).

# Your metaclass should be used to create a few distinct legacy classes;
# create objects based on the classes;
# list the class names that are instantiated by your metaclass.
from datetime import datetime
import time

class My_Meta(type):
    classesInstantiated = []

    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.now()
        My_Meta.classesInstantiated.append(obj.__name__)

        return obj

    def get_instantiation_time(obj):
        return obj.instantiation_time

    def get_all_instantiated_classes():
        return My_Meta.classesInstantiated

class Test_Class1(metaclass=My_Meta):
    pass

class Test_Class2(metaclass=My_Meta):
    pass

class1 = Test_Class1()
time.sleep(1)
class2 = Test_Class2()
print()
print(My_Meta.get_instantiation_time(class1))
print(My_Meta.get_instantiation_time(class2))

print(My_Meta.get_all_instantiated_classes())
