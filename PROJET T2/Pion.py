import pygame
pygame.init()
from Grille import*

class PION(pygame.sprite.Sprite):
    def __init__ (self,grille):
        super().__init__
        self.p1 = pygame.image.load('assets/SPRITE_/PION.png')
        self.hit_p1= self.p1.get_rect()
        print(self.hit_p1)
        self.hit_p1.x=310+190
        self.hit_p1.y=100
        self.colonne=4
        self.grille=grille

        


        
    def Right(self):
        self.hit_p1.x +=100
        self.colonne+=1
        print (self.colonne)
        return self.colonne
    def Left(self):
        self.hit_p1.x -=100
        self.colonne-=1
        print (self.colonne)
        return self.colonne
    def tombe(self):
        self.hit_p1.y+=400
        
        self.grille.ajout_pion(self.colonne) 
