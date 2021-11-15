
from choi import*
from Titre import*
from game import*
from Pion import*
from stage import*
from pv import*
from button import*
import pygame
from pygame.version import PygameVersion
pygame.init()


pygame.display.set_caption("Brawl 4 Monsters")
screen = pygame.display.set_mode((1080, 720))

game = Game(Choix1, Choix2)

grille_img = pygame.image.load('assets/SPRITE_/grille.png')

rejouer_img = pygame.image.load('assets/SPRITE_/debut/rejouer.png')
rejouer_btn = Button(160.5, 574, rejouer_img, 0.8)
rejouer_img_hit = rejouer_img.get_rect()
rejouer_img_hit.x = 160.5
rejouer_img_hit.y = 720

quitter_img = pygame.image.load('assets/SPRITE_/debut/quitter.png')
quitter_btn = Button(660.5, 574, quitter_img, 0.8)
quitter_img_hit = quitter_img.get_rect()
quitter_img_hit.x = 660.5
quitter_img_hit.y = 720

win_1 = pygame.image.load('assets/SPRITE_/debut/Image2.png')
win_2 = pygame.image.load('assets/SPRITE_/debut/Image1.png')
win_1_hit = win_1.get_rect()
win_1_hit.x = 290
win_1_hit.y = 720
win_2_hit = win_2.get_rect()
win_2_hit.x = 290
win_2_hit.y = 720


bg_ = bg

Titre = TITLE()
Choix = Choix_perso()

# Test audio
pion_moove = pygame.mixer.Sound("assets/SOUND_/pion_mooving.ogg")
pion_fall = pygame.mixer.Sound("assets/SOUND_/pion_fall.ogg")
son = music

son.set_volume(0.5)
pion_moove.set_volume(0.3)
pion_fall.set_volume(0.3)

son.play(10)

# Barre de vie
pv = PV()
pv1 = pygame.image.load(f'assets/SPRITE_/barre_vie/{pv.pv1}')
pv2 = pygame.image.load(f'assets/SPRITE_/barre_vie/{pv.pv2}')


while running:

    # fond d'ecran
    screen.blit(bg_, (0, 0))
# Perso 1
    screen.blit(joueur1, (20, 520))
# Perso 2
    screen.blit(joueur2, (950, 520))

# PV
    screen.blit(pv1, (joueur1_hit.x, joueur1_hit.y))
    screen.blit(pv2, (joueur2_hit.x, joueur2_hit.y))
# Grille
    screen.blit(grille_img, (200, 100))
# ecran de fin
    screen.blit(rejouer_img, (rejouer_img_hit.x, rejouer_img_hit.y))
    screen.blit(quitter_img, (quitter_img_hit.x, quitter_img_hit.y))
    screen.blit(win_1, (win_1_hit.x, win_1_hit.y))
    screen.blit(win_2, (win_2_hit.x, win_2_hit.y))
# affichage pion

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
            # Evènement grille rempli
            if game.grille.est_rempli():
                game.new_grille()
            # Evènement puissance 4
            if game.grille.p4(game.pion.colonne):
                game.new_grille()
                if game.pion.p == -1:
                    pv.degat1()
                    pv1 = pygame.image.load(
                        f'assets/SPRITE_/barre_vie/{pv.pv1}')
                else:
                    pv.degat2()
                    pv2 = pygame.image.load(
                        f'assets/SPRITE_/barre_vie/{pv.pv2}')
                if pv.mort1():
                    win_2_hit.y = 315
                    rejouer_img_hit.y = 574
                    quitter_img_hit.y = 574

                elif pv.mort2():
                    win_1_hit.y = 315
                    rejouer_img_hit.y = 574
                    quitter_img_hit.y = 574

            game.newpion()

    pygame.display.flip()

    if rejouer_btn.draw(screen):
        game.new_grille()
        game.newpion()
        rejouer_img_hit.y = 720
        quitter_img_hit.y = 720
        win_2_hit.y = 720
        win_1_hit.y = 720
        pv.num1 = 0
        pv.num2 = 0
        pv1 = pygame.image.load(f'assets/SPRITE_/barre_vie/pv1.png')
        pv2 = pygame.image.load(f'assets/SPRITE_/barre_vie/pv1.png')
    elif quitter_btn.draw(screen):
        running = False
        pygame.quit()
   # def des touches du jeu
    game.pressed[pygame.K_RIGHT] = False
    game.pressed[pygame.K_LEFT] = False
    game.pressed[pygame.K_RETURN] = False
    game.pressed[pygame.K_a] = False

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()

        if i.type == pygame.KEYUP:

            game.pressed[i.key] = True
