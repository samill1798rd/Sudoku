

def fillTablero(newTablero):
    row: [int] = []
    column: [[int]] = []
    for cell in newTablero:
        row.append(int(cell))
        if len(row) == 9:
            column.append(row)
            row = []
    return column

def solveWithAC3(tablero):
    return

def solveWithBTS(tablero):
    return

def solved(col, row, x):
    return

def makeFileOutput(tableroFinal):
    return



def sudokuResolve(tablero):
    tableroResuelto = '382746519467519832915283647254897361731625984896431725543962178629178453178354296 BTS'
    return tableroResuelto


def main():
    grid = []
    #tableroInicial:str = input()
    tableroInicial:str = '070060200040005003050180040000050706001079002000000010300010807800030000000006000'
    if len(tableroInicial) == 81:
        grid = fillTablero(tableroInicial)
        tableroFinal:str = sudokuResolve(tableroInicial)
        print(grid)
    
    else:
        print("Tablero Sudoku Incompleto")


if __name__ == '__main__':
    main()