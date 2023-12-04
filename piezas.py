import pygame
from tablero import *
import os

SPRITES_DIR = r"Assets"
ROOK_SPRITE = os.path.join(SPRITES_DIR, 'Torre-N.png')
BISHARP_SPRITE = os.path.join(SPRITES_DIR, 'Alfil-N.png')

class Rook(pygame.sprite.Sprite):
    def __init__(self, coords, dimension):
        super().__init__()
        self.image = pygame.image.load(ROOK_SPRITE)
        new_size = int(dimension * 0.95)
        self.image = pygame.transform.scale(self.image, (new_size, new_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = coords

