from Colonne import*
from Pion import*
import pygame
pygame.init()


class Grille:
    def __init__(self):

        self.grille = []

        for line in range(7):
            self.grille.append(Colonne())

    def est_vide(self, colonne):
        return self.grille[colonne-1].est_vide()

    def est_rempli(self):
        remplie=0
        for i in range(7):
            if self.grille[i].est_remplie():
                remplie+=1
        if remplie==7:
            return True
        else:
            return False




    def taille(self, colonne):

        print(self.grille[colonne-1].taille())
        return (self.grille[colonne-1].taille())

    def ajout_pion(self, colonne, p):
        if self.taille(colonne) <= 5:
            self.grille[colonne-1].empiler(p)
            print(self.grille)
            return True
        else:
            return False

    
