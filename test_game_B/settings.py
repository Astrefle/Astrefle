import pygame
from lvl import *

pygame.init()
running = True
pygame.display.set_caption("Dodge_Game")
screen = pygame.display.set_mode((1920, 1080))
bg = pygame.image.load("bg.jpg")
pressed = {}
lvl_stage = 0
next_lvl = 0

