# An attribute is a capacious term that can refer to 
# two major kinds of class traits:
# - variables that contain information binded to the class instace
# - methods, so called action sequences that manipulate the state of variables,
#.  or affect behaviour that could be applied to the object


class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

drake.quack()
print(duckling.height)
