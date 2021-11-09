import pygame
from pygame.version import PygameVersion
pygame.init()
import pygame
pygame.init()
from Pion import*
from game import*
from Titre import*
from choi import*
from bouton import*





pygame.display.set_caption("Brawl 4 Monsters")
screen=pygame.display.set_mode((1080,720))

game=Game()

running=True

bg_=pygame.image.load('assets/BG_/WarmWarmheartedIrishwolfhound-max-1mb.gif')

Titre= TITLE()
Choix=Choix_perso()





while running:
#fond d'ecran 
    screen.blit(bg_,(0,0))
#Titre du jeu
    screen.blit(Titre.title1,Titre.hit1)
    screen.blit(Titre.title2,Titre.hit2)
    screen.blit(Titre.title3,Titre.hit3)

#Test affichage perso
    screen.blit(Choix.perso_choisis,Choix.perso_choisis_hit)
    if game.pressed.get(pygame.K_RIGHT):
        Choix.Right()
    elif game.pressed.get(pygame.K_LEFT):
        Choix.Left()  
    
        
   
    for i in game.l_pion:
        screen.blit(i.p1,i.hit_p1)
            
    #Déplacement du pion   
    if game.pressed.get(pygame.K_RIGHT) and game.pion.hit_p1.x+game.pion.hit_p1.width<880:
        game.pion.Right()
    elif game.pressed.get(pygame.K_LEFT) and game.pion.hit_p1.x>200:
        game.pion.Left()
    elif game.pressed.get(pygame.K_RETURN) and game.pion.hit_p1.y <700:
        game.pion.tombe()
        game.newpion()
        
    pygame.display.flip()            



    
#Test affichage Pion
   
    
  
  
  
   #def des touches du jeu 
    game.pressed[pygame.K_RIGHT] = False
    game.pressed[pygame.K_LEFT] = False
    game.pressed[pygame.K_RETURN] = False
    
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running=False
            pygame.quit()
        
        if i.type == pygame.KEYUP:
            game.pressed[i.key] = True
            
