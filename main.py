import pygame
import sys

import pygame.draw
from componentes.movimientos import *
from componentes.superficies import *

# Inicializar Pygame
pygame.init()

# Crear la ventana
pygame.display.set_caption('ChessPY')

# Bucle principal
seleccionando = False
posicion_inicial = None
posicion_actual = (0,0)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.VIDEORESIZE:
            ancho_n, alto_n = evento.size[0], evento.size[1]
            ventana = pygame.display.set_mode((ancho_n, alto_n), pygame.RESIZABLE)
            actualizar_dimensiones(ancho_n, alto_n)
            RecargarVentana()
                
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
                match tipo_pieza:
                    case 'Rook':
                        Rook(board, posicion_inicial, posicion_actual)
                    case 'Knight':
                        print('Caballero')
                        #knight()
                    case 'Bisharp':
                        print('Alfil')
                        #Bisharp()
                    case 'Queen':
                        print('Reina')
                        #Queen()
                    case 'King':
                        print('King')
                        #King()
                    case 'Paw':
                        print('Peon')
                        #Paw()
                    case _:
                        print('Thats not an Chess Piece my man')   

                posicion_inicial = None
                posicion_actual = (0,0)

    # Limpiar la pantalla
    DibujarElementos()

    RecargarVentana()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)