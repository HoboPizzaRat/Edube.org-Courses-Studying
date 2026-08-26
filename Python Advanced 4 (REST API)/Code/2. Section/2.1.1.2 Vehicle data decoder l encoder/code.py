import json


# defines a class named Vehicle, whose objects can carry 
# the vehicle data shown above (the structure of the class 
# should be deducted from the above dialog — call it 
# "reverse engineering" if you want)
class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass

    def __str__(self):
        output = "VEHICLE OBJECT:\n"
        output += f"Registration Number: {self.registration_number}\n"
        output += f"Year of production: {self.year_of_production}\n"
        output += f"Passenger: {self.passenger}\n"
        output += f"Mass: {self.mass}\n"
        return output

# defines a class able to encode the Vehicle object into an 
# equivalent JSON string;
class VehicleEncoder:
    def encode(v):
        if isinstance(v, Vehicle):
            return json.dumps(v.__dict__)
        else:
            raise TypeError(v.__class__.__name__ + "is not JSON serializable")
        

# defines a class able to decode the JSON string into the newly 
# created Vehicle object.
class VehicleDecoder:
    def decode(json_str):
        v = json.loads(json_str)
        registration_number = v["registration_number"]
        year_of_production = int(v["year_of_production"])
        passenger = bool(v["passenger"])
        mass = float(v["mass"])
        return Vehicle(
            registration_number=registration_number, 
            year_of_production=year_of_production, 
            passenger=passenger, 
            mass=mass)

def createVehicleObject():
    registration_number = input("Give registration number: ")
    year_of_production = int(input("Give year of production: "))
    passenger = True if bool(input("passenger (y/n)")) == "y" else False
    mass = float(input("Give cars mass: "))
    return Vehicle(
        registration_number=registration_number,
        year_of_production=year_of_production,
        passenger=passenger,
        mass=mass)

def printOptions():
    print("0 Exit the program")
    print("1 Produce JSON string from an created vehicle object")
    print("2 Decode a JSON string back to vehicle object")

if __name__ == "__main__":
    while(True):
        printOptions()
        choice = int(input("Choice: "))
        if choice == 0:
            break
        elif choice == 1:
            v = createVehicleObject()
            print(VehicleEncoder.encode(v))
        elif choice == 2:
            json_string = input("Give json string: ")
            v = VehicleDecoder.decode(json_string)
            print(v)