import pygame
import sys
from componentes.movimientos import *
from componentes.superficies import *

# Inicializar Pygame
pygame.init()

# Crear la ventana
icono = pygame.image.load("assets/Torre-N.png")
pygame.display.set_icon(icono)
pygame.display.set_caption('ChessPY')

ancho = 900
alto = 600
mi_ventana = crear_ventana(ancho, alto)

# Dimensiones iniciales
dimension_tablero = min(ancho, alto)
box = dimension_tablero // 8
dimension_menu = (ancho // 25, alto // 20)
pos_menu = (ancho - dimension_menu[0] - 5, 5)
dimension_desplegable = (alto // 4, alto // 4)
pos_desplegable = (ancho - dimension_desplegable[0] - 5, pos_menu[1] + dimension_menu[1])

# Bucle principal
seleccionando = False
posicion_inicial = None
posicion_actual = (0, 0)
menu_activo = False
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cerrar_ventana()
            corriendo = False

        elif evento.type == pygame.VIDEORESIZE:
            ancho_n, alto_n = evento.size[0], evento.size[1]
            ventana = pygame.display.set_mode((ancho_n, alto_n), pygame.RESIZABLE)
            actualizar_dimensiones(ancho_n, alto_n)
            dimension_tablero = min(ancho_n, alto_n)
            box = dimension_tablero // 8
            dimension_menu = (ancho_n // 25, alto_n // 20)
            pos_menu = (ancho_n - dimension_menu[0] - 5, 5)
            dimension_desplegable = (alto_n // 4, alto_n // 4)
            pos_desplegable = (ancho_n - dimension_desplegable[0] - 5, pos_menu[1] + dimension_menu[1])

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if x < dimension_tablero and not menu_activo:
                col_seleccionada = x // box
                fila_seleccionada = y // box
                if 0 <= col_seleccionada < 8 and 0 <= fila_seleccionada < 8:
                    pieza_seleccionada = board[fila_seleccionada][col_seleccionada]
                    if pieza_seleccionada:
                        seleccionando = True
                        tipo_pieza, imagen_pieza = pieza_seleccionada
                        posicion_inicial = (col_seleccionada, fila_seleccionada)
                        posicion_actual = (col_seleccionada, fila_seleccionada)

            elif pos_menu[0] <= x <= pos_menu[0] + dimension_menu[0] and pos_menu[1] <= y <= pos_menu[1] + dimension_menu[1]:
                menu_activo = not menu_activo

            elif pos_desplegable[0] <= x <= pos_desplegable[0] + dimension_desplegable[0] and pos_desplegable[1] <= y <= pos_desplegable[1] + dimension_desplegable[1] and menu_activo:
                if pos_desplegable[1] <= y <= pos_desplegable[1] + (dimension_desplegable[1] // 3):
                    mi_ventana = reiniciar_ventana(ancho, alto)
                    reiniciar_variables()
                elif (dimension_desplegable[1] // 3) <= y <= (dimension_desplegable[1] // 3) + (2 * dimension_desplegable[1] // 3):
                    print("pausa")
                elif (2 * dimension_desplegable[1] // 3) <= y <= (2 * dimension_desplegable[1] // 3) + dimension_desplegable[1]:
                    cerrar_ventana()
                    corriendo = False

        elif evento.type == pygame.MOUSEMOTION:
            if seleccionando:
                x, y = evento.pos
                col_seleccionada = x // box
                fila_seleccionada = y // box
                if 0 <= col_seleccionada < 8 and 0 <= fila_seleccionada < 8:
                    posicion_actual = (col_seleccionada, fila_seleccionada)

        elif evento.type == pygame.MOUSEBUTTONUP:
            if seleccionando:
                seleccionando = False
                col_final, fila_final = posicion_actual
                if posicion_inicial and posicion_actual and posicion_inicial != posicion_actual:
                    if 0 <= col_final < 8 and 0 <= fila_final < 8:
                        tipo_pieza1 = board[fila_final][col_final]
                        if tipo_pieza1 is None or tipo_pieza1[0] != tipo_pieza[0]:
                            match tipo_pieza:
                                case 'Rook':
                                    Rook(board, posicion_inicial, posicion_actual)
                                case 'Knight':
                                    Knight(board, posicion_inicial, posicion_actual)
                                case 'Bisharp':
                                    Bisharp(board, posicion_inicial, posicion_actual)
                                case 'Queen':
                                    Queen(board, posicion_inicial, posicion_actual)
                                case 'King':
                                    King(board, posicion_inicial, posicion_actual)
                                case 'Paw':
                                    Paw(board, posicion_inicial, posicion_actual, tipo_pieza1)
                posicion_inicial = None
                posicion_actual = (0, 0)

    # Limpiar la pantalla
    DibujarElementos()
    RecargarVentana(mi_ventana, menu_activo)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)
