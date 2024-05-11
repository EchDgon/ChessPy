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

                
    # Limpiar la pantalla
    DibujarElementos()

    RecargarVentana()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)