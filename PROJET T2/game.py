import pygame
pygame.init()
from Pion import*
from Grille import*


class Game:
    def __init__(self):
        self.grille=Grille()
    
        self.l_pion=[]
        
        self.pion= PION(self.grille,self.l_pion)
        
        self.pressed ={}

        print(self.pressed)
        
        self.l_pion.append(self.pion)
    
    def newpion(self):
       
        self.pion=PION(self.grille,self.l_pion)
        
        self.l_pion.append(self.pion)
        
        if (len(self.l_pion)%2)==0:
            self.pion.p1=pygame.image.load('assets/SPRITE_/pion/PION2.png')  
        
        else:
            self.pion.p1=pygame.image.load('assets/SPRITE_/pion/PION.png')
        
        return self.pion
    
    
           
