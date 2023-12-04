import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Configurar el tamaño del tablero y del sprite
ancho, alto = 480, 480
tamanio_casilla = ancho // 8

# Crear la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Movimiento de las Piezas')

# Cargar sprites (imágenes de las piezas)
torre_imagen = pygame.image.load('Torre-N.png')
torre_imagen = pygame.transform.scale(torre_imagen, (tamanio_casilla, tamanio_casilla))

caballo_imagen = pygame.image.load('Torre-N.png')
caballo_imagen = pygame.transform.scale(caballo_imagen, (tamanio_casilla, tamanio_casilla))

# Crear el tablero
tablero = [[None] * 8 for _ in range(8)]
tablero[3][3] = torre_imagen
tablero[4][4] = torre_imagen
tablero[2][2] = caballo_imagen
tablero[5][5] = caballo_imagen

# Bucle principal
seleccionando = False
posicion_inicial = None
posicion_actual = (0, 0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            col_seleccionada = x // tamanio_casilla
            fila_seleccionada = y // tamanio_casilla
            if tablero[fila_seleccionada][col_seleccionada]:
                seleccionando = True
                posicion_inicial = (col_seleccionada, fila_seleccionada)
        elif evento.type == pygame.MOUSEMOTION:
            if seleccionando:
                x, y = evento.pos
                col_seleccionada = x // tamanio_casilla
                fila_seleccionada = y // tamanio_casilla
                posicion_actual = (col_seleccionada, fila_seleccionada)
        elif evento.type == pygame.MOUSEBUTTONUP:
            if seleccionando:
                seleccionando = False
                # Realizar el movimiento en el tablero
                if tablero[fila_seleccionada][col_seleccionada] is None or \
                    (fila_seleccionada != posicion_inicial[1] or col_seleccionada != posicion_inicial[0]):
                    tablero[fila_seleccionada][col_seleccionada] = tablero[posicion_inicial[1]][posicion_inicial[0]]
                    tablero[posicion_inicial[1]][posicion_inicial[0]] = None

    # Limpiar la pantalla
    ventana.fill(blanco)

    # Dibujar el tablero
    for fila in range(8):
        for col in range(8):
            color = blanco if (fila + col) % 2 == 0 else negro
            pygame.draw.rect(ventana, color, (col * tamanio_casilla, fila * tamanio_casilla, tamanio_casilla, tamanio_casilla))
            if tablero[fila][col]:
                ventana.blit(tablero[fila][col], (col * tamanio_casilla, fila * tamanio_casilla))

    # Dibujar un contorno alrededor de la pieza seleccionada
    if seleccionando:
        pygame.draw.rect(ventana, (255, 0, 0), (posicion_actual[0] * tamanio_casilla, posicion_actual[1] * tamanio_casilla, tamanio_casilla, tamanio_casilla), 3)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)

