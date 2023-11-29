from tablero import *

def valMoveRook(board,  origen, destino):
    if origen[0] != destino[0] and origen[1] != destino[1]:
        return False 
    
    delta_x = 0 if origen[0] == destino[0] else 1 if origen[0] < destino[0] else -1
    delta_y = 0 if origen[1] == destino[1] else 1 if origen[1] < destino[1] else -1
    
    x, y = origen[0], origen[1]
    while (x, y) != (destino[0], destino[1]):
        x = chr(ord(x) + delta_x)
        y += delta_y
        if board[y - 1][chart.index(x)] != '':
            return False  

    return True


def MoveRook(board, origen, destino):
    if valMoveRook(board, origen, destino):
        origen_x, origen_y = chart.index(origen[0]), origen[1] - 1
        destino_x, destino_y = chart.index(destino[0]), destino[1] - 1

        board[destino_y][destino_x] = board[origen_y][origen_x]
        board[origen_y][origen_x] = ''
        return True
    else: 
        return False