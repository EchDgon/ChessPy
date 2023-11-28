import pygame
from tablero import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(DIMENCIONES)
    pygame.display.set_caption("CHEESPY")
    game_over = False
    clock = pygame.time.Clock()
    tamanio_fuente = 30
    seleccion = ['Z', -1]
    fuente = pygame.font.SysFont("arial",tamanio_fuente)
    puntoInicio, dimension = ajustarMedidas(tamanio_fuente)
    while game_over is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        botones = pygame.mouse.get_pressed()
        if botones[0]:
            pos = pygame.mouse.get_pos()
            seleccion = obtenerPosicion(pos, dimension, puntoInicio, seleccion)
        screen.fill(FONDO)
        dibujarTablero(screen, dimension, puntoInicio, tamanio_fuente, fuente, seleccion)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
