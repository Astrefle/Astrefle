import pygame
from pygame import*
from pygame.version import PygameVersion
from random import*
pygame.init()

class P1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.p1 = pygame.image.load('1.png')
        self.p1_hit = self.p1.get_rect()
        self.p1_hit.x = 480
        self.p1_hit.y = 270
        self.vitesse=1.5
        self.pv=3
        self.shield=False
        self.invicible=False
        self.purification=False


    def moove_l(self):
        self.p1_hit.x -= self.vitesse
    def moove_r(self):
        self.p1_hit.x += self.vitesse
    def moove_u(self):
        self.p1_hit.y -= self.vitesse
    def moove_d(self):
        self.p1_hit.y += self.vitesse

class essaim_x(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.p2 = pygame.image.load('3.png')
        self.p2_hit = self.p2.get_rect()
        self.p2_hit.x = 760
        self.p2_hit.y = randint(20,540)
        self.l_p2 = []
        self.vitesse = 1

    def moove(self):
        self.p2_hit.x -= self.vitesse

    def ennemies1(self):
        self.p2 = essaim_x()
        self.l_p2.append(self.p2)

    def moove_f(self):
        self.p2_hit.x -= self.vitesse*1

    def moove_ff(self):
        self.p2_hit.x -= (self.vitesse*2)+1


class essaim_y(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.p3 = pygame.image.load('3.png')
        self.p3_hit = self.p3.get_rect()
        self.p3_hit.x = randint(20,760)
        self.p3_hit.y = 540
        self.l_p3 = []
        self.vitesse = 1

    def moove(self):
        self.p3_hit.y -= self.vitesse

    def ennemies1(self):
        self.p3 = essaim_y()
        self.l_p3.append(self.p3)

    def moove_f(self):
        self.p3_hit.y -= self.vitesse*1

    def moove_ff(self):
        self.p3_hit.y -= (self.vitesse*2)+1


class rayon_y(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.ra = pygame.image.load('3.png')
        self.ra_hit = self.ra.get_rect()
        self.ra_hit.x = randrange(0,760,76)
        self.ra_hit.y = 0
        self.l_ra = []

    def ray1(self):
        for i in range(0,2):
            self.ra=rayon_y()
            self.l_ra.append(self.ra)

    def moove_p(self):
        if self.ra_hit.x<760:
            self.ra_hit.x+=1
    def moove_m(self):
        if self.ra_hit.x>20:
         self.ra_hit.x-=1

