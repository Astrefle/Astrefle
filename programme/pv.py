from bouton import*
import pygame
from pygame.version import PygameVersion
pygame.init()


class PV:

    def __init__(self):
        self.l_pv=['pv1.png','pv2.png','pv3.png','pv4.png',]
        self.num=0
        self.pv=self.l_pv[self.num]
        self.j1=joueur1_hit

    def degat(self):
        self.num+=1
        self.pv=self.l_pv[self.num]
       
        

        

    
    

