import pygame
pygame.init()

class Pion(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__
        self.p1 = pygame.image.load('assets/SPRITE_/Image1-removebg-preview.png')
        self.hit_p1= self.p1.get_rect()
        self.hit_p1.x=500
        self.hit_p1.y=600  

    def Right(self):
        self.hit_p1.x +=1
    def Left(self):
        self.hit_p1.x -=1