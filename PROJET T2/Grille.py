from Colonne import*
from Pion import*
import pygame
pygame.init()


class Grille:
    def __init__(self):
        self.stage = 5

        self.grille = []

        for line in range(7):
            self.grille.append(Colonne())

    def est_vide(self, colonne):
        return self.grille[colonne-1].est_vide()

    def taille(self, colonne):

        print(self.grille[colonne-1].taille())
        return (self.grille[colonne-1].taille())

    def ajout_pion(self, colonne, p):
        if not self.taille(colonne) > 5:

            self.grille[colonne-1].empiler(p)

        print(self.grille)

        if self.grille[colonne-1] == 4:
            print('puissance 4')
