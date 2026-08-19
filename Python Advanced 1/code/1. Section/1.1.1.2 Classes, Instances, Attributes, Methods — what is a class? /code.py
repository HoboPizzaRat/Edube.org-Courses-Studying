# A class expresses an idea; it’s a blueprint or recipe for an instance. 
# it has
# -meaning
# -own instance and information that is separate from other instances
# -idk actions that will be executed when interacting with it
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')
