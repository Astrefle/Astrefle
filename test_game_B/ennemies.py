from random import randint, randrange
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
        self.p1_hit.x = 960
        self.p1_hit.y = 540
        self.vitesse = 1.5
        self.pv = 3
        self.shield = False
        self.invicible = False
        self.purification = False

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
        self.p2_hit.x = 1920
        self.p2_hit.y = randint(20, 1080)
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
        self.p3_hit.x = randint(20, 1920)
        self.p3_hit.y = 1080
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
        self.ray = pygame.image.load('3.png')
        self.ray_hit = self.ray.get_rect()
        self.ray_hit.x = randrange(0, 1910, 191)
        self.ray_hit.y = 0
        self.l_ray = []

    def ray1(self):

        self.ray = rayon_y()
        self.l_ray.append(self.ray)

    def moove_p(self):
        if self.ray_hit.x < 1910:
            self.ray_hit.x += 1

    def moove_m(self):
        if self.ray_hit.x > 20:
            self.ray_hit.x -= 1


class rayon_x(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.rax = pygame.image.load('3.png')
        self.rax_hit = self.rax.get_rect()
        self.rax_hit.x = 0
        self.rax_hit.y = randrange(0, 1070, 107)
        self.l_rax = []

    def ray1(self):

        self.rax = rayon_x()
        self.l_rax.append(self.rax)

    def moove_p(self):
        if self.rax_hit.y < 1070:
            self.rax_hit.y += 1

    def moove_m(self):
        if self.rax_hit.y > 20:
            self.rax_hit.y -= 1
