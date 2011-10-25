import os
import pygame
from pygame.locals import *

class BoySprite(pygame.sprite.Sprite):
    """ Class that renders the boy """
    def __init__(self, gameSurface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('spriteImages', 'boy.png'))
        self.rect = self.image.get_rect()

class StarSprite(pygame.sprite.Sprite):
    """ Class that renders the star """
    def __init__(self, gameSurface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('spriteImages', 'star.png'))
        self.rect = self.image.get_rect()
