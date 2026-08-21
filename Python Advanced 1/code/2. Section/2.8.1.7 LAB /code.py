# define classes representing:

# tires (as a bundle needed by a car to operate); 
# methods available: get_pressure(), pump(); 
# attribute available: size
# engine; methods available: start(), stop(), get_state(); 
# attribute available: fuel type
# vehicle; method available: __init__(VIN, engine, tires); 
# attribute available: VIN

class Tires():
    def __init__(self):
        self.__pressure = 0

    def __pump__(self, amount):
        self.__pressure = amount

    def get_pressure(self):
        return self.__pressure

based on the classes defined above, create the following objects:

    two sets of tires: city tires (size: 15), off-road tires (size: 18)
    two engines: electric engine, petrol engine

instantiate two objects representing cars:

    the first one is a city car, built of an electric engine and city tires
    the second one is an all-terrain car build of a petrol engine and off-road tires
