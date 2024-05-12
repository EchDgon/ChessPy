import pygame
from componentes.piezas import *
from componentes.colores import Colores


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


image = ['menu', icon_menu]

def ChessBoard(ventana, box):
    for i in range(8):
        for j in range(8):
            color = Colores["blanco"] if (i + j) % 2 == 0 else Colores['verde']
            pygame.draw.rect(ventana, color, (j * box, i * box, box, box))
            pygame.draw.rect(ventana, Colores['negro'], (j * box, i * box, box, box), 1 )
            if board[i][j]:
                imagen_pieza = board[i][j][1]

                ancho_imagen, alto_imagen = imagen_pieza.get_size()
                x = j * box + (box - ancho_imagen) // 2
                y = i * box + (box - alto_imagen) // 2
                ventana.blit(imagen_pieza, (x, y))

def BotonMenu(ventana, dimensionX, dimensionY):
    imagen_menu = image[1]
    ancho_menu, alto_menu = imagen_menu.get_size()
    x = (dimensionX - ancho_menu)  // 2
    y = (dimensionY - alto_menu) // 2
    ventana.blit(imagen_menu, (x,y))

def Desplegable(ventana, dimensionX, dimensionY, verga):
        pygame.draw.rect(ventana, Colores["negro"], (0,0, dimensionX, dimensionY // 3 ),2)
        pygame.draw.rect(ventana, Colores["negro"], (0, dimensionY * 0.33, dimensionX, dimensionY // 3 ), 2)
        pygame.draw.rect(ventana, Colores["negro"], (0, dimensionY * 0.66, dimensionX, dimensionY // 3 ) , 2)

        fuente = pygame.font.Font(None, 30)
        opciones = ['REINICIAR', 'PAUSAR', 'SALIR']

        texto_opcion_1 = fuente.render(opciones[0], True, Colores['blanco'])
        ventana.blit(texto_opcion_1, (((dimensionX // 2) // 2), ((dimensionY // 3) // 2)))


