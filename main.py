import pygame
import sys
from componentes.movimientos import *
from componentes.superficies import *
from componentes.tablero import *

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
jugador= True
no=False
cambiar=False

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cerrar_ventana()
            corriendo = False
        elif evento.type == pygame.KEYUP:
            if cambiar:
                if evento.key==pygame.K_q :
                    if fila_final==7:
                        board[fila_final][col_final] = ('Queen1', dark_queen_image)
                    if fila_final==0:
                        board[fila_final][col_final] = ('Queen2', light_queen_image)
                    cambiar=False
                elif evento.key==pygame.K_r :
                    if fila_final==7:
                        board[fila_final][col_final] = ('Rook1', dark_rook_image)
                    if fila_final==0:
                        board[fila_final][col_final] = ('Rook2', light_rook_image)
                    cambiar=False
                elif evento.key==pygame.K_b :
                    if fila_final==7:
                        board[fila_final][col_final] = ('Bisharp1', dark_bisharp_image)
                    if fila_final==0:
                        board[fila_final][col_final] = ('Bisharp2', light_bisharp_image)
                    cambiar=False
                elif evento.key==pygame.K_k :
                    if fila_final==7:
                        board[fila_final][col_final] = ('Knight1', dark_knight_image)
                    if fila_final==0:
                        board[fila_final][col_final] = ('Knight2', light_knight_image)
                    cambiar=False


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
            if x < dimension_tablero and not menu_activo and not cambiar:
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
                                case 'Rook1':
                                    if jugador==False:
                                        no=Rook(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==False:
                                            jugador=True

                                case 'Rook2':
                                    if jugador==True:
                                        no=Rook(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==True:
                                            jugador=False

                                case 'Knight1':
                                    if jugador==False:
                                        no=Knight(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==False:
                                            jugador=True

                                case 'Knight2':
                                    if jugador==True:
                                        no=Knight(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==True:
                                            jugador=False

                                case 'Bisharp1':
                                    if jugador==False:
                                        no=Bisharp(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==False:
                                            jugador=True

                                case 'Bisharp2':
                                    if jugador==True:
                                        no=Bisharp(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==True:
                                            jugador=False

                                case 'Queen1':
                                    if jugador==False:
                                        no=Queen(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==False:
                                            jugador=True

                                case 'Queen2':
                                    if jugador==True:
                                        no=Queen(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==True:
                                            jugador=False

                                case 'King1':
                                    if jugador==False:
                                        no=King(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==False:
                                            jugador=True

                                case 'King2':
                                    if jugador==True:
                                        no=King(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1)
                                        if no==True and jugador==True:
                                            jugador=False
                                            if fila_final==0:
                                                cambiar=True

                                case 'Paw1':
                                    if jugador==False:
                                        no=Paw(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1,1)
                                        
                                        if no==True and jugador==False:
                                            jugador=True
                                            if fila_final==7:
                                                cambiar=True


                                case 'Paw2':
                                    if jugador==True:
                                        no=Paw(board, posicion_inicial, posicion_actual,tipo_pieza,tipo_pieza1,2)
                                        
                                        if no==True and jugador==True:
                                            jugador=False
                                            if fila_final==0:
                                                cambiar=True
                                        
                posicion_inicial = None
                posicion_actual = (0, 0)

    # Limpiar la pantalla
    DibujarElementos()
    RecargarVentana(mi_ventana, menu_activo)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)