from tablero import *

def mover_torre(tablero, posicion_inicial, posicion_final):
    try:
        col_inicial, fila_inicial = posicion_inicial
        col_final, fila_final = posicion_final

        # Verificar si el movimiento es válido para la torre
        if col_inicial == col_final or fila_inicial == fila_final:
            # Verificar si no hay piezas en el camino
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
    
    except Exception as e:
        print(f"Error en mover_torre: {e}")