import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]

# only showing the zipped key_names with key_width amount of lspacing
def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()

# showing empty items if there is no items in the dict
def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()

# showing car object with specified keys(key_names) with key_width of lspacing
def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


# modified method that is able to show lists of items 
# but also when there is only one car object
def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


# trying to get only one object from the server
# getting only one object with specified index from the server
try:
    reply = requests.get('http://localhost:3000/cars/2')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')
