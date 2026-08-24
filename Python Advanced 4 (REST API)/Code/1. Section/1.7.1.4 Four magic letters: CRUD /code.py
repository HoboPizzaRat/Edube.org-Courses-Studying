import requests

# making kays and key widths for the keys
key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


# method of showing key_names of the given data
def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


# showing data of each specific extracted json dictionary item
def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()

# the main method of extracting data from json
def show(json):
    show_head()
    for car in json:
        show_car(car)


# retrieving data from cars api
try:
    reply = requests.get('http://localhost:3000/cars')
# if there is error on request of any kind raise error
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print('Server error')
