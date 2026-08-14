secret_number = 777

def printMsg():
    print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

def askNumber():
    return int(input("Quess a number: "))

def wrongNumber():
    print("That aint the number!")
    
def rightNumber():
    print("OOOOOOOOOH thats the right number!")
    

printMsg()
num = askNumber()

while(num != secret_number):
    wrongNumber()
    num = askNumber()

rightNumber()