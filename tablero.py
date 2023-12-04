import pygame
from piezas import *

white = (255, 255, 255)
dark = (0, 0, 0)

width, height = 600, 600
box = width // 8

ventana = pygame.display.set_mode((width, height))
rook_image = pygame.image.load('Assets/Torre-N.png')
rook_image = pygame.transform.scale(rook_image, (box, box))

board = [[None] * 8 for _ in range(8)]
board[0][0] = ('rook', rook_image)
board[0][7] = ('rook', rook_image)


def ChessBoard(ventana, box):
    for i in range(8):
        for j in range(8):
            jor = white if (i + j) % 2 == 0 else dark
            pygame.draw.rect(ventana, jor, (j * box, i * box, box, box))
            if board[i][j]:
                imagen_pieza = board[i][j][1]
                ventana.blit(imagen_pieza, (j * box, i * box))
