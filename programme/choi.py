import pygame
from pygame.version import PygameVersion
pygame.init()


class Choix_perso:
    def __init__(self):
        self.l_perso = {'1': "Boxer.png", '2': "Demon.png",
                        '3': "ELectro.png", '4': "Mage.png", '5': "Squellette.png"}
        self.num = 1
        self.choix = self.l_perso[f'{self.num}']
        self.perso_choisis = pygame.image.load(
            f'assets/SPRITE_/persoj1/{self.choix}')
        self.perso_choisis_hit = self.perso_choisis.get_rect()
        self.perso_choisis_hit.x = 230
        self.perso_choisis_hit.y = 520

    def Right(self):
        if not self.num >= 5:
            self.num += 1
            self.choix = self.l_perso[f'{self.num}']
            self.perso_choisis = pygame.image.load(
                f'assets/SPRITE_/persoj1/{self.choix}')

    def Left(self):
        if not self.num <= 1:
            self.num -= 1
            self.choix = self.l_perso[f'{self.num}']
            self.perso_choisis = pygame.image.load(
                f'assets/SPRITE_/persoj1/{self.choix}')
