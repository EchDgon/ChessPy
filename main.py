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

# Bucle principal
seleccionando = False
posicion_inicial = None
posicion_actual = (0,0)

menu_activo = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.VIDEORESIZE:
            ancho_n, alto_n = evento.size[0], evento.size[1]
            ventana = pygame.display.set_mode((ancho_n, alto_n), pygame.RESIZABLE)
            actualizar_dimensiones(ancho_n, alto_n)
            dimension_menu = (ancho_n // 25, alto_n // 20)
            pos_menu= (ancho_n - dimension_menu[0] - 5 , 5)
            print("estoy dentro de este bucle")
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            # Verificar si se hizo clic en el tablero de ajedrez
            if x < dimension_tablero and not menu_activo:
                col_seleccionada = x // box
                fila_seleccionada = y // box
                pieza_seleccionada = board[fila_seleccionada][col_seleccionada]
                if pieza_seleccionada:
                        seleccionando = True
                        tipo_pieza, imagen_pieza = pieza_seleccionada
                        posicion_inicial = (col_seleccionada, fila_seleccionada)
            # Verificar si se hizo clic en el botón del menú
            elif x >= pos_menu[0] and x <= pos_menu[0] + dimension_menu[0] and y >= pos_menu[1] and y <= pos_menu[1] + dimension_menu[1]:
                menu_activo = not menu_activo    

                
    # Limpiar la pantalla
    DibujarElementos()

    RecargarVentana(menu_activo)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)