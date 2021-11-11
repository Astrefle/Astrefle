import pygame
from pygame.version import PygameVersion
pygame.init()
import pygame
pygame.init()
from Pion import*
from game import*
from Titre import*


class NEWPION(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__
        self.p2 = pygame.image.load('assets/SPRITE_/PION.png')
        self.hit_p2= self.p2.get_rect()
        print(self.hit_p2)
        self.hit_p2.x=310+190
        self.hit_p2.y=100
        self.colonne=4 
        