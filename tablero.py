def inicializar_tablero():
    tablero = [[' ' for _ in range(8)] for _ in range(8)]
    
    # Diccionario con las posiciones iniciales de las piezas
    piezas = {
        'T': [(0, 0), (0, 7)],
        't': [(7, 0), (7, 7)],
        'C': [(0, 1), (0, 6)],
        'c': [(7, 1), (7, 6)],
        'A': [(0, 2), (0, 5)],
        'a': [(7, 2), (7, 5)],
        'R': [(0, 3)],
        'r': [(7, 3)],
        'D': [(0, 4)],
        'd': [(7, 4)],
        'P': [(1, col) for col in range(8)],
        'p': [(6, col) for col in range(8)]
    }
    
    # Colocar las piezas en el tablero
    for pieza, posiciones in piezas.items():
        for posicion in posiciones:
            fila, columna = posicion
            tablero[fila][columna] = pieza
    
    return tablero

# Ejemplo de uso:
tablero_inicial = inicializar_tablero()

# Imprimir el tablero resultante
for fila in tablero_inicial:
    print(' '.join(fila))
