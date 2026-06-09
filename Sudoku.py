def mostrar_tablero(tablero):

    for fila in range(9):

        if fila % 3 == 0 and fila != 0:
            print("-" * 21)

        for columna in range(9):

            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")

            valor = tablero[fila][columna]

            if valor == 0:
                print(".", end=" ")
            else:
                print(valor, end=" ")

        print()

    print()


def buscar_vacia(tablero):

    for fila in range(9):
        for columna in range(9):

            if tablero[fila][columna] == 0:
                return fila, columna

    return None


def es_posible(tablero, fila, columna, numero):

    # Revisar fila
    for c in range(9):

        if tablero[fila][c] == numero:
            return False

    # Revisar columna
    for f in range(9):

        if tablero[f][columna] == numero:
            return False

    # Revisar cuadrante 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3

    for f in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_columna, inicio_columna + 3):

            if tablero[f][c] == numero:
                return False

    return True


def resolver_sudoku(tablero):

    posicion = buscar_vacia(tablero)

    if posicion is None:
        return True

    fila, columna = posicion

    for numero in range(1, 10):

        if es_posible(tablero, fila, columna, numero):

            tablero[fila][columna] = numero

            if resolver_sudoku(tablero):
                return True

            # Backtracking
            tablero[fila][columna] = 0

    return False


tablero = [
    [0,6,0,1,0,4,0,5,0],
    [0,0,8,3,0,5,6,0,0],
    [2,0,0,0,0,0,0,0,1],
    [8,0,0,4,0,7,0,0,6],
    [0,0,6,0,0,0,3,0,0],
    [7,0,0,9,0,1,0,0,4],
    [5,0,0,0,0,0,0,0,2],
    [0,0,7,2,0,6,9,0,0],
    [0,4,0,5,0,8,0,7,0]
]

print("SUDOKU ORIGINAL\n")
mostrar_tablero(tablero)

if resolver_sudoku(tablero):

    print("SUDOKU RESUELTO\n")
    mostrar_tablero(tablero)

else:
    print("No se encontró solución")