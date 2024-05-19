from componentes.tablero import *
def vali(tipo_pieza1):
    global no
    no=False
    try:
        print(tipo_pieza1[0])
        if(tipo_pieza1[0]=='Rook' or tipo_pieza1[0]=='Knight' or tipo_pieza1[0]=='Bisharp' or tipo_pieza1[0]=='Queen' 
                   or tipo_pieza1[0]=='King' or tipo_pieza1[0]=='Paw'):
            no=False
        else:
            no=True
    except TypeError:
        no=True
        

            
def Rook(tablero, posicion_inicial, posicion_final):
    try:
        col_inicial, fila_inicial = posicion_inicial
        col_final, fila_final = posicion_final
        # Verificar si el movimiento es válido para la torre
        print("col ini(",col_inicial,") fila ini (",fila_inicial,") col fi (",col_final,") fila fi (", fila_final)
        
        if (col_inicial == col_final or fila_inicial == fila_final) and (posicion_inicial!=posicion_final) and (no==True):
            # Verificar si no hay piezas en el camino
            if (col_final<8 and col_final>=0)  and (fila_final<8 and fila_final>=0) :
                paso = 1 if fila_final > fila_inicial or col_final > col_inicial else -1
                if col_inicial == col_final:
                    camino_limpio = all(tablero[i][col_inicial] is None for i in range(fila_inicial + paso, fila_final, paso))
                else:
                    camino_limpio = all(tablero[fila_final][j] is None for j in range(col_inicial + paso, col_final, paso))
                
                if camino_limpio:
                    tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                    tablero[fila_inicial][col_inicial] = None
            else:
                print("Movimiento no válido para una torre")
        else:
            print("Movimiento no válido para una torre")
        
    
    except TypeError as e:
        print(f"Error en mover_torre: {e}")
def Bisharp(tablero, posicion_inicial, posicion_final):
    try:
        col_inicial, fila_inicial = posicion_inicial
        col_final, fila_final = posicion_final
        con=fila_inicial-col_inicial
        con1=fila_inicial+col_inicial

        # Verificar si el movimiento es válido para la torre
        if (col_inicial != col_final and fila_inicial != fila_final) and (posicion_inicial!=posicion_final)and (no==True):
            # Verificar si no hay piezas en el camino
                if (col_final<8 and col_final>=0)  and (fila_final<8 and fila_final>=0) :
                    for i in range(8):
                        for j in range(8):
                            if((i+j)==con1 or (i-j)==con):
                                if i==fila_final and j==col_final:

                                    tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                                    tablero[fila_inicial][col_inicial] = None
                else:
                    print("Movimiento no válido para una Alfil")
        else:
            print("Movimiento no válido para una Alfil")
        
    
    except TypeError as e:
        print(f"Error en mover_Alfil: {e}")

def mover_caballo(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final

def mover_reina(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
def mover_rey(tablero, posicion_inicial, posicion_final):
    col_inicial, fila_inicial = posicion_inicial
    col_final, fila_final = posicion_final
def Paw(tablero, posicion_inicial, posicion_final,pieza):
    try:
        col_inicial, fila_inicial = posicion_inicial
        col_final, fila_final = posicion_final
        print("col ini(",col_inicial,") fila ini (",fila_inicial,") col fi (",col_final,") fila fi (", fila_final, ") piza : ",pieza)

        if ((col_final-1==col_inicial or col_final+1==col_inicial) and fila_inicial==fila_final-1):
                if (pieza[0]=='Paw' or pieza[0]=='Rook' or pieza[0]=='Bisharp' or pieza[0]=='Horse' or pieza[0]=='Queen'):
                    tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                    tablero[fila_inicial][col_inicial] = None
        
        elif (fila_inicial==fila_final-1 and col_inicial==col_final) or (fila_inicial==1 and fila_inicial==fila_final-2 and col_inicial==col_final):
            if (no):
                tablero[fila_final][col_final] = tablero[fila_inicial][col_inicial]
                tablero[fila_inicial][col_inicial] = None
        else:
            print("Movimiento no válido para un Peon")

    except TypeError as e:
        print(f"Error en mover_Peon: {e}")