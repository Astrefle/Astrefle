import pygame
from pygame.version import PygameVersion
pygame.init()


class Choix_perso:
    def __init__(self):
        self.l_perso={'1':"Boxer.png",'2':"Demon.png",'3':"ELectro.png",'4':"Mage.png",'5':"Squellette.png"}
        self.num=1
        self.choix=self.l_perso[f'{self.num}']
        self.perso_choisis= pygame.image.load(f'assets/SPRITE_/persoj1/{self.choix}')
        self.perso_choisis_hit=self.perso_choisis.get_rect()
        self.l_pion_perso={'1':"PION1.png",'2':"PION2.png",'3':"PION3.png",'4':"PION4.png",'5':"PION5.png"}

    
    
    
    def Right(self):
        if not self.num>=5:
            self.num+=1
          
            self.choix=self.l_perso[f'{self.num}']
            self.perso_choisis= pygame.image.load(f'assets/SPRITE_/persoj1/{self.choix}')
     
            
        else:
            print('')
    
        
    def Left(self):
        if not self.num<=1:
            self.num-=1
            
            self.choix=self.l_perso[f'{self.num}']
            self.perso_choisis= pygame.image.load(f'assets/SPRITE_/persoj1/{self.choix}')
          
        else:
            print('')


    def end(self):
        self.end=0
        return self.end
    
        
        
        