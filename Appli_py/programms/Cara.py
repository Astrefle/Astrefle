#@guillaume._frh
import pygame


class Cara():
    def __init__(self, lettre, space, ret):
        super().__init__
        self.lettre = pygame.image.load(f'assets/cara/{lettre}.png')
        self.lettre_rect = self.lettre.get_rect()
        self.lettre_rect.x = space
        self.x_save = space
        self.lettre_rect.y = ret
        self.liste = []

    def add(self):
        self.lettre_rect.x += 10

    def ret(self, lettre):
        if lettre == 'return':
            self.lettre_rect.y += 50
            self.lettre_rect.x = self.x_save - 10

    def mot(self, lettre):
        self.lettre = Cara(lettre, self.lettre_rect.x, self.lettre_rect.y)
        self.liste.append(self.lettre)

    def clean(self):
        self.liste = []
        self.lettre_rect.x = self.x_save
