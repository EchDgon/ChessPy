from componentes.tablero import board

def vali(pieza,tipo_pieza1):
    global no
    no = False
    if pieza=='Rook1' or pieza=='Bisharp1' or pieza=='Knight1' or pieza=='Paw1' or pieza=='Queen1' :
        valor='1'
    else:
        valor='2'
    try:
        if tipo_pieza1[0] in ['Rook'+valor, 'Knight'+valor, 'Bisharp'+valor, 'Queen'+valor, 'King1', 'King2', 'Paw'+valor]:
            no = False
        else:
            no = True
    except TypeError:
        no = True

def Rook(tablero, posicion_inicial, posicion_final,pieza,pieza1):
    global no
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    
    vali(pieza,pieza1)
    if (col_inicial == col_final or fila_inicial == fila_final) and no==True:
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
            no=True
        else:
            print("Movimiento no valido para una torre")
            no=False
    else:
        print("Movimiento no valido para una torre")
        no=False
    return no

def Bisharp(tablero, posicion_inicial, posicion_final,pieza,pieza1):
    global no
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    vali(pieza,pieza1)
    if abs(col_inicial - col_final) == abs(fila_inicial - fila_final) and no==True:
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
            no=True
        else:
            print("Movimiento no valido para un alfil")
            no=False
    else:
        print("Movimiento no valido para un alfil")
        no=False
    return no

def Knight(tablero, posicion_inicial, posicion_final,pieza,pieza1):
    global no
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    vali(pieza,pieza1)
    movimientos_validos = [
        (col_inicial + 1, fila_inicial + 2), (col_inicial - 1, fila_inicial + 2),
        (col_inicial + 1, fila_inicial - 2), (col_inicial - 1, fila_inicial - 2),
        (col_inicial + 2, fila_inicial + 1), (col_inicial - 2, fila_inicial + 1),
        (col_inicial + 2, fila_inicial - 1), (col_inicial - 2, fila_inicial - 1)
    ]
    if (col_final, fila_final) in movimientos_validos and no==True:
        tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
        tablero[fila_inicial][col_inicial] = None
        no=True
    else:
        print("Movimiento no valido para un caballo")
        no=False
    return no

def Queen(tablero, posicion_inicial, posicion_final,pieza,pieza1):
    global no
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    if abs(col_inicial - col_final) == abs(fila_inicial - fila_final):
        Bisharp(tablero, posicion_inicial, posicion_final,pieza,pieza1)
    elif col_inicial == col_final or fila_inicial == fila_final:
        Rook(tablero, posicion_inicial, posicion_final,pieza,pieza1)
    else:
        print("Movimiento no valido para una reina")
        no=False

def King(tablero, posicion_inicial, posicion_final,pieza,pieza1):
    global no
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    vali(pieza,pieza1)
    if max(abs(col_inicial - col_final), abs(fila_inicial - fila_final)) == 1 and no==True:
        tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
        tablero[fila_inicial][col_inicial] = None
        no=True
    else:
        print("Movimiento no valido para un rey")
        no=False
    return no

def Paw(tablero, posicion_inicial, posicion_final,pieza, tipo_pieza1,con):
    global no
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
    vali(pieza,tipo_pieza1) 
    if(con==2):
        ini=-1
        sal=-2
        punto=6
    if con==1:
        ini=1
        sal=2
        punto=1
    if col_inicial == col_final and no==True:
       
        if fila_final == fila_inicial + ini:
            if tablero[fila_final][col_final] is None :
                tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                tablero[fila_inicial][col_inicial] = None
                no=True
            else:
                print("Movimiento no valido para un peon1")
                no=False
        elif fila_final == fila_inicial +sal and fila_inicial == punto:
            if tablero[fila_final][col_final] is None and tablero[fila_inicial + ini][col_inicial] is None:
                tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                tablero[fila_inicial][col_inicial] = None
                no=True
            else:
                print("Movimiento no valido para un peon")
                no=False
    elif abs(col_inicial - col_final) == 1 and fila_final == fila_inicial + ini and no==True:
        if (tablero[fila_final][col_final] is not None):

            if (col_final+1==col_inicial or col_final-1==col_inicial):
                tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                tablero[fila_inicial][col_inicial] = None
                no=True
        else:
            print("Movimiento no valido para un peon3")
            no=False
    else:
        print("Movimiento no valido para un peon")
        no=False
    return no