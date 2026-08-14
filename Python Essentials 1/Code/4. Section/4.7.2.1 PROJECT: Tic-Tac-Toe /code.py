def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    rowCounter = 0
    for i in range(1,13+1):
        if(i == 1 or i == 5 or i == 9 or i == 13):
            print("+-------+-------+-------+")
            continue
        elif(i == 3 or i == 7 or i == 11):
            print(f"|   {board[rowCounter][0]}   |   {board[rowCounter][1]}   |   {board[rowCounter][2]}   |")
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
                row = choice // 3
                col = choice % 3
                position = (row, col)
                print(position)
                if position in make_list_of_free_fields():
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
    pass

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    pass
board = [[1,2,3],[4,5,6],[7,8,9]]

display_board(board)
print(make_list_of_free_fields(board))
enter_move(board)