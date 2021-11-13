import pygame
from pygame.version import PygameVersion
from Titre import*
from button import*

L = 600
H = 700

pygame.display.set_caption("Brawl 4 Monsters")
screen = pygame.display.set_mode((L, H))

start = pygame.image.load('assets/SPRITE_/debut/start_btn.png')
start_btn = Button(180, 210, start, 0.8)

credit_img = pygame.image.load('assets/SPRITE_/debut/credit.png')
credit_btn = Button(180, 310, start, 0.8)

regle_img = pygame.image.load('assets/SPRITE_/debut/regle.png')
regle_btn = Button(180, 420, start, 0.8)

bg_ = pygame.image.load('assets/BG_/WarmWarmheartedIrishwolfhound-max-1mb.gif')

Titre = TITLE()

runn = True

while runn:
    # Fond d'ecran
    screen.blit(bg_, (0, 0))
# Titre du jeu
    screen.blit(Titre.title1, Titre.hit1)
    screen.blit(Titre.title2, Titre.hit2)
    screen.blit(Titre.title3, Titre.hit3)

    screen.blit(start, (160, 200))
    screen.blit(credit_img, (160, 310))
    screen.blit(regle_img, (160, 420))

    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            runn = False
            pygame.quit()

    if start_btn.draw(screen):
        runn = False
        pygame.quit()

    elif credit_btn.draw(screen):
        print('credit')

    elif regle_btn.draw(screen):
        print('regle')
