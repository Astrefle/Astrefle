import pygame
pygame.init()

# Utilisation de Pile


class Colonne():
    def __init__(self):
        self.contenu = []

    def __repr__(self):
        return "Colonne"+str(self.contenu)

    def est_vide(self):
        if self.contenu == []:
            return True
        else:
            return False

    def empiler(self, x):
        self.contenu.append(x)

    def depiler(self):
        assert not self.est_vide(), 'La pile est vide'
        return self.contenu.pop()

    def taille(self):
        return len(self.contenu)

    def sommet(self):
        assert not self.est_vide(), 'La pile est vide'
        return self.contenu[len(self.contenu)-1]

    def limite(self):
        if self.taille() >= 5:
            print('Vous ne pouvez pas ajouter de pions')
        return self.limite
