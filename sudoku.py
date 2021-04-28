import itertools


class Sudoku:
    filas:str = "123456789"
    columnas:str = "ABCDEFGHI"
    celdas:list
    posibilidades:dict
    restricciones:list = []
    celdasRelacionadas:dict = {}
    podado:dict = {}

    def __init__(self, tablero):
        self.celdas = list()
        self.posibilidades = dict()
        self.GenerarCoordendas()
        self.GenerarPosibilidades(tablero)
        self.GenerarRestricciones()
        self.GenerarCeldasRelacionadas()
        self.podado = {v: list() if tablero[i] == '0' else [int(tablero[i]) ] for i, v in enumerate(self.celdas)}

    def GenerarCoordendas(self):
        for col in self.columnas:
            for fil in self.filas:
                self.celdas.append(col + fil)

    def GenerarPosibilidades(self, tablero):
        _tablero = list(tablero)
        for i, coordenadas in enumerate(self.celdas):
            if i > 80:
                print("Se Excedio ", i, str(coordenadas))
                return
            if _tablero[i] == "0":
                self.posibilidades[coordenadas] = list(range(1,10))
            else:
                self.posibilidades[coordenadas] = [int(_tablero[i])]

    def GenerarRestricciones(self):
        def reglasRestrictivas():
            restriccionesDeFilas = []
            restriccionesDeColumnas = []
            restriccionesDeCaja = []
            for fil in self.filas:
                restriccionesDeFilas.append([col + fil for col in self.columnas])
            for col in self.columnas:
                restriccionesDeColumnas.append([col + fil for fil in self.filas])
            coordenadaDeCajaFil = list( (self.columnas[i:i+3] for i in range(0, len(self.filas), 3)) )
            coordenadaDeCajaCol = list( (self.filas[i:i+3] for i in range(0, len(self.columnas), 3)) )
            for fil in coordenadaDeCajaFil:
                for col in coordenadaDeCajaCol:
                    actual = []
                    for x in fil:
                        for y in col:
                            actual.append(x+y)
                    restriccionesDeCaja.append(actual)
            return restriccionesDeFilas + restriccionesDeColumnas + restriccionesDeCaja
        
        for restriccion in reglasRestrictivas():
            restriccionesBinarias = []
            for restricciones in itertools.permutations(restriccion, 2):
                restriccionesBinarias.append(restricciones)
            for _restriccion in restriccionesBinarias:
                listaDeRestricciones = list(_restriccion)
                if listaDeRestricciones not in self.restricciones:
                    self.restricciones.append([_restriccion[0], _restriccion[1]])

    def GenerarCeldasRelacionadas(self):
        for celda in self.celdas:
            self.celdasRelacionadas[celda] = []
            for restriccion in self.restricciones:
                if celda == restriccion[0]:
                    self.celdasRelacionadas[celda].append(restriccion[1])

    def estaCompletado(self):
        for _, posibilidades in self.posibilidades.items():
            if len(posibilidades) > 1:
                return False
        return True

    def __str__(self):
        tablero = ""
        for celda in self.celdas:
            valor = str(self.posibilidades[celda])
            if type(self.posibilidades[celda]) == list:
                valor = str(self.posibilidades[celda][0])
            tablero += valor
        return tablero

# Funcion para crear el archivo output.txt con el resultado
def makeFileOutput(tableroFinal):
    return

class AC3:
    def resolver(self, csp: Sudoku, queue=None):
        if queue == None:
            queue = list(csp.restricciones)
        while queue:
            (xi, xj) = queue.pop(0)
            if self.quitarValor(csp, xi, xj):
                if len(csp.posibilidades[xi]) == 0:
                    return False
                for x in csp.celdasRelacionadas[xi]:
                    if x != xi:
                        queue.append((x, xi))
        return True

    def quitarValor(self, csp: Sudoku, ci, cj):
        def esDiferente(i, j): return i != j
        quitar = False
        for valor in csp.posibilidades[ci]:
            if not any([esDiferente(valor, poss) for poss in csp.posibilidades[cj]]):
                csp.posibilidades[ci].remove(valor)
                quitar = True
        return quitar

# Funcion que Resuelve el algoritmo, las pruebas unitarias corren sobre este
def sudokuResolve(tablero):
    if len(tablero) != 81:
        return
    sudoku = Sudoku(tablero)
    ac3 = AC3()
    backtrack = Backtrack()
    if not ac3.resolver(sudoku):
        return
    else:
        if sudoku.estaCompletado():
            return str(sudoku) + " AC3"
        else:
            assignment = {}
            for celda in sudoku.celdas:
                if len(sudoku.posibilidades[celda]) == 1:
                    assignment[celda] = sudoku.posibilidades[celda][0]
            assignment = backtrack.resolver(assignment, sudoku)
            for celda in sudoku.posibilidades:
                sudoku.posibilidades[celda] = assignment[celda] if len(celda) > 1 else sudoku.posibilidades[celda]
            if assignment:
                return str(sudoku) + " BTS"


def main():
    tableroInicial:str = input()
    #tableroInicial:str = '000260701680070090190004500820100040004602900050003028009300074040050036703018000'
    if len(tableroInicial) == 81:
        tableroFinal:str = sudokuResolve(tableroInicial)
        makeFileOutput(tableroFinal)
    
    else:
        print("Tablero Sudoku Incompleto")


if __name__ == '__main__':
    main()