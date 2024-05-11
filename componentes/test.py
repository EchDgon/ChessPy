import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
azul = (0, 0, 255)

# Configurar la pantalla
ancho, alto = 400, 300
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Menú desplegable')

# Definir algunas constantes para el botón y el menú
BOTON_ANCHO, BOTON_ALTO = 120, 40
MENU_ANCHO, MENU_ALTO = 100, 120
menu_mostrado = False
pausado = False

# Crear el reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()

while True:
    ventana.fill(blanco)
    
    # Coordenadas del botón
    boton_x, boton_y = 140, 120
    
    # Dibujar el botón
    boton = pygame.Rect(boton_x, boton_y, BOTON_ANCHO, BOTON_ALTO)
    pygame.draw.rect(ventana, negro, boton)
    
    # Dibujar el texto del botón
    fuente = pygame.font.Font(None, 30)
    texto_boton = fuente.render('Menú', True, blanco)
    texto_rect = texto_boton.get_rect(center=boton.center)
    ventana.blit(texto_boton, texto_rect)
    
    # Coordenadas del menú desplegable
    menu_x, menu_y = boton_x, boton_y + BOTON_ALTO
    
    if menu_mostrado:
        # Dibujar el menú desplegable
        menu = pygame.Rect(menu_x, menu_y, MENU_ANCHO, MENU_ALTO)
        pygame.draw.rect(ventana, azul, menu)
        pygame.draw.rect(ventana, negro, menu, 2)
        # Opciones del menú
        opciones = ['Nuevo Juego', 'Pausa', 'Salir']
        for i, opcion in enumerate(opciones):
            opcion_y = menu_y + 10 + i * 30
            texto_opcion = fuente.render(opcion, True, blanco)
            texto_rect_opcion = texto_opcion.get_rect(x=menu_x + 10, y=opcion_y)
            ventana.blit(texto_opcion, texto_rect_opcion)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton.collidepoint(evento.pos):
                menu_mostrado = not menu_mostrado
            elif menu_mostrado:
                for i, opcion in enumerate(opciones):
                    if texto_rect_opcion.collidepoint(evento.pos):
                        if opcion == 'Nuevo Juego':
                            print('Nuevo Juego')
                            # Agrega aquí el código para reiniciar el juego
                        elif opcion == 'Pausa':
                            print('Pausa')
                            pausado = not pausado
                            # Agrega aquí el código para pausar o reanudar el juego
                        elif opcion == 'Salir':
                            pygame.quit()
                            sys.exit()
    
    reloj.tick(30)
