from choi2 import*
from Titre import*
from game import*
from choi import*
import pygame
from pygame.version import PygameVersion

from choi2 import Choix_perso2
pygame.init()

pygame.display.set_caption("Brawl 4 Monsters")
screen = pygame.display.set_mode((600, 700))

run = True
jeu_start = 0
suivant = 1
bg_ = pygame.image.load('assets/BG_/WarmWarmheartedIrishwolfhound-max-1mb.gif')
Titre = TITLE()
Choix1 = Choix_perso()
Choix2 = Choix_perso2()
Choix2.perso_choisis_hit.y += 300
pressed = {}

while run:
    # fond d'ecran
    screen.blit(bg_, (0, 0))
# Titre du jeu
    screen.blit(Titre.title1, Titre.hit1)
    screen.blit(Titre.title2, Titre.hit2)
    screen.blit(Titre.title3, Titre.hit3)
# Perso 1 et 2
    screen.blit(Choix1.perso_choisis, Choix1.perso_choisis_hit)
    screen.blit(Choix2.perso_choisis, Choix2.perso_choisis_hit)
    pygame.display.flip()

    pressed[pygame.K_RIGHT] = False
    pressed[pygame.K_LEFT] = False
    pressed[pygame.K_RETURN] = False

    for i in pygame.event.get():
        if i.type == pygame.QUIT:

            run = False
            pygame.quit()

        if i.type == pygame.KEYUP:
            pressed[i.key] = True

        if not suivant == 0:
            if pressed.get(pygame.K_RIGHT):
                Choix1.Right()
            elif pressed.get(pygame.K_LEFT):
                Choix1.Left()
            if pressed.get(pygame.K_RETURN):
                jeu_start += 1
                joueur1 = Choix1.perso_choisis
                Choix1.perso_choisis_hit.y += 300
                Choix2.perso_choisis_hit.y -= 300
                suivant = 0

        if suivant == 0:

            if pressed.get(pygame.K_RIGHT):
                Choix2.Right()
            elif pressed.get(pygame.K_LEFT):
                Choix2.Left()
            if pressed.get(pygame.K_RETURN):
                jeu_start += 1
                joueur2 = Choix2.perso_choisis

        if jeu_start == 3:
            running = True
            run = False
            pygame.quit()
