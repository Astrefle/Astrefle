import pygame
pygame.init()
from Pion import*

class Game:
    def __init__(self):
        self.pion= Pion()
        self.pressed = {}