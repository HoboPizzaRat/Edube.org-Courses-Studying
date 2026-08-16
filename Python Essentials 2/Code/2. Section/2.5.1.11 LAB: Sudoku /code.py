def checkSudoku(sudoku):
    def checkBoxes(sudoku):
        # create box
        for area in range(9):
            box = ""
            for i in  range(0, 3):

                for j in range(0, 3):
                    row_base = i + (area//3)*3
                    col_base = j + (area % 3)*3
                    print(row_base, col_base)
                    box += sudoku[row_base][col_base]
            
            for num in "123456789":
                if num in box:
                    continue
                else:
                    return False
        return True

    def checkRows(sudoku):
        for i in range(9):
            for num in "123456789":
                if num in sudoku[i]:
                    continue
                else:
                    return False
        return True
            
    def checkCols(sudoku):
        for i in range(9):
            col = ""
            for j in range(9):
                col += sudoku[j][i]

            for num in "123456789":
                if num in col:
                    continue
                else:
                    return False
        return True


    areAllVAlid = checkBoxes(sudoku) and checkRows(sudoku) and checkCols(sudoku)

    return areAllVAlid
    


sudoku = [
    "295743861",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "154938672"
]
sudoku2 = [
    "195743862",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "254938671"
]

result = checkSudoku(sudoku)
print(result)

result = checkSudoku(sudoku2)
print(result)
