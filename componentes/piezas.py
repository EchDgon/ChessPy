import pygame
box = 80
menu_box = 30

#Dark Chess Pieces
dark_rook_image = pygame.image.load('Assets/Torre-N.png')
dark_rook_image = pygame.transform.scale(dark_rook_image, (box, box))
dark_knight_image = pygame.image.load('Assets/Caballo-N.png')
dark_knight_image = pygame.transform.scale(dark_knight_image, (box, box))
dark_bisharp_image = pygame.image.load('Assets/Alfil-N.png')
dark_bisharp_image = pygame.transform.scale(dark_bisharp_image, (box, box))
dark_queen_image = pygame.image.load('Assets/Reina-N.png')
dark_queen_image = pygame.transform.scale(dark_queen_image, (box, box))
dark_king_image = pygame.image.load('Assets/Rey-N.png')
dark_king_image = pygame.transform.scale(dark_king_image, (box, box))
dark_paw_image = pygame.image.load('Assets/Peon-N.png')
dark_paw_image = pygame.transform.scale(dark_paw_image, (box, box))

#light Chess Pieces
light_rook_image = pygame.image.load('Assets/Torre-B.png')
light_rook_image = pygame.transform.scale(light_rook_image, (box, box))
light_knight_image = pygame.image.load('Assets/Caballo-B.png')
light_knight_image = pygame.transform.scale(light_knight_image, (box, box))
light_bisharp_image = pygame.image.load('Assets/Alfil-B.png')
light_bisharp_image = pygame.transform.scale(light_bisharp_image, (box, box))
light_queen_image = pygame.image.load('Assets/Reina-B.png')
light_queen_image = pygame.transform.scale(light_queen_image, (box, box))
light_king_image = pygame.image.load('Assets/Rey-B.png')
light_king_image = pygame.transform.scale(light_king_image, (box, box))
light_paw_image = pygame.image.load('Assets/Peon-B.png')
light_paw_image = pygame.transform.scale(light_paw_image, (box, box))

#Menu
icon_menu = pygame.image.load('assets/menu.png')
icon_menu = pygame.transform.scale(icon_menu, (menu_box, menu_box))
