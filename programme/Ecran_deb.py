import pygame
from pygame.display import flip
from pygame.version import PygameVersion
from Titre import*
from button import*
pygame.init()

L = 600
H = 700

pygame.display.set_caption("Brawl 4 Monsters-Acceuil")
screen = pygame.display.set_mode((L, H))

start = pygame.image.load('assets/SPRITE_/debut/start_btn.png')
start_btn = Button(180, 210, start, 0.8)

credit_img = pygame.image.load('assets/SPRITE_/debut/credit.png')
credit_btn = Button(180, 310, credit_img, 0.8)
credit_str = pygame.image.load('assets/SPRITE_/debut/credit_str.png')
credit_str_hit = credit_str.get_rect()
credit_str_hit.x = 48
credit_str_hit.y = 700

regle_img = pygame.image.load('assets/SPRITE_/debut/regle.png')
regle_btn = Button(180, 420, regle_img, 0.8)
regle_str = pygame.image.load('assets/SPRITE_/debut/regle_str.png')
regle_str_hit = regle_str.get_rect()
regle_str_hit.x = 48
regle_str_hit.y = 700

ok_img = pygame.image.load('assets/SPRITE_/debut/ok.png')
ok_btn = Button(160.5, 574, ok_img, 0.8)
ok_img_hit = ok_img.get_rect()
ok_img_hit.x = 160.5
ok_img_hit.y = 700


bg_ = pygame.image.load('assets/BG_/bg/thumb2-4k-sea-moon-digital-art-8-bit.png')

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
    screen.blit(ok_img, (ok_img_hit.x, ok_img_hit.y))
    screen.blit(regle_img, (160, 420))
    screen.blit(credit_str, (credit_str_hit.x, credit_str_hit.y))
    screen.blit(regle_str, (regle_str_hit.x, regle_str_hit.y))
    screen.blit(ok_img, (ok_img_hit.x, ok_img_hit.y))

    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            runn = False
            pygame.quit()

    if start_btn.draw(screen):
        run = True
        runn = False
        pygame.quit()

    elif credit_btn.draw(screen):
        credit_str_hit.y = 94
        ok_img_hit.y = 574

    elif regle_btn.draw(screen):
        regle_str_hit.y = 94
        ok_img_hit.y = 574

    elif ok_btn.draw(screen):
        regle_str_hit.y = 700
        credit_str_hit.y = 700
        ok_img_hit.y = 700
