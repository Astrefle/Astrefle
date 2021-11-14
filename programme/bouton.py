from choi2 import*
from Titre import*
from game import*
from choi import*
import pygame
from pygame.version import PygameVersion
from button import*
from Ecran_deb import*

pygame.init()

pygame.display.set_caption("Brawl 4 Monsters-Choisissez un personnage")
screen = pygame.display.set_mode((600, 700))


right_img = pygame.image.load('assets/SPRITE_/fleche/right.png')
left_img = pygame.image.load('assets/SPRITE_/fleche/left.png')
entre_img = pygame.image.load('assets/SPRITE_/fleche/entre.png')

right_button = Button(430, 550, right_img, 0.8)
left_button = Button(0, 550, left_img, 0.8)
entre_button = Button(210, 450, left_img, 0.8)


jeu_start = 0
suivant = 1
bg_ = pygame.image.load('assets/BG_/bg/numachi.png')
Titre = TITLE()
Choix1 = Choix_perso()
Choix2 = Choix_perso2()
Choix2.perso_choisis_hit.y += 300
pressed = {}

son_select = pygame.mixer.Sound('assets/SOUND_/selec.wav')
son_choix = pygame.mixer.Sound('assets/SOUND_/choix.wav')

while run:
    # Fond d'ecran
    screen.blit(bg_, (0, 0))
# Titre du jeu
    screen.blit(Titre.title1, Titre.hit1)
    screen.blit(Titre.title2, Titre.hit2)
    screen.blit(Titre.title3, Titre.hit3)
# Perso 1 et 2
    screen.blit(Choix1.perso_choisis, Choix1.perso_choisis_hit)
    screen.blit(Choix2.perso_choisis, Choix2.perso_choisis_hit)
# Flêche
    screen.blit(right_img, (430, 550))
    screen.blit(left_img, (0, 550))
    screen.blit(entre_img, (210, 450))

    pygame.display.flip()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()
        if i.type == pygame.KEYUP:
            pressed[i.key] = True

        if jeu_start == 0:
            if right_button.draw(screen):
                son_select.play()
                Choix1.Right()
            elif left_button.draw(screen):
                son_select.play()
                Choix1.Left()
            elif entre_button.draw(screen):
                son_choix.play()
                jeu_start += 1
                joueur1 = Choix1.perso_choisis
                Choix1.perso_choisis_hit.y += 300
                Choix2.perso_choisis_hit.y -= 300
                suivant = 0

        elif jeu_start == 1:
            if right_button.draw(screen):
                son_select.play()
                Choix2.Right()
            elif left_button.draw(screen):
                son_select.play()
                Choix2.Left()
            elif entre_button.draw(screen):
                son_choix.play()
                jeu_start += 1
                joueur2 = Choix2.perso_choisis
                running = True
                run = False
                pygame.quit()
    pressed[pygame.K_RETURN] = False
