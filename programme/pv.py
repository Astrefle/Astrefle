from bouton import*
import pygame
from pygame.version import PygameVersion
pygame.init()


class PV:

    def __init__(self):
        self.l_pv=['pv1.png','pv2.png','pv3.png','pv4.png',]
        self.num1=0
        self.num2=0
        self.pv1=self.l_pv[self.num1]
        self.pv2=self.l_pv[self.num2]


    def degat1(self):
        self.num1+=1
        self.pv1=self.l_pv[self.num1]
    
    def degat2(self):
        self.num2+=1
        self.pv2=self.l_pv[self.num2]
       
    def mort1(self):
        if self.num1==4:
            return True
    
    def mort2(self):
        if self.num2==4:
            return True


        

    
    

