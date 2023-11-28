import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (20, 80, 240)
FONDO = (24, 25, 30)
SELECCIONA = (220, 200, 110)
DIMENCIONES = (800, 600)
LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def dibujarTablero(screen, dimension, p_inicio, tamanio_fuente, fuente, seleccion):
	'''
	# Funcion que dibuja el tablero
	screen: 		referencia del lienzo donde dibujar
	dimension: 		tamanio de los rectangulos
	p_inicio: 		coordenadas del punto de inicio del tablero
	tamanio_fuente: tamanio de fuente segun el tablero
	fuente: 		Objeto fuente 
	seleccion: 		rectangulo seleccionado 
	'''
	color = 0
	for i in range(8):
		for j in range(8):
			x = i * dimension + p_inicio[0]
			y = j * dimension + p_inicio[1]
			if color % 2 == 0:
				pygame.draw.rect(screen, NEGRO, [x, y, dimension, dimension], 0)
			else:
				pygame.draw.rect(screen, BLANCO, [x, y, dimension, dimension], 0)
			if seleccion[0] == LETRAS[i] and j == seleccion[1] - 1:
				pygame.draw.rect(screen, SELECCIONA, [x, y, dimension, dimension], 0)
			color += 1
		color += 1
		dibujarTexto(screen, LETRAS[i], [i * dimension + p_inicio[0], p_inicio[1] - tamanio_fuente], fuente)
		dibujarTexto(screen, str(i + 1), [p_inicio[0] - tamanio_fuente, i * dimension + p_inicio[1]], fuente)


def dibujarTexto(screen, texto, posicion, fuente):
    Texto = fuente.render(texto, 1, AZUL)
    screen.blit(Texto, posicion)


def ajustarMedidas(tamanio_fuente):
    if DIMENCIONES[1] < DIMENCIONES[0]:
        ancho = int((DIMENCIONES[1] - (tamanio_fuente * 2)) / 8)
        inicio = ((DIMENCIONES[0] - DIMENCIONES[1]) / 2) + tamanio_fuente, tamanio_fuente
    else:
        ancho = int((DIMENCIONES[0] - (tamanio_fuente * 2)) / 8)
        inicio = tamanio_fuente, ((DIMENCIONES[1] - DIMENCIONES[0]) / 2) + tamanio_fuente
    return [inicio, ancho]


def obtenerPosicion(mouse, dimension, p_inicio, actual):
    xr, yr = mouse[0], mouse[1]
    for i in range(8):
        for j in range(8):
            x = i * dimension + p_inicio[0]
            y = j * dimension + p_inicio[1]
            if (xr >= x) and (xr <= x + dimension) and (yr >= y) and (yr <= y + dimension):
                actual = [LETRAS[i], j + 1]
    return actual
