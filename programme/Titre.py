from game import*
from Pion import*
import pygame
pygame.init()
pygame.init()


class TITLE(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.title1 = pygame.image.load('assets/BG_/titre/TITRE1.png')
        self.hit1 = self.title1.get_rect()
        self.hit1.x = 130
        self.hit1.y = 30
        self.title2 = pygame.image.load('assets/BG_/titre/TITRE2.png')
        self.hit2 = self.title1.get_rect()
        self.hit2.x = 430
        self.hit2.y = 20
        self.title3 = pygame.image.load('assets/BG_/titre/TITRE3.png')
        self.hit3 = self.title1.get_rect()
        self.hit3.x = 130
        self.hit3.y = 130
