import pygame
from componentes.piezas import *

white = (255, 255, 255)
trust = (135,135,135)
dark = (0, 0, 0)

ancho, alto = 600, 700

ventana = pygame.display.set_mode((ancho, alto))

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
            color = white if (i + j) % 2 == 0 else trust
            pygame.draw.rect(ventana, color, (j * box, i * box, box, box))
            pygame.draw.rect(ventana, dark, (j * box, i * box, box, box), 1 )
            if board[i][j]:
                imagen_pieza = board[i][j][1]

                ancho_imagen, alto_imagen = imagen_pieza.get_size()
                x = j * box + (box - ancho_imagen) // 2
                y = i * box + (box - alto_imagen) // 2
                ventana.blit(imagen_pieza, (x, y))

