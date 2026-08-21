# define classes representing:

# tires (as a bundle needed by a car to operate); 
# methods available: get_pressure(), pump(); 
# attribute available: size
class Tires():
    def __init__(self, size):
        self.__pressure = 0
        self.__size = size

    def pump(self, amount):
        self.__pressure = amount

    def get_pressure(self):
        return self.__pressure

    @property
    def size(self):
        return self.__size

    @size.getter
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        print("cannot set the tires to new size")

    def __str__(self):
        return f"tiresize-{self.__size}"

# engine; methods available: start(), stop(), get_state(); 
# attribute available: fuel type
class Engine():

    def __init__(self, engine_type):
        self.__engine_type = engine_type

    def start(self):
        print("Starting the engine...")
        print("The engine starts roaring...")

    def stop(self):
        print("The engine is stopping for now...")

    def get_state(self):
        print(f"The engine is running on: {self.__engine_type}")
    
    def __str__(self):
            return f"Equipped with enginetype {self.__engine_type}"

# vehicle; method available: __init__(VIN, engine, tires); 
# attribute available: VIN
class Vehicle():

    def __init__(self, VIN, engine, tires):
        self.__vin = VIN
        self.__engine = engine
        self.__tires = tires
        print("--------------------------------------")
        print("Created car with following properties:")
        print(f"VIN: {self.__vin}")
        print(f"Engine: {self.__engine}")
        print(f"Tires: {self.__tires}")
        print("--------------------------------------")

    @property
    def VIN(self):
        return self.__vin

    @VIN.getter
    def VIN(self):
        return self.__vin

    @VIN.setter
    def VIN(self, VIN):
        if not(VIN.isalnum() and len(VIN) == 5):
            print("The given VIN is invalid!")
            return
        self.__vin = VIN

    def turnOn(self):
        print("starting the car")
        self.__engine.start()
        self.__engine.get_state()

    def turnOff(self):
        print("Stopping and shutting down the car")
        self.__engine.stop()
        self.__engine.get_state()

#two sets of tires: city tires (size: 15), off-road tires (size: 18)
cityTires = Tires(15)
offRoadTires = Tires(18)

#two engines: electric engine, petrol engine
electricEngine = Engine("Electric engine")
petrolEngine = Engine("Petrol Engine")

#instantiate two objects representing cars:
#the first one is a city car, built of an electric engine and city tires
cityCar = Vehicle("55555", electricEngine, cityTires)

#the second one is an all-terrain car build of a petrol engine and off-road tires
offRoadCar = Vehicle("66666", petrolEngine, offRoadTires)

cars = [cityCar, offRoadCar]
for car in cars:
    car.turnOn()
    car.turnOff()