import pygame
from pygame.version import PygameVersion
pygame.init()
from choi import*
from game import*

class TITLE(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__
        self.title1 = pygame.image.load('assets/BG_/TITRE1.png')
        self.hit1= self.title1.get_rect()
        self.hit1.x=20
        self.hit1.y=50
        self.title2 = pygame.image.load('assets/BG_/TITRE2.png')
        self.hit2= self.title1.get_rect()
        self.hit2.x=500
        self.hit2.y=40
        self.title3 = pygame.image.load('assets/BG_/TITRE3.png')
        self.hit3= self.title1.get_rect()
        self.hit3.x=20
        self.hit3.y=150


pygame.display.set_caption("Brawl 4 Monsters")
screen=pygame.display.set_mode((600,700))

running=True

bg_=pygame.image.load('assets/BG_/WarmWarmheartedIrishwolfhound-max-1mb.gif')
Titre=TITLE()
Choix=Choix_perso()
game=Game()
while running:
#fond d'ecran
    screen.blit(bg_,(0,0))
#Titre du jeu
    screen.blit(Titre.title1,Titre.hit1)
    screen.blit(Titre.title2,Titre.hit2)
    screen.blit(Titre.title3,Titre.hit3)
    screen.blit(Choix.perso_choisis,Choix.perso_choisis_hit)

    if game.pressed.get(pygame.K_RIGHT):
        Choix.Right()
    elif game.pressed.get(pygame.K_LEFT):
        Choix.Left()

    pygame.display.flip()


    game.pressed[pygame.K_RIGHT] = False
    game.pressed[pygame.K_LEFT] = False
    game.pressed[pygame.K_RETURN] = False
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running=False
            pygame.quit()

        if i.type == pygame.KEYUP:
            game.pressed[i.key] = True