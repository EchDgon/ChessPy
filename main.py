import pygame
from tablero import *
from Movements import *

def main():
    pygame.init()

    icono = pygame.image.load('Icono.png')
    pygame.display.set_icon(icono)

    fuente_titulo = pygame.font.SysFont("bold", 30)
    pygame.display.set_caption("CHESSPY")

    screen = pygame.display.set_mode(boardSize)
    game_over = False
    clock = pygame.time.Clock()
    font_size = 30
    seleccion = ['Z', -1]
    origen = None
    fuente = pygame.font.SysFont("arial",font_size)
    start, dimension = ajustarMedidas(font_size)
    while game_over is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        botones = pygame.mouse.get_pressed()
        if botones[0]:
            pos = pygame.mouse.get_pos()
            nueva_seleccion = obtenerPosicion(pos, dimension, start, seleccion)
            if origen is None:
                origen = nueva_seleccion
            else:
                destino = nueva_seleccion
                if MoveRook(board, origen, destino):
                    origen = None 
                else:
                    origen = None
        
        screen.fill(background)
        dibujarTablero(screen, dimension, start, font_size, fuente, seleccion)
        if origen is not None:
            AddChessPiece(screen, 'T', origen, dimension, start)
        
        Tittle(screen, fuente_titulo)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
