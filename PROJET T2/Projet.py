from bouton import*
from choi import*
from Titre import*
from game import*
from Pion import*
import pygame
from pygame.version import PygameVersion
pygame.init()


pygame.display.set_caption("Brawl 4 Monsters")
screen = pygame.display.set_mode((1080, 720))

game = Game(Choix1, Choix2)

running = True

bg_ = pygame.image.load('assets/BG_/WarmWarmheartedIrishwolfhound-max-1mb.gif')

Titre = TITLE()
Choix = Choix_perso()


while running:
    # fond d'ecran
    screen.blit(bg_, (0, 0))
# Perso 1
    screen.blit(joueur1, (50, 520))
# Perso 2
    screen.blit(joueur2, (900, 520))


# Test affichage pion
    for i in game.l_pion:
        screen.blit(i.p1, i.hit_p1)

    # Déplacement du pion
    if game.pressed.get(pygame.K_RIGHT) and game.pion.hit_p1.x+game.pion.hit_p1.width < 880:
        game.pion.Right()
    elif game.pressed.get(pygame.K_LEFT) and game.pion.hit_p1.x > 200:
        game.pion.Left()
    elif game.pressed.get(pygame.K_RETURN) and game.pion.hit_p1.y < 700:
        game.pion.tombe()
        game.newpion()

    pygame.display.flip()

   # def des touches du jeu
    game.pressed[pygame.K_RIGHT] = False
    game.pressed[pygame.K_LEFT] = False
    game.pressed[pygame.K_RETURN] = False

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()

        if i.type == pygame.KEYUP:
            game.pressed[i.key] = True
