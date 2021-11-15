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

        return (self.grille[colonne-1].taille())

    def ajout_pion(self, colonne, p):
        if self.taille(colonne) <= 5:
            self.grille[colonne-1].empiler(p)
            print(self.grille)
            return True
        else:
            return False
    
    def p4_hori(self,colonne):
        p=self.grille[colonne-1].sommet()
        print(p)
        if colonne>4:
            m=colonne-4
        else:
            m=1
        if colonne<3:
            M=colonne+4
        else:
            M=7
        print(f'm={m}')
        print(f'M={M}')
        while m+3 <= M:
            j=0
            for i in range(m,m+4,1):
                print(f'cellule={self.grille[i-1].cellule(self.taille(colonne))}')
                if self.grille[i-1].cellule(self.taille(colonne))==p:
                    j+=1
            print(f'j={j}')
            if j==4:
                return True
            else:
                m+=1   
        return False 

    def p4(self,colonne):
        if self.grille[colonne-1].p4():
            return True
        elif self.p4_hori(colonne):
            return True

        else:
            return False

    
