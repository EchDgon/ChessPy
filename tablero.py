import pygame
import os
from Piezas import *

#Font colors
dark = (226,135,67)
white = (255, 255, 255)
blue = (20, 80, 240)
background = (24, 25, 30)
idk = (220, 200, 110)
boardSize = (800, 650)
chart = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#Board format
board = [
    ['T', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '']
]

#Sprites
SPRITES_DIR = "./Assets"
ROOK_SPRITE = os.path.join(SPRITES_DIR, "Rook.png")


def Tittle(screen, fuente_titulo):
    texto_titulo = fuente_titulo.render("CHESSPY", True, (255, 255, 255))
    screen.blit(texto_titulo, (10, 10))

def dibujarTablero(screen, dimension, start_point, font_size, fuente, seleccion):
	color = 0
	for i in range(8):
		for j in range(8):
			x = i * dimension + start_point[0]
			y = j * dimension + start_point[1]
			rect = pygame.Rect(x, y, dimension, dimension)
			if color % 2 == 0:
				pygame.draw.rect(screen, dark, [x, y, dimension, dimension], 0)
			else:
				pygame.draw.rect(screen, white, [x, y, dimension, dimension], 0)
			pygame.draw.rect(screen, (50, 50, 50), rect, 2) 
			
			if seleccion[0] == chart[i] and j == seleccion[1] - 1:
				pygame.draw.rect(screen, (255, 255, 102), [x, y, dimension, dimension], 0)
			color += 1
		color += 1
	
	for i in range(8):
		for j in range(8):
			if board[j][i] != '':
				AddChessPiece(screen, board[i][j], [chart[i], j + 1], dimension, start_point)
	
	letra_offset_x = dimension // 2 - font_size // 4
	numero_offset_y = dimension // font_size

	for i in range(8):
		letra_x = start_point[0] + i * dimension + letra_offset_x
		numero_y = start_point[1] + 8 * dimension + numero_offset_y
		dibujarTexto(screen, chart[i], [letra_x, numero_y], fuente, (255, 255, 255), bold=True)
		dibujarTexto(screen, str(i + 1), [start_point[0] - font_size, start_point[1] + i * dimension + numero_offset_y], fuente, (255, 255, 255), bold=True)

def AddChessPiece(screen, piece, posicion, dimension, start_point):
	chart, numero = posicion[0], posicion[1]
	x = (chart.index(posicion[0]) * dimension + start_point[0])
	y = ((numero - 1) * dimension + start_point[1])
	
	if piece == 'T':
		rook_piece = Rook((x, y), dimension)
		screen.blit(rook_piece.image, rook_piece.rect.topleft)

def dibujarTexto(screen, texto, posicion, fuente, color=(255, 255, 255), bold=False):
	fuente.set_bold(bold)
	Texto = fuente.render(texto, 1, color)
	screen.blit(Texto, posicion)


def ajustarMedidas(font_size):
    if boardSize[1] < boardSize[0]:
        ancho = int((boardSize[1] - (font_size * 2)) / 8)
        inicio = ((boardSize[0] - boardSize[1]) / 2) + font_size, font_size
    else:
        ancho = int((boardSize[0] - (font_size * 2)) / 8)
        inicio = font_size, ((boardSize[1] - boardSize[0]) / 2) + font_size
    return [inicio, ancho]


def obtenerPosicion(mouse, dimension, start_point, actual):
    xr, yr = mouse[0], mouse[1]
    for i in range(8):
        for j in range(8):
            x = i * dimension + start_point[0]
            y = j * dimension + start_point[1]
            if (xr >= x) and (xr <= x + dimension) and (yr >= y) and (yr <= y + dimension):
                actual = [chart[i], j + 1]
    return actual
