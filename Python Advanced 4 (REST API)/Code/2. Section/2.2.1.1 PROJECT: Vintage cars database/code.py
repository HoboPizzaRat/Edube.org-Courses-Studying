import requests
import json
import sqlite3

connection = sqlite3.connect("cars.db")
cursor = connection.cursor()

def initialize_database():
    print("Initializing database...")
    result = cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' 
        AND
        name='cars';
        """)
    if result.fetchone():
        print("Table cars already exists.")
        return True
    
    result = cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER,
            brand TEXT,
            model TEXT,
            production_year INTEGER
        )
        """)
    connection.commit()

def check_server(cid=None):
# returns True or False;
# when invoked without arguments simply checks if server responds;
# invoked with car ID checks if the ID is present in the database;
    return True

# prints user menu - nothing else happens here;
def print_menu():
    print("1. List Cars")
    print("2. Add new Car")
    print("3. Delete Car")
    print("4. Update Car")
    print("0. Exit")

def read_user_choice():
# reads user choice and checks if it's valid;
# returns '0', '1', '2', '3' or '4' 
    while(True):
        try:
            choice = input("Enter your choice (0-4): ")
            if choice in ["0", "1", "2", "3", "4"]:
                return choice
        except Exception as e:
            print("Invalid choice!")


def print_header():
# prints elegant cars table header;
    print(f"{"ID".ljust(20)}{"BRAND".ljust(20)}{"MODEL".ljust(20)}{"PRODUCTION_YEAR".ljust(20)}")
    print("-" * 80)

def print_car(car):
# prints one car's data in a way that fits the header;
    print(f"{str(car[0]).ljust(20)}{car[1].ljust(20)}{car[2].ljust(20)}{str(car[3]).ljust(20)}")


def list_cars():
# gets all cars' data from server and prints it;
# if the database is empty prints diagnostic message instead;
    cursor.execute("SELECT * FROM cars")
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print("THE DATABASE IS EMPTY")
    else:
        print_header()
        for row in rows:
            print_car(row)

def name_is_valid(name):
# checks if name (brand or model) is valid;
# valid name is non-empty string containing
# digits, letters and spaces;
# returns True or False;
    isEmpty = len(name.strip()) == 0
    isValid = name.replace(" ", "").isalnum()
    return not isEmpty and isValid

def enter_id():
# allows user to enter car's ID and checks if it's valid;
# valid ID consists of digits only;
# returns int or None (if user enters an empty line);
    while(True):
        try:
            id = int(input("Enter id"))
            return id  
        except Exception as e:
            print("Id must be an integer")
        
def check_id_in_database(id):
    result = cursor.execute("""
        SELECT id FROM cars
        WHERE id=?
        """, (id,))
    if result.fetchone():
        return True
    return False

def enter_production_year():
# allows user to enter car's production year and checks if it's valid;
# valid production year is an int from range 1900..2000;
# returns int or None  (if user enters an empty line);
    while(True):
        try:
            year = int(input("Enter production year: "))
            if year >= 1900 or year <= 2026:
                return year
            else:
                print("Production year must be valid!")
        except Exception as e:
            print("Id must be an integer")

def enter_name():
# allows user to enter car's name (brand or model) and checks if it's valid;
# uses name_is_valid() to check the entered name;
# returns string or None  (if user enters an empty line);
# argument describes which of two names is entered currently ('brand' or 'model');
    while(True):
        name = input("Give cars name (brand or model): ")
        if name_is_valid(name):
            return name
        else:
            print("Name should not be empty or contain special characters!")

def enter_convertible():
# allows user to enter Yes/No answer determining if the car is convertible;
# returns True, False or None  (if user enters an empty line);
    pass

def delete_car():
# asks user for car's ID and tries to delete it from database;
    while(True):
        print("give id to delete: ")
        id = enter_id()
        if check_id_in_database(id):
            cursor.execute("""
                DELETE FROM cars
                WHERE id = ?;
            """,(id,))
            connection.commit()
            return
        else:
            print("Given id was not found!")
            return

def input_car_data(with_id):
# lets user enter car data;
# argument determines if the car's ID is entered (True) or not (False);
# returns None if user cancels the operation or a dictionary of the following structure:
# {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    car_data = {}
    if with_id:
        car_data["id"] = int(enter_id())
        car_data["brand"] = enter_name()
        car_data["model"] = enter_name()
        car_data["production_year"] = enter_production_year()
    else:
        car_data["brand"] = enter_name()
        car_data["model"] = enter_name()
        car_data["production_year"] = enter_production_year()

    return car_data


def add_car():
# invokes input_car_data(True) to gather car's info and adds it to the database;
    car_data = input_car_data(with_id=True)
    if not check_id_in_database(car_data["id"]):
        cursor.execute("""
            INSERT INTO cars (id, brand, model, production_year)
            VALUES(?, ?, ?, ?);
            """, (car_data["id"], car_data["brand"], car_data["model"], car_data["production_year"],))
        connection.commit()
        return True
    else:
        print("This id is already in the database!")
        return False

def update_car():
# invokes enter_id() to get car's ID if the ID is present in the database;
# invokes input_car_data(False) to gather new car's info and updates the database;
    update_id = None
    while(True):
        update_id = enter_id()
        if check_id_in_database(update_id):
            car_data = input_car_data(with_id=False)
            cursor.execute("""
                UPDATE cars 
                SET
                id = ?, 
                brand = ?, 
                model = ?, 
                production_year = ?
                WHERE ID = ?
                """, (update_id, car_data["brand"], car_data["model"], car_data["production_year"], update_id,))
            connection.commit()
            return
        else:
            print("You must give an existing id!")


if __name__ == "__main__":
    initialize_database()
    while True:
        if not check_server():
            print("Server is not responding - quitting!")
            exit(1)
        print_menu()
        choice = read_user_choice()
        if choice == '0':
            print("Bye!")
            exit(0)
        elif choice == '1':
            list_cars()
        elif choice == '2':
            add_car()
        elif choice == '3':
            delete_car()
        elif choice == '4':
            update_car()