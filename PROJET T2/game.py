import pygame
pygame.init()
from Pion import*
from Grille import*


class Game:
    def __init__(self):
        self.grille=Grille()
       
        self.l_pion=[]
        
        self.pion= PION(self.grille)
        
        self.pressed ={}

        print(self.pressed)
        self.l_pion.append(self.pion)
    def newpion(self):
        self.pion=PION(self.grille)
        self.l_pion.append(self.pion)
        return self.pion
       
