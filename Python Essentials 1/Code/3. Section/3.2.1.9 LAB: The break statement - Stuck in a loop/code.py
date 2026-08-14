
def askInput():
    return input("Give me a string: ")


while(True):
    askedInput = askInput()
    if askedInput == "chupacabra":
        break
    print("No thats not it!")

print("You've successfully left the loop.")