import pygame

from componentes.tablero import ChessBoard, BotonMenu, Desplegable
from componentes.colores import Colores
from componentes.piezas import dark_rook_image

ancho = 900
alto = 600

ventana = pygame.display.set_mode((ancho, alto),pygame.RESIZABLE)

def AjusteDimensiones(ancho, alto):
    dimension_tablero = min(ancho , alto)
    dimension_tabla = (ancho - dimension_tablero, alto // 2)
    dimension_info = (ancho - dimension_tablero, alto // 2)
    dimension_menu = (ancho // 25, alto // 20)
    dimension_desplegable = (alto // 4, alto // 4)
    pos_tabla = (dimension_tablero, 0)
    pos_info = (dimension_tablero, alto // 2)
    pos_menu = (ancho - dimension_menu[0] - 5 , 5)
    pos_desplegable = (ancho - dimension_desplegable[0] - 5, pos_menu[1] + dimension_menu[1])
    return dimension_tablero, dimension_tabla, dimension_info, dimension_menu, dimension_desplegable, pos_tabla, pos_info, pos_menu, pos_desplegable

dimension_tablero, dimension_tabla, dimension_info, dimension_menu, dimension_desplegable, pos_tabla, pos_info, pos_menu, pos_desplegable = AjusteDimensiones(ancho, alto)

# Crear superficies para las secciones
superficie_tablero = pygame.Surface((dimension_tablero, alto))
superficie_tabla = pygame.Surface(dimension_tabla)
superficie_info = pygame.Surface(dimension_info)
superficie_menu = pygame.Surface(dimension_menu)
superficie_desplegable = pygame.Surface(dimension_desplegable)

def DibujarElementos():

    superficie_tablero.fill(Colores["blanco"])
    superficie_tabla.fill(Colores["negro"])
    superficie_info.fill(Colores["negro"])
    superficie_menu.fill(Colores["gris"])
    superficie_desplegable.fill(Colores["gris"])
    box = dimension_tablero // 8


    ChessBoard(superficie_tablero, box)
    BotonMenu(superficie_menu, dimension_menu[0], dimension_menu[1])
    Desplegable(superficie_desplegable, dimension_desplegable[0], dimension_desplegable[1], dimension_desplegable)

    pygame.draw.rect(superficie_tabla, Colores['verde'], (15, 15, dimension_tabla[0] - 30, dimension_tabla[1] - 30))
    pygame.draw.rect(superficie_info, Colores["verde"], (15, 15, dimension_info[0] - 30, dimension_info[1] - 30))

# Función para redibujar las superficies en la ventana
def RecargarVentana(boolean):
    # Dibujar las superficies en la ventana principal
    if boolean  == False :
        ventana.blit(superficie_tablero, (0, 0))
        ventana.blit(superficie_tabla, pos_tabla)
        ventana.blit(superficie_info, pos_info)
        ventana.blit(superficie_menu, pos_menu)

        # Actualizar la pantalla
        pygame.display.flip()
    else:
        ventana.blit(superficie_tablero, (0, 0))
        ventana.blit(superficie_tabla, pos_tabla)
        ventana.blit(superficie_info, pos_info)
        ventana.blit(superficie_menu, pos_menu)
        ventana.blit(superficie_desplegable, pos_desplegable)

        # Actualizar la pantalla
        pygame.display.flip()

def actualizar_dimensiones(ancho, alto):
    global dimension_tablero, dimension_tabla, dimension_info, dimension_menu, dimension_desplegable, pos_tabla, pos_info, pos_menu, pos_desplegable, superficie_tablero, superficie_tabla, superficie_info, superficie_menu, superficie_desplegable
    dimension_tablero, dimension_tabla, dimension_info, dimension_menu, dimension_desplegable, pos_tabla, pos_info, pos_menu, pos_desplegable = AjusteDimensiones(ancho, alto)
    superficie_tablero = pygame.Surface((dimension_tablero, alto))
    superficie_tabla = pygame.Surface(dimension_tabla)
    superficie_info = pygame.Surface(dimension_info)
    superficie_menu = pygame.Surface(dimension_menu)
    superficie_desplegable = pygame.Surface(dimension_desplegable)
