import random

def drawCellItem(cell):
    if cell == "X":
        return f"\033[92m{str(cell)}\033[0m"
    elif cell == "O":
        return f"\033[91m{str(cell)}\033[0m"
    else:
        return str(cell)
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    rowCounter = 0
    for i in range(1,13+1):
        if(i == 1 or i == 5 or i == 9 or i == 13):
            print("+-------+-------+-------+")
            continue
        elif(i == 3 or i == 7 or i == 11):
            print(f"|   {drawCellItem(board[rowCounter][0])}   |   {drawCellItem(board[rowCounter][1])}   |   {drawCellItem(board[rowCounter][2])}   |")
            rowCounter += 1
        else:
            print("|       |       |       |")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    choice = None
    while(True):
        try:
            choice = int(input("Give a number between 1-9 as your move:"))
            if(1 <= choice and choice <= 9):
                print("this executes")
                row = (choice-1) // 3
                col = (choice-1) % 3
                position = (row, col)
                print(position)
                if position in make_list_of_free_fields(board):
                    board[row][col] = "O"
                    print(f"Player move({row},{col}) registered successfully!")
                    return board
            else:
                print("Input out of range!")
        except:
            print("The input must be a whole integer between 1-9")
    


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freePlaces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in ["X","O"]:
                freePlaces.append((i, j));
    return freePlaces

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    straightRows = [board[0], board[1], board[2]]
    straightCols = []
    for row in range(3):
        straightline = []
        for col in range(3):
            straightline.append(board[col][row])
        straightCols.append(straightline)
        
    diagonals = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]

    countedlines = [*straightRows, *straightCols, *diagonals]
    

    for line in countedlines:
        containsOnlySigns = True
        for s in line:
            if s != sign:
                containsOnlySigns = False
                continue
        if containsOnlySigns:
            return True

def draw_move(board):
    freePlaces = make_list_of_free_fields(board)

    if len(freePlaces) == 9:
        board[1][1] = "X"
        return board

    (randomx, randomy) = random.choice(freePlaces)
    board[randomx][randomy] = "X"
    return board

    
def checkIsFull(board):
    return len(make_list_of_free_fields(board)) == 0

board = [[1,2,3],[4,5,6],[7,8,9]]
gameIsOn = True
didPlayerWin = False
didPcWin = False

while(gameIsOn):

    
    if checkIsFull(board):
        gameIsOn = False
        break
    
    board = draw_move(board)
    print("AFTER COMPUTER TURN:")
    display_board(board)

    if victory_for(board, "X"):
        didPcWin = True
        gameIsOn = False
        break

    board = enter_move(board)
    print("AFTER PLAYER TURN:")
    display_board(board)

    if victory_for(board, "O"):
        didPlayerWin = True
        gameIsOn = False
        break

if didPlayerWin:
    print("GONGRATULATIONS! THE PLAYER WINS!")
elif didPcWin:
    print("WOW! THE PC's OWN AI IS UNBEATABLE!")