import pygame
pygame.init()

"""class Game:
    def __init__:
        self."""





class TITLE(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__
        self.title1 = pygame.image.load('assets/BG_/TITRE1.png')
        self.hit1= self.title1.get_rect()
        self.hit1.x=500
        self.hit1.y=50
        self.title2 = pygame.image.load('assets/BG_/TITRE2.png')
        self.hit2= self.title1.get_rect()
        self.hit2.x=980
        self.hit2.y=45
        self.title3 = pygame.image.load('assets/BG_/TITRE3.png')
        self.hit3= self.title1.get_rect()
        self.hit3.x=500
        self.hit3.y=150


'''class PION (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__
        self.pion = pygame.image.load('assets/SPRITE_/PION.gif')
        self.hit_pion= self.pion.get_rect()'''



pygame.display.set_caption("Brawl 4 Monsters")
screen=pygame.display.set_mode((1647,720))

running=True

bg_=pygame.image.load('assets/BG_/WarmWarmheartedIrishwolfhound-max-1mb.gif')

Titre= TITLE()






while running:
#fond d'ecran
    screen.blit(bg_,(0,0))

#Titre du jeu
    screen.blit(Titre.title1,Titre.hit1)
    screen.blit(Titre.title2,Titre.hit2)
    screen.blit(Titre.title3,Titre.hit3)




    pygame.display.flip()



    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running=False
            pygame.quit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                print('Ca marche')
            elif i.key == pygame.K_LEFT:
                print('Ca marche')