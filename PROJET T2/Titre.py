import pygame
pygame.init()
import pygame
pygame.init()
from Pion import*
from game import*


class TITLE(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__
        self.title1 = pygame.image.load('assets/BG_/TITRE1.png')
        self.hit1= self.title1.get_rect()
        self.hit1.x=400
        self.hit1.y=50
        self.title2 = pygame.image.load('assets/BG_/TITRE2.png')
        self.hit2= self.title1.get_rect()
        self.hit2.x=700
        self.hit2.y=40
        self.title3 = pygame.image.load('assets/BG_/TITRE3.png')
        self.hit3= self.title1.get_rect()
        self.hit3.x=400
        self.hit3.y=150