import pygame

from componentes.tablero import ChessBoard, Menu

ancho = 900
alto = 600


blanco = (255, 255, 255)
azul = (179,134,82)
negro = (0, 0, 0)

ventana = pygame.display.set_mode((ancho, alto),pygame.RESIZABLE)

def AjusteDimensiones(ancho, alto):
    dimension_tablero = min(ancho , alto)
    dimension_tabla = (ancho - dimension_tablero, alto // 2)
    dimension_info = (ancho - dimension_tablero, alto // 2)
    dimension_menu = (ancho // 25, alto // 20)
    pos_tabla = (dimension_tablero, 0)
    pos_info = (dimension_tablero, alto // 2)
    pos_menu = (ancho - dimension_menu[0] - 10 , 10)
    return dimension_tablero, dimension_tabla, dimension_info, dimension_menu, pos_tabla, pos_info, pos_menu

dimension_tablero, dimension_tabla, dimension_info,dimension_menu, pos_tabla, pos_info, pos_menu = AjusteDimensiones(ancho, alto)

# Crear superficies para las secciones
superficie_tablero = pygame.Surface((dimension_tablero, alto))
superficie_tabla = pygame.Surface(dimension_tabla)
superficie_info = pygame.Surface(dimension_info)
superficie_menu = pygame.Surface(dimension_menu)

# Función para dibujar en las superficies
def DibujarElementos():
    # Limpiar las superficies
    superficie_tablero.fill(blanco)
    superficie_tabla.fill(negro)
    superficie_info.fill(negro)
    superficie_menu.fill(azul)
    box = dimension_tablero // 8
    # Dibujar objetos en cada superficie (ejemplo)
    ChessBoard(superficie_tablero, box)
    Menu(superficie_menu, dimension_menu[0], dimension_menu[1])
    pygame.draw.rect(superficie_tabla, blanco, (25, 25, dimension_tabla[0] - 50, dimension_tabla[1] - 50))
    pygame.draw.rect(superficie_info, blanco, (25, 25, dimension_info[0] - 50, dimension_info[1] - 50))

# Función para redibujar las superficies en la ventana
def RecargarVentana():
    # Dibujar las superficies en la ventana principal
    ventana.blit(superficie_tablero, (0, 0))
    ventana.blit(superficie_tabla, pos_tabla)
    ventana.blit(superficie_info, pos_info)
    ventana.blit(superficie_menu, pos_menu)

    # Actualizar la pantalla
    pygame.display.flip()

def actualizar_dimensiones(ancho, alto):
    global dimension_tablero, dimension_tabla, dimension_info,dimension_menu, pos_tabla, pos_info, pos_menu, superficie_tablero, superficie_tabla, superficie_info, superficie_menu
    dimension_tablero, dimension_tabla, dimension_info, dimension_menu, pos_tabla, pos_info, pos_menu = AjusteDimensiones(ancho, alto)
    superficie_tablero = pygame.Surface((dimension_tablero, alto))
    superficie_tabla = pygame.Surface(dimension_tabla)
    superficie_info = pygame.Surface(dimension_info)
    superficie_menu = pygame.Surface(dimension_menu)