from choi import*
from Grille import*
import pygame
pygame.init()


class PION(pygame.sprite.Sprite):
    def __init__(self, grille, l_pion, choi):
        super().__init__
        self.choi = choi
        self.l_pion_perso = {'Boxer.png': "PION1.png", 'Demon.png': "PION2.png",
                             'ELectro.png': "PION3.png", 'Mage.png': "PION4.png", 'Squellette.png': "PION5.png"}
        self.pion = self.l_pion_perso[f'{self.choi.choix}']
        print(self.choi.choix)
        self.p1 = pygame.image.load(f'assets/SPRITE_/pion/{self.pion}')
        self.hit_p1 = self.p1.get_rect()
        print(self.hit_p1)
        self.hit_p1.x = 310+190
        self.hit_p1.y = 0
        self.colonne = 4

        self.grille = grille
        self.l_pion = l_pion

    def Right(self):
        self.hit_p1.x += 100
        self.colonne += 1
        print(self.colonne)
        return self.colonne

    def Left(self):
        self.hit_p1.x -= 100
        self.colonne -= 1
        print(self.colonne)
        return self.colonne

    def tombe(self):
        
        if (len(self.l_pion) % 2) == 0:
            p = -1

        else:
            p = 1
        if self.grille.ajout_pion(self.colonne, p) == True:
            self.hit_p1.y = self.hit_p1.y+700 - \
                (100*self.grille.taille(self.colonne))
            return True
        else:
            return False
