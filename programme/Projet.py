
from choi import*
from Titre import*
from game import*
from Pion import*
from stage import*
import pygame
from pygame.version import PygameVersion
pygame.init()


pygame.display.set_caption("Brawl 4 Monsters")
screen = pygame.display.set_mode((1080, 720))

game = Game(Choix1, Choix2)

grille_img=pygame.image.load('assets/SPRITE_/grille.png')


bg_ = bg

Titre = TITLE()
Choix = Choix_perso()

# Test audio
pion_moove = pygame.mixer.Sound("assets/SOUND_/pion_mooving.ogg")
pion_fall = pygame.mixer.Sound("assets/SOUND_/pion_fall.ogg")
son = music

son.set_volume(0.8)
pion_moove.set_volume(0.3)
pion_fall.set_volume(0.3)

son.play(10)

# Barre de vie
pv1 = pygame.image.load('assets/SPRITE_/barre_vie/pv1.png')
pv2 = pygame.image.load('assets/SPRITE_/barre_vie/pv1.png')


while running:

# fond d'ecran
    screen.blit(bg_, (0, 0))
# Perso 1
    screen.blit(joueur1, (20, 520))
# Perso 2
    screen.blit(joueur2, (950, 520))

# PV
    screen.blit(pv1, (20, 450))
    screen.blit(pv2, (950, 450))
#Grille
    screen.blit(grille_img,(200,100))

# Test affichage pion

    for i in game.l_pion:
        screen.blit(i.p1, i.hit_p1)

    # Déplacement du pion
    if game.pressed.get(pygame.K_RIGHT) and game.pion.hit_p1.x+game.pion.hit_p1.width < 880:
        game.pion.Right()
        pion_moove.play()
    elif game.pressed.get(pygame.K_LEFT) and game.pion.hit_p1.x > 200:
        game.pion.Left()
        pion_moove.play()
    elif game.pressed.get(pygame.K_RETURN) and game.pion.hit_p1.y < 700:
        if game.pion.tombe() == True:
            pion_fall.play()
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
