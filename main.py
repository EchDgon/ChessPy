import pygame
import sys
from tablero import *
from  movimientos import *
# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((width, height))
pygame.display.set_caption('Movimiento de las Piezas')

# Bucle principal
seleccionando = False
posicion_inicial = None
posicion_actual = (0,0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            col_seleccionada = x // box
            fila_seleccionada = y // box
            pieza_seleccionada = board[fila_seleccionada][col_seleccionada] 
            
            if pieza_seleccionada:
                seleccionando = True
                tipo_pieza, imagen_pieza = pieza_seleccionada
                posicion_inicial = (col_seleccionada, fila_seleccionada)
        elif evento.type == pygame.MOUSEMOTION:
            if seleccionando:
                x, y = evento.pos
                col_seleccionada = x // box
                fila_seleccionada = y // box
                posicion_actual = (col_seleccionada, fila_seleccionada)
        elif evento.type == pygame.MOUSEBUTTONUP:
            if seleccionando:
                seleccionando = False
                # Realizar el movimiento en el tablero según el tipo de pieza
                if tipo_pieza == 'rook':
                    mover_torre(board, posicion_inicial, posicion_actual)
                else:
                    print("Tipo de pieza no reconocido")
                posicion_inicial = None
                posicion_actual = (0,0)

    # Limpiar la pantalla
    ventana.fill(white)

    # Dibujar el board
    ChessBoard(ventana, box)

    # Dibujar un contorno alrededor de la pieza seleccionada
    if seleccionando:
        pygame.draw.rect(ventana, (255, 0, 0), (posicion_actual[0] * box, posicion_actual[1] * box, box, box), 3)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)