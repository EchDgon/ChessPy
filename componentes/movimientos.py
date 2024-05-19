from componentes.tablero import board

def vali(tipo_pieza1):
    global no
    no = False
    try:
        if tipo_pieza1 and tipo_pieza1[0] in ['Rook', 'Knight', 'Bisharp', 'Queen', 'King', 'Paw']:
            no = False
        else:
            no = True
    except TypeError:
        no = True

def Rook(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    if col_inicial == col_final or fila_inicial == fila_final:
        paso = 1 if fila_final > fila_inicial or col_final > col_inicial else -1
        camino_limpio = True
        if col_inicial == col_final:
            for i in range(fila_inicial + paso, fila_final, paso):
                if tablero[i][col_inicial] is not None:
                    camino_limpio = False
                    break
        else:
            for j in range(col_inicial + paso, col_final, paso):
                if tablero[fila_final][j] is not None:
                    camino_limpio = False
                    break
        if camino_limpio:
            tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
            tablero[fila_inicial][col_inicial] = None
        else:
            print("Movimiento no valido para una torre")
    else:
        print("Movimiento no valido para una torre")

def Bisharp(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    if abs(col_inicial - col_final) == abs(fila_inicial - fila_final):
        paso_col = 1 if col_final > col_inicial else -1
        paso_fila = 1 if fila_final > fila_inicial else -1
        camino_limpio = True
        i, j = fila_inicial + paso_fila, col_inicial + paso_col
        while i != fila_final and j != col_final:
            if tablero[i][j] is not None:
                camino_limpio = False
                break
            i += paso_fila
            j += paso_col
        if camino_limpio:
            tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
            tablero[fila_inicial][col_inicial] = None
        else:
            print("Movimiento no valido para un alfil")
    else:
        print("Movimiento no valido para un alfil")

def Knight(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    movimientos_validos = [
        (col_inicial + 1, fila_inicial + 2), (col_inicial - 1, fila_inicial + 2),
        (col_inicial + 1, fila_inicial - 2), (col_inicial - 1, fila_inicial - 2),
        (col_inicial + 2, fila_inicial + 1), (col_inicial - 2, fila_inicial + 1),
        (col_inicial + 2, fila_inicial - 1), (col_inicial - 2, fila_inicial - 1)
    ]
    if (col_final, fila_final) in movimientos_validos:
        tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
        tablero[fila_inicial][col_inicial] = None
    else:
        print("Movimiento no valido para un caballo")

def Queen(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    if abs(col_inicial - col_final) == abs(fila_inicial - fila_final):
        Bisharp(tablero, posicion_inicial, posicion_final)
    elif col_inicial == col_final or fila_inicial == fila_final:
        Rook(tablero, posicion_inicial, posicion_final)
    else:
        print("Movimiento no valido para una reina")

def King(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    if max(abs(col_inicial - col_final), abs(fila_inicial - fila_final)) == 1:
        tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
        tablero[fila_inicial][col_inicial] = None
    else:
        print("Movimiento no valido para un rey")

def Paw(tablero, posicion_inicial, posicion_final, tipo_pieza1):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    if col_inicial == col_final:
        if fila_final == fila_inicial + 1:
            if tablero[fila_final][col_final] is None:
                tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                tablero[fila_inicial][col_inicial] = None
            else:
                print("Movimiento no valido para un peon")
        elif fila_final == fila_inicial + 2 and fila_inicial == 1:
            if tablero[fila_final][col_final] is None and tablero[fila_inicial + 1][col_inicial] is None:
                tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                tablero[fila_inicial][col_inicial] = None
            else:
                print("Movimiento no valido para un peon")
    elif abs(col_inicial - col_final) == 1 and fila_final == fila_inicial + 1:
        if tablero[fila_final][col_final] is not None and tablero[fila_final][col_final][1] != tipo_pieza1[1]:
            tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
            tablero[fila_inicial][col_inicial] = None
        else:
            print("Movimiento no valido para un peon")
    else:
        print("Movimiento no valido para un peon")
