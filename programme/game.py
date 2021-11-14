from choi import*
from Grille import*
from Pion import*
import pygame
pygame.init()


class Game:
    def __init__(self, choi1, choi2):

        self.choi1 = choi1
        self.choi2 = choi2

        self.grille = Grille()

        self.l_pion = []

        self.pressed = {}

        print(self.pressed)

        self.newpion()

    def newpion(self):

        if (len(self.l_pion) % 2) == 0:
            choi = self.choi1
        else:
            choi = self.choi2
        self.pion = PION(self.grille, self.l_pion, choi)

        self.l_pion.append(self.pion)

        return self.pion
