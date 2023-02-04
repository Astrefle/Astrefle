from ast import withitem
from msilib.schema import Class
import random
import re
from venv import create
import pygame
import programms.button
import programms.liste
import programms.Cara
import programms.interface


b = programms.button.Button


'''class Objectif():
    def __init__(self):
        self.objectif = None
        self.running = True
        self.liste = None
        self.c = programms.Cara.Cara('vide', 620, 30)
        self.result = ' '
        self.espace = 10
        
        

    def choice(self):
        self.liste = programms.liste.liste_all()
        self.objectif = self.liste
        return ((self.objectif))

    def épeler(self, mot):
        self.n_liste = []
        mot = str(mot)
        for lettre in mot:
            if lettre == '[' or lettre == ']' or lettre == "'" or lettre == '"' or lettre == '{' or lettre == '}':
                pass
            elif lettre == ' ' or lettre == ':':
                self.n_liste.append('vide')

            elif lettre == ',':
                self.n_liste.append('return')
            else:
                self.n_liste.append(lettre)
        return self.n_liste

    """def print(self):
        
        while self.running:
            for i in self.c.liste:
                self.fiche.blit(i.lettre, (i.lettre_rect.x, i.lettre_rect.y))"""

        


def execute():
    o = Objectif()
    o.choice()

    o.épeler(o.objectif)
    

    for i in o.n_liste:
        o.c.add()
        o.c.ret(i)
        o.c.mot(i)
    
    while run:
            for i in o.c.liste:
                programms.interface.screen.blit(i.lettre, (i.lettre_rect.x, i.lettre_rect.y))'''
    

    
