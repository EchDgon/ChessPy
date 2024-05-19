import pygame
import sys

import pygame.draw
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

# Bucle principal
seleccionando = True
posicion_inicial = None
posicion_actual = (0,0)

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
            dimension_tablero = min(ancho_n , alto_n)
            box = dimension_tablero // 8
            dimension_menu = (ancho_n // 25, alto_n // 20)
            pos_menu= (ancho_n - dimension_menu[0] - 5 , 5)
            dimension_desplegable = (alto_n // 4, alto_n // 4)
            pos_desplegable = (ancho_n - dimension_desplegable[0] - 5, pos_menu[1] + dimension_menu[1])
        
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            if x < dimension_tablero and not menu_activo:
                col_seleccionada = x // box
                fila_seleccionada = y // box
                pieza_seleccionada = board[fila_seleccionada][col_seleccionada]
                if pieza_seleccionada:
                        seleccionando = True
                        tipo_pieza, imagen_pieza = pieza_seleccionada
                        posicion_inicial = (col_seleccionada, fila_seleccionada)

                        match (tipo_pieza):
                            case 'Rook':
                                print("torre")
                            case 'Knight':
                                print("caballo")
                                #knight()
                            case 'Bisharp':
                                print("alfil")
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

            elif (pos_menu[0] <= x <= pos_menu[0] + dimension_menu[0] and 
                  pos_menu[1] <= y <= pos_menu[1] + dimension_menu[1]):
                    
                    menu_activo = not menu_activo 

            elif (pos_desplegable[0] <= x <= pos_desplegable[0] + dimension_desplegable[0] and 
                  pos_desplegable[1] <= y <= pos_desplegable[1] + dimension_desplegable[1] and
                  menu_activo):
                    print("menu")
                    if(pos_desplegable[0] <= x <= pos_desplegable[0] + dimension_desplegable[0] and
                        pos_desplegable[1] <= y <= pos_desplegable[1] + (dimension_desplegable[1] // 3)):
                            mi_ventana = reiniciar_ventana(ancho, alto)
                            reiniciar_variables()
                        
                    elif(pos_desplegable[0] <= x <= pos_desplegable[0] + dimension_desplegable[0] and
                        (dimension_desplegable[1] // 3) <= y <= (dimension_desplegable[1] // 3) + (2 *dimension_desplegable[1] // 3)):
                        print("pausa")
                    elif(pos_desplegable[0] <= x <= pos_desplegable[0] + dimension_desplegable[0] and
                        (2 *dimension_desplegable[1] // 3) <= y <= (2 *dimension_desplegable[1] // 3) + (dimension_desplegable[1])):
                            cerrar_ventana()
        elif evento.type == pygame.MOUSEMOTION:
            if seleccionando:
                x, y = evento.pos
                col_seleccionada = x // box
                fila_seleccionada = y // box
                posicion_actual = (col_seleccionada, fila_seleccionada)
                pieza_seleccionada = board[fila_seleccionada][col_seleccionada]
                tipo_pieza1= pieza_seleccionada
                    
        elif evento.type == pygame.MOUSEBUTTONUP:
            if seleccionando:
                
                seleccionando = False
                    # Realizar el movimiento en el tablero según el tipo de pieza
                
                match tipo_pieza:
                    case 'Rook':
                        vali(tipo_pieza1)
                        Rook(board, posicion_inicial, posicion_actual)
                    case 'Knight':
                        print("caballo")
                            #knight()
                    case 'Bisharp':
                        vali(tipo_pieza1)
                        Bisharp(board, posicion_inicial, posicion_actual)
                            #Bisharp()
                    case 'Queen':
                        print('Reina')
                            #Queen()
                    case 'King':
                        print('King')
                            #King()
                    case 'Paw':
                        vali(tipo_pieza1)
                        Paw(board, posicion_inicial, posicion_actual,tipo_pieza1)
                            #Paw()
                    case _:
                        print('Thats not an Chess Piece my man')   

                posicion_inicial = None
                posicion_actual = (0,0)


                
    # Limpiar la pantalla
    DibujarElementos()

    RecargarVentana(mi_ventana, menu_activo)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)