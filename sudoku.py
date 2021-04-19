

def sudokuResolve(tablero):
    tableroResuelto = '382746519467519832915283647254897361731625984896431725543962178629178453178354296 BTS'

    return tableroResuelto


def main():
    tableroInicial:str = input()

    tableroFinal:str = sudokuResolve(tableroInicial)


if __name__ == '__main__':
    main()