import pygame
from piezas import *

white = (255, 255, 255)
dark = (147, 23, 244)

width, height = 600, 600
box = width // 8

ventana = pygame.display.set_mode((width, height))

board = [[None] * 8 for _ in range(8)]
board[0][0] = ('Rook', dark_rook_image)
board[0][7] = ('Rook', dark_rook_image)
board[0][1] = ('Knight', dark_knight_image)
board[0][6] = ('Knight', dark_knight_image)
board[0][2] = ('Bisharp', dark_bisharp_image)
board[0][5] = ('Bisharp', dark_bisharp_image)
board[0][4] = ('Queen', dark_queen_image)
board[0][3] = ('King', dark_king_image)
for i in range(8):
    board[1][i] = ('Paw', dark_paw_image) 

board[7][0] = ('Rook', light_rook_image)
board[7][7] = ('Rook', light_rook_image)
board[7][1] = ('Knight', light_knight_image)
board[7][6] = ('Knight', light_knight_image)
board[7][2] = ('Bisharp', light_bisharp_image)
board[7][5] = ('Bisharp', light_bisharp_image)
board[7][4] = ('Queen', light_queen_image)
board[7][3] = ('King', light_king_image)
for i in range(8):
    board[6][i] = ('Paw', light_paw_image) 

def ChessBoard(ventana, box):
    for i in range(8):
        for j in range(8):
            jor = white if (i + j) % 2 == 0 else dark
            pygame.draw.rect(ventana, jor, (j * box, i * box, box, box))
            if board[i][j]:
                imagen_pieza = board[i][j][1]
                ventana.blit(imagen_pieza, (j * box, i * box))
