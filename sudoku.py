

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
    tableroResuelto = '148697523372548961956321478567983214419276385823154796691432857735819642284765139 BTS'
    return tableroResuelto


def main():
    grid = []
    #tableroInicial:str = input()
    tableroInicial:str = '000000000302540000050301070000000004409006005023054790000000050700810000080060009'
    if len(tableroInicial) == 81:
        grid = fillTablero(tableroInicial)
        tableroFinal:str = sudokuResolve(tableroInicial)
        print(grid)
    
    else:
        print("Tablero Sudoku Incompleto")


if __name__ == '__main__':
    main()